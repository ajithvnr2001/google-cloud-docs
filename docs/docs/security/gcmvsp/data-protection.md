---
url: https://docs.cloud.google.com/docs/security/gcmvsp/data-protection/
title: Data protection guidelines \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:39.210942+00:00
---

# Data protection guidelines  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/gcmvsp/data-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Data protection guidelines Stay organized with collections  Save and categorize content based on your preferences. 

The following guidelines for the minimum viable security platform align with the data protection pillar.

## Basic level guidelines

Implement the following data protection guidelines first.

Item | 

### Use uniform bucket-level access  
  
---|---  
Description | The `storage.uniformBucketLevelAccess` boolean constraint requires buckets to use uniform bucket-level access. Uniform bucket-level access lets you only use bucket-level Identity and Access Management (IAM) permissions to grant access to your Cloud Storage resources.Using two different and conflicting systems to manage permissions on storage buckets is complex and a common cause of accidental data leaks. This setting turns off the legacy system (access control lists, or ACLs) and makes the modern, centralized system (IAM) the single source of truth for all permissions.  
Related information | 

  * [Require uniform bucket-level access](https://docs.cloud.google.com/storage/docs/org-policy-constraints#uniform-access)

  
Item ID | MVSP-CO-1.42  
Mapping |  Related NIST-800-53 controls:

  * AC-3
  * AC-17
  * AC-20

Related CRI profile controls:

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

Compliance Manager control:

  * [Enable Uniform Bucket-Level Access on Cloud Storage Buckets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-uniform-bucket-level-access)

  
Item | 

### Restrict Cloud SQL public IP addresses  
  
---|---  
Description | Prevent Cloud SQL from having a public IP address and being directly exposed to the internet by setting the `constraints/sql.restrictPublicIp` organization policy constraint. Typically, databases aren't directly exposed to the internet.Preventing public IP addresses helps prevent your databases from getting public IP addresses, ensuring that they are private and only accessible from trusted, internal applications.  
Related information | 

  * [Improve instance security by disabling public IP](https://docs.cloud.google.com/sql/docs/mysql/recommender-disable-public-ip)
  * [Connection organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy#connection_organization_policies)

  
Item ID | MVSP-CO-1.45  
Mapping |  Related NIST-800-53 controls:

  * SC-7

Related CRI profile controls:

  * PR.AC-3.1

Compliance Manager control:

  * [Block Public IP Addresses for Cloud SQL Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-cloud-sql-public-ip-addresses)

  
  
## Intermediate level guidelines

After you implemented the basic guidelines, implement the following data protection guidelines.

Item | 

### Block public access to Cloud Storage buckets  
  
---|---  
Description | The `storage.publicAccessPrevention` boolean constraint prevents storage buckets from being accessed from public sources without authentication. It disables and blocks access control lists (ACLs) and Identity and Access Management (IAM) permissions that grant access to `allUsers` and `allAuthenticatedUsers`. This constraint acts as an organization-wide safety net that actively blocks any setting that would make a bucket publicly accessible.  
Related information | 

  * [Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)

  
Item ID | MVSP-CO-1-43  
Mapping |  Related NIST-800-53 controls:

  * AC-3
  * AC-17
  * AC-20

Related CRI profile controls:

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

Compliance Manager control:

  * [Enforce Public Access Prevention](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-public-access-prevention)

  
Item | 

### Ensure BigQuery datasets aren't publicly readable or set to allAuthenticatedUsers  
  
---|---  
Description | Ensure that BigQuery doesn't have datasets that are open to public access unless the datasets are intended to be public. Datasets in BigQuery often contain sensitive data.Restrict access to the information in a BigQuery dataset to specific users only. To configure this protection, you must set up detailed roles.Reviewing dataset access helps you ensure that you don't unintentionally expose data to the internet.  
Related information | 

  * [Revoke access to a dataset](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam#revoke_access_to_a_dataset)
  * [allAuthenticatedUsers](https://docs.cloud.google.com/iam/docs/principals-overview#all-authenticated-users)
  * [Control access to resources with IAM](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam)

  
Item ID | MVSP-CO-1.46  
Mapping |  Related NIST-800-53 controls:

  * AC-3
  * AC-12
  * AC-17
  * AC-20

Related CRI profile controls:

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.PT-3.1
  * PR-PT-4.1

Compliance Manager control:

  * [Restrict Public Access to BigQuery Datasets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-public-access-bigquery-datasets)

  
  
## Advanced level guidelines

After you implemented the intermediate guidelines, implement the following data protection guidelines.

Item | 

### Create a managed encryption strategy  
  
---|---  
Description | Create an encryption management strategy using Cloud Key Management Service (Cloud KMS) with Autokey, Cloud External Key Manager (Cloud EKM), or both. This strategy lets your organization use and manage its own encryption keys to meet your specific requirements. Using your own encryption keys provides granular, auditable control over data access, including the ability to immediately block access to data by disabling the key.  
Related information | 

  * [Cloud KMS overview](https://docs.cloud.google.com/kms/docs/key-management-service)

  
Item ID | MVSP-CO-1.44  
Mapping |  Related NIST-800-53 controls:

  * SC-12

Related CRI profile controls:

  * PR.DS-1.1

  
  
## What's next

  * [Network security guidelines](https://docs.cloud.google.com/docs/security/gcmvsp/network-security)
  * [Overview of minimum viable secure platform](https://docs.cloud.google.com/docs/security/gcmvsp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
