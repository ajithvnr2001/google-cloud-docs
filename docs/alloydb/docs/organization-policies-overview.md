---
url: https://docs.cloud.google.com/alloydb/docs/organization-policies-overview/
title: AlloyDB organization policies overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:25.026508+00:00
---

# AlloyDB organization policies overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/organization-policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  AlloyDB organization policies overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes AlloyDB for PostgreSQL organization policies, which organization administrators use to set restrictions on how users configure clusters and backups under that organization.

Projects, folders, and organizations are container resources organized in a parent-child resource hierarchy. An _organization_ is the root node in that hierarchy. For more information, see [Resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

Organization policies contain rules, called _constraints_ , that the organization administrator places on a project, folder, or organization. Constraints enforce a policy across all clusters and backups. For example, if you try to create a cluster or backup in an entity that has an organization policy, the constraint runs a check to ensure that the cluster or backup configuration follows the requirements of the constraint. If the check fails, AlloyDB doesn't create the cluster or backup resource.

When you add projects to an organization or folder that uses an organization policy, the projects inherit the constraints of that policy.

For more information about organization policies, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview), [Constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#constraints), and [Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).

The following organization policies are specific to AlloyDB:

  * [Predefined organization policies](https://docs.cloud.google.com/alloydb/docs/alloydb-predefined-constraints)
  * [Custom organization policies](https://docs.cloud.google.com/alloydb/docs/alloydb-custom-constraints)



## Predefined organization policies

To get started, you can use Customer Managed Encryption Key (CMEK) settings of AlloyDB clusters and backups. For more details, see [Use predefined organization policies](https://docs.cloud.google.com/alloydb/docs/alloydb-predefined-constraints). For granular, customizable control over other supported settings, use custom constraints. For more information, see [Use custom organization policies](https://docs.cloud.google.com/alloydb/docs/alloydb-custom-constraints).

### Customer-managed encryption keys (CMEK) organization policies

AlloyDB supports the following organization policy constraints:

  * `constraints/gcp.restrictNonCmekServices`: requires CMEK protection for the `alloydb.googleapis.com` API. When you add this constraint and `alloydb.googleapis.com` to the `Deny` policy list of services, AlloyDB refuses to create a new cluster or a backup resource unless the new cluster or backup resource is enabled with CMEK.
  * `constraints/gcp.restrictCmekCryptoKeyProjects`: limits which [Cloud KMS CryptoKeys](https://docs.cloud.google.com/kms/docs/resource-hierarchy#keys) to use for CMEK protection in AlloyDB clusters and backups. When AlloyDB creates a new cluster or backup using CMEK and this constraint, the CryptoKey must come from an allowed project, folder, or organization.



These constraints help ensure CMEK protection across an organization, and are only enforced on newly created AlloyDB clusters and backups. For more information, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) and [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

## Custom organization policies

For granular, customizable control over the settings, you can create custom constraints and use them in a custom organization policy. Use custom organization policies to improve your security, compliance, and governance.

To learn how to create custom organization policies, see [Use custom organization policies](https://docs.cloud.google.com/alloydb/docs/alloydb-custom-constraints). You can also view a list of [supported custom constraints and operations](https://docs.cloud.google.com/alloydb/docs/alloydb-custom-constraints#supported-custom-constraints-operations).

## Organization policy enforcement rules

AlloyDB enforces the organization policy for the following operations:

  * Instance creation
  * Instance update
  * Cluster creation
  * Backup creation



Like all [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints), policy changes don't apply retroactively to existing clusters and backups. The following are examples:

  * A new policy has no effect on existing instances, clusters, or backups.
  * Unless a user changes the instance, cluster, or backup configuration from a compliance to non-compliance state using the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or RPC, an existing instance, cluster, or backup configuration remains valid.
  * A scheduled maintenance update doesn't cause policy enforcement because maintenance doesn't change the configuration of instances, clusters, or backups.



## What's next

  * [Use predefined organization policies](https://docs.cloud.google.com/alloydb/docs/alloydb-predefined-constraints).
  * Learn about how [private IP](https://docs.cloud.google.com/alloydb/docs/private-ip) works with AlloyDB.
  * Learn how to [configure private services](https://docs.cloud.google.com/alloydb/docs/about-private-services-access) for AlloyDB.
  * Learn about the [organization policy service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * Learn about [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
