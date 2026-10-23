---
url: https://docs.cloud.google.com/data-studio/add-a-google-maps-api-key/
title: Add a Google Maps API key \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:10.972581+00:00
---

# Add a Google Maps API key  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-a-google-maps-api-key/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Add a Google Maps API key Stay organized with collections  Save and categorize content based on your preferences. 

> **NOTE** : This article is for creators of highly trafficked embedded reports that contain Google Maps. To complete the tasks described here, you should be (or work with someone who is) familiar with working in Google Cloud console.

When embedding is enabled, a Data Studio report supports up to 30,000 free Google Map loads per month. Map loads are counted for both embedded and non-embedded views of the report, as well as for PDF download and email views. If your report exceeds the free quota, Google Maps in the report display an error.

You can increase the number of map loads allowed by adding a Google Maps API key to the report.

**IMPORTANT:** Reports that use an API key are no longer subject to the free quota of 30,000 map loads. Each map load counts against your API key pricing tier.

## Create a Google Maps API key

To create and manage Google Maps API keys, see [Using API Keys](https://developers.google.com/maps/documentation/javascript/get-api-key) (opens in the Google Maps Platform documentation). You'll need to have a Google Cloud [billing project](https://pantheon.corp.google.com/projectselector2/google/maps-apis/credentials?_ga=2.185007785.1036907152.1627424416-1520454904.1626384426) set up to complete this step.

  1. On the _Using API Keys_ page, click **Go to the Credentials page**.
  2. If prompted, select your billing project.
  3. In the top left, click **\+ CREATE CREDENTIALS**.
  4. (Optional but recommended) Click **RESTRICT KEY**.



### Restrict the API key to your reports

We recommend that you restrict the API key to just the reports that need to use it by adding the report URLs to the Cloud Console.

  1. Under _Application restrictions_ , select **HTTP referrers (web sites)**.
  2. Under _Website restrictions_ , click **Add an item**.
  3. Enter the URL of the Data Studio report that will use this API key.
  4. Add additional URLs to allow multiple reports to use this key.



You can use wildcards so that multi page reports will work with your API key. If you are embedding your report, you need to include the embed URL of the report as well.

For example, to include multiple pages, use a URL like this:

`https://datastudio.google.com/reporting/<some-report-id>/*`

To include an embedded report, use a URL like this:

`https://datastudio.google.com/embed/reporting/<some-report-id>/*`

> **Tip** : You should remove any multi login portions of the URL, if present. For example, if the URL looks like this: `https://datastudio.google.com/u/0/reporting/…` then you should remove the `/u/0` portion so that it appears like this: `https://datastudio.google.com/reporting/…`

## Add your Google Maps API key to your reports

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select **File > Report settings**.
  3. Enter the API key in the **Google Maps API key** field.



## Pricing

Your billing account will be charged for using the API key. The following [pricing tiers](https://mapsplatform.google.com/pricing/) apply:

  * Dynamic Maps > Maps Javascript API for map loads
  * Dynamic Street View > Maps Javascript API for street view usage



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
