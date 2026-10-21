---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/uninstall/
title: Uninstall hybrid runtime \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:09:54.807998+00:00
---

# Uninstall hybrid runtime  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/uninstall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Uninstall hybrid runtime Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/uninstall.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/uninstall.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/uninstall.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/uninstall.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/uninstall.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/uninstall.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/uninstall.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/uninstall.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/uninstall.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/uninstall.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/uninstall.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/uninstall.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/uninstall.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/uninstall.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/uninstall.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/uninstall.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/uninstall.html)



## Uninstall Apigee hybrid

**Note:** These commands are procedures are intended to uninstall hybrid installations managed with Helm. If you are uninstalling an earlier version of Apigee hybrid managed with `apigeectl`, see [Uninstall hybrid runtime](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/uninstall#apigeectl-installations) in the hybrid v1.11 documentation for uninstallation procedures.

Use the following commands to uninstall the hybrid runtime:

  1. Uninstall the resources in your `apigee` namespace: 
         
         helm uninstall -n apigee ENV_GROUP_RELEASE_NAME ENV_RELEASE_NAME $ORG_NAME ingress-manager telemetry redis datastore
         

     * ENV_GROUP_RELEASE_NAME is the name with which you previously installed the `apigee-virtualhost` chart. In hybrid v1.10, it is usually `apigee-virtualhost-ENV_GROUP`. In Hybrid v1.11 and newer it is usually ENV_GROUP.
     * ENV_RELEASE_NAME is the name with which you previously installed the `apigee-env` chart. In hybrid v1.10, it is usually `apigee-env-ENV_NAME`. In Hybrid v1.11 and newer it is usually ENV_NAME.
     * ORG_NAME is the name with which you previously installed the `apigee-org` chart. It is usually your organization name. If you have defined an ORG_NAME environment variable, you can use that variable in your command.
  2. After uninstalling the resources in the `apigee` namespace, uninstall `apigee-operator`. 
         
         helm uninstall -n apigee-system operator

  3. Delete the Apigee CRDs: 
         
         kubectl delete -k  apigee-operator/etc/crds/default/




Use the following command to remove cert-manager: 

**Note:** Some Google Distributed Cloud versions come with their own bundled version of cert-manager. If for certain reasons, you need to remove this bundled cert-managar and install your own cert-manager, follow the instructions in [Conflicting `cert-manager` installation](https://cloud.google.com/anthos/clusters/docs/on-prem/1.13/known-issues#conflicting-cert-manager-installation) to avoid conflicts. 
    
    
    kubectl -n cert-manager delete secret apigee-ca

If you have a multi-region installation, and you want to install Apigee hybrid again on the same region, you need to follow the instructions for copying the `apigee-ca` secret in [Multi-region deployment on GKE and GKE on-prem](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/multi-region#set-up-the-new-region).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
