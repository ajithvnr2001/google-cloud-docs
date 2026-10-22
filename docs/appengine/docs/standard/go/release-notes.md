---
url: https://docs.cloud.google.com/appengine/docs/standard/go/release-notes/
title: App Engine standard environment for Go 1.12+ release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:08.060502+00:00
---

# App Engine standard environment for Go 1.12+ release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/standard/resources)



Send feedback 

#  App Engine standard environment for Go 1.12+ release notes Stay organized with collections  Save and categorize content based on your preferences. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gaestd-go-release-notes.xml) directly. 

## September 29, 2026

Feature

App Engine permanently blocks insecure traffic with TLS version 1.1 and earlier. For `appspot.com` domains, this block occurs at the connection level. For custom domains, the connection might succeed, but the requests are blocked. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls).

## September 01, 2026

Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

## August 19, 2026

Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

Feature

Starting from Go runtime version 1.26 and later, the lifecycle support dates align more closely with the [Go community release cycle](https://go.dev/wiki/Go-Release-Cycle). For more information, see [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#go).

Feature

You can migrate your App Engine push queues to Cloud Tasks by updating the bundled services SDK. This method lets you upgrade your app without needing to modify your application code. For more information on how to migrate, see the [push queues migration guide](https://docs.cloud.google.com/appengine/migration-center/standard/go/migrating-push-queues-upgrade-sdk) ([Preview](https://cloud.google.com/products/#product-launch-stages)).

## August 14, 2026

Feature

To improve security, starting in August 2026, App Engine opts your application into TLS version 1.2 and later. You can opt out until the end of August 2026. Starting in September 2026, App Engine might permanently block insecure traffic with TLS version 1.1 and earlier. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls).

## July 29, 2026

Feature

Support for enabling only needed legacy bundled services using the [`app_engine_bundled_services`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=go#app_engine_bundled_services) field is in [General Availability](https://cloud.google.com/products/#product-launch-stages).

## June 03, 2026

Feature

App Engine supports [Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc) in [Preview](https://cloud.google.com/products#product-launch-stages). Direct VPC egress lets your workloads access VPC network resources as a simpler, more cost-effective [alternative to Serverless VPC Access connectors](https://docs.cloud.google.com/appengine/docs/standard/compare-direct-vpc-egress-connectors).

## May 27, 2026

Feature

Enable only needed legacy bundled services using the [`app_engine_bundled_services`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=go#app_engine_bundled_services) field for improved security and maintainability of your applications ([Preview](https://cloud.google.com/products/#product-launch-stages)).

## May 21, 2026

Feature

The App Engine Migration hub lets you migrate services in the App Engine standard environment to Cloud Run, and also provides cost-saving recommendations. For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-to-run) ([Preview](https://cloud.google.com/products?e=48754805#product-launch-stages)).

## March 12, 2026

Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## February 19, 2026

Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## February 12, 2026

Feature

Support for deploying your existing apps in the standard environment to Cloud Run using the `gcloud beta app migrate-to-run` command is in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-to-run).

## January 31, 2026

Deprecated

Go 1.11 is [deprecated](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#deprecated). You won't be able to deploy Go 1.11 applications, even if your organization previously used an organization policy to re-enable deployments of legacy runtimes. Your existing Go 1.11 applications will continue to run and receive traffic. We recommend that you [migrate to the latest supported version of Go](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/go-differences).

## October 20, 2025

Feature

[Support for TLS version 1.2 and later](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls), along with a corresponding secure set of cipher suites, is in General Availability (GA).

## August 21, 2025

Feature

Support for [Go 1.25 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

## August 07, 2025

Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls) in the App Engine standard environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

## July 30, 2025

Feature

Support for [Go 1.24 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

Feature

Support for [Go 1.25 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages). This runtime is available for early testers using existing [release candidates](https://go.dev/dl/#unstable).

## July 15, 2025

Feature

Support for [Go 1.24 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## March 18, 2025

Announcement

Container Registry is now [shut down](https://docs.cloud.google.com/artifact-registry/docs/transition/prepare-gcr-shutdown). We recommend that you use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) for storing and managing container images. By default, new deployments created after March 5, 2025, use Artifact Registry instead of Container Registry for storing application build images. For more information, see [Migrate App Engine container images to Artifact Registry](https://docs.cloud.google.com/appengine/migration-center/migrate-to-artifact-registry).

## March 03, 2025

Feature

[Go 1.23](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is now [ generally available](https://cloud.google.com/products/#product-launch-stages).

Feature

For new projects you create after March 2025, App Engine sets the automatic scaling maximum instances default for standard environment deployments to 20. This change doesn't impact existing apps. To override the default, specify a new [`max_instances`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements) value in your `app.yaml` file, and deploy a new version or redeploy over an existing version.

## December 09, 2024

Feature

[Custom organization policies](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#custom-constraints) for Serverless VPC Access connectors are now [generally available](https://cloud.google.com/products/#product-launch-stages), and can be applied to projects, folders, or organizations.

## November 19, 2024

Feature

[Go 1.23](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is now available [in preview](https://cloud.google.com/products/#product-launch-stages).

## July 30, 2024

Feature

In the App Engine page in the Google Cloud console, you can now filter your existing App Engine versions by [runtime lifecycle stages](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle). After you apply this filter, the console displays a warning icon for App Engine versions that are approaching end of support, have reached end of support, are deprecated, and are decomissioned.

## July 12, 2024

Announcement

Deployments for new projects might be impacted from the following changes to org policies:

  * Starting in May 2024, Google Cloud enforces [secure-by-default organization policies](https://resource-manager/docs/secure-by-default-organizations) for all organization resources. This policy prevents App Engine from granting the `Editor` role to the App Engine default services accounts by default.

  * Starting in June 2024, Cloud Build has changed the default behavior for how Cloud Build uses service accounts in new projects. This change is detailed in [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates). As a result of this change, new projects deploying versions for the first time may be using the default App Engine service account with [insufficient permissions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants%22) for deploying versions. 




If you are impacted by this change you can do one of the following:

  * Grant the [Editor](https://docs.cloud.google.com/appengine/docs/standard/roles) role to the App Engine default service account.

  * Review the Cloud Build guidance on changes to the default service account and [opt out of these changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).




## March 26, 2024

Feature

[Go 1.22](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is now [ generally available](https://cloud.google.com/products/#product-launch-stages). 

Starting in Go version 1.22 and later:

  * You can't use `go get` outside of a module in the legacy `GOPATH` mode (`GO111MODULE=off`).
  * Go recommends that you use a `go.mod` file for managing dependencies. 



For more information, see [Specify dependencies](https://docs.cloud.google.com/appengine/docs/standard/go/specifying-dependencies).

## March 12, 2024

Breaking

You can't use the latest version of `dev_appserver.py` to locally run your applications for runtimes that reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule). To continue using an archived version of `dev_appserver.py`, see [Use the local development server after runtimes reach the end of support](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server-for-eos-runtimes).

## February 26, 2024

Feature

[Go 1.22](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is now available [in preview](https://cloud.google.com/products/#product-launch-stages).

## January 30, 2024

Announcement

Go 1.12, 1.13, 1.14, 1.15, 1.16, and 1.18 have reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#end_of_support) on January 30, 2024. Your existing applications using these versions will continue to run and receive traffic. However, App Engine might block re-deployments of applications that use runtimes [after their end of support date](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#go). We recommend that you [migrate to the latest supported version of Go](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/go-differences).

## January 23, 2024

Feature

The option to [update a Serverless VPC Access connector](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#update-connector) is now available at general availability (GA). This feature allows you to edit the machine (instance) type, as well as the minimum and maximum number of instances.

## December 21, 2023

Change

A warning message now appears before you publish a container image to a public repository.

## September 14, 2023

Feature

[Go 1.21](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## August 14, 2023

Feature

[Go 1.21](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is now available [in preview](https://cloud.google.com/products/#product-launch-stages).

## August 07, 2023

Change

Accessing a service that's prohibited by the **Internal** or **Internal and Cloud Load Balancing** [ingress setting](https://docs.cloud.google.com/appengine/docs/standard/ingress-settings) now results in a `404` rather than `403` error code.

## May 01, 2023

Change

[Memory limits](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) for second-generation runtimes have been increased to better support the growing memory utilization of many newer runtimes.

## April 27, 2023

Feature

The [Search API](https://docs.cloud.google.com/appengine/docs/standard/services/search?tab=go) is now available in the [App Engine legacy bundled services for second-generation runtimes](https://docs.cloud.google.com/appengine/docs/standard/services/overview?tab=go#top). Access this legacy bundled service through the [App Engine services SDK for Go 1.12+](https://docs.cloud.google.com/appengine/docs/standard/go/services/access).

## April 18, 2023

Change

If you use the local development server to simulate an App Engine app in production, you must now run `dev_appserver.py` with Python 3 and set the `CLOUDSDK_DEVAPPSERVER_PYTHON` environment variable in your shell to the path of your Python 2 interpreter. Learn more about the [required setup steps](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server).

Change

Updated the Go SDK to version 1.9.75.

## March 24, 2023

Feature

The [Go 1.20 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) for App Engine standard environment is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## February 13, 2023

Feature

The [Go 1.20 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) for App Engine standard environment is now available in [preview](https://cloud.google.com/products/#product-launch-stages).

## January 17, 2023

Feature

The [Go 1.18 and Go 1.19 ](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) runtimes for App Engine standard environment are now [generally available](https://cloud.google.com/products/#product-launch-stages).

## December 21, 2022

Feature

The option to [update a Serverless VPC Access connector](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#update-connector) is now available in preview. This feature allows you to edit the machine (instance) type, as well as the minimum and maximum number of instances.

## December 13, 2022

Feature

You can now use any configured [service account](https://docs.cloud.google.com/iam/docs/service-accounts) in your Cloud project as the [app-level default service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts), while creating and updating your App Engine applications.

## December 07, 2022

Feature

The [Go 1.18 and Go 1.19 runtimes](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) for App Engine standard environment are now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

## November 01, 2022

Feature

[Build environment variables](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#build-env-vars) support is now generally available.

## May 18, 2022

Feature

Specifying a [user-managed service account](https://docs.cloud.google.com/appengine/docs/standard/go112/user-managed-service-accounts) for each App Engine version during deployment is now [generally available](https://cloud.google.com/products/#general-availability).

## April 13, 2022

Feature

The [App Engine legacy bundled services for Go 1.12+](https://docs.cloud.google.com/appengine/docs/standard/go/bundled-services-overview) are now available at the [General Availability release level](https://cloud.google.com/products/#product-launch-stages). These [APIs](https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest) can be [accessed](https://docs.cloud.google.com/appengine/docs/standard/go/services/access) through language-idiomatic libraries. Calls to these API are billed according to the standard rates.

## March 24, 2022

Feature

Support for Serverless VPC Access connectors in Shared VPC host projects is now at general availability (GA). Learn about the [advantages](https://docs.cloud.google.com/appengine/docs/standard/go/connecting-shared-vpc#host-project) of this method and how to [configure connectors in host projects](https://docs.cloud.google.com/appengine/docs/standard/go/shared-vpc-host-project).

## January 28, 2022

Change

Builds are now handled by regional Cloud Build pools within the selected App Engine region. To [view build logs](https://docs.cloud.google.com/appengine/docs/standard/go/testing-and-deploying-your-app#view_build_logs), go to Cloud Build in the Cloud Console, select the History page, and select the region you would like to filter by.

## December 08, 2021

Change

  * Updated Go SDK to version 1.9.72.
  * Added ARM version support for app-engine-go component.



## November 29, 2021

Feature

The [Go 1.16 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) for App Engine standard environment is now generally available.

## November 03, 2021

Feature

[Egress settings](https://docs.cloud.google.com/appengine/docs/standard/go/connecting-vpc#egress) for Serverless VPC Access are now generally available. Egress settings allow you to specify whether or not to send traffic with external destinations through your Serverless VPC Access connector, which is necessary if you want to [set up a static outbound IP address](https://docs.cloud.google.com/appengine/docs/standard/go/outbound-ip-addresses#static-ip) for your App Engine service.

## September 27, 2021

Feature

Many [legacy App Engine APIs](https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest) are now available to select second-generation runtimes. These APIs are [available for Go 1.12+](https://docs.cloud.google.com/appengine/docs/standard/go/services/access) in preview, through language-idiomatic libraries. Calls to these APIs are billed according to the standard rates.

## August 13, 2021

Feature

The [Go 1.16 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) for App Engine standard environment is now available in Public Preview.

## July 21, 2021

Feature

[Egress settings](https://docs.cloud.google.com/appengine/docs/standard/go/connecting-vpc#egress) are now available for Serverless VPC Access. Egress settings allow you to specify whether or not to send traffic with external destinations through your Serverless VPC Access connector, which is necessary if you want to [set up a static outbound IP address](https://docs.cloud.google.com/appengine/docs/standard/go/outbound-ip-addresses#static-ip) for your App Engine service.

## June 30, 2021

Change

Requests from newly created or updated App Engine Cron jobs sent to the App Engine standard environment now come from `0.1.0.2`. For Cron jobs created with older gcloud versions (earlier than 326.0.0), Cron requests will come from `0.1.0.1`. Previously, these requests only came from `0.1.0.1`. See [Understanding the App Engine firewall](https://docs.cloud.google.com/appengine/docs/standard/go/understanding-firewalls) for more information.

Feature

Specifying a [user-managed service account](https://docs.cloud.google.com/appengine/docs/standard/go/user-managed-service-accounts) for each App Engine version during deployment is now available in preview. This feature lets you grant different privileges to each version, based on the specific tasks it performs, and avoid granting more privileges than necessary.

## June 14, 2021

Feature

App Engine is now available in the `us-west1` (Oregon), `asia-southeast1` (Singapore), and `asia-east1` (Taiwan) regions.

## April 27, 2021

Change

Automatic scaling elements `min_instances` and `min_idle_instances` will now only apply to versions of a service that have been [configured to receive traffic](https://docs.cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic). This change is to reduce unexpected billing due to instances running old versions that are not intended to receive traffic.

## April 20, 2021

Feature

[Build environment variables](https://docs.cloud.google.com/appengine/docs/standard/go/testing-and-deploying-your-app#build-env-vars) support is now available in preview.

## April 14, 2021

Feature

[Serverless VPC Access support for Shared VPC](https://docs.cloud.google.com/appengine/docs/standard/go/connecting-vpc#shared-vpc) is now generally available.

## April 13, 2021

Feature

App Engine is now available in the `europe-central2` region (Warsaw).

## March 26, 2021

Feature

App Engine standard environment provides a new metric, **CPU Utilization** , which indicates the CPU utilization average over all active instances. For more information, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-appengine).

## March 11, 2021

Feature

The [Go 1.15](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) runtime for the App Engine standard environment is now generally available.

## November 12, 2020

Change

You can use [network ingress controls](https://docs.cloud.google.com/appengine/docs/standard/go/application-security#ingress_controls) so your app only receives requests that are sent from your project's VPC or that are routed through the Cloud Load Balancing load balancer. This feature is now generally available.

## September 25, 2020

Feature

If you use Cloud Load Balancing, you can use [network ingress controls](https://docs.cloud.google.com/appengine/docs/standard/go/application-security#ingress_controls) so your app only receives requests that are routed through the load balancer.

## August 25, 2020

Feature

The [Go 1.14 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime#go-1.14) for the App Engine standard environment is now generally available.

## July 23, 2020

Feature

[Serverless VPC Access support for Shared VPC](https://docs.cloud.google.com/appengine/docs/standard/go/connecting-vpc#shared-vpc) is now available in Beta.

## July 08, 2020

Feature

External HTTP(S) Load Balancing is now supported for App Engine via [Serverless network endpoint groups](https://load-balancing/docs/negs/setting-up-serverless-negs). Notably, this feature allows you to use [Cloud CDN](https://docs.cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

## June 26, 2020

Feature

The [Go 1.14 runtime Beta](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) for the App Engine standard environment is now available.

## June 11, 2020

Feature

The [Go 1.13 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) for the App Engine standard environment is now generally available.

## June 08, 2020

Feature

App Engine is now available in the `asia-southeast2` region (Jakarta).

## May 14, 2020

Feature

To get a fine-grained view of billing data for each resource used by your App Engine services, you can apply labels to the services, export your billing data to BigQuery, and run queries. For more information, see [Labeling App Engine resources](https://docs.cloud.google.com/appengine/docs/standard/go/labeling-resources).

## April 20, 2020

Feature

App Engine is now available in the `us-west4` region (Las Vegas, NV).

## March 13, 2020

Feature

App Engine is now available in the `asia-northeast3` region (Seoul).

## March 06, 2020

Feature

App Engine is now available in the `us-west3 region` (Salt Lake City, Utah).

## February 11, 2020

Feature

App Engine is changing the URLs that you use to send requests to your apps. URLs now [include a region ID](https://docs.cloud.google.com/appengine/docs/standard/go/how-requests-are-routed#region-id) to help Google route your requests more efficiently and reliably. For example, an app can receive requests at `https://<var>PROJECT_ID</var>.<var>REGION_ID</var>.r.appspot.com`. This new URL is optional for existing apps and is provided for all new apps.

To ensure a smooth transition, we are slowly updating App Engine to use region IDs. If we haven't updated your Google Cloud project yet, you won't see a region ID for your app. Since the ID is optional for existing apps, you don't need to update URLs or make other changes once the region ID is available for your existing apps.

## February 06, 2020

Change

  * You can no longer apply new spending limits to projects. Existing spending limits will continue to work. For more information on how you can limit app costs, see [Limiting Costs](https://docs.cloud.google.com/appengine/docs/managing-costs).



## December 11, 2019

Feature

  * [Serverless VPC Access](https://docs.cloud.google.com/appengine/docs/standard/go/connecting-vpc) is now GA.



## October 16, 2019

Feature

  * The [Go 1.13 runtime](https://docs.cloud.google.com/appengine/docs/standard/go113/runtime) for the App Engine standard environment is now Beta.



## September 27, 2019

Feature

  * Updated Go SDK version to 1.9.71:

    * Support for Go versions 1.9 and older has been removed.
    * The `goapp` tool has been removed.
    * The Go 1.9 GOROOT directory has been removed.



## July 30, 2019

Change

  * The functionalities of the App Engine SDK is delivered exclusively through [Cloud SDK](https://docs.cloud.google.com/sdk/docs). For more information, see [Migrating to Cloud SDK](https://docs.cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration) .



Deprecated

  * The AppCfg tooling and the legacy standalone App Engine SDK, delivered through the `GoogleAppEngineLauncher.dmg`, `GoogleAppEngine.msi`, and `google_appengine.zip` files, are now deprecated. Google will shut down and remove support on July 30, 2020.



## June 27, 2019

Deprecated

  * Support for Go 1.9 on App Engine is now [deprecated](https://docs.cloud.google.com/appengine/docs/deprecations).



Deprecated

  * New Go 1.9 app deployments will not be possible from October 1, 2019. Upgrade your Go 1.9 app to use the [Go 1.11 runtime](https://docs.cloud.google.com/appengine/docs/standard/go111/go-differences) or the [Go 1.12 runtime](https://docs.cloud.google.com/appengine/docs/standard/go112/go-differences).



## May 23, 2019

Fixed

  * Fixed a bug with `main` in app.yaml files for Go 1.11 and Go 1.12 runtimes that rejected valid main package paths.



## May 16, 2019

Feature

  * The [Go 1.12 runtime](https://docs.cloud.google.com/appengine/docs/standard/go112/runtime) on the App Engine standard environment is now generally available.



## April 18, 2019

Feature

  * App Engine is now available in the `asia-northeast2` region (Osaka, Japan).



## April 15, 2019

Feature

  * App Engine is now available in the `europe-west6` region (Zürich, Switzerland).



## March 25, 2019

Feature

  * A migration guide for [moving apps from Go 1.9 to Go 1.12](https://docs.cloud.google.com/appengine/docs/standard/go112/go-differences) is available.



Feature

  * The [Go 1.12 runtime](https://docs.cloud.google.com/appengine/docs/standard/go112) for the App Engine standard environment is now in beta.



## March 20, 2019

Feature

  * The [Go 1.11 runtime](https://docs.cloud.google.com/appengine/docs/standard/go111/runtime) for the App Engine standard environment is now GA.



## November 06, 2018

Breaking

  * Go 1.6 and Go 1.8 deployments from `gcloud` are now blocked.



Feature

  * Updated Go SDK to version 1.9.70.



## October 22, 2018

Feature

  * App Engine is now available in the `asia-east2` region (Hong Kong).



## October 10, 2018

Feature

  * The [Go 1.11 runtime](https://docs.cloud.google.com/appengine/docs/standard/go111) for the App Engine standard environment is now in beta.



Feature

  * A migration guide for [moving apps from Go 1.9 to Go 1.11](https://docs.cloud.google.com/appengine/docs/standard/go111/go-differences) is available.



## September 12, 2018

Feature

  * Updated Go SDK to version 1.9.68.



Fixed

  * Minor bug fixes.



## August 01, 2018

Deprecated

  * New Go 1.6 and Go 1.8 app deployments will not be possible from November 1, 2018.



Deprecated

  * Support for Go 1.6 and Go 1.8 on App Engine is now [deprecated](https://docs.cloud.google.com/appengine/docs/deprecations).



## July 13, 2018

Feature

  * Updated Go SDK to version 1.9.67.



Fixed

  * Fixed a bug which impacted the local development server.



## July 10, 2018

Feature

  * App Engine is now available in the `us-west2` region (Los Angeles).



## July 03, 2018

Feature

  * Updated Go SDK to version 1.9.66.



Feature

  * The [local development server](https://docs.cloud.google.com/appengine/docs/standard/go/tools/using-local-server) now prints the process ID of the running process on startup. You can use the process ID when debugging your app.



## July 02, 2018

Fixed

Fixed a bug in [auto scaling configuration](https://docs.cloud.google.com/appengine/docs/standard/go/config/appref#scaling_elements) where App Engine was aggressively shutting down instances when the `max_instances` setting was used.

## June 26, 2018

Feature

  * Updated Go SDK to version 1.9.65.



Feature

  * Version 1.9 of the [Go runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is now generally available and is set as the default runtime for Go in the App Engine standard environment.

Re-deploying all new and existing applications using [`api_version: go1`](https://docs.cloud.google.com/appengine/docs/standard/go/config/appref#api_version), will now run on Go 1.9. To continue using other API versions, such as Go 1.6, you must specify `api_version: go1.6` in your `app.yaml` file.




## May 15, 2018

Feature

  * Completed a gradual rollout of an upgrade to the automatic scaling system: 
    * Improved efficiency resulting generally in lower instance cost (up to 6% reduction for many users) and up to 30% reduction for _loading requests_ , which are the first request to a new instance.
    * New max instances setting allows you to cap the total number of instances to be scheduled.
    * New min instances setting allows you to specify a minimum number of instance to keep running for your app.
    * New target CPU utilization setting lets you optimize between latency and cost.
    * New target throughput utilization setting lets you optimize for the number of concurrent requests at which new instances are started.
    * No more resident instances in auto scaling. Previously, if you used the `min_idle_instances` setting, the minimum idle instances were labelled as _Resident_ in the Cloud Console, with the remainder of the instances labelled as _Dynamic_. The new scheduler simply labels all instances as _Dynamic_ with auto scaling. However, the underlying behavior remains similar to previous behavior. If you use `min_idle_instances` and enable warmup requests, you will see at least that many dynamic instances running even during periods with no traffic.
    * For more details, see the [auto scaling documentation](https://docs.cloud.google.com/appengine/docs/standard/go/config/appref#scaling_elements).



## March 28, 2018

Feature

  * Updated Go SDK to version 1.9.64.



Feature

  * App Engine flexible environment applications that declare `runtime: go` in their `app.yaml` configuration file now deploy with the Go 1.10 runtime.



## March 19, 2018

Feature

  * Updated Go SDK to version 1.9.63.



Feature

  * Added beta support for version 1.9 of the Go runtime.

You can try out Go 1.9 by specifying [`api_version: go1.9`](https://docs.cloud.google.com/appengine/docs/standard/go/config/appref#api_version) in your `app.yaml` configuration file.

To use the 1.9 beta version, you must first update your Go SDK to 1.9.63 or later. For details about downloading and installing the SDK, see the [Downloads](https://docs.cloud.google.com/appengine/docs/standard/go/download) page.

During the beta period, `api_version: go1` continues to be an alias for `go1.8`. Note that `go1.9` is not guaranteed to work correctly while it is in beta. We are relying on user feedback to ensure that `go1.9` meets users' needs before promoting it to a GA release. Post feedback to the [google-appengine-go](https://groups.google.com/forum/#!forum/google-appengine-go) Google Group.




## January 08, 2018

Feature

  * Includes internal updates for how applications are deployed.



Feature

  * Updated Go SDK to 1.9.62



## December 14, 2017

Feature

  * Improved access control documentation around deploying apps with IAM roles and service accounts:

    * [Predefined App Engine roles](https://docs.cloud.google.com/appengine/docs/standard/go/access-control#predefined_app_engine_roles)
    * [Deploying using IAM roles](https://docs.cloud.google.com/appengine/docs/standard/go/granting-project-access#deploying_using_iam_roles)
    * [Require permissions](https://docs.cloud.google.com/appengine/docs/admin-api/access-control#required_permissions)



## November 15, 2017

Fixed

  * Fix `gcloud app deploy` failing at finding dependencies that are not required.



Feature

  * Updated Go SDK to 1.9.61



Feature

  * Add `--go_debugging` flag to `dev_appserver.py` to enable [Delve debugging](https://github.com/derekparker/delve).



Feature

  * Add `-debug` flag to `goapp serve` to enable Delve debugging.



## October 31, 2017

Feature

  * App Engine is now available in the `asia-south1` region (Mumbai, India).



## October 25, 2017

Feature

  * Version 1.8 of the [Go runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is now generally available and is set as the default runtime for Go in the App Engine standard environment.

Now, when you deploy any new or existing apps that use [`api_version: go1`](https://docs.cloud.google.com/appengine/docs/standard/go/config/appref#api_version), those apps run on Go 1.8. To continue using Go 1.6, you must specify `api_version: go1.6` in your `app.yaml` file.

Before you can use the Go 1.8 runtime locally with `dev_appserver.py` or `goapp`, you must first [update to the latest version of the SDK for App Engine](https://docs.cloud.google.com/appengine/docs/standard/go/download#updating-the-sdk-for-go).

Changes that might affect your app:

    * As of Go 1.7, the `context` package has [moved into the stdlib](https://golang.org/doc/go1.7#context). You must ensure that your code and dependencies work correctly with this change. You can use the [`fix` command](https://golang.org/cmd/fix/) to change your app's imports from `"golang.org/x/net/context"` to `"context"`, for example: [`go tool fix -r context`](https://golang.org/doc/go1.8#tool_fix).
    * In Go 1.8, the internal representation of `time.Time` objects has changed and might break your app if you use either `reflect.DeepEqual` or `==` to compare `time.Time` values. Use [`time.Equal`](https://golang.org/pkg/time/#Time.Equal) to compare timestamps.



Feature

  * Updated Go SDK to version 1.9.60.



## October 11, 2017

Feature

  * Announced general availability of [App Engine firewall](https://docs.cloud.google.com/appengine/docs/standard/go/creating-firewalls).



## October 03, 2017

Fixed

  * Fixed bug in `dev_appserver.py` which used incorrect build constraints for the Go 1.8 beta.



Feature

  * Updated Go SDK to 1.9.59



## September 13, 2017

Feature

  * The `gcloud` commands and Admin API methods used to [map custom domains](https://docs.cloud.google.com/appengine/docs/standard/go/mapping-custom-domains) are now generally available. This includes [`gcloud domains verify`](https://docs.cloud.google.com/sdk/gcloud/reference/domains) and [`apps.authorizedDomains.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list). However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/standard/go/securing-custom-domains-with-ssl).



Feature

  * You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/standard/go/securing-custom-domains-with-ssl).



Change

  * If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [upgrade to managed SSL certificates](https://docs.cloud.google.com/appengine/docs/standard/go/securing-custom-domains-with-ssl#updating_to_managed_ssl_certificates).



## September 11, 2017

Fixed

  * Fixed a bug introduced in 1.9.56 which caused signals and stdin to not be propagated correctly.



Fixed

  * Fixed a bug in goapp.bat which resulted in processes not being properly terminated.



Feature

  * Updated Go SDK to version 1.9.58



## September 05, 2017

Feature

  * App Engine is now available in the `southamerica-east1` region (São Paulo, Brazil).



## August 23, 2017

Feature

  * Beta release of the [App Engine firewall](https://docs.cloud.google.com/appengine/docs/standard/go/creating-firewalls).



## August 09, 2017

Feature

  * Updated Go SDK to version 1.9.57.



Fixed

  * The `aetest` package now reuses HTTP connections, fixing a bug that exhausted file descriptors when running tests.



Feature

  * Go 1.8 uses the new standard library context package when calling `appengine.NewContext()`.



## August 01, 2017

Feature

  * App Engine is now available in the `europe-west3` region (Frankfurt, Germany).



## July 18, 2017

Feature

  * App Engine is now available in the `australia-southeast1` region (Sydney, Australia).



## July 01, 2017

Fixed

  * Fixed an issue with auto-reloading apps.



Feature

  * Updated Go SDK to version 1.9.56



## June 27, 2017

Feature

  * Enable the Go 1.8 beta



Feature

  * Updated Go SDK to version 1.9.55



Feature

This release adds beta support for `go1.8`. To use Go 1.8, set `api_version: go1.8` in your `app.yaml` configuration file. You must also use App Engine SDK, not Cloud SDK. To download the App Engine SDK, go to the [Downloads page](https://docs.cloud.google.com/appengine/docs/standard/go/download) and at the bottom of the page, expand the **Or, you can download the original App Engine SDK for Go** section.

Go 1.8 will be available with the next Cloud SDK release.

During the beta period, `api_version: go1` will continue to be an alias for `go1.6`. Note that `go1.8` is not guaranteed to work correctly while it is in beta. We are relying on user feedback to ensure that `go1.8` meets our users' needs before promoting it to a GA release. Send feedback to the [google-appengine-go](https://groups.google.com/forum/#!forum/google-appengine-go) google group.

  * As of `go1.7` the `context` package has [moved into the stdlib](https://golang.org/doc/go1.7#context). Ensure that your code and dependencies work correctly with this change.
  * Note that `go1.8` changes the way that local timezones and UTC are represented. If you use `reflect.DeepEqual` or `==` to compare `time.Time` values, this might be a breaking change. Instead, use [`time.Equal`](https://golang.org/pkg/time/#Time.Equal) when comparing timestamps.



## June 06, 2017

Feature

  * App Engine is now available in the `europe-west2` region (London).



Feature

  * You can now use the beta-level features in the Admin API and `gcloud` command-line tool to [create and manage your custom domains and SSL certificates](https://docs.cloud.google.com/appengine/docs/standard/go/mapping-custom-domains).



## May 22, 2017

Feature

  * Updated Go SDK to version 1.9.54.



Feature

  * `api_version: go1` and `api_version: go1.6` both use the new `goroot-1.6` directory.



Feature

  * Upgraded to Go 1.6.4



## May 09, 2017

Feature

  * App Engine is now available in the `us-east4` region (North Virginia).



## May 04, 2017

Feature

  * In preparation for the Go 1.8 beta, Go `api_version`s are mapped to specific `GOROOT` directories.



Feature

  * Updated Go SDK to version 1.9.53.



## December 01, 2016

Feature

  * Updated Go SDK to version 1.9.48.



## November 03, 2016

Feature

  * Updated Go SDK to version 1.9.46.



## October 27, 2016

Deprecated

  * The Channel and XMPP services are now [deprecated](https://docs.cloud.google.com/appengine/docs/deprecations). These services will be turned down on October 31, 2017.



## August 01, 2016

Feature

Version 1.9.42

Feature

**Admin API notes**

  * Version 1 of the [Admin API](https://docs.cloud.google.com/appengine/docs/admin-api) is now generally available.



Feature

**Go 1.12+ runtime notes**

  * This release does not include a new Go 1.12+ SDK. Go 1.12+ users should continue to use the 1.9.40 SDK.



## July 18, 2016

Feature

  * New [App Engine guided walkthrough](https://console.cloud.google.com/start/appengine) in the Cloud Console. Pick your preferred language and launch an interactive tutorial directly in the console.



Feature

  * Server Errors and Client Errors now more accurately reflect per-URL status errors in the App Engine dashboard.



Change

  * LeaseTasksByTag requests will be limited to 25 requests per second.



Change

  * Version 1.9.39 was skipped.



Feature

  * Increases the maximum cron tasks limit to 250.



Feature

Version 1.9.40

## July 01, 2016

Feature

**Cloud Datastore**

  * New [Cloud Datastore Pricing](https://cloud.google.com/appengine/pricing#costs-for-datastore-calls) is now in effect.



## May 25, 2016

Feature

**Cloud Datastore**

  * When committing a cross-group transaction, version numbers returned for new or updated entities are all the same. With the previous behavior, entities within the same group committed as part of a cross-group transaction, had the same version number, but entities in different groups might have had different version numbers. This change ensures all new and updated entities have an identical version number, regardless of their entity group, when committed as part of a cross-group transaction. As before, entities that are not updated will not have a new version number.



Feature

  * The error returned by URL Fetch for a request to a port outside of the permitted ranges (80-90, 440-450, 1024-65535) will now always return `INVALID_URL` as documented.



Feature

Version 1.9.37 SDK uses the release tags go1.1–go1.6 when compiling with the development SDK to bring it inline with those used in typical Go 1.6 builds. Starting with the 1.9.37 SDK, all the necessary Go files in your gopath will be uploaded to the server regardless of the release tags they require. This will ensure that the server always has all the files it needs to compile your app regardless of the release tags being used. This addresses problems that may arise from mismatched release tags in the 1.9.35 SDK.

Feature

Version 1.9.38

Feature

**Cloud Datastore**

  * App Engine Go runtime updated to Go 1.6.2.



## May 04, 2016

Fixed

Includes general bug fixes and improvements.

Feature

Version 1.9.37

## May 02, 2016

Feature

**App Engine flexible environment**

  * The [Ruby runtime](https://docs.cloud.google.com/appengine/docs/flexible/ruby) is now available for the App Engine flexible environment.



## April 18, 2016

Feature

In response to your requests, the App Engine Users API joins the rest of App Engine in supporting IAM roles and group expansion. This means that any user who is a project Owner, Editor or Viewer or an App Engine Admin is considered an "admin" by the Users API, regardless of whether the user was granted the role directly or by membership in a group. * This release populates error details, when available, in error messages associated with the "OverQuota" exception type.

Deprecated

  * Google no longer accepts quota increase requests for the mail service. Customers should use [Sendgrid](https://docs.cloud.google.com/appengine/docs/standard/go/mail/sendgrid) instead.



Feature

Version 1.9.36

## March 24, 2016

Fixed

  * Fixes trace timestamps to match log timestamps.



Feature

  * The SDK now includes support for vendoring external dependencies. See the [go command documentation](https://golang.org/cmd/go/#hdr-Vendor_Directories) for more details.



Feature

Version 1.9.35

Change

  * App Engine Managed VMs is renamed to [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible).



Change

  * This release is based on Go 1.6.



## March 04, 2016

Feature

  * Increases default quota for URL fetch for billed apps. Refer to the [Quotas page](https://docs.cloud.google.com/appengine/docs/quotas#UrlFetch) for details.



Feature

Version 1.9.34

## February 17, 2016

Feature

Version 1.9.33

Feature

  * The URL path "/form" is now allowed and will be forwarded to applications. Previously, this path was blocked.



## February 03, 2016

Feature

  * Container construction choices for Managed VMs

The `gcloud preview app deploy` (and `mvn gcloud:deploy`) commands upload your artifacts to our servers and build a container to deploy your app to the Managed VM environment.

There are two mechanisms for building the container image remotely. The default behavior is to build the container on a transient Compute Engine Virtual Machine which has Docker installed. Alternatively, you can use the [Cloud Build](https://docs.cloud.google.com/build/docs) service. To use the Cloud Build service, follow these steps:

    1. [Activate the Cloud Build API](https://support.google.com/cloud/answer/6158841) for your project.
    2. Use the command `gcloud config set app/use_cloud_build True`. This will cause all invocations of `gcloud preview app deploy` to use the service. (To return to the default behavior, use the command `gcloud config set app/use_cloud_build False`.



Feature

  * Enabled response compression in Go runtime. This might reduce bandwidth usage for some users.



Feature

Version 1.9.32

## January 14, 2016

Feature

App Engine now supports Google Groups: Adding a Google Group as a member of a project grants the members of the group access to App Engine. For example, if a Google Group is an Editor on a project, all members of the group now have Editor access to the App Engine application.

Feature

Version 1.9.31

## November 30, 2015

Feature

Version 1.9.30

Feature

  * Stop calculating and storing queue depth for non-existent queues, queues marked for deletion, and in the case of queue table outages.



Feature

Headers for push queue requests made for Task Queue tasks with no payload will now contain a Content-Length entry set to '0'. Previously headers for such requests contained no Content-Length entry.

Feature

Version 1.9.29

Feature

  * For developers using the [endpoints API](https://docs.cloud.google.com/appengine/docs/standard/python/endpoints/create_api#defining_the_api_endpointsapi), added a discoverable boolean parameter to the @Api annotation to allow users to disable API discovery. Using this feature will prevent some client libraries (e.g. JavaScript) and the API Explorer from working, as they depend on discovery.



## October 29, 2015

Change

The Prospective Search API, which was deprecated on July 14, is now restricted to existing users. It will fully shutdown on December 1.

Feature

Improved accuracy of Geo filtering in Search queries.

Feature

Version 1.9.28

## September 25, 2015

Feature

Datastore

  * Bugfix: Repeated numeric facets are now allowed.



Feature

Applications that are newly enabled for billing now default to an unlimited daily budget, and no longer default to a maximum daily budget of $0. This prevents unwanted outages due to running out of budget. To set a ceiling on your application's daily cost, after you enable billing, set a budget in the [app engine settings](https://console.cloud.google.com/project/_/appengine/settings). For more information, see [Setting a daily budget](https://docs.cloud.google.com/appengine/docs/developers-console#setting_a_daily_budget).

Feature

Version 1.9.27

Feature

Datastore

  * Faceted Search is now GA.



## August 27, 2015

Feature

  * Adds "show in context" menu for MVM application logs that have thread_id or request_id as a field in their log entry. This allows sorting app logs based on either field.



Feature

  * Capability to provision applications for current load and configure elastic provisioning based on both VM and application level metrics.



Feature

  * Remote API can now be accessed using OAuth2 credentials using https://developers.google.com/identity/protocols/application-default-credentials



Feature

  * oauth2client library upgraded to version [1.4.2](https://github.com/google/oauth2client/blob/master/CHANGELOG.md)



Feature

  * Use RequestPayloadTooLargeException for URLFetch requests with payloads that are too large.



Feature

Version 1.9.26

## August 14, 2015

Feature

  * appengine/search: 
    * Support offsets and cursors in search requests and responses.



Feature

  * Added PyAMF version 0.7.2 (Beta).



Feature

  * Admin Console menus start redirecting to Cloud Console. Select services such as the Admin Logs will continue to be available in the Admin Console.



Feature

  * Failed tasks in queues configured with a `retry_limit` of zero will no longer be retried.



Feature

Version 1.9.25

Feature

  * appengine/user:new 
    * Add `User.ClientID` field.



Feature

  * Datastore now allows properties to represent the empty list.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
