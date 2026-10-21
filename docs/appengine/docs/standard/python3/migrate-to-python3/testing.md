---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/migrate-to-python3/testing/
title: Testing and deploying your upgraded app in Python 3 \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:35.789174+00:00
---

# Testing and deploying your upgraded app in Python 3  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/migrate-to-python3/testing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Testing and deploying your upgraded app in Python 3 Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python3/how-requests-are-routed#region-id). 

OK

After you upgrade your app to be compatible with both Python 2 and Python 3:

  1. Test the app in a local Python 3 environment.

  2. Deploy and test in App Engine without shifting traffic to your app.

  3. Migrate traffic to your app.




You may need to spend significant time fixing compatibility issues that aren't visible until you run your upgraded app in a Python 3 environment.

To avoid using production data and Google Cloud quota during testing, you can use the following emulators:

  * [Datastore](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator)
  * [Bigtable](https://docs.cloud.google.com/bigtable/docs/emulator)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/emulator)



Other Google Cloud services such as Cloud Storage and Memorystore don't provide emulators.

## Testing locally

To test your app's functionality before deploying, follow the instructions for [running locally](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#running_locally) in the Python 3 runtime.

## Testing on App Engine before shifting traffic

Before routing traffic to your upgraded Python app, deploy the app to the App Engine Python 3 runtime for another round of testing. For example, to test your app's `default` service:

  1. Make sure you've [updated the app's configuration files](https://docs.cloud.google.com/appengine/docs/standard/python3/migrate-to-python3/config-files) for compatibility with the Python 3 runtime.

Don't change environment variables that send requests to emulators or test databases until you're ready to shift traffic to your app.

  2. Deploy your new version, but prevent traffic from automatically routing to the new version: 
         
         gcloud app deploy --no-promote

  3. Access your new version by navigating to the following URL:

`https://VERSION_ID-dot-default-dot-PROJECT_ID.REGION_ID.r.appspot.com`

**Note:** You can find the version ID in the [Google Cloud console](https://console.cloud.google.com/appengine/versions), or specify one when you deploy with the `--version flag`. The gcloud CLI also outputs the version ID when you deploy.



Now you can test your new version in the App Engine runtime environment. You can debug your application by viewing its logs. For more information, see [Writing Application Logs](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs).

Requests sent to `https://PROJECT_ID.REGION_ID.r.appspot.com` are routed to the version previously configured to receive traffic.

To test new versions of other services, follow the same process, but replace `default` in the URL with your service's name:

`https://VERSION-dot-SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com`

For more information about targeting specific services and versions, see [How Requests are Routed](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed).

## Migrating traffic to your app

When you're ready to send traffic to the new version:

  1. Update environment variables in your `app.yaml` file to send requests to your production databases and other services instead of any emulators or test data you were using.

  2. Prevent traffic being automatically routed to your new version upon deployment:
         
         gcloud app deploy --no-promote

  3. When you've confirmed that your app is interacting with your production databases and datastores, use the Google Cloud console to migrate traffic:

[Manage versions](https://console.cloud.google.com/appengine/versions)

Select the latest version of your upgraded app and click **Migrate traffic**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
