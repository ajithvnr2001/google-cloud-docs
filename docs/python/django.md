---
url: https://docs.cloud.google.com/python/django/
title: Getting started with Django \u00a0|\u00a0 Python \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:34.275852+00:00
---

# Getting started with Django  |  Python  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/django/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Guides ](https://docs.cloud.google.com/python/docs/setup)



Send feedback 

#  Getting started with Django Stay organized with collections  Save and categorize content based on your preferences. 

Django apps that run on Google Cloud are running on the same infrastructure that powers all of Google's products, which generally improves the application's ability to adapt to a variable workload.

## Hosting platforms

These are the available options for deploying Django on Google Cloud:

Django deployment option | Get started  
---|---  
**App Engine standard environment** | 
* [Running Django on App Engine standard environment](https://docs.cloud.google.com/python/django/appengine)  
**App Engine flexible environment** | 
* [Running Django on App Engine flexible environment](https://docs.cloud.google.com/python/django/flexible-environment)  
**Cloud Run** | 
* [Running Django on Cloud Run](https://docs.cloud.google.com/python/django/run)
* [Running Django on Cloud Run with Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/deploy-cloud-run-app)
* [Running Django on Cloud Run with Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/quickstart-cloud-run)  
**Google Kubernetes Engine (GKE)** | 
* [Running Django on Google Kubernetes Engine](https://docs.cloud.google.com/python/django/kubernetes-engine)  
**Compute Engine** | 
* [Django in Google Cloud Marketplace](https://docs.cloud.google.com/marketplace/solution/bitnami-launchpad/djangostack?q=django)  
  
For more details on the differences in these platforms, see [App Hosting options on Google Cloud](https://cloud.google.com/hosting-options).

## Databases

The Django object-relational mapper (ORM) works best with an SQL relational database.

If you are starting a new project, [Cloud SQL](https://docs.cloud.google.com/sql) is a good choice. You can deploy a [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/create-instance) or [MySQL](https://docs.cloud.google.com/sql/docs/mysql/create-instance) database that's managed and scaled by Google, and supported by Django.

You can deploy Django with a Spanner backend using the [python-spanner-django](https://github.com/googleapis/python-spanner-django/) database backend.

Sometimes, there are compelling reasons to use a NoSQL database. Using the Django ORM with a NoSQL database is possible, with some limitations, but not officially supported by Django. There are a number of community-supported backend connectors Datastore, including [djangae](https://github.com/potatolondon/djangae) if you're using App Engine, or [django-gcloud-connectors](https://gitlab.com/potato-oss/google-cloud/django-gcloud-connectors) if you're using Cloud Run. If you choose to use MongoDB, you can deploy it using [Cloud Marketplace](https://docs.cloud.google.com/marketplace/solution/click-to-deploy-images/mongodb) and do your own management, or you can use the managed MongoDB hosting service provided by [mLab](https://www.mongodb.com/cloud/atlas/mongodb-google-cloud).

## Caches

[Memorystore](https://docs.cloud.google.com/memorystore) offers managed hosting options for both [Memcache](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview) and [Redis](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview). For App Engine, see the guide for [migrating from Memcache](https://docs.cloud.google.com/appengine/docs/standard/python/migrate-to-python3/memcache-to-memorystore).

## Task queuing

[Pub/Sub](https://docs.cloud.google.com/pubsub) offers messaging for event-driven systems, and [Google Tasks](https://docs.cloud.google.com/tasks) offers asynchronous task execution; see the guide for [choosing between Google Tasks or Pub/Sub](https://docs.cloud.google.com/tasks/docs/comp-pub-sub). For App Engine, see the guide for [migrating from Task queues](https://docs.cloud.google.com/appengine/docs/standard/python/migrate-to-python3/migrating-services#task_queue).

Support for task queuing through Cloud Tasks is available through a number of community-supported packages.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
