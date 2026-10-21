---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/security-best-practices/
title: Managed Service for Apache Spark security best practices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:30.054947+00:00
---

# Managed Service for Apache Spark security best practices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/security-best-practices/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark security best practices Stay organized with collections  Save and categorize content based on your preferences. 

Securing your Managed Service for Apache Spark environment is crucial for protecting sensitive data and preventing unauthorized access. This document outlines key best practices to enhance your Managed Service for Apache Spark security posture, including recommendations for network security, Identity and Access Management, encryption, and secure cluster configuration.

## Network security

  * **Deploy Managed Service for Apache Spark in a private VPC**. Create a dedicated [Virtual Private Cloud](https://docs.cloud.google.com/vpc/docs/overview) for your Managed Service for Apache Spark clusters, isolating them from other networks and the public internet.

  * **Use private IPs**. To protect your Managed Service for Apache Spark clusters from exposure to the public internet, use private IP addresses for enhanced security and isolation.

  * **Configure firewall rules**. Implement strict [firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls) to control traffic to and from your Managed Service for Apache Spark clusters. Allow only necessary ports and protocols.

  * **Use network peering**. For enhanced isolation, establish [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) between your Managed Service for Apache Spark VPC and other sensitive VPCs for controlled communication.

  * **Enable Component Gateway**. Enable the [Managed Service for Apache Spark Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways) when you create clusters to securely access Hadoop ecosystem UIs, such as like the YARN, HDFS, or Spark server UI, instead of opening the firewall ports.




## Identity and Access Management

  * **Isolate permissions**. Use different [data plane service accounts](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) for different clusters. Assign to service accounts only the permissions that clusters need to run their workloads.

  * **Avoid relying on the Google Compute Engine (GCE) default service account**. Don't use the [default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) for your clusters.

  * **Adhere to the principle of least privilege**. Grant only the [minimum necessary permissions](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) to Managed Service for Apache Spark service accounts and users.

  * **Enforce role-based access control (RBAC)**. Consider setting [IAM permissions](https://docs.cloud.google.com/iam/docs/roles-overview) for each cluster.

  * **Use custom roles**. Create fine-grained [custom IAM roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) tailored to specific job functions within your Managed Service for Apache Spark environment.

  * **Review regularly**. Regularly audit IAM permissions and roles to identify and remove any excessive or unused privileges.




## Encryption

  * **Encrypt data at rest**. For data encryption at rest, use the [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service) (KMS) or [Customer Managed Encryption Keys](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/customer-managed-encryption) (CMEK). Additionally, use organizational policies to enforce data encryption at rest for cluster creation.

  * **Encrypt data in transit**. Enable SSL/TLS for communication between Managed Service for Apache Spark components (by enabling [Hadoop Secure Mode](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/security)) and external services. This protects data in motion.

  * **Beware of sensitive data**. Exercise caution when storing and passing sensitive data like PII or passwords. Where required, use encryption and secrets management solutions.




## Secure cluster configuration

  * **Authenticate using Kerberos**. To prevent unauthorized access to cluster resources, implement Hadoop Secure Mode using [Kerberos](https://web.mit.edu/kerberos/#what_is) authentication. For more information, see [Secure multi-tenancy through Kerberos](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/security).

  * **Use a strong root principal password and secure KMS-based storage**. For clusters that use Kerberos, Managed Service for Apache Spark automatically configures security hardening features for all open source components running in the cluster.

  * **Enable OS login**. Enable [OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin) for added security when managing cluster nodes using SSH.

  * **Segregate staging and temp buckets on Google Cloud Storage (GCS)**. To ensure permission isolation, segregate [staging and temp buckets](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket) for each Managed Service for Apache Spark cluster.

  * **Use Secret Manager to store credentials**. The [Secret Manager](https://docs.cloud.google.com/managed-spark/docs/guides/hadoop-google-secret-manager-credential-provider) can safeguard your sensitive data, such as your API keys, passwords, and certificates. Use it to manage, access, and audit your secrets across Google Cloud.

  * **Use custom organizational constraints**. You can use a [custom organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#custom-organization-policies) to allow or deny specific operations on Managed Service for Apache Spark clusters. For example, if a request to create or update a cluster fails to satisfy custom constraint validation as set by your organization policy, the request fails and an error is returned to the caller.




## What's next

Learn more about other Managed Service for Apache Spark security features:

  * [Secure multi-tenancy through service accounts](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/sa-multi-tenancy)
  * [Set up a Confidential VM with inline memory encryption](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/confidential-compute)
  * [Activate an authorization service on each cluster VM](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/ranger-plugin)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
