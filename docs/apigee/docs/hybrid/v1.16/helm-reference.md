---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/helm-reference/
title: Apigee hybrid Helm reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:23.812814+00:00
---

# Apigee hybrid Helm reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/helm-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee hybrid Helm reference Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/helm-reference.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/helm-reference.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/helm-reference.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/helm-reference.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/helm-reference.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/helm-reference.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-reference.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/helm-reference.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/helm-reference.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/helm-reference.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/helm-reference.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/helm-reference.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/helm-reference.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/helm-reference.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/helm-reference.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/helm-reference.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/helm-reference.html)



## Helm supported version

Apigee hybrid supports Helm v3.14.2+. 

## Helm charts for Apigee hybrid components

The hybrid components are installed and managed by the following Helm charts. The table is arranged in the order you will typically install them in during a fresh installation. 

Scope| Components| Helm chart  
---|---|---  
**Apigee operator** | Apigee operator | `apigee-operator`  
**Storage** | Cassandra | `apigee-datastore`  
**In‑memory storage** | Redis | `apigee-redis`  
**Reporting** | Logger  
Metrics | `apigee-telemetry`  
**Ingress** | Apigee Ingress gateway | `apigee-ingress-manager`  
**Organization** | Apigee Connect Agent  
MART  
UDCA  
Watcher | `apigee-org`  
**Environment** | Runtime  
Synchronizer | `apigee-env`  
**Environment group** | virtualhost | `apigee-virtualhost`  
**Note:** The hybrid Helm charts depend on the Apigee hybrid Custom Resource Definitions (CRDs) being installed. See [Install the Apigee hybrid CRDs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-crds) in the Installation guide.

## Recommended upgrade order

We recommend that you upgrade the Helm charts in the following order:

  1. `apigee-operator`
  2. `apigee-datastore`
  3. `apigee-telemetry`
  4. `apigee-redis`
  5. `apigee-ingress-manager`
  6. `apigee-org`
  7. `apigee-env`
  8. `apigee-virtualhost`



## Service accounts and Helm charts

The following table lists the Google Cloud service accounts used by the Apigee Helm charts:

Apigee Helm chart | Service account | IAM roles  
---|---|---  
`apigee-operator` | `apigee-guardrails` | [Service Usage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer)  
`apigee-datastore` | `apigee-cassandra` | [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin)  
`apigee-telemetry` | `apigee-logger`  
`apigee-metrics` | [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter)  
[Monitoring Metric Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter)  
`apigee-org` | `apigee-mart`  
`apigee-watcher`  
`apigee-mint-task-scheduler` (optional) | [Apigee Connect Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect#apigeeconnect.Agent)  
[Apigee Runtime Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.runtimeAgent)  
No role required  
`apigee-env` | `apigee-runtime`  
`apigee-synchronizer` | No role required  
[Apigee Synchronizer Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.synchronizerManager), [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin)  
  
See: [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about)

* * *

**Note:** The `apigeectl` command-line tool has not been supported since Apigee hybrid v1.11. For information on using `apigeectl` in v1.11, see [apigeectl reference (v1.11)](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cli-reference). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
