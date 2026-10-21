---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-namespace/
title: Step 3: Create the apigee namespace \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:44:40.611803+00:00
---

# Step 3: Create the apigee namespace  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-namespace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 3: Create the apigee namespace Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-namespace.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-namespace.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-create-namespace.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-create-namespace.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-namespace.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-namespace.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-namespace.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-namespace.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-namespace.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-create-namespace.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-create-namespace.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-create-namespace.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-create-namespace.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-create-namespace.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-create-namespace.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-create-namespace.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-create-namespace.html)



This step explains how to create the `apigee` Kubernetes namespace in which most Apigee hybrid components operate. 

Create the namespace that will be used for most Apigee hybrid resources. This should match the `namespace` field in the `overrides.yaml` file. If this is not present in `overrides.yaml`, the default namespace is `apigee`. 

**Note:** You can use any namespace. `apigee` is the default namespace. If you use a different namespace, be sure to replace `apigee` with the name of your namespace in the following commands. 

  1. Check if the namespace already exists:
         
         kubectl get namespace apigee

If the namespace exists, your output includes:
         
         NAME     STATUS   AGE
         apigee   Active   1d

  2. If the namespace does not already exist, create it:
         
         kubectl create namespace apigee




Now that hybrid has a space to operate in, the next step is to create the Google Cloud service accounts and credentials required to configure hybrid runtime components

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-namespace) [(NEXT) Step 4: Set up service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-overrides) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-cert-manager) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-crds) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-check-cluster) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-helm-charts) [12](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-workload-identity)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
