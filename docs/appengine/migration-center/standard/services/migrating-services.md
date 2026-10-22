---
url: https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services/
title: Migrate off of legacy bundled services \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:18.348848+00:00
---

# Migrate off of legacy bundled services  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate off of legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Most of the functionality provided by the legacy bundled services is now provided by the [Cloud Client Libraries](https://docs.cloud.google.com/python/docs/reference%0A). For more information, see the recommended alternatives listed below.

If migrating to an unbundled solution is not an option for your project, then you may be able to continue [using legacy bundled services in your Python 3 apps](https://docs.cloud.google.com/appengine/docs/standard/%0Apython3%0A%0A/services/access) as a fallback. This approach gives you flexibility to move to unbundled services later in the migration cycle.

**Note** : Not all the legacy bundled services available for Python 2 have a corresponding service in Python 3 , so those will need to be migrated to either a Google Cloud or third-party service before porting to Python 3 .

After you migrate off of legacy bundled services, you can continue using App Engine or migrate to Cloud Run. Cloud Run is designed to improve upon the App Engine experience, and incorporates many of the best features of both the standard environment and the flexible environment. To compare features and understand how to migrate, see the [App Engine and Cloud Run comparison guide](https://docs.cloud.google.com/appengine/migration-center/run/compare-gae-with-run).

Google Cloud provides standalone products that offer functionality similar to some of the legacy bundled services in the Python runtime. For the legacy bundled services that aren't available as separate products in Google Cloud, such as, mail, and messaging, this guide recommends third-party providers or other workarounds.

This page introduces the migration path for the legacy bundled services.

## Understand Google Cloud permissions

Your migrated app and the Google Cloud services that it uses aren't running in the same sandboxed environment, and your app requires authorization to access each service. For example, to interact with Firestore in Datastore mode (Datastore) or Cloud Tasks, your app must supply the credentials for an account that is authorized to access those services.

By default, apps running in the App Engine standard environment supply the credentials for the default App Engine [service account](https://docs.cloud.google.com/iam/docs/service-accounts), which is authorized to access databases in the same project as your app.

If any of the following conditions are true, use an alternative authentication method that explicitly provides credentials:

  * Your app and the Memorystore database are in different Google Cloud projects.

  * You have changed the roles assigned to the default App Engine service account.




For information about alternative authentication methods, see [Setting up authentication for server-to-server production applications](https://docs.cloud.google.com/docs/authentication/production#auth-cloud-implicit-python).

### Authentication for local development

To develop or test your app locally, create and use a service account. Don't use the [default App Engine service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts#default_service_account) because it has broad permissions for your project. Instead, create and use a service account with the minimum [permissions that you need](https://docs.cloud.google.com/appengine/docs/standard/roles) for your specific development and testing tasks.

To set up a service account and connect it to your app, see [Obtaining and providing service account credentials manually](https://docs.cloud.google.com/docs/authentication/production#obtaining_and_providing_service_account_credentials_manually).

## Install client libraries

To use Google Cloud services from a Python app, install the Python client library for the service. Google Cloud services also provide [REST APIs and other interfaces](https://docs.cloud.google.com/apis/docs/overview#accessing-cloud-apis).

To install a client library for the Python 3 runtime:

  1. Add the library name to your app's [`requirements.txt`](https://pip.pypa.io/en/latest/user_guide/#requirements-files) file. For example:
         
         google-cloud-ndb
         

  2. [Deploy your app](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#deploying_your_application).




App Engine automatically uploads all libraries listed in the `requirements.txt` file to the Python 3 runtime.

## Migration paths for App Engine bundled services

### Blobstore

To store and retrieve data, use [Cloud Storage](https://docs.cloud.google.com/storage) through the [Cloud Client Libraries](https://docs.cloud.google.com/storage/docs/reference/libraries). To get started, see [Using Cloud Storage](https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage) and [Migrate from Blobstore to Cloud Storage](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-storage) guide. To simulate this migration, [add Blobstore usage to a sample app](https://developers.googleblog.com/2022/07/how-to-use-app-engine-blobstore-Module15.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_mgrblobstore_sms_202029) and [migrate to Cloud Storage](https://developers.googleblog.com/2022/08/migrating-from-app-engine-blobstore-to-cloud-storage-module-16.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_mgrcloudstorage_sms_202029).

### Datastore

If your Python 2 app uses NDB to interact with Datastore, [migrate to the Cloud NDB library](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-ndb). Cloud NDB is meant primarily as a transition tool for migrating Python 2 apps. We recommend that Python 3 apps use the [Datastore mode client library](https://docs.cloud.google.com/datastore/docs/reference/libraries).

For details, see [Migrating to Cloud NDB](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-ndb). To simulate this migration with a sample app, see [Migrating from App Engine ndb to Cloud NDB](https://developers.googleblog.com/2021/07/migrating-from-app-engine-ndb-to-cloud-ndb.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_mgrcloudndb_201021).

### Images

To migrate the App Engine Images service, deploy a containerized image transformation service to Cloud Run and route your App Engine Images service calls to it. To host and serve images, store them in a Cloud Storage bucket or distribute them using Cloud CDN. For more information, see [Migrate the Images service](https://docs.cloud.google.com/appengine/migration-center/standard/python/images-to-cloud-run). 

### Logging

We recommend that you update your app to use Cloud Logging, which supports features such as viewing logs in the Logs Explorer, downloading logs, filtering messages by severity, and correlating app messages with specific requests. Alternatively, if you prefer simplicity over data accuracy, you can write structured logs to `stdout` or `stderr`. For more information, see [Writing and viewing logs](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs) and [Migrating to Cloud Logging](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-logging).

### Mail

To improve email security and ensure reliable, high-volume email delivery, we recommend that you [migrate from the legacy Mail service to an SMTP-based email service](https://docs.cloud.google.com/appengine/migration-center/standard/python/mail-to-smtp), such as SendGrid, Mailgun, or Mailjet. 

### Memcache

To cache application data, [use Memorystore for Redis](https://docs.cloud.google.com/appengine/docs/standard/using-memorystore). 

For details, see [Migrate Memcache to Memorystore](https://docs.cloud.google.com/appengine/migration-center/standard/python/memcache-to-memorystore). To simulate this migration, [add Memcache usage](https://developers.googleblog.com/2022/05/how-to-use-app-engine-memcache-in-flask-apps.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_mgrmemcache_sms_202006) to a sample app and [migrate to Memorystore for Redis](https://developers.googleblog.com/2022/06/Migrating-from-App-Engine-Memcache-to-Cloud-Memorystore-Module-13.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_mgrmemorystore_sms_202029).

**Note:** Unlike Memcache, **Memorystore for Redis doesn't provide a free tier**. For more information about Memorystore pricing, see [Quotas and limits](https://docs.cloud.google.com/memorystore/docs/redis/quotas).

For apps that use Memcache only to reduce latency for NDB (or Cloud NDB) requests, use [Cloud NDB's built-in support for Redis](https://cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-ndb#determine_caching) instead of Memcache or Memorystore for Redis. 

### Modules

To obtain information and modify your application's running services, use a combination of environment variables and the App Engine Admin API:

Service information | How to access  
---|---  
Current application ID | `GAE_APPLICATION` environment variable  
Current project ID | `GOOGLE_CLOUD_PROJECT` environment variable  
Current service name | `GAE_SERVICE` environment variable  
Current service version | `GAE_VERSION` environment variable  
Current instance ID | `GAE_INSTANCE` environment variable  
Default hostname | Admin API [`apps.get`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps/get) method  
List of services | Admin API [`apps.services.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/list) method  
List of versions for a service | Admin API [`apps.services.versions.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/list) method  
Default version for a service, including any traffic splits | Admin API [`apps.services.get`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/get) method  
List of running instances for a version | Admin API [`apps.services.versions.instances.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/list) method  
  
For more information about the data available about your application's running services, see [ Python 3 runtime environment](https://docs.cloud.google.com/appengine/docs/standard/%0Apython3%0A%0A/runtime#environment_variables).

### Namespaces

The [Namespaces API](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy) enables multitenant apps to partition data across tenants simply by specifying a unique namespace string for each tenant.

While Datastore [supports multitenancy](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy) directly, other Google Cloud services do not. If your multitenant app uses other Google Cloud services, you will need to handle multitenancy manually. To have completely isolated instances of services, you can create new projects programmatically using the [Cloud Resource Manager API](https://docs.cloud.google.com/resource-manager/docs/creating-project) and access resources across projects.

### OAuth

Instead of using the App Engine OAuth service to verify OAuth 2.0 tokens, use the [`oauth2.tokeninfo`](https://developers.google.com/apis-explorer/#search/oauth2/oauth2/v2/oauth2.tokeninfo) method of the [OAuth 2.0 API](https://developers.google.com/identity/protocols/OAuth2).

### Search

Host any full-text search database such as Elasticsearch on Compute Engine and access it from your service.

### Task queue

The App Engine Task Queue service is available in two different modes. Migrating away from either points towards two different standalone Cloud products.

#### Push tasks

Instead of App Engine Task Queue push tasks service for asynchronous code execution, use [Cloud Tasks](https://docs.cloud.google.com/tasks) [client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries#python) with a Python 3 standard environment endpoint as the target. For more information, see [Migrating push queues to Cloud Tasks](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues).

To simulate this migration with a sample app, see [How to use App Engine push queues in Flask apps](https://developers.googleblog.com/2021/09/how-to-use-app-engine-push-queues-in.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_mgrgaetasks_sms_201028) and [migrating to Cloud Tasks](https://developers.googleblog.com/2021/10/migrating-app-engine-push-queues-to.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_mgrcloudtasks_sms_201112).

#### Pull tasks

If you use the Task Queue pull tasks service, for example, queuing up tasks or messages to be processed by separate workers, [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub) can be a good alternative. It it offers similar functionality and delivery guarantees. Like other Cloud services, Pub/Sub provides convenient [client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries#python) to access the service. For more information, see [Writing and responding to Pub/Sub messages](https://docs.cloud.google.com/appengine/docs/standard/writing-and-responding-to-pub-sub-messages) and [Task Queue pull tasks to Pub/Sub](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-pull-queues) migration guide.

To simulate this migration with a sample app, see [How to use App Engine pull tasks](https://developers.googleblog.com/2022/11/how-to-use-app-engine-pull-tasks-module-18.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_mgrgaepull_sms_202013) usage to a sample app and [migrating to Pub/Sub](https://developers.googleblog.com/2022/12/migrating-from-app-engine-pull-tasks-to.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_mgrpubsub_sms_202016).

### URL Fetch

By default, the Python 2.7 runtime uses the URL Fetch service to handle outbound HTTP(S) requests, even if you use standard Python libraries to issue those requests.

If your app uses URL Fetch APIs directly, for example to make asynchronous requests, we recommend migrating to a standard Python library such as the [Requests library](https://docs.python-requests.org/en/master/).

For more information, see [Migrating Outbound Requests](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-outbound-requests).

### User authentication

For an alternative to the Users API, use any of the HTTP-based authentication mechanisms described on the [User authentication](https://docs.cloud.google.com/appengine/docs/standard/authenticating-users) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
