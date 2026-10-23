---
url: https://docs.cloud.google.com/looker/docs/admin-panel-general-settings/
title: Admin settings - General settings \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:23.274906+00:00
---

# Admin settings - General settings  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-general-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - General settings Stay organized with collections  Save and categorize content based on your preferences. 

The **Settings** page in the **General** section of the **Admin** panel lets Looker admins configure the instance-wide settings for Looker. Some settings are available only for Looker (original) instances or only for Looker (Google Cloud core) instances.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Settings

The following settings are available for Looker instances.

### License Key

**Note:** [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances don't include this setting.

The license key is unique to the Looker instance that you're using. It enables or disables certain Looker features based on your licensing agreement.

The license key is hidden by default. Select the eye icon visibility to display the license key.

If your Looker license is renewed or reactivated after having been revoked, the Looker UI might continue to display a **License has been revoked** banner. To manually refresh the license status and clear the banner, click the **Update** button next to the license key.

### Host URL

**Note:** [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances don't include this setting. For information about how to set up a custom domain in Looker (Google Cloud core), see the [Set up a custom domain for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain) documentation page.

The host URL is the base portion of your Looker instance's URL. It is used specifically when links to your instance are created in scheduled emails and in all absolute URLs that Looker generates.

Your instance can use only one `cloud.looker.com` domain at a time. To make your Looker instance accessible from multiple URLs, you must configure a custom domain. For information about how to set up a custom domain for a Looker-hosted instance, see [Configure custom domains for Looker-hosted instances](https://docs.cloud.google.com/looker/docs/looker-hosted-custom-domain).

Make sure the **Host URL** setting uses `http://` or `https://` appropriately, based on your instance's server configuration.

Changing the host URL may affect the functionality of some Looker features. See the [How to change the URL of a Looker instance](https://docs.cloud.google.com/looker/docs/best-practices/how-to-change-the-looker-instance-url) Best Practices page for more information about changing instance URLs.

### Technical Contacts

**Note:** [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances don't include this setting. You can add technical contacts for Looker (Google Cloud core) [through the Google Cloud console](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts). Set the [notification category](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories) to **Technical**.

Email addresses that are added to this box will receive notifications of security updates, major bug fixes, and new Looker releases. The email address must belong to a valid Looker user. If you add an email that doesn't belong to a valid Looker user — for example, an email address for a distribution list — the email address will appear in the **Technical Contact** field, but Looker won't be able to deliver notifications to this address.

Looker Support requires permission from a technical contact to do any of the following:

  * Cause downtime for the instance, which could be due to a non-scheduled version update, performance changes to your Looker server, or other reasons
  * Change something about your Looker license, possibly to enable new features for you.

**Note:** Infrastructure-related maintenance notifications, which may cause services to be temporarily unavailable, are sent using Google Cloud's Essential Contacts system instead of using the Looker Technical Contact list. The **Google Cloud Project Number** must be correctly configured for these infrastructure notifications to be properly routed to the project's Essential Contacts.

### Application Time Zone

When displaying data in an Explore, a Look, or a dashboard, Looker can convert time data from the connection's [**Database Time Zone**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#database_time_zone) to the appropriate time zone for that user.

If the **User Specific Time Zones** option is enabled, then an [admin can set the user's default time zone](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#timezone) or [users can set their own default time zone](https://docs.cloud.google.com/looker/docs/user-account#profile_section). If the admin or user has not set the user's default time zone, then the **Application Time Zone** is used for that user, and all time-based data queried by that user will be converted to the **Application Time Zone**.

The **Application Time Zone** setting is also used as the default time zone for [content deliveries](https://docs.cloud.google.com/looker/docs/scheduling). The time zone used for schedules does not affect time data returned by a query; it affects only the time a data delivery is sent.

See the [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) documentation page for more information.

## Feature Configuration

The following feature configuration settings are available for Looker instances.

### Closed System

**Note:** This option must be enabled by Looker (original); contact [Looker Support](http://console.cloud.google.com/support/cases) to get started. This option is already available by default for [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances.

The **Closed System** setting is used in conjunction with [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) to prevent users in one group from knowing about the users in another group. This is often useful for multi-tenant installations.

The locations in Looker where users might see other users include the following:

  * The [Users page](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) in the **Admin** section of Looker
  * [Users' folders](https://docs.cloud.google.com/looker/docs/viewing-looks) in the **Folders** section of the Looker main menu, if they have been [granted at least **View** access](https://docs.cloud.google.com/looker/docs/organizing-spaces#space_access_levels) to another user's personal folder
  * The [Manage Access pop-up](https://docs.cloud.google.com/looker/docs/organizing-spaces), which is a part of folder management



When the **Closed System** setting is enabled, a non-admin user without the [`see_users`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see-users) permission can see only the other users with whom they share a group and only those groups of which they are a member.

Admins and any users who have been granted the `see_users` permission can see all users and groups on the instance.

**Caution:** An admin can override the **Closed System** setting by editing folder visibility to allow a user to see the personal folder of another user with whom they don't share a group.

### Login Consent Configuration

**Note:** This setting is available only for [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances.

When enabled, **Login Consent Configuration** causes a consent screen to be displayed to all users who attempt to sign in to the Looker instance. The consent screen will display the message that was entered in the **Message Configuration** field, and will require users to click the **I Agree** button on the consent screen before they can sign in to the instance. Once you have enabled **Login Consent Configuration** , the **Message Configuration** field becomes visible.

### Message Configuration

**Note:** This setting is available only for [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances.

If the **Login Consent Configuration** option is enabled, in the **Message Configuration** field, enter the message that will be displayed to all users who attempt to sign in to the Looker instance. This field becomes visible only after **Login Consent Configuration** is enabled.

### Default Private Personal Folders

**Note:** The **Default Private Personal Folders** option is not available for Looker instances with **Closed System** enabled.

When **Default Private Personal Folders** is enabled, a user's personal folder is by default visible only to that user and to Looker admins. By default, other users won't see the folder in the [People folder](https://docs.cloud.google.com/looker/docs/finding-content#people_folder), and the content in the folder won't be visible on [boards](https://docs.cloud.google.com/looker/docs/finding-content#navigating_to_content_on_boards) or in [content searches](https://docs.cloud.google.com/looker/docs/finding-content#searching_for_saved_content).

If you do want to provide access to a personal folder, you can add access to other users or to user groups through the [**Manage Access**](https://docs.cloud.google.com/looker/docs/organizing-spaces#manage) option from the personal folder's gear menu.

If you disable the **Default Private Personal Folders** option, a user's personal folder can be viewed by any Looker user in the **All Users** user group.

### New Account Notification

The **New Account Notification** setting can be enabled or disabled. When it is enabled, any Looker admin user will be emailed when a new Looker account is created. ([Signed embed](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding) users are an exception; emails are not generated when a signed embed user is created.) The email will contain the new user's email address.

### In-App Guides

In-app guides let Looker communicate with users in the application through tutorials, banners, alerts, and surveys. These communications are used to help users get more out of the platform, alert them to new features, get user feedback on the platform, and invite users to trainings and events where they can learn how to better use Looker.

Administrators can choose to disable guides for their instance, which will disable the guides for all users on that instance. There is no way to selectively turn off in-app guides for certain users. Looker won't show in-app guides to [embedded users](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding) or non-admin users on [private label](https://docs.cloud.google.com/looker/docs/privatelabel) instances.

Guides are designed and deployed by Looker's Customer Experience team and will change over time. Looker uses third-party software (Pendo) JavaScript to serve the guides. Looker vets the individual guides and adds them to the allowlist. When fetching a guide from Pendo, Looker uses SHA-256 integrity hashes to validate that the guide is unchanged. If there are any changes to the guide after Looker's review, Looker prevents use of the changed guide. If a user's browser cannot reach the Pendo server, then the guide isn't displayed.

### Onboarding

When enabled, Looker admins and developers who log in to a new Looker instance will see the Looker onboarding walkthrough, which guides users through the four major steps to make use of a Looker instance:

  1. Adding a connection
  2. Creating a project
  3. Editing project files as needed
  4. Exploring data



Once any combination of admins or developers completes the full guide, it stops being displayed.

The **In-App Guides** setting must be enabled for the **Onboarding** option to be available.

### Cookie Notification Banner

When enabled, this setting will show a cookie notification banner to all users on your instance. This setting is disabled by default.

We recommend that you enable this setting if your Looker instance must comply with the European Union's data protection regulations.

### Curated Search

**Note:** **Curated Search** does not apply to closed systems but is otherwise enabled by default.

When **Curated Search** is enabled, a user can [search](https://docs.cloud.google.com/looker/docs/finding-content#curated_search) for content across shared folders, their personal folder, and boards. Content that is saved in other users' personal folders will be included in the results only if such content is also pinned to a board. The search results will exclude content that exists only in the personal folders of other users. A user has the option to exclude content in personal folders by selecting the switch next to the **Curated Search** feature name in the search dialog modal.

### Limit Automatically refresh dashboard option

When this setting is enabled, only Looker admins will be able to enable the [Automatically refresh dashboard](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#autorefresh) option on user-defined dashboards. This prevents non-admin users from automatically refreshing data on dashboards and dashboard tiles. Automatically refreshing dashboard data can place a significant strain on some database systems.

### Full Screen Visualizations

When enabled, this feature enables full-screen and expanded views for visualizations within dashboard tiles. See the [Viewing dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards#view_options) documentation page for more information on view options.

Full-screen and expanded functionality can be turned off on a dashboard in the dashboard's [**Settings** menu](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#allow_full-screen_mode_for_visualizations).

### Visual Drilling

The **Visual Drilling** feature is not supported by [dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards). For dashboards, visual drilling is possible through the use of the [`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link#using_link_to_customize_drill_visualizations) parameter.

When **Visual Drilling** is turned off, the drill overlay always displays the data table.

When **Visual Drilling** is enabled, the drill overlays for Looks and Explores consider the underlying data to select the best visualization type, which can be a table visualization or some other visualization type. Or, with **Visual Drilling** enabled, you can use the `link` parameter to customize a drill visualization, as shown on the [`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link#using_link_to_customize_drill_visualizations) parameter documentation page and on the [More powerful data drilling](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-more-powerful-data-drilling) Best Practices page. When the visualization from a drill is not a table, [buttons](https://docs.cloud.google.com/looker/docs/viewing-looks#vis_drilling) let the user switch between the default visualization type and a data table.

For more information about visualization types, see the [Visualization types](https://docs.cloud.google.com/looker/docs/visualization-types) documentation page.

### Smart Single Value Text Size

Enabling the **Smart Single Value Text Size** feature automatically resizes the fonts on single value visualizations displayed within dashboard tiles. Fonts are resized to display at least 8-10 value characters within a tile; if the characters in the visualization overflow horizontally or vertically at a given size, the font size will step down. The minimum font size allowed is 14 pixels. Once the minimum font size is reached, any overflowing characters will be truncated with an ellipsis (...). The maximum font size allowed is 104 pixels.

When you're using this feature, single value tiles on dashboards may look less consistent, but more characters will fit on smaller tiles.

When this feature is enabled, the **Auto Resize Value** option in the [Single value chart Style menu](https://docs.cloud.google.com/looker/docs/single-value-options#style_menu_options) has no effect.

### Include custom filter values for boards

Enabling the **Include custom filter values for boards** feature enables the [**Include custom filter values** setting](https://docs.cloud.google.com/looker/docs/presenting-content#adding_dashboards_to_boards_with_custom_filter_values_applied) instance-wide by default when users add dashboards to boards.

### Google Cloud Project Number

A Google Cloud project number is required to enable in-app support. This value can be obtained from the Cloud Overview page in the [console_name_short](http://console.cloud.google.com).

This change can take up to two hours to take effect. To implement the change immediately, click the **Update** button next to the [License Key](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#license_key) setting after entering your Google Cloud project number.

If you don't have a Google Cloud project for Looker yet, you can create one by following our [Create a Google Cloud project guide](https://developers.google.com/workspace/guides/create-project) or our more in-depth documentation on [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

### Use Gravatar

**Note:** [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances don't include this setting.

When enabled, this setting displays the **Profile Picture** option on the [user menu](https://docs.cloud.google.com/looker/docs/user-menu), letting users select or create an avatar for their account using the [Gravatar](http://en.gravatar.com/) app.

### User Specific Time Zones

When [adding a connection](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#creating_a_new_database_connection), you specify what time zone your database stores time information as the [**Database Time Zone**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#database_time_zone).

When **User Specific Time Zones** is enabled, each user is assigned a time zone, and Looker converts time-based data from the **Database Time Zone** to a user's time zone when the user views query results or interprets filters.

When **User Specific Time Zones** is disabled, Looker converts time-based data for all users to the [**Query Time Zone**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#query_time_zone) value.

See the [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) documentation page for more information.

### Default Visualization Colors

Each Looker instance must have a default color collection. The **Default Visualization Colors** setting lets you define a default color collection for visualizations, and also lets you create new color collections for use in your instances. You can select an existing color collection or create a custom color collection. The default color collection for the **Default Visualization Colors** setting is Shoreline.

If the [**Modern User Interface** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#modern_user_interface) is enabled, you will see the [Modern color collection](https://docs.cloud.google.com/looker/docs/color-collections#the_modern_color_collection) as an option for the **Default Visualization Colors** setting. The **Default Visualization Colors** setting interacts with the [**Visualization Theme** setting](https://docs.cloud.google.com/looker/docs/modern-ui#modern_visualizations) in the following ways:

**Default Visualization Colors** setting | Visualization theme for new chart | Color collection used by chart  
---|---|---  
Shoreline (default) | Modern | Modern  
Shoreline (default) | Classic | Shoreline  
Any color collection other than Shoreline | Modern or Classic | The selected color collection  
  
### Selecting an existing color collection

To set an existing color collection as your default, choose the color collection from the drop-down menu and click **Update**.

**Note:** Setting a new default color collection will update all visualizations on Looks and dashboards that use the default color collection. Visualizations that are saved with a different color collection, or a custom palette, won't be affected.

You can see the first categorical, sequential, and diverging palettes of each collection directly under the drop-down menu. These are the palettes that will be used as the visualization defaults. To view all the palettes in the color collection, visit the [Color collections](https://docs.cloud.google.com/looker/docs/color-collections#lookers_color_collection_palettes) documentation page.

#### Creating a custom color collection

To create a custom color collection, follow these steps:

  1. Select last **New color collection** option from the **Default Visualization Colors** collection drop-down menu.
  2. Give your new collection a unique name in the **Name** field.
  3. Click each color palette to open the **Colors in Palette** menu.
  4. Select individual colors in the **Colors in Palette** menu to edit one at a time, or select **Edit All** to edit all of the colors at once.
  5. Repeat steps 3 and 4 for each color palette.
  6. When you're finished editing your new color collection, click **Create**.



Color values can be formatted as hex strings, such as `#2ca6cd`, or as [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`. Or you can click the color wheel to open and select a shade from the color picker. If you choose to edit all colors, use a comma between each color name to separate them. To add or remove a color, click the **+** or **-** signs.

The new collection will automatically become the instance default, but you can choose a different default if you want.

Collection IDs and palette IDs for any new custom color collections are based on each collection's name. This allows LookML dashboards that use those collections to render consistently across instances if both instances have the same custom collections named identically.

#### Deleting a custom color collection

You can delete a custom color collection by selecting the collection from the drop-down menu and clicking the **Delete** button that appears. You cannot delete Looker's built-in color collections.

### Load Assets from CDN

This option is available only for customer-hosted instances. Because Looker-hosted instances always load assets from the CDN, you cannot disable this setting for these instances.

CDN stands for _content delivery network._ A CDN is a network of servers that stores content in multiple geographic locations to reduce page load time for users. Your data is never stored on these servers; only items that are specific to Looker (such as images) are stored on the CDN.

The **Load Assets from CDN** setting can be either enabled or disabled. When it is enabled, Looker pages should load faster.

### Persist Assets in Browser cache

When this setting is enabled, static assets such as JavaScript files and fonts are cached in each user's browser storage. This speeds up subsequent navigations, because the browser does not need to continue to reload these assets from the Looker server.

### Mobile Application Access

When this setting is enabled, users can log in to their Looker account on the instance using the [Looker mobile app](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app) and the [Looker (Legacy) app](https://docs.cloud.google.com/looker/docs/mobile-app-legacy). When this setting is disabled, any existing mobile sessions are terminated.

### Force mobile authentication

When this setting is enabled, users are required to sign in to the [Looker mobile app](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app) and the [Looker (Legacy) app](https://docs.cloud.google.com/looker/docs/mobile-app-legacy) every time they open the app on their mobile device.

Additionally, users will be logged out of the mobile app after 60 minutes of inactivity.

### Data history playback

When enabled, this feature allows users to explore data changes over time for visualizations within dashboards. See the [Viewing dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards#tile_three-dot_menu) documentation page for more information.

### Force BigQuery Readonly Scope usage

Enabling this setting signs out users that have OAuth credentials that allow read and write scope on any of BigQuery connections. When the users authenticate again, Looker will create read-only OAuth credentials for those users instead. See [Restricting OAuth scope to read-only for Google BigQuery connections](https://docs.cloud.google.com/looker/docs/best-practices/oauth-read-only) for more information.

### Reduce Filter Queries

This feature reduces the number of queries that are sent by filters. When **Reduce Filter Queries** is enabled, Looker moves any filter that requests suggestions into a dialog where the filter won't fetch suggestions until a user clicks on it in the dialog.

### Content Certification

This setting enables or disables [content certification](https://docs.cloud.google.com/looker/docs/content-certification).

### Certification Process URL

When a user who does not have the [`certify_content` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#certify_content) wants to request certification of their content, and they select a dashboard's or LookML dashboard's [three-dot dashboard menu](https://docs.cloud.google.com/looker/docs/viewing-dashboards#three-dot_dashboard_menu), a Look's [Explore actions gear menu](https://docs.cloud.google.com/looker/docs/viewing-looks#the_look_explore_actions_gear_menu), or an Explore or self-service Explore's [Explore actions gear menu](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_actions_gear_menu), they will see an option that says **Want to get this dashboard/look/Explore certified?** that includes a **Learn how** link.

By default, the **Learn how** link opens up the [Content certification](https://docs.cloud.google.com/looker/docs/content-certification) documentation page.

The **Certification Process URL** field lets admins enter a custom URL that the **Learn how** link will open. Organizations can create documents that describe their individual certification process, which users can connect to using this custom URL.

### Revoke certification on edit

By default, certification of content is revoked after any major edit. Major edits include changing the query or dashboard tile content, adding or removing a dashboard tile, or changing filter values.

Minor changes, which won't cause certification to be revoked, include changing a title or dashboard tile title, repositioning dashboard tiles, or changing a dashboard layout without changing the content of any of the dashboard tiles.

For a complete list of actions that will and won't cause certification to be revoked, see the [Content certification](https://docs.cloud.google.com/looker/docs/content-certification#revoke-certification) documentation page.

If the **Revoke certification on edit** option is disabled, certification won't be revoked after a major edit. In this case, the only way to revoke content certification is for a Looker admin or a user that has the [`certify_content` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#certify_content) to manually [revoke the content certification](https://docs.cloud.google.com/looker/docs/content-certification#revoke-certification).

### Auto-certify LookML

When this option is enabled, all LookML dashboards and LookML Explores will be automatically certified. This applies both to existing LookML dashboards and LookML Explores and any LookML dashboards or LookML Explores created in the future.

## Data Policy

The following data policy settings are available for Looker instances.

### Public URLs

The **Public URL** setting can be enabled or disabled. When this setting is enabled, Looker users with appropriate permissions can [generate public URLs](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls) to access Looker data.

**Note:** Although public URLs are not guessable, anyone who has one can access your data without security restraints. Use with caution.

### Email Domain Allowlist for Scheduled Content

**Note:** In [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances, you set the email domain allowlist for an instance [within the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-view-console#edit_instance_settings). The **Settings** page within a Looker (Google Cloud core) instance doesn't contain this setting.

This setting lets Looker admins define the email domains to which your users can [deliver](https://docs.cloud.google.com/looker/docs/scheduling) Looker content — Looks, dashboards, queries with visualizations — or [alert notifications](https://docs.cloud.google.com/looker/docs/alerts-overview) through email.

To limit content deliveries and alert notifications to email addresses with a specific domain, you can enter the domain in the format `domain.suffix`. For example, to limit email deliveries to just emails with `gmail.com` and `friendly_domain.org` domains, you can specify these domains in the **Email Domain Allowlist for Scheduled Content** field and then grant users the `schedule_look_emails` permission.

See more about how this setting and a user's permissions affect their ability to deliver Looker content and alert notifications in the Permissions overview section on this page.

#### `looker_internal_email_domain_allowlist` user attribute

In addition to the email domains that are included in the global **Email Domain Allowlist for Scheduled Content** field, you can also specify email domains on a per-group level using the `looker_internal_email_domain_allowlist` [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes). The user attribute accepts the same string format as the **Email Domain Allowlist for Scheduled Content** admin setting.

If a group is assigned multiple email domain sets, for example through membership in multiple groups, then members of that group will be able to send emails to all domains that are assigned to each of the user attribute values, as well as the domains that are listed in the **Email Domain Allowlist for Scheduled Content** admin setting. In other words, the set of email domains that a group can send emails to is the union of the set of email domains that are listed in the **Email Domain Allowlist for Scheduled Content** field and every set of email domains that are assigned to the group by the `looker_internal_email_domain_allowlist` user attribute.

#### Permissions overview

Embed and non-embed users must have at least the `schedule_look_emails` permission to be able to email any Looker content. To send [alert notifications](https://docs.cloud.google.com/looker/docs/alerts-overview), a user must also have `create_alerts` permissions.

Embed and non-embed users who have the `schedule_look_emails` permission may also be granted the `schedule_external_look_emails` permission (see more on [permissions and dependencies](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_and_dependencies) on the **Roles** documentation page).

For an overview of how user permissions affect the domains to which users can send Looker content deliveries or alert notifications, see the following table:

**User type** | **Permissions** | **Email Domain Allowlist for Scheduled Content contains the domain`friendly_domain.org`** | **Email Domain Allowlist for Scheduled Content contains no domains**  
---|---|---|---  
Non-embed | `[schedule_look_emails](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#schedule_look_emails)` only | Can email content deliveries to their own email address, to the email address of another Looker [user](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) on the same instance, or to an email address with the `friendly_domain.org` domain | Can email content deliveries to any email address  
`[schedule_look_emails](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#schedule_look_emails)` and `[create_alerts](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_alerts)` | Can email content deliveries and alert notifications to their own email address, to the email address of another Looker [user](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) on the same instance, or to an email address with the `friendly_domain.org` domain | Can email content deliveries and alert notifications to any email address  
`[schedule_external_look_emails](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#schedule_external_look_emails)` only | Can email content deliveries to any email address | Can email content deliveries to any email address  
`[schedule_external_look_emails](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#schedule_external_look_emails)` and `[create_alerts](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_alerts)` | Can email content deliveries and alert notifications to any email address | Can email content deliveries and alert notifications to any email address  
Signed embed | `[schedule_look_emails](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#schedule_look_emails)` only | Can email content deliveries to an email address with the `friendly_domain.org` domain | Cannot email any Looker content  
`[schedule_look_emails](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#schedule_look_emails)` and `[create_alerts](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_alerts)` | Can email content deliveries and alert notifications to an email address with the `friendly_domain.org` domain | Cannot email any Looker content or alert notifications  
`[schedule_external_look_emails](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#schedule_external_look_emails)` | Can email content deliveries to any email address | Can email content deliveries to any email address  
`[schedule_external_look_emails](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#schedule_external_look_emails)` and `[create_alerts](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_alerts)` | Can email content deliveries and alert notifications to any email address | Can email content deliveries and alert notifications to any email address  
  
Embedded Looker content is accessed through a dedicated embed user account, not by individual user accounts. When a person accesses Looker content through an embed, Looker isn't expected to know the individual user's email address.

One exception to the rules that are stipulated in the table is as follows: You can provide Looker with an embed user's email address by defining it in the `email` user attribute in the [signed embed URL](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#building_the_embed_url). For example:
    
    
    ...&user_attributes={"email":"joe@domain.com"}
    

If you define the `email` user attribute in the embed URL, Looker will allow an embed user who has only the `schedule_look_emails` permission to email Looker content to their own email address, even if their email domain isn't in the **Email Domain Allowlist for Scheduled Content** field, or if the **Email Domain Allowlist for Scheduled Content** field is blank.

### URL Allowlist for Data Actions

This setting lets you define URLs (such as `https://looker.com`) where your users can process [data actions](https://docs.cloud.google.com/looker/docs/reference/param-field-action).

For example, if you add the URL `https://looker.com` to the URL allowlist for data actions, data actions will be able to be processed only at `https://looker.com`. Attempts to process data actions at other URLs won't be allowed.

If this field is left blank, there are no URL restrictions for data actions. However, if you have included a [user attribute in a data action](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#data_actions), this field is required. In that case, you must provide valid URLs to process data actions.

### Block Inline Embedded Images in Query Results

By default, Looker does not display [Base64](https://en.wikipedia.org/wiki/Base64) encoded images in query results. Disable this setting to display Base64 encoded images in query results.

### Block Formulas and Macros in CSV and Excel Files

When this setting is enabled, Looker prepends a `'` character to all values that could be interpreted as formulas or macros in queries that are downloaded in CSV or Excel spreadsheet formats.

### Outgoing Webhook Token

If a user uses a webhook to deliver content — such as a [dashboard](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#webhook) or a [Look](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_webhooks) — the request will include a special Looker token that can be set here. Servers that receive webhooks can then verify that requests contain this value to verify the legitimacy of webhook requests. To reset the roken, click **Reset**.

### Automated Gemini in Looker enablement and user management

**Note:** This setting is not available for Looker (Google Cloud core) instances. Gemini in Looker isn't enabled automatically for Looker (Google Cloud core) instances. 

This setting is enabled by default for all Looker (original) instances except those that are hosted in the [EMEA region](https://docs.cloud.google.com/looker/docs/looker-original-locations) and those that are enrolled in Looker's [Extended Support Release (ESR) program](https://docs.cloud.google.com/looker/docs/standard-extended-support-release-program-overview). You can manage Gemini in Looker enablement manually from the [**Gemini in Looker**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) page in the **Platform** section of the **Admin** panel.

A new user group called [**Default Gemini Users**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#default-gemini-users) has been created automatically for all Looker (original) instances that use an [open system configuration](https://docs.cloud.google.com/looker/docs/access-levels#open_and_closed_systems_of_access_to_folders). Users in this group are assigned the [**Gemini** role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini), which grants them the ability to use [Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) features.

The status of the **Automated Gemini in Looker enablement and user management** setting affects the group as follows:

  * If you enable the setting: 
    * New users who are added to the instance are added to the group automatically.
  * If you disable the setting: 
    * New users who are added to the instance must be added to the group manually.
    * If you want to remove members from the **Default Gemini Users** group, you must remove them manually.



The status of the setting as of June 9, 2025, has the following effects:

  * If the setting was enabled prior to June 9, 2025, all existing users have been added to the group and all new users will be added to the group. Gemini in Looker has been enabled automatically.
  * If the setting was disabled as of June 9, 2025, all users must be added to the group manually. Gemini in Looker has not been enabled automatically.



Gemini in Looker can be enabled or disabled manually on the [Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) page in the **Platform** section of the **Admin** panel. Its status is not affected by the status of the **Automated Gemini in Looker enablement and user management** setting.

### Auto enablement of MFA

This setting is enabled by default.

When **Auto enablement of MFA** is enabled, your Looker instance will require [multi-factor authentication (MFA)](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-two-factor) whenever a user tries to [log in by using an email and a password](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-password).

**Note:** Starting in Looker 26.18, MFA is required for all instances, except for those instances where **Auto enablement of MFA** has previously been disabled.

### Default Export Format

The **Default Export Format** setting lets you choose the default file format that is used when users choose to [download data](https://docs.cloud.google.com/looker/docs/downloading). Users can still choose a different file format if they like. The following formats are available:

Format | File extension | Description  
---|---|---  
TXT | `.txt` | Generates a text file delimited by tabs.  
Excel Spreadsheet | `.xlsx` | Generates a spreadsheet file using the format for Microsoft Excel 2007 and later.  
CSV | `.csv` | Generates a text file delimited by commas.  
JSON | `.json` | Generates a JSON file with one record per line.  
HTML | `.html` | Generates basic HTML to display the data in a way that is similar to how the user sees it in their browser; however, the formatting is not exactly the same because Looker's CSS won't be included.  
Markdown | `.md` | Generates a standard Markdown file with a `|` delimited table.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
