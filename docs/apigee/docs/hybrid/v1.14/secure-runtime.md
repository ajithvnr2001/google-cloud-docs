---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/secure-runtime/
title: Securing the runtime installation \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:49:19.535069+00:00
---

# Securing the runtime installation  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/secure-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Securing the runtime installation Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/secure-runtime.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/secure-runtime.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/secure-runtime.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/secure-runtime.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/secure-runtime.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/secure-runtime.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/secure-runtime.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/secure-runtime.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/secure-runtime.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/secure-runtime.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/secure-runtime.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/secure-runtime.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/secure-runtime.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/secure-runtime.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/secure-runtime.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/secure-runtime.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/secure-runtime.html)



A typical Apigee hybrid installation is made of multiple pods, as listed in the following table. Each of these pods require specific access to ports, and not every pod needs to communicate with every other pod. For a detailed map of these internal connections and the security protocols they employ, see [Internal connections](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/ports#internal).

Pod | Description  
---|---  
`apigee-logger` | Contains an Apigee logger agent that sends application logs to Cloud Operations.   
`apigee-metrics` | Contains an Apigee metrics agent that sends application logs to Cloud Operations.   
`apigee-cassandra` | Contains the hybrid runtime persistence layer.  
`apigee-synchronizer` | Synchronizes configuration between the management (control) plane and runtime (data) plane.  
`apigee-udca` | Allows transfer of analytics data to the management plane.  
`apigee-mart` | Contains the Apigee administrative API endpoint.  
`apigee-runtime` | Contains the gateway for API request processing and policy execution.  
  
Google recommends that you follow these methods and best practices to harden, secure, and isolate the runtime pods:

Method | Description  
---|---  
Kubernetes security overview | Review the Google Kubernetes Engine (GKE) document [ Security overview](https://cloud.google.com/kubernetes-engine/docs/concepts/security-overview). This document provides an overview of each layer of your Kubernetes infrastructure, and explains how you can configure its security features to best suit your needs. For Google Kubernetes Engine's current guidance for hardening your GKE cluster, see [ Hardening your cluster's security](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).  
Network policies |  Use network policies to restrict communication between Pods and to pods that have access outside the Kubernetes network. For more information, see [ Creating a cluster network policy](https://cloud.google.com/kubernetes-engine/docs/how-to/network-policy) in the GKE documentation.  A network policy is a specification of how groups of pods are allowed to communicate with each other and other network endpoints. The Kubernetes [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/#the-networkpolicy-resource) resource uses labels to select pods and define rules which specify what traffic is allowed to the selected pods.  You can implement a Container Network Interface (CNI) plugin to add network policies to an Apigee hybrid runtime installation. Network policies let you isolate pods from outside access and enable access to specific pods. You can use an open source CNI plugin, such as [Calico](https://docs.tigera.io/calico/3.25/about) to get started.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
