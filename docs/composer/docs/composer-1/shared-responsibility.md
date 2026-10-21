---
url: https://docs.cloud.google.com/composer/docs/composer-1/shared-responsibility/
title: Managed Airflow shared responsibility model \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T09:29:02.020616+00:00
---

# Managed Airflow shared responsibility model  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/shared-responsibility/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Managed Airflow shared responsibility model Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/shared-responsibility "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/shared-responsibility "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

Running a business-critical application on Managed Airflow requires multiple parties to carry different responsibilities. While not an exhaustive list, this document lists the responsibilities for both Google and the Customer sides.

## Google Responsibilities

  * [Hardening](https://docs.cloud.google.com/container-optimized-os/docs/concepts/security) and [patching](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching) the Managed Airflow environment's components and underlying infrastructure, including Google Kubernetes Engine cluster, Cloud SQL database (that hosts the Airflow database), Pub/Sub, Artifact Registry and other environment elements. In particular, this includes auto-upgrading the underlying infrastructure, including the GKE cluster and Cloud SQL instance of an environment.

**Note:** Managed Airflow (Legacy Gen 1) is in the post-maintenance mode and new versions of Managed Airflow (Legacy Gen 1) with security fixes are no longer published. Migrate to Managed Airflow (Gen 2) or Managed Airflow (Gen 3) to get the latest version updates with security improvements.
  * Protecting access to Managed Airflow environments through incorporating access control provided by IAM, [encrypting data at rest by default](https://docs.cloud.google.com/security/encryption-at-rest/default-encryption), providing [additional customer-managed storage encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek), [encrypting data in transit](https://docs.cloud.google.com/security/encryption-in-transit).

  * Providing Google Cloud integrations for Identity and Access Management, Cloud Audit Logs and Cloud Key Management Service.

  * Restricting and logging Google administrative access to customers' clusters for contractual support purposes with [Access Transparency](https://docs.cloud.google.com/access-transparency) and [Access Approval](https://docs.cloud.google.com/cloud-provider-access-management/access-approval/docs/overview).

  * Publishing information about backward incompatible changes between Managed Airflow and Airflow versions in [Managed Airflow Release Notes](https://docs.cloud.google.com/composer/docs/release-notes).

  * Keeping Managed Airflow documentation up to date:

    * Providing description of all functionalities provided by Managed Airflow.

    * Providing troubleshooting instructions that help to keep environments in a healthy state.

    * Publishing information about known issues with workarounds (if they exist).

  * Resolving critical security incidents related to Managed Airflow environments and Airflow images provided by Managed Airflow (excluding customer-installed Python packages) by delivering new environment versions addressing the incidents.

  * Depending on customer's Support Plan, troubleshooting of Managed Airflow environment health issues.

  * Maintaining and expanding the functionality of the [Managed Airflow Terraform provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/composer_environment).

  * Cooperating with the Apache Airflow community to maintain and develop [Google Airflow operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/cloud_composer.html).

**Note:** Google won't fix or troubleshoot issues in operator providers for third-party services or products.
  * Troubleshooting and, if possible, fixing issues in Airflow core functionalities.




## Customer responsibilities

  * Upgrading to new Managed Airflow and Airflow versions to keep support for the product and to resolve security issues once Managed Airflow service publishes a Managed Airflow version that addresses the issues.

  * Maintaining the DAGs code to keep it compatible with the used Airflow version.

  * Keeping the environment's GKE cluster configuration intact, particularly including its auto-upgrade feature.

  * Maintaining proper permissions in IAM for the environment's service account. Particularly, keeping permissions required by the [Managed Airflow Agent](https://docs.cloud.google.com/composer/docs/composer-1/access-control#composer-sa) and the [environment's service account](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account). Maintaining required permission for the CMEK key used for Managed Airflow environment encryption and rotating it according to your needs.

**Caution:** We recommend to [set up a user-managed service account](https://docs.cloud.google.com/composer/docs/composer-1/access-control#custom-service-account) for Managed Airflow environments that has only the required set of permissions that are necessary to run the environment and perform operations defined in your DAGs. The **Composer Worker** (`composer.worker`) role provides this required set of permissions in most cases. Add extra permissions to this service account only when it's necessary for the operation of your DAGs.
  * Maintaining proper permissions in IAM for the environment's bucket and Artifact Registry repository where Managed Airflow's component images are stored .

**Caution:** Users with read-write access to the following components: 
    * Your environment's bucket
    * Artifact Registry repositories with container images used by: %Airflow components, `GKEPodOperator`, or `GKEStartPodOperator`

can deploy their own versions of DAGs or container images to an environment even without explicit Managed Airflow-related permissions. These DAGs or images can be later executed in your environment with the permissions of the Managed Airflow environment service account.

  * Maintaining proper IAM permissions for a service account that performs PyPI packages installations. For more information, see [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account-security).

**Caution:** Users with read-write access to the environment's bucket or those who can initiate PyPI packages installations can initiate the process of building images on behalf of a service account which is used to perform such builds. This service account is called the environment's service account that is specified during the environment creation, It can be a user-provided service account, or the default service account. 
  * Maintaining proper end user permissions in IAM and Airflow UI Access Control configuration.

  * Keeping Airflow database size below 16 GB through using the [maintenance DAG](https://docs.cloud.google.com/composer/docs/composer-1/cleanup-airflow-database). 

  * Resolving all DAG parsing issues before raising support cases to Cloud Customer Care.

  * Naming DAGs in a proper way (for example, without using invisible characters like SPACE or TAB in DAG names) so that metrics can be reported correctly for DAGs.

  * Upgrade the code of DAGs so that it doesn't use deprecated operators and migrate to their up to date alternatives. Deprecated operators might be removed from Airflow providers, which might impact your plans to upgrade to a later Managed Airflow or Airflow version. The deprecated operators are also not maintained and they must be used 'as is'.

  * Configuring proper IAM permissions when using secret backends like Secret Manager so that the environment's service account has access to it.

  * Adjusting Managed Airflow environment parameters (such as CPU and memory for Airflow components) and Airflow configurations to meet performance and load expectations of Managed Airflow environments using [Managed Airflow optimization guide](https://docs.cloud.google.com/composer/docs/composer-2/optimize-environments) and [environment scaling guide](https://docs.cloud.google.com/composer/docs/composer-1/scale-environments).

  * Avoiding removing permissions required by Managed Airflow Agent and environment's service accounts (removing these permissions can lead either to failed management operations or to DAG and task failures).

  * Keeping [all services and APIs required by Managed Airflow](https://docs.cloud.google.com/composer/docs/composer-1/enable-composer-service#required-services) always enabled. These dependencies must have quotas configured at levels required for Managed Airflow.

  * Keeping Artifact Registry repositories that host container images used by Managed Airflow environments.

  * [Following recommendations and best practices](https://docs.cloud.google.com/composer/docs/composer-1/write-dags) for implementing DAGs.

  * Diagnosing DAG and task failures using instructions for [scheduler troubleshooting](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-scheduling), [DAG troubleshooting](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-dags) and [triggerer troubleshooting](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-triggerer).

  * Avoiding installing or running additional components in the environment's GKE cluster that interfere with Managed Airflow components and prevent them from functioning correctly.

  * Configuring and managing [snapshots](https://docs.cloud.google.com/composer/docs/composer-1/configure-scheduled-snapshots) to meet your data retention and business continuity needs. Google does not restore deleted environments or their database backups.

  * Maintaining the Python dependency supply chain for [packages that are installed by the customer](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies). This includes [troubleshooting installation](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-package-installation) errors caused by Python dependency mismatches and defining specific version constraints when adding or modifying these packages.




## What's next

  * [Access control with IAM](https://docs.cloud.google.com/composer/docs/composer-1/access-control)
  * [Clean up the Airflow database](https://docs.cloud.google.com/composer/docs/composer-1/cleanup-airflow-database)
  * [Security overview](https://docs.cloud.google.com/composer/docs/composer-1/composer-security-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
