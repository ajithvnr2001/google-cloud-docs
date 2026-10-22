---
url: https://docs.cloud.google.com/stackdriver/docs/support-info/telemetry-agents/
title: Support time horizons for the Ops Agent and Google-Built OpenTelemetry Collector \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:06.259118+00:00
---

# Support time horizons for the Ops Agent and Google-Built OpenTelemetry Collector  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/support-info/telemetry-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Support time horizons for the Ops Agent and Google-Built OpenTelemetry Collector Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) and [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel) are supported. This document doesn't apply to the [legacy Monitoring agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/monitoring) or the [legacy Logging agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging); for deprecation information about these agents, see [Cloud Logging and Monitoring agents deprecation policy](https://docs.cloud.google.com/stackdriver/docs/agent-deprecation-policy).

Google Cloud Observability defines three support modes for versions of the Ops Agent and Google-Built OpenTelemetry Collector:

  * **Active support**, for two years: Users of a new minor version get active support for two years after release.
  * **Keep the Lights On (KTLO)**, for the next one year: During this period, packages remain available for installation.
  * **Unsupported**, for anything beyond three years: Users with existing deployments can continue to collect telemetry, but there is no support or assurance of installation-package availability.



## Support modes and durations

The following table summarizes each support mode, and the linked subsections provide additional information:

| Active support  
(years 1 and 2) | KTLO  
(year 3) | Unsupported  
(after year 3)  
---|---|---|---  
Bug fixes & security patches |  |  |   
New distro support |  |  |   
Case support |  |  |   
Upgrade support |  |  |   
Fleet-wide installation |  |  |   
Manual installation |  |  | Possibly  
Telemetry ingestion |  |  |   
  
### Active support mode

Each minor version of the Ops Agent and the Google-Built OpenTelemetry Collector gets active support for two years after release. During this period, users can expect the following:

  * Regular bug fixes and feature upgrades, applied as a new version.
  * Security scanning and patches, applied as new a version.
  * Support for new distro releases, applied as a new version.
  * Support cases accepted for the Ops Agent and Google-Built OpenTelemetry Collector.
  * Compatibility with Google fleet-wide management tools.
  * Ability to migrate or upgrade to the latest version from any version in active-support mode.
  * For Google-Built OpenTelemetry Collector, container image vulnerabilities fixed for the current version and released in the subsequent version.



### KTLO support mode

After two years of active support, each minor version moves to KTLO support. During this period, users can expect the following:

  * No bug fixes, unless the issue exists also exists in the latest version, where it will be fixed for the next version.
  * No releases to support new distros.
  * No support cases accepted.
  * Packages and repositories for installation of the version remain available, so users can still install the version manually or by using Google fleet-wide management tools.
  * No migration or upgrade assistance beyond the documentation.
  * Google fleet-wide management tools that were available and compatible during the active-support period continue to be available.



### Unsupported mode

After the period of KTLO support, each minor version moves to the unsupported mode. During this period, users can expect the following:

  * Existing deployments can still send telemetry. Users with existing unsupported deployments won't experience broken workflows unless something outside the Ops Agent or Google-Built OpenTelemetry Collector, like a logs or metrics API, changes.
  * New installations might be possible but are strongly discouraged.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
