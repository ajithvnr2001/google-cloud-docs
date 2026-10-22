---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/release-notes/
title: App Engine standard environment for Java gen2 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:07.923646+00:00
---

# App Engine standard environment for Java gen2 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/standard/resources)



Send feedback 

#  App Engine standard environment for Java gen2 release notes Stay organized with collections  Save and categorize content based on your preferences. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gaestd-java-release-notes.xml) directly. 

## September 29, 2026

Feature

App Engine permanently blocks insecure traffic with TLS version 1.1 and earlier. For `appspot.com` domains, this block occurs at the connection level. For custom domains, the connection might succeed, but the requests are blocked. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls).

## August 19, 2026

Feature

You can migrate your App Engine push queues to Cloud Tasks by updating the bundled services SDK. This method lets you upgrade your app without needing to modify your application code. For more information on how to migrate, see the [push queues migration guide](https://docs.cloud.google.com/appengine/migration-center/standard/java/migrating-push-queues-upgrade-sdk) ([Preview](https://cloud.google.com/products/#product-launch-stages)).

## August 18, 2026

Feature

Support for [migrating from the App Engine Images service to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/standard/java/images-to-cloud-run) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

## August 14, 2026

Feature

To improve security, starting in August 2026, App Engine opts your application into TLS version 1.2 and later. You can opt out until the end of August 2026. Starting in September 2026, App Engine might permanently block insecure traffic with TLS version 1.1 and earlier. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls).

## July 29, 2026

Feature

Support for enabling only needed legacy bundled services using the [`app_engine_bundled_services`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#app_engine_apis) field is in [General Availability](https://cloud.google.com/products/#product-launch-stages).

## July 07, 2026

Feature

To modernize image processing, [migrate from the App Engine Images service to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/standard/java/images-to-cloud-run) by routing calls to a Cloud Run image transformation service while your app continues to run on App Engine (Preview).

## June 03, 2026

Feature

App Engine supports [Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc) in [Preview](https://cloud.google.com/products#product-launch-stages). Direct VPC egress lets your workloads access VPC network resources as a simpler, more cost-effective [alternative to Serverless VPC Access connectors](https://docs.cloud.google.com/appengine/docs/standard/compare-direct-vpc-egress-connectors).

## May 27, 2026

Feature

Enable only needed legacy bundled services using the [`app_engine_bundled_services`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#app_engine_apis) field for improved security and maintainability of your applications ([Preview](https://cloud.google.com/products/#product-launch-stages)).

## May 21, 2026

Feature

The App Engine Migration hub lets you migrate services in the App Engine standard environment to Cloud Run, and also provides cost-saving recommendations. For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-to-run) ([Preview](https://cloud.google.com/products?e=48754805#product-launch-stages)).

## March 02, 2026

Feature

Support for [migrating from the legacy Mail API to an SMTP-based email service](https://docs.cloud.google.com/appengine/migration-center/standard/java/mail-to-smtp), such as SendGrid, Mailgun, or Mailjet is in [General Availability](https://cloud.google.com/products/#product-launch-stages).

## February 12, 2026

Feature

Support for deploying your existing apps in the standard environment to Cloud Run using the `gcloud beta app migrate-to-run` command is in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-to-run).

## January 31, 2026

Deprecated

Java 8 is [deprecated](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#deprecated). You won't be able to deploy Java 8 applications, even if your organization previously used an organization policy to re-enable deployments of legacy runtimes. Your existing Java 8 applications will continue to run and receive traffic. We recommend that you [migrate to the latest supported version of Java](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/java-differences).

## December 22, 2025

Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## October 31, 2025

Feature

To improve email security and ensure reliable, high-volume email delivery, [migrate from the legacy Mail API to an SMTP-based email service](https://docs.cloud.google.com/appengine/migration-center/standard/java/mail-to-smtp), such as SendGrid, Mailgun, or Mailjet (Preview).

Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 20, 2025

Feature

[Support for TLS version 1.2 and later](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls), along with a corresponding secure set of cipher suites, is in General Availability (GA).

## August 07, 2025

Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls) in the App Engine standard environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

## June 30, 2025

Feature

For new deployments, the [URL Fetch API](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/issue-requests?tab=java) validates the certificate of the host it contacts by default.

## March 18, 2025

Announcement

Container Registry is now [shut down](https://docs.cloud.google.com/artifact-registry/docs/transition/prepare-gcr-shutdown). We recommend that you use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) for storing and managing container images. By default, new deployments created after March 5, 2025, use Artifact Registry instead of Container Registry for storing application build images. For more information, see [Migrate App Engine container images to Artifact Registry](https://docs.cloud.google.com/appengine/migration-center/migrate-to-artifact-registry).

## March 03, 2025

Feature

For new projects you create after March 2025, App Engine sets the automatic scaling maximum instances default for standard environment deployments to 20. This change doesn't impact existing apps. To override the default, specify a new [`max_instances`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements) value in your `app.yaml` file, and deploy a new version or redeploy over an existing version.

## December 09, 2024

Feature

[Custom organization policies](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#custom-constraints) for Serverless VPC Access connectors are now [generally available](https://cloud.google.com/products/#product-launch-stages), and can be applied to projects, folders, or organizations.

## October 31, 2024

Change

Java 11 has reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#end_of_support). Your existing Java 11 applications using will continue to run and receive traffic. However, App Engine might block re-deployments of applications that use runtimes [after their end of support date](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java). We recommend that you [upgrade to the latest supported version of Java](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/upgrade-java-runtime).

## July 30, 2024

Feature

In the App Engine page in the Google Cloud console, you can now filter your existing App Engine versions by [runtime lifecycle stages](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle). After you apply this filter, the console displays a warning icon for App Engine versions that are approaching end of support, have reached end of support, are deprecated, and are decomissioned.

## July 16, 2024

Feature

You can now configure an HTTP connector to improve CPU and memory utilization for your App Engine apps. To configure an HTTP connector, include the `appengine.use.httpconnector` system property in your [appengine-web.xml](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml) file. For more information, see [Google App Engine Java new performant HTTP connector](https://github.com/GoogleCloudPlatform/appengine-java-standard/blob/main/httpconnector.md) GitHub page.

## July 12, 2024

Announcement

Deployments for new projects might be impacted from the following changes to org policies:

  * Starting in May 2024, Google Cloud enforces [secure-by-default organization policies](https://resource-manager/docs/secure-by-default-organizations) for all organization resources. This policy prevents App Engine from granting the `Editor` role to the App Engine default services accounts by default.

  * Starting in June 2024, Cloud Build has changed the default behavior for how Cloud Build uses service accounts in new projects. This change is detailed in [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates). As a result of this change, new projects deploying versions for the first time may be using the default App Engine service account with [insufficient permissions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants%22) for deploying versions. 




If you are impacted by this change you can do one of the following:

  * Grant the [Editor](https://docs.cloud.google.com/appengine/docs/standard/roles) role to the App Engine default service account.

  * Review the Cloud Build guidance on changes to the default service account and [opt out of these changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).




## February 26, 2024

Feature

[Java 21](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## January 23, 2024

Feature

The option to [update a Serverless VPC Access connector](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#update-connector) is now available at general availability (GA). This feature allows you to edit the machine (instance) type, as well as the minimum and maximum number of instances.

## December 21, 2023

Change

A warning message now appears before you publish a container image to a public repository.

## December 06, 2023

Feature

[Java 21](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime) is now available [in preview](https://cloud.google.com/products/#product-launch-stages). Update your configuration files based on either of the following options, depending on what your app currently uses: 

  * If you use legacy bundled services, you must upgrade your apps to run on either:

    * Java Enterprise Edition 10 (EE10 - default, recommended): Java EE10 does not support `javax.servlet.*` APIs and requires you to update your apps and third-party dependencies to use newer Java artifacts like the `Jakarta` namespace.
    * Java Enterprise Edition 8 (EE8): Java EE8 lets you use `javax.servlet.*` APIs, but you must make minor configuration changes to your `appengine-web.xml` file.
  * If you don't use legacy bundled services, update the version in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=java) file.

See [Upgrade an existing application](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/upgrade-java-runtime) for all options.




## August 07, 2023

Change

Accessing a service that's prohibited by the **Internal** or **Internal and Cloud Load Balancing** [ingress setting](https://docs.cloud.google.com/appengine/docs/standard/ingress-settings) now results in a `404` rather than `403` error code.

## June 22, 2023

Feature

The Java runtime now supports using [Maven wrappers](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/specifying-dependencies#declaring_and_managing_dependencies) for managing your project's dependency on Maven.

## May 01, 2023

Change

[Memory limits](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) for second-generation runtimes have been increased to better support the growing memory utilization of many newer runtimes.

## April 27, 2023

Feature

The [Search API](https://docs.cloud.google.com/appengine/docs/standard/services/search?tab=java) is now available in the [App Engine legacy bundled services for second-generation runtimes](https://docs.cloud.google.com/appengine/docs/standard/services/overview?tab=java). Access this legacy bundled service through the [App Engine API JAR](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access).

## April 18, 2023

Change

  * Updated the Java SDK to version 2.0.13.
  * Upgraded Jetty web server to version `9.4.51.v20230217`.



## December 21, 2022

Feature

The option to [update a Serverless VPC Access connector](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#update-connector) is now available in preview. This feature allows you to edit the machine (instance) type, as well as the minimum and maximum number of instances.

## December 13, 2022

Feature

You can now use any configured [service account](https://docs.cloud.google.com/iam/docs/service-accounts) in your Cloud project as the [app-level default service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts), while creating and updating your App Engine applications.

## November 01, 2022

Feature

[Build environment variables](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#build-env-vars) support is now generally available.

## July 18, 2022

Change

  * Updated the Java SDK to version 1.9.98.
  * Updated Jetty web server to version `jetty-9.4.46.v20220331`.



## July 01, 2022

Feature

The [Java 17 runtime for App Engine standard environment ](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime) is now [generally](https://cloud.google.com/products/#product-launch-stages) available.

## June 06, 2022

Change

The Java 17 runtime (preview) now uses [Ubuntu 22](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime#the_runtimes_open_jdk_environment).

## May 26, 2022

Change

  * Updated the Java SDK to version 1.9.97.
  * Added missing classes in the `appegine-jsr107cache.jar` file.



## May 18, 2022

Feature

Specifying a [user-managed service account](https://docs.cloud.google.com/appengine/docs/standard/java11/user-managed-service-accounts) for each App Engine version during deployment is now [generally available](https://cloud.google.com/products/#general-availability).

## April 13, 2022

Feature

The [App Engine legacy bundled services for Java 11/17](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/bundled-services-overview) are now available at the [General Availability release level](https://cloud.google.com/products/#product-launch-stages). These [APIs](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled) can be [accessed](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access) through language-idiomatic libraries. Calls to these API are billed according to the standard rates.

## April 08, 2022

Change

  * Updated the Java SDK to version 1.9.96 to also support Java 17 (preview). 
  * Updated Jetty web server to version 9.4.45.v20220203.



## March 24, 2022

Feature

Support for Serverless VPC Access connectors in Shared VPC host projects is now at general availability (GA). Learn about the [advantages](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/connecting-shared-vpc#host-project) of this method and how to [configure connectors in host projects](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/shared-vpc-host-project).

## March 15, 2022

Feature

All released artifacts that start with version `2.x.x` use the [open source](https://docs.cloud.google.com/blog/topics/developers-practitioners/open-sourcing-app-engine-standard-java-runtime) release mechanism. Released artifacts that start with version `1.9.9xx` or earlier use the internal build system. See the [`appengine-java-standard`](https://github.com/GoogleCloudPlatform/appengine-java-standard) repository for more details.

## March 14, 2022

Feature

The [Java 17 runtime for App Engine standard environment ](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime) is now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

## February 17, 2022

Change

Updated the Java SDK to version 1.9.95.

## January 28, 2022

Change

Builds are now handled by regional Cloud Build pools within the selected App Engine region. To [view build logs](https://docs.cloud.google.com/appengine/docs/standard/java11/testing-and-deploying-your-app#view_build_logs), go to Cloud Build in the Cloud Console, select the History page, and select the region you would like to filter by.

## January 19, 2022

Change

Updated Java SDK to version 1.9.94.

## December 01, 2021

Change

Updated Java SDK to version 1.9.93.

## November 03, 2021

Feature

[Egress settings](https://docs.cloud.google.com/appengine/docs/standard/java11/connecting-vpc#egress) for Serverless VPC Access are now generally available. Egress settings allow you to specify whether or not to send traffic with external destinations through your Serverless VPC Access connector, which is necessary if you want to [set up a static outbound IP address](https://docs.cloud.google.com/appengine/docs/standard/java11/outbound-ip-addresses#static-ip) for your App Engine service.

## November 02, 2021

Change

  * Upgrade to Jetty version 9.4.44.v20210927



## September 27, 2021

Feature

Many [legacy App Engine APIs](https://docs.cloud.google.com/appengine/docs/standard/java11/reference/services/bundled) are now available to select second-generation runtimes. These APIs are [available for Java 11](https://docs.cloud.google.com/appengine/docs/standard/java11/services/access) in preview, through language-idiomatic libraries. Calls to these APIs are billed according to the standard rates.

## July 21, 2021

Feature

[Egress settings](https://docs.cloud.google.com/appengine/docs/standard/java11/connecting-vpc#egress) are now available for Serverless VPC Access. Egress settings allow you to specify whether or not to send traffic with external destinations through your Serverless VPC Access connector, which is necessary if you want to [set up a static outbound IP address](https://docs.cloud.google.com/appengine/docs/standard/java11/outbound-ip-addresses#static-ip) for your App Engine service.

## July 16, 2021

Change

  * Updated Java SDK to version 1.9.90.



## June 30, 2021

Change

Requests from newly created or updated App Engine Cron jobs sent to the App Engine standard environment now come from `0.1.0.2`. For Cron jobs created with older gcloud versions (earlier than 326.0.0), Cron requests will come from `0.1.0.1`. Previously, these requests only came from `0.1.0.1`. See [Understanding the App Engine firewall](https://docs.cloud.google.com/appengine/docs/standard/java11/understanding-firewalls) for more information.

Feature

Specifying a [user-managed service account](https://docs.cloud.google.com/appengine/docs/standard/java11/user-managed-service-accounts) for each App Engine version during deployment is now available in preview. This feature lets you grant different privileges to each version, based on the specific tasks it performs, and avoid granting more privileges than necessary.

## June 14, 2021

Feature

App Engine is now available in the `us-west1` (Oregon), `asia-southeast1` (Singapore), and `asia-east1` (Taiwan) regions.

## May 20, 2021

Change

  * Updated Java SDK to version 1.9.89.
  * Upgraded to Jetty version 9.4.41.v20210516.
  * Stopped releasing Maven artifact `appengine-api-labs-1.9.xx.jar`. Last release is 1.9.88.



## April 27, 2021

Change

Automatic scaling elements `min_instances` and `min_idle_instances` will now only apply to versions of a service that have been [configured to receive traffic](https://docs.cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic). This change is to reduce unexpected billing due to instances running old versions that are not intended to receive traffic.

## April 20, 2021

Feature

[Build environment variables](https://docs.cloud.google.com/appengine/docs/standard/java11/testing-and-deploying-your-app#build-env-vars) support is now available in preview.

## April 14, 2021

Feature

[Serverless VPC Access support for Shared VPC](https://docs.cloud.google.com/appengine/docs/standard/java11/connecting-vpc#shared-vpc) is now generally available.

## April 13, 2021

Feature

App Engine is now available in the `europe-central2` region (Warsaw).

## April 01, 2021

Change

  * Updated Java SDK to version 1.9.88.
  * Upgraded to Jetty 9.4.39 to fix CVE-2021-28163, CVE-2021-28164, CVE-2021-28165.



## March 26, 2021

Feature

App Engine standard environment provides a new metric, **CPU Utilization** , which indicates the CPU utilization average over all active instances. For more information, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-appengine).

## November 12, 2020

Change

You can use [network ingress controls](https://docs.cloud.google.com/appengine/docs/standard/java11/application-security#ingress_controls) so your app only receives requests that are sent from your project's VPC or that are routed through the Cloud Load Balancing load balancer. This feature is now generally available.

## September 25, 2020

Feature

If you use Cloud Load Balancing, you can use [network ingress controls](https://docs.cloud.google.com/appengine/docs/standard/java11/application-security#ingress_controls) so your app only receives requests that are routed through the load balancer.

## July 23, 2020

Feature

[Serverless VPC Access support for Shared VPC](https://docs.cloud.google.com/appengine/docs/standard/java11/connecting-vpc#shared-vpc) is now available in Beta.

## July 08, 2020

Feature

External HTTP(S) Load Balancing is now supported for App Engine via [Serverless network endpoint groups](https://load-balancing/docs/negs/setting-up-serverless-negs). Notably, this feature allows you to use [Cloud CDN](https://docs.cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

## June 08, 2020

Feature

App Engine is now available in the `asia-southeast2` region (Jakarta).

## May 14, 2020

Feature

To get a fine-grained view of billing data for each resource used by your App Engine services, you can apply labels to the services, export your billing data to BigQuery, and run queries. For more information, see [Labeling App Engine resources](https://docs.cloud.google.com/appengine/docs/standard/java11/labeling-resources).

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

App Engine is changing the URLs that you use to send requests to your apps. URLs now [include a region ID](https://docs.cloud.google.com/appengine/docs/standard/java11/how-requests-are-routed#region-id) to help Google route your requests more efficiently and reliably. For example, an app can receive requests at `https://<var>PROJECT_ID</var>.<var>REGION_ID</var>.r.appspot.com`. This new URL is optional for existing apps and is provided for all new apps.

To ensure a smooth transition, we are slowly updating App Engine to use region IDs. If we haven't updated your Google Cloud project yet, you won't see a region ID for your app. Since the ID is optional for existing apps, you don't need to update URLs or make other changes once the region ID is available for your existing apps.

## February 06, 2020

Deprecated

  * You can no longer apply new spending limits to projects. Existing spending limits will continue to work. For more information on how you can limit app costs, see [Limiting Costs](https://docs.cloud.google.com/appengine/docs/managing-costs).



## December 11, 2019

Feature

  * [Serverless VPC Access](https://docs.cloud.google.com/appengine/docs/standard/java11/connecting-vpc) is now GA.



## December 07, 2019

Feature

  * Upgrade Jarkata Jasper JSP compiler to version 9.0.24.



Feature

  * Updated Java SDK to version 1.9.77.



## October 17, 2019

Feature

  * The [Java 11 runtime](https://docs.cloud.google.com/appengine/docs/standard/java11/runtime) for the App Engine standard environment is now GA.



## July 30, 2019

Feature

  * The functionalities of the App Engine SDK is delivered exclusively through [Cloud SDK](https://docs.cloud.google.com/sdk/docs). For more information, see [Migrating to Cloud SDK](https://docs.cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration).



Deprecated

  * The AppCfg tooling and the legacy standalone App Engine SDK, delivered through the `GoogleAppEngineLauncher.dmg`, `GoogleAppEngine.msi`, and `google_appengine.zip` files, are now deprecated. Google will shut down and remove support on July 30, 2020.



## June 24, 2019

Feature

  * Updated Java SDK to version 1.9.76.



## June 05, 2019

Feature

  * The [Java 11 runtime](https://docs.cloud.google.com/appengine/docs/standard/java11/runtime) for the App Engine standard environment is now Beta.



## June 03, 2019

Fixed

  * Fixed performance issue for large batch GETs from Memcache.



Feature

  * The Google App Engine API jar is now compiled as a Java 8 target.



Feature

  * Updated Java SDK to version 1.9.75.



## April 30, 2019

Feature

  * Updated Java SDK to version 1.9.74.



## April 18, 2019

Feature

  * App Engine is now available in the `asia-northeast2` region (Osaka, Japan).



## April 15, 2019

Feature

  * App Engine is now available in the `europe-west6` region (Zürich, Switzerland).



## March 26, 2019

Feature

  * Updated Java SDK to version 1.9.73.



## February 13, 2019

Deprecated

  * You can no longer build Java 7 apps. Java 7 app deployment was blocked on January 25.



Feature

  * Updated Java SDK to version 1.9.72.



## January 25, 2019

Deprecated

  * App deployments on the Java 7 runtime are now blocked. If your app is currently using the Java 7 runtime, it will be automatically migrated to the [Java 8 runtime](https://docs.cloud.google.com/appengine/docs/standard/java/runtime).



## January 21, 2019

Feature

  * Updated Java SDK to version 1.9.78.



## December 28, 2018

Feature

  * Updated Java SDK to version 1.9.69.



Feature

  * Upgrade the ASM library to improve handling of Java 11 bytecode.



Feature

  * Stop bundling the ECJ (Eclipse compiler) in the JSP compilation classpath.



## December 19, 2018

Feature

  * Updated Java SDK to version 1.9.71.



Feature

  * [`DeleteSchema` method](https://docs.cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/search#deleteSchema--) in `com.google.appengine.api.search.Index` is now supported. To completely delete an index, you need to delete the index's documents and schema.



## December 06, 2018

Feature

  * Updated Jetty to version 9.4.14.v20181114.



Feature

  * Updated Java SDK to version 1.9.70.



## October 25, 2018

Feature

  * Updated Java SDK to version 1.9.68.



Fixed

  * Minor bug fixes.



## October 22, 2018

Feature

  * App Engine is now available in the `asia-east2` region (Hong Kong).



## October 18, 2018

Fixed

  * `AppEngineSession.setAttribute` supports null values, [fixing a bug](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2283) that would previously throw null pointer exceptions.



Feature

  * Updated Java SDK to version 1.9.67.



## October 03, 2018

Feature

  * Updated Jetty to version 9.4.12.v20180830.



Feature

  * Updated Java SDK to version 1.9.66.



## September 19, 2018

Fixed

  * Fixed grammar in staging option defaults help.



Feature

  * Updated Java SDK to version 1.9.65.



Feature

  * Improved support for using Java 11 to develop and deploy apps on the Java 8 runtime.



Fixed

  * Fixed LocalMailService javadoc.



Feature

**Java runtime notes**

Feature

  * `min-instances` can be set to 0 in `appengine-web.xml`.



Feature

  * `DatastoreType` always returns high replication.



Feature

  * `enhance_jdos` will fail if it raises an exception.



## August 24, 2018

Deprecated

**Shutdown of Cloud Endpoints Frameworks v1 is approaching**

Cloud Endpoints Frameworks v1 for the App Engine standard environment was deprecated on August 2, 2017. The [service is scheduled to be shutdown](https://docs.cloud.google.com/appengine/docs/deprecations/endpoints-v1) on September 3, 2018, and the documentation will be removed. To avoid an outage, you must migrate your v1 application. For information on migrating your application to Endpoints Frameworks v2, see the following:

  * [Java Migration Guide](https://docs.cloud.google.com/endpoints/docs/frameworks/java/migrating)
  * [Migrating Android Projects](https://docs.cloud.google.com/endpoints/docs/frameworks/java/migrating-android)



## July 10, 2018

Feature

  * App Engine is now available in the `us-west2` region (Los Angeles).



## July 02, 2018

Fixed

Fixed a bug in [auto scaling configuration](https://docs.cloud.google.com/appengine/docs/standard/java11/config/appref#scaling_elements) where App Engine was aggressively shutting down instances when the `max-instances` setting was used.

## May 31, 2018

Feature

  * Adds --application flag to `dev_appserver.py`.



Feature

**Java runtime notes**

Feature

  * Updated Java SDK to version 1.9.64.



Fixed

  * Fixes issues where the [Java runtime does not support `<min-instances>0</min-instances>`](https://issuetracker.google.com/80273043).



Fixed

  * Fixes a problem where environment variables set in the `appengine-web.xml` file were not passed through the staging process and available to the app.



Feature

  * Prevent deployment with filenames containing carriage returns.



## May 15, 2018

Feature

  * Completed a gradual rollout of an upgrade to the automatic scaling system: 
    * Improved efficiency resulting generally in lower instance cost (up to 6% reduction for many users) and up to 30% reduction for _loading requests_ , which are the first request to a new instance.
    * New max instances setting allows you to cap the total number of instances to be scheduled.
    * New min instances setting allows you to specify a minimum number of instance to keep running for your app.
    * New target CPU utilization setting lets you optimize between latency and cost.
    * New target throughput utilization setting lets you optimize for the number of concurrent requests at which new instances are started.
    * No more resident instances in auto scaling. Previously, if you used the `min_idle_instances` setting, the minimum idle instances were labelled as _Resident_ in the Cloud Console, with the remainder of the instances labelled as _Dynamic_. The new scheduler simply labels all instances as _Dynamic_ with auto scaling. However, the underlying behavior remains similar to previous behavior. If you use `min_idle_instances` and enable warmup requests, you will see at least that many dynamic instances running even during periods with no traffic.
    * For more details, see the [auto scaling documentation](https://docs.cloud.google.com/appengine/docs/standard/java11/config/appref#scaling_elements).



## February 27, 2018

Feature

**Java runtime notes**

  * Updated Java SDK to version 1.9.63.



## February 07, 2018

Feature

  * Updated Java SDK to version 1.9.62.



Fixed

  * Fixed a [Cloud SDK issue](https://issuetracker.google.com/issues/72808542) where the Java 8 Servlet 3.1 quickstart processing failed during deployment.



Feature

**Java runtime notes**

## January 22, 2018

Feature

**Java runtime notes**

  * Java SDK version 1.9.61 was patched. If you have previously installed this version, [download](https://docs.cloud.google.com/appengine/docs/standard/java/download) and reinstall the SDK.



## January 18, 2018

Feature

**Java runtime notes**

  * Updated Java SDK to version 1.9.61.



## December 20, 2017

Feature

  * Changed the default character encoding to `UTF-8` in the local development server when the runtime is Java 8. Also, allow the character encoding to be set explicitly using the `appengine.file.encoding` system property. These changes mimic what happens in production.



Feature

  * Added a new flag to the `appcfg` command called `enable_new_staging_defaults` to prepare for future Cloud SDK integration to provide better default values for Java application deployment flags.



Fixed

  * Fixed a bug when using the appcfg flag 'use_google_application_default_credentials' did not work correctly on Google Compute Engine VMs.



Feature

**Java runtime notes**

Feature

  * Added a deprecation warning when deploying or locally running a Java 7 application.



Fixed

  * Fixed issue where the [Development server filter running on Windows fails to parse some servlet URL](https://issuetracker.google.com/63595917).



Feature

  * Updated Java SDK to version 1.9.60.



## December 14, 2017

Feature

  * Updated the local development server to set the `url-stream-handler` configuration parameter to `native` by default. This change reflects the behavior of the Java 8 runtime in production. For more information on `url-stream-handler`, see the [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java/config/appref#url-stream-handler) reference.



Feature

  * Updated Java SDK to version 1.9.59.



Feature

**Java runtime notes**

Fixed

  * Fixed a [local development server bug](https://issuetracker.google.com/63595917) to resolve issues with servlet URLs that contain the colon character.



Fixed

  * Fixed the [`NoClassDefFoundError`](https://github.com/GoogleCloudPlatform/endpoints-framework-gradle-plugin/issues/53) error that occurs when using the local development server with the Java 8 runtime and Endpoints Framework Gradle Plugin.



Feature

  * Improved access control documentation around deploying apps with IAM roles and service accounts:

    * [Predefined App Engine roles](https://docs.cloud.google.com/appengine/docs/standard/java11/access-control#predefined_app_engine_roles)
    * [Deploying using IAM roles](https://docs.cloud.google.com/appengine/docs/standard/java11/granting-project-access#deploying_using_iam_roles)
    * [Require permissions](https://docs.cloud.google.com/appengine/docs/admin-api/access-control#required_permissions)



## October 31, 2017

Feature

  * App Engine is now available in the `asia-south1` region (Mumbai, India).



## October 11, 2017

Feature

  * Use 1.8 target for the Jetty 9 JSP compiler when using JDK 9.



Fixed

  * Fix the [Jetty quickstart module for annotations](https://webtide.com/jetty-9-quick-start/) in the App Engine flexible environment.



Feature

**Java runtime notes**

Feature

  * Announced general availability of [App Engine firewall](https://docs.cloud.google.com/appengine/docs/standard/java11/creating-firewalls).



Fixed

  * Fixed [local development server bug](https://issuetracker.google.com/63595917) where certain characters caused problems with URL parsing.



Feature

  * Updated Java SDK to version 1.9.58



## September 25, 2017

Deprecated

  * The Java 8 runtime no longer supports JDK9 JARs that contain `module-info.class`.



Fixed

  * Fixed `NoClassDefFoundError` exception on the local development server when using Cloud Endpoints v2 on the Java 8 runtime.



Feature

  * [The Java 8 runtime is now generally available](https://cloudplatform.googleblog.com/2017/09/Java-8-on-App-Engine-Standard-environment-is-now-generally-available.html).



Feature

  * Updated Java SDK to version 1.9.57



Deprecated

  * The local development server no longer supports `-Xbootclasspath/p` and `google_sql.jar` in the path.



Feature

**Java runtime notes**

Deprecated

  * Cloud Endpoints v1 is no longer supported on the Java 8 runtime.



## September 18, 2017

Feature

  * Release 1.3.3 for `com.google.cloud.tools:appengine-gradle-plugin`



Feature

**Java runtime notes**

Feature

  * `datastore-indexes-auto.xml` is no longer removed during non-clean rebuilds. ([#165](https://github.com/GoogleCloudPlatform/app-gradle-plugin/issues/165))



Feature

  * The local development server now logs output to `dev_appserver.out`. ([#156](https://github.com/GoogleCloudPlatform/app-gradle-plugin/pull/156))



Feature

  * Switched to use sync instead of copy on the explodeWar task. ([#162](https://github.com/GoogleCloudPlatform/app-gradle-plugin/pull/162))



## September 13, 2017

Feature

  * The `gcloud` commands and Admin API methods used to [map custom domains](https://docs.cloud.google.com/appengine/docs/standard/java11/mapping-custom-domains) are now generally available. This includes [`gcloud domains verify`](https://docs.cloud.google.com/sdk/gcloud/reference/domains) and [`apps.authorizedDomains.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list). However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/standard/java11/securing-custom-domains-with-ssl).



Feature

  * If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [upgrade to managed SSL certificates](https://docs.cloud.google.com/appengine/docs/standard/java11/securing-custom-domains-with-ssl#updating_to_managed_ssl_certificates).



Feature

  * You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/standard/java11/securing-custom-domains-with-ssl).



## September 11, 2017

Feature

  * Updated Java SDK to version 1.9.56



Feature

  * Added support for the environment variables `GAE_RUNTIME` (`java 7` or `java 8`) and GAE_ENV (`standard`) in the Google App Engine SDK.



Feature

  * For flexible runtimes compatible with the App Engine standard environment APIs (`compat` runtimes), this SDK version includes updates to the `appengine-web.xml` file configuration to add support for `subnetwork_name`, `session_affinity`, and updated liveness and readiness health checks.



Feature

**Java runtime notes**

## September 05, 2017

Feature

  * Updated Java SDK to version 1.9.55



Fixed

  * Fixed bug where security manager was being used for the SDK even when the app was using Java 8/Jetty 9.



Feature

  * App Engine is now available in the `southamerica-east1` region (São Paulo, Brazil).



Feature

  * Emit error message when using the [appstats](https://docs.cloud.google.com/appengine/docs/standard/java/tools/appstats) filter with Java8.



Fixed

  * Fixed [Issue 63123716: Url fetching with Google Java HTTP Client not working on dev-server](https://issuetracker.google.com/issues/63123716)



## August 01, 2017

Feature

  * App Engine is now available in the `europe-west3` region (Frankfurt, Germany).



## July 18, 2017

Feature

  * App Engine is now available in the `australia-southeast1` region (Sydney, Australia).



## June 28, 2017

Feature

**What's New**

  * [Java 8 runtime for App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard/java/runtime-java8) is in Beta.
  * Just add `<runtime>java8</runtime>` in the `appengine-web.xml` file.
  * Based on OpenJDK 8, Servlet 3.1 and Jetty 9.3.
  * Feature compatibility with Java 7 on App Engine and the built-in App Engine APIs.
  * Supports all Google Cloud-based APIs accessible from the [Google Cloud Client Library for Java](https://googleapis.github.io/google-cloud-java/google-cloud-clients/).
  * All public Java 8 APIs are available, [class whitelisting](https://docs.cloud.google.com/appengine/docs/standard/java/jrewhitelist) has been removed.
  * The [Java security manager](https://docs.oracle.com/javase/7/docs/api/java/lang/SecurityManager.html) is removed for the Java 8 runtime.
  * Support for read only [GCP Metadata server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) project and service accounts values.
  * Java SDK 1.9.54 supports the Java 8 runtime.



Breaking

**Known Java 8 Runtime Limitations**

  * The `/tmp` directory is writable. Files in `/tmp` will consume memory allocated to your instance.
  * Async Servlet 3.1 is not supported.
  * WebSocket is not supported.
  * The Jetty 9 configuration cannot be modified.
  * App Engine APIs can only be called from the thread that handles a web request or from threads created using [ThreadManager](https://docs.cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/ThreadManager)
  * `WEB-INF/appengine-web.xml` must be used for configuration, `app.yaml` is not currently supported.
  * Deployment must be done through the Maven, Gradle, or IDE plugins.
  * If you create a thread pool using for example `ExecutorService pool = Executors.newCachedThreadPool(ThreadManager.currentRequestThreadFactory())` then it must be shutdown down explicitly using `pool.shutdown()` before the current request terminates.
  * Previously it was possible to reference vendored classes like `com.google.appengine.repackaged.org.joda.Instant` inadvertently when just `org.joda.Instant` was intended. The vendoring scheme has changed so code that did that no longer works.
  * Native network APIs (for example `HttpURLConnection`) are enabled for billed applications, but will return an exception (`java.net.SocketTimeoutException` or `java.io.IOException`) when used in free applications. Free applications can access `*.googleapis.com` and `accounts.google.com`, and they can also be [configured](https://docs.cloud.google.com/appengine/docs/standard/java/config/appref#url-stream-handler) to use the URLFetch service.
  * The `google-cloud-java` APIs need to be wrapped in an `executor`. See [Pub/Sub Publisher hangs unless submitted through an executor](https://github.com/googleapis/google-cloud-java/issues/2150).
  * Cloud Endpoints must be [migrated](https://docs.cloud.google.com/endpoints/docs/frameworks/legacy/v1/java/migrating) from v1 to v2.
  * Channels and XMPP APIs are not supported.
  * `appengine-labs-api.jar` APIs are not supported resulting in [Appstats for Java](https://docs.cloud.google.com/appengine/docs/standard/java/tools/appstats) not being supported.
  * The Java 8 runtime default is to use the native Java HTTP(S) transport, not the URL Fetch transport, as is the case for Java 7 runtime. For more information, see [url-stream-handler](https://docs.cloud.google.com/appengine/docs/standard/java/config/appref#url-stream-handler).



## June 15, 2017

Feature

  * Updated Java SDK to version 1.9.54.



## June 06, 2017

Feature

  * App Engine is now available in the `europe-west2` region (London).



Feature

  * You can now use the beta-level features in the Admin API and `gcloud` command-line tool to [create and manage your custom domains and SSL certificates](https://docs.cloud.google.com/appengine/docs/standard/java11/mapping-custom-domains).



## May 09, 2017

Feature

  * App Engine is now available in the `us-east4` region (North Virginia).



Feature

  * Updated Java SDK to version 1.9.53.



Fixed

  * Fixed a Java SDK issue where JSP tag library usage would not work with a Java 8 SpringBoot application.



## May 08, 2017

Feature

  * Expose `environment` parameter for including additional environment variables through the maven/gradle configuration.



Feature

  * Release 1.3.1 for `com.google.cloud.tools:appengine-(gradle/maven)-plugin`



Feature

  * Running locally on development server will read and include environment variables from the `appengine-web.xml` configuration file.



## May 02, 2017

Feature

  * New maven goals for configuration deployment : `appengine:deployCron`, `appengine:deployDispatch`, `appengine:deployDos`, `appengine:deployIndex`, `appengine:deployQueue`



Feature

  * Staging flexible apps with maven/gradle only copies `app.yaml` into build/target directory. For deployment of configuration files, use `src/main/appengine`.



Change

  * Gradle exploded app directory default changed from `build/exploded-app` to `build/exploded-<module-name>`



Feature

  * Release 1.3.0 for `com.google.cloud.tools.appengine-(gradle/maven)-plugin`



Feature

  * New gradle tasks for configuration deployment : `appengineDeployCron`, `appengineDeployDispatch`, `appengineDeployDos`, `appengineDeployIndex`, `appengineDeployQueue`



Change

  * Default development server is Dev App Server v1 (only java modules)



## April 19, 2017

Feature

  * Updated Java SDK to version 1.9.52.



Feature

  * Update the `quickstart-web.xml` processing to use the latest Jetty capabilities to better support Java 8 SpringBoot applications.



Fixed

  * Fix SDK error when booting a SpringBoot application.



Fixed

  * Fix local execution of multiple services located in directories ending with the same name.



Feature

  * Upgrade to Jetty 9.3.18 for the [Java 8 alpha](https://docs.google.com/a/google.com/forms/d/1MDzykTWp77YzRgFs5R6ONOuKWYnKEhfy5VhSJYbDvmo/viewform) standard environment runtime.



Feature

  * Better support for Java 8 standard environment alpha runtime.



## March 29, 2017

Feature

  * [Java 8 alpha](https://docs.google.com/a/google.com/forms/d/1MDzykTWp77YzRgFs5R6ONOuKWYnKEhfy5VhSJYbDvmo/viewform) applications without a `web.xml` file can now run in the [local development server](https://docs.cloud.google.com/appengine/docs/standard/java/tools/using-local-server).



Feature

  * Updated Java SDK to version 1.9.51.



## March 21, 2017

Feature

  * Updated the `com.google.cloud.tools:appengine-gradle-plugin` to 1.1.1.



Fixed

  * Fixed [issue 108](https://github.com/GoogleCloudPlatform/app-gradle-plugin/issues/108) with flexible environment deployments in multi-module Gradle projects failing.



## March 06, 2017

Feature

  * Updated the `com.google.cloud.tools:appengine-maven-plugin` to 1.2.1.



Fixed

  * Fixed [issue 144](https://github.com/GoogleCloudPlatform/app-maven-plugin/issues/144) with custom deployable parameters incorrectly adding in extra directory.



## March 01, 2017

Feature

  * Added support for testing multiple services with the local development server.



Feature

  * Package Java class files in the .zip files even if the application does not have JSPs.



Feature

  * Stop generating a web.xml file for apps that use the Java 7 runtime and include a `web.xml` that specifies the servlet 3.1 schema.



Feature

  * Updated Java SDK to version 1.9.50.



## February 17, 2017

Feature

Updated the `com.google.cloud.tools` [maven](https://docs.cloud.google.com/appengine/docs/java/tools/maven-reference) (1.2.0) and [gradle](https://docs.cloud.google.com/appengine/docs/java/tools/gradle-reference) (1.1.0) plugins for App Engine:

  * Added `clearDatastore` flag for clearing the local datastore upon startup.
  * Added source-context tasks/goals.



## January 30, 2017

Feature

  * Updated Java SDK to version 1.9.49.



## December 01, 2016

Feature

  * Updated Java SDK to version 1.9.48.



## November 03, 2016

Change

  * Version 1.9.45 was skipped.



Feature

  * Updated Java Runtime and SDK to version 1.9.46.



## October 27, 2016

Deprecated

  * The Channel and XMPP services are now [deprecated](https://docs.cloud.google.com/appengine/docs/deprecations). These services will be turned down on October 31, 2017.



## October 17, 2016

Feature

  * Updated Java Runtime and SDK to version 1.9.44.



Feature

  * Add new BlobInfo property, which is set when a Blobstore blob is stored in a Cloud Storage bucket.



## August 01, 2016

Feature

Version 1.9.42

Fixed

  * Version 1.9.42 includes general bug fixes and improvements.



Feature

**Admin API notes**

  * Version 1 of the [Admin API](https://docs.cloud.google.com/appengine/docs/admin-api) is now generally available.



Change

  * Version 1.9.41 was skipped.



## July 21, 2016

Fixed

**Java 11 runtime notes**

  * Fixes potentially incorrect reported memory usage in the App Engine dashboard (the values under Instance "Average Memory" and the "Memory Usage" graph). This issue does not affect billing.



## July 18, 2016

Feature

  * New [App Engine guided walkthrough](https://console.cloud.google.com/start/appengine) in the Cloud Console. Pick your preferred language and launch an interactive tutorial directly in the console.



Feature

  * Server Errors and Client Errors now more accurately reflect per-URL status errors in the App Engine dashboard.



Feature

  * LeaseTasksByTag requests will be limited to 25 requests per second.



Change

  * Version 1.9.39 was skipped.



Feature

  * Increases the maximum cron tasks limit to 250.



Feature

Version 1.9.40

Feature

**Java runtime notes**

  * All Java applications will be automatically upgraded to use the 64-bit version of the Java runtime. This rolling upgrade will start on July 20, 2016.



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

Version 1.9.38

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

**Java runtime notes**

  * Google no longer accepts quota increase requests for the mail service. Customers should use [Sendgrid](https://docs.cloud.google.com/appengine/docs/standard/java/mail/sendgrid) instead.



Feature

Version 1.9.36

## March 24, 2016

Fixed

  * Fixes trace timestamps to match log timestamps.



Change

Version 1.9.35

  * App Engine Managed VMs is renamed to [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible).



Change

**Java runtime notes**

  * This release does not include a new Java SDK. Java users should continue to use the 1.9.34 SDK.



## March 16, 2016

Feature

**Java runtime notes**

  * Version 1.9.34 of the Java SDK is available.



## March 04, 2016

Feature

Version 1.9.34

  * Increases default quota for URL fetch for billed apps. Refer to the [Quotas page](https://docs.cloud.google.com/appengine/docs/quotas#UrlFetch) for details.



Feature

**Java runtime notes**

  * This release does not include a new Java SDK. Java users should continue to use the 1.9.32 SDK.



## February 17, 2016

Feature

Version 1.9.33

  * The URL path "/form" is now allowed and will be forwarded to applications. Previously, this path was blocked.



Change

**Java runtime notes**

  * This release does not include a new Java SDK. Java users should continue to use the 1.9.32 SDK.



## February 03, 2016

Feature

Version 1.9.32

  * Container construction choices for Managed VMs

The `gcloud preview app deploy` (and `mvn gcloud:deploy`) commands upload your artifacts to our servers and build a container to deploy your app to the Managed VM environment.

There are two mechanisms for building the container image remotely. The default behavior is to build the container on a transient Compute Engine Virtual Machine which has Docker installed. Alternatively, you can use the [Cloud Build](https://docs.cloud.google.com/build/docs) service. To use the Cloud Build service, follow these steps:

    1. [Activate the Cloud Build API](https://support.google.com/cloud/answer/6158841) for your project.
    2. Use the command `gcloud config set app/use_cloud_build True`. This will cause all invocations of `gcloud preview app deploy` to use the service. (To return to the default behavior, use the command `gcloud config set app/use_cloud_build False`.



Feature

**Java runtime notes**

  * Improved exception handling for the low-level API for Datastore, `Transaction.rollback()`. Instead of an exception, it generates an `INFO` log message when an operation associated with the transaction has failed.



## January 14, 2016

Feature

App Engine now supports Google Groups: Adding a Google Group as a member of a project grants the members of the group access to App Engine. For example, if a Google Group is an Editor on a project, all members of the group now have Editor access to the App Engine application.

Feature

Version 1.9.31

## December 30, 2015

Feature

Version 1.9.30

Feature

Headers for push queue requests made for Task Queue tasks with no payload will now contain a Content-Length entry set to '0'. Previously headers for such requests contained no Content-Length entry.

Feature

Version 1.9.29

Feature

  * Stop calculating and storing queue depth for non-existent queues, queues marked for deletion, and in the case of queue table outages.



Feature

  * For developers using the [endpoints API](https://docs.cloud.google.com/appengine/docs/standard/python/endpoints/create_api#defining_the_api_endpointsapi), added a discoverable boolean parameter to the @Api annotation to allow users to disable API discovery. Using this feature will prevent some client libraries (e.g. JavaScript) and the API Explorer from working, as they depend on discovery.



## October 29, 2015

Feature

**Java runtime notes**

  * Disabled Files API in the Java DevAppServer.



Breaking

The Prospective Search API, which was deprecated on July 14, 2015, is now restricted to existing users. It will fully shutdown on December 1, 2015.

Feature

Improved accuracy of Geo filtering in Search queries.

Feature

Version 1.9.28

## September 25, 2015

Feature

Datastore

Fixed

  * Bugfix: Repeated numeric facets are now allowed.



Feature

Applications that are newly enabled for billing now default to an unlimited daily budget, and no longer default to a maximum daily budget of $0. This prevents unwanted outages due to running out of budget. To set a ceiling on your application's daily cost, after you enable billing, set a budget in the [app engine settings](https://console.cloud.google.com/project/_/appengine/settings). For more information, see [Setting a daily budget](https://docs.cloud.google.com/appengine/docs/developers-console#setting_a_daily_budget).

Feature

  * Faceted Search is now GA.



Feature

Version 1.9.27

## August 27, 2015

Feature

  * Adds "show in context" menu for MVM application logs that have thread_id or request_id as a field in their log entry. This allows sorting app logs based on either field.



Feature

  * Capability to provision applications for current load and configure elastic provisioning based on both VM and application level metrics.



Feature

  * Remote API can now be accessed using OAuth2 credentials using https://developers.google.com/identity/protocols/application-default-credentials



Feature

**Java runtime notes**

  * Java's URLFetch API gains a property to specify default fetch deadline. `appengine.api.urlfetch.defaultDeadline` is a floating point number in seconds that can be used to specify a default URLFetch timeout for Java in appengine-web.xml.



Feature

  * oauth2client library upgraded to version [1.4.2](https://github.com/google/oauth2client/blob/master/CHANGELOG.md)



Feature

  * Use RequestPayloadTooLargeException for URLFetch requests with payloads that are too large.



Feature

Version 1.9.26

## August 14, 2015

Feature

  * Added PyAMF version 0.7.2 (Beta).



Feature

  * Admin Console menus start redirecting to Cloud Console. Select services such as the Admin Logs will continue to be available in the Admin Console.



Feature

  * Failed tasks in queues configured with a `retry_limit` of zero will no longer be retried.



Feature

Version 1.9.25

Feature

  * Datastore now allows properties to represent the empty list.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
