---
url: https://docs.cloud.google.com/workstations/docs/limit-workstations-per-developer/
title: Limit the number of workstations per developer \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:09.457696+00:00
---

# Limit the number of workstations per developer  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/limit-workstations-per-developer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Limit the number of workstations per developer Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how Cloud Workstations Admins can limit the number of workstations created per developer per workstation configuration. 

This helps you control costs incurred by workstations.

To learn more about pricing see [Cloud Workstations pricing](https://cloud.google.com/workstations/pricing).

## Limit the number of workstations per workstation configuration

To limit developers so they can create only one workstation per workstation configuration, run the following `gcloud` CLI command:
    
    
        gcloud workstations configs create CONFIG \
            --cluster=CLUSTER \
            --region=REGION \
            --project=PROJECT \
            --max-usable-workstations-count 1
    

**Note:** The default value for `maxUsableWorkstations` is 0, which means a developer can create an unlimited number of workstations.

The `maxUsableWorkstations` limit is only enforced in the `CreateWorkstation` API for developers with **Cloud Workstations Creator** permissions.

The limit is not enforced when a **Cloud Workstations Admin** creates additional workstations for a configuration and grants `workstations.workstation.use` to a specific developer.

## Exempting users from maximum usable workstation limit

A _Cloud Workstations Admin_ can also exempt developers from this limit by granting them `roles/workstations.workstationLimitExemptedCreator` role.

For more information about granting this role, see [Access control with IAM and Cloud Workstations](https://docs.cloud.google.com/workstations/docs/access-control#workstations-limit-exempted-creator).

## What's next

  * See a list of [workstation configuration parameters](https://docs.cloud.google.com/workstations/docs/customize-development-environment).
  * [Set up security best practices](https://docs.cloud.google.com/workstations/docs/set-up-security-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
