---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-chrome/
title: Configure Chrome Enterprise cloud-managed browsers \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:12.654304+00:00
---

# Configure Chrome Enterprise cloud-managed browsers  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-chrome/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure Chrome Enterprise cloud-managed browsers Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise seamlessly integrates with Chrome Enterprise to deliver AI-powered custom content suggestions to the address bar of your users' cloud-managed Chrome browsers. This page describes the steps to enable and configure [cloud-managed Chrome browsers](https://support.google.com/chrome/a/answer/9116814) to show these suggestions in the Chrome address bar ([omnibox](https://www.chromium.org/user-experience/omnibox/)).

**Note:** To complete these steps, you need the necessary permissions to manage Chrome browsers for your organization.

## Before you begin

### Set up Gemini Enterprise

Before setting up the Gemini Enterprise x Chrome Enterprise integration, set up Gemini Enterprise. Learn more about how to [get started with Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/quickstart-gemini-enterprise).

### Sign up for Chrome Enterprise Core

Chrome Enterprise Core lets you use the Google Admin console to set up the Gemini Enterprise Chrome policy. Learn more about [how to set up Chrome Enterprise Core](https://support.google.com/chrome/a/answer/9116814).

### Enroll users and browsers

There are two options to manage Chrome browsers from the Google Admin console using Chrome Enterprise Core: Device-level browser enrollment and User profile-level browser enrollment. Learn more about these options in [_Cloud-managed Chrome browser_](https://support.google.com/chrome/a/topic/9025410).

## Enable Enterprise Search Aggregator Chrome policy

**Note:** Changes may take up to 24 hours to apply for all cloud-managed browsers.

  1. Login to [Google Workspace Admin Console](http://admin.google.com) using your credentials. ![Login to Google Workspace Admin Console](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/configure-chrome-images/espacio_de_agentes-chrome_ui-00.png)
  2. Navigate to Menu > Chrome Browser > **Settings** to reveal the _User & browser settings_ view. ![User and browser settings view](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/configure-chrome-images/espacio_de_agentes-chrome_ui-01.png)
  3. Choose the specific **Group** or **Organizational Unit** from the respective list, or retain the default setting. Note: Learn more about [applying settings to certain users of Google Chrome](https://support.google.com/a/answer/13815697). ![Choose a Group or Organizational Unit](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/configure-chrome-images/espacio_de_agentes-chrome_ui-02.png)
  4. In the _Omnibox search provider_ category, select **Enterprise search aggregator.** ![Enterprise search aggregator list entry](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/configure-chrome-images/espacio_de_agentes-chrome_ui-03.png)
  5. Add a name, shortcut, search URL, and suggest URL, then select **Save**. ![Add a name, shortcut, search URL, and suggest URL](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/configure-chrome-images/espacio_de_agentes-chrome_ui-04.png) **Properties**  
---  
**Name** | The name that is shown to the user in their address bar.   
**Shortcut** | The keyword that the user enters to trigger the search. The shortcut can include plain words and characters, but cannot include spaces or start with the @ symbol. Shortcuts must be unique.   
**Search URL** | The URL on which to search. Enter the web address for the search engine's results page (for example, 1234), and append the search terms inside a bracketed query string.   

     * **Example copied value:** https://vertexaisearch.cloud.google.com/home/cid/**1234**  

     * **Formatted value:** https://vertexaisearch.cloud.google.com/home/cid/**1234?q={searchTerms}**
**Note:** To find the ID for your Gemini Enterprise agent, navigate to your [Google Cloud Console's AI Applications](https://console.cloud.google.com/gen-app-builder/start) page, select the appropriate Gemini Enterprise application, then select Integration > Web App.  
**Suggest URL** | The URL that provides search suggestions. 
     * **Example copied value:** https://discoveryengine.googleapis.com/v1alpha/projects/1234/locations/global/collections/default_collection/engines/enterprisesearch/**servingConfigs/default_search:search**  

     * **Formatted value:** https://discoveryengine.googleapis.com/v1alpha/projects/1234/locations/global/collections/default_collection/engines/enterprisesearch/**completionConfig:completeQuery**
**Note:** To find the ID for your Gemini Enterprise agent, navigate to your [Google Cloud Console's AI Applications](https://console.cloud.google.com/gen-app-builder/start) page, select the appropriate Gemini Enterprise application, then select Integration > Web App.  
**Icon URL** _(optional)_ | Company branded icon that will be shown when user types **@** or starts the scoped search. 
     * **Recommended format:** favicon
     * **Supported file formats:** JPEG, PNG, and ICO.   
**Require address bar shortcut to see search recommendations** | Specifies whether the address bar shortcut is required to see search recommendations from this provider.   
  
## Enable autocomplete in your Gemini Enterprise project

To enable Autocomplete in your Gemini Enterprise project, go to your [Google Cloud Console Gemini Enterprise page](https://console.cloud.google.com/gemini-enterprise/start), select your app, then select **Configurations > Autocomplete**. Autocomplete by default won't start making suggestions until it has sufficient quality data (typically a few days). To start generating autocomplete suggestions in Chrome sooner, select **Now**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
