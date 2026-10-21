---
url: https://docs.cloud.google.com/appengine/docs/flexible/locations/
title: App Engine locations \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:23.107725+00:00
---

# App Engine locations  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/flexible/resources)



Send feedback 

#  App Engine locations Stay organized with collections  Save and categorize content based on your preferences. 

App Engine is _regional_ , which means the infrastructure that runs your apps is located in a specific region, and Google manages it so that it is available redundantly across [all of the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).

Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your apps are run. You can generally select the region nearest to your app's users, but you should consider [the locations where App Engine is available](https://cloud.google.com/about/locations/#region) as well as the [locations](https://cloud.google.com/about/locations/#region) of the other Google Cloud products and services that your app uses. Using services across multiple locations can affect your app's latency as well as its [pricing](https://cloud.google.com/appengine/pricing).

You cannot change an app's region after you set it.

**Note:** Two locations, which are called `europe-west` and `us-central` in App Engine commands and in the Google Cloud console, are called `europe-west1` and `us-central1`, respectively, elsewhere in Google documentation.

If you already created an App Engine application, you can view its region by doing one of the following:

  * Run the `gcloud app describe` command.

  * Open the [App Engine Dashboard in the Google Cloud console](https://console.cloud.google.com/appengine). The region appears near the top of the page.




To select a region, you create an App Engine application in your Google Cloud project. See _Manage projects, applications, and billing_ for details in your language for either the [standard](https://docs.cloud.google.com/appengine/docs/standard/managing-projects-apps-billing) or [flexible](https://docs.cloud.google.com/appengine/docs/flexible/managing-projects-apps-billing) environment.

## Cloud Storage location

When you create an app, App Engine creates a default [bucket](https://docs.cloud.google.com/storage/docs/buckets) in [Cloud Storage](https://docs.cloud.google.com/storage). Generally, the location of this bucket is the region matching the location of your App Engine app.

The following App Engine app locations create buckets that are multi-region:

  * Apps located in `us-central` create a bucket in the `US` multi-region.
  * Apps located in `europe-west` create a bucket in the `EU` multi-region.



To learn more about Cloud Storage bucket locations, see [Bucket locations](https://docs.cloud.google.com/storage/docs/locations).

## Firestore location

When you create an app, App Engine creates a default database in [Firestore](https://docs.cloud.google.com/firestore). Generally, the location of this database is the region matching the location of your App Engine app.

The following App Engine app locations create databases that are multi-region:

  * Apps located in `us-central` create a database in the `nam5` multi-region.
  * Apps located in `europe-west` create a database in the `eur3` multi-region.



To learn more about Firestore bucket locations, see [Database locations](https://docs.cloud.google.com/firestore/docs/locations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
