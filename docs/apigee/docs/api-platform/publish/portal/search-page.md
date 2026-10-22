---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/search-page/
title: Creating a custom search page \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:31.916353+00:00
---

# Creating a custom search page  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/search-page/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Creating a custom search page Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

To enable search of the publicly available content in your portal, you can create a dedicated search page where you embed a [Google Custom Search Engine (CSE)](https://cse.google.com).

![Click for larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/publish/images/search-page-1.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/publish/images/search-page-1.png)

![Click for larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/publish/images/search-page-2.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/publish/images/search-page-2.png)

Before embedding a Google custom search engine, note the following: 

  * Search using a Google CSE can return only results for **publicly available content**. In other words, a portal user must not be required to sign in to the portal to view the content.
  * At this time, you cannot disable ads in search results unless you are an approved non-profit site.
  * Google CSE is not included with an Apigee license. (An out-of-the-box search solution in the integrated portal is planned for a future release.)
  * The [Google Search Console](https://search.google.com/search-console/about) (also not included with an Apigee license) is another tool you may use to remove or manage your portal's presence in Google's search index.



To create a custom search page:

  1. [Publish your portal content](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-publish).
  2. Create a Google custom search engine:

     1. Navigate to the [Google custom search](https://cse.google.com/cse) configuration page.
     2. Click **Add** to create a new custom search engine.
     3. Configure your custom search engine and identify the portal site domain. See [Create a search engine](https://support.google.com/programmable-search/answer/11082370?ref_topic=4513742) in the Google Custom Search Help. The custom search configuration returns something like the following: 
            
            <script async src="https://cse.google.com/cse.js?cx=e13bcb52d46f04dfd"></script>
            <div class="gcse-search"></div>

Where `cx=e13bcb52d46f04dfd` is the Google search engine ID.
**Tip:** You can expedite site indexing by verifying and submitting your site using Google Search Console. See [Verify your site in Search console](https://support.google.com/customsearch/answer/2402989?ref_topic=4513742%22%20class=%22external) in the Google Search Console Help.
  3. Add the following custom script to your portal. See [Adding custom scripts](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-scripts).

Set the `cx` variable to your Google search engine ID, for example `e13bcb52d46f04dfd`, and the `path` value to your search page URL, for example, `/search`.
         
         <script>
         window.portal = {
          pageEventListeners: {
            onLoad: (path) => {
              // Update with your search page URL
              if (path === '/your-search-page-URL') {
                // Add your Google search engine ID
                var cx = 'your-search-engine-id';
                var gcse = document.createElement('script');
                gcse.type = 'text/javascript';
                gcse.async = true;
                gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
                var s = document.getElementsByTagName('script')[0];
                s.parentNode.insertBefore(gcse, s);
                gcse.onload = function () {
                  var search = document.createElement('gcse:search');
                  // Note the element ID name
                  var searchBox = document.getElementById('search-box');
                  searchBox.appendChild(search);
                };
              }
            }
          }
         };
         </script>
         

  4. Create a new search page in your portal and customize it as described in [Manage pages in your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-pages).

  5. Add the custom search element ID (`search-box`) defined in your custom script at the location that you want the Google search box to appear. For example `<div id="search-box"></div>`

  6. Add the search page to your portal navigation, as described in [Set up navigation](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-menus).

  7. Publish your search page and navigation updates.


It takes time for Google to index your site so you may not see search results right away. (It can take a couple of days up to a month to complete full indexing.) You may want to delay publishing the search page until you have tested your portal site search (over time) and are satisfied with the results being returned.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
