---
url: https://docs.cloud.google.com/composer/docs/composer-1/security-practices/
title: Security best practices \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:57.750225+00:00
---

# Security best practices  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/security-practices/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Security best practices Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/security-practices "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-3/security-practices "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

Securing your Managed Airflow environment is crucial for protecting sensitive data and preventing unauthorized access. This page outlines key best practices, including recommendations for network security, Identity and Access Management, encryption, and environment configuration management.

To get more information about security features available in Managed Airflow, see [Security overview](https://docs.cloud.google.com/composer/docs/composer-1/composer-security-overview).

## Manage environment configuration and DAGs using version control

[ ![An example of an Airflow CI/CD pipeline](https://docs.cloud.google.com/static/composer/docs/images/composer-airflow-secure-cicd.svg)](https://docs.cloud.google.com/static/composer/docs/images/composer-airflow-secure-cicd.svg) **Figure 1.** An example of an Airflow CI/CD pipeline (click to enlarge) 

  * [Create your environment using Terraform](https://docs.cloud.google.com/composer/docs/composer-1/terraform-create-environments). In this way, you can store environment's configuration as code in a repository. In this way, changes to your environment configuration can be reviewed before they are applied, and you can reduce the number of users who have permissions to change the configuration by assigning roles with less permissions.

  * In Identity and Access Management, disable direct access to DAGs and environment's configuration to regular users, as detailed in the Identity and Access Management section.

  * [Deploy DAGs in your environment with a CI/CD pipeline](https://docs.cloud.google.com/composer/docs/composer-1/dag-cicd-github), so that DAG code is retrieved from a repository. In this way, DAGs are reviewed and approved before the changes are merged to the version control system. During the review process, approvers make sure that DAGs meet the security criteria established within their teams. The review step is critical to prevent deployment of DAGs that might perform unwanted actions.

Some important security aspects to take into account when reviewing DAGs are:

    * DAGs that modify the content of the environment's bucket must not modify the code of other DAGs or access sensitive data, unless intended.

    * DAGs must not make direct queries to the Airflow database, unless intended. A DAG in a Managed Airflow environment has access to all tables in the Airflow database. It is possible to retrieve information from any table, process it, and then store it outside of the Airflow database.




## Network security

  * Use [Private IP environments](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip) so that Airflow components in that run your environment's cluster are not assigned public IP addresses and communicate only over Google's internal network.

  * [Implement strict firewall rules](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip#private-ip-firewall-rules) to control traffic to and from your environment's cluster.

  * [Configure connectivity to Google APIs and services](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip#connectivity-domains) through the `private.googleapis.com` domain so that your environment accesses Google APIs and services through IP addresses only routable from within Google Cloud.

  * Review the general firewall rules in your project and in the VPC network where your environment is located. Depending on the way you configure them, Airflow components of your environment, such as Airflow workers that run your DAGs, might access the internet.




## Identity and Access Management

  * Isolate permissions. [Create environment service accounts](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account) and use different service accounts for different environments. Assign to these service accounts only permissions that are strictly necessary to operate these environments and perform operations defined in Airflow DAGs that they run.

  * Avoid using service accounts with broad permissions. While it is possible to create an environment that uses an account with broad permissions, such as those granted by the **Editor** basic role, this creates a risk of DAGs using broader permissions than intended.

  * Don't rely on default service accounts of Google services used by Managed Airflow. It is often impossible to reduce permissions available to these service accounts without also affecting other Google services in your project.

  * Make sure that you are familiar with [security considerations for environment's service accounts](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account-security) and understand how this account interacts with permissions and roles that you grant to individual users in your project.

  * Adhere to the principle of least privilege. Grant only the minimum necessary permissions to users. For example, [assign IAM roles](https://docs.cloud.google.com/composer/docs/composer-1/access-control#user-account), so that only administrators can access the environment's bucket and the environment's cluster , and direct access is disabled for regular users. For example, the **Composer User** role enables access only to DAG UI and Airflow UI.

  * Enforce [Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-1/airflow-rbac), which allows to reduce visibility in Airflow UI and DAG UI based on user's Airflow role, and can be used to assign DAG-level permissions for individual DAGs.

  * Review regularly. Regularly audit IAM permissions and roles to identify and remove any excessive or unused privileges.

  * Beware of passing and storing sensitive data:

    * Exercise caution when passing storing sensitive data like personally identifiable information or passwords. Where required, [use Secret Manager](https://docs.cloud.google.com/composer/docs/composer-1/configure-secret-manager) to securely store Airflow connections and Airflow secrets, API keys, passwords, and certificates. Don't store this information in your DAGs or environment variables.

    * Grant IAM permissions to the environment's bucket only to trusted users. Use per-object permissions, if possible. [Security considerations for environment's service accounts](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account-security) list several ways in which users with access to the environment's bucket can perform actions on behalf of the environment's service account.

    * Make sure that you are familiar with [what data is stored in the snapshots](https://docs.cloud.google.com/composer/docs/composer-1/save-load-snapshots) and provide permissions to create environment snapshots and access the bucket where they are stored only to trusted users.

    * All Managed Airflow's external interfaces use encryption by default. When connecting to external products and services, make sure that you use encrypted communication (SSL/TLS).




## What's next

  * [Security overview](https://docs.cloud.google.com/composer/docs/composer-1/composer-security-overview)
  * [Access control with IAM](https://docs.cloud.google.com/composer/docs/composer-1/access-control)
  * [Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-1/airflow-rbac)
  * [Airflow summit presentation about DAG security](https://www.youtube.com/watch?v=QhnItssm4yU)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
