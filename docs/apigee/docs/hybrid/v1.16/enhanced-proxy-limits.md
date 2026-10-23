---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits/
title: Enhanced per-environment proxy limits \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:57.971791+00:00
---

# Enhanced per-environment proxy limits  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enhanced per-environment proxy limits Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enhanced-proxy-limits.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/enhanced-proxy-limits.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/enhanced-proxy-limits.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/enhanced-proxy-limits.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/enhanced-proxy-limits.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enhanced-proxy-limits.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/enhanced-proxy-limits.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/enhanced-proxy-limits.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/enhanced-proxy-limits.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/enhanced-proxy-limits.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/enhanced-proxy-limits.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/enhanced-proxy-limits.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/enhanced-proxy-limits.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/enhanced-proxy-limits.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/enhanced-proxy-limits.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/enhanced-proxy-limits.html)



## Overview

New Apigee hybrid organizations can be provisioned with the ability to deploy more than 50 proxies per environment enabled. This feature is also available for [Apigee X](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#api-proxies). 

  * The maximum number of deployed API proxies and shared flows per organization is 6000. 
  * The maximum number of proxy deployment units per Apigee instance is 6000. 
  * The maximum number of API base paths per Apigee organization is 6000. 



When more than 50 proxies are deployed in an environment, Apigee will automatically partition the environment into several distinct replica sets, each containing a subset of proxies deployed in the environment. These replica subsets are equivalent in behavior to a single environment in the way it loads and runs a set of proxies and other environment resources. This will be transparent to the user, and you can continue to use the environment as you would a single environment. 

**Note:** Enhanced proxy limits feature is only available for new hybrid organizations. This feature is available exclusively as part of the [2024 subscription plan](https://cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements#subscription-2024-entitlements), and is subject to the entitlements granted under that subscription. They cannot be enabled on existing organizations. 

## Provisioning

To provision a new org with the enhanced number of proxies per environment: 

  1. Provide your project ID and organization name to your Apigee representative to set up the enhanced proxy limit. 
  2. Follow the Apigee hybrid [installation instructions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-before-begin) to provision the hybrid org. In your overrides file, add the [`enhanceProxyLimits`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#enhanceproxylimits) top-level property: 
         
         enhanceProxyLimits: true
         

Apply changes to `enhanceProxyLimits` by updating the `apigee-org` chart and the `apigee-virtualhost` chart for every environment group.

**Alert:** Do not change this value once set. 
  3. Create and deploy a proxy. 
  4. Verify that the enhanced proxy limits are enabled: 
     1. Get the name of the configmap for your Apigee namespace: 
            
            kubectl get configmap -n APIGEE_NAMESPACE

Your output should look similar to the following: 
            
            NAME                                                             DATA   AGE
            ...
            _apigee-synchronizer-hybr-example-env-dggroupconfi-bc7726a_       3      12m
            ...

     2. Check the named configmap: 
            
            kubectl get configmap -n APIGEE_NAMESPACE CONFIGMAP_NAME -o yaml

Where `CONFIGMAP_NAME` is the name of the configmap from the previous step. 

Your output should look similar to the following: 
            
            kubectl get configmap -n apigee apigee-synchronizer-hybr-example-env-dggroupconfi-bc7726a -o yaml
            apiVersion: v1
            data:
            contract.revid: "2"
            contract.uid: 4a792429-20fb-4b29-bed3-3f8ce7b3353e
            deploymentGroups: auto-2ecde5ae-04
            kind: ConfigMap
            metadata:
            creationTimestamp: "2024-05-15T20:04:26Z"
            labels:
                apigee.cloud.google.com/platform: apigee
            name: apigee-synchronizer-hybr-test-env-dggroupconfi-bc7726a
            namespace: apigee
            ownerReferences:
            - apiVersion: apigee.cloud.google.com/v1alpha2
                blockOwnerDeletion: true
                controller: true
                kind: ApigeeEnvironment
                name: hybrid-dev--test-env-4f37f70
                uid: 696e84ec-5c54-4858-a2e0-e36db5ff3506
            resourceVersion: "2520100"
            uid: b297bd33-300a-48cf-bf85-6c7cd0ff288f
            

  5. Check for the existence of runtime pods containing the substring `auto`: 
         
         kubectl get pods -n APIGEE_NAMESPACE | grep auto

Your output should look similar to the following: 
         
         kubectl get pods -n apigee | grep auto
         apigee-runtime-hybr-test-env-auto-2ecde5a-bca5298-4gsrw   1/1     Running     0                98m




## Limitations

Apigee offers enhanced per-environment proxy limits only on newly created orgs. Converting existing orgs to use enhanced proxy limits is not supported. 

Backups of an organization that was created without enhanced proxy limits enabled cannot be restored to an organization created with the feature enabled. 

## Known issues

  * Proxy chaining: 
    * Proxy chaining with mTLS is not supported. See [known issue 392135466](https://docs.cloud.google.com/apigee/docs/release/known-issues#392135466). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
