---
url: https://docs.cloud.google.com/appengine/docs/standard/using-firestore/
title: Use Firestore \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:35.023173+00:00
---

# Use Firestore  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/using-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Use Firestore Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby

Firestore is a NoSQL document database built for automatic scaling, high performance, and ease of application development. Firestore is a NoSQL document database built for automatic scaling, high performance, and ease of application development. As the successor to Datastore, Firestore is the recommended database for all new applications. Firestore offers multiple interfaces, including a Datastore-compatible API to support legacy code built on Datastore.

## Using Datastore mode with App Engine

To use Datastore mode with App Engine:

  1. If you haven't already done so, [create a database](https://docs.cloud.google.com/datastore/docs/store-query-data#create_a_database) and choose Firestore in Datastore mode.

You can use existing Datastore databases with App Engine apps. These existing databases [will be automatically upgraded to Firestore in Datastore mode](https://docs.cloud.google.com/datastore/docs/upgrade-to-firestore). 

     1. If you have a new Python 3 apps, you should use the [Datastore mode client library](https://docs.cloud.google.com/datastore/docs/reference/libraries) to interact with Datastore mode:

        1. In your app, declare Datastore as a dependency by adding `google-cloud-datastore` to your app's `requirements.txt` file. Learn more [about specifying dependencies](https://docs.cloud.google.com/appengine/docs/standard/python3/specifying-dependencies).

        2. Use the Google Cloud Client Library to [read and write entities](https://docs.cloud.google.com/datastore/docs/concepts/entities) and to [query data](https://docs.cloud.google.com/datastore/docs/concepts/queries).

     2. If you are planning to upgrade your Python 2 app to Python 3, Google recommends porting your Python 2 app that uses [App Engine NDB](https://docs.cloud.google.com/appengine/docs/standard/python/ndb) to Python 3, and _then_ [migrating to Cloud NDB](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-ndb). To learn how to access App Engine NDB in Python 3, see the [Accessing App Engine legacy bundled services for Python 3](https://docs.cloud.google.com/appengine/docs/standard/python3/services/access).

For additional resources plus an example of migrating from a Python 2 `webapp` app using App Engine NDB to an equivalent Python 3 Flask app with App Engine NDB enabled, see the [bundled services for Python 3](https://docs.cloud.google.com/appengine/docs/standard/python3/services/access#example_app_engine_ndb). 

## Configuring indexes

Datastore mode uses [indexes](https://docs.cloud.google.com/datastore/docs/concepts/indexes) for every query your application makes. The indexes are updated whenever an entity changes, so the results can be returned quickly when the app makes a query.

Datastore mode automatically creates single-property indexes for use with simple types of queries. For complex queries that include multiple properties, you'll need to configure composite indexes in your app's `index.yaml` file.

The App Engine development server will update your `index.yaml` file with the composite indexes needed to run your tests. Similarly, the [Datastore mode emulator can generate indexes](https://docs.cloud.google.com/datastore/docs/tools) when you run tests.

You can also add the indexes to your app's `index.yaml` file [manually](https://docs.cloud.google.com/appengine/docs/standard/configuring-datastore-indexes-with-index-yaml) if you do not run local tests or your tests do not include complex queries.

## Setting database permissions

By default, your app has all the permissions required to read and write to Datastore mode and Firestore databases in your Google Cloud project.

To manage these permissions, each App Engine app uses a [default service account](https://docs.cloud.google.com/appengine/docs/standard/default-service-account) that gives full read and write access to Datastore mode and Firestore databases in the same project as the app. You can [change the permissions of the default service account](https://docs.cloud.google.com/appengine/docs/standard/access-control#modify-service-account), but your app may lose access unless you assign an IAM role with the [required permissions](https://docs.cloud.google.com/datastore/docs/access/iam#required_permissions).

For information about allowing other users, apps, or projects to access a database, see [Accessing your database](https://docs.cloud.google.com/datastore/docs/activate).

## Using the Datastore mode emulator for local testing

The Google Cloud CLI includes a local [emulator of the production Datastore mode mode environment](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator). You can use the emulator to develop and test your application locally. In addition, the emulator can help you generate indexes for your production Datastore mode mode instance and delete unneeded indexes.

If you use the App Engine [local development server](https://docs.cloud.google.com/appengine/docs/standard/python/tools/using-local-server) to test your app, you can ensure that the server will use the Datastore mode emulator by setting the `--support_datastore_emulator=true` flag when starting the server.

If you are using the Datastore mode emulator, dev_appserver will display:
    
    ... Using Cloud Datastore Emulator.
    

## Pricing, quotas, and limits

Datastore mode offers a free quota with daily limits. Paid accounts offer unlimited storage, read, and write operations. More information is available on the [Datastore Quotas](https://docs.cloud.google.com/appengine/docs/standard/quotas#Datastore) page.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
