---
url: https://docs.cloud.google.com/kms/docs/org-policy-constraints/
title: Organization policy constraints for Cloud KMS \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:29.572464+00:00
---

# Organization policy constraints for Cloud KMS  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/org-policy-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Organization policy constraints for Cloud KMS Stay organized with collections  Save and categorize content based on your preferences. 

This page provides supplemental information about [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) constraints that let you enforce limitations for Cloud Key Management Service. You can use these constraints to limit resource locations or allowed protection levels for Cloud KMS keys across an entire project or organization.

You can also use [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) to enforce the use of CMEK in your organization and use organization policies to [control key destruction](https://docs.cloud.google.com/kms/docs/control-key-destruction).

## Cloud KMS constraints

The following constraints can be applied to an organization policy and relate to Cloud Key Management Service.

### Enforce resource locations

**API Name** : `constraints/gcp.resourceLocations`

When you apply the `resourceLocations` constraint, you specify one or more [locations](https://docs.cloud.google.com/kms/docs/locations#location_types). Once set, creation of new resources (e.g key rings, keys, key versions) is limited to the specified locations.

Keys in other locations, created or imported before the constraint was applied, will remain usable. However, [key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) (automated creation of a new primary key version) will fail if the result would be a new key version in a disallowed location.

**Note:** Enabling or disabling `resourceLocations` may take up to 10 minutes to go into effect.

### Allowed protection levels

**API Name** : `constraints/cloudkms.allowedProtectionLevels`

When you apply the `allowedProtectionLevels` constraint, you specify one or more [protection levels](https://docs.cloud.google.com/kms/docs/algorithms#protection_levels). Once set, new keys, key versions, and import jobs must use one of the specified protection levels.

Keys with other protection levels, created before the constraint was applied, will remain usable. However, [key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) (automated creation of a new primary key version) will fail if the result would be a new key version with a disallowed protection level.

**Note:** Enabling or disabling `allowedProtectionLevels` may take up to 10 minutes to go into effect.

## What's next

  * Learn about [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) and using organization policies to [control key destruction](https://docs.cloud.google.com/kms/docs/control-key-destruction).
  * Learn about the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail) that applies to organization policies.
  * See [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) for instructions on working with constraints and organization policies in the Google Cloud console.
  * See [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints) for instructions on working with constraints and organization policies in the gcloud CLI.
  * See the Resource Manager API [reference documentation](https://docs.cloud.google.com/resource-manager/reference/rest) for relevant API methods, such as [`projects.setOrgPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
