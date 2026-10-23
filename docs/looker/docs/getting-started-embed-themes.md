---
url: https://docs.cloud.google.com/looker/docs/getting-started-embed-themes/
title: Getting started with embedding \u2014 applying custom themes \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:33.745421+00:00
---

# Getting started with embedding — applying custom themes  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/getting-started-embed-themes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Getting started with embedding — applying custom themes Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page describes how to use custom themes with embedded dashboards, Looks, and Explores. For information about using custom themes with Looker internal dashboards, see the [Themes for internal dashboards](https://docs.cloud.google.com/looker/docs/themes-for-internal-dashboards) documentation page.

You can use [custom themes](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores#creating_a_custom_theme) to customize the appearance of your embedded Looker dashboards, Looks, and Explores. Use custom themes to customize font family, text color, background color, button color, tile color, and other visual elements.

**Note:** Custom themes are not supported on embedded [merged queries](https://docs.cloud.google.com/looker/docs/merged-results) or embedded dashboard tiles that are based on a merged query.

For example, you can select a **dark** theme to change the appearance of your embedded dashboard.

![](https://docs.cloud.google.com/static/looker/docs/images/admin-themes-example-720-v2.png)

## Setting a default theme for embedded dashboards, Looks, and Explores

To specify the default theme for the embedded dashboards, Looks, and Explores on your instance, navigate to the **Themes** page in the **Platform** section of the **Admin** panel, select the **Embed** tab, click a theme's three-dot menu, and select **Set as Default**.

The default theme is used for embedded dashboards, Looks, and Explores on your Looker instance, unless you specify different settings for an individual dashboard, Look, or Explore.

## Applying a theme to specific embedded dashboards and Explores

If you want an embedded dashboard, Look, or Explore to use a theme other than the default theme, you can specify a different theme in the URL of the embedded dashboard, Look, or Explore. To do this, add the parameter `theme=` with the name of the theme to the end of the embed URL. For example, if you have a theme called "Red" that you want to apply to a dashboard, add `theme=Red` at the end of your embed dashboard URL:
    
    
    https://example.looker.com/embed/dashboards/246?theme=Red
    

For an Explore, add `theme=Red` at the end of your embed Explore URL:
    
    
    https://example.looker.com/embed/explore/model_name/explore_name?theme=Red
    

The theme element in the URL is not case-sensitive, so you can use either `theme=Red` or `theme=red`.

## For more information

  * For information about creating a custom theme for embedded dashboards, Looks, and Explores, see the [Themes for embedded dashboards, Looks, and Explores](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) documentation page.
  * For information about applying custom elements of a theme, see the [Using the _theme URL argument to apply individual dashboard theme elements](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores#using_the_theme_url_argument_to_apply_individual_dashboard_theme_elements) section of the **Themes for embedded dashboards, Looks, and Explores** documentation page.
  * For information about using the API to apply and manage custom themes for embedded dashboards, Looks, and Explores, see the [Theme method documentation](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
