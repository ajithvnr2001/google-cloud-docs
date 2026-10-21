---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/logging-view/
title: View logs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:06:56.726719+00:00
---

# View logs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/logging-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  View logs Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/logging-view.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/logging-view.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/logging-view.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/logging-view.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/logging-view.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/logging-view.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/logging-view.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/logging-view.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/logging-view.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/logging-view.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/logging-view.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/logging-view.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/logging-view.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/logging-view.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/logging-view.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/logging-view.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/logging-view.html)



This topic explains how to [view log data](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) by using the Logs Explorer in the Google Cloud console or by using the `kubectl logs` command. 

**Note:** Ingress logs are managed through Anthos Service Mesh (ASM). To view access logs, refer to [Accessing logs in Cloud Logging](https://docs.cloud.google.com/service-mesh/v1.12/docs/observability/accessing-logs) in the ASM documentation.

## View logs in the Logs Explorer

This section explains how to view Apigee hybrid logs in the Logs Explorer or directly by using `kubectl`. 

Logging is provided by default on GKE and GKE on-prem. On these platforms, be sure that you have disabled logging in your overrides file by setting `logger.enabled` to `false`. On AKS, you must explicitly enable logging by setting `logger.enabled` to `true` in your overrides file.

If you are on GKE or Anthos GKE, logs are automatically sent to [Cloud Logging](https://docs.cloud.google.com/monitoring/kubernetes-engine).

**To view logs in the Logs Explorer:**

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Resource type** drop-down list, select **Kubernetes Container** , the name of your cluster, and your namespace ID.

For more information, see [View logs](https://docs.cloud.google.com/logging/docs/view/overview) in the Google Cloud console documentation.




The following example shows hybrid log output in the Logs Explorer:

![](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.11/images/logging-explorer-k8s-container.png)

## View log files directly

You can view the logs that are written to each pod's filesystem directly using [`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/), as follows:
    
    
    kubectl logs pod_name -n namespace

For example:
    
    
    kubectl logs apigee-mp-hybrid-docs-test-blue-6fb96f5b9-2k8hp -n my-namespace

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
