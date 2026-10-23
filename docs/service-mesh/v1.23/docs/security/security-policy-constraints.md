---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/security/security-policy-constraints/
title: Cloud Service Mesh security policy constraints \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:20.678147+00:00
---

# Cloud Service Mesh security policy constraints  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/security/security-policy-constraints/

You are viewing archived v1.23 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.23/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh security policy constraints

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This guide does not support `TRAFFIC_DIRECTOR` [control plane implementation](https://docs.cloud.google.com/service-mesh/v1.23/docs/check-control-plane-implementation).

Cloud Service Mesh with Istio APIs provides you with powerful and flexible APIs that you can use to configure your mesh. However, without proper management over these resources, your mesh might expose security vulnerabilities. Integrating [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) with Cloud Service Mesh security policy constraints can help enforce your mesh with security best practices and prevent vulnerabilities.

This page assumes you are already familiar with [policy constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints).

## Constraints templates

When you [install Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller), select **Install default template library**. This option deploys all of the Cloud Service Mesh security policy constraint templates needed for your mesh. For a full list of the Cloud Service Mesh security constraint templates, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library) and look for templates that are prefixed with `Asm`.

## Constraints bundle

We offer an out-of-box constraints bundle for Cloud Service Mesh security policy. For the bundle details and instructions, see [Using Cloud Service Mesh security policies](https://docs.cloud.google.com/anthos-config-management/docs/how-to/using-asm-security-policy).

To follow a tutorial that shows you how to apply this bundle, see [Strengthen your app's security with Cloud Service Mesh, Config Sync, and Policy Controller](https://docs.cloud.google.com/service-mesh/v1.23/docs/strengthen-app-security).

## Add-on constraints

Some constraint templates are installed with the default template library, but not included in the security policy bundle. These constraint templates serve specific use cases, and you can configure your own constraints:

  * [AsmAuthzPolicyDisallowedPrefix](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmauthzpolicydisallowedprefix)
  * [AsmAuthzPolicyEnforceSourcePrincipals](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmauthzpolicyenforcesourceprincipals)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
