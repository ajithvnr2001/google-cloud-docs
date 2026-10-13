---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-scripts/
title: Adding custom scripts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:31.833617+00:00
---

# Adding custom scripts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-scripts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Adding custom scripts Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Warning** : Custom scripts are supported for integrating third-party services such as web metrics or feedback tools. Avoid using custom scripts to manipulate the DOM to override or otherwise change built-in behaviors of the portal.

To add custom JavaScript code or HTML content before the `<body>` tag on each page in your portal:

  1. In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click **Settings** in the navigation menu.

  3. In the **Custom Scripts** section, enter the custom JavaScript code in the text box. You can include multiple scripts. **Warning** : Make sure to enclose your custom code in `<script>` and `</script>` tags. Invalid JavaScript code has the potential to impact the correct display of content or introduce security vulnerabilities across your entire site.

  4. Click **Save**.




The following sections provide examples of custom scripts:

  * Executing a custom script during and onLoad or onUnload JavaScript event

  * Adding a cookie consent popup




See also [Configuring analytics tracking](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-analytics).

## Executing a custom script during an onLoad or onUnload JavaScript event

Define custom scripts to be executed when each page in your portal:

  * Loads into the DOM using the `onLoad` JavaScript event.
  * Is navigated away from using the `onUnload` JavaScript event.



Your custom function must be defined as part of the `portal.pageEventListeners` in the global namespace (declared on the `window` variable).

Both the `onLoad` and `onUnload` events receive as their first parameters the current path of the page (`/quickstart`, for example). The `onUnload` function receives as its second parameter the return value from the `onLoad` call enabling context to be passed between the two events. Use `onUnload` to clean up the event listeners that are no longer required and perform other clean up activities.

For example:
    
    
    <script>
    window.portal = {};
    window.portal.pageEventListeners = {
      onLoad: (path) => {
        if (path === '/quickstart') {
          // Change text content of first <p> element to something
          // else. (DOM must be loaded when onLoad is called)
          document.getElementsByTagName('p')[0].textContent =
              'Welcome to the quick start! Be sure to send us your feedback.';
          // print a custom message to the console every second while user is on
          // quickstart page.
          const interval =
              window.setInterval(() => console.log('Hello'), 1000);
          return interval;
        }
        return undefined;
      },
      onUnload: (path, contextReturnedFromOnLoad) => {
        if (contextReturnedFromOnLoad != null) {
          // Stop printing custom message to console every second.
          window.clearInterval(contextReturnedFromOnLoad)
    
        }
      },
    };
    </script>
    
    

## Adding a cookie consent popup

Custom scripts may be used to implement a cookie consent solution. There are a number of popular open source options implemented in JavaScript; select one that meets your specific compliance requirements.

For example, the following script uses the [Cookie Info Script](https://cookieinfoscript.com/).
    
    
    <script type="text/javascript" id="cookieinfo" src="//cookieinfoscript.com/js/cookieinfo.min.js">
    </script>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
