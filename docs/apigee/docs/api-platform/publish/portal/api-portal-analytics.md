---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-analytics/
title: Configuring analytics tracking \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:55.519492+00:00
---

# Configuring analytics tracking  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configuring analytics tracking Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Configure Google analytics or your own custom analytics tracking, as described in the following sections.

## Configuring Google Analytics

Before you can configure Google Analytics, you'll need a Google Analytics account and access to the tracking code that will be added to your portal pages and used to track activity on your site. For more information, see [ Google Analytics help](https://support.google.com/analytics).

To configure Google Analytics:

  1. In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click your portal.

  3. Click **Settings** in the navigation menu.

  4. Click the **Custom Scripts** tab.

  5. Under **Google Analytics** , enter your Google Analytics tracking ID.

  6. Click **Save**.




## Configuring custom analytics tracking

Configure your own custom analytics tracking solution by passing event details to your own custom function. Your custom function must be defined as part of the `portal.onAnalyticsEvent` in the global namespace (declared on the `window` variable).

For example, you might want to send the event details to an analytics service other than Google Analytics:
    
    
    <script>
    window.portal = {};
    window.portal.onAnalyticsEvent = (event) => {
      // log event to console
      console.log(event);
      // TODO: publish event to custom analytics service
    }
    </script>
    

Add your custom script to each page in your portal on the **Custom Scripts** tab of the Settings page. For more information, see [Adding custom scripts](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-scripts).

The portal generates the following types of events in the same format used by Google Analytics:

Event type | Example format | More information  
---|---|---  
Page visits | 
    
    
    {
      hitType: 'pageview',
      page: '/apis'
    };
    

| [Page Views](https://developers.google.com/analytics/devguides/collection/analyticsjs/pages)  
Clicks on **Execute** on the Try it panel in the API reference doc | 
    
    
    {
      hitType: 'event',
      eventCategory: 'docsEvents',
      eventAction: 'apixExecute'
    }

| [Event Measurement](https://developers.google.com/analytics/devguides/collection/analyticsjs/events)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
