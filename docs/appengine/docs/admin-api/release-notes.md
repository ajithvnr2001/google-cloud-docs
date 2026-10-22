---
url: https://docs.cloud.google.com/appengine/docs/admin-api/release-notes/
title: App Engine Admin API release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:08.883358+00:00
---

# App Engine Admin API release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/admin-api/release-notes)



Send feedback 

#  App Engine Admin API release notes Stay organized with collections  Save and categorize content based on your preferences. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/app-engine-admin-api-release-notes.xml) directly. 

## December 21, 2023

Change

A warning message now appears before you publish a container image to a public repository.

## March 06, 2020

Feature

App Engine is now available in the `us-west3 region` (Salt Lake City, Utah).

## February 11, 2020

Change

App Engine is changing the URLs that you use to send requests to your apps. URLs now [include a region ID](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id) to help Google route your requests more efficiently and reliably. For example, an app can receive requests at `https://PROJECT_ID.REGION_ID.r.appspot.com`. This new URL is optional for existing apps and is provided for all new apps.

To ensure a smooth transition, we are slowly updating App Engine to use region IDs. If we haven't updated your Google Cloud project yet, you won't see a region ID for your app. Since the ID is optional for existing apps, you don't need to update URLs or make other changes once the region ID is available for your existing apps.

## February 06, 2020

Deprecated

You can no longer apply new spending limits to projects. Existing spending limits will continue to work. For more information on how you can limit app costs, see [Limiting Costs](https://docs.cloud.google.com/appengine/docs/managing-costs).

## December 11, 2019

Feature

[Serverless VPC Access](https://docs.cloud.google.com/appengine/docs/standard/python/connecting-vpc) is now GA.

## July 30, 2019

Change

The functionalities of the App Engine SDK is delivered exclusively through [Cloud SDK](https://docs.cloud.google.com/sdk/docs). For more information, see [Migrating to Cloud SDK](https://docs.cloud.google.com/appengine/docs/standard/python/sdk-gcloud-migration).

Deprecated

The AppCfg tooling and the legacy standalone App Engine SDK, delivered through the `GoogleAppEngineLauncher.dmg`, `GoogleAppEngine.msi`, and `google_appengine.zip` files, are now deprecated. Google will shut down and remove support on July 30, 2020.

## April 18, 2019

Feature

App Engine is now available in the `asia-northeast2` region (Osaka, Japan).

## April 15, 2019

Feature

App Engine is now available in the `europe-west6` region (Zürich, Switzerland).

## April 09, 2019

Feature

[Serverless VPC Access](https://docs.cloud.google.com/appengine/docs/standard/python/connecting-vpc) is now in beta. Serverless VPC Access enables your app to connect to internal resources in your VPC network, such as Compute Engine VM instances, Cloud Memorystore instances, and more.

## December 21, 2018

Feature

Added `select`, `mmap`, `grp`, `fcntl`, `spwd` modules to the Python interpreter.

Feature

Added `fork`, `waitpid`, `chown`, `execv`, `fchmod`, `fchown`, `ftruncate`, `kill`, `lchown`, `lstat`, `readline`, `setuid` functions to the `os` module.

## December 14, 2018

Feature

The [Python 3.7 runtime](https://docs.cloud.google.com/appengine/docs/standard/python3) for the App Engine standard environment is now GA.

## December 12, 2018

Change

All apps have been switched to BSD network sockets. No changes to apps are required.

Feature

The [Sockets API](https://docs.cloud.google.com/appengine/docs/standard/python/sockets) is now GA.

## November 16, 2018

Change

nginx is now the default web server. No changes to apps are required.

## November 08, 2018

Fixed

Minor bug fixes.

## October 31, 2018

Feature

The Python 3 runtime supports recursive entries in the `requirements.txt` file.

## October 25, 2018

Fixed

Minor bug fixes.

## October 22, 2018

Feature

App Engine is now available in the `asia-east2` region (Hong Kong).

## October 15, 2018

Feature

All Python 2.7 apps now run on 64-bit Python interpreter.

Feature

All apps on the Python 2.7 runtime now run in the [gVisor sandbox](https://github.com/google/gvisor).

## September 26, 2018

Feature

Allow using locally installed `grpcio` as a workaround for import failures on dev_appserver.

## September 05, 2018

Change

Started rolling out [Cloud Datastore Emulator](https://docs.cloud.google.com/appengine/docs/standard/python/tools/migrate-cloud-datastore-emulator) as the default local datastore emulation when using the `dev_appserver` local development server.

## August 24, 2018

Deprecated

**Shutdown of Cloud Endpoints Frameworks v1 is approaching**

Cloud Endpoints Frameworks v1 for the App Engine standard environment was deprecated on August 2, 2017. The [service is scheduled to be shutdown](https://docs.cloud.google.com/appengine/docs/deprecations/endpoints-v1) on September 3, 2018, and the documentation will be removed. To avoid an outage, you must migrate your v1 application. For information on migrating your application to Endpoints Frameworks v2, see the [Python Migration Guide](https://docs.cloud.google.com/endpoints/docs/frameworks/python/migrating).

## August 14, 2018

Fixed

Minor bug fixes.

## August 08, 2018

Feature

A list of [differences between Python 2.7 and Python 3.7 runtimes](https://docs.cloud.google.com/appengine/docs/standard/python3/python-differences) is available.

Feature

The [Python 3.7 runtime](https://docs.cloud.google.com/appengine/docs/standard/python3) for the App Engine standard environment is now in beta.

## July 12, 2018

Feature

The [local development server](https://docs.cloud.google.com/appengine/docs/standard/go/tools/using-local-server) now prints the process ID of the running process on startup. You can use the process ID when debugging your app.

Fixed

Fix a crush that happened when dev_appserver speaked to a running Cloud Datastore Emulator. Previously, the crush happened when the environment variable "DATASTORE_PROJECT_ID" existed in the shell that ran dev_appserver.

## July 10, 2018

Feature

App Engine is now available in the `us-west2` region (Los Angeles).

## July 02, 2018

Fixed

Fixed a bug in [auto scaling configuration](https://docs.cloud.google.com/appengine/docs/standard/python/config/appref#scaling_elements) where App Engine was aggressively shutting down instances when the `max_instances` setting was used.

## June 28, 2018

Feature

Purged the `DATASTORE_PROJECT_ID` environment variable from the local development server (`dev_appserver`) process. Now `dev_appserver` can run alongside the Cloud Datastore Emulator.

Feature

The local development server will now print the process ID of the app process on startup.

## June 21, 2018

Fixed

Minor bug fixes.

## May 24, 2018

Feature

Migrated SSL library from version 2.7 to version 2.7.11 for all apps. See the [Python SSL version 2.7 shutdown docs](https://docs.cloud.google.com/appengine/docs/deprecations/python-ssl-27) details.

## May 17, 2018

Fixed

Minor bug fixes.

## May 15, 2018

Change

No more resident instances in auto scaling. Previously, if you used the `min_idle_instances` setting, the minimum idle instances were labelled as _Resident_ in the Cloud Console, with the remainder of the instances labelled as _Dynamic_. The new scheduler simply labels all instances as _Dynamic_ with auto scaling. However, the underlying behavior remains similar to previous behavior. If you use `min_idle_instances` and enable warmup requests, you will see at least that many dynamic instances running even during periods with no traffic.

For more details, see the [auto scaling documentation](https://docs.cloud.google.com/appengine/docs/standard/python/config/appref#scaling_elements).

Feature

New target CPU utilization setting lets you optimize between latency and cost.

Feature

New max instances setting allows you to cap the total number of instances to be scheduled.

Feature

New target throughput utilization setting lets you optimize for the number of concurrent requests at which new instances are started.

Feature

Completed a gradual rollout of an upgrade to the automatic scaling system:

Feature

New min instances setting allows you to specify a minimum number of instance to keep running for your app.

Feature

Improved efficiency resulting generally in lower instance cost (up to 6% reduction for many users) and up to 30% reduction for _loading requests_ , which are the first request to a new instance.

## April 11, 2018

Change

**Python runtime notes**

Feature

Added [PyTz version 2017.3](https://pypi.python.org/pypi/pytz/2017.3) to the built-in third-party libraries.

## April 03, 2018

Fixed

Minor bug fixes.

## January 23, 2018

Fixed

Fixes the [ipaddr library import issue](https://issuetracker.google.com/issues/71704025) when starting PHP app with the local development server.

## December 20, 2017

Feature

  * Added [SetupTools version 36.6.0](https://pypi.python.org/pypi/setuptools/36.6.0) to the built-in third-party libraries.



## December 14, 2017

Feature

  * Improved access control documentation around deploying apps with IAM roles and service accounts:

    * [Predefined App Engine roles](https://docs.cloud.google.com/appengine/docs/standard/python/access-control#predefined_app_engine_roles)
    * [Deploying using IAM roles](https://docs.cloud.google.com/appengine/docs/standard/python/granting-project-access#deploying_using_iam_roles)
    * [Require permissions](https://docs.cloud.google.com/appengine/docs/admin-api/access-control#required_permissions)



## December 09, 2017

Issue

**Known problem** : [Werkzeug 0.13 update adds a module that is not supported by App Engine](https://issuetracker.google.com/issues/70426718) that results in a `ImportError: cannot import name SpooledTemporaryFile` error. You can downgrade or pin your app to an earlier version of werkzeug to fix the error. See the linked issue for details.

## December 05, 2017

Feature

For all incoming HTTP requests, `dev_appserver.py` now requires that all HTTP requests must have an HTTP `Host` header and its value is either `localhost`, an IPv4 or IPv6 loopback address, or if specified, the value passed in via `--host`. For HTTP/1.0 only, requests with no `Host` header are still allowed. To disable host checking, set the `--enable_host_checking` flag to `false`. However, it is strongly recommended to leave host checking enabled, as it guards against DNS rebinding attacks.

Feature

Introduced additional security-header related behavior to the `dev_appserver.py` admin console: * Inbound requests containing an `Origin` header are rejected. * Added the following headers to all responses: * `X-Frame-Options=SAMEORIGIN` * `X-XSS-Protection=1; mode=block` * `Content-Security-Policy=default-src 'self'; frame-ancestors 'none'`

## November 15, 2017

Deprecated

Announced the [deprecation of the Python SSL library version 2.7](https://docs.cloud.google.com/appengine/docs/deprecations/python-ssl-27). Applications should migrate to use SSL version 2.7.11.

## October 31, 2017

Feature

App Engine is now available in the `asia-south1` region (Mumbai, India).

## October 25, 2017

Fixed

Minor bug fixes

## October 11, 2017

Feature

Announced general availability of [App Engine firewall](https://docs.cloud.google.com/appengine/docs/standard/python/creating-firewalls).

## September 21, 2017

Feature

Updated `pytz` to 2017.2

## September 13, 2017

Change

If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [upgrade to managed SSL certificates](https://docs.cloud.google.com/appengine/docs/standard/python/securing-custom-domains-with-ssl#updating_to_managed_ssl_certificates).

Feature

You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/standard/python/securing-custom-domains-with-ssl).

Feature

The `gcloud` commands and Admin API methods used to [map custom domains](https://docs.cloud.google.com/appengine/docs/standard/python/mapping-custom-domains) are now generally available. This includes [`gcloud domains verify`](https://docs.cloud.google.com/sdk/gcloud/reference/domains) and [`apps.authorizedDomains.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list). However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/standard/python/securing-custom-domains-with-ssl).

## September 05, 2017

Fixed

  * Release includes minor bug fixes.



Feature

App Engine is now available in the `southamerica-east1` region (São Paulo, Brazil).

## August 28, 2017

Change

This release does not include support for [Google Cloud Client Libraries](https://googleapis.github.io/google-cloud-python/) or for gRPC server requests.

Feature

This release adds client support for gRPC so that you can connect to gRPC servers from your App Engine application. For more information on how to request and install the `grpcio` library, see [Using third-party libraries](https://docs.cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27).

## August 01, 2017

Feature

App Engine is now available in the `europe-west3` region (Frankfurt, Germany).

## July 18, 2017

Feature

App Engine is now available in the `australia-southeast1` region (Sydney, Australia).

## June 27, 2017

Feature

Added Django v1.11 to the [built-in third-party libraries](https://docs.cloud.google.com/appengine/docs/standard/python/tools/built-in-libraries-27).

## June 21, 2017

Feature

Added the following new libraries to the built-in third party libraries:

  * ujson v1.35
  * lxml v3.7.3
  * flask v0.12.



Feature

Search API: increased the maximum [facet discovery value limit](https://docs.cloud.google.com/appengine/docs/standard/python/refdocs/google.appengine.api.search.search#google.appengine.api.search.search.FacetOptions) to 100.

## June 15, 2017

Change

For SSL `2.7.11`, if you don't specify the certificate root path, the default is set to `/etc/ca-certificates.crt`.

Feature

For MySQLdb, you can now use the `utf8mb4` character set.

Feature

You can use the [PWD module](https://docs.python.org/2/library/pwd.html) for the Unix password database.

## June 06, 2017

Feature

You can now use the beta-level features in the Admin API and `gcloud` command-line tool to [create and manage your custom domains and SSL certificates](https://docs.cloud.google.com/appengine/docs/standard/python/mapping-custom-domains).

Feature

App Engine is now available in the `europe-west2` region (London).

## May 15, 2017

Change

To ensure application compatibility, removed the fix for <https://bugs.python.org/issue22221> for the tokenizer, which would ensure PEP-263 is correctly handled.

Feature

Modified the SSL certificate validation behavior in the SSL module versioned as `2.7.11` to not validate certificates. This behavior can be controlled by an [environment variable](https://docs.cloud.google.com/appengine/docs/standard/python/config/appref#environment_variables) `PYTHONHTTPSVERIFY`, which can be set to `1` to require certificate validation.

Feature

Updated the Python runtime to Python 2.7.12.

## May 09, 2017

Feature

App Engine is now available in the `us-east4` region (North Virginia).

## April 27, 2017

Change

In preparation for the Go 1.8 beta, Go `api_version`s are mapped to specific `GOROOT` directories.

## April 05, 2017

Fixed

Fixed a bug preventing Server Name Indication (SNI) from working for remote API shell.

## March 20, 2017

Change

Support Server Name Indication (SNI) for remote API shell.

## January 23, 2017

Fixed

Fixed a bug that caused the `remote_api_shell.py` tool to not work on Cloud Shell.

## December 01, 2016

Feature

Includes pycrypto update to 2.6.1.

Feature

Includes pytz update to 2016.4.

## October 27, 2016

Deprecated

The Channel and XMPP services are now [deprecated](https://docs.cloud.google.com/appengine/docs/deprecations). These services will be turned down on October 31, 2017.

## August 01, 2016

Change

Version 1.9.42

Change

**Python 2 runtime notes**

  * This release does not include a new Python 2 SDK. Python 2 users should continue to use the 1.9.40 SDK.



Feature

**Admin API notes** * Version 1 of the [Admin API](https://docs.cloud.google.com/appengine/docs/admin-api) is now generally available.

## July 18, 2016

Change

LeaseTasksByTag requests will be limited to 25 requests per second.

Feature

Increases the maximum cron tasks limit to 250.

Change

Version 1.9.40 (Version 1.9.39 was skipped).

Feature

Server Errors and Client Errors now more accurately reflect per-URL status errors in the App Engine dashboard.

Feature

New [App Engine guided walkthrough](https://console.cloud.google.com/start/appengine) in the GCP Console. Pick your preferred language and launch an interactive tutorial directly in the console.

Feature

**Python runtime notes**

  * Python Endpoints accepts all valid Google ID token issuers.



## July 01, 2016

Feature

**Cloud Datastore**

New [Cloud Datastore Pricing](https://cloud.google.com/appengine/pricing#costs-for-datastore-calls) is now in effect.

## May 25, 2016

Feature

**Cloud Datastore**

  * When committing a cross-group transaction, version numbers returned for new or updated entities are all the same. With the previous behavior, entities within the same group committed as part of a cross-group transaction, had the same version number, but entities in different groups might have had different version numbers. This change ensures all new and updated entities have an identical version number, regardless of their entity group, when committed as part of a cross-group transaction. As before, entities that are not updated will not have a new version number.



Change

Version 1.9.38 released.

Change

The error returned by URL Fetch for a request to a port outside of the permitted ranges (80-90, 440-450, 1024-65535) will now always return `INVALID_URL` as documented.

## May 04, 2016

Fixed

General bug fixes and improvements.

Change

Version 1.9.37

Feature

**Python runtime notes**

  * Includes a new version of the third_party library "ssl" based on Python 2.7.11. The library can be selected with version: "2.7.11" in the [`libraries`](https://docs.cloud.google.com/appengine/docs/standard/python/config/appref#libraries) section of the `app.yaml` file.



## May 02, 2016

Feature

**App Engine flexible environment**

  * The [Ruby runtime](https://docs.cloud.google.com/appengine/docs/flexible/ruby) is now available for the App Engine flexible environment.



## April 18, 2016

Change

Version 1.9.36

Feature

In response to your requests, the App Engine Users API joins the rest of App Engine in supporting IAM roles and group expansion. This means that any user who is a project Owner, Editor or Viewer or an App Engine Admin is considered an "admin" by the Users API, regardless of whether the user was granted the role directly or by membership in a group. * This release populates error details, when available, in error messages associated with the "OverQuota" exception type.

Feature

**Python runtime notes**

  * Google no longer accepts quota increase requests for the mail service. Customers should use [Sendgrid](https://docs.cloud.google.com/appengine/docs/standard/python/mail/sendgrid) instead.



## March 24, 2016

Fixed

Fixes trace timestamps to match log timestamps.

Change

Version 1.9.35

Change

App Engine Managed VMs is renamed to [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible).

## March 04, 2016

Feature

Increases default quota for URL fetch for billed apps. Refer to the [Quotas page](https://docs.cloud.google.com/appengine/docs/quotas#UrlFetch) for details.

Change

Version 1.9.34

## February 17, 2016

Feature

The URL path "/form" is now allowed and will be forwarded to applications. Previously, this path was blocked.

Change

Version 1.9.33

## February 03, 2016

Change

Version 1.9.32

Feature

Container construction choices for Managed VMs

The `gcloud preview app deploy` (and `mvn gcloud:deploy`) commands upload your artifacts to our servers and build a container to deploy your app to the Managed VM environment.

There are two mechanisms for building the container image remotely. The default behavior is to build the container on a transient Compute Engine Virtual Machine which has Docker installed. Alternatively, you can use the [Cloud Build](https://docs.cloud.google.com/build/docs) service. To use the Cloud Build service, follow these steps: 1\. [Activate the Cloud Build API](https://support.google.com/cloud/answer/6158841) for your project. 2\. Use the command `gcloud config set app/use_cloud_build True`. This will cause all invocations of `gcloud preview app deploy` to use the service. (To return to the default behavior, use the command `gcloud config set app/use_cloud_build False`.

## January 14, 2016

Feature

App Engine now supports Google Groups: Adding a Google Group as a member of a project grants the members of the group access to App Engine. For example, if a Google Group is an Editor on a project, all members of the group now have Editor access to the App Engine application.

Change

Version 1.9.31

## November 30, 2015

Change

Version 1.9.30

Feature

**Python runtime notes**

  * Stackdriver Debugger is enabled automatically for Python applications running on App Engine. [Try it](https://docs.cloud.google.com/debugger/docs/setting-up-python-on-app-engine).



Feature

Headers for push queue requests made for Task Queue tasks with no payload will now contain a Content-Length entry set to '0'. Previously headers for such requests contained no Content-Length entry.

Change

Version 1.9.29

Feature

For developers using the [endpoints API](https://docs.cloud.google.com/appengine/docs/standard/python/endpoints/create_api#defining_the_api_endpointsapi), added a discoverable boolean parameter to the @Api annotation to allow users to disable API discovery. Using this feature will prevent some client libraries (e.g. JavaScript) and the API Explorer from working, as they depend on discovery.

Feature

Stop calculating and storing queue depth for non-existent queues, queues marked for deletion, and in the case of queue table outages.

## October 29, 2015

Deprecated

The Prospective Search API, which was deprecated on July 14, 2015, is now restricted to existing users. It will fully shutdown on December 1, 2015.

Feature

Improved accuracy of Geo filtering in Search queries.

Change

**Python runtime notes**

  * Allow use of quoted numbers within comparison clauses of Search queries. 
  * https://issuetracker.google.com/issues/35899722



Change

Version 1.9.28

## September 25, 2015

Fixed

Bugfix: Repeated numeric facets are now allowed.

Change

Datastore

Feature

Applications that are newly enabled for billing now default to an unlimited daily budget, and no longer default to a maximum daily budget of $0. This prevents unwanted outages due to running out of budget. To set a ceiling on your application's daily cost, after you enable billing, set a budget in the [app engine settings](https://console.cloud.google.com/project/_/appengine/settings). For more information, see [Setting a daily budget](https://docs.cloud.google.com/appengine/docs/developers-console#setting_a_daily_budget).

Change

Version 1.9.27

Feature

Faceted Search is now GA.

## August 27, 2015

Feature

oauth2client library upgraded to version [1.4.2](https://github.com/google/oauth2client/blob/master/CHANGELOG.md)

Feature

Use RequestPayloadTooLargeException for URLFetch requests with payloads that are too large.

Feature

Remote API can now be accessed using OAuth2 credentials using https://developers.google.com/identity/protocols/application-default-credentials

Feature

Adds "show in context" menu for MVM application logs that have thread_id or request_id as a field in their log entry. This allows sorting app logs based on either field.

Feature

Capability to provision applications for current load and configure elastic provisioning based on both VM and application level metrics.

Change

Version 1.9.26

## August 14, 2015

Change

Version 1.9.25

Feature

Datastore now allows properties to represent the empty list.

Feature

Admin Console menus start redirecting to GCP Console. Select services such as the Admin Logs will continue to be available in the Admin Console.

Feature

Added PyAMF version 0.7.2 (Beta).

Feature

Failed tasks in queues configured with a `retry_limit` of zero will no longer be retried.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
