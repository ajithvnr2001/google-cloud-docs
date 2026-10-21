---
url: https://docs.cloud.google.com/looker/docs/private-embedding/
title: Private embedding \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:51.863729+00:00
---

# Private embedding  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/private-embedding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Private embedding Stay organized with collections  Save and categorize content based on your preferences. 

In addition to [public embedding](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls#embed), you can also embed Looks, Explores, and dashboards privately. With private embedding, you can require a user to authenticate using a Looker login, [Google OAuth](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-google), or [OpenID Connect](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect). If a user is not authenticated, you have the option to show an error message or display a login screen.

Users who are logged in and accessing privately embedded content are subject to the settings in the [**Sessions**](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-sessions) **Admin** panel, which determine how long they can stay logged in, if they can log in from multiple browsers, and if they will be logged out after a period of inactivity.

If you require a more advanced or customizable embedded solution, check out our [Signed embedding](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding) documentation page.

**Note:** Embedded content always reflects the production version of the content. Any changes made while in [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode) that affect content and that have not been deployed to production won't appear in an embed.

## Generating an embed URL

To generate and copy a [private embed URL](https://docs.cloud.google.com/looker/docs/private-embedding) for a dashboard, a Look, or an Explore visualization, select **Get embed URL** from a dashboard [three-dot menu](https://docs.cloud.google.com/looker/docs/viewing-dashboards#three-dot_dashboard_menu), or from the Explore action gear menu on an [Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_actions_gear_menu) or a [Look](https://docs.cloud.google.com/looker/docs/viewing-looks#the_look_explore_actions_gear_menu).

![](https://docs.cloud.google.com/static/looker/docs/images/get-embed-url-dash-2420.png)

The **Private Embed** screen includes the following elements:

  1. The **Content URL** field shows the full private embed URL.
  2. The **Apply theme to dashboard URL** field lets you select a theme to be added to the embed URL if you are generating a dashboard or an Explore embed URL and your instance has [custom themes](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) enabled. The theme will be applied when the embedded dashboard or Explore is viewed.
  3. The **Include current params in URL** switch lets you choose whether to apply current parameters, such as filter values, to the embed URL. If enabled, those parameters will be applied when the embedded content is viewed.
  4. Select the **Copy Link** button to copy the full embed URL to your clipboard.



Once you've generated and copied the embed URL, you can paste the URL into a new browser window or tab to preview the embedded content. You can also use this URL to embed the content in an iframe.

## Previewing the embedded content

Paste your embed URL in your browser to preview your embed content's behavior and appearance.

## Viewing the embedded content in an iframe

Place the embed URL into an iframe. For example:
    
    
      <iframe
          src="https://instance_name.cloud.looker.com/embed/dashboards/1"
          width="1000"
          height="2000"
          frameborder="0">
      </iframe>
    

And then embed the iframe as desired.

### Changing the embedded appearance of a dashboard

Viewing a dashboard with `/embed` in the URL shows you how the dashboard will appear when it's embedded.

By default, an embedded dashboard is displayed using the [default theme](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores#default_theme) for your Looker instance. You can change the appearance of your embedded dashboard in several ways, depending on the type of dashboard you are using:

  * For any type of dashboard, you can specify a different theme name [in the embed URL](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores#specify_theme) to change the theme used to display the dashboard.
  * For any type of dashboard, you can use the [`_theme` URL argument](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores#using_the__theme_url_argument_to_apply_individual_dashboard_theme_elements) to change individual dashboard theme elements.
  * For a [LookML dashboard](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards), you can also modify the embedded appearance of a dashboard through the [`embed_style`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#embed_style) parameter.



Using the `theme` URL argument, the **Edit Embed Settings** option, or the `embed_style` parameter makes changes only to the dashboard the argument, option, or parameter is applied to. If you want to customize the appearance of multiple embedded dashboards, use a [theme](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) instead.

Some display settings override others. For more information, see the [Creating and applying themes for embedded dashboards and Explores](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores#themes_precedence) documentation page.

## Enable login screen for private embeds

You can add the parameter `allow_login_screen=true` to your embed URL if you want to display a login screen to users who haven't logged in already. For example:
    
    
    <iframe src="https://instance_name.cloud.looker.com/embed/looks/4?allow_login_screen=true"></iframe>
                                                                ^^^^^^^^^^^^^^^^^^^^^^^
    

If you do not add this parameter, a 401 error will be displayed to users who are not already logged in.

**Note:** Using [same-origin protections for your Looker login pages](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#same-origin_protections_for_looker_login_pages) might prevent you from enabling a login screen for private embeds.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
