---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-org-policies/
title: About organization policies \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:38.794856+00:00
---

# About organization policies  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-org-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About organization policies Stay organized with collections  Save and categorize content based on your preferences. 

This document describes [organization policies](https://docs.cloud.google.com/organization-policy/overview) for Memorystore for Valkey. [Organization policy administrators](https://docs.cloud.google.com/organization-policy/create-organization-policies#delegate-admin) use these policies to set restrictions on how users configure instances for an organization.

Organization policies give you centralized, programmatic control over your organization's resources. These policies contain rules, called [_constraints_](https://docs.cloud.google.com/organization-policy/overview#constraints), that an organization policy administrator places on a project, folder, or organization. Constraints enforce a policy across all instances. For example, if you try to create an instance in an organization, project, or folder that has an organization policy, then the constraint runs a check to ensure that the instance configuration follows the requirements of the constraint. If the check fails, then Memorystore for Valkey doesn't create the instance.

When you add projects to an organization or folder that uses an organization policy, the projects inherit the constraints of that policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#hierarchy_evaluation_rules).

## Types of organization policies

The following types of organization policies are specific to Memorystore for Valkey:

  * Predefined organization policies
  * Custom organization policies



### Predefined organization policies

You can use the predefined constraints of organization policies to control the customer-managed encryption key (CMEK) settings of Memorystore for Valkey instances. For more information, see [Ensure CMEK protection for your instances by using predefined organization policy constraints](https://docs.cloud.google.com/memorystore/docs/valkey/use-predefined-org-policies).

#### CMEK organization policy constraints

Memorystore for Valkey supports organization policy constraints for CMEK. By using these constraints, you can enforce CMEK protection for your instances and control which [Cloud Key Management Service (KMS) keys](https://docs.cloud.google.com/kms/docs/resource-hierarchy) you can use to help protect your data.

Memorystore for Valkey supports the following organization policy constraints that help ensure CMEK protection across an organization:

  * `constraints/gcp.restrictNonCmekServices`: use this constraint to enforce CMEK protection for your instances. If the [Memorystore for Valkey API](https://docs.cloud.google.com/kms/docs/cmek-org-policy) is in the `Deny` policy list of services for this constraint, then you can't create non-CMEK-protected instances.
  * `constraints/gcp.restrictCmekCryptoKeyProjects`: use this constraint to limit which Cloud KMS keys you can use for CMEK protection. If you configure this constraint, then the instances that use CMEK encryption must use a key from an allowed project, folder, or organization.



These constraints help ensure CMEK protection across an organization and are enforced only on newly created Memorystore for Valkey instances. For more information, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) and [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).

### Custom organization policies

If you want granular, customizable control over either non-CMEK settings or specific fields that are restricted in your organization policies, then you can create custom constraints and use the constraints in a custom organization policy. By using custom organization policies, you can improve the security, compliance, and governance of your Memorystore for Valkey instances by enforcing consistent configurations and restrictions for the instances. This ensures that your instances adhere to security best practices and regulatory requirements.

To learn how to create custom organization policies, see [Enforce consistent configurations and restrictions for your instances by using custom organization policy constraints](https://docs.cloud.google.com/memorystore/docs/valkey/use-custom-org-policies). You can also view a list of [supported custom constraints and operations](https://docs.cloud.google.com/memorystore/docs/valkey/use-custom-org-policies#supported-custom-constraints-and-operations).

## Organization policy enforcement rules

Memorystore for Valkey enforces organization policies for the following operations:

  * Creating an instance
  * Updating an instance



## Limitations

Organization policies have the following limitations:

  * Changes to organization policies don't apply retroactively to existing instances.
  * A new policy has no effect on existing instances.



## What's next

  * Learn more about [organization policies](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about [organization policy constraints](https://docs.cloud.google.com/organization-policy/overview#constraints).
  * Use [predefined organization policies](https://docs.cloud.google.com/memorystore/docs/valkey/use-predefined-org-policies).
  * Use [custom organization policies](https://docs.cloud.google.com/memorystore/docs/valkey/use-custom-org-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
