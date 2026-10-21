---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/migrating/
title: Migrating to Cloud Endpoints Frameworks version 2.0 \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:20.553604+00:00
---

# Migrating to Cloud Endpoints Frameworks version 2.0  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/migrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Migrating to Cloud Endpoints Frameworks version 2.0 Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Endpoints Frameworks was formerly called Endpoints. To distinguish between the two versions, this page refers to the new version as Endpoints Frameworks version 2.0, and the older version as Endpoints version 1.0. This page describes how to migrate an Cloud Endpoints version 1.0 application to [Endpoints Frameworks version 2.0](https://docs.cloud.google.com/endpoints/docs/frameworks/python). The migration consists of a library change and an application configuration change, but you don't have to make any changes to your code.

## Benefits

Endpoints version 2.0 brings a number of benefits, including:

  * Reduced request latency.
  * Better integration with App Engine features, such as custom domains.
  * New API management features.



Endpoints Frameworks version 2.0 doesn't affect the interfaces to your API. Existing clients continue to work after migration without any client-side code changes.

## Feature overview

The following features are backward compatible with Endpoints version 1.0:

  * JSON-REST protocol, which is used by all Google client libraries
  * Discovery service
  * All existing authentication features (OAuth2/OpenID Connect)
  * Client library support for generated clients
  * CORS (for JavaScript callers not using Google JavaScript client library)
  * API Explorer



Traffic splitting is unavailable.

## Currently excluded features

The following features are unavailable. If you require any of these, please submit a [feature request](https://github.com/cloudendpoints/endpoints-python/issues).

  * JSON-RPC protocol, which is required for legacy iOS clients. To create iOS clients for your Endpoints Frameworks version 2.0 API, we recommend that you use [Google APIs Objective-C client library for REST APIs](https://github.com/google/google-api-objectivec-client-for-rest/wiki).
  * Automatic ETags
  * Automatic `kind` fields
  * IDE integration
  * `fields` partial responses
  * Automatic PATCH API method creation



## Migrating from Endpoints version 1.0

**Important:** You must download the linked packages and import them into your application. You must remove the old dependencies.

To migrate from version 1.0:

  1. Create a subfolder named `/lib` in your application's main directory.

  2. Install the library from your application's main directory:
         
         pip install -t lib google-endpoints --ignore-installed
         

  3. Remove the `- name: endpoints` and `version 1.0` entries from your application's `app.yaml` file under the `libraries` section. For example:
         
         libraries:
         - name: endpoints   #Remove
           version: 1.0      #Remove
         

  4. In the `libraries` section in the `app.yaml` file, add the following:
         
         libraries:
         - name: pycrypto
           version: 2.6
         - name: ssl
           version: 2.7.11
         

Endpoints Frameworks requires these versions of the `pycrypto` and `ssl` libraries.

  5. In the `handlers` section in the `app.yaml` file, change the `url` directive from `- url: /_ah/spi/.*` to `- url: /_ah/api/.*`.

  6. In the root directory of your application, create or modify a file named `appengine_config.py` to include the following:
         
         from google.appengine.ext import vendor
         
         vendor.add('lib')
         

  7. Check your API version string. Your version string, specified in the `@endpoints.api(version='v1', ...)` decorator, appears in your API's path. If you specify a version string compatible with the [SemVer standard](https://semver.org/spec/v2.0.0.html), only the major version number appears in your API's path when you deploy your API. For example, an API called `echo` with version `2.1.0` would have a path such as `/echo/v2`. If you update the `echo` API to version `2.2.0` and deploy a backwards-compatible change, the path remains `/echo/v2`. This allows you to update the API version number when you make a backwards-compatible change without breaking existing paths for your clients. But if you update the `echo` API to version `3.0.0` (because you are deploying a breaking change), the path is changed to `/echo/v3`.

  8. Redeploy your Endpoints Frameworks application. **Note** : When migrating, you must deploy to a new App Engine version. This is done automatically if you don't specify a version. See [Known Issues](https://docs.cloud.google.com/endpoints/docs/frameworks/known-issues#endpoints_frameworks_migration).




### Verifying a new deployment

To verify that the new framework is serving traffic:

  1. Send some requests to the new deployment.
  2. Visit the Cloud Logging page for your project.  


[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  3. If requests are shown with having paths beginning with `/_ah/api`, then Endpoints Frameworks version 2.0 is now serving your API. The logs shouldn't show any requests with paths beginning with `/_ah/spi`. These requests indicate that the Endpoints version 1.0 proxy is still serving requests.



## Adding API management

Endpoints Frameworks version 2.0 adds API management features, including:

  * API key management
  * API sharing
  * User authentication
  * API metrics
  * API logs



To get started, go to the [Getting started with Endpoints Frameworks for Python](https://docs.cloud.google.com/endpoints/docs/frameworks/python) page.

## Troubleshooting

This section describes common erratic behaviors when migrating to Endpoints Frameworks version 2.0 and suggested solutions.

### API returns `404` errors, but API Explorer still lists APIs correctly

You are required to remove the old version 1.0 Endpoints configuration when migrating to Endpoints Frameworks version 2.0. If the old configuration is still present in the application's configuration, the Endpoints service continues to treat the app as a version 1.0 app. You might see requests in your App Engine logs sent to `/_ah/spi`, which result in `HTTP 404` errors sent to the client.

  1. Remove the following lines, from the `app.yaml` file if they are present:
         
         handlers:
         - url: /_ah/spi/.*
           script: ...
         

  2. Make sure the `handlers` section in your `app.yaml` file has the correct path:
         
         handlers:
         # The endpoints handler must be mapped to /_ah/api.
         - url: /_ah/api/.*
           script: ...
         




### Error message: `ImportError: cannot import name locked_file`

This happens if your dependencies contain a version of the `oauth2client` library that is incompatible with App Engine. See the [known issue](https://docs.cloud.google.com/endpoints/docs/frameworks/known-issues#error_message_importerror_cannot_import_name_locked_file).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
