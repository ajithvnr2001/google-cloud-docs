---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-instance-creation-troubleshooting/
title: Troubleshooting Looker (Google Cloud core) instance creation failures \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:57.589401+00:00
---

# Troubleshooting Looker (Google Cloud core) instance creation failures  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-instance-creation-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Troubleshooting Looker (Google Cloud core) instance creation failures Stay organized with collections  Save and categorize content based on your preferences. 

When a Looker (Google Cloud core) instance creation fails, you can use this troubleshooting guide to resolve issues stemming from instance creation or network validation. The troubleshooting process is broken down into two decision trees based on symptoms:

  * Symptom: Instance creation failure
  * Symptom: Network validation failures



## Symptom: Instance creation failure

If you're encountering a failure while trying to create a Looker (Google Cloud core) instance, use the following decision tree to begin troubleshooting. This tree helps route you to setup guides for first-time deployments, to Sales for discontinued editions or quota increases, to network configuration steps for a Shared VPC, or to specific bug mitigations for intermittent Filestore errors.

**Troubleshooting steps:**

  1. **First-time creation?** If yes, review the [setup guide](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#create_instance) to ensure that all steps were followed.
  2. **Quota Issue?** If you suspect a quota issue, contact your Sales or Account Executive. If you have recently deleted a Looker (Google Cloud core) instance, or if a previous provisioning attempt failed, your project's quota may still be in use. It can take up to 24 hours for the quota to reset. If immediate provisioning is required, contact [Customer Care](https://docs.cloud.google.com/looker/docs/looker-core-support) to request a manual, temporary quota bump to bypass the reset window.
  3. **Trial/Monthly Standard?** If you're using an expired or discontinued edition, refer to current [Looker pricing](https://cloud.google.com/looker/pricing).
  4. **None of the above?** Proceed to the Network Validation Failures tree.



## Symptom: Network validation failures

If you're encountering network validation failures, such as `RANGES_NOT_RESERVED` or `RANGES_EXHAUSTED`, use the following decision tree to troubleshoot. This tree helps identify specific range reservation errors and verify if a Shared VPC is in use. You may be guided to reserve IP ranges, expand existing allocations, or perform manual Looker service account setup steps for Shared VPC environments.

**Troubleshooting steps:**

  1. **RANGES_NOT_RESERVED?** Reserve the necessary IP ranges for your instance.
  2. **RANGES_EXHAUSTED?** Expand the existing IP range allocation.
  3. **Shared VPC?** If you're using a [Shared VPC](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip#shared-vpc), ensure that the Looker service account is enabled and has the `compute.globalAddresses.get` permission.
  4. **None of the above?** Contact [Support](https://docs.cloud.google.com/looker/docs/looker-core-support) if you need further assistance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
