---
url: https://docs.cloud.google.com/appengine/docs/flexible/go/release-notes/
title: App Engine flexible environment for Go release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:33:24.310842+00:00
---

# App Engine flexible environment for Go release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/go/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/flexible/resources)



Send feedback 

#  App Engine flexible environment for Go release notes Stay organized with collections  Save and categorize content based on your preferences. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gaeflex-go-release-notes.xml) directly. 

## September 29, 2026

Feature

App Engine permanently blocks insecure traffic with TLS version 1.1 and earlier. For `appspot.com` domains, this block occurs at the connection level. For custom domains, the connection might succeed, but the requests are blocked. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls).

## September 01, 2026

Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

## August 20, 2026

Feature

Starting from August 2026, to provide modern security patches and support for MySQL 8.4 and later, the App Engine flexible environment uses Cloud SQL Auth Proxy v2 as the built-in sidecar container for connections to Cloud SQL. To use the latest Cloud SQL Auth Proxy container immediately, restart your VMs or deploy a new version of your application.

## August 19, 2026

Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

Feature

Starting from Go runtime version 1.26 and later, the lifecycle support dates align more closely with the [Go community release cycle](https://go.dev/wiki/Go-Release-Cycle). For more information, see [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go).

## August 14, 2026

Feature

To improve security, starting in August 2026, App Engine opts your application into TLS version 1.2 and later. You can opt out until the end of August 2026. Starting in September 2026, App Engine might permanently block insecure traffic with TLS version 1.1 and earlier. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls).

## June 29, 2026

Feature

Support for deploying your existing apps in the flexible environment to Cloud Run using the `gcloud beta app migrate-to-run` command is in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Deploy an App Engine app in the flexible environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-flexible-to-run).

## March 12, 2026

Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## February 19, 2026

Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## October 20, 2025

Feature

[Support for TLS version 1.2 and later](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls), along with a corresponding secure set of cipher suites, is in General Availability (GA).

## August 21, 2025

Feature

Support for [Go 1.25 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

## August 07, 2025

Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls) in the App Engine flexible environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

## July 30, 2025

Feature

Support for [Go 1.25 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages). This runtime is available for early testers using existing [release candidates](https://go.dev/dl/#unstable).

Feature

Support for [Go 1.24 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

## July 15, 2025

Feature

Support for [Go 1.24 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## March 18, 2025

Announcement

Container Registry is now [shut down](https://docs.cloud.google.com/artifact-registry/docs/transition/prepare-gcr-shutdown). We recommend that you use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) for storing and managing container images. By default, new deployments created after March 5, 2025, use Artifact Registry instead of Container Registry for storing application build images. For more information, see [Migrate App Engine container images to Artifact Registry](https://docs.cloud.google.com/appengine/migration-center/migrate-to-artifact-registry).

## March 03, 2025

Feature

[Go 1.23](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now [ generally available](https://cloud.google.com/products/#product-launch-stages).

## November 19, 2024

Feature

[Go 1.23](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now available [in preview](https://cloud.google.com/products/#product-launch-stages).

## July 30, 2024

Feature

In the App Engine page in the Google Cloud console, you can now filter your existing App Engine versions by [runtime lifecycle stages](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle). After you apply this filter, the console displays a warning icon for App Engine versions that are approaching end of support, have reached end of support, are deprecated, and are decomissioned.

## July 12, 2024

Announcement

Deployments for new projects might be impacted from the following changes to org policies:

  * Starting in May 2024, Google Cloud enforces [secure-by-default organization policies](https://resource-manager/docs/secure-by-default-organizations) for all organization resources. This policy prevents App Engine from granting the `Editor` role to the App Engine default services accounts by default.
  * Starting in June 2024, Cloud Build has changed the default behavior for how Cloud Build uses service accounts in new projects. This change is detailed in [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates). As a result of this change, new projects deploying versions for the first time may be using the default App Engine service account with [insufficient permissions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants%22) for deploying versions. 



If you are impacted by this change, you can do the following:

  * Review the Cloud Build guidance on changes to the default service account and [opt out of these changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).
  * Grant the [Editor](https://docs.cloud.google.com/appengine/docs/flexible/roles) role to the App Engine default service account.



## July 10, 2024

Announcement

Go version 1.19 and earlier have reached [end of support](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle#end_of_support). You cannot re-deploy versions that use runtimes [after their end of support date](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go). We recommend that you upgrade your app to use the [latest version of Go](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime#newversions).

## March 26, 2024

Feature

[Go 1.22](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now [ generally available](https://cloud.google.com/products/#product-launch-stages). 

Starting in Go version 1.22 and later:

  * You can't use `go get` outside of a module in the legacy `GOPATH` mode (`GO111MODULE=off`).
  * Go recommends that you use a `go.mod` file for managing dependencies. 



For more information, see [Specify dependencies](https://docs.cloud.google.com/appengine/docs/standard/go/specifying-dependencies).

## February 26, 2024

Feature

[Go 1.22](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now available in [preview](https://cloud.google.com/products/#product-launch-stages).

## December 21, 2023

Change

A warning message now appears before you publish a container image to a public repository.

## September 08, 2023

Feature

[Go 1.21](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## August 14, 2023

Feature

[Go 1.21](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now available in [preview](https://cloud.google.com/products/#product-launch-stages).

## August 07, 2023

Change

Accessing a service that's prohibited by the **Internal** or **Internal and Cloud Load Balancing** [ingress setting](https://docs.cloud.google.com/appengine/docs/flexible/ingress-settings) now results in a `404` rather than `403` error code.

## April 28, 2023

Feature

You can now specify version "`1.20`" in the `runtime_version` setting of your `app.yaml` file. [Learn more](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime#newversion).

## March 24, 2023

Feature

You can now use `ssh` to log in to App Engine flexible environment instances that use only [internal IP addresses](https://docs.cloud.google.com/appengine/docs/flexible/disable-external-ip).

## March 23, 2023

Feature

[Go 1.18 and 1.19](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) are now [generally available](https://cloud.google.com/products/#product-launch-stages). These versions require you to specify an operating system version in your app.yaml. [Learn more](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime#newversions).

## February 21, 2023

Feature

The [Go runtime versions 1.18 and 1.19](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) are now available in [preview](https://cloud.google.com/products/#product-launch-stages) and are built on a modern and secure operating system (Ubuntu 22). These new runtime versions use Google Cloud's [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) and require updates to your app.yaml. [Learn more](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime#go_versions).

## December 13, 2022

Feature

You can now use any configured [service account](https://docs.cloud.google.com/iam/docs/service-accounts) in your Cloud project as the [app-level default service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts), while creating and updating your App Engine applications.

## November 09, 2022

Feature

The option to set [IP mode to `internal`](https://cloud.google.com/appengine/docs/flexible/troubleshooter/connectivity-questions#virtual_machines_with_only_internal_ip_addresses_require) for App Engine flexible environment instances is now generally available.

## May 23, 2022

Feature

You can now disable external ephemeral IP addresses for App Engine Flex services. Read our documentation to [learn how](https://docs.cloud.google.com/appengine/docs/flexible/go/disable-external-ip). This feature is at the [Preview](https://cloud.google.com/products/#product-launch-stages) launch stage.

## May 18, 2022

Feature

Specifying a [user-managed service account](https://docs.cloud.google.com/appengine/docs/flexible/go/user-managed-service-accounts) for each App Engine version during deployment is now [generally available](https://cloud.google.com/products/#general-availability).

## July 19, 2021

Feature

Specifying a [user-managed service account](https://docs.cloud.google.com/appengine/docs/flexible/go/user-managed-service-accounts) for each App Engine version during deployment is now available in preview. This feature lets you grant different privileges to each version, based on the specific tasks it performs, and avoid granting more privileges than necessary.

## June 30, 2021

Change

Requests from internal services to the App Engine flexible environment no longer originate from `10.0.0.1`. The IP ranges are as follows: \- Cron requests from newly created or updated App Engine Cron jobs sent to the App Engine flexible environment now come from `0.1.0.2`. For Cron jobs created with older gcloud versions (earlier than 326.0.0), Cron requests will come from `0.1.0.1`. Previously, these requests only came from both `0.1.0.1` and `10.0.0.1`. \- For other Cloud Scheduler jobs and Cloud Tasks queues (including App Engine Task Queues), requests sent to the App Engine flexible environment now only come from `0.1.0.2`. Previously, these requests came from both `0.1.0.2` and `10.0.0.1`. \- For URL Fetch, requests sent to the App Engine flexible environment now only come from `0.1.0.40`. Previously, these requests came from both `0.1.0.40` and `10.0.0.1`.

For more information, see [Understanding the App Engine firewall](https://docs.cloud.google.com/appengine/docs/flexible/go/understanding-firewalls).

## June 14, 2021

Feature

App Engine is now available in the `us-west1` (Oregon), `asia-southeast1` (Singapore), and `asia-east1` (Taiwan) regions.

## April 13, 2021

Feature

App Engine is now available in the `europe-central2` region (Warsaw).

## November 12, 2020

Change

You can use [network ingress controls](https://docs.cloud.google.com/appengine/docs/flexible/go/application-security#ingress_controls) so your app only receives requests that are sent from your project's VPC or that are routed through the Cloud Load Balancing load balancer. This feature is now generally available.

## September 25, 2020

Feature

You can use [network ingress controls](https://docs.cloud.google.com/appengine/docs/flexible/go/application-security#ingress_controls) so your app only receives requests that are sent from your project's VPC or that are routed through the Cloud Load Balancing load balancer.

## July 08, 2020

Feature

External HTTP(S) Load Balancing is now supported for App Engine via [Serverless network endpoint groups](https://load-balancing/docs/negs/setting-up-serverless-negs). Notably, this feature allows you to use [Cloud CDN](https://docs.cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

## June 08, 2020

Feature

App Engine is now available in the `asia-southeast2` region (Jakarta).

## May 14, 2020

Feature

To get a fine-grained view of billing data for each resource used by your App Engine services, you can apply labels to the services, export your billing data to BigQuery, and run queries. For more information, see [Labeling App Engine resources](https://docs.cloud.google.com/appengine/docs/flexible/go/labeling-resources).

## April 20, 2020

Feature

App Engine is now available in the `us-west4` region (Las Vegas, NV).

## April 13, 2020

Change

Quotas for sockets have been removed. There is no longer a limit on the number of socket connections or the amount of data you can send and receive through a socket.

## March 13, 2020

Feature

App Engine is now available in the `asia-northeast3` region (Seoul).

## March 06, 2020

Feature

App Engine is now available in the `us-west3 region` (Salt Lake City, Utah).

## February 11, 2020

Feature

App Engine is changing the URLs that you use to send requests to your apps. URLs now [include a region ID](https://docs.cloud.google.com/appengine/docs/flexible/go/how-requests-are-routed#region-id) to help Google route your requests more efficiently and reliably. For example, an app can receive requests at `https://PROJECT_ID.REGION_ID.r.appspot.com`. This new URL is optional for existing apps and is provided for all new apps.

To ensure a smooth transition, we are slowly updating App Engine to use region IDs. If we haven't updated your Google Cloud project yet, you won't see a region ID for your app. Since the ID is optional for existing apps, you don't need to update URLs or make other changes once the region ID is available for your existing apps.

## April 18, 2019

Feature

  * App Engine is now available in the `asia-northeast2` region (Osaka, Japan).



## April 15, 2019

Feature

  * App Engine is now available in the `europe-west6` region (Zürich, Switzerland).



## April 09, 2019

Feature

[Cloud Tasks](https://docs.cloud.google.com/tasks/docs) is now GA and can be used to set up tasks to be performed asychronously, outside of user requests.

## March 04, 2019

Feature

[Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs) is now GA and can be used to set up scheduled units of work (cron jobs).

## October 22, 2018

Feature

  * App Engine is now available in the `asia-east2` region (Hong Kong).



## October 11, 2018

Feature

  * The default App Engine flexible environment [Go runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now Go 1.11.



## August 01, 2018

Feature

  * Support for Go 1.8 on App Engine is now [deprecated](https://docs.cloud.google.com/appengine/docs/deprecations).



Deprecated

  * New Go 1.6 and Go 1.8 app deployments will not be possible from November 1, 2018.



## July 10, 2018

Feature

  * App Engine is now available in the `us-west2` region (Los Angeles).



## March 28, 2018

Feature

  * Go 1.10 speeds up builds and includes minor changes throughout the standard library. Changes to the `bytes` and `net/url` packages require some code changes. For details, see the [Go 1.10 release page](https://golang.org/doc/go1.10).



Feature

  * You can submit feedback to the [google-appengine-go](https://groups.google.com/forum/#!forum/google-appengine-go) Google Group.



Change

  * Support is still available for the existing Go 1.9 and 1.8 runtimes.



Feature

  * The Go runtime now defaults to the latest Go release, version 1.10, for deployments specifying [`runtime: go`](https://docs.cloud.google.com/appengine/docs/flexible/go/reference/app-yaml#general) in your `app.yaml` configuration file.



Feature

**Go runtime notes**

## February 14, 2018

Feature

The build pipeline is now generally available (GA):

Feature

  * Produces an application image with [gcr.io/distroless/base](https://github.com/GoogleCloudPlatform/distroless/tree/master/base) as the base image.



The distroless base image contains a minimal Linux, glibc-based system. The application image does not use the Debian Linux distribution, reducing the image size by ~390MB.

Please send feedback to the [Google App Engine Go Group](https://groups.google.com/forum/#!forum/google-appengine-go).

Feature

  * You can build your application with a specific Go runtime version. Specifying `runtime: go` in your `app.yaml` file uses the latest supported runtime version release, which is currently Go 1.9.



## January 10, 2018

Feature

  * App Engine is now available in the `northamerica-northeast1` region (Montréal, Canada).



## December 14, 2017

Feature

  * Improved access control documentation around deploying apps with IAM roles and service accounts:

    * [Predefined App Engine roles](https://docs.cloud.google.com/appengine/docs/flexible/go/access-control#predefined_app_engine_roles)
    * [Deploying using IAM roles](https://docs.cloud.google.com/appengine/docs/flexible/go/granting-project-access#deploying_using_iam_roles)
    * [Require permissions](https://docs.cloud.google.com/appengine/docs/admin-api/access-control#required_permissions)



## October 31, 2017

Feature

  * App Engine is now available in the `asia-south1` region (Mumbai, India).



## October 11, 2017

Feature

  * Announced general availability of [App Engine firewall](https://docs.cloud.google.com/appengine/docs/flexible/go/creating-firewalls).



## October 02, 2017

Feature

  * For the App Engine flexible environment, all responses are now compressed with gzip by default once you redeploy your app. No changes need to be made to your `app.yaml` file.



## September 27, 2017

Feature

The beta build pipeline has been updated:

Feature

  * Produces an application image with [gcr.io/distroless/base](https://github.com/GoogleCloudPlatform/distroless/tree/master/base) as the base image. This affects only new deployments, deployed with the `gcloud beta app deploy` command.



The distroless base image contains a minimal Linux, glibc-based system. The application image will no longer contain the Go SDK or Debian utilities, reducing the image size by ~390MB. If your applications rely on these at runtime, let us know at [google-appengine-go](https://groups.google.com/forum/#!forum/google-appengine-go).

To try out the new beta build pipeline, ensure you are running `gcloud` 173.0.0 or later and invoke `gcloud beta app deploy`. Optionally, specify a supported Go version in your `app.yaml` file. You can use the existing build pipeline by running `gcloud app deploy`.

Feature

  * Developers can now build their applications with a specific Go runtime version. For the beta build pipeline, specifying `runtime: go` in your `app.yaml` file will use the latest supported runtime version release, which is currently Go 1.9.



## September 26, 2017

Feature

  * For the App Engine flexible environment, billing increments for instances are reduced from per-minute increments to per-second increments. Additionally, the minimum usage cost for instance resources is reduced from 10 minutes to 1 minute.



## September 18, 2017

Change

  * [Updated health checks](https://docs.cloud.google.com/appengine/docs/flexible/go/reference/app-yaml#updated_health_checks) are now the default for new projects. To upgrade a project from legacy health checks, run the command `gcloud app update --split-health-checks`.



Deprecated

  * Legacy health checks will no longer be available after September 30th, 2018.



## September 13, 2017

Feature

  * The `gcloud` commands and Admin API methods used to [map custom domains](https://docs.cloud.google.com/appengine/docs/flexible/go/mapping-custom-domains) are now generally available. This includes [`gcloud domains verify`](https://docs.cloud.google.com/sdk/gcloud/reference/domains) and [`apps.authorizedDomains.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list). However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/flexible/go/securing-custom-domains-with-ssl).



Feature

  * If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [upgrade to managed SSL certificates](https://docs.cloud.google.com/appengine/docs/flexible/go/securing-custom-domains-with-ssl#updating_to_managed_ssl_certificates).



Feature

  * You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/flexible/go/securing-custom-domains-with-ssl).



## September 05, 2017

Feature

  * App Engine is now available in the `southamerica-east1` region (São Paulo, Brazil).



## August 23, 2017

Feature

  * Beta release of the [App Engine firewall](https://docs.cloud.google.com/appengine/docs/flexible/go/creating-firewalls).



## August 01, 2017

Feature

  * App Engine is now available in the `europe-west3` region (Frankfurt, Germany).



## July 18, 2017

Feature

  * App Engine is now available in the `australia-southeast1` region (Sydney, Australia).



## July 12, 2017

Feature

  * You can now use updated health checks, which allow you to use separate checks to confirm that your instance is running and ready to serve content. You must enable updated health checks, which are currently in Beta. For more information, see [Health checks](https://docs.cloud.google.com/appengine/docs/flexible/go/configuring-your-app-with-app-yaml#health_checks).
  * If you use updated health checks, deployments will fail if your application does not reach a ready state.



## June 06, 2017

Feature

  * App Engine is now available in the `europe-west2` region (London).



Feature

  * You can now use the beta-level features in the Admin API and `gcloud` command-line tool to [create and manage your custom domains and SSL certificates](https://docs.cloud.google.com/appengine/docs/flexible/go/using-custom-domains-and-ssl) .



## May 09, 2017

Feature

  * App Engine is now available in the `us-east4` region (North Virginia).



## April 11, 2017

Change

  * Added [information](https://docs.cloud.google.com/appengine/docs/flexible/go/upgrading) about upgrading from the App Engine Task Queue API in the compat runtimes to using Cloud Tasks in the flexible environment and added information for how to verify requests from the Task Queue API.



## March 28, 2017

Feature

  * The flexible environment is now available in the [`europe-west` region](https://docs.cloud.google.com/appengine/docs/locations).



## March 09, 2017

Feature

  * The [.NET core runtime](https://docs.cloud.google.com/appengine/docs/flexible/dotnet) for the App Engine flexible environment is now in Beta.



Feature

  * The App Engine flexible environment is now generally available (GA). You can run Node.js, Ruby, Python, Java, and Go applications with a [99.95% SLA](https://cloud.google.com/appengine/sla).



Feature

  * The [PHP 7 runtime](https://docs.cloud.google.com/appengine/docs/flexible/php) for the App Engine flexible environment is now in Beta.



## December 06, 2016

Change

  * New applications that have not been deployed in the flexible environment must specify `env: true` in the `app.yaml` file instead of `vm:true`. Applications that were previously deployed can continue to use `vm:true` but will need to switch to `env:true` in the future. For more details, see [upgrade guide](https://docs.cloud.google.com/appengine/docs/flexible/go/upgrading).



## November 15, 2016

Feature

This release includes a few key new features:

  * Multi-zonal deployment support.
  * A modern networking stack with increased throughput.
  * Custom machine types.
  * Asia-Northeast1 region availability.



Feature

There is a new release of the App Engine flexible environment. To choose this environment, use `env:flex` instead of `vm:true` in your `app.yaml` configuration file. You can learn more about the details of this release by visiting the [upgrade guide](https://docs.cloud.google.com/appengine/docs/flexible/go/upgrading).

Change

There are also a few breaking changes:

  * HTTP headers have been changed.
  * Environment variables have been changed.
  * There are multiple changes to the `app.yaml` schema.



For details and a full list of changes, visit the [upgrade guide](https://docs.cloud.google.com/appengine/docs/flexible/go/upgrading).

Deprecated

This release also marks the deprecation of a few features:

  * The python-compat runtime.
  * The python27 runtime.
  * The java-compat runtime.
  * The jetty9-compat runtime.
  * The [Go App Engine package](https://github.com/golang/appengine) no longer works on the App Engine flexible environment. Instead, use the [`cloud.google.com/go/...` package](https://github.com/GoogleCloudPlatform/google-cloud-go).



## May 02, 2016

Feature

  * The [Ruby runtime](https://docs.cloud.google.com/appengine/docs/flexible/ruby) is now available for the App Engine flexible environment.



## March 24, 2016

Change

  * App Engine Managed VMs is renamed to [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible).



## February 03, 2016

Feature

  * Container construction choices for Managed VMs

The `gcloud preview app deploy` (and `mvn gcloud:deploy`) commands upload your artifacts to our servers and build a container to deploy your app to the Managed VM environment.

There are two mechanisms for building the container image remotely. The default behavior is to build the container on a transient Compute Engine Virtual Machine which has Docker installed. Alternatively, you can use the [Cloud Build](https://docs.cloud.google.com/build/docs) service, which is in Beta. To use the Cloud Build service, follow these steps:

    1. [Activate the Cloud Build API](https://support.google.com/cloud/answer/6158841) for your project.
    2. Use the command `gcloud config set app/use_cloud_build True`. This will cause all invocations of `gcloud preview app deploy` to use the service. To return to the default behavior, use the command `gcloud config set app/use_cloud_build False`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
