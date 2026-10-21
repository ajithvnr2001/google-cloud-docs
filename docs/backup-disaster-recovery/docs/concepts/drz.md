---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/drz/
title: Data residency for backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:43:49.413425+00:00
---

# Data residency for backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/drz/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Reference ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference)



Send feedback 

#  Data residency for backup vault Stay organized with collections  Save and categorize content based on your preferences. 

Data residency organizational policy is not supported on workloads that require a management server and backup/recovery appliance. 

This page describes the data residency support for backup vault, including supported workloads and limitations.

Data residency for backup vault meets compliance and regulatory requirements by allowing you to limit the geographic locations (regions) where Google Cloud data is stored at rest according to [Service Specific Terms](https://cloud.google.com/terms/service-terms). With data residency, organization policy administrators can enforce geographic locations where backup data can be stored.

Organizations with data residency requirements can set up a [Resource Locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) organization policy constraint that restricts the location of new backup resources at the organization, project, or folder level of their resource hierarchy.

## Data residency and organization policy constraints

With Google Cloud's [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints), you can define the geographic locations where your resources are created. If your organization policy uses the [resource location constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) (`constraints/gcp.resourceLocations`), any new Backup and DR resources you create must adhere to this constraint.

This location constraint is only checked when new resources are created. For example, if you apply the policy after you've already created some Backup vaults, those existing resources won't be affected. However, the policy does apply to the following:

  * New resources created by existing backup plans.
  * Manually triggered restore operations.
  * New backup plans.



Any of these operations will fail if it violates the resource location constraint.

## Data residency compatibility

Data residency enforcement can be used with all workloads that don't depend on a management server and backup/recovery appliance.

Customers still have complete control over the location of backups managed by management servers and backup/recovery appliances, through the configuration options in the management server. However, these workloads are not constrained by the organizational policies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
