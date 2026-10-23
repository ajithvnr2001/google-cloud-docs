---
url: https://docs.cloud.google.com/kms/docs/use-keys-google-cloud/
title: Use Cloud KMS keys in Google Cloud \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:17.153429+00:00
---

# Use Cloud KMS keys in Google Cloud  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/use-keys-google-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Use Cloud KMS keys in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Cloud KMS customer-managed encryption keys in other Google Cloud services to secure your resources. For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

When a service supports CMEK, it's said to have a _CMEK integration_. Some services, such as GKE, have multiple CMEK integrations for protecting different types of data related to the service. For a list of services with CMEK integrations, see Enable CMEK for supported services on this page.

## Before you begin

Before you can use Cloud KMS keys in other Google Cloud services, you must have a project resource to contain your Cloud KMS keys. We recommend using a separate project for your Cloud KMS resources that does not contain any other Google Cloud resources.

## CMEK integrations

### Prepare to enable CMEK integration

For the exact steps to enable CMEK, see the documentation for the relevant Google Cloud service. You can find a link to the CMEK documentation for each service in Enable CMEK for supported services on this page. For each service, you can expect to follow steps similar to the following:

  1. [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) or select an existing key ring. The key ring should be located as geographically near as possible to the resources you want to secure.

  2. In the selected key ring, [create a key](https://docs.cloud.google.com/kms/docs/creating-keys) or select an existing key. Ensure that the protection level, purpose, and algorithm for the key are appropriate for the resources you want to protect. This key is the CMEK key.

  3. [Get the resource ID for the CMEK key](https://docs.cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version). You need this resource ID later.

  4. Grant the [CryptoKey Encrypter/Decrypter IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the CMEK key to the service account for the service.

**Note:** You can grant the Cloud KMS CryptoKey Encrypter/Decrypter role at the key, key ring, project, folder, or organization level. To follow the principle of least privilege, we recommend granting this role at the lowest level that meets your needs.**Caution:** As long as your service account has the Cloud KMS CryptoKey Encrypter/Decrypter role, the service can encrypt and decrypt its data. If you revoke the role or if you disable or destroy the CMEK key, the data can no longer be accessed. Leaving your CMEK key inaccessible can affect your services.



After you have created the key and assigned the required permissions, you can create or configure a service to use your CMEK key.

**Note:** Some services only let you configure CMEK keys at the time the resource is created. Other services let you enable and disable CMEK keys on existing resources.

### Use Cloud KMS keys with CMEK-integrated services

The following steps use Secret Manager as an example. For the exact steps to use a Cloud KMS CMEK key in a given service, locate that service in the list of CMEK-integrated services.

In Secret Manager, you can use a CMEK to protect data at rest.

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/project)

  2. To create a secret, click **Create Secret**.

  3. In the **Encryption** section, select **Use a customer-managed encryption key (CMEK)**.

  4. In the **Encryption key** box do the following:

     1. Optional: To use a key in another project, do the following:

        1. Click **Switch project**.
        2. Enter all or part of the project name in the search bar, then select the project.
        3. To view available keys for the selected project, click **Select**.
     2. Optional: To filter available keys by location, key ring, name, or protection level, enter search terms in the  filter_alt filter bar.

     3. Select a key from the list of available keys in the selected project. You can use the displayed location, key ring, and protection level details to be sure you choose the correct key.

     4. If the key you want to use is not shown in the list, then click **Enter key manually** and enter the [resource ID](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id) of the key

  5. Finish configuring your secret, and then click **Create secret**. Secret Manager creates the secret and encrypts it using the specified CMEK key.




### Enable CMEK for supported services

To enable CMEK, first locate the selected service in the following table. You can enter search terms in the field to filter the table. All services in this list support software and hardware (HSM) keys. Products that integrate with Cloud KMS when using external [ Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm) keys are indicated in the **EKM supported** column.

Follow the instructions for each service you want to enable CMEK keys for.

Show only EKM compatible services

Service | Protected with CMEK | EKM supported | Topic  
---|---|---|---  
Agent Assist | Data at rest | Yes |  [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/agent-assist/docs/cmek)  
Agent Retrieval | Data associated with Collections | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/cmek)  
Agent Search | Data at rest | No |  [Customer-managed encryption keys](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek)  
AlloyDB for PostgreSQL | Data written to databases | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/alloydb/docs/cmek)  
Anti Money Laundering AI | Data in AML AI instance resources | No |  [Encrypt data using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/cmek)  
Apigee | Data at rest | No |  [Introduction to CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts)  
Apigee API hub | Data at rest | Yes |  [Encryption](https://docs.cloud.google.com/apigee/docs/apihub/provision#step-encryption)  
Application Integration | Data at rest | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/application-integration/docs/cmek)  
Artifact Registry | Data in repositories | Yes |  [Enabling customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek)  
Backup and DR Service | Backup Vault Container | Yes |  [Managing Backup Vault encryption](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek#backup-vault-container)  
Backup and DR Service | Backups at rest | Yes |  [Managing backup encryption](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek#backups-at-rest)  
Backup for GKE | Data in Backup for GKE | Yes |  [About Backup for GKE CMEK encryption](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-cmek)  
BigQuery | Data in BigQuery | Yes |  [Protecting data with Cloud KMS keys](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption)  
Bigtable | Data at rest | Yes |  [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/bigtable/docs/cmek)  
Cloud Data Fusion | Environment data | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys)  
Cloud Healthcare API | Cloud Healthcare API datasets | Yes |  [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/healthcare-api/docs/cmek)  
Cloud Logging | Data in the Log Router | Yes |  [Manage the keys that protect Log Router data](https://docs.cloud.google.com/logging/docs/routing/managed-encryption)  
Cloud Logging | Data in Logging storage | Yes |  [Manage the keys that protect Logging storage data ](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage)  
Cloud Run | Container image | Yes |  [Using customer-managed encryption keys with Cloud Run ](https://docs.cloud.google.com/run/docs/securing/using-cmek)  
Cloud Run functions | Data in Cloud Run functions | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/functions/docs/securing/cmek)  
Cloud SQL | Data written to databases | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek)  
Cloud SQL | Standard and enhanced backups | Yes |  [Cloud SQL backups overview](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups)  
Cloud Storage | Data in storage buckets | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys)  
Cloud Tasks | Task body and header at rest | Yes |  [Use customer-managed encryption keys](https://docs.cloud.google.com/tasks/docs/use-cmek)  
Cloud TPU | Persistent disks | No |  [Encrypt a TPU VM boot disk with a customer-managed encryption key (CMEK)](https://docs.cloud.google.com/tpu/docs/cmek-tpu)  
Cloud Workstations | Data on VM disks | Yes |  [Encrypt workstation resources](https://docs.cloud.google.com/workstations/docs/encrypt-workstation-resources)  
Colab Enterprise | Runtimes and notebook files | No |  [Use customer-managed encryption keys](https://docs.cloud.google.com/colab/docs/cmek)  
Compute Engine | Persistent disks | Yes |  [Protecting resources with Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#encrypt_a_new_persistent_disk_with_cmek)  
Compute Engine | Snapshots | Yes |  [Protecting resources with Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#create_snapshot)  
Compute Engine | Custom images | Yes |  [Protecting resources with Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#encrypt_an_imported_image)  
Compute Engine | Machine images | Yes |  [Protecting resources with Cloud KMS keys](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-instance)  
Conversational Analytics API | DataAgent resources (context, instructions, examples) | No |  [Protect a DataAgent resource with CMEK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek#protect-data-agent)  
Conversational Analytics API | Conversation resources (messages, state history) | No |  [Protect a Conversation resource with CMEK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek#protect-conversation)  
Customer Experience Insights | Data at rest | Yes |  [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/contact-center/insights/docs/cmek)  
Data Studio | Data at rest | Yes |  [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/data-studio/cmek)  
Database Migration Service Homogeneous Migrations | MySQL migrations - data written to databases | Yes |  [Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek)  
Database Migration Service Homogeneous Migrations | PostgreSQL migrations - Data written to databases | Yes |  [Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek)  
Database Migration Service Homogeneous Migrations | PostgreSQL to AlloyDB migrations - Data written to databases | Yes |  [About CMEK](https://docs.cloud.google.com/alloydb/docs/use-cmek)  
Database Migration Service Homogeneous Migrations | SQL Server migrations - Data written to databases | Yes |  [About CMEK](https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmek)  
Database Migration Service Heterogeneous Migrations | Oracle to PostgreSQL data at rest | Yes |  [Use customer-managed encryption keys (CMEK) for continuous migrations](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/cmek-for-migration-jobs)  
Dataflow | Pipeline state data | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys)  
Dataform | Data in repositories | Yes |  [Use customer-managed encryption keys](https://docs.cloud.google.com/dataform/docs/cmek)  
Dataproc Metastore | Data at rest | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/dataproc-metastore/docs/cmek)  
Datastream | Data in transit | Yes |  [Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/datastream/docs/use-cmek)  
Dialogflow CX | Data at rest | Yes |  [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek)  
Document AI | Data at rest and data in use | Yes |  [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/document-ai/docs/cmek)  
Eventarc Advanced ([Preview](https://cloud.google.com/products/#product-launch-stages)) | Data at rest | Yes |  [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek)  
Eventarc Standard | Data at rest | Yes |  [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/eventarc/docs/use-cmek)  
Filestore | Data at rest | Yes |  [Encrypt data with customer-managed encryption keys](https://docs.cloud.google.com/filestore/docs/cmek)  
Firestore | Data at rest | Yes |  [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/firestore/docs/use-cmek)  
Gemini Code Assist | Data at rest | No |  [Encrypt data with customer-managed encryption keys](https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek)  
Gemini Enterprise | Data at rest | No |  [Customer-managed encryption keys](https://docs.cloud.google.com/agentspace/agentspace-enterprise/docs/cmek)  
Gemini Enterprise - Gemini Notebook Enterprise | Data at rest | No |  [Customer-managed encryption keys](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/cmek)  
Google Cloud Managed Lustre | Data at rest | Yes |  [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/managed-lustre/docs/cmek)  
Google Cloud Managed Service for Apache Kafka | Data associated with topics | Yes |  [Configure message encryption](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/encryption)  
Google Cloud NetApp Volumes | Data at rest | Yes |  [Create a CMEK policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/create-cmek-policy)  
Google Cloud Observability ([Preview](https://cloud.google.com/products/#product-launch-stages)) | Data at rest | Yes |  [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets)  
Google Distributed Cloud | Data on Edge nodes | Yes |  [Local storage security](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/security#storage)  
Google Kubernetes Engine | Data on VM disks | Yes |  [Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek)  
Google Kubernetes Engine | Application-layer secrets | Yes |  [Application-layer Secrets encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets)  
Integration Connectors | Data at rest | Yes |  [Encryption methods](https://docs.cloud.google.com/integration-connectors/docs/encryption)  
Knowledge Catalog | Data at rest | Yes |  [Customer-managed encryption keys](https://docs.cloud.google.com/dataplex/docs/cmek)  
Looker (Google Cloud core) | Data at rest | Yes |  [Enable CMEK for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-cmek)  
Managed Service for Apache Airflow | Environment data | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/composer/docs/cmek)  
Managed Service for Apache Spark | Cluster data on VM disks | Yes |  [Customer-managed encryption keys](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/customer-managed-encryption)  
Managed Service for Apache Spark | Serverless data on VM disks | Yes |  [Customer-managed encryption keys](https://docs.cloud.google.com/dataproc-serverless/docs/guides/cmek-serverless)  
Memorystore for Redis | Data at rest | Yes |  [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/redis/cmek)  
Memorystore for Redis Cluster | Data at rest | Yes |  [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/cluster/use-cmek)  
Memorystore for Valkey | Data at rest | Yes |  [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/valkey/use-cmek)  
Migrate to Virtual Machines | Data migrated from VMware, AWS, and Azure VM sources | Yes |  [Use CMEK to encrypt data stored during a migration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/cmek#migration-data)  
Migrate to Virtual Machines | Data migrated from disk and machine image sources | Yes |  [Use CMEK to encrypt data on target disks and machine images](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/cmek#target-disk-machine-images)  
Parameter Manager | Parameter version payloads | Yes |  [Enable customer-managed encryption keys for Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/cmek)  
Pub/Sub | Data associated with topics | Yes |  [Configuring message encryption](https://docs.cloud.google.com/pubsub/docs/cmek)  
Secret Manager | Secret payloads | Yes |  [Enable Customer-Managed Encryption Keys for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek)  
Secure Source Manager | Instances | Yes |  [Encrypt data with customer-managed encryption keys](https://docs.cloud.google.com/secure-source-manager/docs/cmek)  
Security Command Center | Data at rest | Yes |  [Enable CMEK for Security Command Center](https://docs.cloud.google.com/security-command-center/docs/cmek)  
Service Extensions ([Preview](https://cloud.google.com/products/#product-launch-stages)) | Plugins data | No |  [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/service-extensions/docs/cmek)  
Spanner | Data at rest | Yes |  [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/spanner/docs/cmek)  
Speech-to-Text | Data at rest | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/speech-to-text/v2/docs/encryption)  
Vector Search | Data at rest | No |  [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/cmek)  
Vertex AI | Data associated with resources | Yes |  [Using customer-managed encryption keys](https://docs.cloud.google.com/vertex-ai/docs/general/cmek)  
Vertex AI Workbench managed notebooks (**Deprecated**) | User data at rest | No |  [Customer-managed encryption keys](https://docs.cloud.google.com/vertex-ai/docs/workbench/managed/cmek)  
Vertex AI Workbench user-managed notebooks (**Deprecated**) | Data on VM disks | No |  [Customer-managed encryption keys](https://docs.cloud.google.com/vertex-ai/docs/workbench/user-managed/cmek)  
Vertex AI Workbench instances | Data on VM disks | Yes |  [Customer-managed encryption keys](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/cmek)  
Workflows | Data at rest | Yes |  [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/workflows/docs/use-cmek)  
Workload Manager | Custom rule type evaluation data | Yes |  [Enable customer-managed encryption keys for evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/enable-cmek)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
