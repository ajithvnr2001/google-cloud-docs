---
url: https://docs.cloud.google.com/looker/docs/privatelabel/
title: Admin settings - Private Label \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:08.753881+00:00
---

# Admin settings - Private Label  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/privatelabel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Private Label Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are using a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance, you will see this page only if you are using the [**Enterprise** edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#enterprise_edition) or the [**Embed** edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#embed_edition) of Looker (Google Cloud core).

You can customize Looker to remove references to Looker and blend the look and feel of Looker with your branding.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

On the **Private Label** admin page, you can configure the following options:

  * Documentation Links
  * Email Subscription Options
  * Help Menu
  * Custom Favicon
  * Custom Logo
  * Custom Document Title
  * Looker Mentions in Scheduled Emails
  * Custom Welcome Email Advanced Settings
  * Looker Mentions in Account Setup
  * Looker Logo in Alerts
  * Looker Links in Alerts
  * Looker Mentions in Folders Pages



Depending on your pricing plan, you can also customize the following options:

  * Download PDFs Without Logo
  * Embed Without Logo



## Enabling private label

Google Cloud must enable the private label option for your instance. [Contact a Google Cloud sales specialist](https://cloud.google.com/contact) for pricing and additional information.

## Private Label Admin page

In the Looker **Admin** panel, the **Private Label** page lets you load custom logos and customize how certain links to Looker are shown or hidden.

### Documentation Links

**Documentation Links** lets you show or hide the following links to Looker's documentation:

  * The **Docs** and **User Guide** options in the **Help** menu
  * The link in the **Custom Filters** panel
  * The question mark icon in the **matches (advanced)** option in the **Filters** panel
  * The question mark icon next to the [custom format field](https://docs.cloud.google.com/looker/docs/custom-formatting#using_custom_formatting_in_visualizations) in the **Series** tab of a [table visualization](https://docs.cloud.google.com/looker/docs/table-options#series_menu_options)
  * The documentation links in embedded dashboards and Conversational Analytics dashboard data agents



### Email Subscription Options

By default, there is a link on the Account page where a user can manage their [email subscriptions](https://docs.cloud.google.com/looker/docs/user-account#changing_your_email_subscription_settings). Your selection in **Email Subscription Options** determines whether or not that link is shown on the Account page.

### Help Menu

The **Help Menu** setting lets you show or hide the **Help** menu on the main menu bar.

### Custom Favicon

Turn on the **Custom Favicon** switch to upload a custom favicon. Looker displays the favicon in browser tabs and windows.

After you turn on the switch, Looker displays buttons to let you choose your favicon file and upload it. The favicon must be in ICO, PNG, or GIF file format, and must be one of the following sizes:

  * 16 x 16 pixels
  * 32 x 32 pixels
  * 48 x 48 pixels
  * 64 x 64 pixels



### Custom Logo

Turn on this switch to upload a custom logo.

Looker displays the following versions of the logo:

  * The first is small, rendered at 75 by 32 pixels, in the menu bar.
  * The second is large, rendered at 210 by 90 pixels, and appears on various pages in the product, including the following: 
    * User login
    * Password reset
    * User account setup
    * Email unsubscribe
    * Download a dashboard as a PDF



After you turn on the switch, Looker displays buttons to let you choose and upload your file icon. The logo must be in ICO, PNG, or GIF file format, and 500 KB or smaller.

### Custom Document Title

Enable this option to enter a custom document title. Looker displays the document title in the browser tabs and windows.

The document title usually shows a user's location within the Looker application, but Looker will display the custom document title when there is not an available specific document title.

### Looker Mentions in Scheduled Emails

By default, deliveries of [Looks](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#include_links), [dashboards](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#include_links), and LookML dashboards to email include a link to the **View full report** or **View full dashboard** option.

This link lets the email recipients connect to your Looker instance and further explore the data delivered in the email. Disabling the **Looker Mentions in Scheduled Emails** option replaces this text with **View full dashboard**.

To remove the link altogether, see the [**Emailed Data Policy** options](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-scheduled-emails#default_emailed_data_policy_options) on the **Scheduled Emails** page in the **Admin** panel.

### Custom Welcome Email Advanced Settings

If you have enabled [custom welcome emails](https://docs.cloud.google.com/looker/docs/admin-panel-users-custom-welcome-email), you can edit the body text of the emails that new Looker [users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) will receive when they are added to your instance. By default, Looker welcome emails include the subject line "Welcome to Looker" and header text that reads "You've been invited to join Looker!"

If you enable the **Custom Welcome Email Advanced Settings** option, you can also edit the subject line and header text in welcome emails. The header text and body text support HTML for adding formatting and links.

In addition, when you enable this option, the **Activate Your Account** button that is included in welcome emails is colored gray instead of purple.

### Looker Mentions in Account Setup

By default, new users who activate their Looker account with email and password authentication will see references to Looker in the welcome message on the account setup page.

They will also see "Welcome to Looker" in the browser tab.

To remove the reference to Looker in the welcome message and browser tab, turn on the **Looker Mentions in Account Setup** option. When this option is enabled, new users will only see "Welcome" on the page and on the browser tab.

If **Custom Logo** is also enabled, the Looker logo will be replaced with the specified logo image file. With both features enabled, a new user will see the following on the account setup page:

If **Custom Favicon** is also enabled, the Looker logo will be replaced with the specified icon image file on the account setup page browser tab.

### Looker Logo in Alerts

By default, [alert notification emails](https://docs.cloud.google.com/looker/docs/alerts-overview#alert_notifications_to_email) include the Looker logo.

To remove the Looker logo from alert notification emails, turn on **Looker Logo in Alerts**. Recipients will then see whitespace instead of the Looker logo.

Use **Looker Logo in Alerts** together with **Looker Links in Alerts** to further customize the appearance of alert notification emails.

### Looker Links in Alerts

By default, [alert notification emails](https://docs.cloud.google.com/looker/docs/alerts-overview#alert_notifications_to_email) include the following links:

  * A purple **Go to Content** button that links back to the Looker content on which the alert is set
  * An **Unfollow this alert** link that removes the recipient from the alert subscription
  * An **Edit this alert** link that links back to the Looker content on which the alert is set



The **Looker Links in Alerts** setting lets you remove the links from alert notification emails. To remove links back to Looker in alert notification emails, turn on **Looker Links in Alerts**. The purple **Go to Content** button will no longer appear, and the bottom two links will be replaced with instructions for navigating to the content in Looker to modify or disable the alert.

When **Looker Links in Alerts** is enabled along with **Looker Logo in Alerts**, recipients will only see the alert information and instructions to navigate to the content in Looker to modify or disable the alert.

### Looker Mentions in Folders Pages

By default, a user sees the message **Welcome to Looker!** in the folder when there is no content saved in their personal folder.

To remove the reference to Looker, turn on **Looker Mentions in Folders Pages**. When this is enabled, users will only see **Welcome!** in their empty personal folder.

## Additional optional private label features

There are two additional private label features that allow you to further customize PDF downloads and embedded content. Looker must enable these features for your instance. [Contact a Google Cloud sales specialist](https://cloud.google.com/contact) for pricing and additional information.

### Download PDFs Without Logo

By default, generated PDFs include a footnote that reads **Generated by Looker on`<TIMESTAMP>`**.

When **Download PDFs Without Logo** is enabled for your instance, the footnote instead reads **Generated on`<TIMESTAMP>`**.

### Embed Without Logo

By default, content that's embedded in an iFrame includes a footer that reads **Powered by Looker**.

When **Embed without Logo** is enabled for your instance, the footer is removed.

For more embedded content customization options, see the [**Remove Look Navigation**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#remove_look_navigation) feature on the [**Embed** page](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed) in the **Admin** panel.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
