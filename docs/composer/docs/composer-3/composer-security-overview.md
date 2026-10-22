---
url: https://docs.cloud.google.com/composer/docs/composer-3/composer-security-overview/
title: Managed Airflow security overview \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:06.553699+00:00
---

# Managed Airflow security overview  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/composer-security-overview/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Managed Airflow security overview Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/composer-security-overview "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/composer-security-overview "View this page for Managed Airflow \(Legacy Gen 1\)")

Managed Airflow offers a handful of security features and compliances that are beneficial for enterprise companies with stricter security requirements.

These three sections present information about Managed Airflow security features:

  * **Basic security features**. Describes features that are available in Managed Airflow environments by default.
  * **Advanced security features**. Describes features which you can use to modify Managed Airflow to your security requirements.
  * **Compliance to standards**. Provides a list of standards that Managed Airflow is compliant with.



## Basic security features

This section lists security-related features provided by default for each Managed Airflow environment.

### Encryption at rest

Managed Airflow utilizes [encryption at rest in Google Cloud](https://docs.cloud.google.com/security/encryption/default-encryption).

Managed Airflow stores data in different services. For example, the Airflow Metadata DB uses Cloud SQL database, DAGs are stored in Cloud Storage buckets.

By default, data is encrypted using Google-owned and Google-managed encryption keys.

If you prefer, you can configure Managed Airflow environments to be encrypted with customer-managed encryption keys.

### Uniform bucket-level access

[Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) allows you to uniformly control access to your Cloud Storage resources. This mechanism also applies to your environment's bucket, which stores your DAGs and plugins.

### User permissions

Managed Airflow has several features for managing user permissions:

  * **IAM roles and permissions**. Managed Airflow environments in a Google Cloud project can be accessed only by users whose accounts are added to IAM of the project.

  * **Managed Airflow-specific roles and permissions**. You [assign these roles and permissions](https://docs.cloud.google.com/composer/docs/composer-3/access-control) to user accounts in your project. Each role defines the types of operations that a user account can perform on Managed Airflow environments in your project.

  * **Airflow UI Access Control**. Users in your project [can have different access levels in the Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac). This mechanism is called Airflow UI Access Control (Airflow Role-Based Access Control, or Airflow RBAC).

  * **Domain Restricted Sharing (DRS)**. Managed Airflow supports [Domain Restricted Sharing organizational policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints). If you use this policy, then only users from the selected domains can access your environments.




### Private IP environments

You can create Managed Airflow environments in the [Private IP networking configuration](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type). It is also possible to switch an existing environment to the Private IP networking configuration.

In the Private IP mode, Airflow components of your environment (and thus your DAGs) do not have access to the public internet. Depending on how you [configure your VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network), a Private IP environment can gain access the internet through you VPC network.

### Your environment's cluster uses Shielded VMs

_Shielded VMs_ are virtual machines (VMs) on Google Cloud hardened by a set of security controls that help defend against rootkits and bootkits.

Managed Airflow environments use [Shielded VMs](https://docs.cloud.google.com/shielded-vm) to run the nodes of their environment cluster.

## Advanced security features

This section lists advanced security-related features for Managed Airflow environments.

### Customer Managed Encryption Keys (CMEK)

Managed Airflow supports [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). CMEK provide you with more control over the keys used to encrypt data at rest within a Google Cloud project.

You can [use CMEK with Managed Airflow](https://docs.cloud.google.com/composer/docs/composer-3/configure-cmek-encryption) to encrypt and decrypt data generated by a Managed Airflow environment.

### VPC Service Controls (VPC SC) Support

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) is a mechanism to mitigate data exfiltration risks.

Managed Airflow can be selected as a secured service inside a VPC Service Controls perimeter. All underlying resources used by Managed Airflow are configured to support VPC Service Controls architecture and follow its rules. Only Private IP environments can be created in a VPC SC perimeter.

Deploying [Managed Airflow environments with VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-3/configure-vpc-sc) gives you:

  * Reduced risk of data exfiltration.

  * Protection against data exposure due to misconfigured access controls.

  * Reduced risk of malicious users copying data to unauthorized Google Cloud resources, or external attackers accessing Google Cloud resources from the internet.




### Web server network access control levels (ACL)

Airflow web servers in Managed Airflow are always provisioned with an externally accessible IP address. You can control from which IP addresses the Airflow UI can be accessed. Managed Airflow supports IPv4 and IPv6 ranges.

You can [configure web server access restrictions](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#web-server-access) in Google Cloud console, `gcloud`, API, and Terraform.

### Secret Manager as a storage for sensitive configuration data

In Managed Airflow, you can [configure Airflow to use Secret Manager](https://docs.cloud.google.com/composer/docs/composer-3/configure-secret-manager) as a backend where Airflow connection variables are stored.

DAG developers can also read variables and connection stored in Secret Manager from the DAG code.

## Compliance to standards

See the pages linked below to check Managed Airflow's compliance with various standards:

  * [HIPAA Compliance](https://docs.cloud.google.com/security/compliance/hipaa#customer_responsibilities)
  * [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services)
  * [PCI DSS](https://docs.cloud.google.com/security/compliance/pci-dss)
  * ISO/IEC: [27001](https://docs.cloud.google.com/security/compliance/iso-27001), [27017](https://docs.cloud.google.com/security/compliance/iso-27017), [27018](https://docs.cloud.google.com/security/compliance/iso-27018)
  * SOC: [SOC 1](https://docs.cloud.google.com/security/compliance/soc-1), [SOC 2](https://docs.cloud.google.com/security/compliance/soc-2), [SOC 3](https://docs.cloud.google.com/security/compliance/soc-3)
  * NIST: [NIST800-53](https://docs.cloud.google.com/security/compliance/nist800-53), [NIST800-171](https://docs.cloud.google.com/security/compliance/nist800-171)
  * [DRZ FedRamp Moderate](https://docs.cloud.google.com/security/compliance/fedramp)
  * [Data Residency/Location Restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) ([configuration guide](https://docs.cloud.google.com/composer/docs/composer-3/configure-resource-location-restrictions) for Managed Airflow) 



## See also

Some of the security features mentioned in this article are discussed in the the Airflow Summit 2020 presentation: [Run Airflow DAGs in a secure way](https://www.youtube.com/watch?v=QhnItssm4yU).

## What's next

  * [Security best practices](https://docs.cloud.google.com/composer/docs/composer-3/security-practices)
  * [Access controls](https://docs.cloud.google.com/composer/docs/composer-3/access-control)
  * [Environment architecture](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
