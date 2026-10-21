---
url: https://docs.cloud.google.com/feeds/gaestd-ruby-release-notes.xml
title: App Engine standard environment Ruby - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:23:11.687760+00:00
---

# App Engine standard environment Ruby - Release notes

> Source: https://docs.cloud.google.com/feeds/gaestd-ruby-release-notes.xml

tag:google.com,2016:gaestd-ruby-release-notesApp Engine standard environment Ruby - Release notesGoogle Cloud Platform2026-09-29T00:00:00-07:00September 29, 2026tag:google.com,2016:gaestd-ruby-release-notes#September_29_20262026-09-29T00:00:00-07:00Feature 

App Engine permanently blocks insecure traffic with TLS version 1.1 and earlier. For `appspot.com` domains, this block occurs at the connection level. For custom domains, the connection might succeed, but the requests are blocked. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls).

]]> August 14, 2026tag:google.com,2016:gaestd-ruby-release-notes#August_14_20262026-08-14T00:00:00-07:00Feature 

To improve security, starting in August 2026, App Engine opts your application into TLS version 1.2 and later. You can opt out until the end of August 2026. Starting in September 2026, App Engine might permanently block insecure traffic with TLS version 1.1 and earlier. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls).

]]> June 03, 2026tag:google.com,2016:gaestd-ruby-release-notes#June_03_20262026-06-03T00:00:00-07:00Feature 

App Engine supports [Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc) in [Preview](https://cloud.google.com/products#product-launch-stages). Direct VPC egress lets your workloads access VPC network resources as a simpler, more cost-effective [alternative to Serverless VPC Access connectors](https://docs.cloud.google.com/appengine/docs/standard/compare-direct-vpc-egress-connectors).

]]> May 21, 2026tag:google.com,2016:gaestd-ruby-release-notes#May_21_20262026-05-21T00:00:00-07:00Feature 

The App Engine Migration hub lets you migrate services in the App Engine standard environment to Cloud Run, and also provides cost-saving recommendations. For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-to-run) ([Preview](https://cloud.google.com/products?e=48754805#product-launch-stages)).

]]> March 17, 2026tag:google.com,2016:gaestd-ruby-release-notes#March_17_20262026-03-17T00:00:00-07:00Feature 

Support for [Ruby 4.0 runtime](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime) is in [General Availability](https://cloud.google.com/products/#product-launch-stages).

]]> March 03, 2026tag:google.com,2016:gaestd-ruby-release-notes#March_03_20262026-03-03T00:00:00-08:00Feature 

Support for [Ruby 4.0 runtime](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

]]> February 12, 2026tag:google.com,2016:gaestd-ruby-release-notes#February_12_20262026-02-12T00:00:00-08:00Feature 

Support for deploying your existing apps in the standard environment to Cloud Run using the `gcloud beta app migrate-to-run` command is in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-to-run).

]]> October 20, 2025tag:google.com,2016:gaestd-ruby-release-notes#October_20_20252025-10-20T00:00:00-07:00Feature 

[Support for TLS version 1.2 and later](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls), along with a corresponding secure set of cipher suites, is in General Availability (GA).

]]> August 07, 2025tag:google.com,2016:gaestd-ruby-release-notes#August_07_20252025-08-07T00:00:00-07:00Feature 

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls) in the App Engine standard environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

]]> June 17, 2025tag:google.com,2016:gaestd-ruby-release-notes#June_17_20252025-06-17T00:00:00-07:00Feature 

Support for the [Ruby 3.4 runtime](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

]]> May 05, 2025tag:google.com,2016:gaestd-ruby-release-notes#May_05_20252025-05-05T00:00:00-07:00Feature 

Support for [Ruby 3.4 runtime](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

]]> March 18, 2025tag:google.com,2016:gaestd-ruby-release-notes#March_18_20252025-03-18T00:00:00-07:00Announcement 

Container Registry is now [shut down](https://docs.cloud.google.com/artifact-registry/docs/transition/prepare-gcr-shutdown). We recommend that you use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) for storing and managing container images. By default, new deployments created after March 5, 2025, use Artifact Registry instead of Container Registry for storing application build images. For more information, see [Migrate App Engine container images to Artifact Registry](https://docs.cloud.google.com/appengine/migration-center/migrate-to-artifact-registry).

]]> March 03, 2025tag:google.com,2016:gaestd-ruby-release-notes#March_03_20252025-03-03T00:00:00-08:00Feature 

For new projects you create after March 2025, App Engine sets the automatic scaling maximum instances default for standard environment deployments to 20. This change doesn't impact existing apps. To override the default, specify a new [`max_instances`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements) value in your `app.yaml` file, and deploy a new version or redeploy over an existing version.

]]> December 09, 2024tag:google.com,2016:gaestd-ruby-release-notes#December_09_20242024-12-09T00:00:00-08:00Feature 

[Custom organization policies](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#custom-constraints) for Serverless VPC Access connectors are now [generally available](https://cloud.google.com/products/#product-launch-stages), and can be applied to projects, folders, or organizations.

]]> July 31, 2024tag:google.com,2016:gaestd-ruby-release-notes#July_31_20242024-07-31T00:00:00-07:00Feature 

[Ruby 3.3](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

]]> July 30, 2024tag:google.com,2016:gaestd-ruby-release-notes#July_30_20242024-07-30T00:00:00-07:00Feature 

In the App Engine page in the Google Cloud console, you can now filter your existing App Engine versions by [runtime lifecycle stages](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle). After you apply this filter, the console displays a warning icon for App Engine versions that are approaching end of support, have reached end of support, are deprecated, and are decomissioned.

]]> July 12, 2024tag:google.com,2016:gaestd-ruby-release-notes#July_12_20242024-07-12T00:00:00-07:00Announcement 

Deployments for new projects might be impacted from the following changes to org policies:

  * Starting in May 2024, Google Cloud enforces [secure-by-default organization policies](https://resource-manager/docs/secure-by-default-organizations) for all organization resources. This policy prevents App Engine from granting the `Editor` role to the App Engine default services accounts by default.

  * Starting in June 2024, Cloud Build has changed the default behavior for how Cloud Build uses service accounts in new projects. This change is detailed in [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates). As a result of this change, new projects deploying versions for the first time may be using the default App Engine service account with [insufficient permissions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants%22) for deploying versions. 




If you are impacted by this change you can do one of the following:

  * Grant the [Editor](https://docs.cloud.google.com/appengine/docs/standard/roles) role to the App Engine default service account.

  * Review the Cloud Build guidance on changes to the default service account and [opt out of these changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).


]]> June 18, 2024tag:google.com,2016:gaestd-ruby-release-notes#June_18_20242024-06-18T00:00:00-07:00Feature 

[Ruby 3.3](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime) is now available [in preview](https://cloud.google.com/products/#product-launch-stages).

]]> January 30, 2024tag:google.com,2016:gaestd-ruby-release-notes#January_30_20242024-01-30T00:00:00-08:00Announcement 

Ruby 2.5, 2.6, and 2.7 have reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#end_of_support) on January 30, 2024. Your existing applications using these versions will continue to run and receive traffic. However, App Engine might block re-deployments of applications that use runtimes [after their end of support date](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#ruby). We recommend that you [upgrade to the latest supported version of Ruby](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime).

]]> January 23, 2024tag:google.com,2016:gaestd-ruby-release-notes#January_23_20242024-01-23T00:00:00-08:00Feature 

The option to [update a Serverless VPC Access connector](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#update-connector) is now available at general availability (GA). This feature allows you to edit the machine (instance) type, as well as the minimum and maximum number of instances.

]]> December 21, 2023tag:google.com,2016:gaestd-ruby-release-notes#December_21_20232023-12-21T00:00:00-08:00Change 

A warning message now appears before you publish a container image to a public repository.

]]> August 07, 2023tag:google.com,2016:gaestd-ruby-release-notes#August_07_20232023-08-07T00:00:00-07:00Change 

Accessing a service that's prohibited by the **Internal** or **Internal and Cloud Load Balancing** [ingress setting](https://docs.cloud.google.com/appengine/docs/standard/ingress-settings) now results in a `404` rather than `403` error code.

]]> May 01, 2023tag:google.com,2016:gaestd-ruby-release-notes#May_01_20232023-05-01T00:00:00-07:00Change 

[Memory limits](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) for second-generation runtimes have been increased to better support the growing memory utilization of many newer runtimes.

]]> April 14, 2023tag:google.com,2016:gaestd-ruby-release-notes#April_14_20232023-04-14T00:00:00-07:00Feature 

The [Ruby 3.2 runtime](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime) for App Engine standard environment is now [generally available](https://cloud.google.com/products/#product-launch-stages).

]]> March 06, 2023tag:google.com,2016:gaestd-ruby-release-notes#March_06_20232023-03-06T00:00:00-08:00Feature 

The [Ruby 3.2 runtime](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime) for App Engine standard environment is now available in [preview](https://cloud.google.com/products/#product-launch-stages).

]]> December 21, 2022tag:google.com,2016:gaestd-ruby-release-notes#December_21_20222022-12-21T00:00:00-08:00Feature 

The option to [update a Serverless VPC Access connector](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#update-connector) is now available in preview. This feature allows you to edit the machine (instance) type, as well as the minimum and maximum number of instances.

]]> December 13, 2022tag:google.com,2016:gaestd-ruby-release-notes#December_13_20222022-12-13T00:00:00-08:00Feature 

You can now use any configured [service account](https://docs.cloud.google.com/iam/docs/service-accounts) in your Cloud project as the [app-level default service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts), while creating and updating your App Engine applications.

]]> November 01, 2022tag:google.com,2016:gaestd-ruby-release-notes#November_01_20222022-11-01T00:00:00-07:00Feature 

[Build environment variables](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#build-env-vars) support is now generally available.

]]> May 18, 2022tag:google.com,2016:gaestd-ruby-release-notes#May_18_20222022-05-18T00:00:00-07:00Feature 

Specifying a [user-managed service account](https://docs.cloud.google.com/appengine/docs/standard/ruby/user-managed-service-accounts) for each App Engine version during deployment is now [generally available](https://cloud.google.com/products/#general-availability).

]]> May 04, 2022tag:google.com,2016:gaestd-ruby-release-notes#May_04_20222022-05-04T00:00:00-07:00Feature 

The [Ruby 3.0 runtime](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime) for App Engine standard environment is now [generally available](https://cloud.google.com/products/#product-launch-stages).

]]>
