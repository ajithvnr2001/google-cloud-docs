---
url: https://docs.cloud.google.com/appengine/docs/standard/migrating-traffic/
title: Migrating traffic \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:26.531314+00:00
---

# Migrating traffic  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/migrating-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Migrating traffic Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby

Traffic migration switches the request routing between the versions within a service of your application, moving traffic from one or more versions to a single new version.

For information about splitting traffic between two or more versions of your app, see [Traffic Splitting](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic).

## Before you begin

Before you can configure traffic to a version, ensure that your user account includes the [required privileges](https://docs.cloud.google.com/appengine/docs/standard/access-control#basic_roles).

## Migrating traffic gradually

You can choose to route requests to the target version, either gradually or immediately.

By default, [warmup requests](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests) are disabled and traffic is migrated immediately to a version. You can also choose to disable warmup requests if you want the traffic immediately migrated to a version.

If you immediately migrate traffic to a new version without any running instances then you will experience a spike in latency for loading requests. Deploying a new version with the same name as an existing version causes an immediate traffic migration. All instances of the old version are immediately shut down. There will be a latency spike due to loading requests for the new version.

**Note:** Gradual traffic migration traffic between versions running in the flexible environment is not supported. You must migrate traffic immediately to versions that are running in the flexible environment.

If warmup requests are enabled, you can migrate traffic between versions that reside in different environments only by specifying to migrate traffic immediately.

### Adding warmup requests to your application

When warmup requests are enabled, traffic is migrated gradually by first sending a _warmup request_ to new instances before those instances receive any user requests. Warmup requests improve user response time by allowing the version currently receiving traffic to handle those requests but the traffic migration to the new version can take a short amount of time while the new instances are created.

When warmup requests are not enabled, user requests are sent to those new instances before they have been created. Due to the delay caused by creating the new instances and loading application code, latency can occur for those user responses.

For all runtimes except for Java, to avoid latency and enable warmup requests, include the `inbound_services` element in your configuration file before you deploy your application to App Engine.

For example, you include the following in your `app.yaml` file before deploying it to App Engine:
    
    
    inbound_services:
    - warmup
    

For complete details about enabling warmup requests, see [Configuring warmup requests to improve performance](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests).

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
