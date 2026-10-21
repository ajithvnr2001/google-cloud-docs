---
url: https://docs.cloud.google.com/run/docs/runtime-support/
title: Cloud Run runtime lifecycle \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:05.888049+00:00
---

# Cloud Run runtime lifecycle  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/runtime-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Resources ](https://docs.cloud.google.com/run/docs/resources)



Send feedback 

#  Cloud Run runtime lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Container images deployed directly to Cloud Run are not subject to this policy. The Cloud Run lifecycle policy only applies to workloads that use Google-managed base images. For a list of these, see [Cloud Run runtime base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#using_language_runtimes).

Runtimes on Cloud Run are base images that include components and operating system, software required to build and execute code written for a specific programming language, and software to support your function.

![Diagram outlining the stages in the lifecycle of a Cloud Run
runtime](https://docs.cloud.google.com/static/docs/buildpacks/images/runtime-lifecycle.svg)

Runtimes are available in different release stages, such as Preview or General Availability (GA). For more information, see the [product launch stages](https://cloud.google.com/products#product-launch-stages).

## Preview

If you deploy a workload using the Google Cloud CLI when a runtime is in Preview, use the [`gcloud beta run deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/deploy) command. 

## General Availability (GA)

During the [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages) support window:

  * Runtime components are regularly updated with security and bug fixes. 
  * To maintain stability, Cloud Run avoids implementing breaking features or breaking changes into the runtime. Breaking changes will be announced in advance in Cloud Run [release notes](https://docs.cloud.google.com/run/docs/release-notes).



When a language version is no longer actively maintained by the respective community, Cloud Run will also stop providing maintenance and support for that language runtime. Before a runtime reaches the deprecation phase as described in the runtimes support schedule, Google will provide a notification to customers in the Google Cloud console.

Google may make changes to any runtime's support schedule or lifecycle in accordance with the terms of your agreement for the use of Google Cloud services.

## Runtime lifecycle

| GA-level support | Deprecated | Decommissioned  
---|---|---|---  
Creation and redeployment | Yes | Yes | No  
Running existing workloads | Yes | Yes | May be disabled  
Language patches | [As per policy](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates) | [As per policy](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates) | No updates  
Patching [system packages](https://docs.cloud.google.com/docs/buildpacks/stacks) | [As per policy](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates) | [As per policy](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates) | No updates  
Patching OS | [As per policy](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates) | [As per policy](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates) | No updates  
Customer support | GA-level support | No runtime support | No runtime support  
  
## Notification Period

Cloud Run will begin issuing notifications 90 days before the runtime reaches deprecation. Upon notification, you should prepare to upgrade your function to a newer supported runtime.

## Deprecation and Decommissioning

When a component is no longer actively maintained, Cloud Run may deprecate and eventually remove the runtime.

This has three aspects: a publication of the deprecation date, a deprecation period, and a decommission date. In the following schedule, the deprecation date is the start of the deprecation period and ends at the beginning of the decommission date. The decommission date indicates the start of the decommission period.

During the deprecation period, you can generally continue to create new workloads and update existing workloads using the runtime. You should use this time to migrate workloads that use the deprecated runtime to a more up-to-date runtime.

After the decommission date, you can no longer create new workloads or update existing workloads using the runtime. You must choose a more up-to-date runtime to deploy your workloads. Workloads that continue to use a decommissioned runtime may be disabled.

## Support Schedule

Here is the list of supported Cloud Run runtimes, as well as runtimes that have been deprecated or decommissioned.

Based on qualification and stability of releases, availability and key dates might be delayed. A blank deprecation or decommission date means that phase has not yet been scheduled. Revisit this page to stay up to date.

**Note:** **Runtime ID** is often used when deploying from the from the command line or through Terraform

### Node.js

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
Node.js 26   
(Preview) | nodejs26 | 
* google-24 (default)
* google-24-full
| 
* [google-24/nodejs26](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/nodejs26)
* [google-24-full/nodejs26](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/nodejs26)
|  |   
Node.js 24 | nodejs24 | 
* google-24 (default)
* google-24-full
| 
* [google-24/nodejs24](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/nodejs24)
* [google-24-full/nodejs24](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/nodejs24)
| 2028-04-30 | 2028-10-31  
Node.js 22 | nodejs22 | 
* google-22 (default)
* google-22-full
| 
* [google-22/nodejs22](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/nodejs22)
* [google-22-full/nodejs22](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs22)
| 2027-04-30 | 2027-10-31  
Node.js 20 | nodejs20 | 
* google-22 (default)
* google-22-full
| 
* [google-22/nodejs20](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/nodejs20)
* [google-22-full/nodejs20](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs20)
| 2026-04-30 | 2026-10-30  
Node.js 18 | nodejs18 | 
* google-22 (default)
* google-22-full
| 
* [google-22/nodejs18](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/nodejs18)
* [google-22-full/nodejs18](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs18)
| 2025-04-30 | 2025-10-30  
Node.js 16 | nodejs16 |  google-18-full  |  [google-18-full/nodejs16](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs16) | 2024-01-30 | 2025-01-30  
Node.js 14 | nodejs14 |  google-18-full  |  [google-18-full/nodejs14](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs14) | 2024-01-30 | 2025-01-30  
Node.js 12 | nodejs12 |  google-18-full  |  [google-18-full/nodejs12](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs14) | 2024-01-30 | 2025-01-30  
Node.js 10 | nodejs10 |  google-18-full  |  [google-18-full/nodejs10](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs10) | 2024-01-30 | 2025-01-30  
Node.js 8 | nodejs8 |  Decommissioned  |  Decommissioned  | 2020-06-05 | Feb 2021  
Node.js 6 | nodejs6 |  Decommissioned  |  Decommissioned  | 2019-04-17 | Aug 2020  
  
### Python

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
Python 3.14 | python314 | 
* google-24 (default)
* google-24-full
| 
* [google-24/python314](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/python314)
* [google-24-full/python314](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/python314)
| 2030-10-10 | 2031-04-10  
Python 3.13 | python313 | 
* google-22 (default)
* google-22-full
| 
* [google-22/python313](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/python313)
* [google-22-full/python313](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python313)
| 2029-10-10 | 2030-04-10  
Python 3.12 | python312 | 
* google-22 (default)
* google-22-full
| 
* [google-22/python312](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/python312)
* [google-22-full/python312](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python312)
| 2028-10-02 | 2029-04-02  
Python 3.11 | python311 | 
* google-22 (default)
* google-22-full
| 
* [google-22/python311](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/python311)
* [google-22-full/python311](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python311)
| 2027-10-24 | 2028-04-24 | Python 3.10 | python310 | 
* google-22 (default)
* google-22-full
| 
* [google-22/python310](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/python310)
* [google-22-full/python310](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python310)
| 2026-10-04 | 2027-04-04  
Python 3.9 | python39 |  google-18-full  |  [google-18-full/python39](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python39) | 2025-10-05 | 2026-04-05  
Python 3.8 | python38 |  google-18-full  |  [google-18-full/python38](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python38) | 2024-10-14 | 2025-10-14  
Python 3.7 | python37 |  google-18-full  |  [google-18-full/python37](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python37) | 2024-01-30 | 2025-01-30  
  
###  Go 

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
Go 1.27 | go127 | 
* google-24 (default)
* google-24-full
| 
* [google-24/go127](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/go127)
* [google-24-full/go127](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/go127)
| Aug/Sept 2027 | Feb/March 2028  
Go 1.26 | go126 | 
* google-24 (default)
* google-24-full
| 
* [google-24/go126](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/go126)
* [google-24-full/go126](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/go126)
| Feb/March 2027 | Aug/Sept 2027  
Go 1.25 | go125 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go125](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go125)
* [google-22-full/go125](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go125)
| 2026-10-01 | 2027-04-01  
Go 1.24 | go124 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go124](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go124)
* [google-22-full/go124](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go124)
| 2026-09-02 | 2027-03-02  
Go 1.23   
| go123 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go123](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go123)
* [google-22-full/go123](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go123)
| 2026-02-21 | 2026-08-21  
Go 1.22 | go122 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go122](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go122)
* [google-22-full/go122](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go122)
| 2026-01-28 | 2026-07-28  
Go 1.21 | go121 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go121](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go121)
* [google-22-full/go121](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go121)
| 2025-09-03 | 2026-03-03  
Go 1.20 | go120 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go120](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go120)
* [google-22-full/go120](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go120)
| 2024-05-01 | 2025-05-01  
Go 1.19 | go119 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go119](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go119)
* [google-22-full/go119](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go119)
| 2024-04-30 | 2025-01-30  
Go 1.18 | go118 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go118](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go118)
* [google-22-full/go120](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go118)
| 2024-01-30 | 2025-01-30  
Go 1.16 | go116 |  google-18-full  |  [google-18-full/go116](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/go116) | 2024-01-30 | 2025-01-30  
Go 1.13 | go113 |  google-18-full  |  [google-18-full/go113](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/go113) | 2024-01-30 | 2025-01-30  
Go 1.11 | go111 |  Decommissioned  |  Decommissioned  | 2020-08-05 | Feb 2021  
**Note:** Go's [release policy](https://go.dev/doc/devel/release#policy) states that each major Go release is supported until there are two newer major releases. Thus, depending on when newer versions of Go are made publicly available, key dates such as end of support, deprecation, and decommission might be postponed. 

###  Java 

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
Java 25 | java25 | 
* google-24 (default)
* google-24-full
| 
* [google-24/java25](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/java25)
* [google-24-full/java25](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/java25)
| October 2031 |   
Java 21 | java21 | 
* google-22 (default)
* google-22-full
| 
* [google-22/java21](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/java21)
* [google-22-full/java21](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/java21)
| September 2031 |   
Java 17 | java17 | 
* google-22 (default)
* google-22-full
| 
* [google-22/java17](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/java17)
* [google-22-full/java17](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/java17)
| October 2027 |   
Java 11 | java11 |  google-18-full  |  [google-18-full/java11](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/java11) | 2024-10-31 | 2025-10-31  
  
### Ruby

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
Ruby 4.0 | ruby40 |  google-24-full (default)  |  [google-24-full/ruby40](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/ruby40) | 2029-03-31 | 2029-09-30  
Ruby 3.4 | ruby34 | 
* google-22 (default)
* google-22-full
| 
* [google-22/ruby34](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/ruby34)
* [google-22-full/ruby34](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby34)
| 2028-03-31 | 2028-09-30  
Ruby 3.3 | ruby33 | 
* google-22 (default)
* google-22-full
| 
* [google-22/ruby33](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/ruby33)
* [google-22-full/ruby33](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby33)
| 2027-03-31 | 2027-09-30  
Ruby 3.2 | ruby32 | 
* google-22 (default)
* google-22-full
| 
* [google-22/ruby32](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/ruby32)
* [google-22-full/ruby32](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby32)
| 2026-03-31 | 2026-09-30  
Ruby 3.0 | ruby30 |  google-18-full  |  [google-18-full/ruby30](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby30) | 2024-03-31 | 2025-03-31  
Ruby 2.7 | ruby27 |  google-18-full  |  [google-18-full/ruby27](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby27) | 2024-01-30 | 2025-01-30  
Ruby 2.6 | ruby26 |  google-18-full  |  [google-18-full/ruby26](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby26) | 2024-01-30 | 2025-01-30  
  
### PHP

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
PHP 8.5 | php85 |  google-24-full (default)  |  [google-24-full/php85](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/php85) | 2029-12-31 | 2030-06-30  
PHP 8.4 | php84 |  google-22-full (default)  |  [google-22-full/php84](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php84) | 2028-12-31 | 2029-06-30  
PHP 8.3 | php83 |  google-22-full (default)  |  [google-22-full/php83](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php83) | 2027-12-31 | 2028-06-30  
PHP 8.2 | php82 |  google-22-full (default)  |  [google-22-full/php82](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php82) | 2026-12-31 | 2027-06-30  
PHP 8.1 | php81 |  google-18-full  |  [google-18-full/php81](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/php81) | 2025-12-31 | 2026-06-30  
PHP 7.4 | php74 |  google-18-full  |  [google-18-full/php74](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/php74) | 2024-01-30 | 2025-01-30  
  
### .NET

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
.NET 10 | dotnet10 | 
* google-24 (default)
* google-24-full
| 
* [google-24/dotnet10](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/dotnet10)
* [google-24-full/dotnet10](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/dotnet10)
| 2028-11-14 | 2029-05-14  
.NET 8 | dotnet8 | 
* google-22 (default)
* google-22-full
| 
* [google-22/dotnet8](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/dotnet8)
* [google-22-full/dotnet8](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/dotnet8)
| 2026-11-10 | 2027-05-10  
.NET 6 | dotnet6 | 
* google-22 (default)
* google-22-full
| 
* [google-22/dotnet6](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/dotnet6)
* [google-22-full/dotnet6](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/dotnet6)
| 2024-11-12 | 2025-11-12  
.NET Core 3 | dotnet3 |  google-18-full  |  [google-18-full/dotnet3](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/dotnet3) | 2024-01-30 | 2025-01-30  
  
### OS only

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
OS only 24 | osonly24 |  google-24 (default)  |  [google-24/osonly24](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/osonly24) | April 30, 2029 |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
