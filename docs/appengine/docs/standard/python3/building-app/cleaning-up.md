---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/cleaning-up/
title: Clean Up \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:22.399628+00:00
---

# Clean Up  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/cleaning-up/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Clean Up Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to clean up your Google Cloud project to avoid incurring charges to your account. Leaving your project and web service running does not necessarily incur charges; however, a large amount of traffic to your service might exceed the [free quotas](https://docs.cloud.google.com/appengine/docs/standard/quotas).

To clean up your project and retain its data, select one of the following options:

  * Disable your app

  * Disable billing

  * Delete your project


**Note:** You can't delete the default app.

## Disable your app

[Disabling your app](https://docs.cloud.google.com/appengine/docs/standard/managing-costs#disable_manually) stops it from running instances and serving requests. If your app is processing a request, your app completes the request before being disabled. Disabling your app might lead to disruptions in using other services associated with your app, such as Datastore. To disable App Engine without affecting access to your database, see [Unlink your database from App Engine](https://docs.cloud.google.com/datastore/docs/app-engine-requirement#unlink_your_database_from).

To disable an App Engine application and retain its data, do the following:

  1. In the Google Cloud console, go to the **Settings** page:

[Go to Settings](https://console.cloud.google.com/appengine/settings)

  2. In the **Application settings** tab, click **Disable application**.

  3. In the **App ID** field, enter the ID of the app you want to disable, and then click **Disable**.

**Note:** Billing charges can still occur for the other services in your Google Cloud project, like stored data. For more information, see [Disabling an application](https://cloud.google.com/appengine/pricing#managing).



## Disable billing

Disabling billing stops automatic payments for all services in your project. Even if you disable billing, you are still responsible for all outstanding charges on your account.

To disable billing on your project, do the following:

  1. In the Google Cloud console, go to the **Account management** page:

[Go to Account management](https://console.cloud.google.com/billing/manage)

  2. In the **Billing account** field, select the billing account containing the project you want to disable billing for.

  3. In the **Actions** column for the project you want to disable billing for, click the icon displayed as three dots arranged vertically (more_vert), and then click **Disable billing**.

  4. To confirm, click **Disable billing**.

**Caution:** If your billing account remains disabled for an extended period, some resources might be removed from the projects associated with that account. For example, if you use Google Cloud, your Compute Engine resources might be removed. Removed resources are not recoverable.



## Delete your project

To release all the Google Cloud resources in your Google Cloud project, delete your project by doing the following:

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

To deploy Python 3 web services and authenticate users, see [Python 3 App Engine tutorials](https://docs.cloud.google.com/docs/tutorials).

[ Previous arrow_back  Personalize data  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/personalizing-data-for-authenticated-users)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
