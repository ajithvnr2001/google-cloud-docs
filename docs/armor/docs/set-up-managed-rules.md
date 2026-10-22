---
url: https://docs.cloud.google.com/armor/docs/set-up-managed-rules/
title: Set up managed rules \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:26.228990+00:00
---

# Set up managed rules  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/set-up-managed-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Set up managed rules Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to enable, configure, and manage updates for Google Cloud Armor managed rules.

## Deployment and update strategies

When configuring Cloud Armor managed rules, select one of the following version strategies depending on your organization's risk tolerance:

  * **`stable` (production-validated, recommended):** Google automatically updates the rules (or expedites updates for zero-day rules). This is a safe baseline recommended for production traffic.
  * **`canary` (early access):** Google automatically updates the rules with early-exposure signatures. We recommend running in preview mode ahead of the stable version.



## Configuration use cases

This section describes common use cases for setting up managed rules.

### Set up managed rules by category

To use managed rules, you create a security policy, add the managed rules category to the policy, and attach the policy to a backend service.

  1. Create a security policy:
         
         gcloud compute security-policies create POLICY_NAME \
             --global
         

  2. Add the stable SQL injection (`sqli`) managed rules to the policy with a deny action:
         
         gcloud compute security-policies rules create 100 \
             --security-policy POLICY_NAME \
             --action deny-403 \
             --expression "evaluateManagedRules('google:sqli:stable')"
         

  3. Attach the security policy to your backend service:
         
         gcloud compute backend-services update BACKEND_SERVICE \
             --global \
             --security-policy POLICY_NAME
         

A Cloud Armor security policy doesn't take effect until you attach it to a backend service. Attaching the policy enables Cloud Armor to inspect and protect incoming traffic sent to that backend service.

Replace the following:

     * `POLICY_NAME`: the name of the security policy
     * `BACKEND_SERVICE`: the name of the backend service that you want to protect



### Evaluate new rules with canary preview mode

Deploying the `canary` version in preview mode alongside the `stable` version in enforced mode lets you evaluate new rules in logs before they start blocking live traffic.

  1. Add the canary version of managed rules in preview mode at a higher priority (priority 100):
         
         gcloud compute security-policies rules create 100 \
             --security-policy POLICY_NAME \
             --action deny-403 \
             --expression "evaluateManagedRules('google:xss:canary')" \
             --preview
         

  2. Add the stable version of managed rules in enforced mode at a lower priority (priority 200):
         
         gcloud compute security-policies rules create 200 \
             --security-policy POLICY_NAME \
             --action deny-403 \
             --expression "evaluateManagedRules('google:xss:stable')"
         




## What's next

  * [Review Logging and monitoring metrics](https://docs.cloud.google.com/armor/docs/request-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
