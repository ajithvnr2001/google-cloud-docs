---
url: https://docs.cloud.google.com/assured-workloads/docs/framework-reference/
title: Assured Workloads frameworks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:34:56.286723+00:00
---

# Assured Workloads frameworks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/framework-reference/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Assured Workloads frameworks

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

_Applicable only for[Assured Workloads frameworks](https://docs.cloud.google.com/assured-workloads/docs/frameworks-overview)_

This page provides reference content for the built-in frameworks that are included in Assured Workloads and Audit Manager.

##  Google Recommended AI Essentials - Gemini Enterprise Agent Platform

**Supported cloud provider:** Google Cloud 

This framework outlines Google recommended security best practices for Gemini Enterprise Agent Platform workloads, providing a prescriptive collection of essential preventative and detective policies. When you acctivate AI Protection within the Security Command Center, a detailed security compliance assessment against this framework is automatically displayed on the Agent Platform Security dashboard.

This framework includes the following cloud controls: 

  * [ Block Default VPC Network for Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-workbench-that-checks-vpc-network-usage)
  * [ Block File Downloading in JupyterLab Console ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#custom-vertex-ai-workbench-instance-detector-for-disabling-file-downloading-in-jupyterlab)
  * [ Block Internet Access for Runtime Templates in Agent Platform Colab Enterprise ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-runtime-template-internet-access)
  * [ Block Internet Access for Runtime Templates in Agent Platform Colab Enterprise ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-runtime-template-idle-shutdown)
  * [ Block Public IP Address for Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-workbench-that-restricts-public-ip)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#custom-detectors-for-vertex-ai-workbench-instance-root-access)
  * [ Define Secret Manager Replication Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-secret-manager-automatic-replication-for-google-agent-platform)
  * [ Enable Audit Logging for Agent Platform ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logging-for-google-agent-platform)
  * [ Enable Automatic Upgrades for Agent Platform WorkBench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#custom-detector-for-vertex-ai-notebooks-auto-upgrade)
  * [ Enable CMEK for Agent Platform Custom Jobs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cmek-key-is-use-for-vertex-ai-customjob)
  * [ Enable CMEK for Agent Platform Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cmek-key-is-use-for-vertex-ai-dataset)
  * [ Enable CMEK for Agent Platform Feature Store ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-feature-store-that-checks-whether-cmek-is-enabled)
  * [ Enable CMEK for Agent Platform Hyperparameter Tuning Jobs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cmek-key-is-use-for-vertex-ai-hyperparametertuningjob)
  * [ Enable CMEK for Agent Platform instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-agent-platform)
  * [ Enable CMEK for Agent Platform Metadata Stores ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-metadata-store-that-checks-whether-cmek-is-enabled)
  * [ Enable CMEK for Agent Platform Model Endpoints ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cmek-key-is-use-for-vertex-ai-endpoint)
  * [ Enable CMEK for Agent Platform Models ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cmek-key-is-use-for-vertex-ai-model)
  * [ Enable CMEK for Agent Platform TensorBoard ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-tensorboard-that-checks-whether-cmek-is-enabled)
  * [ Enable CMEK for Agent Platform Training Pipelines ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cmek-key-is-use-for-vertex-ai-trainingpipeline)
  * [ Enable CMEK for Agent Platform Workbench Instance Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-instance-disk-that-checks-whether-cmek-is-enabled)
  * [ Enable CMEK for Runtime Templates in Agent Platform Colab Enterprise ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-notebook-runtime-template-that-checks-whether-cmek-is-enabled)
  * [ Enable Delete to Trash Feature for Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-workbench-that-checks-whether-delete-to-trash-is-enabled)
  * [ Enable Integrity Monitoring for Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#custom-vertex-ai-notebooks-detectors-for-integrity-monitoring)
  * [ Enable Model Armor ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-model-armor)
  * [ Enable Secure Boot for Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#custom-detector-for-vertex-ai-workbench-secure-boot)
  * [ Enable Secure Boot for Runtime Templates in Agent Platform Colab Enterprise ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-runtime-template-secure-boot)
  * [ Enable vTPM on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#custom-vertex-ai-workbench-detectors-for-vtpm)
  * [ Restrict the Use of Default Service Account for Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-workbench-that-restricts-default-service-account-usage)
  * [ Use labels for Agent Platform agents ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#annotate-agents-of-google-agent-platform)



##  CIS GCP Foundations Benchmark v3.0

**Supported cloud provider:** Google Cloud 

Prescriptive guidance for establishing a secure baseline configuration for Google Cloud Platform. This benchmark provides technical best practices for hardening foundational services like IAM, Logging, Networking, and Storage.

This framework includes the following cloud controls: 

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Restrict API Keys for Required APIs Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-api-keys-for-required-apis-only)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn Off Local Infile Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-local-infile-db-flag-mysql)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



##  CIS GKE 1.7

**Supported cloud provider:** Google Cloud 

The CIS GKE Benchmark is a set of security recommendations and best practices specifically tailored for Google Kubernetes Engine (GKE) clusters. The benchmark aims to enhance the security posture of GKE environments.

This framework includes the following cloud controls: 

  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Disable Client Certificate Authentication for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-client-cert-auth-gke)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable PodSecurityPolicies for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-pod-security-policy-gke-cluster)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Require GKE Sandbox for GKE clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-sandbox-gke)
  * [ Require Private Nodes in GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-private-nodes-gke)
  * [ Require Workload Identity Federation for GKE and the GKE Metadata Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-metadata-server-gke)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Use Google Groups for Kubernetes RBAC ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-google-group-rbac-gke)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



##  CIS Critical Security Controls v8

**Supported cloud provider:** Google Cloud 

A prioritized set of safeguards to protect against prevalent cyber threats. It offers a practical approach to cyber defense, tiered into Implementation Groups (IG1, IG2, IG3) to suit organizations of varying maturity.

This framework includes the cloud control groups and cloud controls in the following sections. 

###  cis-controls-1-1

Establish and maintain an accurate, detailed, and up-to-date inventory of all enterprise assets with the potential to store or process data, to include: end-user devices (including portable and mobile), network devices, non-computing/IoT devices, and servers. Ensure the inventory records the network address (if static), hardware address, machine name, enterprise asset owner, department for each asset, and whether the asset has been approved to connect to the network. For mobile end-user devices, MDM type tools can support this process, where appropriate. This inventory includes assets connected to the infrastructure physically, virtually, remotely, and those within cloud environments. Additionally, it includes assets that are regularly connected to the enterprise’s network infrastructure, even if they are not under control of the enterprise. Review and update the inventory of all enterprise assets bi-annually, or more frequently.

  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Define Set Storage Class Lifestyle Action on Bucket ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-set-storage-class-lifestyle-action-on-bucket)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)



###  cis-controls-10-2

Configure automatic updates for anti-malware signature files on all enterprise assets.

  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  cis-controls-10-3

Disable autorun and autoplay auto-execute functionality for removable media.

  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  cis-controls-10-6

Centrally manage anti-malware software.

  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  cis-controls-11-1

Establish and maintain a documented data recovery process that includes detailed backup procedures. In the process, address the scope of data recovery activities, recovery prioritization, and the security of backup data. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)
  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)



###  cis-controls-11-2

Perform automated backups of in-scope enterprise assets. Run backups weekly, or more frequently, based on the sensitivity of the data.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)



###  cis-controls-11-3

Protect recovery data with equivalent controls to the original data. Reference encryption or data separation, based on requirements.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)



###  cis-controls-11-4

Establish and maintain an isolated instance of recovery data. Example implementations include, version controlling backup destinations through offline, cloud, or off-site systems or services.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)



###  cis-controls-11-5

Test backup recovery quarterly, or more frequently, for a sampling of in-scope enterprise assets.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)



###  cis-controls-12-2

Design and maintain a secure network architecture. A secure network architecture must address segmentation, least privilege, and availability, at a minimum. Example implementations may include documentation, policy, and design components.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)



###  cis-controls-12-3

Securely manage network infrastructure. Example implementations include version-controlled Infrastructure-as-Code (IaC), and the use of secure network protocols, such as SSH and HTTPS.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)



###  cis-controls-12-5

Centralize network AAA.

  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  cis-controls-12-6

Adopt secure network management protocols (e.g., 802.1X) and secure communication protocols (e.g., Wi-Fi Protected Access 2 (WPA2) Enterprise or more secure alternatives).

  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  cis-controls-12-7

Require users to authenticate to enterprise-managed VPN and authentication services prior to accessing enterprise resources on end-user devices.

  * [ Define Secret Manager Rotation Schedule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-secret-manager-rotation-schedule)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  cis-controls-13-1

Centralize security event alerting across enterprise assets for log correlation and analysis. Best practice implementation requires the use of a SIEM, which includes vendor-defined event correlation alerts. A log analytics platform configured with security-relevant correlation alerts also satisfies this Safeguard.

  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)



###  cis-controls-13-2

Deploy a host-based intrusion detection solution on enterprise assets, where appropriate and/or supported.

  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)



###  cis-controls-13-3

Deploy a network intrusion detection solution on enterprise assets, where appropriate. Example implementations include the use of a Network Intrusion Detection System (NIDS) or equivalent cloud service provider (CSP) service.

  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)



###  cis-controls-13-4

Perform traffic filtering between network segments, where appropriate.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)



###  cis-controls-13-5

Manage access control for assets remotely connecting to enterprise resources. Determine amount of access to enterprise resources based on: up-to-date anti-malware software installed, configuration compliance with the enterprise’s secure configuration process, and ensuring the operating system and applications are up-to-date.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Define Set Storage Class Lifestyle Action on Bucket ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-set-storage-class-lifestyle-action-on-bucket)



###  cis-controls-13-6

Collect network traffic flow logs and/or network traffic to review and alert upon from network devices.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)



###  cis-controls-13-7

Deploy a host-based intrusion prevention solution on enterprise assets, where appropriate and/or supported. Example implementations include use of an Endpoint Detection and Response (EDR) client or host-based IPS agent.

  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)



###  cis-controls-13-8

Deploy a network intrusion prevention solution, where appropriate. Example implementations include the use of a Network Intrusion Prevention System (NIPS) or equivalent CSP service.

  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)



###  cis-controls-13-9

Deploy port-level access control. Port-level access control utilizes 802.1x, or similar network access control protocols, such as certificates, and may incorporate user and/or device authentication.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)



###  cis-controls-14-1

Establish and maintain a security awareness program. The purpose of a security awareness program is to educate the enterprise’s workforce on how to interact with enterprise assets and data in a secure manner. Conduct training at hire and, at a minimum, annually. Review and update content annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  cis-controls-14-3

Train workforce members on authentication best practices. Example topics include MFA, password composition, and credential management.

  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  cis-controls-14-5

Train workforce members to be aware of causes for unintentional data exposure. Example topics include mis-delivery of sensitive data, losing a portable end-user device, or publishing data to unintended audiences.

  * [ Enforce HTTPS Traffic Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-https-traffic-only-policy)



###  cis-controls-16-1

Establish and maintain a secure application development process. In the process, address such items as: secure application design standards, secure coding practices, developer training, vulnerability management, security of third-party code, and application security testing procedures. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Restrict API Keys for Required APIs Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-api-keys-for-required-apis-only)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)



###  cis-controls-16-11

Leverage vetted modules or services for application security components, such as identity management, encryption, auditing, and logging. Using platform features in critical security functions will reduce developers’ workload and minimize the likelihood of design or implementation errors. Modern operating systems provide effective mechanisms for identification, authentication, and authorization and make those mechanisms available to applications. Use only standardized, currently accepted, and extensively reviewed encryption algorithms. Operating systems also provide mechanisms to create and maintain secure audit logs.

  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)



###  cis-controls-16-12

Apply static and dynamic analysis tools within the application life cycle to verify that secure coding practices are being followed.

  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)



###  cis-controls-16-2

Establish and maintain a process to accept and address reports of software vulnerabilities, including providing a means for external entities to report. The process is to include such items as: a vulnerability handling policy that identifies reporting process, responsible party for handling vulnerability reports, and a process for intake, assignment, remediation, and remediation testing. As part of the process, use a vulnerability tracking system that includes severity ratings and metrics for measuring timing for identification, analysis, and remediation of vulnerabilities. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard. Third-party application developers need to consider this an externally-facing policy that helps to set expectations for outside stakeholders.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  cis-controls-16-3

Perform root cause analysis on security vulnerabilities. When reviewing vulnerabilities, root cause analysis is the task of evaluating underlying issues that create vulnerabilities in code, and allows development teams to move beyond just fixing individual vulnerabilities as they arise.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  cis-controls-16-7

Use standard, industry-recommended hardening configuration templates for application infrastructure components. This includes underlying servers, databases, and web servers, and applies to cloud containers, Platform as a Service (PaaS) components, and SaaS components. Do not allow in-house developed software to weaken configuration hardening.

  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Local Infile Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-local-infile-db-flag-mysql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)



###  cis-controls-17-2

Establish and maintain contact information for parties that need to be informed of security incidents. Contacts may include internal staff, service providers, law enforcement, cyber insurance providers, relevant government agencies, Information Sharing and Analysis Center (ISAC) partners, or other stakeholders. Verify contacts annually to ensure that information is up-to-date.

  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)



###  cis-controls-17-4

Establish and maintain a documented incident response process that addresses roles and responsibilities, compliance requirements, and a communication plan. Review annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  cis-controls-17-9

Establish and maintain security incident thresholds, including, at a minimum, differentiating between an incident and an event. Examples can include: abnormal activity, security vulnerability, security weakness, data breach, privacy incident, etc. Review annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  cis-controls-18-1

Establish and maintain a penetration testing program appropriate to the size, complexity, industry, and maturity of the enterprise. Penetration testing program characteristics include scope, such as network, web application, Application Programming Interface (API), hosted services, and physical premise controls; frequency; limitations, such as acceptable hours, and excluded attack types; point of contact information; remediation, such as how findings will be routed internally; and retrospective requirements.

  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  cis-controls-18-2

Perform periodic external penetration tests based on program requirements, no less than annually. External penetration testing must include enterprise and environmental reconnaissance to detect exploitable information. Penetration testing requires specialized skills and experience and must be conducted through a qualified party. The testing may be clear box or opaque box.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  cis-controls-18-5

Perform periodic internal penetration tests based on program requirements, no less than annually. The testing may be clear box or opaque box.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)



###  cis-controls-2-7

Use technical controls, such as digital signatures and version control, to ensure that only authorized scripts, such as specific .ps1 and .py files, are allowed to execute. Block unauthorized scripts from executing. Reassess bi-annually, or more frequently.

  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)



###  cis-controls-3-1

Establish and maintain a documented data management process. In the process, address data sensitivity, data owner, handling of data, data retention limits, and disposal requirements, based on sensitivity and retention standards for the enterprise. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)



###  cis-controls-3-11

Encrypt sensitive data at rest on servers, applications, and databases. Storage-layer encryption, also known as server-side encryption, meets the minimum requirement of this Safeguard. Additional encryption methods may include application-layer encryption, also known as client-side encryption, where access to the data storage device(s) does not permit access to the plain-text data.

  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)



###  cis-controls-3-14

Log sensitive data access, including modification and disposal.

  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)



###  cis-controls-3-2

Establish and maintain a data inventory based on the enterprise’s data management process. Inventory sensitive data, at a minimum. Review and update inventory annually, at a minimum, with a priority on sensitive data.

  * [ Enforce HTTPS Traffic Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-https-traffic-only-policy)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)



###  cis-controls-3-3

Configure data access control lists based on a user’s need to know. Apply data access control lists, also known as access permissions, to local and remote file systems, databases, and applications.

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)



###  cis-controls-3-4

Retain data according to the enterprise’s documented data management process. Data retention must include both minimum and maximum timelines.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)



###  cis-controls-3-5

Securely dispose of data as outlined in the enterprise’s documented data management process. Ensure the disposal process and method are commensurate with the data sensitivity.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)



###  cis-controls-3-6

Encrypt data on end-user devices containing sensitive data. Example implementations can include: Windows BitLocker®, Apple FileVault®, Linux® dm-crypt.

  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)



###  cis-controls-3-7

Establish and maintain an overall data classification scheme for the enterprise. Enterprises may use labels, such as “Sensitive,” “Confidential,” and “Public,” and classify their data according to those labels. Review and update the classification scheme annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  cis-controls-3-8

Document data flows. Data flow documentation includes service provider data flows and should be based on the enterprise’s data management process. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)



###  cis-controls-3-9

Encrypt data on removable media.

  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)



###  cis-controls-4-1

Establish and maintain a documented secure configuration process for enterprise assets (end-user devices, including portable and mobile, non-computing/IoT devices, and servers) and software (operating systems and applications). Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  cis-controls-4-2

Establish and maintain a documented secure configuration process for network devices. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  cis-controls-4-3

Configure automatic session locking on enterprise assets after a defined period of inactivity. For general purpose operating systems, the period must not exceed 15 minutes. For mobile end-user devices, the period must not exceed 2 minutes.

  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-service-usage)



###  cis-controls-4-4

Implement and manage a firewall on servers, where supported. Example implementations include a virtual firewall, operating system firewall, or a third-party firewall agent.

  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)



###  cis-controls-4-5

Implement and manage a host-based firewall or port-filtering tool on end-user devices, with a default-deny rule that drops all traffic except those services and ports that are explicitly allowed.

  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)



###  cis-controls-4-6

Securely manage enterprise assets and software. Example implementations include managing configuration through version-controlled Infrastructure-as-Code (IaC) and accessing administrative interfaces over secure network protocols, such as Secure Shell (SSH) and Hypertext Transfer Protocol Secure (HTTPS). Do not use insecure management protocols, such as Telnet (Teletype Network) and HTTP, unless operationally essential.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)



###  cis-controls-4-7

Manage default accounts on enterprise assets and software, such as root, administrator, and other pre-configured vendor accounts. Example implementations can include: disabling default accounts or making them unusable.

  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)



###  cis-controls-4-8

Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web application module, or service function.

  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)



###  cis-controls-5-1

Establish and maintain an inventory of all accounts managed in the enterprise. The inventory must at a minimum include user, administrator, and service accounts. The inventory, at a minimum, should contain the person’s name, username, start/stop dates, and department. Validate that all active accounts are authorized, on a recurring schedule at a minimum quarterly, or more frequently.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)



###  cis-controls-5-2

Use unique passwords for all enterprise assets. Best practice implementation includes, at a minimum, an 8-character password for accounts using Multi-Factor Authentication (MFA) and a 14-character password for accounts not using MFA. 

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)



###  cis-controls-5-4

Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Conduct general computing activities, such as internet browsing, email, and productivity suite use, from the user’s primary, non-privileged account.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  cis-controls-5-5

Establish and maintain an inventory of service accounts. The inventory, at a minimum, must contain department owner, review date, and purpose. Perform service account reviews to validate that all active accounts are authorized, on a recurring schedule at a minimum quarterly, or more frequently.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Configure Remote Access Inactivity Timeout ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-remote-access-inactivity-timeout)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)



###  cis-controls-5-6

Centralize account management through a directory or identity service.

  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Require OS Login on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-instance-os-login)



###  cis-controls-6-1

Establish and follow a documented process, preferably automated, for granting access to enterprise assets upon new hire or role change of a user.

  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable the Confidential VM Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-vm-service)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)



###  cis-controls-6-2

Establish and follow a process, preferably automated, for revoking access to enterprise assets, through disabling accounts immediately upon termination, rights revocation, or role change of a user. Disabling accounts, instead of deleting accounts, may be necessary to preserve audit trails.

  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable the Confidential VM Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-vm-service)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)



###  cis-controls-6-3

Require all externally-exposed enterprise or third-party applications to enforce MFA, where supported. Enforcing MFA through a directory service or SSO provider is a satisfactory implementation of this Safeguard.

  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  cis-controls-6-5

Require MFA for all administrative access accounts, where supported, on all enterprise assets, whether managed on-site or through a service provider.

  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  cis-controls-6-6

Establish and maintain an inventory of the enterprise’s authentication and authorization systems, including those hosted on-site or at a remote service provider. Review and update the inventory, at a minimum, annually, or more frequently.

  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable the Confidential VM Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-vm-service)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)



###  cis-controls-6-7

Centralize access control for all enterprise assets through a directory service or SSO provider, where supported.

  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Require OS Login on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-instance-os-login)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)



###  cis-controls-6-8

Define and maintain role-based access control, through determining and documenting the access rights necessary for each role within the enterprise to successfully carry out its assigned duties. Perform access control reviews of enterprise assets to validate that all privileges are authorized, on a recurring schedule at a minimum annually, or more frequently.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  cis-controls-7-2

Establish and maintain a risk-based remediation strategy documented in a remediation process, with monthly, or more frequent, reviews.

  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  cis-controls-7-7

Remediate detected vulnerabilities in software through processes and tooling on a monthly, or more frequent, basis, based on the remediation process.

  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  cis-controls-8-1

Establish and maintain a documented audit log management process that defines the enterprise’s logging requirements. At a minimum, address the collection, review, and retention of audit logs for enterprise assets. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)



###  cis-controls-8-11

Conduct reviews of audit logs to detect anomalies or abnormal events that could indicate a potential threat. Conduct reviews on a weekly, or more frequent, basis.

  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)



###  cis-controls-8-2

Collect audit logs. Ensure that logging, per the enterprise’s audit log management process, has been enabled across enterprise assets.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)



###  cis-controls-8-3

Ensure that logging destinations maintain adequate storage to comply with the enterprise’s audit log management process.

  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)



###  cis-controls-8-4

Standardize time synchronization. Configure at least two synchronized time sources across enterprise assets, where supported.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)



###  cis-controls-8-5

Configure detailed audit logging for enterprise assets containing sensitive data. Include event source, date, username, timestamp, source addresses, destination addresses, and other useful elements that could assist in a forensic investigation.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)



###  cis-controls-8-6

Collect DNS query audit logs on enterprise assets, where appropriate and supported.

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)



###  cis-controls-8-7

Collect URL request audit logs on enterprise assets, where appropriate and supported.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Define Secret Manager Rotation Schedule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-secret-manager-rotation-schedule)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)



###  cis-controls-8-8

Collect command-line audit logs. Example implementations include collecting audit logs from PowerShell®, BASH™, and remote administrative terminals.

  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)



###  cis-controls-8-9

Centralize, to the extent possible, audit log collection and retention across enterprise assets in accordance with the documented audit log management process. Example implementations primarily include leveraging a SIEM tool to centralize multiple log sources.

  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)



###  cis-controls-9-1

Ensure only fully supported browsers and email clients are allowed to execute in the enterprise, only using the latest version of browsers and email clients provided through the vendor.

  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)



###  cis-controls-9-2

Use DNS filtering services on all end-user devices, including remote and on-premises assets, to block access to known malicious domains.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)



###  cis-controls-9-3

Enforce and update network-based URL filters to limit an enterprise asset from connecting to potentially malicious or unapproved websites. Example implementations include category-based filtering, reputation-based filtering, or through the use of block lists. Enforce filters for all enterprise assets.

  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)



###  cis-controls-9-4

Restrict, either through uninstalling or disabling, any unauthorized or unnecessary browser or email client plugins, extensions, and add-on applications.

  * [ Require Binary Authorization on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-binary-authorization)



##  CSA Cloud Controls Matrix v4.0.11

**Supported cloud provider:** Google Cloud 

A cybersecurity control framework designed specifically for the cloud computing environment. It provides a comprehensive set of controls across key domains to help you assess the security posture of your cloud services.

This framework includes the cloud control groups and cloud controls in the following sections. 

###  ccm-aa-01

Establish, document, approve, communicate, apply, evaluate and maintain audit and assurance policies and procedures and standards. Review and update the policies and procedures at least annually.

  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  ccm-aa-02

Conduct independent audit and assurance assessments according to relevant standards at least annually.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)



###  ccm-ais-01

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures for application security to provide guidance to the appropriate planning, delivery and support of the organization's application security capabilities. Review and update the policies and procedures at least annually.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  ccm-ais-02

Establish, document and maintain baseline requirements for securing different applications.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)



###  ccm-ais-03

Define and implement technical and operational metrics in alignment with business objectives, security requirements, and compliance obligations.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  ccm-ais-04

Define and implement a SDLC process for application design, development, deployment, and operation in accordance with security requirements defined by the organization.

  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)



###  ccm-ais-05

Implement a testing strategy, including criteria for acceptance of new information systems, upgrades and new versions, which provides application security assurance and maintains compliance while enabling organizational speed of delivery goals. Automate when applicable and possible.

  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)



###  ccm-bcr-03

Establish strategies to reduce the impact of, withstand, and recover from business disruptions within risk appetite.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)



###  ccm-bcr-07

Establish communication with stakeholders and participants in the course of business continuity and resilience procedures.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)



###  ccm-bcr-08

Periodically backup data stored in the cloud. Ensure the confidentiality, integrity and availability of the backup, and verify data restoration from backup for resiliency.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)



###  ccm-bcr-09

Establish, document, approve, communicate, apply, evaluate and maintain a disaster response plan to recover from natural and man-made disasters. Update the plan at least annually or upon significant changes.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)



###  ccm-bcr-10

Exercise the disaster response plan annually or upon significant changes, including if possible local emergency authorities.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)



###  ccm-bcr-11

Supplement business-critical equipment with redundant equipment independently located at a reasonable minimum distance in accordance with applicable industry standards.

  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)



###  ccm-ccc-01

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures for managing the risks associated with applying changes to organization assets, including application, systems, infrastructure, configuration, etc. The policies and procedures must be managed, regardless of whether the assets are managed internally or externally. Review and update the policies and procedures at least annually.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-service-usage)



###  ccm-ccc-02

Follow a defined quality change control, approval and testing process with established baselines, testing, and release standards.

  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)



###  ccm-ccc-07

Implement detection measures with proactive notification in case of changes deviating from the established baseline.

  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)



###  ccm-cek-01

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures for Cryptography, Encryption and Key Management. Review and update the policies and procedures at least annually.

  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)



###  ccm-cek-02

Define and implement cryptographic, encryption and key management roles and responsibilities.

  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)



###  ccm-cek-03

Provide cryptographic protection to data at-rest and in-transit, using cryptographic libraries certified to approved standards.

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  ccm-cek-04

Use encryption algorithms that are appropriate for data protection, considering the classification of data, associated risks, and usability of the encryption technology.

  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)



###  ccm-cek-05

Establish a standard change management procedure, to accommodate changes from internal and external sources, for review, approval, implementation and communication of cryptographic, encryption and key management technology changes.

  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)



###  ccm-cek-08

CSPs must provide the capability for CSCs to manage their own data encryption keys.

  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)



###  ccm-cek-10

Generate Cryptographic keys using industry accepted cryptographic libraries specifying the algorithm strength and the random number generator used.

  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)



###  ccm-cek-11

Manage cryptographic secret and private keys that are provisioned for a unique purpose.

  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)



###  ccm-cek-18

Define, implement and evaluate processes, procedures and technical measures to manage archived keys in a secure repository requiring least privilege access, which include provisions for legal and regulatory requirements.

  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)



###  ccm-cek-21

Define, implement and evaluate processes, procedures and technical measures in order for the key management system to track and report all cryptographic materials and changes in status, which include provisions for legal and regulatory requirements.

  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)



###  ccm-dcs-07

Implement physical security perimeters to safeguard personnel, data, and information systems. Establish physical security perimeters between the administrative and business areas and the data storage and processing facilities areas.

  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)



###  ccm-dcs-09

Allow only authorized personnel access to secure areas, with all ingress and egress points restricted, documented, and monitored by physical access control mechanisms. Retain access control records on a periodic basis as deemed appropriate by the organization.

  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)



###  ccm-dsp-01

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures for the classification, protection and handling of data throughout its lifecycle, and according to all applicable laws and regulations, standards, and risk level. Review and update the policies and procedures at least annually.

  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)



###  ccm-dsp-02

Apply industry accepted methods for the secure disposal of data from storage media such that data is not recoverable by any forensic means.

  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)



###  ccm-dsp-07

Develop systems, products, and business practices based upon a principle of security by design and industry best practices.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Restrict API Keys for Required APIs Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-api-keys-for-required-apis-only)



###  ccm-dsp-08

Develop systems, products, and business practices based upon a principle of privacy by design and industry best practices. Ensure that systems' privacy settings are configured by default, according to all applicable laws and regulations.

  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)



###  ccm-dsp-10

Define, implement and evaluate processes, procedures and technical measures that ensure any transfer of personal or sensitive data is protected from unauthorized access and only processed within scope as permitted by the respective laws and regulations.

  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)



###  ccm-dsp-16

Data retention, archiving and deletion is managed in accordance with business requirements, applicable laws and regulations.

  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)



###  ccm-dsp-17

Define and implement, processes, procedures and technical measures to protect sensitive data throughout its lifecycle.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  ccm-grc-01

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures for an information governance program, which is sponsored by the leadership of the organization. Review and update the policies and procedures at least annually.

  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  ccm-grc-03

Review all relevant organizational policies and associated procedures at least annually or when a substantial change occurs within the organization.

  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  ccm-grc-07

Identify and document all relevant standards, regulations, legal, contractual, and statutory requirements, which are applicable to your organization.

  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)



###  ccm-iam-01

Establish, document, approve, communicate, implement, apply, evaluate and maintain policies and procedures for identity and access management. Review and update the policies and procedures at least annually.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)



###  ccm-iam-03

Manage, store, and review the information of system identities, and level of access.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)



###  ccm-iam-04

Employ the separation of duties principle when implementing information system access.

  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)



###  ccm-iam-05

Employ the least privilege principle when implementing information system access.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)



###  ccm-iam-07

De-provision or respectively modify access of movers, leavers, or system identity changes in a timely manner in order to effectively adopt and communicate identity and access management policies.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Define Secret Manager Rotation Schedule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-secret-manager-rotation-schedule)



###  ccm-iam-09

Define, implement and evaluate processes, procedures and technical measures for the segregation of privileged access roles such that administrative access to data, encryption and key management capabilities and logging capabilities are distinct and separated.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Configure Remote Access Inactivity Timeout ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-remote-access-inactivity-timeout)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)



###  ccm-iam-10

Define and implement an access process to ensure privileged access roles and rights are granted for a time limited period, and implement procedures to prevent the culmination of segregated privileged access.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Configure Remote Access Inactivity Timeout ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-remote-access-inactivity-timeout)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)



###  ccm-iam-11

Define, implement and evaluate processes and procedures for customers to participate, where applicable, in the granting of access for agreed, high risk privileged access roles as defined by the organizational risk assessment.

  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)



###  ccm-iam-12

Define, implement and evaluate processes, procedures and technical measures to ensure the logging infrastructure is read-only for all with write access, including privileged access roles, and that the ability to disable it is controlled through a procedure that ensures the segregation of duties and break glass procedures.

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)



###  ccm-iam-13

Define, implement and evaluate processes, procedures and technical measures that ensure users are identifiable through unique IDs or which can associate individuals to the usage of user IDs.

  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)



###  ccm-iam-14

Define, implement and evaluate processes, procedures and technical measures for authenticating access to systems, application and data assets, including multifactor authentication for at least privileged user and sensitive data access. Adopt digital certificates or alternatives which achieve an equivalent level of security for system identities.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)



###  ccm-iam-16

Define, implement and evaluate processes, procedures and technical measures to verify access to data and system functions is authorized.

  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)



###  ccm-ivs-01

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures for infrastructure and virtualization security. Review and update the policies and procedures at least annually.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)



###  ccm-ivs-03

Monitor, encrypt and restrict communications between environments to only authenticated and authorized connections, as justified by the business. Review these configurations at least annually, and support them by a documented justification of all allowed services, protocols, ports, and compensating controls.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)



###  ccm-ivs-04

Harden host and guest OS, hypervisor or infrastructure control plane according to their respective best practices, and supported by technical controls, as part of a security baseline.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  ccm-ivs-06

Design, develop, deploy and configure applications and infrastructures such that CSP and CSC (tenant) user access and intra-tenant access is appropriately segmented and segregated, monitored and restricted from other tenants.

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)



###  ccm-ivs-07

Use secure and encrypted communication channels when migrating servers, services, applications, or data to cloud environments. Such channels must include only up-to-date and approved protocols.

  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)



###  ccm-ivs-09

Define, implement and evaluate processes, procedures and defense-in-depth techniques for protection, detection, and timely response to network-based attacks.

  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)



###  ccm-log-01

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures for logging and monitoring. Review and update the policies and procedures at least annually.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)



###  ccm-log-02

Define, implement and evaluate processes, procedures and technical measures to ensure the security and retention of audit logs.

  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)



###  ccm-log-03

Identify and monitor security-related events within applications and the underlying infrastructure. Define and implement a system to generate alerts to responsible stakeholders based on such events and corresponding metrics.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)



###  ccm-log-04

Restrict audit logs access to authorized personnel and maintain records that provide unique access accountability.

  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)



###  ccm-log-05

Monitor security audit logs to detect activity outside of typical or expected patterns. Establish and follow a defined process to review and take appropriate and timely actions on detected anomalies.

  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)



###  ccm-log-07

Establish, document and implement which information metadata and data system events should be logged. Review and update the scope at least annually or whenever there is a change in the threat environment.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)



###  ccm-log-08

Generate audit records containing relevant security information.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)



###  ccm-log-12

Monitor and log physical access using an auditable access control system.

  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)



###  ccm-sef-01

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures for Security Incident Management, E-Discovery, and Cloud Forensics. Review and update the policies and procedures at least annually.

  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)



###  ccm-sef-02

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures for the timely management of security incidents. Review and update the policies and procedures at least annually.

  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)



###  ccm-sef-08

Maintain points of contact for applicable regulation authorities, national and local law enforcement, and other legal jurisdictional authorities.

  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)



###  ccm-sta-04

Delineate the shared ownership and applicability of all CSA CCM controls according to the SSRM for the cloud service offering.

  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)



###  ccm-sta-08

CSPs periodically review risk factors associated with all organizations within their supply chain.

  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)



###  ccm-sta-09

Service agreements between CSPs and CSCs (tenants) must incorporate at least the mutually-agreed upon provisions and terms that include Scope, characteristics and location of business relationship and services offered, Information security requirements (including SSRM), Change management process, Logging and monitoring capability, Incident management and communication procedures, Right to audit and third party assessment, Service termination, Interoperability and portability requirements, and Data privacy.

  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)



###  ccm-tvm-01

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures to identify, report and prioritize the remediation of vulnerabilities, in order to protect systems against vulnerability exploitation. Review and update the policies and procedures at least annually.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)



###  ccm-tvm-02

Establish, document, approve, communicate, apply, evaluate and maintain policies and procedures to protect against malware on managed assets. Review and update the policies and procedures at least annually.

  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)



###  ccm-tvm-03

Define, implement and evaluate processes, procedures and technical measures to enable both scheduled and emergency responses to vulnerability identifications, based on the identified risk.

  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  ccm-tvm-06

Define, implement and evaluate processes, procedures and technical measures for the periodic performance of penetration testing by independent third parties.

  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  ccm-uem-04

Maintain an inventory of all endpoints used to store and access company data.

  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)



###  ccm-uem-07

Manage changes to endpoint operating systems, patch levels, and applications through the company's change management processes.

  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)



###  ccm-uem-10

Configure managed endpoints with properly configured software firewalls.

  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)



###  ccm-uem-11

Configure managed endpoints with Data Loss Prevention (DLP) technologies and rules in accordance with a risk assessment.

  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)



##  DBG CSA CCM

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

DBG CSA CCM

This framework includes the cloud control groups and cloud controls in the following sections. 

###  csa-ccm-bcr-08-3

The BCR-08.3 monitors configuration of standard Backup agents for three GCP services running in the current project:

  * [Backup Agent for GKE](https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) is enabled for all GKE clusters;
  * [Backup configuration](https://cloud.google.com/sql/docs/mysql/backup-recovery/backups) is enabled for Cloud SQL instances;
  * [Continuous backup](https://cloud.google.com/alloydb/docs/backup/overview) is enabled for AlloyDB instances;



The controls is violated if any of the required Backup configurations is not enabled.

  * [ Enabled Backups ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enabled-backups)



###  csa-ccm-bcr-11-2

The BCR-11.2 monitors effective value of the Organization Policy gcp.resourceLocations.

The control is violated if the Organization Policy is not set or is not restricting location of new resources to the regions:

  * europe-west3 (Frankfurt)
  * europe-west6 (Milan)
  * europe-west8 (Zurich)


  * [ Location Policy EW3 EW6 EW8 ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#location-policy-ew3-ew6-ew8)



###  csa-ccm-bcr-11-4

The BCR-11.4 monitors geographical location of Google Cloud resources, supporting regionalization.

Complaint Google Cloud resources should be launched in any of these regions:

  * europe-west3 (Frankfurt)
  * europe-west6 (Milan)
  * europe-west8 (Zurich)



The control is violated if any other location is used. This includes EU multi-region.

  * [ GCP Foundation Landing Zone Constraints Regions To Europe ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gcp-foundation-landing-zone-constraints-regions-to-europe)
  * [ GCP Foundation Resources Not Running Outside Europe ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gcp-foundation-resources-not-running-outside-europe)



###  csa-ccm-ccc-05-1

Check shared responsibility documentation in change procedures

  * [ Changes impacting CSC ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#changes-impacting-csc)



###  csa-ccm-ccc-06

CCC-06 monitors that every Google Cloud project enables only those GCP services that have been tested and approved for usage.

  * [ GCP Foundation No Preliminary Approved Services Enabled ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gcp-foundation-no-preliminary-approved-services-enabled)



###  csa-ccm-cek-02-5

Newly created data storage services must use CMEK, located in a specific dedicated project. This project ID must be enforced with Organization Policy constraints/gcp.restrictCmekCryptoKeyProjects

  * [ CMEK Dedicated Project Restricted ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cmek-dedicated-project-restricted)



###  csa-ccm-cek-04-3

All keys, used for encrypting data in storage, should be generated in on-premise HSM device and then imported to GCP CMEK. All keys are stored in the cloud-based HSM system

  * [ CMEK Keys Imported and Stored In HSM ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cmek-keys-imported-and-stored-in-hsm)



###  csa-ccm-cek-08-3

All Storage Service used in GCP should use Customer Managed Encryption Key for encrypting data-at-rest.

  * [ CMEK Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cmek-usage)



###  csa-ccm-dsp-04

DSP-04.1 monitors that all resources, supporting labels, have a label attached.

  * [ GCP Foundation Resource With Label Has Label Assigned ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gcp-foundation-resource-with-label-has-label-assigned)



###  csa-ccm-dsp-16

DSP-16.3 monitors configuration of GCS buckets. Every GCS bucket needs to have the Soft Delete feature enabled or both features: Object Versioning and Object Retention enabled simultaneously.

  * [ GCP Foundation GCS Has Retention Deletion Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gcp-foundation-gcs-has-retention-deletion-rules)



###  csa-ccm-ivs-05-1

IVS-05.1 monitors that every GCP project has the attached Resource Manager Tag that define the environment.

  * [ Tags Attached To Projects ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#tags-attached-to-projects)



###  csa-ccm-ivs-09-1

Firewall rules are not using tags and do not enable access to any services from the public Internet

  * [ FW Rule Disable Tags and Wide Internet Ingress ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#fw-rule-disable-tags-and-wide-internet-ingress)



###  csa-ccm-log-04-1

Restrict audit logs access to authorized personnel and maintain records that provide unique access accountability.

  * [ Disable Audit Log Exemption ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-audit-log-exemption)



###  csa-ccm-log-06

Use a reliable time source across all relevant information processing systems.

  * [ GCP Foundation Trusted Image Org Policy Enabled For All Projects ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gcp-foundation-trusted-image-org-policy-enabled-for-all-projects)



##  DORA

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Digital Operational Resilience Act

This framework includes the cloud control groups and cloud controls in the following sections. 

###  dora-article-07

Financial entities must maintain updated ICT systems, protocols and tools that are appropriate for use, reliable, and resilient.

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Define Rotation Period for Cloud KMS Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-key-rotation-period)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Limit KMS Crypto Keys Users to Three ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#limit-kms-crypto-keys-users)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  dora-article-09

Financial entities must implement security tools that continually monitor and control ICT systems and ensure, but not limited to, privacy, availability, integrity and confidentiality.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Assess Actions that Don't Require Identification or Authentication ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#permit-actions-without-identification-authentication)
  * [ Authorize and Monitor Privileged Remote Access ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#authorize-monitor-privileged-remote-access)
  * [ Authorize Wireless Access to Production Systems ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#authorize-wireless-access-production-systems)
  * [ Automate Account Management System ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#automate-account-management-system)
  * [ Automate Near Real-time Event Analysis ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#automate-real-time-event-analysis)
  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Block Administrator Roles from Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-admin-roles-from-service-accounts)
  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Configure a Wireless Intrusion Detection Mechanism ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-wireless-intrusion-detection-mechanism)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure Log Metrics and Alerts for Cloud Storage IAM Policy Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-log-metrics-for-bucket-iam-changes)
  * [ Configure Network Devices to Fail in a Secure State ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-network-devices-fail-secure)
  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Configure VPC Firewall Rules, Subnets, and VPN Gateway ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-vpc-firewall-subnet-gateway)
  * [ Control Integrations with External Systems ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#control-integrations-external-systems)
  * [ Control Remote Device Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#control-remote-device-connections)
  * [ Correlate Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#correlate-audit-records)
  * [ Create Alerts for Monitoring Security Command Center Errors ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-alerts-for-monitoring-scc-errors)
  * [ Create Artifact Registry Cleanup Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-artifact-registry-cleanup-policies)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Create Inventory of Security Data Assets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-inventory-of-security-data-assets)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Define Allowed Services for Service Perimeter ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-allowed-services-for-service-perimeter)
  * [ Define Cloud Billing Budget Threshold ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-billing-budget-threshold)
  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Define Mobile Code Policies and Controls ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-mobile-code-policies-and-controls)
  * [ Define Rotation Period for Cloud KMS Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-key-rotation-period)
  * [ Define Service Perimeters in VPC Service Controls ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-service-perimeter)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Define the Maximum Number of Concurrent Sessions for System Accounts in Workforce Identity Pools ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-maximum-concurrent-sessions-for-system-accounts)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Define Worker Pools for Cloud Builds ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-worker-pools-for-cloud-builds)
  * [ Develop System and Communications Protection Policy and Procedures ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#develop-system-communications-protection-policy-procedures)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Employ Monthly Checks for Flaw Remediation Status ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#employ-automated-flaw-status-checks-monthly)
  * [ Employ Spam Protection Mechanisms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#employ-spam-protection-mechanisms)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable Audit Logs Bucket Enumeration ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-bucket-enumeration)
  * [ Enable Audit Logs for All Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-for-allservices)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Data Write Audit Logs for Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-write-audit-logs-orgpolicy)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Enable Encryption for Mobile Devices ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-mobile-devices)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Events Data Sharing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-events-data-sharing)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable SDP for Data Discovery ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-sdp-data-discovery)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enable System Use Notifications on VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-system-use-notifications)
  * [ Enable the Confidential VM Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-vm-service)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Enforce 2-Step Verification for Super Admin Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-mfa-for-super-admin-accounts)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Enforce Domain Restricted Sharing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-domain-restricted-sharing)
  * [ Enforce HTTPS Traffic Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-https-traffic-only-policy)
  * [ Enforce IAM Least Privilege ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-iam-leastpriviledge-orgpolicy)
  * [ Enforce Least Privilege ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-access-control-policy-by-least-privilege)
  * [ Enforce Least Privilege Guide ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-least-privilege-overall-guide)
  * [ Enforce Separation of Duties ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-separation-of-duties)
  * [ Enforce Session Lock Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-lock-policy)
  * [ Enforce SSL Encryption for Remote Access ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-encryption-for-remote-access)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Generate Auditable Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#generate-audit-events)
  * [ Implement Authorized Decision Makers for Access Requests ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-authorized-decision-makers)
  * [ Implement Centralized Security Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-centralized-security-monitoring)
  * [ Implement certificate lifecycle management ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-certificate-lifecycle-management)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)
  * [ Implement Error Handling Mechanism ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-error-handling)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Implement On-Demand Audit Log Access ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-on-demand-audit-log-access)
  * [ Implement Remote Access Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-remote-access-policy)
  * [ Implement Secure Domain Name Resolution Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-secure-domain-name-resolution-service)
  * [ Implement Security Alert Advisory Management ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-security-alert-advisory-management)
  * [ Import Google Workspace Audit Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#import-google-workspace-audit-logs)
  * [ Inspect the External Load Balancer and SSL Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#inspect-loadbalancer-ssl)
  * [ Limit KMS Crypto Keys Users to Three ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#limit-kms-crypto-keys-users)
  * [ Limit Super Admin Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-logging-on-super-admin-accounts)
  * [ Maintain Resource Isolation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#maintain-resource-isolation)
  * [ Manage Access to Audit Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-audit-log-access)
  * [ Manage Access to Google Cloud Resources from Mobile Devices ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-access-from-mobile-devices)
  * [ Manage Data Handling and Retention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-data-handling-and-retention)
  * [ Manage Malicious Code Protection Mechanisms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-malicious-code-protection-mechanisms)
  * [ Manage Publicly Accessible Content ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-public-content-access)
  * [ Manage System Integrity Policies and Procedures ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-system-integrity-policies-procedures)
  * [ Perform Integrity Checks Every Month ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#perform-integrity-verification-checks-monthly)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Protect System Memory ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#protect-system-memory)
  * [ Remove Inactive Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#remove-inactive-accounts)
  * [ Remove Temporary Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#remove-temporary-accounts)
  * [ Require Additional Logging for Sensitive Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-additional-logging-for-sensitive-buckets)
  * [ Require Audit Logging for Privileged Activities ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-audit-logging-for-privileged-activities)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Require Least Privilege ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-non-privileged-iam-accounts-for-non-security-functions-access)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)
  * [ Require Unique Super Admin Account ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-unique-super-admin-account)
  * [ Restrict Access Control Points for Authorized and Managed Remote Access ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-control-points-for-authorized-remote-access)
  * [ Restrict Access to Audit Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-audit-log-access)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Restrict Cloud Shell Access Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloudshell-access-settings)
  * [ Restrict CMEK Crypto Key Projects ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cmek-crypto-key-projects)
  * [ Restrict External IP Addresses to Specific VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-external-ip-to-specific-vm-instances)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)
  * [ Restrict Non-Privileged Users from Executing Privileged Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-iam-audit-logs)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)
  * [ Restrict VM IP Forwarding for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-vm-ip-forwarding-compute-engine)
  * [ Restrict VPC Networks on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-vpc-networks-vertexai)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)
  * [ Review Authentication, Authorization, User Account Management ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#review-authentication-authorization-user-management)
  * [ Review Log and Alert Configuration ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#review-log-alert-configuration)
  * [ Separate User and Administrator Roles ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#separate-user-admin-roles)
  * [ Set Ingress and Egress Controls for Compute ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-compute-egress-ingress-controls)
  * [ Set Log Bucket Flag for Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-logbucket-for-bucket-logging)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Set Up Job Scheduling and Configurations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-up-scheduling-configurations)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Synchronize System Clocks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#synchronize-system-clocks)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)
  * [ Triage and Remediate System Flaws ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#triage-remediate-system-flaws)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)
  * [ Use IAM Tags ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-iam-tags)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)
  * [ Use Secure Web Proxy for Network Traffic Control ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-secure-web-proxy-traffic-control)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  dora-article-10

Financial entities must implement mechanisms for prompt detection of anomalous activities and support ICT related incident response.

  * [ Activate Security Command Center ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#activate-security-command-center)
  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Automate Integrity Verification ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#automate-integrity-verification)
  * [ Automate Near Real-time Event Analysis ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#automate-real-time-event-analysis)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Configure a Wireless Intrusion Detection Mechanism ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-wireless-intrusion-detection-mechanism)
  * [ Configure Log Metrics and Alerts for Cloud Storage IAM Policy Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-log-metrics-for-bucket-iam-changes)
  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Create Alerts for Monitoring Security Command Center Errors ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-alerts-for-monitoring-scc-errors)
  * [ Create Artifact Registry Cleanup Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-artifact-registry-cleanup-policies)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Employ Monthly Checks for Flaw Remediation Status ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#employ-automated-flaw-status-checks-monthly)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable Audit Logs Bucket Enumeration ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-bucket-enumeration)
  * [ Enable Audit Logs for All Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-for-allservices)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable Data Write Audit Logs for Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-write-audit-logs-orgpolicy)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Generate Auditable Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#generate-audit-events)
  * [ Implement Alerting for Incidence Response ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-alerting-incident-response-mechanism)
  * [ Implement Audit Lifecycle Management ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-audit-lifecycle-management)
  * [ Implement Centralized Security Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-centralized-security-monitoring)
  * [ Implement Error Handling Mechanism ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-error-handling)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Implement Security Alert Advisory Management ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-security-alert-advisory-management)
  * [ Import Google Workspace Audit Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#import-google-workspace-audit-logs)
  * [ Incorporate Integrity Monitoring into Incident Response ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#incorporate-integrity-monitoring-in-incident-response)
  * [ Limit Super Admin Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-logging-on-super-admin-accounts)
  * [ Manage Access to Audit Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-audit-log-access)
  * [ Manage Data Handling and Retention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-data-handling-and-retention)
  * [ Manage Malicious Code Protection Mechanisms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-malicious-code-protection-mechanisms)
  * [ Manage System Integrity Policies and Procedures ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-system-integrity-policies-procedures)
  * [ Perform Integrity Checks Every Month ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#perform-integrity-verification-checks-monthly)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Protect System Memory ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#protect-system-memory)
  * [ Require Additional Logging for Sensitive Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-additional-logging-for-sensitive-buckets)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Restrict Access to Audit Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-audit-log-access)
  * [ Restrict Resource Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-service-usage)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)
  * [ Review Log and Alert Configuration ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#review-log-alert-configuration)
  * [ Set Log Bucket Flag for Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-logbucket-for-bucket-logging)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Synchronize System Clocks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#synchronize-system-clocks)
  * [ Triage and Remediate System Flaws ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#triage-remediate-system-flaws)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)



##  EU Data Boundary

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Supports compliance with EU data residency requirements by restricting resource locations to EU regions.

This framework includes the following cloud controls: 

  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Disable the Creation and Update of Kafka Connect Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-kafka-connect-clusters-create-and-update)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable Looker (Google Cloud core) Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#looker-regulatory-settings)
  * [ Enable Regulatory Settings for Apigee ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#apigee-regulatory-settings)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)



##  EU Data Boundary and Support

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Supports compliance with EU data residency and support requirements by restricting resource locations to EU regions and limiting support access to EU-based personnel.

This framework includes the following cloud controls: 

  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Configure Spanner to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#spanner-regulatory-settings)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Disable Spanner Multi-Region Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-spanner-multi-region)
  * [ Disable the Creation and Update of Kafka Connect Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-kafka-connect-clusters-create-and-update)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Advanced Service Controls for Spanner ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-spanner-advanced-service-controls)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable Looker (Google Cloud core) Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#looker-regulatory-settings)
  * [ Enable Regulatory Settings for Apigee ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#apigee-regulatory-settings)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)



##  FedRAMP High

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Controls for meeting FedRAMP High compliance requirements.

This framework includes the following cloud controls: 

  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Configure Google Cloud Serverless for Apache Spark to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#serverless-regulatory-settings)
  * [ Configure Spanner to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#spanner-regulatory-settings)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Define the Permitted Versions for Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-function-generations)
  * [ Disable Creation of Global Load Balancers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-load-balancing)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Regulatory Settings for Cloud Deploy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#clouddeploy-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Identity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-identity-ruleset)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable Looker (Google Cloud core) Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#looker-regulatory-settings)
  * [ Enable Regulatory Settings for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-dns-regulatory-settings)
  * [ Enable Regulatory Settings for Gemini Enterprise ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gemini-enterprise-regulatory-settings)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict the BigQuery Data Transfer Service API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#bigquery-datatransfer-regulatory-settings)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)



##  FedRAMP Low 20x

**Supported cloud provider:** Google Cloud 

A Government-wide program that provides a standardized, reusable approach to security assessment and authorization for cloud computing products and services that process unclassified information used by agencies. FedRAMP Low impact is most appropriate for CSOs where the loss of confidentiality, integrity and availability would result in limited adverse effect on an agency's operations, assets or individuals.

This framework includes the cloud control groups and cloud controls in the following sections. 

###  ksi-ced-1

Ensure employees receive security awareness training.

  * [ Conduct Security Awareness Training ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#conduct-security-awareness-training)



###  ksi-ced-2

Mandate role-specific training for high-risk roles, in particular for roles with privileged access.

  * [ Conduct Role-specific Training ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#conduct-role-specific-training)



###  ksi-cmt-1

Log and monitor system modifications. Ensure that all system changes are documented and configuration baselines are updated.

  * [ Configure Log Metrics and Alerts for Audit Logging Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-log-metrics-for-audit-logging-changes)
  * [ Configure Log Metrics and Alerts for Cloud SQL Configuration Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-log-metrics-for-sql-config-changes)
  * [ Configure Log Metrics and Alerts for Cloud Storage IAM Policy Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-log-metrics-for-bucket-iam-changes)
  * [ Configure Log Metrics and Alerts for Custom Role Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-log-metrics-for-custom-role-changes)
  * [ Configure Log Metrics and Alerts for VPC Network Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-log-metrics-for-network-changes)
  * [ Configure Log Metrics and Alerts for VPC Network Firewall Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-log-metrics-for-firewall-changes)
  * [ Configure Log Metrics and Alerts for VPC Route Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-log-metrics-for-network-route-changes)
  * [ Restrict Non-Privileged Users from Executing Privileged Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-iam-audit-logs)



###  ksi-cmt-3

Implement automated testing and validation of changes before deployment.

  * [ Require Automated Testing and Validation of Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-automated-testing-and-validation-of-changes)



###  ksi-cmt-4

Implement a documented change management procedure.

  * [ Define Change Management Procedures ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-change-management-procedures)



###  ksi-cmt-5

Evaluate the risk and potential impact of every change.

  * [ Evaluate Risk and Impact of Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#evaluate-risk-and-impact-of-changes)



###  ksi-cna-1

Configure all information resources to limit inbound and outbound traffic.

  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Extract External IP Addresses for VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#compute-external-ip-list)
  * [ Extract GKE Public IP Addresses List ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#get-cloud-gke-public-ip-list)
  * [ Extract Public IP Addresses for Cloud SQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#get-cloud-sql-public-ip-list)
  * [ Restrict External IP Addresses to Specific VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-external-ip-to-specific-vm-instances)
  * [ Retrieve Cloud NAT Configurations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#get-nat-configuration)
  * [ Set Ingress and Egress Controls for Compute ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-compute-egress-ingress-controls)



###  ksi-cna-2

Design systems to help reduce the attack surface and minimize lateral movement if compromised.

  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)



###  ksi-cna-3

Implement traffic flow controls using logical networking and related capabilities.

  * [ Configure VPC Firewall Rules, Subnets, and VPN Gateway ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-vpc-firewall-subnet-gateway)
  * [ Define Allowed Services for Service Perimeter ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-allowed-services-for-service-perimeter)
  * [ Define Service Perimeters in VPC Service Controls ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-service-perimeter)
  * [ Define Worker Pools for Cloud Builds ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-worker-pools-for-cloud-builds)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Retrieve VPC Network Peering Configurations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#get-vpc-peering-configurations)



###  ksi-cna-4

Use immutable infrastructure with strictly defined functionality and privileges.

  * [ Define External Build Integrations for Cloud Build ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-external-build-integrations)
  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)
  * [ Guidance for Immutable Infrastructure on Google Cloud ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#guidance-for-immutable-infrastructure-on-google-cloud)
  * [ Review Artifact Registry Images ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#review-artifact-registry-images)
  * [ Review Cloud Run Images ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#review-cloud-run-images)
  * [ Review Hardened Compute Images ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#review-hardened-compute-images)
  * [ Verify GKE Container Optimized OS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-gke-container-optimized-os)



###  ksi-cna-5

Enforce denial-of-service protection to help protect information systems resources built on Google Cloud.

  * [ Enable L7 DDoS Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-l7-ddos-protection)



###  ksi-cna-6

Design information systems with high availability and rapid recovery capabilities to help prevent data loss.

  * [ Assess the Availability of Compute and GKE Resources ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#assess-resource-availability)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ GKE Node Pool Autoscaling ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-gke-node-pool-autoscaling)
  * [ Retrieve GKE Availability ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retrieve-gke-availability)
  * [ Verify Cloud SQL Failover Replication ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-sql-failover-replication)
  * [ Verify Cloud Storage Regional Deployment ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-storage-regional-deployment)



###  ksi-cna-7

Implement cloud-first information resources that are based on the host provider's best practices and documented guidance.

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Implement Best Practices for Cloud Deployments ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-best-practices-for-cloud-deployments)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)



###  ksi-iam-1

Enforce multi-factor authentication (MFA) using methods that are difficult to intercept or impersonate (phishing-resistant MFA) for user authentication.

  * [ Enforce 2-Step Verification for Super Admin Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-mfa-for-super-admin-accounts)
  * [ Enforce Two-Step Verification ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-mfa)



###  ksi-iam-2

Implement secure, passwordless methods when feasible, or enforce strong passwords with multi-factor authentication (MFA) for secure user authentication and authorization.

  * [ Enforce Password for MySQL Database ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-password-mysql-db)
  * [ Use Multifactor or Passwordless Authentication ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-multifactor-or-passwordless-authentication)



###  ksi-iam-3

Enforce secure authentication methods for all non-user accounts and services within Google Cloud to help protect data and resources from unauthorized access.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)



###  ksi-iam-4

Implement a security authorization model that is least-privileged, role and attribute-based, and just-in-time. Use this model for all user and non-user accounts and services to help reduce the risk of unauthorized access or misuse.

  * [ Automate Account Management System ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#automate-account-management-system)
  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Define IsLive Attribute for Delete Action Lifestyle Rule on Bucket ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-islive-for-delete-action-lifestyle-rule-on-bucket)
  * [ Use Least Privilege and Just in Time Access ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privilege-and-just-in-time-access)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  ksi-iam-5

Enforce zero-trust design principles on your applications and services to enhance security.

  * [ Implement Zero-Trust Principles ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-zero-trust-principles)



###  ksi-iam-6

Automatically disable or secure accounts with privileged access when suspicious activity is detected to help mitigate security risks.

  * [ Disable Suspicious Accounts Automatically ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-suspicious-accounts-automatically)



###  ksi-inr-1

Report incidents according to FedRAMP requirements and cloud service provider policies.

  * [ Report Security Incidents to US-CERT ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#report-security-incidents-to-us-cert)



###  ksi-inr-2

Maintain a log of incidents and review past incidents for patterns or vulnerabilities at regular intervals.

  * [ Require Incident Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-incident-logs)



###  ksi-inr-3

Generate after-action reports, and incorporate lessons learned into operations.

  * [ Generate After Action Reports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#generate-after-action-reports)



###  ksi-mla-1

Implement a centralized and tamper-resistant logging system using a Security Information and Event Management (SIEM) or similar system to record all application and service events, activities, and changes.

  * [ Use Central SIEM ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-central-siem)



###  ksi-mla-2

Regularly review the audit logs of your applications and services.

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable Data Write Audit Logs for Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-write-audit-logs-orgpolicy)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Import Google Workspace Audit Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#import-google-workspace-audit-logs)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Require IAM Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-iam-logs)
  * [ Review Log and Alert Configuration ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#review-log-alert-configuration)



###  ksi-mla-3

Detect vulnerabilities and promptly remediate or mitigate them to help reduce the risk impact on applications and services.

  * [ Create Alerts for Monitoring Security Command Center Errors ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-alerts-for-monitoring-scc-errors)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable Security Command Center ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-scc)



###  ksi-mla-4

Conduct regular authenticated vulnerability scans on information resources.

  * [ Perform Authenticated Vulnerability Scans ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#perform-authenticated-vulnerability-scans)



###  ksi-mla-5

Implement Infrastructure as Code (IaC) and perform configuration evaluation and testing.

  * [ Enforce Configuration Management for IAC ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-iac-configuration-management)



###  ksi-mla-6

Track and prioritize the mitigation and remediation of identified vulnerabilities in a central system.

  * [ Centrally Track Remediation of Vulnerabilities ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#centrally-track-remediation-of-vulnerabilities)



###  ksi-piy-1

Maintain an updated information resource inventory or code that defines all deployed assets, software, and services.

  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Maintain Resource Inventory ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#maintain-resource-inventory)
  * [ Review Resource Inventory ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#review-resource-inventory)



###  ksi-piy-2

Outline policies with the security objectives for all information resources.

  * [ Define Security Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policies)



###  ksi-piy-3

Maintain a vulnerability disclosure program that includes intentional, organized, universal guidance for how every information resource, including personnel, is secured.

  * [ Maintain a Vulnerability Disclosure Program ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#maintain-a-vulnerability-disclosure-program)



###  ksi-piy-4

Build security considerations into the Software Development Lifecycle (SDLC) and align with Cybersecurity and Infrastructure Security Agency's (CISA's) Secure By Design principles.

  * [ Enforce HTTPS Traffic Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-https-traffic-only-policy)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Implement Software Development Lifecycle Security Considerations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-software-development-lifecycle-security-considerations)



###  ksi-piy-5

Document the methods that are used to evaluate information resource implementations.

  * [ Document Information Resource Implementations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#document-information-resource-implementations)



###  ksi-piy-6

Maintain dedicated staff and budget for security with executive support, in line with the size, complexity, scope, and risk of the service offering.

  * [ Provide Dedicated Resources for Security ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#provide-dedicated-resources-for-security)



###  ksi-piy-7

Document risk management decisions for software supply chain security.

  * [ Document and Manage Software Supply Chain Security Risk Management ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#document-and-manage-software-supply-chain-security-risk-management)



###  ksi-rpl-1

Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) to ensure minimal service disruption and data loss during incidents and contingencies.

  * [ Define Recovery Time and Recovery Point Objectives ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-recovery-time-and-recovery-point-objectives)



###  ksi-rpl-2

Develop and maintain a recovery plan that aligns with the defined recovery objectives.

  * [ Develop a Recovery Plan ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#develop-a-recovery-plan)



###  ksi-rpl-3

Perform system backups that are aligned with recovery objectives.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)
  * [ Perform System Backups ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#perform-system-backups)



###  ksi-rpl-4

Test your organization's ability to recover from incidents and contingencies at regular intervals.

  * [ Test Incident Response Capabilities ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#test-incident-response-capabilities)



###  ksi-svc-1

Regularly review and strengthen the network and system configurations to help ensure a secure baseline.

  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Require Security Hardening ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-security-hardening)



###  ksi-svc-2

Encrypt all core content data that is exchanged between machines that connect to Google Cloud, or alternatively, secure all network traffic to help protect data.

  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Ensure Minimum TLS Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#ensure-min-tls)



###  ksi-svc-3

Ensure all federal and sensitive information at rest is encrypted.

  * [ Use Default Encryption ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-default-encryption)



###  ksi-svc-4

Manage configurations centrally to ensure consistent governance and security.

  * [ Manage Configurations Centrally ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#manage-configurations-centrally)



###  ksi-svc-5

Implement cryptographic mechanisms and integrity verification tools to enforce system and information resource integrity and help detect unauthorized changes.

  * [ Retrieve Binary Authorization Configurations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retrieve-binary-authorization-configuration)



###  ksi-svc-6

Use automated key management systems to help protect, manage, and regularly rotate digital keys and certificates.

  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Implement certificate lifecycle management ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-certificate-lifecycle-management)
  * [ Retrieve Cloud KMS Configurations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retrieve-kms-configurations)



###  ksi-svc-7

Implement a consistent, risk-informed approach for applying security patches to your applications and services.

  * [ Employ Monthly Checks for Flaw Remediation Status ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#employ-automated-flaw-status-checks-monthly)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Require Auto Upgrade Schedule Set for Agent Platform Workbench ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-vertexai-auto-upgrade-schedule-set)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)



###  ksi-tpr-1

Identify all third-party information resources to understand, monitor, and manage supply chain risks.

  * [ Identify Third-Party Information Resources ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#identify-third-party-information-resources)



###  ksi-tpr-2

Ensure that the services that are federal information or are likely to impact the confidentiality, integrity, or availability of federal information are FedRAMP authorized and securely configured.

  * [ Confirm FedRAMP Authorization of Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#confirm-fedramp-authorization-of-services)
  * [ Restrict Resource Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-service-usage)



###  ksi-tpr-3

Identify and prioritize mitigation of potential supply chain risks.

  * [ Identify Supply Chain Risks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#identify-supply-chain-risks)



###  ksi-tpr-4

Monitor third-party software information resources for upstream vulnerabilities, using contractual notification requirements or active monitoring services.

  * [ Monitor Third-Party Information Resources for Upstream Vulnerabilities ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#monitor-third-party-information-resources-for-upstream-vulnerabilities)



##  FedRAMP Moderate

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Controls for meeting FedRAMP Moderate compliance requirements.

This framework includes the following cloud controls: 

  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Configure Google Cloud Serverless for Apache Spark to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#serverless-regulatory-settings)
  * [ Configure Spanner to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#spanner-regulatory-settings)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Looker (Google Cloud core) Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#looker-regulatory-settings)
  * [ Enable Regulatory Settings for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-dns-regulatory-settings)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict the BigQuery Data Transfer Service API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#bigquery-datatransfer-regulatory-settings)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)



##  HIPAA

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Health Insurance Portability and Accountability Act

This framework includes the cloud control groups and cloud controls in the following sections. 

###  hipaa-security-ss164-308-a-3-i-workforce-security

Implement policies and procedures to ensure that all members of its workforce have appropriate access to electronic protected health information and to prevent those workforce members who do not have access from obtaining access to electronic protected health information.

  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)



###  hipaa-security-ss164-308-a-3-ii-a-workforce-security-authorization-and-or-supervision

Implement procedures for the authorization and/or supervision of workforce members who work with EPHI or in locations where it might be accessed.

  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)



###  hipaa-security-ss164-308-a-7-ii-a-contingency-plan-data-backup-plan

Establish and implement procedures to create and maintain retrievable exact copies of EPHI.

  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)



###  hipaa-security-ss164-310-d-2-iii-device-and-media-controls-accountability

Maintain a record of the movements of hardware and electronic media and any person responsible therefore.

  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)



###  hipaa-security-ss164-312-a-1-access-control

Implement technical policies and procedures for electronic information systems that maintain electronic protected health information to allow access only to those persons or software programs that have been granted access rights

  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)



###  hipaa-security-ss164-312-a-2-iv-access-control-encryption-and-decryption

Implement a mechanism to encrypt and decrypt EPHI.

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Define Rotation Period for Cloud KMS Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-key-rotation-period)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)



###  hipaa-security-ss164-312-b-audit-controls

Implement hardware, software, and/or procedural mechanisms that record and examine activity in information systems that contain or use electronic protected health information.

  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)



###  hipaa-security-ss164-312-e-1-transmission

Implement technical security measures to guard against unauthorized access to electronic protected health information that is being transmitted over an electronic communications network.

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)



###  hipaa-security-ss164-312-e-2-i-transmission-security-integrity-controls

Implement security measures to ensure that electronically transmitted EPHI is not improperly modified without detection until disposed of.

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)



###  hipaa-security-ss164-312-e-2-ii-transmission-security-encryption

Implement a mechanism to encrypt EPHI whenever deemed appropriate.

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Define Rotation Period for Cloud KMS Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-key-rotation-period)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)



##  IL2

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Controls for meeting IL2 compliance requirements.

This framework includes the following cloud controls: 

  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Configure Spanner to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#spanner-regulatory-settings)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Define the Permitted Versions for Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-function-generations)
  * [ Disable Creation of Global Load Balancers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-load-balancing)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Regulatory Settings for Cloud Deploy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#clouddeploy-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Identity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-identity-ruleset)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable Looker (Google Cloud core) Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#looker-regulatory-settings)
  * [ Enable Regulatory Settings for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-dns-regulatory-settings)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict the BigQuery Data Transfer Service API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#bigquery-datatransfer-regulatory-settings)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)



##  IL4

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Controls for meeting IL4 compliance requirements.

This framework includes the following cloud controls: 

  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Configure Spanner to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#spanner-regulatory-settings)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Disable Compute Instance Data Access APIs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-compute-instance-data-access)
  * [ Disable Creation of Global Load Balancers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-load-balancing)
  * [ Disable GKE Diagnostic Administrative Access ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-diagnostic-access)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Disable Spanner Multi-Region Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-spanner-multi-region)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Identity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-identity-ruleset)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable Regulatory Settings for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-dns-regulatory-settings)
  * [ Enable Regulatory Settings for Gemini Enterprise ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gemini-enterprise-regulatory-settings)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)
  * [ Specify Cloud KMS Key Protection Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-kms-protection-levels)



##  IL5

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Controls for meeting IL5 compliance requirements.

This framework includes the following cloud controls: 

  * [ Allow Only IL5 Compliant APIs for Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gemini-enterprise-agent-platform-allow-il5-compliant-apis)
  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Configure Spanner to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#spanner-regulatory-settings)
  * [ Create CMEK Project and Key Ring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-cmek-project-and-keyring)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Disable Compute Instance Data Access APIs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-compute-instance-data-access)
  * [ Disable Creation of Global Load Balancers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-load-balancing)
  * [ Disable diagnostic and administrative access pathways in Cloud SQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloudsql-diagnostic-access)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Disable Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#iam-disable-service-account-key-creation)
  * [ Disable Spanner Multi-Region Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-spanner-multi-region)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Identity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-identity-ruleset)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable Regulatory Settings for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-dns-regulatory-settings)
  * [ Prevent Automatic Creation of Default Network ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-default-network-creation)
  * [ Prevent Automatic Granting of Editor Role to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-default-service-accounts-auto-editor)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Cloud SQL Resource Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#sql-restrict-noncompliant-resource-creation)
  * [ Restrict Public Access to Data Stored in Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#storage-public-access-prevention)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)
  * [ Set Zonal DNS as Default for Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gce-zonal-dns-default)
  * [ Specify Cloud KMS Key Protection Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-kms-protection-levels)



##  ISO 27001:2022

**Supported cloud provider:** Google Cloud 

The international standard for an Information Security Management System (ISMS). It provides a systematic, risk-based approach to managing sensitive information by specifying requirements for establishing and improving security controls.

This framework includes the cloud control groups and cloud controls in the following sections. 

###  iso-27001-2022-a-5-1

Information security policy and topic-specific policies shall be defined, approved by management, published, communicated to and acknowledged by relevant personnel and relevant interested parties, and reviewed at planned intervals and if significant changes occur.

  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)



###  iso-27001-2022-a-5-10

Rules for the acceptable use and procedures for handling information and other associated assets shall be identified, documented and implemented.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)



###  iso-27001-2022-a-5-12

Information shall be classified according to the information security needs of the organization based on confidentiality, integrity, availability and relevant interested party requirements.

  * [ Define Set Storage Class Lifestyle Action on Bucket ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-set-storage-class-lifestyle-action-on-bucket)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)



###  iso-27001-2022-a-5-14

Information transfer rules, procedures, or agreements shall be in place for all types of transfer facilities within the organization and between the organization and other parties.

  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)



###  iso-27001-2022-a-5-15

Rules to control physical and logical access to information and other associated assets shall be established and implemented based on business and information security requirements.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-service-usage)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)



###  iso-27001-2022-a-5-17

Allocation and management of authentication information shall be controlled by a management process, including advising personnel on appropriate handling of authentication information.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)



###  iso-27001-2022-a-5-18

Access rights to information and other associated assets shall be provisioned, reviewed, modified and removed in accordance with the organization’s topic-specific policy on and rules for access control.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)



###  iso-27001-2022-a-5-19

Processes and procedures shall be defined and implemented to manage the information security risks associated with the use of supplier’s products or services.

  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)



###  iso-27001-2022-a-5-20

Relevant information security requirements shall be established and agreed with each supplier based on the type of supplier relationship.

  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)



###  iso-27001-2022-a-5-23

Processes for acquisition, use, management and exit from cloud services shall be established in accordance with the organization’s information security requirements.

  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Require Auto Upgrade Schedule Set for Agent Platform Workbench ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-vertexai-auto-upgrade-schedule-set)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-service-usage)



###  iso-27001-2022-a-5-24

The organization shall plan and prepare for managing information security incidents by defining, establishing and communicating information security incident management processes, roles and responsibilities.

  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)



###  iso-27001-2022-a-5-25

The organization shall assess information security events and decide if they are to be categorized as information security incidents.

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)



###  iso-27001-2022-a-5-28

The organization shall establish and implement procedures for the identification, collection, acquisition and preservation of evidence related to information security events.

  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)



###  iso-27001-2022-a-5-30

ICT readiness shall be planned, implemented, maintained and tested based on business continuity objectives and ICT continuity requirements.

  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)



###  iso-27001-2022-a-5-33

Records shall be protected from loss, destruction, falsification, unauthorized access and unauthorized release.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)



###  iso-27001-2022-a-5-5

The organization shall establish and maintain contact with relevant authorities.

  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)



###  iso-27001-2022-a-5-6

The organization shall establish and maintain contact with special interest groups or other specialist security forums and professional associations.

  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)



###  iso-27001-2022-a-5-9

An inventory of information and other associated assets, including owners, shall be developed and maintained.

  * [ Define Set Storage Class Lifestyle Action on Bucket ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-set-storage-class-lifestyle-action-on-bucket)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)



###  iso-27001-2022-a-6-7

Security measures shall be implemented when personnel are working remotely to protect information accessed, processed or stored outside the organization’s premises.

  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)



###  iso-27001-2022-a-8-1

Information stored on, processed by or accessible using user end point devices shall be protected.

  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)



###  iso-27001-2022-a-8-10

Information stored in information systems, devices or in any other storage media shall be deleted when no longer required.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)



###  iso-27001-2022-a-8-13

Backup copies of information, software and systems shall be maintained and regularly tested in accordance with the agreed topic-specific policy on backup.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)



###  iso-27001-2022-a-8-14

Information processing facilities shall be implemented with redundancy sufficient to meet availability requirements.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)



###  iso-27001-2022-a-8-15

Logs that record activities, exceptions, faults and other relevant events shall be produced, stored, protected and analysed.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Configure Log Sinks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-log-sinks)
  * [ Configure Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-network-traffic-monitoring)
  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)



###  iso-27001-2022-a-8-16

Networks, systems and applications shall be monitored for anomalous behaviour and appropriate actions taken to evaluate potential information security incidents.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Configure Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-network-traffic-monitoring)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)



###  iso-27001-2022-a-8-17

The clocks of information processing systems used by the organization shall be synchronized to approved time sources.

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)



###  iso-27001-2022-a-8-2

The allocation and use of privileged access rights shall be restricted and managed.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  iso-27001-2022-a-8-20

Networks and network devices shall be secured, managed and controlled to protect information in systems and applications.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure Log Sinks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-log-sinks)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)



###  iso-27001-2022-a-8-21

Security mechanisms, service levels and service requirements of network services shall be identified, implemented and monitored.

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)



###  iso-27001-2022-a-8-22

Groups of information services, users and information systems shall be segregated in the organization’s networks.

  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)



###  iso-27001-2022-a-8-23

Access to external websites shall be managed to reduce exposure to malicious content.

  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)



###  iso-27001-2022-a-8-24

Rules for the effective use of cryptography, including cryptographic key management, shall be defined and implemented.

  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Define Secret Manager Rotation Schedule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-secret-manager-rotation-schedule)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Enforce HTTPS Traffic Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-https-traffic-only-policy)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  iso-27001-2022-a-8-25

Rules for the secure development of software and systems shall be established and applied.

  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)



###  iso-27001-2022-a-8-26

Information security requirements shall be identified, specified and approved when developing or acquiring applications.

  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)



###  iso-27001-2022-a-8-27

Principles for engineering secure systems shall be established, documented, maintained and applied to any information system development activities.

  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Restrict API Keys for Required APIs Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-api-keys-for-required-apis-only)



###  iso-27001-2022-a-8-28

Secure coding principles shall be applied to software development.

  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)



###  iso-27001-2022-a-8-29

Security testing processes shall be defined and implemented in the development life cycle.

  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Configure Remote Access Inactivity Timeout ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-remote-access-inactivity-timeout)



###  iso-27001-2022-a-8-3

Access to information and other associated assets shall be restricted in accordance with the established topic-specific policy on access control.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  iso-27001-2022-a-8-30

The organization shall direct, monitor and review the activities related to outsourced system development.

  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)



###  iso-27001-2022-a-8-4

Read and write access to source code, development tools and software libraries shall be appropriately managed.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)



###  iso-27001-2022-a-8-5

Secure authentication technologies and procedures shall be implemented based on information access restrictions and the topic-specific policy on access control.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Configure Remote Access Inactivity Timeout ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-remote-access-inactivity-timeout)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)



###  iso-27001-2022-a-8-6

The use of resources shall be monitored and adjusted in line with current and expected capacity requirements.

  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)



###  iso-27001-2022-a-8-7

Protection against malware shall be implemented and supported by appropriate user awareness.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  iso-27001-2022-a-8-8

Information about technical vulnerabilities of information systems in use shall be obtained, the organization’s exposure to such vulnerabilities shall be evaluated and appropriate measures shall be taken.

  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Require Auto Upgrade Schedule Set for Agent Platform Workbench ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-vertexai-auto-upgrade-schedule-set)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Turn Off Local Infile Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-local-infile-db-flag-mysql)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  iso-27001-2022-a-8-9

Configurations, including security configurations, of hardware, software, services and networks shall be established, documented, implemented, monitored and reviewed.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Require Auto Upgrade Schedule Set for Agent Platform Workbench ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-vertexai-auto-upgrade-schedule-set)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



##  ITAR

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Controls for meeting International Traffic in Arms Regulations (ITAR) compliance requirements.

This framework includes the following cloud controls: 

  * [ Allow Only ITAR Compliant APIs for Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#gemini-enterprise-agent-platform-allow-itar-compliant-apis)
  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Create CMEK Project and Key Ring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-cmek-project-and-keyring)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Disable Compute Instance Data Access APIs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-compute-instance-data-access)
  * [ Disable Creation of Global Load Balancers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-load-balancing)
  * [ Disable Creation of Global Self-managed SSL Certificates ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-self-managed-ssl-certs-creation)
  * [ Disable GKE Diagnostic Administrative Access ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-diagnostic-access)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable VM Manager ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vm-manager)
  * [ Enforce In-Transit Regions for Pub/Sub Messages ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-in-transit-regions-for-pubsub)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Access to VM Core Memory ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-vm-core-memory-access)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)



##  Qatar National Information Assurance Standard v2.1

**Supported cloud provider:** Google Cloud 

Qatar NIAS is intended to provide organizations within the State of Qatar with the necessary foundation and the relevant tools to enable the implementation of a full-fledged Information Security Management System within organizations.

This framework includes the cloud control groups and cloud controls in the following sections. 

###  qa-nias-2-1-am-1

Users are provided access based on the concept of least privilege and governed by a Need to Know or a Need to Have basis.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)
  * [ Restrict API Keys for Required APIs Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-api-keys-for-required-apis-only)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  qa-nias-2-1-am-11

Centralized authentication repositories such as LDAP and authentication databases are protected from denial-of-service attacks and use secure and authenticated channels for retrieval of authentication data. Such repositories shall log the following events: unauthorized update or access; start and end date and time of activity (together with system identifier); user identification (for illegal logon); sign-on and sign-off activity (for illegal logon); and session, terminal, or remote connection.

  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)



###  qa-nias-2-1-am-12

Organizations must develop and maintain a set of policies, plans and procedures, derived from the National Data Classification Policy (IAP-NAT-DCLS) that covers system users' identification, authentication, and authorization.

  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)



###  qa-nias-2-1-am-14

All system users are uniquely identifiable and authenticated on each occasion that access is granted to a system.

  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)



###  qa-nias-2-1-am-17

Unprotected authentication information that grants system access, or decrypts an encrypted device is located on, or with the system or device, to which the authentication information grants access to.

  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)



###  qa-nias-2-1-am-18

System authentication data while in use is not susceptible to attacks including, but not limited to, replay, man-in-the-middle, and session hijacking.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)



###  qa-nias-2-1-am-2

Access is managed and controlled through system access controls, identification and authentication, and audit trails based on the sensitivity of the information. These requests for access shall be authorized by a staff member's supervisor or manager.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)



###  qa-nias-2-1-am-20

Passwords are changed at least every 90 days.

  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)



###  qa-nias-2-1-am-23

Screen and session locks are configured as follows: activate after a maximum of 15 minutes of system user inactivity; activate standardly by the system user, if desired; lock to completely conceal all information on the screen; ensure the screen does not appear to be turned off while in the locked state; have the system user re-authenticate to unlock the system; and deny system users the ability to disable the locking mechanism.

  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)



###  qa-nias-2-1-am-24

Access to a system is suspended after a specified number of failed logon attempts or as soon as possible after the staff member no longer needs access, due to changing roles or leaving the organization.

  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)



###  qa-nias-2-1-am-3

Access rights of a user or entity to create, read, update, delete or transmit an organization's information assets shall be based on a matrix (hierarchical) model of rights defined by business rules that are established by the owners of that information.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)
  * [ Restrict API Keys for Required APIs Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-api-keys-for-required-apis-only)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)



###  qa-nias-2-1-am-31

The use of privileged accounts is documented, controlled, accountable, and kept to a minimum. Privileged accounts shall only be used for administrative work.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)



###  qa-nias-2-1-am-32

System administrators are assigned an individual account for undertaking their administration tasks.

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)



###  qa-nias-2-1-am-34

The system management log is updated to record the following information: sanitization activities; system start-up and shutdown; component or system failures; maintenance activities; backup and archival activities; system recovery activities; and special or out of hours activities.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)



###  qa-nias-2-1-am-35

Remote access shall not be provided unless authorized explicitly by the department head and only if it is warranted by business requirements and only after due diligence has been performed to analyse associated risks and suitable controls are implemented to mitigate the identified risks.

  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)



###  qa-nias-2-1-am-36

Two-factor authentication, using a hardware token, biometric control or similar is used when accessing systems processing data classified at C3 or above.

  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)



###  qa-nias-2-1-am-37

Remote access sessions are secured by using suitable end-to-end encryption as specified in section C-10, Cryptographic Security (CY).

  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)



###  qa-nias-2-1-am-6

Any unauthorized effort to circumvent the organization's access control shall be perceived as a security incident and shall be handled in accordance with established incident handling procedure and appropriate human resources policies and procedures.

  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  qa-nias-2-1-am-7

Audit logs shall be enabled and maintained in such a manner as to allow compliance monitoring with government policy and to assist in Incident Management.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  qa-nias-2-1-am-8

Logical access to organization networks is technically controlled. This may be by using Network Admission Control (NAC) services and devices.

  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)



###  qa-nias-2-1-cy-1

Cryptographic algorithms, encryption hardware or software, key management systems, and digital signatures shall demonstrate compliance with the Approved Encryption/Cryptographic Algorithms and Systems as specified by the competent authority within the Law No. (16) of 2010 on the Promulgation of the Electronic Commerce and Transactions Law.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-service-usage)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  qa-nias-2-1-cy-2

The lifetime of the key shall be determined primarily by the application and the information infrastructure it is used in. Keys shall be immediately revoked and replaced if they have been or suspected of being compromised.

  * [ Define Secret Manager Rotation Schedule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-secret-manager-rotation-schedule)



###  qa-nias-2-1-cy-3

Information assets classified as C3 (IAP-NAT-DCLS) are encrypted and protected against unauthorized disclosure when stored and in transit regardless of the storing format or media. Organizations may apply these cryptographic controls to assets with lower confidentiality requirements, if determined necessary by their risk assessment.

  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-service-usage)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)



###  qa-nias-2-1-cy-4

Information assets classified as I3 (IAP-NAT-DCLS) have assured integrity using cryptographic hashing. Organizations may apply these cryptographic controls to assets with lower integrity requirements, if determined necessary by their risk assessment.

  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)



###  qa-nias-2-1-cy-5

The following protocols or better, with approved algorithms outlined in Qatar National Cryptographic Standard - English v1.0 (or higher) issued by the competent authority, are used for securing data classified as C3 when in transit: for securing web traffic: TLS (+128 bits) (RFC4346); for securing file transfers: SFTP (SFTP); for secure remote access: SSH v2 (RFC4253) or IPSEC (RFC 4301); and only S/MIME v3 (RFC3851) or better are used for securing emails. See CY11 for the associated requirement.

  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)



###  qa-nias-2-1-cy-6

Passwords must always be encrypted or hashed and protected against unauthorized disclosure when they are stored or in transit, regardless of the storing format or media. Privileged passwords shall be encrypted and stored off-site with backup files each time the password is changed to ensure complete recovery.

  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)



###  qa-nias-2-1-cy-7

Where Hardware Security Modules (HSMs) are used, they are certified to at least FIPS 2-140 Level 2 (FIPS2-140) or Common Criteria (CC3.1) EAL4.

  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)



###  qa-nias-2-1-cy-9

Suitable key management processes are defined, as per (ISO1-11770) and used to manage the lifecycle of cryptographic keys, covering the following functions: Key Custodians Roles and Responsibilities, Key Generation, Dual Control and Split Knowledge, Secure Key Storage, Key Usage, Secure Key Distribution and in Transit, Key Backup and Recovery, Periodic Key Status Checking, Key Compromise, Key Revocation and Destruction, and Audit Trails and Documentation.

  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)



###  qa-nias-2-1-gs-1

Networks are protected from other networks by gateways and data flows are properly controlled.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)



###  qa-nias-2-1-gs-13

Export of data to a less classified system is restricted by filtering data using at least checks on classification labels.

  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)



###  qa-nias-2-1-gs-2

Gateways connecting organization networks to other organization networks, or to uncontrolled public networks, are implemented as follows: with an appropriate network device to control data flow, with all data flows appropriately controlled, and with gateway components physically located within an appropriately secured server room.

  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)



###  qa-nias-2-1-gs-6

Demilitarized zones (DMZs) are used to separate externally accessible systems from uncontrolled public networks and internal networks through usage of firewalls and other network security capable equipment.

  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)



###  qa-nias-2-1-gs-7

Gateways must: be the only communications paths into and out of internal networks; by default, deny all connections into and out of the network; allow only explicitly authorised connections; be managed using a secure path isolated from all connected networks; provide sufficient audit capability to detect gateway security breaches and attempted network intrusions; and provide real-time alarms.

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  qa-nias-2-1-gs-8

Gateways are hardened prior to any implementation on production site and are protected against the following: malicious code and vulnerabilities, wrong or poor configurations, account compromise and privilege escalation, rogue network monitoring, denial of service (DoS) attacks, and information or data leakage.

  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  qa-nias-2-1-gs-9

Monitoring and supervision of gateways is in place and includes threat prevention mechanisms, logging, alerts, and surveillance of equipment. See section B-10, Logging and Security Monitoring (SM).

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  qa-nias-2-1-ie-12

Ensure information exchanged between systems is secured against misuse, unauthorized access, or data corruption. For transmitting information classified at C2, I2 or above, authenticated, and encrypted channels shall be used as specified in CY5, section C-10, Cryptographic Security (CY).

  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)



###  qa-nias-2-1-ie-3

Ensure that necessary agreements (specifically confidentiality agreements) between the entities exchanging information have been established prior to information exchange. Agreements shall provide information on responsibilities, information exchange notification procedure, technical standards for transmission, identification of couriers, liabilities, ownership, and controls. For vendors and third-parties a formal Non-Disclosure Agreement (NDA) shall be used. Appendix D provides an NDA template.

  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)



###  qa-nias-2-1-ie-4

The organization must ensure media which is used to exchange information is protected against unauthorized access, manipulation, or misuse within or outside the organization environment.

  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)



###  qa-nias-2-1-ie-8

Protect information exchanged using electronic messaging from unauthorized access, change, or interruption of service.

  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)



###  qa-nias-2-1-ms-20

Media, including faulty media, containing classified information is sanitised to the extent possible prior to disposal.

  * [ Define Set Storage Class Lifestyle Action on Bucket ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-set-storage-class-lifestyle-action-on-bucket)



###  qa-nias-2-1-ns-1

Details of internal network and system configuration, employee or device-related directory services, and other sensitive technology are not publicly disclosed or enumerable by unauthorized personnel.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)



###  qa-nias-2-1-ns-17

A separate internal DNS server is set up and placed in the internal network for internal domain information that is not disclosed to the Internet.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)



###  qa-nias-2-1-ns-2

The organization removes or disables all the default accounts (for example, root or administrator) or changes the password as specified in section C-6, Software Security (SS).

  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)



###  qa-nias-2-1-ns-20

Zones files are digitally signed, and cryptographic mutual authentication and data integrity of zone transfers and dynamic updates is provided.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)



###  qa-nias-2-1-ns-21

Cryptographic origin authentication and integrity assurance of DNS data is provided.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)



###  qa-nias-2-1-ns-22

DNS services including zone transfers are provided to authorized users only.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)



###  qa-nias-2-1-ns-25

The Internet gateway denies all Internet services unless specifically enabled.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)



###  qa-nias-2-1-ns-27

The organization has the capability needed to monitor the traffic, deduce traffic patterns, usage, and so. See section B-10, Logging and Security Monitoring (SM) for more information.

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  qa-nias-2-1-ns-29

TLS protection is used with the SMTP mail server in line with section C-10, Cryptographic Security (CY).

  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)



###  qa-nias-2-1-ns-5

Networks are designed and configured to limit opportunities of unauthorized access to information transiting the network infrastructure. Organizations should use the following technologies to meet this requirement: switches instead of hubs; port security on switches to limit access and disable all unused ports; routers and firewalls segregating parts of the network on a need-to-know basis; IPsec or IP version 6; application-level encryption; an automated tool that compares the running configuration of network devices against the documented configuration; network edge authentication; restrict and manage end-user devices communicating to organization network through techniques such as MAC address filtering; IPS or IDS to detect and prevent malicious activity within the network; and time and day restrictions.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)



###  qa-nias-2-1-ns-53

Voice and data are separate networks. The separation should be physical, but use of Virtual LANS is permitted. The voice gateway, which interfaces with the PSTN, segregates H.323, SIP, or other VoIP protocols from the data network.

  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)



###  qa-nias-2-1-ns-6

Management networks adopt the following protection measures: dedicated networks are used for management devices by implementing a separate management VLAN or physically separate infrastructure; and secure channels are used, for example, by using VPNs or SSH.

  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)



###  qa-nias-2-1-ns-7

VLANs are used to separate IP telephone traffic in business critical networks.

  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)



###  qa-nias-2-1-ns-8

Administrative access is only permitted from the most highly classified VLAN to one at the same level of classification or of lower classification.

  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)



###  qa-nias-2-1-pr-5

Security evaluation of the product is done on a dedicated evaluation configuration including functionality tests, security tests, and patching to protect against potential threats and vulnerabilities.

  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  qa-nias-2-1-pr-8

Products have been purchased from developers that have made a commitment to the ongoing maintenance of the assurance of their product.

  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)



###  qa-nias-2-1-pr-9

Product patching and updating processes are in place. Updates of products shall follow the change management policies specified in section B-5, Change Management (CM).

  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Require Auto Upgrade Schedule Set for Agent Platform Workbench ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-vertexai-auto-upgrade-schedule-set)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  qa-nias-2-1-ss-13

Workstations use a hardened standard operating environment (SOE) covering the following: removal of unwanted software; disabling of unused or undesired functionality in installed software and operating systems; implementation of access controls on relevant objects to limit system users and programs to the minimum access needed to perform their duties; installation of software-based firewalls limiting inbound and outbound network connections; and configuration of either remote logging or the transfer of local event logs to a central server.

  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)



###  qa-nias-2-1-ss-14

Potential vulnerabilities in their SOEs and systems are reduced by the following: removing unnecessary file shares; ensuring patching is up to date; disabling access to all unnecessary input and output functionality; removing unused accounts; renaming default accounts; and replacing default passwords.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Require Auto Upgrade Schedule Set for Agent Platform Workbench ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-vertexai-auto-upgrade-schedule-set)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  qa-nias-2-1-ss-15

High-risk servers, such as web, email, file, and Internet Protocol telephony servers, having connectivity to uncontrolled public networks meet the following guidelines: maintain effective functional separation between servers allowing them to operate independently; minimise communications between servers at both the network and file system level, as appropriate; and limit system users and programs to the minimum access needed to perform their duties.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn Off Local Infile Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-local-infile-db-flag-mysql)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  qa-nias-2-1-ss-16

Check the integrity of all servers whose functions are critical to the organization, and those identified as being at a high risk of compromise. Wherever possible these checks should be performed from a trusted environment rather than the system itself.

  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)



###  qa-nias-2-1-ss-17

Store the integrity information securely off the server in a manner that maintains integrity.

  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)



###  qa-nias-2-1-ss-19

As part of the organization's ongoing audit schedule, compare the stored integrity information against current integrity information to determine whether a compromise, or a legitimate but incorrectly completed system modification, has occurred.

  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)



###  qa-nias-2-1-ss-2

All applications (including new and developed) are classified using the National Data Classification Policy (IAP-NAT-DCLS) and accorded security protection appropriate to its Confidentiality, Integrity, and Availability ratings.

  * [ Define Set Storage Class Lifestyle Action on Bucket ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-set-storage-class-lifestyle-action-on-bucket)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-service-usage)



###  qa-nias-2-1-ss-20

The organization must resolve any detected changes in accordance with the organization's information and communications technology (ICT) security incident management procedures.

  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)



###  qa-nias-2-1-ss-21

All software applications are reviewed to determine whether they attempt to establish any external connections. If automated outbound connection functionality is included, organizations should make a business decision to determine whether to permit or deny these connections, including an assessment of the risks involved in doing so.

  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)



###  qa-nias-2-1-ss-23

Connectivity and access between each web application component is minimized.

  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)



###  qa-nias-2-1-ss-24

Personal information and sensitive data is protected while in storage and in transmission using appropriate cryptographic controls.

  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)



###  qa-nias-2-1-ss-29

Database files are protected from access that bypasses the database's normal access controls.

  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn Off Local Infile Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-local-infile-db-flag-mysql)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)



###  qa-nias-2-1-ss-3

Security requirements, including functional, technical, and assurance requirements, are developed and implemented as part of system requirements.

  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Enable PodSecurityPolicies for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-pod-security-policy-gke-cluster)



###  qa-nias-2-1-ss-30

Databases provide functionality to allow for auditing of system users' actions.

  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  qa-nias-2-1-ss-31

System users who do not have sufficient privilege to view database contents cannot see associated metadata in a list of results from a search engine query. If results from database queries cannot be appropriately filtered, organizations must ensure that all query results are appropriately sanitized to meet the minimum-security privilege of system users.

  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)



###  qa-nias-2-1-ss-4

Dedicated test and development infrastructure, including systems and data, are available and separate from production systems. Furthermore, information flow between the environments shall be strictly limited according to a defined and documented policy, with access granted only to system users with a clear business requirement and write access to the authoritative source for the software shall be disabled.

  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)



###  qa-nias-2-1-ss-5

All applications, whether acquired or developed, are available for production use only after appropriate quality and security assurance tests and checks to ensure that the system confirms and complies with the intended security requirements.

  * [ Enable PodSecurityPolicies for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-pod-security-policy-gke-cluster)



###  qa-nias-2-1-ss-6

Software developers use secure programming practices when writing code, including the following: complying with best practices, for example, the Mitre top 25 most dangerous programming errors (Mitre); designing software to use the lowest privilege level needed to achieve its task; denying access by default; checking return values of all system calls; and validating all inputs.

  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Restrict API Keys for Required APIs Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-api-keys-for-required-apis-only)



###  qa-nias-2-1-ss-7

Software should be reviewed and/or tested for vulnerabilities before it is used in a production environment. Software should be reviewed and/or tested by an independent party and not by the developer.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  qa-nias-2-1-vl-1

Emergency destruction, locking plan, remote wipe, or auto destruct is in place for any MDs and laptops.

  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)



###  qa-nias-2-1-vl-2

Harden the hypervisor, administrative layer, the virtual machine and related components as per the industry accepted best practices and security guidelines and the vendor recommendations.

  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn Off Local Infile Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-local-infile-db-flag-mysql)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  qa-nias-2-1-vl-3

Enforce least privilege and separation of duties for managing the virtual environment, as follows: define specific roles and granular privileges for each administrator in the central virtualization management software; limit direct administrative access to the hypervisor to the extent possible; and depending on the risk and the classification of the information processed, organizations should consider the use of multi factor authentication or dual or split control of administrative passwords between multiple administrators. For more information, refer to section C9 Access Management.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  qa-nias-2-1-vl-5

Virtualized technology environment should be augmented by third party security technology to provide layered security controls, such as defence in depth approach, to complement the controls provided by the vendor and technology itself.

  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)



###  qa-nias-2-1-vl-6

Segregate virtual machines based on the classification of data they process or store.

  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)



###  qa-nias-2-1-vl-7

A change management process encompasses the virtual technology environment. It includes the following: ensure that virtual machine profile is updated, and the integrity of the virtual machine image is maintained at all times; and care should be taken to maintain and update VMs which are not in an active state (dormant or no longer used). For more information, refer to Section B6- Change Management.

  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Require Auto Upgrade Schedule Set for Agent Platform Workbench ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-vertexai-auto-upgrade-schedule-set)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  qa-nias-2-1-vl-8

Logs from the virtual technology environment shall be logged and monitored along with other IT infrastructure. Refer to Section B10 Logging and Security Monitoring.

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



##  NIST 800-53 Revision 5

**Supported cloud provider:** Google Cloud 

A comprehensive catalog of security and privacy controls for building a robust security program. Mandated for U.S. federal systems, it is now a best-practice framework used by organizations across all sectors.

This framework includes the cloud control groups and cloud controls in the following sections. 

###  nist-r5-ac-02

A. Define and document the types of accounts allowed and specifically prohibited for use within the system. B. Assign account managers. C. Require organization-defined prerequisites and criteria for group and role membership. D. Specify: a. Authorized users of the system. b. Group and role membership. c. Access authorizations or privileges and organization-defined attributes for each account. E. Require approvals by organization-defined personnel or roles for requests to create accounts. F. Create, enable, modify, disable, and remove accounts in accordance with organization-defined policy, procedures, prerequisites, and criteria. G. Monitor the use of accounts. H. Notify account managers and organization-defined personnel or roles within: a. An organization-defined time period when accounts are no longer required. b. An organization-defined time period when users are terminated or transferred. c. An organization-defined time period when system usage or need-to-know changes for an individual. I. Authorize access to the system based on: a. A valid access authorization. b. Intended system usage. c. Organization-defined attributes. J. Review accounts for compliance with account management requirements as per organization-defined frequency. K. Establish and implement a process for changing shared or group account authenticators when individuals are removed from the group. L. Align account management processes with personnel termination and transfer processes.

  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)



###  nist-r5-ac-03

Enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)



###  nist-r5-ac-04

Enforce approved authorizations for controlling the flow of information within the system and between connected systems based on organization-defined information flow control policies.

  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)



###  nist-r5-ac-05

Identify and document organization-defined duties of individuals requiring separation. Define system access authorizations to support separation of duties.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)



###  nist-r5-ac-06

Employ the principle of least privilege, allowing only authorized accesses for users or processes acting on behalf of users that are necessary to accomplish assigned organizational tasks.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  nist-r5-ac-06-05

Restrict privileged accounts on the system to organization-defined personnel or roles.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)



###  nist-r5-ac-07

Enforce a limit of organization-defined number of consecutive invalid logon attempts by a user during an organization-defined time period. When the maximum number of unsuccessful attempts exceed, automatically, lock the account or node for an organization-defined time period; lock the account or node until released by an administrator; delay next logon prompt per organization-defined delay algorithm; notify system administrator; take other organization-defined action.

  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  nist-r5-ac-12

Automatically terminate a user session after organization-defined conditions or trigger events requiring session disconnect.

  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)



###  nist-r5-ac-17

Establish and document usage restrictions, configuration and connection requirements, and implementation guidance for each type of remote access allowed. Authorize each type of remote access to the system prior to allowing such connections.

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)



###  nist-r5-ac-17-03

Route remote accesses through authorized and managed network access control points.

  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)



###  nist-r5-ac-17-04

Authorize the execution of privileged commands and access to security-relevant information using remote access only in a format that provides assessable evidence and for organization-defined needs. Document the rationale for remote access in the security plan for the system.

  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)



###  nist-r5-ac-18

Establish configuration requirements, connection requirements, and implementation guidance for each type of wireless access. Authorize each type of wireless access to the system prior to allowing such connections.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)



###  nist-r5-ac-19

Establish configuration requirements, connection requirements, and implementation guidance for organization-controlled mobile devices, to include when such devices are outside of controlled areas. Authorize the connection of mobile devices to organizational systems.

  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)



###  nist-r5-au-01

Develop, document, and disseminate a compliant audit and accountability policy and the procedures for its implementation, ensuring the policy addresses its purpose, scope, roles, and responsibilities. Designate a specific official to manage this documentation, and regularly review and update the policy and procedures based on a defined schedule or in response to specific events.

  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)



###  nist-r5-au-02

A. Identify the types of events that the system is capable of logging in support of the audit function: B. Coordinate the event logging function with other organizational entities requiring audit-related information to guide and inform the selection criteria for events to be logged. C. Specify the organization-defined event types that are a subset of the event types defined in AU-02a, along with the frequency of; or situation requiring logging for each identified event type. D. Provide a rationale for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations of incidents. E. Review and update the event types selected for logging as per organization-defined frequency.

  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)



###  nist-r5-au-03

Ensure that audit records contain information that establishes the following: A. What type of event occurred. B. When the event occurred. C. Where the event occurred. D. Source of the event. D. Outcome of the event. F. Identity of any individuals, subjects, or objects and entities associated with the event.

  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)



###  nist-r5-au-03-01

Generate audit records containing organization-defined additional information.

  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)



###  nist-r5-au-04

Allocate audit log storage capacity to accommodate organization-defined audit log retention requirements.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)



###  nist-r5-au-05

Alert organization-defined personnel or roles within organization-defined time period in the event of an audit logging process failure. Take organization-defined additional actions.

  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)



###  nist-r5-au-05-02

Provide an alert within organization-defined real-time period to organization-defined personnel, roles, or locations, when organization-defined audit logging failure events requiring real-time alerts occur.

  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)



###  nist-r5-au-06

Review and analyze system audit records as per organization-defined frequency for indications of organization-defined inappropriate or unusual activity and the potential impact of the inappropriate or unusual activity. Report findings to organization-defined personnel or roles. Adjust the level of audit record review, analysis, and reporting within the system when there is a change in risk based on law enforcement information, intelligence information, or other credible sources of information.

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)



###  nist-r5-au-07

Provide and implement an audit record reduction and report generation capability that supports on-demand audit record review, analysis, and reporting requirements and after-the-fact investigations of incidents. The capability must not alter the original content or time ordering of audit records.

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  nist-r5-au-11

Retain audit records for organization-defined time period consistent with records retention policy to provide support for after-the-fact investigations of incidents and to meet regulatory and organizational information retention requirements.

  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)



###  nist-r5-au-12

A. Provide audit record generation capability for the event types the system is capable of auditing as defined in AU-2a on organization-defined system components. B. Allow organization-defined personnel or roles to select the event types that are to be logged by specific components of the system. C. Generate audit records for the event types defined in AU-2c that include the audit record content defined in AU-3.

  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  nist-r5-ca-2-2

Include as part of control assessments, as per organization-defined frequency, announced or unannounced: in-depth monitoring; security instrumentation; automated security test cases; vulnerability scanning; malicious user testing; insider threat assessment; performance and load testing; data leakage or data loss assessment or organization-defined other forms of assessment.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  nist-r5-ca-7

Develop a system-level continuous monitoring strategy and implement continuous monitoring in accordance with the organization-level continuous monitoring strategy that includes: A. Establishing the organization-defined system-level metrics. B. Establishing organization-defined frequencies for monitoring and assessment of control effectiveness. C. Ongoing control assessments in accordance with the continuous monitoring strategy. D. Ongoing monitoring of system and organization-defined metrics in accordance with the continuous monitoring strategy. E. Correlation and analysis of information generated by control assessments and monitoring. F. Response actions to address results of the analysis of control assessment and monitoring information. G. Reporting the security and privacy status of the system to organization-defined personnel or roles as per organization-defined frequency.

  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)



###  nist-r5-ca-9

A. Authorize internal connections of organization-defined system components or classes of components to the system. B. Document, for each internal connection, the interface characteristics, security and privacy requirements, and the nature of the information communicated. C. Terminate internal system connections after organization-defined conditions. D. Review as per organization-defined frequency, the continued need for each internal connection.

  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)



###  nist-r5-cm-01

A. Develop, document, and disseminate to organization-defined personnel or roles: a. A configuration management policy that is defined at an organization-level, mission or business process-level, or at system-level. The policy must address purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance. The policy must be consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. b. Procedures to facilitate the implementation of the configuration management policy and the associated configuration management controls. B. Designate an organization-defined official to manage the development, documentation, and dissemination of the configuration management policy and procedures. C. Review and update the current configuration management policies, and procedures as per organization-defined frequencies and events.

  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)



###  nist-r5-cm-02

A. Develop, document, and maintain under configuration control, a current baseline configuration of the system. B. Review and update the baseline configuration of the system: a. As per organization-defined frequency. b. When required due to organization-defined circumstances. c. When system components are installed or upgraded.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)



###  nist-r5-cm-06

A. Establish and document configuration settings for components employed within the system that reflect the most restrictive mode consistent with operational requirements using organization-defined common secure configurations. B. Implement the configuration settings. C. Identify, document, and approve any deviations from established configuration settings for organization-defined system components based on organization-defined operational requirements. D. Monitor and control changes to the configuration settings in accordance with organizational policies and procedures.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)



###  nist-r5-cm-07

Configure the system to provide only organization-defined mission essential capabilities. Prohibit or restrict the use of organization-defined functions, ports, protocols, software, or services.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  nist-r5-cm-09

Develop, document, and implement a configuration management plan for the system that: A. Addresses roles, responsibilities, and configuration management processes and procedures. B. Establishes a process for identifying configuration items throughout the system development life cycle and for managing the configuration of the configuration items. C. Defines the configuration items for the system and places the configuration items under configuration management. D. Is reviewed and approved by organization-defined personnel or roles. E. Protects the configuration management plan from unauthorized disclosure and modification.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)



###  nist-r5-cp-06

Establish an alternate storage site, including necessary agreements to permit the storage and retrieval of system backup information. Ensure that the alternate storage site provides controls equivalent to that of the primary site.

  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  nist-r5-cp-07

A. Establish an alternate processing site, including necessary agreements to permit the transfer and resumption of organization-defined system operations for essential mission and business functions within organization-defined time period consistent with recovery time and recovery point objectives, when the primary processing capabilities are unavailable. B. Make available at the alternate processing site, the equipment and supplies required to transfer and resume operations or put contracts in place to support delivery to the site within the organization-defined time period for transfer and resumption. C. Provide controls at the alternate processing site that are equivalent to those at the primary site.

  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  nist-r5-ia-04

Manage system identifiers by: A. Receiving authorization from organization-defined personnel or roles to assign an individual, group, role, service, or device identifier. B. Selecting an identifier that identifies an individual, group, role, service, or device. C. Assigning the identifier to the intended individual, group, role, service, or device. D. Preventing reuse of identifiers for organization-defined time period.

  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)



###  nist-r5-ia-05

Manage system authenticators by: a. Verifying, as part of the initial authenticator distribution, the identity of the individual, group, role, service, or device receiving the authenticator. b. Establishing initial authenticator content for any authenticators issued by the organization. c. Ensuring that authenticators have sufficient strength of mechanism for their intended use. d. Establishing and implementing administrative procedures for initial authenticator distribution, for lost or compromised or damaged authenticators, and for revoking authenticators. e. Changing default authenticators prior to first use. f. Changing or refreshing authenticators as per organization-defined time period by authenticator type or when organization-defined events occur. g. Protecting authenticator content from unauthorized disclosure and modification. h. Requiring individuals to take, and having devices implement, specific controls to protect authenticators. i. Changing authenticators for group or role accounts when membership to those accounts changes.

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)



###  nist-r5-ia-08

Uniquely identify and authenticate non-organizational users or processes acting on behalf of non-organizational users.

  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)



###  nist-r5-ma-04

A. Approve and monitor nonlocal maintenance and diagnostic activities. B. Allow the use of nonlocal maintenance and diagnostic tools only as consistent with organizational policy and documented in the security plan for the system. C. Employ strong authentication in the establishment of nonlocal maintenance and diagnostic sessions. D. Maintain records for nonlocal maintenance and diagnostic activities. E. Terminate session and network connections when nonlocal maintenance is completed.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)



###  nist-r5-mp-02

Restrict access to organization-defined types of digital or non-digital media to organization-defined personnel or roles.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)



###  nist-r5-pe-01

A. Develop, document, and disseminate to organization-defined personnel or roles: a. A physical and environmental protection policy that is defined at an organization-level, mission or business process-level, or at system-level. The policy must address purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance. The policy must be consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. b. Procedures to facilitate the implementation of the physical and environmental protection policy and the associated physical and environmental protection controls. B. Designate an organization-defined official to manage the development, documentation, and dissemination of the physical and environmental protection policy and procedures. C. Review and update the current physical and environmental protection policies and procedures as per organization-defined frequencies and events.

  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)



###  nist-r5-pl-08

A. Develop security and privacy architectures for the system: a. Describe the requirements and approach to be taken for protecting the confidentiality, integrity, and availability of organizational information. b. Describe the requirements and approach to be taken for processing personally identifiable information to minimize privacy risk to individuals. c. Describe how the architectures are integrated into and support the enterprise architecture. d. Describe any assumptions about, and dependencies on, external systems and services. B. Review and update the architectures at an organization-defined frequency to reflect changes in the enterprise architecture. C. Reflect planned architecture changes in security and privacy plans, Concept of Operations (CONOPS), criticality analysis, organizational procedures, and procurements and acquisitions.

  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  nist-r5-ra-03

A. Conduct a risk assessment, including: a. Identifying threats to and vulnerabilities in the system. b. Determining the likelihood and magnitude of harm from unauthorized access, use, disclosure, disruption, modification, or destruction of the system, the information it processes, stores, or transmits, and any related information. c. Determining the likelihood and impact of adverse effects on individuals arising from the processing of personally identifiable information. B. Integrate risk assessment results and risk management decisions from the organization and mission or business process perspectives with system-level risk assessments; C. Document risk assessment results in security and privacy plans, risk assessment report, and organization-defined document. D. Review risk assessment results at an organization-defined frequency. E. Disseminate risk assessment results to organization-defined personnel or roles. F Update the risk assessment at an organization-defined frequency or when there are significant changes to the system, its environment of operation, or other conditions that may impact the security or privacy state of the system.

  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)



###  nist-r5-ra-05

A. Monitor and scan for vulnerabilities in the system and hosted applications at organization-defined frequency or randomly in accordance with organization-defined process and when new vulnerabilities potentially affecting the system are identified and reported; B. Employ vulnerability monitoring tools and techniques that facilitate interoperability among tools and automate parts of the vulnerability management process by using standards for: a. Enumerating platforms, software flaws, and improper configurations. b. Formatting checklists and test procedures. c. Measuring vulnerability impact. C. Analyze vulnerability scan reports and results from vulnerability monitoring. D. Remediate legitimate vulnerabilities at organization-defined response times in accordance with an organizational assessment of risk. E. Share information obtained from the vulnerability monitoring process and control assessments with organization-defined personnel or roles to help eliminate similar vulnerabilities in other systems. F. Employ vulnerability monitoring tools that include the capability to readily update the vulnerabilities to be scanned.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  nist-r5-sa-03

Acquire, develop, and manage the system using an organization-defined system development life cycle that incorporates information security and privacy considerations. Define and document information security and privacy roles and responsibilities throughout the system development life cycle. Identify individuals having information security and privacy roles and responsibilities. Integrate the organizational information security and privacy risk management process into system development life cycle activities.

  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)



###  nist-r5-sa-08

Apply organization-defined security and privacy engineering principles in the specification, design, development, implementation, and modification of the system and system components.

  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  nist-r5-sa-10

Require the developer of the system, system component, or system service to: A. Perform configuration management during system, component, or service; design, development, implementation, operation. or disposal. B. Document, manage, and control the integrity of changes to organization-defined configuration items under configuration management. C. Implement only organization-approved changes to the system, component, or service. D. Document approved changes to the system, component, or service and the potential security and privacy impacts of such changes. E. Track security flaws and flaw resolution within the system, component, or service and report findings to organization-defined personnel.

  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)



###  nist-r5-sa-11

Require the developer of the system, system component, or system service, at all post-design stages of the system development life cycle, to: A. Develop and implement a plan for ongoing security and privacy assessments; B. Perform unit, integration, system, regression, testing as per organization-defined frequency and at organization-defined depth and coverage. C. Produce evidence of the execution of the assessment plan and the results of the testing and evaluation. D. Implement a verifiable flaw remediation process. E. Correct flaws identified during testing and evaluation.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  nist-r5-sa-21

Require that the developer of an organization-defined system, system component, or system service has appropriate access authorizations as determined by assigned organization-defined official government duties. The developer must satisfy the additional organization-defined additional personnel screening criteria.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  nist-r5-sc-03

Isolate security functions from nonsecurity functions.

  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)



###  nist-r5-sc-05

Protect against the effects of organization-defined denial-of-service events. Employ organization-defined controls by type of denial-of-service event.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)



###  nist-r5-sc-07

Monitor and control communications at the external managed interfaces to the system and at key internal managed interfaces within the system. Implement subnetworks for publicly accessible system components that are physically and logically separated from internal organizational networks. Connect to external networks or systems only through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  nist-r5-sc-07-05

Deny network communications traffic by default and allow by exception at managed interfaces for organization-defined systems.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)



###  nist-r5-sc-08

Protect the confidentiality and integrity of transmitted information.

  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)



###  nist-r5-sc-10

Terminate the network connection associated with a communications session at the end of the session or after an organization-defined time period of inactivity.

  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)



###  nist-r5-sc-12

Establish and manage cryptographic keys when cryptography is employed within the system in accordance with key management requirements such as organization-defined requirements for key generation, distribution, storage, access, and destruction.

  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  nist-r5-sc-13

Determine the required uses for cryptography and implement the specific types of cryptography needed for each of those defined uses.

  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  nist-r5-sc-23

Protect the authenticity of communications sessions.

  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)



###  nist-r5-sc-28

Protect the confidentiality and integrity of the organization-defined information at rest.

  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)



###  nist-r5-sc-28-01

Implement cryptographic mechanisms to prevent unauthorized disclosure and modification of the organization-defined information at rest on organization-defined system components.

  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)



###  nist-r5-si-01

A. Develop, document, and disseminate to organization-defined personnel or roles: a. A system and information integrity policy that is defined at an organization-level, mission or business process-level, or at system-level. The policy must address purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance. The policy must be consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. b. Procedures to facilitate the implementation of the system and information integrity policy and the associated system and information integrity controls. B. Designate an organization-defined official to manage the development, documentation, and dissemination of the system and information integrity policy and procedures. C. Review and update the current system and information integrity policies and procedures as per organization-defined frequencies and events.

  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)



###  nist-r5-si-02

Identify, report, and correct system flaws. Test software and firmware updates related to flaw remediation for effectiveness and potential side effects before installation. Install security-relevant software and firmware updates within an organization-defined time period of the release of the updates. Incorporate flaw remediation into the organizational configuration management process.

  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)



###  nist-r5-si-02-02

Determine if system components have applicable security-relevant software and firmware updates installed using organization-defined automated mechanisms at an organization-defined frequency.

  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)



###  nist-r5-si-03

A. Implement signature or non-signature based malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code. B. Automatically update malicious code protection mechanisms as new releases are available in accordance with organizational configuration management policy and procedures. C. Configure malicious code protection mechanisms to: a. Perform periodic scans of the system at organization-defined frequency and real-time scans of files from external sources at endpoint; network entry and exit points as the files are downloaded, opened, or executed in accordance with organizational policy. b. Block malicious code; quarantine malicious code; take organization-defined action, and send alerts to organization-defined personnel or roles in response to malicious code detection. D. Address the receipt of false positives during malicious code detection and eradication and the resulting potential impact on the availability of the system.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)



###  nist-r5-si-04

A. Monitor the system to detect: a. Attacks and indicators of potential attacks in accordance with organization-defined monitoring objectives. b. Unauthorized local, network, and remote connections. B. Identify unauthorized use of the system through organization-defined techniques and methods. C. Invoke internal monitoring capabilities or deploy monitoring devices: a. Strategically within the system to collect organization-determined essential information. b. At ad hoc locations within the system to track specific types of transactions of interest to the organization. D. Analyze detected events and anomalies. E. Adjust the level of system monitoring activity when there is a change in risk to organizational operations and assets, individuals, other organizations, or the Nation. F. Obtain legal opinion regarding system monitoring activities. G. Provide organization-defined system monitoring information to organization-defined personnel or roles as needed or as per organization-defined frequency.

  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  nist-r5-si-04-02

Employ automated tools and mechanisms to support near real-time analysis of events.

  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)



###  nist-r5-si-04-04

Determine criteria for unusual or unauthorized activities or conditions for inbound and outbound communications traffic. Monitor inbound and outbound communications traffic at an organization-defined frequency for organization-defined unusual or unauthorized activities or conditions.

  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)



###  nist-r5-si-07

a. Employ integrity verification tools to detect unauthorized changes to organization-defined software, firmware, and information. b. Take organization-defined actions when unauthorized changes to the software, firmware, and information are detected.

  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)



###  nist-r5-si-07-01

Perform an integrity check of organization-defined software, firmware, and information, at startup and organization-defined transitional states or security-relevant events, at an organization-defined frequency.

  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)



###  nist-r5-si-07-02

Employ automated tools that provide notification to organization-defined personnel or roles upon discovering discrepancies during integrity verification.

  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)



###  nist-r5-si-12

Manage and retain information within the system and information output from the system in accordance with applicable laws, executive orders, directives, regulations, policies, standards, guidelines and operational requirements.

  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)



##  NIST AI 600-1 Privacy Controls

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

NIST AI 600-1 based privacy controls for GenAI adoption

This framework includes the cloud control groups and cloud controls in the following sections. 

###  nist-600-1-gv-6.1-001

Categorize different types of generative AI (GAI) content with associated third-party rights. For example, category copyrights, intellectual properties, and data privacy.

  * [ Configure Model Armor with Sensitive Data Filters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-model-armor-with-sensitive-data-filters)
  * [ Label Dataset Sensitivity Based on Sensitive Data Protection Findings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-data-catalog-to-label-dataset-sensitivity-based-on-sdp-findings)



###  nist-600-1-mg-2.2-002

Document training data sources to trace the origin and provenance of AI-generated content.

  * [ Enable Data Lineage API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-lineage-on-google-cloud)



###  nist-600-1-mg-2.2-007

Use real-time auditing tools where they can be demonstrated to aid in the tracking and validation of the lineage and authenticity of AI-generated data.

  * [ Enable Data Lineage API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-lineage-on-google-cloud)



###  nist-600-1-mg-2.2-009

Consider opportunities to responsibly use synthetic data and other privacy enhancing techniques in GAI development, where appropriate and applicable, match the statistical properties of real-world data without disclosing personally identifiable information or contributing to homogenization.

  * [ Enable Provenance Tracking of Agent Platform Synthetic Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-provenance-tracking-of-synthetic-datasets)
  * [ Enable SDP for Data Discovery ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-sdp-data-discovery)



###  nist-600-1-mg-3.2-003

Document sources and types of training data and their origins, potential biases present in the data related to the GAI application and its content provenance, architecture, training process of the pre-trained model including information on hyperparameters, training duration, and any fine-tuning processes applied.

  * [ Enable Data Lineage API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-lineage-on-google-cloud)



###  nist-600-1-mp-2.1-002

Institute test and evaluation for data and content flows within the GAI system, including but not limited to, original data sources, data transformations, and decision-making criteria.

  * [ Enable Data Lineage API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-lineage-on-google-cloud)
  * [ Enable SDP for Data Discovery ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-sdp-data-discovery)



###  nist-600-1-mp-4.1-001

Conduct periodic monitoring of AI-generated content for privacy risks; address any possible instances of PII or sensitive data exposure.

  * [ Configure Model Armor with Sensitive Data Filters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-model-armor-with-sensitive-data-filters)
  * [ Enable SDP for Data Discovery ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-sdp-data-discovery)



###  nist-600-1-mp-4.1-004

Document training data curation policies, to the extent possible and according to applicable laws and policies.

  * [ Enable Data Lineage API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-lineage-on-google-cloud)



###  nist-600-1-mp-4.1-005

Establish policies for collection, retention, and minimum quality of data, in consideration of the following risks: Disclosure of inappropriate CBRN information; Use of Illegal or dangerous content; Offensive cyber capabilities; Training data imbalances that could give rise to harmful biases; Leak of personally identifiable information, including facial likenesses of individuals.

  * [ Enable Data Lineage API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-lineage-on-google-cloud)



###  nist-600-1-mp-4.1-009

Leverage approaches to detect the presence of PII or sensitive data in generated output text, image, video, or audio.

  * [ Configure Model Armor with Sensitive Data Filters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-model-armor-with-sensitive-data-filters)
  * [ Enable SDP for Data Discovery ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-sdp-data-discovery)



###  nist-600-1-mp-4.1-010

Conduct appropriate diligence on training data use to assess intellectual property, and privacy, risks, including to examine whether use of proprietary or sensitive training data is consistent with applicable laws.

  * [ Enable Data Lineage API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-lineage-on-google-cloud)
  * [ Label Dataset Sensitivity Based on Sensitive Data Protection Findings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-data-catalog-to-label-dataset-sensitivity-based-on-sdp-findings)



###  nist-600-1-ms-1.1-002

Integrate tools designed to analyze content provenance and detect data anomalies, verify the authenticity of digital signatures, and identify patterns associated with misinformation or manipulation.

  * [ Enable Sensitive Data Protection to Detect PII in Agent Platform Training Data ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-sdp-to-detect-pii-in-training-data)



###  nist-600-1-ms-2.2-004

Use techniques such as anonymization, differential privacy or other privacy enhancing technologies to help minimize the risks associated with linking AI-generated content back to individual human subjects.

  * [ Enable SDP for Data Discovery ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-sdp-data-discovery)
  * [ Enable Sensitive Data Protection to Detect PII in Agent Platform Training Data ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-sdp-to-detect-pii-in-training-data)



###  nist-600-1-ms-2.5-005

Verify that the Generative Artificial Intelligence (GAI) system training data and test, evaluation, verification, and validation (TEVV) data provenance, and fine-tuning or retrieval-augmented generation data is grounded.

  * [ Enable Data Lineage API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-lineage-on-google-cloud)



###  nist-600-1-ms-2.6-002

Assess existence or levels of harmful bias, intellectual property infringement, data privacy violations, obscenity, extremism, violence, or CBRN information in system training data.

  * [ Configure Model Armor with Sensitive Data Filters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-model-armor-with-sensitive-data-filters)
  * [ Enable SDP for Data Discovery ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-sdp-data-discovery)



###  nist-600-1-ms-2.9-002

Document GAI model details including: proposed use and organizational value; assumptions and limitations, data collection methodologies; data provenance; data quality; model architecture (for example, convolutional neural network and transformers); optimization objectives; training algorithms; RLHF approaches; fine-tuning or retrieval-augmented generation approaches; evaluation data; ethical considerations; legal and regulatory requirements.

  * [ Enable Data Lineage API ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-data-lineage-on-google-cloud)



##  NIST Cybersecurity Framework 1.1

**Supported cloud provider:** Google Cloud 

A strategic framework to help organizations manage cybersecurity risk. It organizes activities into five core functions: Identify, Protect, Detect, Respond, and Recover, providing a high-level view of your security posture.

This framework includes the cloud control groups and cloud controls in the following sections. 

###  nist-csf-de-ae

Anomalies and Events (DE.AE): Anomalous activity is detected and the potential impact of events is understood.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  nist-csf-de-ae-1

A baseline of network operations and expected data flows for users and systems is established and managed.

  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)



###  nist-csf-de-ae-2

Detected events are analyzed to understand attack targets and methods.

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  nist-csf-de-ae-3

Event data are collected and correlated from multiple sources and sensors.

  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)



###  nist-csf-de-ae-4

Impact of events is determined.

  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  nist-csf-de-ae-5

Incident alert thresholds are established.

  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  nist-csf-de-cm

Security Continuous Monitoring (DE.CM): The information system and assets are monitored to identify cybersecurity events and verify the effectiveness of protective measures.

  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  nist-csf-de-cm-1

The network is monitored to detect potential cybersecurity events.

  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)



###  nist-csf-de-cm-2

The physical environment is monitored to detect potential cybersecurity events.

  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  nist-csf-de-cm-3

Personnel activity is monitored to detect potential cybersecurity events.

  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)



###  nist-csf-de-cm-4

Malicious code is detected.

  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  nist-csf-de-cm-5

Unauthorized mobile code is detected.

  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  nist-csf-de-cm-6

External service provider activity is monitored to detect potential cybersecurity events.

  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  nist-csf-de-cm-7

Monitoring for unauthorized personnel, connections, devices, and software is performed.

  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  nist-csf-de-cm-8

Vulnerability scans are performed.

  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)



###  nist-csf-de-dp-1

Roles and responsibilities for detection are well defined to ensure accountability.

  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  nist-csf-de-dp-4

Event detection information is communicated.

  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  nist-csf-id-am

Asset Management: The data, personnel, devices, systems, and facilities that enable the organization to achieve business purposes are identified and managed consistent with their relative importance to organizational objectives and the organization's risk strategy.

  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  nist-csf-id-am-1

Physical devices and systems within the organization are inventoried.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)



###  nist-csf-id-am-4

External information systems are catalogued.

  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)



###  nist-csf-id-am-6

Cybersecurity roles and responsibilities for the entire workforce and third-party stakeholders (for example, suppliers, customers, partners) are established.

  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)



###  nist-csf-id-gv-1

Organizational cybersecurity policy is established and communicated.

  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)



###  nist-csf-id-gv-3

Legal and regulatory requirements regarding cybersecurity, including privacy and civil liberties obligations, are understood and managed.

  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)



###  nist-csf-id-gv-4

Governance and risk management processes address cybersecurity risks.

  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)



###  nist-csf-id-ra-1

Asset vulnerabilities are identified and documented.

  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  nist-csf-id-ra-2

Cyber threat intelligence is received from information sharing forums and sources.

  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)



###  nist-csf-id-ra-3

Threats, both internal and external, are identified and documented.

  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  nist-csf-id-sc-3

Contracts with suppliers and third-party partners are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and Cyber Supply Chain Risk Management Plan.

  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)



###  nist-csf-pr-ac

Identity Management, Authentication and Access Control (PR.AC): Access to physical and logical assets and associated facilities is limited to authorized users, processes, and devices, and is managed consistent with the assessed risk of unauthorized access to authorized activities and transactions.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  nist-csf-pr-ac-1

Identities and credentials are issued, managed, verified, revoked, and audited for authorized devices, users and processes.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)



###  nist-csf-pr-ac-2

Physical access to assets is managed and protected.

  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)



###  nist-csf-pr-ac-3

Remote access is managed.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  nist-csf-pr-ac-4

Access permissions and authorizations are managed, incorporating the principles of least privilege and separation of duties.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure Remote Access Inactivity Timeout ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-remote-access-inactivity-timeout)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Define Secret Manager Rotation Schedule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-secret-manager-rotation-schedule)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-service-usage)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  nist-csf-pr-ac-5

Network integrity is protected (for example, network segregation, network segmentation).

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  nist-csf-pr-ac-6

Identities are proofed and bound to credentials and asserted in interactions.

  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)



###  nist-csf-pr-ac-7

Users, devices, and other assets are authenticated (for example, single-factor, multi-factor) commensurate with the risk of the transaction (for example, individuals' security and privacy risks and other organizational risks).

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)



###  nist-csf-pr-ds-1

Data-at-rest is protected.

  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)



###  nist-csf-pr-ds-2

Data-in-transit is protected.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  nist-csf-pr-ds-3

Assets are formally managed throughout removal, transfers, and disposition.

  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)



###  nist-csf-pr-ds-4

Adequate capacity to ensure availability is maintained.

  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)



###  nist-csf-pr-ds-5

Protections against data leaks are implemented.

  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)



###  nist-csf-pr-ip

Information Protection Processes and Procedures (PR.IP): Security policies (that address purpose, scope, roles, responsibilities, management commitment, and coordination among organizational entities), processes, and procedures are maintained and used to manage protection of information systems and assets.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)



###  nist-csf-pr-ip-1

A baseline configuration of information technology or industrial control systems is created and maintained incorporating security principles (e.g. concept of least functionality).

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn Off Local Infile Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-local-infile-db-flag-mysql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  nist-csf-pr-ip-10

Response and recovery plans are tested.

  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)



###  nist-csf-pr-ip-12

A vulnerability management plan is developed and implemented.

  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  nist-csf-pr-ip-2

A System Development Life Cycle to manage systems is implemented.

  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Restrict API Keys for Required APIs Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-api-keys-for-required-apis-only)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)



###  nist-csf-pr-ip-3

Configuration change control processes are in place.

  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)



###  nist-csf-pr-ip-4

Backups of information are conducted, maintained, and tested.

  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)



###  nist-csf-pr-ip-6

Data is destroyed according to policy.

  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)



###  nist-csf-pr-ip-9

Response plans (Incident Response and Business Continuity) and recovery plans (Incident Recovery and Disaster Recovery) are in place and managed.

  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)



###  nist-csf-pr-ma-1

Maintenance and repair of organizational assets are performed and logged, with approved and controlled tools.

  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)
  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)



###  nist-csf-pr-pt

Protective Technology (PR.PT): Technical security solutions are managed to ensure the security and resilience of systems and assets, consistent with related policies, procedures, and agreements.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Service Account Key Uploads ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-upload)
  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  nist-csf-pr-pt-1

Audit and log records are determined, documented, implemented, and reviewed in accordance with policy.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Define Secret Manager Rotation Schedule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-secret-manager-rotation-schedule)
  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)



###  nist-csf-pr-pt-3

The principle of least functionality is incorporated by configuring systems to provide only essential capabilities.

  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)



###  nist-csf-pr-pt-4

Communications and control networks are protected.

  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)



###  nist-csf-pr-pt-5

Mechanisms (for example, failsafe, load balancing, hot swap) are implemented to achieve resilience requirements in normal and adverse situations.

  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)



###  nist-csf-rc-im

Improvements (RC.IM): Recovery planning and processes are improved by incorporating lessons learned into future activities.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)



###  nist-csf-rc-rp-1

Recovery plan is executed during or after a cybersecurity incident.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)



###  nist-csf-rs-an

Analysis (RS.AN): Analysis is conducted to ensure effective response and support recovery activities.

  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  nist-csf-rs-an-1

Notifications from detection systems are investigated.

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)



###  nist-csf-rs-an-5

Processes are established to receive, analyze and respond to vulnerabilities disclosed to the organization from internal and external sources (for example internal testing, security bulletins, or security researchers).

  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  nist-csf-rs-co-1

Personnel know their roles and order of operations when a response is needed.

  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)



###  nist-csf-rs-co-4

Coordination with stakeholders occurs consistent with response plans.

  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)



###  nist-csf-rs-im-2

Response strategies are updated.

  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)



###  nist-csf-rs-mi-2

Incidents are mitigated.

  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)



###  nist-csf-rs-rp-1

Response plan is executed during or after an incident.

  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)



##  PCI DSS v4.0.1

**Supported cloud provider:** Google Cloud 

A regulatory framework that defines the mandatory PCI Data Security Standard (DSS) for businesses that process, store, or transmit cardholder data. PCI DSS defines specific technical and operational requirements to help protect cardholder data wherever it is processed, stored, or transmitted. PCI DSS provides a set of prescriptive technical and operational requirements to help prevent fraud. The framework aligns with PCI DSS v4.0.1.

This framework includes the cloud control groups and cloud controls in the following sections. 

###  pci-dss-v4-1-2-1

Configuration standards for NSC rule sets must be defined, implemented, and maintained.

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-network-traffic-monitoring)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  pci-dss-v4-1-2-6

Security features must be defined and implemented for all services, protocols, and ports that are in use and considered to be insecure, such that the risk is mitigated.

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  pci-dss-v4-1-3-1

Inbound traffic to the CDE must be restricted to only traffic that is necessary and all other traffic must be specifically denied.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)



###  pci-dss-v4-1-3-2

Outbound traffic from the CDE must be restricted to only traffic that is necessary and all other traffic must be specifically denied.

  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)



###  pci-dss-v4-1-4-1

NSCs are implemented between trusted and untrusted networks.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)



###  pci-dss-v4-1-4-2

Inbound traffic from untrusted networks to trusted networks must be restricted to the following: communications with system components that are authorized to provide publicly accessible services, protocols, and ports; stateful responses to communications initiated by system components in a trusted network; and all other traffic must be denied.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  pci-dss-v4-1-4-3

Anti-spoofing measures must be implemented to detect and block forged source IP addresses from entering the trusted network.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)



###  pci-dss-v4-1-4-4

System components that store cardholder data must not be directly accessible from untrusted networks.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)



###  pci-dss-v4-10-1-1

All security policies and operational procedures that are identified in Requirement 10 are documented, kept up to date, in use, and known to all affected parties.

  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)



###  pci-dss-v4-10-2-1

Audit logs are enabled and active for all system components and cardholder data.

  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  pci-dss-v4-10-2-1-1

Audit logs capture all individual user access to cardholder data.

  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  pci-dss-v4-10-2-1-2

Audit logs capture all actions taken by any individual with administrative access, including any interactive use of application or system accounts.

  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)



###  pci-dss-v4-10-2-1-4

Audit logs capture all invalid logical access attempts.

  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)



###  pci-dss-v4-10-3-3

Audit log files, including those for external-facing technologies, are promptly backed up to a secure, central, internal log servers, or other media that is difficult to modify.

  * [ Configure Log Sinks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-log-sinks)



###  pci-dss-v4-10-4-1-1

Automated mechanisms are used to perform audit log reviews.

  * [ Configure Log Metrics and Alerts for Cloud SQL Configuration Changes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-log-metrics-for-sql-config-changes)



###  pci-dss-v4-10-5-1

Retain audit log history for at least 12 months, with at least the most recent three months immediately available for analysis.

  * [ Configure Log Sinks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-log-sinks)
  * [ Retain Audit Records ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#retain-audit-records)



###  pci-dss-v4-11-5-1

Intrusion-detection and intrusion-prevention techniques are used to detect and/or prevent intrusions into the network as follows: all traffic is monitored at the perimeter of the CDE; all traffic is monitored at critical points in the CDE; personnel are alerted to suspected compromises; all intrusion-detection and prevention engines, baselines, and signatures are kept up to date.

  * [ Configure Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-network-traffic-monitoring)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)



###  pci-dss-v4-12-10-5

The security incident response plan includes monitoring and responding to alerts from security monitoring systems, including but not limited to: intrusion-detection and intrusion-prevention systems; network security controls; change-detection mechanisms for critical files; the change-and tamper-detection mechanism for payment pages; detection of unauthorized wireless access points.

  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  pci-dss-v4-12-5-1

An inventory of system components that are in scope for PCI DSS, including a description of function and use, is maintained and kept current.

  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)



###  pci-dss-v4-2-2-1

Configuration standards must be developed, implemented, and maintained to ensure that they cover all system components, address all known security vulnerabilities, are consistent with industry-accepted system hardening standards or vendor hardening recommendations, are updated as new vulnerability issues are identified, as defined in Requirement 6.3.1, and are applied when new systems are configured and verified as in place before or immediately after a system component is connected to a production environment.

  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable PodSecurityPolicies for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-pod-security-policy-gke-cluster)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)



###  pci-dss-v4-2-2-3

Primary functions requiring different security levels must be managed to ensure the following: only one primary function exists on a system component, or primary functions with different security levels that exist on the same system component are isolated from each other, or primary functions with different security levels on the same system component are all secured to the level required by the function with the highest security need.

  * [ Enable IP Alias Range for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-ip-alias-range)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)



###  pci-dss-v4-2-2-4

Only necessary services, protocols, daemons, and functions must be enabled, and all unnecessary functionality must be removed or disabled.

  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Disable Alpha Features on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-alpha-features)
  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-service-usage)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn Off Local Infile Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-local-infile-db-flag-mysql)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)



###  pci-dss-v4-2-2-5

If any insecure services, protocols, or daemons are present, ensure that the business justification is documented and additional security features are documented and implemented that reduce the risk of using insecure services, protocols, or daemons.

  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)



###  pci-dss-v4-2-2-6

System security parameters must be configured to prevent misuse.

  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn Off Local Infile Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-local-infile-db-flag-mysql)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)



###  pci-dss-v4-2-2-7

All non-console administrative access must be encrypted using strong cryptography.

  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  pci-dss-v4-3-2-1

Account data storage must be kept to a minimum through implementation of data retention and disposal policies, procedures, and processes that must include at least the following: coverage for all locations of stored account data; coverage for any sensitive authentication data (SAD) stored prior to completion of authorization; limiting data storage amount and retention time to that which is required for legal or regulatory, and business requirements; specific retention requirements for stored account data that defines length of retention period and includes a documented business justification; processes for secure deletion or rendering account data unrecoverable when no longer needed per the retention policy; and a process for verifying, at least once every three months, that stored account data exceeding the defined retention period has been securely deleted or rendered unrecoverable.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Define Set Storage Class Lifestyle Action on Bucket ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-set-storage-class-lifestyle-action-on-bucket)
  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)



###  pci-dss-v4-3-3-2

SAD that is stored electronically prior to completion of authorization must be encrypted using strong cryptography.

  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)



###  pci-dss-v4-3-3-3

Issuers and companies that support issuing services and store sensitive authentication data must ensure that any storage of sensitive authentication data is limited to that which is needed for a legitimate issuing business need and is secured and encrypted using strong cryptography.

  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)



###  pci-dss-v4-3-5-1

PAN is rendered unreadable anywhere it is stored by using any of the following approaches: one-way hashes based on strong cryptography of the entire PAN; truncation (hashing cannot be used to replace the truncated segment of PAN); if hashed and truncated versions of the same PAN, or different truncation formats of the same PAN, are present in an environment, additional controls are in place such that the different versions cannot be correlated to reconstruct the original PAN; index tokens; and strong cryptography with associated key-management processes and procedures.

  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)



###  pci-dss-v4-3-5-1-3

If disk-level or partition-level encryption is used (rather than file-, column-, or field-level database encryption) to render PAN unreadable, ensure the following: logical access is managed separately and independently of native operating system authentication and access control mechanisms; decryption keys are not associated with user accounts; and authentication factors (such as, passwords, passphrases, or cryptographic keys) that allow access to unencrypted data are stored securely.

  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)



###  pci-dss-v4-3-6-1

Procedures must be defined and implemented to protect cryptographic keys used to protect stored account data against disclosure and misuse that include access to keys is restricted to the fewest number of custodians necessary.

  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)



###  pci-dss-v4-3-6-1-2

Secret and private keys used to protect stored account data must be stored in one (or more) of the following forms at all times: encrypted with a key-encrypting key that is at least as strong as the data-encrypting key, and that is stored separately from the data-encrypting key; within a secure cryptographic device (SCD) (for example, a hardware security module (HSM) or PTS-approved point-of-interaction device); and as at least two full-length key components or key shares, in accordance with an industry-accepted method.

  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)



###  pci-dss-v4-3-7-1

Key-management policies and procedures must be implemented to include generation of strong cryptographic keys used to protect stored account data.

  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  pci-dss-v4-3-7-2

Key-management policies and procedures must be implemented to include secure distribution of cryptographic keys used to protect stored account data.

  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)



###  pci-dss-v4-3-7-3

Key-management policies and procedures must be implemented to include secure storage of cryptographic keys used to protect stored account data.

  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)



###  pci-dss-v4-3-7-5

Key management policies and procedures must be implemented to include the retirement, replacement, or destruction of keys used to protect stored account data, as deemed necessary when: the key has reached the end of its defined cryptoperiod; the integrity of the key has been weakened (including when personnel with knowledge of a cleartext key component leaves the company, or the role for which the key component was known); the key is suspected of or known to be compromised; and retired or replaced keys are not used for encryption operations.

  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)



###  pci-dss-v4-4-2-1

Strong cryptography and security protocols must be implemented to safeguard PAN during transmission over open, public networks to ensure the following: only trusted keys and certificates are accepted; certificates used to safeguard PAN during transmission over open, public networks are confirmed as valid and are not expired or revoked; the protocol in use supports only secure versions or configurations and does not support fallback to, or use of insecure versions, algorithms, key sizes, or implementations; and the encryption strength is appropriate for the encryption methodology in use.

  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  pci-dss-v4-5-2-1

An anti-malware solution(s) must be deployed on all system components, except for those system components identified in periodic evaluations per Requirement 5.2.3 that concludes the system components are not at risk from malware.

  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)



###  pci-dss-v4-5-2-2

The deployed anti-malware solution(s) must detect all known types of malware and remove, block, or contain all known types of malware.

  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)



###  pci-dss-v4-6-3-1

Security vulnerabilities must be identified and managed to ensure the following: new security vulnerabilities are identified using industry-recognized sources for security vulnerability information, including alerts from international and national computer emergency response teams (CERTs); vulnerabilities are assigned a risk ranking based on industry best practices and consideration of potential impact; risk rankings identify, at a minimum, all vulnerabilities considered to be a high-risk or critical to the environment; and vulnerabilities for bespoke and custom, and third-party software (for example, operating systems and databases) are covered.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  pci-dss-v4-6-3-3

All system components must be protected from known vulnerabilities by installing applicable security patches or updates to ensure the following: patches or updates for critical vulnerabilities (identified according to the risk ranking process at Requirement 6.3.1) are installed within one month of release; and all other applicable security patches or updates are installed within an appropriate time frame as determined by the entity’s assessment of the criticality of the risk to the environment as identified according to the risk ranking process at Requirement 6.3.1.

  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Require Auto Upgrade Schedule Set for Agent Platform Workbench ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-vertexai-auto-upgrade-schedule-set)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)



###  pci-dss-v4-6-4-1

For public-facing web applications, new threats and vulnerabilities must be addressed on an ongoing basis and these applications must be protected against known attacks using either of the following two methods: **Reviewing public-facing web applications using manual or automated application vulnerability security assessment tools or methods** as follows: at least once every 12 months and after significant changes; by an entity that specializes in application security; including, at a minimum, all common software attacks in Requirement 6.2.4; all vulnerabilities are ranked in accordance with Requirement 6.3.1; all vulnerabilities are corrected; and the application is re-evaluated after the corrections. Or, **Installing an automated technical solution(s) that continually detects and prevents web-based attacks** as follows: installed in front of public-facing web applications to detect and prevent web- based attacks; actively running and up-to-date as applicable; generating audit logs; and configured to either block web-based attacks or generate an alert that is immediately investigated.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)



###  pci-dss-v4-6-4-2

For public-facing web applications, an automated technical solution must be deployed that continually detects and prevents web-based attacks, with these minimum checks: installed in front of public-facing web applications and is configured to detect and prevent web-based attacks; actively running and up-to-date as applicable; generating audit logs; and configured to either block web-based attacks or generate an alert that is immediately investigated.

  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)



###  pci-dss-v4-7-2-1

An access control model must be defined and include granting access as follows: appropriate access depending on the entity’s business and access needs; access to system components and data resources that is based on users’ job classification and functions; and the least privileges required (for example, user, administrator) to perform a job function.

  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)



###  pci-dss-v4-7-2-2

Access must be assigned to users (including privileged users) based on the job classification and function, and least privileges necessary to perform job responsibilities.

  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)



###  pci-dss-v4-7-2-5

All application and system accounts and related access privileges must be assigned and managed based on the least privileges necessary for the operability of the system or application and ensure that access is limited to the systems, applications, or processes that specifically require their use.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Restrict API Keys for Required APIs Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-api-keys-for-required-apis-only)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  pci-dss-v4-7-3-1

An access control system(s) must be in place that restricts access based on a user’s need to know and covers all system components.

  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)



###  pci-dss-v4-7-3-2

The access control system(s) must be configured to enforce permissions assigned to individuals, applications, and systems based on job classification and function.

  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)



###  pci-dss-v4-7-3-3

The access control system(s) must be set to deny all by default.

  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-service-usage)



###  pci-dss-v4-8-2-1

All users must be assigned a unique ID before access to system components or cardholder data is allowed.

  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)



###  pci-dss-v4-8-2-3

Service providers with remote access to customer premises must use unique authentication factors for each customer premises.

  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)



###  pci-dss-v4-8-2-5

Access for terminated users must be immediately revoked.

  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)



###  pci-dss-v4-8-2-8

If a user session has been idle for more than 15 minutes, the user must re-authenticate to reactivate the terminal or session.

  * [ Configure Remote Access Inactivity Timeout ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-remote-access-inactivity-timeout)
  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)



###  pci-dss-v4-8-3-2

Strong cryptography must be used to render all authentication factors unreadable during transmission and storage on all system components.

  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  pci-dss-v4-8-3-9

If passwords or passphrases are used as the only authentication factor for user access (in any single-factor authentication implementation) then they must be changed at least once every 90 days, or the security posture of accounts must be dynamically analyzed, and real-time access to resources must be automatically determined accordingly.

  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)



###  pci-dss-v4-8-6-2

Passwords or passphrases for any application and system accounts that can be used for interactive login must not be hard coded in scripts, configuration or property files, or bespoke and custom source code.

  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)



###  pci-dss-v4-8-6-3

Passwords or passphrases for any application and system accounts must be protected against misuse by ensuring the following: passwords or passphrases are changed periodically (at the frequency defined in the entity’s targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1) and upon suspicion or confirmation of compromise; and passwords or passphrases are constructed with sufficient complexity appropriate for how frequently the entity changes the passwords or passphrases.

  * [ Define Secret Manager Rotation Schedule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-secret-manager-rotation-schedule)
  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)



##  Security Essentials

**Supported cloud provider:** Google Cloud 

Google Cloud Security Essentials provides a foundational security and compliance baseline for Google Cloud customers.The framework is built on Google's extensive threat intelligence and best practices,giving you visibility into your security posture and helping you meet common compliance requirements right from the start.

This framework includes the following cloud controls: 

  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Public IP Address for Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#detective-policy-for-vertex-ai-workbench-that-restricts-public-ip)
  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-logging-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Enable PodSecurityPolicies for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-pod-security-policy-gke-cluster)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



##  SOC2 2017

**Supported cloud provider:** Google Cloud 

A regulatory framework that an independent auditor can use to evaluate and report on your organization's controls that are relevant to the AICPA's Trust Services Criteria, such as Security and Availability. The resulting audit report provides you with an evaluation of your organization's systems and the data that they handle.The framework aligns with SOC 2 2017 (With Revised Points of Focus - 2022).

This framework includes the cloud control groups and cloud controls in the following sections. 

###  soc2-2017-a-1-2-11

Management identifies threats to data recoverability (such as, ransomware attacks) that could impair the availability of the system and related data and implements mitigation procedures.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ Require Object Versioning for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-object-versioning)



###  soc2-2017-a-1-2-8

Procedures are in place for backing up data, monitoring to detect backup failures, and initiating corrective action when such failures occur.

  * [ Enable AlloyDB Automated Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-alloydb-automated-backups)
  * [ Enable AlloyDB Backups on Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-continuous-automated-backups)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)



###  soc2-2017-c-1-1-2

Confidential information is retained for no longer than necessary to fulfill the identified purpose, unless a law or regulation specifically requires otherwise.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)



###  soc2-2017-c-1-1-3

Policies and procedures are in place to protect confidential information from erasure or destruction during the specified retention period of the information.

  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)



###  soc2-2017-c-1-2-2

Policies and procedures are in place to automatically or manually erase or otherwise destroy confidential information that has been identified for destruction.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)



###  soc2-2017-cc-1-3-3

Management and the board of directors delegate authority, define responsibilities, and use appropriate processes and technology to assign responsibility and segregate duties as necessary at the various levels of the organization.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)



###  soc2-2017-cc-2-1-2

Information systems capture internal and external sources of data.

  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  soc2-2017-cc-2-1-6

The entity identifies, documents, and maintains records of system components such as infrastructure, software, and other information assets. Information assets include physical endpoint devices and systems, virtual systems, data and data flows, external information systems, and organizational roles.

  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)



###  soc2-2017-cc-2-2-1

A process is in place to communicate required information to enable all personnel to understand and carry out their internal control responsibilities.

  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)



###  soc2-2017-cc-3-2-5

Risk assessment includes considering how the risk should be managed and whether to accept, avoid, reduce, or share the risk.

  * [ Configure the Disable VPC Internal IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-internal-ipv6-addresses-org-policy)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)



###  soc2-2017-cc-3-2-7

The entity identifies the vulnerabilities of system components, including system processes, infrastructure, software,

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  soc2-2017-cc-4-1-1

Management includes a balance of ongoing and separate evaluations.

  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)



###  soc2-2017-cc-4-1-5

Ongoing evaluations are built into the business processes and adjust to changing conditions.

  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)



###  soc2-2017-cc-4-1-8

Management uses a variety of ongoing and separate risk and control evaluations to determine whether internal controls are present and functioning. Depending on the entity’s objectives, such risk and control evaluations may include first- and second-line monitoring and control testing, internal audit assessments, compliance assessments, resilience assessments, vulnerability scans, security assessment, penetration testing, and third-party assessments.

  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)



###  soc2-2017-cc-5-2-2

Management selects and develops control activities over the technology infrastructure, which are designed and implemented to help ensure the completeness, accuracy, and availability of technology processing.

  * [ Enable Auto Repair for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-repair)
  * [ Enable Automatic Backups for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-automatic-backups-cloud-sql)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)



###  soc2-2017-cc-5-2-3

Management selects and develops control activities that are designed and implemented to restrict technology access rights to authorized users commensurate with their job responsibilities and to protect the entity’s assets from external threats.

  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)



###  soc2-2017-cc-5-3-1

Management establishes control activities that are built into business processes and employees’ day-to-day activities through policies establishing what is expected and relevant procedures specifying actions.

  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)



###  soc2-2017-cc-6-1-10

The entity uses encryption to protect data at rest, during processing, or in transmission, when such protections are deemed appropriate based on the entity’s risk mitigation strategy.

  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Encrypt Data at Rest with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-data-at-rest-cmek)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Enforce CMEK for Supported Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-supported-services)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Non CMEK Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-non-cmek-services)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  soc2-2017-cc-6-1-11

The entity protects cryptographic keys during generation, storage, use, and destruction. Cryptographic modules, algorithms, key lengths, and architectures are appropriate based on the entity’s risk mitigation strategy.

  * [ Avoid RSASHA1 for DNSSEC Signing ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#avoid-rsasha1-cloud-dns)
  * [ Create and Manage Asymmetric Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-manage-asymmetric-keys)
  * [ Define Cloud KMS Crypto Keys Protection Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-protection-level)
  * [ Define Cloud KMS Crypto Keys Purpose ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-cloud-kms-cryptokeys-for-encrypt-decrypt-purpose)
  * [ Define Secret Manager Rotation Schedule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-secret-manager-rotation-schedule)
  * [ Enable CMEK for AlloyDB Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-for-alloydb-cluster)
  * [ Enable CMEK for BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-datasets)
  * [ Enable CMEK for BigQuery Tables ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bigquery-tables)
  * [ Enable CMEK for Cloud SQL Databases ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-cmek-cloud-sql-database)
  * [ Enable CMEK for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-bucket)
  * [ Enable CMEK on Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek-on-disk)
  * [ Enable CMEK on GKE Node Pool Boot Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-nodepool-boot-disk)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Encryption on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-encryption-gke-cluster)
  * [ Encrypt Pub/Sub topic with CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#encrypt-pubsub-topic-cmek)
  * [ Enforce CMEK ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-cmek)
  * [ Require CMEK on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek-on-dataproc-cluster)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)
  * [ Verify Cloud KMS Key Version Algorithm ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#verify-cloud-kms-key-version-algorithm)



###  soc2-2017-cc-6-1-12

Logical access to and use of confidential information is restricted to identified purposes.

  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)



###  soc2-2017-cc-6-1-3

The entity restricts logical access to information assets, including: infrastructure, for example server, storage, network elements, APIs, and endpoint devices; software; and data at rest, during processing, or in transmission, through the use of access control software, rule sets, and standard configuration hardening processes.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Service Account Key Creation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-service-account-key-creation)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Configure Remote Access Inactivity Timeout ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-remote-access-inactivity-timeout)
  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Enable Confidential Computing for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-confidential-computing)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable CSEK On Compute Engine Persistent Disks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-csek-on-disk)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Enforce Compute Session Inactive Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-session-termination-policy)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)



###  soc2-2017-cc-6-1-4

The entity identifies and authenticates persons, infrastructure, and software prior to accessing information assets, whether locally or remotely. The entity uses more complex or advanced user authentication techniques such as multifactor authentication when such protections are deemed appropriate based on its risk mitigation strategy.

  * [ Enable Workload Identity Federation for GKE on clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-workload-identity-gke)



###  soc2-2017-cc-6-1-5

The entity uses network segmentation, zero trust architectures, and other techniques to isolate unrelated portions of the entity's information technology from each other based on the entity’s risk mitigation strategy.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Configure Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-network-traffic-monitoring)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable Private Google Access for VPC Subnets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access-subnets-vpc)
  * [ Enable Private Google Access on an instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-google-access)
  * [ Prevent IP Forwarding on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-ip-forwarding)



###  soc2-2017-cc-6-1-7

Combinations of data classification, separate data structures, port restrictions, access protocol restrictions, user identification, and digital certificates are used to establish access control rules and configuration standards for information assets.

  * [ Block Automatic IAM Grants to Default Service Accounts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Project-Wide SSH Keys on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-project-wide-ssh-keys)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Block Terminal Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-terminal-access-on-vertexai)
  * [ Configure Remote Access Inactivity Timeout ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-remote-access-inactivity-timeout)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enable Uniform Bucket-Level Access on Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-uniform-bucket-level-access)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Set Uniform Bucket Level Access for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)
  * [ Terminate Network Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#terminate-network-connections)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  soc2-2017-cc-6-1-9

New internal and external infrastructure and software are registered, authorized, and documented prior to being granted access credentials and implemented on the network or access point. Credentials are removed and access is disabled when access is no longer required or the infrastructure and software are no longer in use.

  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable OS Login for All Instances at Project Level ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login-all-instances-project-level)
  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)
  * [ Require Service Account Key Rotation ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-service-account-key-rotation)
  * [ Restrict User Managed Service Account Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-user-managed-service-account-keys)



###  soc2-2017-cc-6-2-3

Processes are in place to disable, destroy, or otherwise prevent the use of access credentials when no longer valid.

  * [ Require Rotation of API Key ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-api-key-rotation)



###  soc2-2017-cc-6-3-2

Processes are in place to remove access to protected information assets when no longer required.

  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)



###  soc2-2017-cc-6-3-3

The entity uses access control structures, such as role-based access controls, to restrict access to protected information assets, limit privileges, and support segregation of incompatible functions.

  * [ Block Legacy Authorization on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-legacy-authorization)
  * [ Block Root Access on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-root-access-on-vertexai)
  * [ Create GKE Clusters with Limited Privileges ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)
  * [ Define Agent Platform Workbench Instance Access Mode ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vertexai-access-mode)
  * [ Enable 3625 Trace Database Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-3625-trace-db-flag-sql-server)
  * [ Enable OS Login ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-os-login)
  * [ Enable Skip Show Database Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-skip-show-db-flag-mysql)
  * [ Restrict API Access to Google Cloud APIs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-access-to-cloud-apis)
  * [ Restrict API Keys for Required APIs Only ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-api-keys-for-required-apis-only)
  * [ Set Application Restriction on API Keys ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-applications-api-keys)
  * [ Use Custom Service Accounts for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-non-default-service-account)
  * [ Use Least Privilege Service Accounts for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-least-privileges-service-accounts-gke)



###  soc2-2017-cc-6-5-1

Procedures are in place to remove, delete, or otherwise render data and software inaccessible from physical assets and other devices owned by the entity, its vendors, and employees when the data and software are no longer required on the asset or the asset will no longer be under the control of the entity.

  * [ Define Retention Period for Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-retention-period-for-storage-buckets)



###  soc2-2017-cc-6-6

The entity implements logical access security measures to protect against threats from sources outside its system boundaries.

  * [ Block Public IP Addresses for AlloyDB Cluster Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-alloydb-public-ip-addresses)
  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Enable DNSSEC for Cloud DNS ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-dnssec-for-cloud-dns)
  * [ Enforce Public Access Prevention ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-public-access-prevention)
  * [ Restrict Public Access to BigQuery Datasets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-bigquery-datasets)
  * [ Restrict Public Access to Cloud SQL Database Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-sql-instance)
  * [ Restrict Public Access to Cloud Storage Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-access-cloud-storage-buckets)
  * [ Restrict Public IP Addresses to Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-compute-instances-public-ip-addresses)



###  soc2-2017-cc-6-6-1

The types of activities that can occur through a communication channel, for example FTP site, router port, are restricted.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Enable Control Plane Authorized Networks on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-control-plane-authorized-networks)
  * [ Enable Private Clusters for GKE ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-private-clusters-kubernetes)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)



###  soc2-2017-cc-6-6-4

Boundary protection systems, for example, firewalls, demilitarized zones, intrusion detection or prevention systems, and endpoint detection and response systems, are configured, implemented, and maintained to protect external access points.

  * [ Block External IP Address Access on Compute Engine VM Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ip-addresses-for-vm-access)
  * [ Block Generic Access to Cassandra Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cassandra-ports)
  * [ Block Generic Access to CiscoSecure/WebSM Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ciscosecure-websm-ports)
  * [ Block Generic Access to Directory Service Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-directory-services-ports)
  * [ Block Generic Access to DNS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-dns-ports)
  * [ Block Generic Access to Elasticsearch Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-elasticsearch-ports)
  * [ Block Generic Access to FTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ftp-ports)
  * [ Block Generic Access to HTTP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-http-ports)
  * [ Block Generic Access to LDAP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-ldap-ports)
  * [ Block Generic Access to Memcached Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-memcached-ports)
  * [ Block Generic Access to MongoDB Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mongodb-ports)
  * [ Block Generic Access to MySQL Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-mysql-ports)
  * [ Block Generic Access to NetBIOS Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-netbios-ports)
  * [ Block Generic Access to Oracle Database Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-oracle-db-ports)
  * [ Block Generic Access to POP3 Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-pop3-server-ports)
  * [ Block Generic Access to PostgreSQL Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-postgresql-ports)
  * [ Block Generic Access to RDP Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-rdp-port)
  * [ Block Generic Access to Redis Server Ports from All IP Addresses ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-redis-server-ports)
  * [ Block Generic Access to SMTP Server Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-smtp-server-ports)
  * [ Block Generic Access to SSH Ports ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-access-to-ssh-port)
  * [ Block Generic Access to Telnet Servers ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-telnet-server-ports)
  * [ Block Overly Permissive Firewall Rules ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-firewall-all-ip-addresses)
  * [ Block Public IP Addresses for Cloud SQL Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-cloud-sql-public-ip-addresses)
  * [ Configure Access Controls for the Network Boundary ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#access-control-network-boundary)
  * [ Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)
  * [ Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-cloud-run-egress-settings-org-policy)
  * [ Configure the Disable VPC External IPv6 Usage Organization Policy ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-external-ipv6-addresses-org-policy)
  * [ Define a Security Policy to Mitigate for DDoS Events ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-policy-mitigate-ddos-events)
  * [ Define VPC Connector Egress For Cloud Run Functions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-vpc-connector-for-cloud-functions)
  * [ Enable Network Policy on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-network-policy)
  * [ Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-restrict-authorised-networks-org-policy)
  * [ Enforce Deny All Egress Firewall Rule ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-deny-all-egress-firewall-policy)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)
  * [ Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-public-ip-addresses-on-vertexai)
  * [ Use Custom VPC Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-network-with-custom-firewall-rules)



###  soc2-2017-cc-6-7-1

Data loss prevention processes and technologies are used to restrict ability to authorize and execute transmission, movement, and removal of information.

  * [ Disable File Downloads on Agent Platform Workbench Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-file-downloads-on-vertexai)



###  soc2-2017-cc-6-7-2

Encryption technologies or secured communication channels are used to protect transmission of data and other communications beyond connectivity access points.

  * [ Enable SSL Encryption On AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-ssl-encryption)
  * [ Enforce SSL for all Incoming Database Connections ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-ssl-incoming-connections-database)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Use TLS 1.2 or Higher ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher)



###  soc2-2017-cc-6-8-1

The ability to install and modify applications and software is restricted to authorized individuals. Utility software capable of bypassing normal operating or security procedures is limited to use by authorized individuals and is monitored regularly.

  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)



###  soc2-2017-cc-6-8-2

Processes are in place to detect changes to software and configuration parameters that may be indicative of unauthorized or malicious software.

  * [ Enable Integrity Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-integrity-monitoring)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enable Secure Boot on Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-secure-boot-on-compute-engine-instances)



###  soc2-2017-cc-7-1-1

The entity has defined configuration standards to be used for hardening systems.

  * [ Block Serial Ports for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#block-serial-ports-on-compute-engine-instances)
  * [ Disable Legacy Metadata Server Endpoints on Compute Engine ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-legacy-metadata-endpoints)
  * [ Don't Use Kubernetes Web UI ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-gke-web-ui)
  * [ Don't Use Legacy Networks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#delete-legacy-network)
  * [ Don't Use User Connections Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-connections-db-flag-sql-server)
  * [ Don't Use User Options Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dont-use-user-options-db-flag-sql-server)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Error Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-error-statement-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable PodSecurityPolicies for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-pod-security-policy-gke-cluster)
  * [ Enable Secure Boot for Shielded GKE Nodes ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-nodepool-secure-boot)
  * [ Enable Shielded GKE Nodes on a Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-nodes)
  * [ Enable Shielded VM for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-shielded-vm-compute-instances)
  * [ Ensure Minimum TLS 1.2 Version ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#use-tls-1-2-higher-google-cloud-services)
  * [ Prevent Nested Virtualization for Compute Engine VMs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#prevent-vm-nested-virtualization-for-compute-engine-instances)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Restrict Default Network Creation for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-default-network-creation-for-compute-engine)
  * [ Restrict Insecure SSL Policies for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-insecure-ssl-policies-compute)
  * [ Restrict Legacy TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-legacy-tls-versions)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)
  * [ Turn Off Contained Database Authentication Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)
  * [ Turn Off Cross Database Ownership Chaining Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-cross-db-ownership-chaining-sql-server)
  * [ Turn Off External Scripts Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-external-scripts-db-flag-sql-server)
  * [ Turn Off Local Infile Flag for MySQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-local-infile-db-flag-mysql)
  * [ Turn Off Log Executor Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)
  * [ Turn off Log Hostname Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-hostname-db-flag-postgresql)
  * [ Turn Off Log Min Duration Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)
  * [ Turn off Log Parser Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)
  * [ Turn off Log Planner Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-planner-stats-flag-postgresql)
  * [ Turn off Log Statement Stats Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)
  * [ Turn Off Remote Access Flag for SQL Server ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-remote-access-db-flag-sql-server)



###  soc2-2017-cc-7-1-5

The entity conducts infrastructure and software vulnerability scans designed to identify potential vulnerabilities or misconfigurations on a periodic basis and after significant changes are made to the environment. Action is taken to remediate identified deficiencies in a timely manner to support the achievement of the entity’s objectives.

  * [ Enable Artifact Analysis Vulnerability Scanning ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-artifact-analysis-vulnerability-scanning)



###  soc2-2017-cc-7-2-1

Detection policies, procedures, and tools are defined and implemented on infrastructure and software to identify potential intrusions, inappropriate access, and anomalies in the operation of or unusual activity on systems. Procedures may include a defined governance process for security event detection and management, use of intelligence sources to identify newly discovered threats and vulnerabilities, and logging of unusual system activities.

  * [ Configure Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-network-traffic-monitoring)
  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Cloud DNS Logs Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-dns-logging)
  * [ Enable Cloud Logging on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-logging)
  * [ Enable Cloud Monitoring on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cluster-cloud-monitoring)
  * [ Enable Firewall Rule Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-firewall-rule-logging)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Intranode Visibility for GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-intranode-visibility)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Log Locks Wait Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-locks-wait-db-flag-postgresql)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)



###  soc2-2017-cc-7-2-2

Detection measures are designed to identify anomalies that could result from actual or attempted compromise of physical barriers, unauthorized actions of authorized personnel, use of compromised identification and authentication credentials, unauthorized access from outside the system boundaries, compromise of authorized external parties, and implementation or connection of unauthorized hardware and software.

  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Implement Continuous Network Traffic Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-continuous-network-traffic-monitoring)



###  soc2-2017-cc-7-3-2

Detected security events are communicated to and reviewed by the individuals responsible for the management of the security program, and actions are taken, if necessary.

  * [ Define Essential Contacts ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-essential-contacts)



###  soc2-2017-cc-8-1-1

A process for managing system changes throughout the life cycle of the system and its components (infrastructure, data, software, and manual and automated procedures) is used to support the achievement of entity objectives.

  * [ Define Storage Class Lifestyle Action ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-storage-class-lifestyle-action)



###  soc2-2017-cc-8-1-14

A process is in place to identify, evaluate, test, approve, and implement patches in a timely manner on infrastructure and software.

  * [ Enable Auto Upgrade on GKE Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-auto-upgrade)
  * [ Require Auto Upgrade Schedule Set for Agent Platform Workbench ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-vertexai-auto-upgrade-schedule-set)
  * [ Require Container-Optimized OS for a GKE Cluster ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-container-optimized-os)
  * [ Subscribe a GKE Cluster to a Release Channel ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#subscribe-release-channel-gke-cluster)
  * [ Use Latest Image Versions on Dataproc Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-latest-image-version-on-dataproc-cluster)



###  soc2-2017-cc-8-1-5

A process is in place to track system changes prior to implementation.

  * [ Enable Cloud Asset Inventory Service ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-cloud-asset-api)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)



###  soc2-2017-p-4-2-1

Personal information is retained for no longer than necessary to fulfill the stated purposes, unless a law or regulation specifically requires otherwise.

  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)



###  soc2-2017-p-4-2-2

Policies and procedures have been implemented to protect personal information from erasure or destruction during the specified retention period of the information.

  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)



###  soc2-2017-pi-1-2-3

Records of system input activities are created and maintained completely and accurately in a timely manner.

  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)



###  soc2-2017-pi-1-3-4

System processing activities are recorded completely and accurately in a timely manner.

  * [ Configure Security Logging Policies for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#define-security-logging-policy)
  * [ Enable Audit Logs for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-audit-logs-gcp-services)
  * [ Enable Flow Logs for VPC Subnet ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs)
  * [ Enable Load Balancer Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-load-balancer-logging)
  * [ Enable Log Checkpoints Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-checkpoint-db-flag-postgresql)
  * [ Enable Log Connections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-connections-db-flag-postgres)
  * [ Enable Log Disconnections Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-disconnections-db-flag-postgres)
  * [ Enable Log Duration Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-duration-db-flag-postgresql)
  * [ Enable Log Error Verbosity Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-error-verbosity-db-flag-postgres)
  * [ Enable Log Min Messages Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-min-messages-db-flag-postgres)
  * [ Enable Log Statement Flag for PostgreSQL ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-statement-db-flag-postgres)
  * [ Enable Log Temp Files Flag for PostgreSQL instance ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-log-temp-files-db-flag-postgresql)
  * [ Enable Subnet Flow Logs ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-subnet-flowlogs)
  * [ Enable VPC Flow Logs for Compute Engine Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-vpc-flow-logs-for-compute-engine-instances)
  * [ Implement Event Logging for Google Cloud Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#implement-event-logging)
  * [ Require Cloud Storage Bucket Logging ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-bucket-logging)
  * [ Set Log Error Verbosity Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-error-verbosity-flag)
  * [ Set Log Min Error Statement Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-error-statement-flag)
  * [ Set Log Min Messages Flag for AlloyDB Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-alloydb-log-min-messages-flag)



###  soc2-2017-pi-1-5

The entity implements policies and procedures to store inputs, items in processing, and outputs completely, accurately, and timely in accordance with system specifications to meet the entity’s objectives.

  * [ Allocate Audit Log Storage Capacity ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#allocate-audit-log-storage-capacity)



###  soc2-2017-pi-1-5-1

Stored items are protected to prevent theft, corruption, destruction, or deterioration that would prevent output from meeting specifications.

  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)



###  soc2-2017-pi-1-5-2

System records are archived, and archives are protected against theft, corruption, destruction, or deterioration that would prevent them from being used.

  * [ Configure Log Sinks ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#configure-log-sinks)
  * [ Enable Object Versioning on Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-object-versioning-on-buckets)
  * [ Lock Storage Bucket Retention Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-storage-bucket-locked-retention-policy)



##  Switzerland Data Boundary

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Supports compliance with Switzerland data residency requirements by restricting resource locations to Switzerland regions.

This framework includes the following cloud controls: 

  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Disable the Creation and Update of Kafka Connect Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-kafka-connect-clusters-create-and-update)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable Looker (Google Cloud core) Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#looker-regulatory-settings)
  * [ Enable Regulatory Settings for Apigee ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#apigee-regulatory-settings)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)



##  UK Data Boundary

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Supports compliance with UK data residency requirements by restricting resource locations to UK regions.

This framework includes the following cloud controls: 

  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Disable the Creation and Update of Kafka Connect Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-kafka-connect-clusters-create-and-update)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable Looker (Google Cloud core) Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#looker-regulatory-settings)
  * [ Enable Regulatory Settings for Apigee ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#apigee-regulatory-settings)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)



##  US Data Boundary

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Supports compliance with US data residency requirements by restricting resource locations to US regions.

This framework includes the following cloud controls: 

  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Disable the Creation and Update of Kafka Connect Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-kafka-connect-clusters-create-and-update)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable Looker (Google Cloud core) Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#looker-regulatory-settings)
  * [ Enable Regulatory Settings for Apigee ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#apigee-regulatory-settings)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)



##  US Data Boundary and Support

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supported cloud provider:** Google Cloud 

Supports compliance with US data residency and support requirements by restricting resource locations to US regions and limiting support access to US-based personnel.

This framework includes the following cloud controls: 

  * [ BigQuery compliance settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#big-query-regulatory-settings)
  * [ Cloud Databases Context Store Regulatory Settings ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-databases-contextstore-regulatory-settings)
  * [ Configure Dataplex to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataplex-regulatory-settings)
  * [ Configure Dataproc to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#dataproc-regulatory-settings)
  * [ Configure Google Agent Platform to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#google-agent-platform-regulatory-settings)
  * [ Configure Spanner to Support Data Boundaries ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#spanner-regulatory-settings)
  * [ Define Locations for Cloud Logging Buckets ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-storage-locations)
  * [ Define Locations for Technical Support Services ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-technical-support-services)
  * [ Disable Global Cloud Armor Policies ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-global-cloud-armor)
  * [ Disable Pub/Sub Subscription Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-subscription-transforms)
  * [ Disable Pub/Sub Topic Message Transforms ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-pubsub-topic-transforms)
  * [ Disable Spanner Multi-Region Instances ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-spanner-multi-region)
  * [ Disable the Creation and Update of Kafka Connect Clusters ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#disable-kafka-connect-clusters-create-and-update)
  * [ Enable Access Transparency ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-axt)
  * [ Enable Advanced Service Controls for Spanner ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enable-spanner-advanced-service-controls)
  * [ Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-logging-regulatory-settings)
  * [ Enable Compliance Settings for Cloud Monitoring ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#cloud-monitoring-regulatory-settings)
  * [ Enable Looker (Google Cloud core) Compliance with FedRAMP or DoD Impact Levels ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#looker-regulatory-settings)
  * [ Enable Regulatory Settings for Apigee ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#apigee-regulatory-settings)
  * [ Require CMEK Protection ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#require-cmek)
  * [ Restrict Resource Locations ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-resource-locations)
  * [ Restrict Service Usage ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#enforce-service-usage-restrictions)
  * [ Restrict TLS Versions ](https://docs.cloud.google.com/assured-workloads/docs/compliance-cloud-controls#restrict-tls-versions)



## What's next

  * Learn more about [Assured Workloads frameworks](https://docs.cloud.google.com/assured-workloads/docs/frameworks-overview).
  * Learn how to [manage frameworks](https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
