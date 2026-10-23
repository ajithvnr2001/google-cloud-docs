---
url: https://docs.cloud.google.com/looker/docs/mobile-app-drilling/
title: Drilling in the mobile application \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:00.466080+00:00
---

# Drilling in the mobile application  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/mobile-app-drilling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Drilling in the mobile application Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The [Looker Studio mobile application](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app) does not support drilling on Looker visualizations.

If mobile application access is [enabled](https://docs.cloud.google.com/looker/docs/mobile-app-enablement) for your instance and you have [installed](https://docs.cloud.google.com/looker/docs/mobile-app-installation) the app on your mobile device, you can [sign in to your Looker account](https://docs.cloud.google.com/looker/docs/mobile-app-sign-in) and interact with your data in the app. The Looker mobile app lets you drill into data to gain deeper insights.

## Interacting with and drilling into data

In the Looker web application, clicking on any data point in a visualization displays a tooltip or opens a menu with actions like drilling down, taking actions, or opening links. In the Looker mobile application, you can perform similar interactions by tapping on data points:

  1. [Navigate](https://docs.cloud.google.com/looker/docs/mobile-app-navigating-to-content) to a dashboard or Look.
  2. Tap on any data point that you want to interact with.
  3. Tapping the data point opens a bottom sheet. Depending on how the visualization is configured by your LookML developer, you can: 
     * **Drill into the data** : Tap a dimension name to drill into the data using that dimension.
     * **Take configured actions** : Tap a data action to perform tasks like sending an email or setting field values.
     * **Open links** : Tap any configured links to navigate to other Looks, dashboards, or external websites.



![](https://docs.cloud.google.com/static/looker/docs/images/mobile-drill-2612.png)

> Drilling is not supported on histogram or donut type visualizations.

## Configuring links in visualizations for the mobile application

This section describes how to configure links in your Explore so they work properly in the Looker mobile application.

There are two ways to add links inside your dashboard tiles:

### 1\. Embed inside a LookML link parameter (Recommended)

In development mode, navigate to the LookML file describing your Explore. Choose the dimension or measure you want to add the link to. Add a `link` parameter and specify the required URL:
    
    
    link: {
      label: "View Dashboard"
      url: "https://example.looker.com/dashboards/10"
    }
    

### 2\. Add an href tag in HTML

In development mode, navigate to the LookML file describing your Explore. Choose the dimension or measure you want to add the link to. Add an `html` parameter with an `href` attribute pointing to the link:

Example:
    
    
    html: <a target="_self" href='dashboards-next/10'>{{rendered_value}}</a>;;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
