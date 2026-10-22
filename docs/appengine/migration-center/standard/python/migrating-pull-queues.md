---
url: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-pull-queues/
title: Migrating pull queues to Pub/Sub (Python) \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:02.075796+00:00
---

# Migrating pull queues to Pub/Sub (Python)  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-pull-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrating pull queues to Pub/Sub (Python) Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to migrate pull queue code from Task Queues to Pub/Sub. Pub/Sub is now the preferred way of performing pull queue work in App Engine.

If your app uses both pull queues and push queues, use this guide to migrate your pull queues to Pub/Sub before migrating your push queues to the new push queue service Cloud Tasks. Migrating your pull queues after migrating push queues to Cloud Tasks is not recommended because the required use of the `queue.yaml` file is likely to cause unexpected behavior with Cloud Tasks.

## Features not currently available in Pub/Sub

The following Task Queues features are not currently available in Pub/Sub:

  * Batching by tag
  * Automatic deduplication



## Pricing and quotas

Migrating your pull queues to Pub/Sub might affect the pricing and quotas for your app.

### Pricing

Pub/Sub has its own [pricing](https://cloud.google.com/pubsub/pricing). As with Task Queues, sending requests to your App Engine app with Pub/Sub can cause your app to incur costs.

### Quotas

The Pub/Sub [quotas](https://docs.cloud.google.com/pubsub/quotas) are different from the quotas for Task Queues. Like with Task Queues, sending requests to your App Engine app from Pub/Sub might impact your App Engine [request quotas](https://docs.cloud.google.com/appengine/docs/standard/quotas#Requests).

## Before migrating

If you have not done so already, set up your [Python development environment](https://docs.cloud.google.com/python/docs/setup) to use a Python version that is compatible with Google Cloud, and install testing tools for creating isolated Python environments. 

The following sections discuss the setup steps before migrating your pull queues to Pub/Sub.

### Enabling the Pub/Sub API

To enable the Pub/Sub API, click [**Enable** on the Pub/Sub API](https://console.cloud.google.com/apis/library/pubsub.googleapis.com) in the API Library. If you see a **Manage** button instead of an **Enable** button, you have previously enabled the Pub/Sub API for your project and do not need to do so again.

### Authenticating your app to the Pub/Sub API

You must authenticate your app to the Pub/Sub API. This section discusses authentication for two different use cases.

To develop or test your app locally, we recommend using a service account. For instructions on setting up a service account and connecting it to your app, read [Obtaining and providing service account credentials manually](https://docs.cloud.google.com/docs/authentication#service-accounts).

To deploy your app on App Engine, you do not need to provide any new authentication. The Application Default Credentials (ADC) infer authentication details for App Engine apps.

### Downloading the Google Cloud CLI

Download and install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) to use the gcloud CLI with the Pub/Sub API if you have not installed it previously. Run the following command from your terminal if you already have the Google Cloud CLI installed.
    
    
    gcloud components update

### Importing the Cloud Client Libraries

Follow the steps below to use the Pub/Sub Python client library with your existing App Engine app:

  1. Update the `app.yaml` file. Follow the instructions for your version of Python:

###  Python 2 

For Python 2 apps, add the latest versions of the `grpcio` library.

The following is an example `app.yaml` file:
         
         runtime: python27
         threadsafe: yes
         api_version: 1
         
         libraries:
         - name: grpcio
           version: latest
         

###  Python 3 

For Python 3 apps, specify the `runtime` element in your `app.yaml` file with a supported Python 3 version. For example:
         
         runtime: python310 # or another support version
         

The Python 3 runtime installs libraries automatically, so you do not need to specify built-in libraries from the previous Python 2 runtime. If your Python 3 app is using other legacy bundled services when migrating, you can continue to specify the necessary built-in libraries. Otherwise, you can delete the unnecessary lines in your `app.yaml` file.

  2. Update the `requirements.txt` file. Follow the instructions for your version of Python:

###  Python 2 

Add the Cloud Client Libraries for Pub/Sub to your list of dependencies in the `requirements.txt` file.
         
         google-cloud-pubsub
         

Then run `pip install -t lib -r requirements.txt` to update the list of available libraries for your app.

###  Python 3 

Add the Cloud Client Libraries for Pub/Sub to your list of dependencies in the `requirements.txt` file.
         
         google-cloud-pubsub
         

App Engine automatically installs these dependencies during app deployment in the Python 3 runtime, so delete the `lib` folder if one exists.

  3. For Python 2 apps, if your app is using built-in or copied libraries, you must specify those paths in the `appengine_config.py` file, located in the same folder as your `app.yaml` file:
         
         import pkg_resources
         from google.appengine.ext import vendor
         
         # Set PATH to your libraries folder.
         PATH = 'lib'
         # Add libraries installed in the PATH folder.
         vendor.add(PATH)
         # Add libraries to pkg_resources working set to find the distribution.
         pkg_resources.working_set.add_entry(PATH)
         

The `appengine_config.py` file above assumes that the current working directory is where the `lib` folder is located. In some cases, such as unit tests, the current working directory can be different. To avoid errors, you can explicitly pass in the full path to the `lib` folder using:
         
         import os
         path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')

  4. Import the Pub/Sub Python client library in any files that use pull queues from the Task Queues API:
         
         from google.cloud import pubsub




## Pub/Sub and pull queues

### Feature comparison

Pub/Sub sends work to workers through a publisher/subscriber relationship. A [pull subscription](https://docs.cloud.google.com/pubsub/docs/subscriber#pull-subscription) in Pub/Sub is like a pull queue in Task Queues because the subscriber pulls the message from the topic. The table below lists the core feature for pull queues in Task Queues and the associated feature for pull subscriptions in Pub/Sub.

Task Queues feature | Pub/Sub feature  
---|---  
Queue | Topic  
Task | Message  
Worker | Subscriber  
  
To learn more about the Pub/Sub architecture, read [Cloud Pub/Sub: A Google-Scale Messaging Service](https://docs.cloud.google.com/pubsub/architecture).

### Workflow comparison

Below is a comparison of a typical workflow for a pull queue in Task Queues and a [pull subscription](https://docs.cloud.google.com/pubsub/docs/subscriber#pull-subscription) in Pub/Sub.

Task Queues workflow | Pub/Sub workflow  
---|---  
You create the pull queue | You create the topic and subscribe your subscriber (i.e. worker) to the topic  
You create and enqueue the task | You create the message and publish it to the topic  
The worker leases the task | The subscriber pulls the message from the topic  
The worker processes the task | The subscriber processes the message  
The worker deletes the task from the queue | The subscriber acknowledges the message  
The lease expires | The topic deletes the message when all of its subscribers have acknowledged the message  
  
## Creating pull subscriptions in Pub/Sub

You can use a Pub/Sub pull subscription like a Task Queues pull queue. Subscriptions to a topic do not expire and can exist simultaneously for multiple workers. This means that a message can be processed by more than one worker, which is one of the primary use cases for Pub/Sub. To recreate your Task Queues pull queues as Pub/Sub pull subscriptions, create a topic for each worker and subscribe only the associated worker to the topic. This ensures that each message is processed by exactly one worker as in Task Queues. To learn about creating and managing pull subscriptions, read about [managing topics and subscriptions](https://docs.cloud.google.com/pubsub/docs/admin).

## Deleting pull queues

After you migrate your Task Queues pull queues to Pub/Sub pull subscriptions, delete them from Task Queues using your `queue.yaml` file. We recommend deleting each pull queue before migrating the next one. This prevents your app from duplicating the work it receives from the new Pub/Sub pull subscription while you migrate your other pull queues. Note that deleting your Task Queues pull queues one by one rather than in a single deployment might have a greater effect on your App Engine [deployment quota](https://docs.cloud.google.com/appengine/docs/standard/quotas#Deployments).

After you delete all your pull queues from Task Queues, you can omit the `queue.yaml` file from future deployments of your app.

If your app only uses pull queues, remove any references to the Task Queues API in your code. If your app uses both pull queues and push queues, you can either remove the references to the Task Queues API that occur in files that only use pull queues, or wait until you have also migrated your push queues and then remove references to the Task Queues API from all files.

## What's next

  * [Pub/Sub documentation](https://docs.cloud.google.com/pubsub/docs)
  * [Migrating push queues](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues)
  * For a hands-on tutorial, see the [Migrate from App Engine Task Queue pull queues to Pub/Sub codelab](https://codelabs.developers.google.com/codelabs/cloud-gae-python-migrate-19-pubsub). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
