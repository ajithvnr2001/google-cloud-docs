---
url: https://docs.cloud.google.com/appengine/docs/flexible/migrating/
title: Migrate services from the standard environment to the flexible environment \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:35.360009+00:00
---

# Migrate services from the standard environment to the flexible environment  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/migrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Migrate services from the standard environment to the flexible environment Stay organized with collections  Save and categorize content based on your preferences. 

The App Engine flexible environment does not provide the API libraries present in the App Engine SDK. If you decide to migrate your application [from the App Engine standard environment to the flexible environment](https://docs.cloud.google.com/appengine/docs/flexible/flexible-for-standard-users), you must update your code to use services and APIs that are available across all Google Cloud environments.

See the following sections for instructions on how to migrate specific legacy bundled services and APIs from the standard environment to the flexible environment.

## Differences between the standard environment and the flexible environment

In addition to the [key differences outlined here](https://docs.cloud.google.com/appengine/docs/flexible/flexible-for-standard-users#similarities_and_key_differences), paths with `/_ah/` are not blocked in the flexible environment. If your app in the standard environment uses paths with `/_ah/` to access specific services, see the section for the appropriate service below.

## App identity

When running on the flexible environment, you can use a combination of environment variables and the [Compute Engine Metadata service](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to obtain information about your application:

Application info | How to access  
---|---  
Application / project ID | Either the `GOOGLE_CLOUD_PROJECT` environment variable or the `/project/project-id` resource in the metadata server  
Default hostname | App Engine Admin API [`apps.get`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps/get) method  
Service account name | The [`/instance/service-accounts` resource](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#serviceaccountname) in the metadata server  
OAuth 2.0 access token | The `/instances/service-accounts` resource in the metadata server. See the Compute Engine [Authenticating with service account credentials documentation](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#authenticating_applications_using_service_account_credentials)  
  
The following functionality is not directly available:

  * There is no default Cloud Storage bucket for your project. To use a bucket in your application, you can create a Cloud Storage bucket and use the project ID as the bucket name. You can then use the `GOOGLE_CLOUD_PROJECT` environment variable in your application as the bucket name.
  * You cannot sign blobs with the default service account. You can work around this by using the [Identity and Access Management (IAM) API](https://docs.cloud.google.com/iam/reference/rest) or by providing a service account private key to your application when deploying.
  * Similarly, there is no built-in API to obtain public certificates for verifying signatures. However, every service account's public certificates are available at `https://www.googleapis.com/robot/v1/metadata/x509/{service account email}`.
  * Note that if you use the Java runtime, the App Engine [SystemProperty](https://docs.cloud.google.com/appengine/docs/legacy/standard/java/javadoc/com/google/appengine/api/utils/SystemProperty) APIs are not available for App Engine flexible environment. However, you can set environment variables in `app.yaml` and use `System.env` to get the values, as described in [Defining environment variables](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#defining_environment_variables).



For more details on environment variables, see the runtime overview pages or the [`app.yaml` reference page](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#handlers_environment_variables).

## Background threads

Because the flexible environment has no sandbox limitations, you're free to create threads or processes that live outside of the request environment. You typically do not need to use anything other than your language’s built-in threading or multiprocessing tools.

## Blobstore

Usage of the Blobstore service has largely been replaced in both the standard environment and flexible environment by [Cloud Storage](https://docs.cloud.google.com/storage/docs). Use the [Google Cloud client libraries](https://docs.cloud.google.com/sdk/cloud-client-libraries) to store and retrieve data in Cloud Storage.

For more information, see [Using Cloud Storage](https://docs.cloud.google.com/appengine/docs/flexible/using-cloud-storage)

## Capabilities

There is no functionality similar to the Capabilities service available outside of the standard environment.

## Websockets

The App Engine flexible environment supports websockets. For more information, see [Creating persistent connections with WebSockets](https://docs.cloud.google.com/appengine/docs/flexible/using-websockets-and-session-affinity).

## Firestore in Datastore mode (Datastore)

You can access [Datastore](https://docs.cloud.google.com/datastore/docs) from anywhere using the Datastore API. Use the [Google Cloud client libraries](https://docs.cloud.google.com/sdk/cloud-client-libraries) to store and retrieve data from Datastore.

The same Datastore data is available regardless of if you use the App Engine libraries, the Google Cloud client libraries, or call the API directly.

If you are using the Python [`ndb`](https://docs.cloud.google.com/appengine/docs/legacy/standard/python/ndb) library and prefer NDB-style Datastore access, we encourage you to migrate to [Cloud NDB](https://googleapis.dev/python/python-ndb/latest). See the [Cloud NDB repo](https://github.com/googleapis/python-ndb) for more information.

While both the Cloud NDB and Datastore client libraries are supported on Python 2 and 3, and work for App Engine standard environment or flexible environment as well as _non-App Engine_ apps, their primary purpose is to help Python 2 developers move away from bundled legacy services like App Engine `ndb`. Cloud NDB has the additional goal of preserving the NDB user experience.

For more information, see [Using Datastore](https://docs.cloud.google.com/appengine/docs/flexible/using-firestore-in-datastore-mode).

## Images

The Images service is not available outside of the standard environment. However, you can easily serve images directly from your application or directly from Cloud Storage.

If you need to do image processing, you can install and use any image processing library such as:

  * [Pillow](https://python-pillow.org/) for Python
  * [ImageJ2](http://imagej.net/ImageJ2), [imgscalr](https://github.com/rkalla/imgscalr), or [thumbnailator](https://github.com/coobird/thumbnailator) for Java 
  * [imaging](https://godoc.org/github.com/disintegration/imaging) for Go
  * [GD](http://php.net/manual/en/book.image.php) or [ImageMagick](http://php.net/manual/en/book.imagick.php) for PHP



The Images service also provided functionality to avoid dynamic requests to your application by handling image resizing using a serving URL. If you want similar functionality, you can generate the re-sized images ahead of time and upload them to Cloud Storage for serving. Alternatively, you could use a third-party content delivery network (CDN) service that offers image resizing.

For more resources, see the following guides:

  * [Using Cloud Storage](https://docs.cloud.google.com/appengine/docs/flexible/using-cloud-storage)
  * [Serving Static Files](https://docs.cloud.google.com/appengine/docs/flexible/serving-static-files)



## Logging

Like the standard environment, logging works automatically in the flexible environment. However, the logs are collected in a different format. Logs will not be bundled by requests, and logs from `stdout` and `stderr` are collected separately.

If you want more control over application logging, the ability to group logs, and the ability to log additional metadata, you can use the [Cloud Logging](https://docs.cloud.google.com/logging/docs) API directly with the [Google Cloud client libraries](https://docs.cloud.google.com/sdk/cloud-client-libraries).

For more details, see [Writing application logs](https://docs.cloud.google.com/appengine/docs/flexible/writing-application-logs).

## Mail

The App Engine Mail service is not available outside the standard environment. You will need to use a third-party mail provider such as [SendGrid](https://sendgrid.com/), [Mailgun](https://www.mailgun.com/), or [Mailjet](https://www.mailjet.com/) to send email. All of these services offer APIs to send email from applications running anywhere.

For more details, see [Sending messages with third-party services](https://docs.cloud.google.com/appengine/docs/flexible/sending-messages).

## Memcache

The Memcache service is not available in the App Engine flexible environment. To cache application data, use [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-flex).

## Modules

The Modules API is not available outside of the standard environment. However, you can use a combination of environment variables and the [App Engine Admin API](https://docs.cloud.google.com/appengine/docs/admin-api) to obtain information about and modify your application's running services:

Service information | How to access  
---|---  
Current service name | `GAE_SERVICE` environment variable  
Current service version | `GAE_VERSION` environment variable  
Current instance ID | `GAE_INSTANCE` environment variable  
Default hostname | App Engine Admin API [`apps.get`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps/get) method  
List of services | App Engine Admin API [`apps.services.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/list) method  
List of versions for a service | App Engine Admin API [`apps.services.versions.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/list) method  
Default version for a service, including any traffic splits | App Engine Admin API [`apps.services.get`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/get) method  
List of running instances for a version | App Engine Admin API [`apps.services.versions.instances.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/list) method  
  
You can also use the App Engine Admin API to [deploy](https://docs.cloud.google.com/appengine/docs/admin-api/deploying-apps) and [manage](https://docs.cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic) services and versions in your application.

For more details on environment variables, see the runtime overview pages or the [`app.yaml` reference page](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#handlers_environment_variables).

## Namespaces

Outside of the standard environment, only [Datastore](https://docs.cloud.google.com/datastore/docs) supports [multitenancy directly](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy). For other services, you will need to handle multitenancy manually. To have completely isolated instances of services, you can create new projects programmatically using the [Cloud Resource Manager API](https://docs.cloud.google.com/resource-manager/docs/creating-project) and access resources across projects.

## OAuth

The OAuth service is not available in the flexible environment. If you need to verify OAuth 2.0 tokens you can do so with the [`oauth2.tokeninfo`](https://developers.google.com/apis-explorer/#search/oauth2/oauth2/v2/oauth2.tokeninfo) method of the [OAuth 2.0 API](https://developers.google.com/identity/protocols/OAuth2).

## Remote

The Remote API service is not applicable to the flexible environment. The majority of backing services, such as Datastore, that are accessible from the flexible environment are also accessible from anywhere.

## Search

The Search service is currently unavailable outside of the flexible environment. You can host any full-text search database such as Apache Solr on Compute Engine or [Elasticsearch Service on Elastic Cloud](https://console.cloud.google.com/marketplace/product/elastic-prod/elastic-cloud) and access it from both the standard environment and flexible environment.

## Sockets

The flexible environment has no sandbox restrictions, so you can open and use outbound sockets normally.

## Task Queue

To use the push Task Queue service outside of the first generation standard environment, you can use [Google Tasks](https://docs.cloud.google.com/tasks).

In many cases where you might use pull queues, such as queuing up tasks or messages that will be pulled and processed by separate workers, [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) can be a good alternative as it offers similar functionality and delivery guarantees.

## URL Fetch

The URL Fetch service is not available in the flexible environment. However, there are no sandbox restrictions, so your app can use any HTTP library to get URL Fetch functionality.

If you use Python, we recommend using [Requests](http://docs.python-requests.org/). If you use Java, we recommended using [The Google HTTP Client Library for Java](https://developers.google.com/api-client-library/java/google-http-java-client/) or [OkHttp](http://square.github.io/okhttp/).

## Users

The Users service is not available outside of the standard environment. You can use any HTTP-based authentication mechanism in the flexible environment, such as:

  * [Google Identity Platform](https://developers.google.com/identity/), which provides many options for authentication and authorization of Google user accounts.
  * [Firebase Authentication](https://firebase.google.com/docs/auth/), which provides authentication using username/password and federated identity using Google, Facebook, Twitter, and more.
  * [Auth0](https://auth0.com/), which provides authentication with various identity providers and single sign-on features.
  * [OAuth 2.0](https://oauth.net/2/) and [OpenID Connect](http://openid.net/connect/) which provide federated identity from the provider of your choice. Google is an [OpenID Connect identity provider](https://developers.google.com/identity/protocols/oauth2/openid-connect). There are also several [other](https://en.wikipedia.org/wiki/OpenID_Connect#Adoption) providers available.



Note that because the Users service is not available, it is not possible to use [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml) for Java or [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml) for other runtimes to make URLs accessible only by administrators. You will need to handle this logic within your application.

## What's next

For an overview of the key differences between the flexible environment and the standard environment with guidelines for applications that use both environments, see [App Engine flexible environment for users of standard environment](https://docs.cloud.google.com/appengine/docs/flexible/flexible-for-standard-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
