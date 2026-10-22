---
url: https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle/
title: Runtime lifecycle \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:09.520501+00:00
---

# Runtime lifecycle  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/flexible/resources)



Send feedback 

#  Runtime lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

The App Engine flexible environment [runtimes](https://docs.cloud.google.com/appengine/docs/flexible) use open source components that are maintained by their respective communities. The runtimes are identified by their language version, for example, Java 17, Python 3.10, and so forth.

![Diagram outlining the stages in the lifecycle of an App Engine runtime](https://docs.cloud.google.com/static/appengine/docs/images/appengine-runtime-lifecycle.svg)

Google provides support for a runtime during [General availability (GA)](https://cloud.google.com/products/#product-launch-stages). During this support window:

  * Runtime components are regularly updated with security and bug fixes.
  * To maintain stability, App Engine avoids implementing breaking features or changes into the runtime. Breaking changes will be announced in advance on the runtime-specific [release notes](https://docs.cloud.google.com/appengine/docs/flexible/resources#release-notes).



When a language version is no longer actively maintained by the respective community, App Engine will also stop providing maintenance and support for that language runtime. Before a runtime reaches the end of support phase as described in the [runtimes support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule), Google will provide a notification to customers.

Google may make changes to any runtime's support schedule or lifecycle in accordance with the terms of your agreement for the use of Google Cloud platform services.

## Custom runtimes

[Custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/about-custom-runtimes) allow you to define new runtime environments which may include additional components like language interpreters or application servers.

Custom runtimes are not impacted by the runtime lifecycle policy.

## Runtime lifecycle

| GA-level support | End of Support | Deprecated | Decommissioned  
---|---|---|---|---  
Creation & redeployment | Yes | No | No | No  
Project Configuration Updates | Yes | Yes | No | No  
Running existing workloads | Yes | Yes | Yes | No  
UI & CLI Warnings | Yes | Yes | No | No  
Language patches | Automatic | No automatic updates | No automatic updates | No automatic updates  
Patching APIs & SDKs | Automatic | No automatic updates | No automatic updates | No automatic updates  
Customer Support | GA-level support | No runtime support | No runtime support | No runtime support  
  
### Notification period

App Engine will begin issuing in-app notifications 90 days before the application reaches end of support. Upon notification, you should prepare to upgrade your application to a newer runtime that is supported in the flexible environment .

### End of support

**Important:** Google will no longer apply security updates or patches to components of the runtime environment that have reached end of support. To continue receiving security updates, we strongly encourage you to upgrade your application to a supported runtime version as soon as it becomes available. 

When runtime components reach the end of support date:

  * Google will no longer apply security updates or patches to components of the runtime environment.
  * Your application will continue to run and receive traffic.
  * You will no longer be able to create and/or update the application on the unsupported runtime.
  * Issues arising from the use of an unsupported runtime will not be eligible for technical support



We strongly encourage you to upgrade your application to a supported runtime version as soon as it becomes available to continue receiving security updates and being eligible for technical support.

Alternatively, you can redeploy your application using a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/about-custom-runtimes). 

### Deprecated

If Google allowed your Organization to re-enable deployments in an unsupported runtime, Google will remove that ability once the runtime is deprecated.

Where practicable, we will make reasonable efforts to notify you in advance of the deprecation by in-app notifications or other means. In certain instances, including in circumstances involving critical security vulnerabilities or similar high severity issues, advance notice may not be practicable.

### Decommissioned

Applications that continue to use a decommissioned runtime may be disabled without further notice. You must choose a more up-to-date runtime to deploy your application.

See the runtimes [support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule) for key dates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
