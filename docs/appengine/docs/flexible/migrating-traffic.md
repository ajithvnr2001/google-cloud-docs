---
url: https://docs.cloud.google.com/appengine/docs/flexible/migrating-traffic/
title: Migrating traffic \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:24.017180+00:00
---

# Migrating traffic  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/migrating-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Migrating traffic Stay organized with collections  Save and categorize content based on your preferences. 

Traffic migration switches the request routing between the versions within a service of your application, moving traffic from one or more versions to a single new version.

Traffic is migrated immediately between your versions in the flexible environment. Unlike versions in the standard environment, [gradual traffic migration](https://docs.cloud.google.com/appengine/docs/standard/migrating-traffic) is not supported in the flexible environment.

If you immediately migrate traffic to a new version without any running instances then your app will have a spike in latency while instances are being created. You can avoid a spike in latency by using the [App Engine Admin API](https://docs.cloud.google.com/appengine/docs/admin-api) to provision sufficient instances of the new app's version before you migrate traffic to it.

Set [`minTotalInstances`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#automaticscaling) for the new version to the number needed to handle expected traffic. After migration is complete, you can reset this field so that autoscaling occurs if traffic drops.

You can split traffic between versions of your app, increasing the amount of traffic a version receives in stages. 

For information about splitting traffic between two or more versions of your app, see [Traffic Splitting](https://docs.cloud.google.com/appengine/docs/flexible/splitting-traffic).

## Before you begin

Before you can configure traffic to a version, ensure that your user account includes the [required privileges](https://docs.cloud.google.com/appengine/docs/flexible/access-control#basic_roles).

## Migrating traffic to a new version

### Console

To migrate traffic in the Google Cloud console, go to the Versions page:

[Go to Versions](https://console.cloud.google.com/appengine/versions)

  1. Select the version to which you want to migrate 100% of the traffic.
  2. Click **Migrate traffic**.
  3. Optional: When warmup requests are enabled your traffic is migrated gradually. To migrate traffic immediately, select the option under the **Show advanced options** section.



### gcloud

After installing the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), you run the [`gcloud app services set-traffic`](https://docs.cloud.google.com/sdk/gcloud/reference/app/services/set-traffic) command to migrate 100% of traffic to a single version. For example:

  * To migrate traffic immediately: 
        
        gcloud app services set-traffic [MY_SERVICE] --splits [MY_VERSION]=1

  * To gradually migrate traffic, you include the optional `--migrate` flag: 
        
        gcloud app services set-traffic [MY_SERVICE] --splits [MY_VERSION]=1 --migrate




### API

To programmatically migrate traffic, you can use the Admin API, see [Migrating and Splitting Traffic](https://docs.cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic) for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
