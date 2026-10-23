---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general/
title: Google Cloud Best Practices Reference \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:49.574503+00:00
---

# Google Cloud Best Practices Reference  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Google Cloud Best Practices Reference Stay organized with collections  Save and categorize content based on your preferences. 

Workload Manager checks the state of your resources against the up-to-date best practices and helps you improve the quality, reliability, and performance of your workloads running on Google Cloud.

This document lists the best practices that Workload Manager supports for evaluating your workloads running on Google Cloud. To learn about Workload Manager, see [Product overview](https://docs.cloud.google.com/workload-manager/docs/overview).

## Severity levels

When you run an evaluation, Workload Manager evaluates resources by comparing their current state with best practices. If a resource doesn't comply with a selected best practice, Workload Manager assigns it a severity level that indicates how far the resource is out of compliance. The Google Cloud console marks each non-compliant resource with an icon. The following table explains these icons, their corresponding severity levels, how the current resource setting might impact your workload, and recommendations for modifying the resource to adhere to best practices. Icon | Severity level | Impacts | Recommendation  
---|---|---|---  
![](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg) | Critical | System Reliability, Unplanned Outages, Unsupported Configuration |  Resolve as soon as possible to prevent an impact on system availability and data integrity due to a high risk of an unplanned outage.  
![](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg) | High | Degraded Performance, System Stability | Resolve during the next planned maintenance window.  
![](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg) | Medium | Suboptimal Performance, Supportability | Resolve at your earliest convenience.  
![](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg) | Low | Informational, Non-essential Behavior | Although there's no resolution needed, reviewing this best practice can provide useful insights.  
  
## Supported best practices

Workload Manager supports evaluating the following workload types to help ensure they adhere to Google Cloud best practices:

  * **Google Cloud (General)** : Best practices for core Google Cloud services. 
    * API keys
    * Access Transparency
    * AlloyDB for PostgreSQL
    * Apigee X
    * Artifact
    * BigQuery
    * Cloud Bigtable
    * Cloud Build
    * Cloud DNS
    * Cloud Functions
    * Cloud Interconnect
    * Cloud Key Management Service
    * Cloud Load Balancing
    * Cloud Pub/Sub
    * Cloud Router
    * Cloud Run
    * Cloud SQL
    * Cloud Spanner
    * Cloud Storage
    * Cloud VPN
    * Composer
    * Compute Engine
    * Dataproc
    * Filestore
    * Firestore
    * Google Kubernetes Engine
    * IAM
    * Memorystore for Memcache
    * Memorystore for Redis
    * Memorystore for Redis Cluster
    * Operations
    * Organization Policy Service
    * Resource Manager
    * Secret Manager
    * Security Command Center
    * Sensitive Data Protection
    * Gemini Enterprise Agent Platform
    * Gemini Enterprise Agent Platform Workbench
  * **MySQL** : Best practices for MySQL database deployments. 
    * General
  * **Redis** : Best practices for Redis deployments. 
    * General
  * **SAP** : Best practices for SAP systems. 
    * General
    * HANA
    * HANA Insights
    * HANA Security Best Practices
    * High Availability
    * NetWeaver
  * **SQL Server** : Best practices for SQL Server database deployments. 
    * Cost Optimization
    * Failover Cluster
    * Performance
    * Stability
  * **OpenShift** : Best practices for Red Hat OpenShift clusters. 
    * Cost Optimization
    * Operational Efficiency
    * Reliability
    * Security



The following sections list the supported best practices for your workloads that run on Google Cloud.

A total of **627** best practice rules are available.

### Count of rules by Best practices

Category | Rule Count  
---|---  
API keys| 4  
Access Transparency| 1  
AlloyDB for PostgreSQL| 4  
Apigee X| 1  
Artifact Registry| 1  
BigQuery| 10  
Cloud Bigtable| 3  
Cloud Build| 1  
Cloud DNS| 3  
Cloud Functions| 3  
Cloud Key Management Service| 14  
Cloud Load Balancing| 4  
Cloud Logging| 3  
Cloud Pub/Sub| 7  
Cloud Router| 6  
Cloud Run| 3  
Cloud SQL| 35  
Cloud Spanner| 6  
Cloud Storage| 20  
Cloud VPN| 4  
Composer| 1  
Compute Engine| 95  
Dataproc| 2  
Filestore| 5  
Firestore| 1  
Gemini Enterprise Agent Platform| 18  
Gemini Enterprise Agent Platform Workbench| 11  
Google Kubernetes Engine| 55  
IAM| 75  
Memorystore for Memcache| 2  
Memorystore for Redis| 8  
Memorystore for Redis Cluster| 3  
NetApp Volumes| 1  
Networking| 5  
Organization Policy Service| 58  
Resource Manager| 3  
SecOps| 1  
Secret Manager| 2  
Security Command Center| 1  
Sensitive Data Protection| 1  
MySQL: General| 7  
OpenShift: Cost Optimization| 1  
OpenShift: Operational Efficiency| 6  
OpenShift: Reliability| 5  
OpenShift: Security| 6  
Redis: General| 7  
SAP: General| 14  
SAP: HANA| 10  
SAP: HANA Insights| 18  
SAP: HANA Security Best Practices| 19  
SAP: High Availability| 33  
SAP: NetWeaver| 3  
SQL Server: Cost Optimization| 2  
SQL Server: Failover Cluster| 2  
SQL Server: Performance| 10  
SQL Server: Stability| 3  
**Total**| **627**  
  
The best practices are tagged to help you identify their focus areas: 

  * **Reliability** , **Security** , and **FinOps** rules are mapped to the pillars of the [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework).
  * **CSPR** : [Cloud Security Posture Review](https://cloud.google.com/consulting/portfolio/cloud-security-posture-review-subscription).
  * **MVSP** : [Minimal Viable Security Posture](https://docs.cloud.google.com/docs/security/gcmvsp).



Select one or more rule categories to filter the following list.

Google Cloud (General)MySQLOpenShiftRedisSAPSQL ServerGoogle Cloud Best Practices - API keysGoogle Cloud Best Practices - Access TransparencyGoogle Cloud Best Practices - AlloyDB for PostgreSQLGoogle Cloud Best Practices - Apigee XGoogle Cloud Best Practices - Artifact RegistryGoogle Cloud Best Practices - BigQueryGoogle Cloud Best Practices - Cloud BigtableGoogle Cloud Best Practices - Cloud BuildGoogle Cloud Best Practices - Cloud DNSGoogle Cloud Best Practices - Cloud FunctionsGoogle Cloud Best Practices - Cloud Key Management ServiceGoogle Cloud Best Practices - Cloud Load BalancingGoogle Cloud Best Practices - Cloud LoggingGoogle Cloud Best Practices - Cloud Pub/SubGoogle Cloud Best Practices - Cloud RouterGoogle Cloud Best Practices - Cloud RunGoogle Cloud Best Practices - Cloud SQLGoogle Cloud Best Practices - Cloud SpannerGoogle Cloud Best Practices - Cloud StorageGoogle Cloud Best Practices - Cloud VPNGoogle Cloud Best Practices - ComposerGoogle Cloud Best Practices - Compute EngineGoogle Cloud Best Practices - DataprocGoogle Cloud Best Practices - FilestoreGoogle Cloud Best Practices - FirestoreGoogle Cloud Best Practices - Gemini Enterprise Agent PlatformGoogle Cloud Best Practices - Gemini Enterprise Agent Platform WorkbenchGoogle Cloud Best Practices - Google Kubernetes EngineGoogle Cloud Best Practices - IAMGoogle Cloud Best Practices - Memorystore for MemcacheGoogle Cloud Best Practices - Memorystore for RedisGoogle Cloud Best Practices - Memorystore for Redis ClusterGoogle Cloud Best Practices - NetApp VolumesGoogle Cloud Best Practices - NetworkingGoogle Cloud Best Practices - Organization Policy ServiceGoogle Cloud Best Practices - Resource ManagerGoogle Cloud Best Practices - SecOpsGoogle Cloud Best Practices - Secret ManagerGoogle Cloud Best Practices - Security Command CenterGoogle Cloud Best Practices - Sensitive Data ProtectionMySQL: GeneralOpenShift: Cost OptimizationOpenShift: Operational EfficiencyOpenShift: ReliabilityOpenShift: SecurityRedis: GeneralSAP: GeneralSAP: HANASAP: HANA InsightsSAP: HANA Security Best PracticesSAP: High AvailabilitySAP: NetWeaverSQL Server: Cost OptimizationSQL Server: Failover ClusterSQL Server: PerformanceSQL Server: StabilityCriticalHighMediumLowReliabilitySecurityFinOpsCSPRMVSP

### Google Cloud Best Practices - API keys (4 results)

  * ####  Api key no restriction link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, api key, Security, CSPR, CoNa

Asset: `apikeys.googleapis.com/Key`

Details

Verifies that all API keys have restrictions applied, preventing misuse that could lead to security breaches, unauthorized data access, and unexpected costs.

  * ####  Api key no service restriction link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, api key, Security, CSPR, CoNa

Asset: `apikeys.googleapis.com/Key`

Details

Ensures API keys are restricted to specific services, preventing potential misuse that could lead to unauthorized API activation, security vulnerabilities, and unexpected costs.

  * ####  Api key older 90 days link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: IAM, api key, Security, CSPR

Asset: `apikeys.googleapis.com/Key`

Details

Enforces a 90day rotation policy for API keys to minimize the security risk from lost, leaked, or compromised credentials.

  * ####  Api keys link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, api key, Security, CSPR

Asset: `apikeys.googleapis.com/Key`

Details

Flags the existence of any API key to encourage the use of more secure authentication methods, such as service accounts, thereby reducing the risk associated with static, longlived credentials.




### Google Cloud Best Practices - Access Transparency (1 results)

  * ####  Organization access transparency enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Access Transparency, serviceusage, Security, Compliance

Asset: `serviceusage.googleapis.com/Service`

Details

Checks if Access Transparency service is enabled. Access Transparency provides you with logs of actions that Google personnel take when accessing your content.




### Google Cloud Best Practices - AlloyDB for PostgreSQL (4 results)

  * ####  Alloy cluster automated backups not enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: AlloyDB, Backup, Reliability, Cost, BCDR, DataProtection, CSPR

Asset: `alloydb.googleapis.com/Cluster`

Details

Verifies that AlloyDB clusters have an automated backup policy enabled, ensuring critical data is protected against loss and can be rapidly recovered to maintain business continuity and service reliability.

  * ####  Alloy cluster continuous backups not enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: AlloyDB, Backup, BCDR, DataProtection, Reliability, Cost, CSPR

Asset: `alloydb.googleapis.com/Cluster`

Details

Verifies AlloyDB clusters have continuous backup enabled, providing crucial pointintime recovery (PITR) to protect against data loss and ensure business continuity.

  * ####  Alloy cluster maintenance policy link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Operations, BCDR, CSPR

Asset: `alloydb.googleapis.com/Cluster`

Details

Verifies that AlloyDB clusters have a maintenance update policy defined. Defining a maintenance policy allows organizations to schedule updates during nonpeak hours to minimize disruption. The absence of this policy implies default timing which may coincide with critical operational periods.

  * ####  Alloy instance public IP link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: AlloyDB, Security, Network, CSPR

Asset: `alloydb.googleapis.com/Instance`

Details

Checks if AlloyDB instances have public IP enabled. Public IPs expose the instance to the internet, increasing the attack surface. It is recommended to use private IPs instead.




### Google Cloud Best Practices - Apigee X (1 results)

  * ####  Apigee multiregion instances link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, API, Apigee, HighAvailability, BCDR, CoNa

Asset: `apigee_Organization_RESOURCE_INSTANCE`

Details

Verifies that an Apigee X Organization has Apigee instances deployed across at least 2 different regions. Multi-regional Apigee deployment ensures API gateway redundancy, low latency, and protects against regional outages.




### Google Cloud Best Practices - Artifact Registry (1 results)

  * ####  Artifact registry multi regional link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Availability, BCDR

Asset: `artifactregistry.googleapis.com/Repository`

Details

Verifies that Artifact Registry repositories are configured to use a multiregion location (e.g., us, europe, asia). Using multiregion locations ensures artifacts are replicated across multiple geographical regions, significantly enhancing availability and resilience against regional outages.




### Google Cloud Best Practices - BigQuery (10 results)

  * ####  BigQuery dataset CMEK disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: BigQuery, Dataset, Encryption, CMEK, Security, CSPR

Asset: `bigquery.googleapis.com/Dataset`

Details

Checks if BigQuery datasets are encrypted using CustomerManaged Encryption Keys (CMEK) from Cloud KMS. While BigQuery encrypts data at rest by default with Googlemanaged keys, CMEK offers finergrained control over key management, including rotation, access control, and audit logging. This rule inspects the defaultEncryptionConfiguration field within the datasets configuration. A violation is triggered if this field is missing or if it exists but lacks a kmsKeyName property. The absence of defaultEncryptionConfiguration or kmsKeyName signifies that the dataset is not employing CMEK for encryption, potentially impacting compliance and security posture.

  * ####  BigQuery dataset missing labels link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: BigQuery, Dataset, Labels, Organization, FinOps, Management, CSPR

Asset: `bigquery.googleapis.com/Dataset`

Details

Checks if a BigQuery dataset has labels applied. Labels are userdefined keyvalue pairs that help organize and manage resources within Google Cloud. They are used for filtering, grouping, and cost reporting. This rule checks for the presence of the labels field on the dataset. A violation is triggered if the labels field is missing or if its empty.

  * ####  BigQuery dataset missing resource tags link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: BigQuery, Dataset, Tags, Organization, Management, AccessControl, FinOps, CSPR, CoNa, MVSP

Asset: `bigquery.googleapis.com/Dataset`

Details

Checks if a BigQuery dataset has resource tags applied. Resource tags are keyvalue pairs managed through Resource Manager. They are used for broader organizational purposes, including integration with other Google Cloud services and external systems (e.g., for access control via tag bindings). This rule checks for the presence of the resourceTags field. A violation is generated if the tags field is missing, or it is empty.

  * ####  BigQuery dataset multi region link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, BigQuery, MultiRegion, HighAvailability, BCDR

Asset: `bigquery.googleapis.com/Dataset`

Details

Verifies that BigQuery datasets are configured with a multi-region location (like 'US' or 'EU') to ensure high resilience and data redundancy across regions. Regional datasets (configs with a hyphen) do not satisfy this standard.

  * ####  BigQuery dataset public link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: BigQuery, Dataset, Security, Privacy, Cost, Reliability, CSPR

Asset: `bigquery.googleapis.com/Dataset`

Details

Checks if BigQuery datasets are not publicly exposed. Publicly exposed datasets can lead to unintentional data leakage and potential privacy violations. BigQuery offers granular access controls via IAM roles, and datasets should be restricted to authorized users and service accounts only. This rule checks for the presence of allUsers or allAuthenticatedUsers in the datasets access control list, which grants public access. The absence of these entries indicates that the dataset is not publicly accessible.

  * ####  BigQuery table CMEK link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: BigQuery, Table, Encryption, CMEK, KMS, Security, Compliance, CSPR

Asset: `bigquery.googleapis.com/Table`

Details

Checks if BigQuery tables are encrypted using CustomerManaged Encryption Keys (CMEK) in Cloud KMS. By default, BigQuery encrypts data at rest using Googlemanaged keys. CMEK provides more granular control over the encryption keys, allowing organizations to manage key rotation, access, and auditing. This rule examines the encryptionConfiguration field within the tables configuration. If this field is missing, or if it exists but does not contain a kmsKeyName, it indicates that the table is not using CMEK for encryption.

  * ####  BigQuery table expiration link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: BigQuery, Table, Expiration, DataLifecycle, CostOptimization, DataGovernance, CSPR

Asset: `bigquery.googleapis.com/Table`

Details

Checks if a BigQuery table has an expiration time set. Setting an expiration time on tables is a best practice for managing data lifecycle and controlling storage costs, especially for temporary or staging tables. This rule examines the expirationTime field within the tables configuration. If expirationTime is null (or missing, which is treated the same way in Rego), it indicates that the table does not have an expiration time set, and a violation is generated. An explicit expiration time is a good practice for data governance.

  * ####  BigQuery table missing labels link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: BigQuery, table, Labels, Organization, FinOps, Management, CSPR

Asset: `bigquery.googleapis.com/Table`

Details

Checks if a BigQuery table has labels applied. Labels are userdefined keyvalue pairs that help organize and manage resources within Google Cloud. They are used for filtering, grouping, and cost reporting. This rule checks for the presence of the labels field on the table. A violation is triggered if the labels field is missing or if its empty.

  * ####  BigQuery table missing resource tags link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: BigQuery, Table, Tags, Organization, Management, AccessControl, FinOps, CSPR, CoNa, MVSP

Asset: `bigquery.googleapis.com/Table`

Details

Checks if a BigQuery table has resource tags applied. Resource tags are keyvalue pairs managed through Resource Manager. They are used for broader organizational purposes, including integration with other Google Cloud services and external systems (e.g., for access control via tag bindings). This rule checks for the presence of the resourceTags field. A violation is generated if the resourceTags field is missing, or if it is empty.

  * ####  BigQuery table partition link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: BigQuery, Table, Partition, Expiration, DataLifecycle, CostOptimization, TimePartitioning, CSPR

Asset: `bigquery.googleapis.com/Table`

Details

Checks if a timepartitioned BigQuery table has a partition expiration time set. Partition expiration automatically deletes partitions that are older than the specified duration. This is crucial for managing storage costs and data lifecycle, especially for large, timeseries datasets. This rule examines the timePartitioning field and, specifically, the expirationMs field within timePartitioning. If timePartitioning is missing, or expirationMs is missing or if its not a positive integer, it indicates that partition expiration is not configured correctly, and a violation is generated.




### Google Cloud Best Practices - Cloud Bigtable (3 results)

  * ####  Bigtable cluster redundancy link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Database, Bigtable, HighAvailability, BCDR

Asset: `bigtableadmin_Instance_RESOURCE_CLUSTER`

Details

Verifies that Bigtable instances have clusters deployed across 3 or more different regions. Multi-regional cluster redundancy ensures 99.999% availability, robust disaster recovery, and low-latency access for globally distributed applications.

  * ####  Bigtable instance replication enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Database, Bigtable, Replication, HighAvailability

Asset: `bigtableadmin_Instance_RESOURCE_CLUSTER`

Details

Verifies that Bigtable instances have replication enabled by ensuring they have clusters deployed in at least 2 different zones or regions. Replication is critical for high availability, failover, and disaster recovery.

  * ####  Bigtable profile multi cluster routing link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, HighAvailability, BCDR, Bigtable

Asset: `bigtableadmin.googleapis.com/AppProfile`

Details

Verifies that Bigtable App Profiles utilize multi_cluster_routing_use_any to enable automatic failover and ensure high availability. Using singlecluster routing creates a single point of failure, risking service disruptions if the specific cluster becomes unavailable.




### Google Cloud Best Practices - Cloud Build (1 results)

  * ####  Cloudbuild pool redundancy link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Security, CloudBuild, HighAvailability, BCDR

Asset: `cloudresourcemanager_Project_RESOURCE_WORKERPOOL`

Details

Verifies that Cloud Build private worker pools are deployed across at least 2 different regions. Deploying private worker pools in multiple regions ensures that CI/CD workflows can fail over if a regional build service experiences an outage.




### Google Cloud Best Practices - Cloud DNS (3 results)

  * ####  DNS policy logging link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: DNS, Policy, Logging, Security, Auditing, VPC, CSPR, CoNa, MVSP

Asset: `dns.googleapis.com/Policy`

Details

Checks if logging is enabled for a Cloud DNS Policy. DNS policies define rules for DNS resolution behavior, often used for outbound forwarding or private DNS lookups. Enabling logging records the queries processed by the policy, which is essential for security auditing and troubleshooting DNS resolution issues within your VPC networks. This rule examines the enableLogging field within the DNS Policy configuration. A violation is generated if enableLogging is missing or if its false.

  * ####  DNS zone public dnssec link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: DNS, DNSSEC, Security, ManagedZone, Public, CSPR, CoNa

Asset: `dns.googleapis.com/ManagedZone`

Details

Checks if DNSSEC (Domain Name System Security Extensions) is enabled for a public managed zone in Cloud DNS. DNSSEC adds a layer of security by digitally signing DNS records, preventing DNS spoofing and cache poisoning attacks. This rule examines the dnssecConfig field within the managed zones configuration. If dnssecConfig is missing, or if its state is off or missing, it indicates that DNSSEC is not enabled. A violation is generated if DNSSEC is not enabled for public zones. This rule filters to affect only managed zones where visibility is set to public.

  * ####  DNS zone public logging link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: DNS, ManagedZone, Logging, Security, Auditing, Public, CSPR, CoNa, MVSP

Asset: `dns.googleapis.com/ManagedZone`

Details

Checks if logging is enabled for a public Cloud DNS managed zone. Enabling DNS logging records the queries received by the zones name servers, which is essential for security auditing, troubleshooting, and compliance. This rule examines the loggingConfig field within the managed zones configuration. A violation is generated if the zones visibility is public and either loggingConfig is missing, or loggingConfig.enableLogging is missing or false.




### Google Cloud Best Practices - Cloud Functions (3 results)

  * ####  Cloudfunctions ingress gclb link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Security, Network, HighAvailability

Asset: `cloudfunctions.googleapis.com/Function`

Details

Verifies that Cloud Functions have ingress settings configured to ALLOW_INTERNAL_AND_GCLB. This setting restricts access to internal traffic and Google Cloud Load Balancing, which is a requirement for implementing multi-regional High Availability using Global External Load Balancers while preventing direct public access.

  * ####  Function min instance link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Performance, Serverless

Asset: `cloudfunctions.googleapis.com/Function`

Details

Ensures that Cloud Functions have the minInstances setting configured to a value greater than 0. This configuration prevents cold starts, ensuring consistent performance and reduced latency during traffic spikes by keeping instances warm and ready.

  * ####  Project multiregion functions link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Serverless, CloudFunctions, HighAvailability, BCDR

Asset: `cloudresourcemanager_Project_RESOURCE_FUNCTION`

Details

Verifies that a Project has Cloud Functions deployed across at least 2 different regions. Multi-regional Cloud Function deployment ensures serverless application redundancy and ensures seamless failover in the event of a regional outage.




### Google Cloud Best Practices - Cloud Key Management Service (14 results)

  * ####  Cloud KMS cryptokey protection level hsm link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: KMS, CryptoKey, Security, HSM, ProtectionLevel, Encryption, CSPR, CoNa

Asset: `cloudkms.googleapis.com/CryptoKey`

Details

Checks if a Cloud KMS CryptoKeys protection level is set to HSM. The protectionLevel determines where cryptographic operations are performed. HSM means they occur within a Hardware Security Module. HSM provides a higher level of security. This rule checks the versionTemplate.protectionLevel field. A violation is generated if the protectionLevel is HSM. While SOFTWARE protection level is acceptable for some use cases, HSM is generally recommended for higher security requirements.

  * ####  Cloud KMS cryptokey protection level software link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: KMS, CryptoKey, Security, HSM, ProtectionLevel, Encryption, CSPR, CoNa

Asset: `cloudkms.googleapis.com/CryptoKey`

Details

Checks if a Cloud KMS CryptoKeys protection level is set to SOFTWARE. The protectionLevel determines where cryptographic operations are performed. SOFTWARE means operations occur in software, while HSM means they occur within a Hardware Security Module. HSM provides a higher level of security. This rule checks the versionTemplate.protectionLevel field. A violation is generated if the protectionLevel is SOFTWARE. While SOFTWARE protection level is acceptable for some use cases, HSM is generally recommended for higher security requirements.

  * ####  Cloud KMS cryptokey symmetric rotation link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: KMS, CryptoKey, Rotation, Security, Encryption, Symmetric, KeyRotation, CSPR, CoNa

Asset: `cloudkms.googleapis.com/CryptoKey`

Details

Checks if a Cloud KMS CryptoKey with the GOOGLE_SYMMETRIC_ENCRYPTION algorithm and an ENABLED state has key rotation configured. Regular key rotation is a critical security best practice. This rule verifies the following 1. state The keys state is ENABLED. 2. purpose The keys purpose is ENCRYPT_DECRYPT. 3. versionTemplate.algorithm The algorithm is GOOGLE_SYMMETRIC_ENCRYPTION. 4. rotationPeriod or nextRotationTime If either of these fields is missing, it indicates that rotation is not configured, and a violation is generated. The absence of rotation significantly increases the risk if a key is compromised.

  * ####  Cloud KMS ekm connection redundant resolvers link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Security, KMS, ExternalKey, HighAvailability

Asset: `cloudkms.googleapis.com/EkmConnection`

Details

Ensures that External Key Manager (EKM) connections have redundant service resolvers to prevent cryptographic operations failure during endpoint outages.

  * ####  Cloud KMS key folder publicly exposed link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Compute Engine, image, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

Detects publicly exposed KMS keys within a folder for preventing unauthorized access and decryption of sensitive data, thereby safeguarding your critical information assets and mitigating breach risks.

  * ####  Cloud KMS key organization publicly exposed link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Compute Engine, image, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Ensure your organizations KMS encryption keys are not publicly exposed through IAM policies, safeguarding sensitive data from unauthorized access and preventing costly data breaches.

  * ####  Cloud KMS key project publicly exposed link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Compute Engine, image, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Safeguard critical data and maintain compliance by preventing public KMS key exposure, which restricts cryptographic operations to authorized identities only and mitigates risks of unauthorized access and data breaches.

  * ####  Cloud KMS key publicly exposed link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Compute Engine, image, Security, CSPR, CoNa

Asset: `cloudkms.googleapis.com/CryptoKey`

Details

This rule identifies publicly exposed KMS keys, preventing unauthorized data decryption to safeguard sensitive information, ensure data integrity, and avert costly breaches.

  * ####  Cloud KMS key purpose symmetric link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: KMS, CryptoKey, Security, Encryption, CSPR, CoNa

Asset: `cloudkms.googleapis.com/CryptoKey`

Details

Checks if the Cloud KMS CryptoKey purpose is set to ENCRYPT_DECRYPT. While KMS supports other purposes like asymmetric signing or decryption, this rule enforces symmetric encryption keys as the baseline. If asymmetric keys are required for specific workloads, this rule may generate false positives and should be scoped accordingly.

  * ####  Cloud KMS key ring publicly exposed link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Compute Engine, image, Security, CSPR, CoNa

Asset: `cloudkms.googleapis.com/KeyRing`

Details

Prevent unauthorized access to sensitive encrypted data by ensuring KMS key ring IAM policies do not grant public permissions, thereby safeguarding data confidentiality and integrity.

  * ####  Cloud KMS key rotation disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: KMS, KeyRotation, Security, Cryptography, Compliance, Reliability, CSPR, CoNa

Asset: `cloudkms.googleapis.com/CryptoKey`

Details

Checks if Google Cloud Key Management Service (KMS) keys have automatic key rotation enabled. Regular key rotation is a critical security best practice to limit the potential impact of a compromised key. If a key is compromised, rotation limits the time an attacker can use it. This rule flags KMS keys that either do not have rotation enabled. Shorter rotation periods are generally preferred for enhanced security.

  * ####  Cloud KMS key rotation enabled 1yr link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: KMS, KeyRotation, Security, Cryptography, Compliance, Reliability, CSPR, CoNa

Asset: `cloudkms.googleapis.com/CryptoKey`

Details

Checks if Google Cloud Key Management Service (KMS) keys have automatic key rotation enabled and if the rotation period is within an acceptable limit (not greater than 365 days). Regular key rotation is a critical security best practice to limit the potential impact of a compromised key. If a key is compromised, rotation limits the time an attacker can use it. This rule flags KMS keys that either do not have rotation enabled or have a rotation period exceeding 365 days. Shorter rotation periods are generally preferred for enhanced security.

  * ####  Cloud KMS keyring multi region link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, BCDR, Availability, Resiliency

Asset: `cloudkms.googleapis.com/KeyRing`

Details

Verifies that Cloud KMS KeyRings are configured for multiregion or global availability to maximize resilience against regional outages. Keys stored in single regions are not replicated across multiple geographic areas, creating a single point of failure during regional incidents.

  * ####  Cloud KMS owner role link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: KMS, Security, CSPR

Asset: `cloudkms_CryptoKey_RESOURCE_IAM_POLICY_1`

Details

Restricting the highly permissive Owner role on KMS projects safeguards cryptographic keys from accidental or malicious actions, enhancing data security and operational stability.




### Google Cloud Best Practices - Cloud Load Balancing (4 results)

  * ####  Compute forwarding rule network tier link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, LoadBalancing, NetworkTier, Performance

Asset: `compute.googleapis.com/ForwardingRule`

Details

Verifies that Forwarding Rules (used by Load Balancers) are configured to use the Premium Network Tier. Premium Tier routing sends traffic over Google's high-speed global network backbone instead of the public internet, ensuring maximum reliability, low latency, and SLA guarantees.

  * ####  Compute regional backend service zone distribution link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, LoadBalancing, HighAvailability

Asset: `compute.googleapis.com/RegionBackendService`

Details

Verifies that regional Backend Services (used by Internal Load Balancers) have backends distributed across at least 2 different zones within the region. Multi-zonal backend distribution ensures high availability and failover capability during zonal outages.

  * ####  Glb backend distribution link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, LoadBalancing, HighAvailability, BCDR

Asset: `compute_BackendService_RESOURCE_RELATIONSHIP`

Details

Verifies that Global Load Balancing backends are distributed across at least 2 regions and 2 zones. Multi-regional and multi-zonal backend distribution ensures high availability, fault tolerance, and seamless failover in the event of a regional or zonal outage.

  * ####  Target pool health check enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, LoadBalancing, HighAvailability

Asset: `compute.googleapis.com/TargetPool`

Details

Ensure target pools (Network Load Balancers) have health checks enabled to prevent routing traffic to unhealthy VM backends.




### Google Cloud Best Practices - Cloud Logging (3 results)

  * ####  Log sink link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Logging, Security, Compliance, CSPR, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_5`

Details

Flags Google Cloud projects that do not have valid log sinks configured at any folder/org/project level.

  * ####  Logging bucket multi region link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Security, Logging, HighAvailability, BCDR

Asset: `logging.googleapis.com/LogBucket`

Details

Verifies that Cloud Logging buckets are configured in multi-regional or global locations (e.g., 'global', 'us', 'eu') to ensure high availability and resilience against regional outages. Regional log buckets are susceptible to data loss if the region experiences an outage.

  * ####  Logging sink not aggregated at folder or organization link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: logging, Security, CSPR

Asset: `logging.googleapis.com/LogSink`

Details

Identifies Folder or Organization level log sinks that are not configured as aggregated. Aggregated sinks are essential at Folder/Org level to centralize logs from all child projects and resources for security auditing and operations.




### Google Cloud Best Practices - Cloud Pub/Sub (7 results)

  * ####  Pub/Sub sub exponential backoff link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Pub/Sub, Subscription, Reliability, Resilience, CSPR

Asset: `pubsub.googleapis.com/Subscription`

Details

Verifies that Pub/Sub subscriptions are configured with an exponential backoff retry policy by checking for the presence of retryPolicy, minimumBackoff, and maximumBackoff settings. Implementing exponential backoff is crucial for system stability as it prevents subscriber failures from causing immediate, uncoordinated retry storms that can overwhelm the messaging system during transient outages.

  * ####  Pub/Sub subscription dead letter topic configured link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Messaging, DisasterRecovery, Resiliency

Asset: `pubsub.googleapis.com/Subscription`

Details

Ensure Pub/Sub subscriptions have a dead letter topic configured to isolate un-processable messages and prevent stream blocking.

  * ####  Pub/Sub subscription deadletter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Pub/Sub, Subscription, DeadLetter, Reliability, Messaging, ErrorHandling, CSPR

Asset: `pubsub.googleapis.com/Subscription`

Details

Checks if a Pub/Sub subscription has a deadletter topic configured. A deadletter topic (DLT) is essential for handling message delivery failures. When a message cannot be delivered to a subscriber after multiple attempts, it can be sent to a DLT, preventing message loss and allowing for analysis of delivery issues. This rule examines the deadLetterPolicy field within the subscriptions configuration. If deadLetterPolicy is missing or if it exists but does not have a deadLetterTopic field, the rule generates a violation. Using a DLT is a best practice for reliable message processing.

  * ####  Pub/Sub subscription retry policy configured link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Messaging, Resiliency

Asset: `pubsub.googleapis.com/Subscription`

Details

Ensure Pub/Sub subscriptions have custom retry policies configured with exponential backoff to handle transient failures gracefully.

  * ####  Pub/Sub topic message retention link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, DataProtection, Pub/Sub, CoNa

Asset: `pubsub.googleapis.com/Topic`

Details

Verifies that Pub/Sub topics have a message retention duration configured. Message retention ensures that messages are persisted for a specified period, guaranteeing availability even when subscribers are temporarily unavailable or for historical replay.

  * ####  Pub/Sub topic message Cloud Storage policy link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Security, Pub/Sub, DataResidency, Compliance, CoNa

Asset: `pubsub.googleapis.com/Topic`

Details

Verifies that Pub/Sub topics are configured with a message storage policy that restricts message persistence to specific regions. Restricting message storage to certified regions prevents compliance violations and ensures data residency requirements are respected.

  * ####  Pub/Sub topic schema link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: PubSub, Messaging, Schema, DataGovernance, Reliability

Asset: `pubsub.googleapis.com/Topic`

Details

Checks if Pub/Sub topics have a schema configured. Enforcing a schema ensures data quality and prevents malformed messages from breaking downstream consumers.




### Google Cloud Best Practices - Cloud Router (6 results)

  * ####  Compute router advertises all subnets link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Network, CloudRouter, Routing

Asset: `compute.googleapis.com/Router`

Details

Verifies that Cloud Routers are configured to advertise all subnets (either using DEFAULT advertisement mode or CUSTOM mode with ALL_SUBNETS group). This ensures that new subnets are automatically advertised to on-premises networks, preventing connectivity gaps.

  * ####  Compute router bfd enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, BGP, BFD, HighAvailability

Asset: `compute.googleapis.com/Router`

Details

Verifies that Bidirectional Forwarding Detection (BFD) is enabled on all BGP peers of a Cloud Router. BFD provides sub-second link failure detection to ensure fast BGP failover and high availability.

  * ####  Compute router bgp keepalive link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Network, BGP, Keepalive, HighAvailability

Asset: `compute.googleapis.com/Router`

Details

Verifies that BGP keepalive timer is configured to exactly 20 seconds on Cloud Router. A 20-second keepalive interval ensures timely peering failure detection and predictable BGP convergence.

  * ####  Compute router bgp peer redundancy link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, CloudRouter, BGP, Redundancy

Asset: `compute.googleapis.com/Router`

Details

Verifies that Cloud Routers have at least 2 BGP peers configured. Redundant BGP sessions ensure high availability and prevent routing disruptions during maintenance or network failures.

  * ####  Project multiregion routers link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, Router, HighAvailability, BCDR

Asset: `cloudresourcemanager_Project_RESOURCE_ROUTER`

Details

Verifies that a Project has Cloud Routers deployed across at least 2 different regions. Multi-regional Cloud Router deployment ensures hybrid networking redundancy (VPN, Interconnect, NAT) and protects against regional outages.

  * ####  Project regional routers redundancy link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, CloudRouter, Redundancy, HighAvailability

Asset: `cloudresourcemanager_Project_RESOURCE_ROUTER`

Details

Verifies that for each region where Cloud Routers are deployed in a Project, there are at least 2 Cloud Routers configured. Regional router redundancy ensures high availability for hybrid connectivity (VPN/Interconnect) and prevents single points of failure.




### Google Cloud Best Practices - Cloud Run (3 results)

  * ####  Run global load balancer ingress link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, High Availability, Networking, Cloud Run

Asset: `run.googleapis.com/Service`

Details

Ensures that Cloud Run services are configured to accept traffic only from Internal sources and Cloud Load Balancing. This restriction forces traffic through a Global External Load Balancer, which is a prerequisite for achieving the high availability, fault tolerance, and optimized latency of a multiregion architecture.

  * ####  Run service min instance link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Latency, Serverless, Cloud Run

Asset: `run.googleapis.com/Service`

Details

Ensures Cloud Run services configure a minimum number of instances greater than zero. This configuration is critical for latencysensitive applications to prevent cold starts and maintain immediate availability. The issue arises when the autoscaling.knative.dev/minScale annotation is missing (defaulting to 0) or explicitly set to 0.

  * ####  Run service no VPC egress link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudRun, Serverless, VPC, Networking, Security, Egress, CSPR, CoNa, MVSP

Asset: `run.googleapis.com/Service`

Details

Verifies if a Cloud Run service is configured to use Serverless VPC Access for egress traffic. Routing egress traffic through a VPC connector allows Cloud Run services to access internal resources securely and can be used to route traffic through Cloud NAT for a static outbound IP. A violation occurs if the run.googleapis.com/vpc-access-connector annotation is missing.




### Google Cloud Best Practices - Cloud SQL (35 results)

  * ####  Cloudsql backup multi region link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Backup

Asset: `sqladmin.googleapis.com/Instance`

Details

Verifies that Cloud SQL instance backups are configured for multi-region storage. By default, backups are stored in the same region as the instance, which does not provide protection against regional outages. Configuring multi-region storage ensures data availability and business continuity during such events.

  * ####  Cloudsql instance ca cert invalid link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: CloudSQL, Security, Certificate, Expiration, Reliability, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks the expiration status of the Certificate Authority (CA) certificate for Cloud SQL instances. Regularly rotating CA certificates and ensuring they are not expired is a critical security best practice. An expired CA certificate can disrupt client connections to the database, leading to application downtime. This rule checks two key things 1. If a CA certificate exists for the instance (indicating that SSL/TLS is likely configured, which is recommended). 2. If the existing CA certificates expiration time (expirationTime) is in the future. A violation is generated if either no CA certificate is found or if the found certificate is expired (its expirationTime is in the past). The rule uses the current time (obtained via time.now_ns()) to perform the expiration check. The time is converted to seconds since the epoch for comparison.

  * ####  Cloudsql instance deletion protection link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Database, Security, Reliability, Data Protection, CSPR, CoNa

Asset: `sqladmin.googleapis.com/Instance`

Details

Verifies that Cloud SQL instances have deletion protection enabled to prevent accidental deletion and potential data loss. When settings.deletionProtectionEnabled is set to false or not configured, the database is vulnerable to immediate removal by human error or automation scripts.

  * ####  Cloudsql instance maintenance window link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Operations, Maintenance, BCDR

Asset: `sqladmin.googleapis.com/Instance`

Details

Verifies that Cloud SQL instances have a maintenance window configured, ensuring system updates are scheduled during offpeak hours to minimize business impact and prevent unexpected downtime.

  * ####  Cloudsql instance pitr disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, Instance, Backup, PITR, Recovery, Reliability, DataProtection, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Verifies that Cloud SQL instances have PointinTime Recovery (PITR) enabled. PITR allows restoring the database to a specific point in time, providing crucial data recovery capabilities. This rule directly checks the pointInTimeRecoveryEnabled setting within the backupConfiguration. If pointInTimeRecoveryEnabled is false or not present, it indicates that PITR is not enabled.

  * ####  Cloudsql instance Cloud Storage autoresize link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, Instance, Storage, AutoResize, Reliability, Availability, Performance, Cost, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if Cloud SQL instances have automatic storage resizing enabled. Enabling storageAutoResize allows the instances storage capacity to automatically increase as needed, preventing potential outofstorage errors and downtime. Without automatic resizing, the instance can become unavailable if it runs out of storage space. This rule checks for the presence and value of the storageAutoResize setting within the instances configuration. If storageAutoResize is false or not present, it indicates that automatic storage resizing is disabled, which can lead to operational issues. Enabling this feature is crucial for maintaining the reliability and availability of the database.

  * ####  Cloudsql mysql local infile enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, MySQL, Instance, Security, Flags, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Enabling local_infile on Cloud SQL for MySQL can expose the server to file read exploits; disable it unless absolutely necessary.

  * ####  Cloudsql mysql skip show database link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, MySQL, Instance, Security, Flags, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Ensures the skip_show_database flag is enabled (set to on) for Cloud SQL for MySQL instances. Enabling this flag prevents users from using the SHOW DATABASES command unless they have the SHOW DATABASES privilege. This enhances security by limiting the ability of users to discover database names, reducing the risk of unauthorized access attempts and information disclosure. Its a form of security through obscurity.

  * ####  Cloudsql mysql slow query log disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, MySQL, Instance, Performance, Flags, Performance, Troubleshooting, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if the slow_query_log database flag is enabled (set to on) for Cloud SQL for MySQL instances. Enabling this flag activates the slow query log, which records SQL statements that exceed a defined execution time threshold (controlled by long_query_time). The slow query log is an essential tool for identifying performance bottlenecks, optimizing queries, and troubleshooting database performance issues. Disabling this flag hinders your ability to diagnose and resolve slow query problems.

  * ####  Cloudsql no auto backup link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, BCDR, DataProtection, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Verifies that Cloud SQL instances have automated backups enabled, ensuring that critical data can be recovered in the event of corruption, deletion, or service failure. Disabling automated backups eliminates the ability to perform pointintime recovery.

  * ####  Cloudsql password policy not enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: CloudSQL, Instance, Security, Password, Reliability, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Verifies that Cloud SQL instances have a password validation policy enabled. For security best practices, it is strongly recommended to set a Password Validation Policy. Relying on default or not setting the password validation, significantly increases the risk of unauthorized access and potential data breaches. This rule checks for the absence of password validation. If password validation is not enforced for Instance, it indicates a potential security vulnerability.

  * ####  Cloudsql pgsql log checkpoints link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Reliability, Performance, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Ensures that the log_checkpoints database flag is enabled (set to on) for Cloud SQL for PostgreSQL instances. Checkpoints are critical points in the transaction log sequence where PostgreSQL writes all dirty data buffers to disk and updates the control file. Logging checkpoints provides valuable information for monitoring database recovery time, diagnosing performance issues related to I/O, and understanding write activity. Disabling this flag can hinder troubleshooting and recovery analysis.

  * ####  Cloudsql pgsql log connections disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Instance, Logging, Flags, Security, Troubleshooting, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if the log_connections database flag is enabled (set to on) for Cloud SQL for PostgreSQL instances. When enabled, this flag logs each successful connection attempt to the database server, including the username and client IP address. This information is crucial for security auditing, tracking database access, and troubleshooting connectionrelated issues. It complements the log_disconnections flag, which logs the end of sessions. This rule flags instances where connection logging is disabled.

  * ####  Cloudsql pgsql log disconnections disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Instance, Logging, Flags, Security, Troubleshooting, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if the log_disconnections database flag is enabled (set to on) for Cloud SQL for PostgreSQL instances. When enabled, this flag logs the end of each client session, including the session duration. This information is valuable for auditing, security analysis (e.g., detecting unusual connection patterns), and troubleshooting connectionrelated issues. It complements the log_connections flag, which logs the start of connections. This rule flags instances where disconnection logging is disabled.

  * ####  Cloudsql pgsql log error verbosity link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Instance, Logging, Flags, Troubleshooting, Debugging, Reliability, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Ensures that the log_error_verbosity database flag for Cloud SQL for PostgreSQL instances is set to either default or verbose. This flag controls the amount of detail included in error messages written to the server log. Setting it to default or verbose provides more information for troubleshooting and debugging compared to the terse setting, which minimizes detail. More verbose error logs can significantly aid in diagnosing the root cause of database problems.

  * ####  Cloudsql pgsql log hostname link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Instance, Logging, Troubleshooting, Security, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Ensures that the log_hostname database flag is enabled (set to on) for Cloud SQL for PostgreSQL instances. When enabled, this flag logs the hostnames of connecting clients in addition to their IP addresses. Logging hostnames can be valuable for troubleshooting, security auditing, and identifying the source of connections. This can be particularly helpful in environments where IP addresses change frequently (e.g., due to DHCP) or where multiple clients connect from the same IP address (e.g., through a proxy or NAT). However, enabling this can introduce a slight performance overhead due to the hostname.

  * ####  Cloudsql pgsql log lock waits link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, Performance, Reliability, PostgreSQL, Instance, Logging, Flags, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Ensures that the log_lock_waits database flag is enabled (set to on) for Cloud SQL for PostgreSQL instances. Enabling this flag logs long lock waits, which are often indicative of performance bottlenecks or concurrency issues within the database. By monitoring these logs, administrators can identify and address the root causes of slow queries or application performance problems. This proactive approach helps maintain database health and responsiveness.

  * ####  Cloudsql pgsql log min duration disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Instance, Logging, Flags, Performance, Troubleshooting, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if the log_min_duration_statement database flag is set to 1 (disabled) on Cloud SQL for PostgreSQL instances. This flag controls the minimum execution time (in milliseconds) a statement must take before its logged. Setting it to 1 disables logging of statement durations, hindering performance monitoring and troubleshooting. Its generally recommended to set a specific threshold (e.g., 2000 for 2 seconds) to capture slow queries without overwhelming the logs. This rule flags instances where durationbased statement logging is disabled.

  * ####  Cloudsql pgsql log min error too high link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Instance, Logging, Flags, Troubleshooting, Security, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if the log_min_error_statement database flag is set to error, log, fatal, or panic for Cloud SQL for PostgreSQL instances. This flag controls the severity level of SQL statements that are logged as errors. Setting it to error or a stricter level (log, fatal, panic) ensures that all errorcausing statements are logged, which is crucial for troubleshooting, auditing, and security analysis. Settings less strict than error (e.g., warning, notice) may not capture all error conditions, hindering your ability to diagnose and resolve problems. This rule flags instances with a setting less strict than error.

  * ####  Cloudsql pgsql log min messages non default link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Instance, Logging, Flags, Logging, Troubleshooting, Reliability, CSPR, CoNa

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if the log_min_messages database flag is set to its default value (warning) for Cloud SQL for PostgreSQL instances. This flag controls the severity level of messages that are written to the server log. While the default (warning) is generally appropriate, its often recommended to adjust this setting based on your specific operational needs and the desired level of logging detail. Setting it to a more verbose level (e.g., notice, info, debug) can provide more information for troubleshooting, while setting it to a less verbose level (e.g., error, log, fatal, panic) can reduce log volume. This rule flags instances where the setting is not the default (warning). Its a policy decision whether to enforce the default or allow deviations.

  * ####  Cloudsql pgsql log statement link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Instance, Logging, Flags, Troubleshooting, Performance, Security, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Verifies that the log_statement database flag is configured to a value other than none for Cloud SQL for PostgreSQL instances. The log_statement flag controls which SQL statements are logged. Appropriate logging of SQL statements is crucial for auditing, security analysis, performance troubleshooting, and debugging. Setting it to values like ddl, mod, or all (depending on your needs) provides valuable insights into database activity. A setting of none disables statement logging entirely, hindering these important capabilities.

  * ####  Cloudsql pgsql log temp files link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Instance, Logging, Flags, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Ensures that the log_temp_files database flag is enabled (set to a nonzero value) for Cloud SQL for PostgreSQL instances. This flag controls the logging of temporary file usage. Setting it to a value other than 0 (which disables logging) allows you to monitor the size and number of temporary files created by queries. Excessive temporary file creation can indicate inefficient queries, poorly tuned work_mem settings, or potential performance bottlenecks. Analyzing these logs can help optimize query performance and resource utilization. A value of 0 disables logging, while positive values indicate a threshold in KB.

  * ####  Cloudsql pgsql max connections link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, Reliability, Performance, SQL, PostgreSQL, Instance, Connections, Flags, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Ensures that the max_connections database flag is explicitly configured for Cloud SQL for PostgreSQL instances. Setting an appropriate value for max_connections is crucial for resource management and preventing connection exhaustion. Without a defined limit, a surge in connection requests could overwhelm the database, leading to performance degradation or denial of service. The optimal value depends on the instance size and workload.

  * ####  Cloudsql pgsql pgaudit disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, PostgreSQL, Instance, Auditing, Flags, Security, Auditing, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if the cloudsql.enable_pgaudit flag is enabled (set to on) for Cloud SQL for PostgreSQL instances. This flag enables the pgaudit extension, which provides detailed session and object audit logging capabilities. pgaudit allows you to track specific database activities, such as SELECT, INSERT, UPDATE, and DELETE operations, and to configure granular auditing rules based on users, roles, and objects. This is crucial for security auditing, compliance, and forensic analysis.

  * ####  Cloudsql public access link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: CloudSQL, Instance, Security, Networking, CSPR, MVSP

Asset: `sqladmin.googleapis.com/Instance`

Details

Detects Cloud SQL instances that are configured to allow connections from any IP address (0.0.0.0/0) in their authorized networks. Exposing a database instance to the public internet is a critical security risk and should be avoided unless absolutely necessary and with extreme caution. Public accessibility dramatically increases the attack surface, making the instance vulnerable to unauthorized access, bruteforce attacks, and data breaches. Access should be restricted to specific, known IP addresses or ranges.

  * ####  Cloudsql require ssl link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: CloudSQL, Instance, Security, SSL, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Enforces the use of SSL/TLS connections for all clients connecting to this Cloud SQL instance. Requiring SSL/TLS encrypts data in transit, protecting against eavesdropping and maninthemiddle attacks. This is a critical security best practice for any database handling sensitive information. Without SSL/TLS, data is transmitted in plain text.

  * ####  Cloudsql root password not set link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: CloudSQL, Instance, Security, Password, Reliability, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if a root password is set for Cloud SQL instances. For security best practices, a strong, unique root password should be set for all Cloud SQL instances. This rule directly checks the rootPassword field within the instance configuration. An empty or missing rootPassword field indicates a significant security vulnerability, as it means the instance can be accessed without a password or with a default password.

  * ####  Cloudsql server contained database auth enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, SQL Server, Instance, Security, Authentication, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if contained database authentication is enabled on Cloud SQL for SQL Server instances. Contained databases allow authentication at the database level, rather than solely at the instance (server) level. While this can simplify database portability, it also introduces potential security risks if not carefully managed. Users authenticated to a contained database may bypass instancelevel security controls. Its generally recommended to disable contained database authentication unless specifically required and with a thorough understanding of the security implications.

  * ####  Cloudsql server cross database owner chain link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, Reliability, SQL Server, Instance, Security, Ownership Chaining, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Ensures that cross db ownership chaining is disabled (set to off) on Cloud SQL for SQL Server instances. Disabling this setting is a crucial security best practice. When enabled, it can allow users in one database to potentially gain unintended access to objects in other databases if ownership chains are not carefully managed. This can lead to privilege escalation vulnerabilities.

  * ####  Cloudsql server ext scripts enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, SQL Server, Instance, Security, Flags, Security, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if the external scripts enabled flag is enabled on Cloud SQL for SQL Server instances. This flag controls the ability to execute external scripts (e.g., R, Python) within the SQL Server environment. While this feature can be useful for advanced analytics and machine learning, enabling it introduces potential security risks if not carefully managed. External scripts can potentially access system resources or execute malicious code. Its generally recommended to disable this feature unless specifically required and with appropriate security precautions in place.

  * ####  Cloudsql server remote access link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, SQL Server, Instance, Security, Access Control, Reliability, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Ensures that the remote access database flag is disabled (set to off) on Cloud SQL for SQL Server instances. Disabling this flag prevents SQL Server clients on remote machines from connecting to this instance using the Dedicated Administrator Connection (DAC). While the DAC is a powerful troubleshooting tool, restricting its use to local connections only significantly reduces the attack surface. Misconfigured or compromised remote access can lead to unauthorized database control.

  * ####  Cloudsql server traceflag 3625 enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, SQL Server, Instance, Security, Reliability, Security, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if trace flag 3625 is enabled on Cloud SQL for SQL Server instances. Trace flag 3625 limits the amount of information returned to nonsysadmin users in error messages, potentially masking sensitive details about the database structure or configuration. While useful in some security contexts, this trace flag is often disabled in development and testing environments to provide more detailed error information for troubleshooting. This rule flags instances where trace flag 3625 is enabled. Its important to understand the implications of this flag and whether it aligns with your security and operational needs.

  * ####  Cloudsql server unlimited user conn link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, SQL Server, Instance, Connections, Flags, Performance, Reliability, CSPR

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if the user connections database flag is set to 0 (unlimited) on Cloud SQL for SQL Server instances. Setting user connections to 0 allows an unlimited number of simultaneous user connections, which can lead to resource exhaustion, performance degradation, and potential denialofservice. Its a best practice to configure a specific, reasonable limit for user connections based on the instance size and expected workload to prevent resource contention and maintain database stability. This rule flags instances where the connections are unlimited.

  * ####  Cloudsql server user options set link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudSQL, SQL Server, Instance, Configuration, Flags, Reliability, CSPR, CoNa

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if the user options database flag is configured on Cloud SQL for SQL Server instances. The user options flag specifies serverwide default settings for query processing behavior for all users. Its generally recommended to avoid setting global user options and instead allow individual users or applications to configure their own sessionlevel settings as needed. Relying on global user options can lead to unexpected behavior or compatibility issues if different applications require different settings. This rule flags instances where user options is set (i.e., not its default, unconfigured state, typically represented by 0 or an empty string).

  * ####  Cloudsql zonal instance failover replica link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: CloudSQL, Instance, Reliability, Availability, HA, Zonal, Failover, CSPR, CoNa

Asset: `sqladmin.googleapis.com/Instance`

Details

Checks if a Cloud SQL instance is configured for high availability (HA). This rule focuses on zonal instances (nonregional) and verifies whether a failover replica is available. For zonal instances, having a failover replica is critical for resilience. If failoverReplicaAvailable is false for a zonal instance, it means that the instance is a single point of failure and is vulnerable to outages within that zone. A zonal instance without a failover replica does not meet the requirements for high availability. This is considered a high severity issue because it directly impacts the reliability and uptime of the database.




### Google Cloud Best Practices - Cloud Spanner (6 results)

  * ####  Spanner database backup age link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Spanner, Backup, Security, CSPR

Asset: `spanner.googleapis.com/Backup`

Details

Verifies that Cloud Spanner backups are older than their minimum retention period.

  * ####  Spanner database no CMEK link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Spanner, Security, Encryption, CMEK, CSPR, MVSP

Asset: `spanner.googleapis.com/Database`

Details

Verifies that Cloud Spanner databases are encrypted using Customer-Managed Encryption Keys (CMEK) rather than Google-managed keys.

  * ####  Spanner database pitr enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Database, Backup, Recovery, BCDR

Asset: `spanner.googleapis.com/Database`

Details

Ensure Spanner databases have Point-in-Time Recovery (PITR) configured by verifying the version retention period is set to a non-default duration.

  * ####  Spanner database drop protection disabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Reliability, Data Protection, CSPR

Asset: `spanner.googleapis.com/Database`

Details

Enforces drop protection on Cloud Spanner databases to safeguard against accidental deletion, which can lead to irreversible data loss and significant service disruption. This rule checks if the enableDropProtection flag is missing or explicitly set to false, which leaves the database vulnerable to unintended removal.

  * ####  Spanner instance insufficient capacity link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Performance, Capacity Management, CSPR

Asset: `spanner.googleapis.com/Instance`

Details

Verifies that Cloud Spanner instances are provisioned with at least 1 node or 1000 processing units, ensuring adequate capacity for production workloads to prevent latency and throttling. Instances with lower capacity may struggle during traffic spikes, impacting application reliability.

  * ####  Spanner instance multi region link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Availability, BCDR, CSPR

Asset: `spanner.googleapis.com/Instance`

Details

Verifies that Cloud Spanner instances are configured with a multiregion instance configuration to ensure 99.999% availability and high resilience against regional outages. Instances configured with singleregion configurations (identified by the regional prefix in the config setting) do not meet this availability standard.




### Google Cloud Best Practices - Cloud Storage (20 results)

  * ####  Cloud Storage bucket soft delete policy enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Storage, Backup, DataProtection

Asset: `storage.googleapis.com/Bucket`

Details

Verify that Google Cloud Storage buckets have a soft delete policy enabled to protect against accidental or malicious object deletions.

  * ####  Cloud Storage bucket turbo replication link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Storage, Replication, DisasterRecovery, BCDR

Asset: `storage.googleapis.com/Bucket`

Details

Verify that GCS dual-region buckets have Turbo Replication enabled to guarantee a 15-minute RPO under the Google Cloud SLA.

  * ####  Cloud Storage bucket abort incomplete multipart upload link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: CloudStorage, Lifecycle, CostOptimization

Asset: `storage.googleapis.com/Bucket`

Details

Checks if Cloud Storage buckets have a lifecycle rule configured to abort incomplete multipart uploads. Incomplete uploads consume storage space and incur costs indefinitely if not cleaned up.

  * ####  Cloud Storage bucket CMEK rotation link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Asset: `storage_Bucket_RESOURCE_RELATIONSHIP`

Details

Ensure Cloud Storage buckets are encrypted with a customer-managed encryption key (CMEK) that has a rotation period of <= 90 days.

  * ####  Cloud Storage bucket dual multi region link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Bucket, Availability, Resilience, DisasterRecovery

Asset: `storage.googleapis.com/Bucket`

Details

Verifies that Cloud Storage buckets are configured with dual-region or multi-region location types. This configuration ensures high availability and data resilience by distributing data across multiple geographic locations. A region location type leaves data vulnerable to single-region outages and does not meet high-availability requirements.

  * ####  Cloud Storage bucket empty lifecycle link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Storage, Bucket, Lifecycle, Reliability, Cost, CSPR, CoNa

Asset: `storage.googleapis.com/Bucket`

Details

Identifies Cloud Storage buckets that have lifecycle rules defined, but where those rules are missing a specified action. A lifecycle rule without an action is ineffective and serves no purpose. Lifecycle rules are designed to manage object lifecycle through actions like deletion or storage class transitions. An empty action indicates a configuration error that should be corrected. This could be a sign of an incomplete setup or a typo in the configuration.

  * ####  Cloud Storage bucket gdpr link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Storage, Bucket, GDPR, Compliance, Location, EU, DataResidency, CSPR

Asset: `storage.googleapis.com/Bucket`

Details

Checks if a Google Cloud Storage bucket is located outside of the European Union (EU) geographical boundaries. For organizations subject to GDPR or similar data residency regulations, storing data in compliant locations is critical. This rule identifies buckets where the location field does not correspond to an EU multiregion (EU) or a specific EU region (typically starting with EUROPE). Buckets found outside the EU region might require review for compliance.

  * ####  Cloud Storage bucket logging enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Storage, Bucket, Logging, Security, Audit, CSPR, CoNa, MVSP

Asset: `storage.googleapis.com/Bucket`

Details

Checks if logging is enabled for the Cloud Storage bucket. Access logging provides detailed records of requests made to the bucket, which is important for security auditing and monitoring access to sensitive data.

  * ####  Cloud Storage bucket missing classification label link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Storage, Bucket, Labels, DataGovernance, Classification, Security, CSPR, CoNa

Asset: `storage.googleapis.com/Bucket`

Details

Verifies that the Cloud Storage bucket has a 'classification' label configured. Classification labels (e.g., public, private, confidential) are crucial for data governance and applying appropriate security controls.

  * ####  Cloud Storage bucket missing labels link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Storage, Bucket, Labels, Organization, FinOps, CSPR, CoNa

Asset: `storage.googleapis.com/Bucket`

Details

Ensures Cloud Storage buckets have labels applied for resource organization, cost allocation, and policy enforcement.

  * ####  Cloud Storage bucket missing owner label link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Storage, Bucket, Labels, Owner, Security, CSPR, CoNa

Asset: `storage.googleapis.com/Bucket`

Details

Verifies that the Cloud Storage bucket has an 'owner' label configured. Labeling resources with owners helps in accountability, cost allocation, and resource management.

  * ####  Cloud Storage bucket multi region link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Storage, MultiRegion, HighAvailability, BCDR

Asset: `storage.googleapis.com/Bucket`

Details

Verifies that Cloud Storage buckets are configured to use a multi-region or dual-region location to ensure maximum availability, data redundancy, and protection against regional service outages. Single-region buckets do not meet this high availability standard.

  * ####  Cloud Storage bucket no CMEK link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Storage, Bucket, Encryption, CMEK, Security, CSPR

Asset: `storage.googleapis.com/Bucket`

Details

Checks if a Cloud Storage bucket is encrypted using a CustomerManaged Encryption Key (CMEK). Using CMEKs provides greater control over your data encryption keys compared to Googlemanaged encryption. With CMEKs, you manage the key lifecycle, including rotation, access control, and auditing, within Cloud KMS. This is often a requirement for regulatory compliance or enhanced security postures where you need direct control over your encryption keys. If a bucket is not using a CMEK, its using Googlemanaged encryption by default.

  * ####  Cloud Storage bucket publicly exposed link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Tags: Security, Storage, IAM, CSPR, CoNa, MVSP

Asset: `storage.googleapis.com/Bucket`

Details

Detects if a Cloud Storage bucket is publicly accessible. Public buckets allow any user on the internet to read or write data, which represents a severe data leak risk.

  * ####  Cloud Storage bucket versioned no lifecycle cleanup link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: CloudStorage, Storage, Bucket, Cost, Reliability, CSPR, CoNa, MVSP

Asset: `storage.googleapis.com/Bucket`

Details

Verifies if a Cloud Storage bucket with Object Versioning enabled also has a Lifecycle rule to clean up noncurrent versions. Enabling versioning without a lifecycle rule can lead to infinite storage cost growth as older versions are never deleted. A violation occurs if versioning.enabled is true, but no lifecycle rule has the 'Delete' action combined with a 'daysSinceNoncurrentTime' condition.

  * ####  Cloud Storage bucket versioning disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Storage, Bucket, Versioning, Reliability, Recovery, CSPR, CoNa

Asset: `storage.googleapis.com/Bucket`

Details

Checks if object versioning is enabled for the Cloud Storage bucket. Object versioning preserves previous versions of an object when its overwritten or deleted, providing a crucial safeguard against accidental data loss or corruption. With versioning enabled, you can restore earlier versions of objects if needed. Disabling versioning means that overwrites and deletions are permanent.

  * ####  Cloud Storage public access prevention link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Security, Storage, Compliance, CSPR, CoNa, MVSP

Asset: `storage.googleapis.com/Bucket`

Details

Checks if Public Access Prevention (PAP) is enforced on Cloud Storage buckets. Enabling PAP prevents buckets from being made public via IAM policies or ACLs, protecting sensitive data from accidental exposure to the internet.

  * ####  Cloud Storage retention policy not locked link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Storage, Bucket, Retention, Policy, Lock, Compliance, DataLoss, DataGovernance, CSPR, CoNa

Asset: `storage.googleapis.com/Bucket`

Details

Checks if a Google Cloud Storage bucket has a retention policy configured and if that policy is locked. A retention policy specifies a minimum duration that objects in the bucket must be retained. Locking the retention policy makes it permanent and immutable, preventing accidental or malicious deletion or modification of the policy. This rule checks for two conditions 1. If a retention policy (retentionPolicy) is not configured on the bucket. 2. If a retention policy is configured, but it is not locked (retentionPolicy.isLocked is false or missing). If either of these conditions is true, the rule generates a violation. Having an unlocked retention policy, or no policy at all, can increase the risk of data loss or tampering. A locked retention policy is crucial for compliance and data governance.

  * ####  Cloud Storage retention policy undefined link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Storage, Bucket, Retention, Policy, Lock, Compliance, DataLoss, DataGovernance, CSPR, CoNa

Asset: `storage.googleapis.com/Bucket`

Details

Checks if a Google Cloud Storage bucket has a retention policy configured and if that policy is locked. A retention policy specifies a minimum duration that objects in the bucket must be retained. Locking the retention policy makes it permanent and immutable, preventing accidental or malicious deletion or modification of the policy. This rule checks for two conditions 1. If a retention policy (retentionPolicy) is not configured on the bucket. 2. If a retention policy is configured, but it is not locked (retentionPolicy.isLocked is false or missing). If either of these conditions is true, the rule generates a violation. Having an unlocked retention policy, or no policy at all, can increase the risk of data loss or tampering. A locked retention policy is crucial for compliance and data governance.

  * ####  Cloud Storage uniform bucket access link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Storage, Bucket, Security, CSPR

Asset: `storage.googleapis.com/Bucket`

Details

Checks if Uniform BucketLevel Access (UBLA) is enabled for the Cloud Storage bucket. Enabling UBLA provides a simplified and consistent way to manage permissions using IAM roles at the bucket level, rather than managing individual object ACLs. This is generally recommended for improved security and manageability. With UBLA, you only use IAM to control access, making permissions easier to audit and understand. Disabling UBLA means you are relying on a combination of IAM and object ACLs, which can become complex and difficult to manage.




### Google Cloud Best Practices - Cloud VPN (4 results)

  * ####  Compute vpn tunnel bgp enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Network, VPN, BGP, Routing

Asset: `compute.googleapis.com/VpnTunnel`

Details

Verifies that Compute Engine VPN Tunnels have BGP routing enabled (i.e., they are associated with a Cloud Router). Static routing for VPN tunnels lacks dynamic failover capabilities and is not recommended for high-availability production workloads.

  * ####  Compute vpngateway ha link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: VPN, Networking, HighAvailability, Reliability

Asset: `compute.googleapis.com/TargetVpnGateway`

Details

Checks if Cloud VPN Gateways are using the deprecated Classic VPN (TargetVpnGateway) instead of High Availability (HA) VPN. Classic VPN does not provide a 99.99% SLA.

  * ####  Project multiregion vpngateways link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, VPN, HighAvailability, BCDR

Asset: `cloudresourcemanager_Project_RESOURCE_VPNGATEWAY`

Details

Verifies that a Project has VPN Gateways deployed across at least 2 different regions. Multi-regional VPN Gateway deployment ensures hybrid networking redundancy and protects against regional outages.

  * ####  Project regional vpntunnels link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, VPN, HighAvailability, BCDR

Asset: `cloudresourcemanager_Project_RESOURCE_VPNTUNNEL`

Details

Verifies that for each region where VPN Tunnels are deployed in a Project, there are at least 2 VPN Tunnels configured. Regional VPN tunnel redundancy ensures 99.99% SLA compliance, seamless failover, and robust hybrid connectivity.




### Google Cloud Best Practices - Composer (1 results)

  * ####  Composer environment scheduler ha link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, High Availability, Composer, Airflow, CoNa

Asset: `composer.googleapis.com/Environment`

Details

Verifies that Cloud Composer environments are configured with at least two Airflow schedulers to ensure high availability. Running with a single scheduler poses a risk of workflow disruption during failures or maintenance.




### Google Cloud Best Practices - Compute Engine (95 results)

  * ####  Autoscaler min replicas redundant link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Compute, Autoscaling, HighAvailability

Asset: `compute.googleapis.com/Autoscaler`

Details

Validates that Compute Engine Autoscalers have minNumReplicas configured to at least 2 to ensure redundant instance availability during scale-down events.

  * ####  Compute address network tier link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, NetworkTier, IPAddress, Performance

Asset: `compute.googleapis.com/Address`

Details

Verifies that External IP Addresses are configured to use the Premium Network Tier. Premium Network Tier routes traffic over Google's global backbone network rather than the public internet, ensuring high availability, lower routing hops, and superior performance.

  * ####  Compute autonetworks enabled link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Compute, Network, VPC, AutoMode, Subnets, Networking, Configuration, CSPR

Asset: `compute.googleapis.com/Network`

Details

Checks if a Compute Engine VPC network has the autoCreateSubnetworks feature enabled. Automode VPC networks automatically create a subnet in each Google Cloud region, which might not align with desired network segmentation or IP address management strategies. While convenient for setup, custommode VPCs offer more granular control. This rule identifies networks where autoCreateSubnetworks is explicitly set to true. It is often recommended to use custommode VPC networks for better control and security posture.

  * ####  Compute avoid target pools link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, LoadBalancing, Legacy, Migration, Reliability, CSPR, CoNa

Asset: `compute.googleapis.com/TargetPool`

Details

Detects the usage of legacy Compute Engine Target Pools. Target Pools are deprecated for modern load balancing scenarios in favor of Backend Services, which offer superior health checking, autoscaling, and multiregion capabilities. The presence of a Target Pool indicates a legacy configuration that should be migrated to ensure application reliability and feature parity.

  * ####  Compute backend service logging link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, BackendService, Logging, Security, Auditing, Monitoring, LoadBalancing, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/BackendService`

Details

Checks if logging is enabled for a Compute Engine Backend Service. Backend service logging records requests processed by the load balancer, providing essential visibility for monitoring traffic, troubleshooting errors, security analysis, and auditing. This rule examines the logConfig field within the backend services configuration. A violation is generated if logConfig is missing, or if logConfig.enable is missing or if its set to false.

  * ####  Compute backend service no health check link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Compute, LoadBalancing, CoNa

Asset: `compute.googleapis.com/BackendService`

Details

Detects Load Balancer Backend Services that do not have health checks configured. Health checks are critical for routing traffic away from unhealthy instances to prevent service outages.

  * ####  Compute be bucket cdn link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Compute, BackendBucket, CDN, Performance, Caching, CSPR

Asset: `compute.googleapis.com/BackendBucket`

Details

Checks if Cloud CDN is enabled for a Compute Engine backend bucket. Cloud CDN caches content closer to users, improving performance and reducing origin server load. This rule examines the enableCDN field within the backend buckets configuration. If enableCDN is false or missing, it indicates that Cloud CDN is not enabled, and a violation is generated.

  * ####  Compute be bucket edge security policy link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, BackendBucket, Security, EdgeSecurityPolicy, CloudArmor, External, CSPR

Asset: `compute.googleapis.com/BackendBucket`

Details

Checks if an Edge Security Policy is associated with a Compute Engine backend bucket. Edge Security Policies (part of Cloud Armor) provide advanced security features, such as DDoS protection and WAF, for globally distributed applications. For backend buckets serving content through an external load balancer, associating an Edge Security Policy is a security best practice. This rule checks for the presence of the edgeSecurityPolicy field within the backend buckets configuration. If edgeSecurityPolicy is missing or null, it indicates that no Edge Security Policy is associated, and a violation is generated.

  * ####  Compute be connection drain link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, BackendService, Reliability, Availability, LoadBalancing

Asset: `compute.googleapis.com/BackendService`

Details

Checks if Connection Draining is enabled for Compute Engine Backend Services. Connection draining minimizes interruption to users by keeping existing connections open for a specified duration when instances are removed or become unhealthy. This rule checks if connectionDraining.drainingTimeoutSec is set to a value greater than 0.

  * ####  Compute be regional service ext sec policy link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, RegionBackendService, Security, LoadBalancing, External, SecurityPolicy, CSPR

Asset: `compute.googleapis.com/RegionBackendService`

Details

Checks if a regional external Compute Engine backend service has a security policy configured. For external load balancers, its crucial to have a Security Policy to protect against threats. This rule checks the following 1. loadBalancingScheme Verifies that the backend service is used for external load balancing. It checks for both EXTERNAL and EXTERNAL_MANAGED. 2. securityPolicy Checks if a Security Policy is configured. Backend services use securityPolicy, not edgeSecurityPolicy. A violation is generated if the loadBalancingScheme indicates an external service and the securityPolicy is either missing or null.

  * ####  Compute be regional service insecure protocol http link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, RegionBackendService, Security, Protocol, Encryption, HTTP, TCP, HTTPS, CSPR

Asset: `compute.googleapis.com/RegionBackendService`

Details

Checks if a Compute Engine Backend Service is configured to use the unencrypted HTTP or TCP protocols. Using plain HTTP or TCP for backend connections can expose application traffic, including potentially sensitive data, on the internal network. It is strongly recommended to use secure protocols like HTTPS, SSL, or HTTP/2, or appropriate proxy protocols (such as TCP_PROXY) to ensure data confidentiality and integrity. This rule flags backend services where the protocol field is set to HTTP or TCP.

  * ####  Compute be regional service insecure protocol tcp link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, RegionBackendService, Security, Protocol, Encryption, HTTP, TCP, HTTPS, CSPR

Asset: `compute.googleapis.com/RegionBackendService`

Details

Checks if a Compute Engine Backend Service is configured to use the unencrypted HTTP or TCP protocols. Using plain HTTP or TCP for backend connections can expose application traffic, including potentially sensitive data, on the internal network. It is strongly recommended to use secure protocols like HTTPS, SSL, or HTTP/2, or appropriate proxy protocols (such as TCP_PROXY) to ensure data confidentiality and integrity. This rule flags backend services where the protocol field is set to HTTP or TCP.

  * ####  Compute be service cdn link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Compute, BackendService, CDN, Performance, Caching, CSPR

Asset: `compute.googleapis.com/BackendService`

Details

Checks if Cloud CDN is enabled for a Compute Engine backend service. Cloud CDN caches content closer to users, improving performance and reducing origin server load. This rule examines the enableCDN field within the backend services configuration. If enableCDN is false or missing, it indicates that Cloud CDN is not enabled, and a violation is generated.

  * ####  Compute be service ext sec policy link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, BackendService, Security, LoadBalancing, External, SecurityPolicy, CSPR

Asset: `compute.googleapis.com/BackendService`

Details

Checks if an external Compute Engine backend service has a security policy configured. For external load balancers, its crucial to have a Security Policy to protect against threats. This rule checks the following 1. loadBalancingScheme Verifies that the backend service is used for external load balancing. It checks for both EXTERNAL and EXTERNAL_MANAGED. 2. securityPolicy Checks if a Security Policy is configured. Backend services use securityPolicy, not edgeSecurityPolicy. A violation is generated if the loadBalancingScheme indicates an external service and the securityPolicy is either missing or null.

  * ####  Compute be service iap over http link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, BackendService, IAP, Security, Encryption, HTTP, HTTPS, CSPR

Asset: `compute.googleapis.com/BackendService`

Details

Checks if a Compute Engine Backend Service has IdentityAware Proxy (IAP) enabled while using the unencrypted HTTP protocol. Enabling IAP adds authentication and authorization, but if the connection between the load balancer and the backend service uses plain HTTP, the traffic (including potentially sensitive application data or session information) is unencrypted on the internal network. This poses a security risk. This rule checks if iap.enabled is true AND protocol is HTTP. It is strongly recommended to use HTTPS for backend services when IAP is enabled to ensure endtoend encryption.

  * ####  Compute be service insecure protocol link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, BackendService, Security, Protocol, Encryption, HTTP, TCP, HTTPS, CSPR

Asset: `compute.googleapis.com/BackendService`

Details

Checks if a Compute Engine Backend Service is configured to use the unencrypted HTTP or TCP protocols. Using plain HTTP or TCP for backend connections can expose application traffic, including potentially sensitive data, on the internal network. It is strongly recommended to use secure protocols like HTTPS, SSL, or HTTP/2, or appropriate proxy protocols (such as TCP_PROXY) to ensure data confidentiality and integrity. This rule flags backend services where the protocol field is set to HTTP or TCP.

  * ####  Compute cloud armor attached link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Security, Compute, Network, Cloud Armor, Compliance, CSPR

Asset: `compute_Instance_RESOURCE_7`

Details

Flags Compute Engine VM instances with public IPs that do not have Cloud Armor attached.

  * ####  Compute default service account used link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Security, Service Account, Security, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Detects Compute Engine instances that are using the default Compute Engine service account. The default service account is automatically created and has broad permissions (Editor role) by default, which violates the principle of least privilege. Its a security best practice to create and use custom service accounts with the minimum necessary permissions for each instance. Using the default service account increases the risk of unauthorized access and privilege escalation if an instance is compromised.

  * ####  Compute disk csek disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Disk, Encryption, CSEK, Security, sha256, CSPR

Asset: `compute.googleapis.com/Disk`

Details

Checks if a Compute Engine disk is encrypted using CustomerSupplied Encryption Keys (CSEK). With CSEK, you provide your own encryption key, and Google Cloud uses that key, represented by its SHA256 hash, to protect your data. This rule examines the diskEncryptionKey field and, specifically, the sha256 field within it. If diskEncryptionKey is missing, or if sha256 is missing, empty, or null, it signifies that CSEK is not in use, triggering a violation.

  * ####  Compute disk database hdd link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Performance, Compute, Disk, Storage, CoNa

Asset: `compute.googleapis.com/Disk`

Details

Detects persistent disks of type 'pd-standard' (HDD) that are attached to VM instances configured as databases. Databases require high IOPS and low latency, which standard HDDs cannot provide, leading to performance bottlenecks.

  * ####  Compute disk no snapshot schedule link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Compute, Disk, Backup, CoNa

Asset: `compute.googleapis.com/Disk`

Details

Detects Compute Engine persistent disks that do not have any snapshot schedule policies attached. Snapshot schedules automate backing up disk data, which is essential for disaster recovery and preventing data loss.

  * ####  Compute disk regional check link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, High Availability, Compute, Disk, Storage

Asset: `compute.googleapis.com/Disk`

Details

Ensure Compute Engine persistent disks are configured as Regional Persistent Disks to provide high availability and protect against zonal outages. Regional disks synchronously replicate data between two zones in the same region, ensuring accessibility even if a specific zone becomes unavailable. This rule checks if the replicaZones field lists multiple zones.

  * ####  Compute firewall all protocols internet link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/Firewall`

Details

A firewall rule permitting internet traffic on all protocols significantly broadens the network attack surface, increasing the risk of unauthorized access, potential service disruptions, and costly security incidents.

  * ####  Compute firewall logging link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Firewall, VPC, Logging, Security, Auditing, Network, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/Firewall`

Details

Checks if logging is enabled for a VPC Firewall rule. Firewall Rules Logging records connections that match the rule, providing valuable insights for security auditing, troubleshooting network connectivity, and understanding traffic patterns. This rule examines the logConfig field within the firewall rules configuration. A violation is generated if logConfig is missing, or if logConfig.enable is missing or if its set to false.

  * ####  Compute firewall management ports open to internet link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, Security, Network, Firewall, SSH, RDP, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/Firewall`

Details

Checks if firewall rules allow unrestricted public access (0.0.0.0/0 or

  * ####  Compute firewall policy all protocols internet link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/FirewallPolicy`

Details

This rule identifies overly permissive firewall configurations that allow unrestricted internet ingress on all protocols, helping you reduce your networks attack surface and safeguard against unauthorized access.

  * ####  Compute firewall policy logging link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, FirewallPolicy, Logging, Security, Auditing, Network, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/FirewallPolicy`

Details

Checks if a Compute Engine Firewall Policy contains any enabled rules that do not have logging enabled. Firewall logging records connections matching rules, essential for auditing and troubleshooting. This policy iterates through the rules array embedded within the FirewallPolicy resource. A violation is generated if the Firewall Policy contains at least one rule where disabled is not true (i.e., the rule is enabled) AND enableLogging is not true (i.e., logging is disabled), considering that missing boolean fields often default to false. Rules with the highest priority (typically default rules) are excluded.

  * ####  Compute firewall policy mgmt ports open to internet link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, Security, Network, Firewall, SSH, RDP, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/FirewallPolicy`

Details

Checks if firewall policies allow unrestricted public access (0.0.0.0/0 or

  * ####  Compute firewall policy public ingress link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, FirewallPolicy, Security, Network, PublicAccess, Ingress, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/FirewallPolicy`

Details

Checks if a Compute Engine Firewall Policy contains any enabled ingress rules allowing traffic from any source IP address (0.0.0.0/0 for IPv4 or /0 for IPv6). This policy iterates through the rules array embedded within the FirewallPolicy resource data. Allowing public ingress traffic can be a significant security risk if not intended. This rule flags the entire policy if even one such rule exists.

  * ####  Compute firewall policy unusual protocol internet link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/FirewallPolicy`

Details

Identifies firewall rules exposing unusual internetfacing protocols, enabling proactive attack surface reduction to enhance security and prevent costly system compromises.

  * ####  Compute firewall policy unusual tcp ports internet link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/FirewallPolicy`

Details

Enhances security by identifying firewall rules granting unrestricted public internet access to commonly targeted TCP ports (e.g., 20, 21, 22, 25, 53, 80, 110, 143, 443), enabling proactive attack surface reduction and defense against unauthorized exploitation.

  * ####  Compute firewall policy unusual udp ports internet link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/FirewallPolicy`

Details

Identifies firewall policies that expose typically TCPassociated or other sensitive UDP ports to the internet, enabling you to reduce your attack surface and enhance service reliability by preventing potential misconfigurations or exploits.

  * ####  Compute firewall publicly exposed internet link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, Security, Network, Firewall, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/Firewall`

Details

Detects Compute Engine firewall rules that are publicly exposed. A firewall rule is considered publicly exposed if it allows traffic from any IP address (0.0.0.0/0 for IPv4 or /0 for IPv6) for ingress rules, or allows traffic to any IP address for egress rules. Publicly exposed firewall rules significantly increase the attack surface and risk of unauthorized access. Firewall rules should be configured with the principle of least privilege, allowing only necessary traffic from/to specific, trusted sources/destinations. This rule checks for both ingress and egress rules with overly permissive source or destination ranges, including cases where ranges are empty or null.

  * ####  Compute firewall unusual protocols internet link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/Firewall`

Details

Reduces your attack surface by identifying active ingress firewall rules that expose uncommon network protocols (not TCP, UDP, or ICMP) to the internet, preventing potential breaches through unmonitored services.

  * ####  Compute firewall unusual tcp ports internet link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/Firewall`

Details

Reduce your systems internet attack surface by identifying and reviewing firewall rules that expose a curated list of potentially vulnerable TCP ports 20,21,22,25,53,80,110,143,443,587,989,990,995,1194,3389 to public access.

  * ####  Compute firewall unusual udp ports internet link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/Firewall`

Details

This rule enhances your network security by identifying publicly exposed firewall rules allowing unusual UDP ports 20,21,22,25,53,80,110,143,443,587,989,990,995,and 1194, thereby minimizing your attack surface and preventing potential service exploitation that could impact reliability, performance, or lead to unexpected costs.

  * ####  Compute firewall using network tags link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Network, Firewall, Tags, Security, CSPR

Asset: `compute.googleapis.com/Firewall`

Details

Flags VPC Firewall rules that use network tags. Network tags are less secure than IAM-governed secure tags for firewall targeting.

  * ####  Compute google private access link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Subnet, Subnetwork, VPC, PrivateGoogleAccess, Networking, Security, CSPR, CoNa

Asset: `compute.googleapis.com/Subnetwork`

Details

Checks if Private Google Access (PGA) is disabled for a Compute Engine Subnetwork. PGA allows VM instances in the subnet without external IP addresses to reach Google APIs and services using Googles internal network, enhancing security and potentially reducing egress costs. If PGA is disabled, VMs without external IPs cannot access these services directly. This rule examines the privateIpGoogleAccess field within the Subnetwork configuration. A violation is generated if privateIpGoogleAccess is missing or set to false.

  * ####  Compute http load balancer link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security, CSPR

Asset: `compute.googleapis.com/TargetHttpProxy`

Details

This rule identifies HTTP load balancers, which transmit unencrypted data, critically exposing sensitive information, eroding customer trust, and often violating compliance mandates, thereby underscoring the necessity of HTTPS for secure, private, and trustworthy communications.

  * ####  Compute image old not deprecated link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Images, Lifecycle, FinOps, Cost, CSPR

Asset: `compute.googleapis.com/Image`

Details

Detects Compute Engine images that are older than 90 days and are not in a deprecated state. Old, unused images can accumulate, increasing storage costs and potentially posing security risks if they contain outdated software or vulnerabilities. Its a best practice to regularly review and deprecate or delete old images that are no longer needed. This rule flags images older than 90 days that havent been deprecated, prompting a review of their status and potential removal.

  * ####  Compute instance automatic restart link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, Reliability, Availability, HighAvailability, Resiliency, CSPR, CoNa

Asset: `compute.googleapis.com/Instance`

Details

Checks if the Automatic Restart feature is enabled for Compute Engine instances. Automatic restart ensures that if an instance is terminated by a nonuserinitiated event (like a hardware failure), it is automatically restarted, maintaining high availability.

  * ####  Compute instance in mig check link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Compute, HighAvailability, Resiliency

Asset: `compute.googleapis.com/Instance`

Details

Checks if Compute VM instance is part of a Managed Instance Group (MIG). Standalone VMs are not resilient to host failures and lack auto-healing.

  * ####  Compute instance live migration link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Availability, Compute, Maintenance

Asset: `compute.googleapis.com/Instance`

Details

Checks if Compute Engine instances are configured for live migration. Live migration keeps instances running during host system events, such as software or hardware updates, by moving them to another host. Instances not set to MIGRATE (e.g., set to TERMINATE) will be stopped during maintenance, potentially causing application downtime.

  * ####  Compute instance non default service account link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, IAM, Security, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Verifies that Compute Engine instances do not use the default compute service account.

  * ####  Compute legacy network link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Compute, Network, VPC, AutoMode, Subnets, Networking, Configuration, CSPR

Asset: `compute.googleapis.com/Network`

Details

Identifies legacy Compute Engine VPC networks. Legacy networks lack subnet support, use a single global IP range, and do not support modern VPC features. Migrating to custom mode VPC networks is recommended to enable subnets, improve network segmentation, and reduce the attack surface.

  * ####  Compute machine image CMEK disabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Compute, Machine Image, NIST-800-53-SC-28

Asset: `compute.googleapis.com/MachineImage`

Details

Ensures that Compute Engine Machine Images are encrypted with a CustomerManaged Encryption Key (CMEK), providing control over the encryption keys used to protect the image data at rest. This configuration is critical for meeting strict compliance requirements and enhancing data security. A misconfiguration occurs if the machineImageEncryptionKey.kmsKeyName field is missing or empty.

  * ####  Compute mig health check disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: compute, Security, CSPR

Asset: `compute.googleapis.com/InstanceGroupManager`

Details

Identifies Managed Instance Groups (MIGs) that do not have an auto-healing health check configured. Configuring health checks is a critical operational best practice to guarantee automatic VM recovery in case of application failures.

  * ####  Compute mig regional check link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, Reliability, Availability, HighAvailability, MIG

Asset: `compute.googleapis.com/InstanceGroupManager`

Details

Checks if a Compute Engine Managed Instance Group (MIG) is configured as Zonal. Regional MIGs are recommended for high availability because they distribute VM instances across multiple zones within a region, safeguarding workloads against singlezone failures. This rule identifies MIGs where the configuration is tied to a specific zone rather than a region.

  * ####  Compute missing labels link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Compute, VM, Instance, Labels, Organization, Management, FinOps, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Ensures Compute Engine instances have labels applied for better resource organization, cost allocation, and filtering capabilities.

  * ####  Compute missing resource tags link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, VM, Tags, FinOps, Organization, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/Instance`

Details

Ensures Compute Engine instances have Resource Manager tags applied via the params.resourceManagerTags field for consistent governance, policy enforcement, and cost analysis.

  * ####  Compute missing tags link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Network, Firewall, Tags, FinOps, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Ensures Compute Engine instances have network tags applied for effective firewall rule targeting and network segmentation.

  * ####  Compute nat log disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Logging, Security

Asset: `compute.googleapis.com/Router`

Details

Enabling Cloud NAT logging provides critical telemetry for rapid troubleshooting and security analysis, enhancing network reliability and operational visibility.

  * ####  Compute nat log errors only link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Logging, Security

Asset: `compute.googleapis.com/Router`

Details

Enable comprehensive Cloud NAT logging for both translations and errors to significantly improve troubleshooting capabilities and operational visibility, as erroronly logging limits crucial diagnostic insights for network reliability and security analysis.

  * ####  Compute nat router logging link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Router, NAT, Logging, Monitoring, Security, Networking, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/Router`

Details

Checks if logging is disabled for Cloud NAT configurations on a Compute Engine Router. Cloud NAT logging provides visibility into NAT translations and errors, crucial for monitoring, troubleshooting, and security analysis. This rule iterates through all NAT configurations (nats array) associated with a router. If any NAT configuration is found where the logConfig.enable field is missing or set to false, a violation is generated for the router.

  * ####  Compute neg zonal link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, new-rule, CoNa

Asset: `compute.googleapis.com/NetworkEndpointGroup`

Details

Checks for the existence of Zonal Network Endpoint Groups (NEGs). Zonal NEGs constrain traffic to a single availability zone, creating a potential single point of failure during zonal outages. This rule identifies these resources to ensure their use is intentional and that they are part of a broader multi-zone high-availability strategy.

  * ####  Compute network auto create subnet link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security

Asset: `compute.googleapis.com/Network`

Details

Disable autocreated subnetworks to enforce intentional network design, enhancing security by preventing default, potentially insecure subnets in every region and optimizing costs by avoiding unnecessary resource allocation.

  * ####  Compute network default link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Network, VPC, Default, Security, Networking, CSPR

Asset: `compute.googleapis.com/Network`

Details

Checks for the existence of the default Compute Engine network. The default network is automatically created in new projects (unless disabled) and comes with permissive firewall rules (e.g., allowinternal, allowrdp, allowssh from anywhere). While convenient for initial setup, using the default network for production workloads is discouraged due to its flat structure and overly broad default permissions. Its recommended to create custom VPC networks with more restrictive, purposebuilt firewall rules. This rule identifies networks named default.

  * ####  Compute network global dynamic routing link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Network, Reliability, HighAvailability, HybridConnectivity

Asset: `compute.googleapis.com/Network`

Details

Checks if the VPC Network is configured with Global Dynamic Routing. Global Dynamic Routing allows Cloud Routers to learn and advertise routes from all regions, facilitating crossregion failover and simplified network management for hybrid environments. This rule identifies networks where routingConfig.routingMode is not explicitly set to GLOBAL.

  * ####  Compute no public IP link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Compute, Public IP, Compliance, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Detects Compute Engine VM instances configured with public (external) IP addresses. Exposing VMs directly to the internet increases vulnerability to unauthorized access and brute-force attacks. VMs should use private IPs and access the internet via Cloud NAT or Identity-Aware Proxy (IAP) unless public access is explicitly required.

  * ####  Compute project default network tier premium link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Network, NetworkTier

Asset: `compute.googleapis.com/Project`

Details

Verifies that the default network service tier for the project is set to PREMIUM. Using STANDARD tier as default may lead to lower performance and reliability for network traffic. PREMIUM tier utilizes Google's global network for optimal routing.

  * ####  Compute regional backend service logging link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, RegionBackendService, Logging, Security, Auditing, Monitoring, LoadBalancing, CSPR, CoNa, MVSP

Asset: `compute.googleapis.com/RegionBackendService`

Details

Checks if logging is enabled for a Compute Engine Backend Service. Backend service logging records requests processed by the load balancer, providing essential visibility for monitoring traffic, troubleshooting errors, security analysis, and auditing. This rule examines the logConfig field within the backend services configuration. A violation is generated if logConfig is missing, or if logConfig.enable is missing or if its set to false.

  * ####  Compute snapshot long retention keep snapshots link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Snapshots, Resource Policies, DataRetention, Reliability, FinOps, CSPR, CoNa

Asset: `compute.googleapis.com/ResourcePolicy`

Details

Detects Compute Engine snapshot schedules (within resource policies) that have both a retention period exceeding 365 days and are configured to keep automatic snapshots even after the source disk is deleted (onSourceDiskDelete set to KEEP_AUTO_SNAPSHOTS). While long retention periods and keeping snapshots after source disk deletion might be valid in specific scenarios, this combination can lead to significant storage costs and potentially retain data longer than necessary. This rule flags such configurations for review to ensure that they align with data retention policies and cost optimization goals.

  * ####  Compute snapshot no guest flush link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Snapshots, Resource Policies, Backup, Reliability, CSPR

Asset: `compute.googleapis.com/ResourcePolicy`

Details

Detects Compute Engine snapshot schedules (within resource policies) that do not have applicationconsistent snapshots enabled (i.e., guestFlush is not set to true). Applicationconsistent snapshots ensure that the data on the disk is in a consistent state at the time of the snapshot, which is crucial for reliable backups and recovery, especially for applications like databases. Without guestFlush, the snapshot might capture data in an inconsistent state, potentially leading to data corruption or unrecoverable backups. This rule flags snapshot schedules lacking application consistency.

  * ####  Compute snapshot older than 365d link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Snapshots, Lifecycle, Reliability, FinOps, CSPR

Asset: `compute.googleapis.com/Snapshot`

Details

Detects Compute Engine snapshots that are older than 365 days. Old snapshots can consume significant storage space and increase costs. While some snapshots may need to be retained for long periods, its a best practice to regularly review and delete snapshots that are no longer needed. This rule flags snapshots older than 365 days for review, allowing you to determine if they can be safely deleted or archived.

  * ####  Compute sole tenant ng maintenance link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, NodeGroup, Availability, Isolation, SoleTenant

Asset: `compute.googleapis.com/NodeGroup`

Details

Checks if Sole Tenant Node Groups are configured with the MIGRATE_WITHIN_NODE_GROUP maintenance policy. This setting ensures that during host maintenance, VMs are livemigrated to other nodes within the same dedicated group, preserving physical isolation and availability. Violations occur if the maintenance policy is missing or set to a different mode like DEFAULT or RESTART_IN_PLACE.

  * ####  Compute ssl load balancer link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security

Asset: `compute.googleapis.com/TargetSslProxy`

Details

Ensures that application traffic is served by modern HTTPS Load Balancers instead of legacy SSL Proxy Load Balancers. When an HTTPS Load Balancer is used, it provides layer 7 traffic management, including features like URL maps, integration with Googlemanaged certificates, and advanced security controls. This is valuable for enhancing security with features like SSL Policies and Cloud Armor integration, improving traffic management with contentbased routing, and simplifying certificate lifecycle management. This is particularly helpful for standard web applications that can benefit from applicationaware security and routing rules. However, the SSL Proxy Load Balancer may still be required for specific nonHTTP workloads that use SSL for transport layer encryption.

  * ####  Compute subnet flowlogs link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Subnet, VPC, FlowLogs, Networking, Security, CSPR, CoNa

Asset: `compute.googleapis.com/Subnetwork`

Details

Checks if VPC Flow Logs are enabled for a Compute Engine Subnetwork. VPC Flow Logs record a sample of network flows sent from and received by VM instances in the subnet. This provides crucial visibility for network monitoring, forensics, security analysis, and realtime troubleshooting. This rule examines the enableFlowLogs field within the Subnetwork configuration. A violation is generated if enableFlowLogs is missing or set to false.

  * ####  Compute targethttpsproxy ssl link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, TargetHttpsProxy, SSL, TLS, Security, Policy, Encryption, LoadBalancing, CSPR

Asset: `compute.googleapis.com/TargetHttpsProxy`

Details

Checks if a Compute Engine TargetHttpsProxy resource has an SSL Policy defined. SSL Policies control the set of TLS features (such as TLS versions and cipher suites) that the proxy negotiates with clients. Associating a specific SSL Policy allows for enforcing stricter security standards than the default. This rule examines the sslPolicy field within the TargetHttpsProxy configuration. If sslPolicy is missing or null/empty, it indicates that no specific SSL Policy is assigned, and a violation is generated. Relying on default SSL settings might not meet specific security or compliance requirements.

  * ####  Compute tcp load balancer link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Network, Security

Asset: `compute.googleapis.com/TargetSslProxy`

Details

Validates SSL Proxy Load Balancer usage, guiding towards HTTPS Load Balancers for web traffic to enhance security, performance, and operational efficiency.

  * ####  Compute unattached disk link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: CostOptimization, Compute, Disk, Storage, CoNa

Asset: `compute.googleapis.com/Disk`

Details

Detects persistent disks that are not attached to any VM instance. Unattached disks continue to incur charges, leading to unnecessary cloud spend.

  * ####  Compute unused publicip address link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Address, IP, PublicIP, CostOptimization, Unused, Networking, CSPR, CoNa

Asset: `compute.googleapis.com/Address`

Details

Checks for Compute Engine external IP addresses that are reserved but not currently in use by any resource. Reserved but unused public IP addresses incur costs and may indicate orphaned resources or configuration oversights. This rule identifies addresses where the addressType is EXTERNAL and the status is RESERVED. It is recommended to either assign unused addresses to a resource or release them to avoid unnecessary charges.

  * ####  Compute VM confidential compute disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Security, Confidential Computing, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Checks if Confidential Computing is enabled for Compute Engine VM instances. Confidential Computing uses hardwarebased encryption to protect data in use, even from the cloud provider. This provides a higher level of security and privacy for sensitive workloads. This rule flags instances where Confidential Computing is not enabled. Enabling Confidential Computing may be a requirement for compliance or to meet specific security needs.

  * ####  Compute VM deletion protection disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Security, Deletion Protection, Security, Reliability, CSPR, CoNa

Asset: `compute.googleapis.com/Instance`

Details

Checks if deletion protection is enabled for Compute Engine VM instances. Deletion protection prevents accidental deletion of critical VMs. When enabled, any attempt to delete the instance through the API, CLI, or console will fail unless deletion protection is first explicitly disabled. This provides an important safeguard against human error or malicious actions. This rule flags instances without deletion protection enabled.

  * ####  Compute VM disk CMEK link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, Security, Encryption, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Checks if all disks attached to a Compute Engine VM instance are encrypted using a CustomerManaged Encryption Key (CMEK). Encrypting disks protects data at rest, preventing unauthorized access to the data if the physical storage is compromised. Using CMEKs gives you control over the encryption keys, including key rotation and access management. This rule flags instances where any attached disk is not encrypted with a CMEK.

  * ####  Compute VM IP forwarding enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Security, Networking, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Checks if IP forwarding is enabled for Compute Engine VM instances. Enabling IP forwarding allows a VM to route traffic between different networks, effectively acting as a router. While this capability is necessary for some use cases (e.g., NAT gateways, VPN servers), it should only be enabled when explicitly required. Enabling IP forwarding on instances that dont need it increases the attack surface and can potentially be exploited to bypass network security controls. This rule flags instances with IP forwarding enabled.

  * ####  Compute VM no integrity monitoring link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, Security, Shielded VM, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Checks if Integrity Monitoring is enabled for Compute Engine VM instances. Shielded VM provides verifiable integrity of your VM instances, helping to protect against advanced threats like rootkits and bootkits. Integrity Monitoring allows you to monitor the boot integrity of your instances. vTPM provides a virtualized Trusted Platform Module. Secure Boot helps ensure that the system only runs authentic software. This rule flags instances where any of these features are not enabled.

  * ####  Compute VM no secure boot link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, Security, Shielded VM, CSPR, CoNa

Asset: `compute.googleapis.com/Instance`

Details

Checks if Secure Boot is enabled for Compute Engine VM instances. Shielded VM provides verifiable integrity of your VM instances, helping to protect against advanced threats like rootkits and bootkits. Integrity Monitoring allows you to monitor the boot integrity of your instances. vTPM provides a virtualized Trusted Platform Module. Secure Boot helps ensure that the system only runs authentic software. This rule flags instances where any of these features are not enabled.

  * ####  Compute VM no tpm link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, Security, Shielded VM, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Checks if vTPM is enabled for Compute Engine VM instances. Shielded VM provides verifiable integrity of your VM instances, helping to protect against advanced threats like rootkits and bootkits. Integrity Monitoring allows you to monitor the boot integrity of your instances. vTPM provides a virtualized Trusted Platform Module. Secure Boot helps ensure that the system only runs authentic software. This rule flags instances where any of these features are not enabled.

  * ####  Compute VM oslogin 2fa disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Security, OSLogin, 2FA, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Checks if OS Login is enabled for Compute Engine VM instances without enabling twofactor authentication (2FA). While OS Login itself enhances security by using IAM for access control, requiring 2FA adds a crucial extra layer of protection against compromised credentials. Without 2FA, an attacker who obtains a users password could gain access to the VM. This rule flags instances where OS Login is enabled, but 2FA is not enabled.

  * ####  Compute VM oslogin disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Security, OSLogin, CSPR

Asset: `compute.googleapis.com/Instance`

Details

(Note - this rule checks instance-level metadata overrides only. Protect-level OS login configurations are not validated by this rule.) Checks if OS Login is enabled for Compute Engine VM instances. OS Login provides centralized and granular access control to VMs using IAM roles, rather than relying on individual SSH keys managed at the instance or project level. OS Login improves security, simplifies key management, and enhances auditability. This rule flags instances where OS Login is not enabled.

  * ####  Compute VM project ssh keys allowed link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Security, SSH, Security, Reliability, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Checks if a Compute Engine VM instance allows the use of projectwide SSH keys. Projectwide SSH keys can be added to a projects metadata and automatically grant access to all instances within that project unless explicitly blocked or OS Login is enabled. Relying solely on projectwide SSH keys violates the principle of least privilege and increases the risk of unauthorized access if a key is compromised. Its generally recommended to either use OS Login (which provides more granular control) or explicitly block projectwide SSH keys and use instancespecific keys instead. This rule flags instances that do not block projectwide SSH keys and do not have OS Login enabled.

  * ####  Compute VM serial port enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Compute, Security, Compute Engine, Serial Port, CSPR

Asset: `compute.googleapis.com/Instance`

Details

Checks if serial port access is enabled for Compute Engine VM instances. The serial port provides a textbased console for interacting with the VM, primarily for debugging and troubleshooting. While useful in specific situations, enabling the serial port increases the attack surface, as it can potentially be used to gain unauthorized access if not properly secured. It is generally recommended to disable serial port access unless explicitly needed and with appropriate security measures (e.g., strong authentication, firewall rules). This rule flags instances with serial port access enabled.

  * ####  Compute VM shielded VM incomplete link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, Security, Shielded VM, CSPR, CoNa

Asset: `compute.googleapis.com/Instance`

Details

Checks if all Shielded VM features (Integrity Monitoring, vTPM, and Secure Boot) are enabled for Compute Engine VM instances. Shielded VM provides verifiable integrity of your VM instances, helping to protect against advanced threats like rootkits and bootkits. Integrity Monitoring allows you to monitor the boot integrity of your instances. vTPM provides a virtualized Trusted Platform Module. Secure Boot helps ensure that the system only runs authentic software. This rule flags instances where any of these features are not enabled.

  * ####  Compute VM subnet private access link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Asset: `compute_Instance_RESOURCE_6`

Details

Ensure VM instances are connected to subnets that have Private Google Access enabled.

  * ####  Compute vpntunnel ike version link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, VpnTunnel, VPN, IKEv1, IKEv2, Security, Encryption, Networking, CSPR

Asset: `compute.googleapis.com/VpnTunnel`

Details

Checks if a Compute Engine VPN Tunnel is configured to use the IKEv1 protocol. IKEv1 (Internet Key Exchange version 1) is an older VPN protocol with known security weaknesses compared to the more modern IKEv2. Using IKEv1 increases the risk of security vulnerabilities. This rule examines the ikeVersion field within the VPN Tunnel configuration. A violation is generated if ikeVersion is set to 1. It is strongly recommended to use IKEv2 (version 2) for enhanced security and reliability.

  * ####  Firewall deny egress default link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Firewall, Network, Compliance, CSPR, CoNa, MVSP

Asset: `compute_Network_RESOURCE_2`

Details

Flags Compute Engine VPC Networks that are not configured with a default egress deny firewall rule.

  * ####  Firewall policy deny egress default link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Networking, Security, Compliance, CSPR, CoNa, MVSP

Asset: `compute_Network_RESOURCE_1`

Details

Flags Compute Engine VPC Networks that are not configured with a default egress deny firewall policy.

  * ####  Compute Engine images publicly exposed link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Compute Engine, image, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Prevents unauthorized access and potential data exfiltration by detecting if a projects IAM policy grants public access (allUsers or allAuthenticatedUsers), which would expose all contained Compute Engine images.

  * ####  Osconfig vuln report critical link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Tags: Compute, Security, osconfig, Vulnerability, CSPR

Asset: `compute_Instance_RESOURCE_8`

Details

Detects Compute Engine VM instances that have OS Config vulnerability reports containing vulnerabilities with a CRITICAL severity level. Critical vulnerabilities represent the highest level of risk and should be addressed immediately to prevent potential exploitation.

  * ####  Privategoogleaccess compute link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Networking, Security, Compliance

Asset: `compute_Instance_RESOURCE_1`

Details

Ensure Private Google Access is enabled specifically for subnetworks attached to VM Instances.

  * ####  Project multiregion nat link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Network, NAT, HighAvailability, BCDR

Asset: `cloudresourcemanager_Project_RESOURCE_ROUTER`

Details

Verifies that a Project has Cloud NAT configured across at least 2 different regions. Multi-regional Cloud NAT deployment ensures redundancy and protects against regional outages for outbound connectivity.

  * ####  Project multizone instances link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Compute, Instance, HighAvailability, BCDR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_INSTANCE`

Details

Verifies that a Project has Compute Engine application service VMs deployed across at least 2 different zones. Multi-zonal VM deployment ensures compute redundancy and protects against zonal outages.

  * ####  Snapshot Cloud Storage multi region link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Compute, Backup, DisasterRecovery, BCDR

Asset: `compute.googleapis.com/Snapshot`

Details

Verify that Compute Engine disk snapshots are stored in multi-region locations to ensure survivability and recovery capability during a regional outage.

  * ####  Sslpolicy modern with tlsv12 link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Compute, SslPolicy, TLS, Security, Encryption, Profile, Modern, CSPR

Asset: `compute.googleapis.com/SslPolicy`

Details

Checks if a Compute Engine SSL Policy meets recommended security standards by having its profile set to MODERN and its minimum TLS version set to TLS_1_2. The MODERN profile includes strong cipher suites and disables older, less secure TLS versions. Setting the minimum TLS version to TLS_1_2 further enhances security by disallowing TLS 1.0 and 1.1. This rule examines the profile and minTlsVersion fields. A violation is generated if the profile is not MODERN OR the minTlsVersion is not TLS_1_2.

  * ####  Subnet stack type link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Security, Network, Compliance

Asset: `compute.googleapis.com/Subnetwork`

Details

Checks if a Compute Engine VPC subnetwork is configured with a dual-stack (IPV4_IPV6) stack type. Enforcing IPv4-only stack types helps maintain a consistent security posture, reduces network complexity, and ensures alignment with organizational policies that restrict IPv6 usage to prevent unauthorized access paths.




### Google Cloud Best Practices - Dataproc (2 results)

  * ####  Dataproc autoscaling graceful decommission link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Dataproc, Autoscaling, Reliability, CostOptimization

Asset: `dataproc.googleapis.com/AutoscalingPolicy`

Details

Checks if Dataproc AutoscalingPolicies define a gracefulDecommissionTimeout. A graceful timeout ensures that running jobs are allowed to finish before worker nodes are scaled down.

  * ####  Dataproc cluster master ha link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Availability, HighAvailability, BCDR

Asset: `dataproc.googleapis.com/Cluster`

Details

Verifies that Dataproc clusters operate in High Availability mode by provisioning three master instances. Running with fewer than three master nodes introduces a single point of failure, jeopardizing production stability and data processing continuity during maintenance or outages.




### Google Cloud Best Practices - Filestore (5 results)

  * ####  Filestore instance backup conf link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Reliability, Data Protection, Backup, CSPR

Asset: `file.googleapis.com/Instance`

Details

Ensure Filestore instances have a defined backup schedule to enable robust data recovery and safeguard against data loss from accidental deletion or corruption. This rule specifically validates the presence of a backupConfig in the instance settings, which is essential for business continuity.

  * ####  Filestore instance deletion protection disabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Reliability, Data Protection, CoNa

Asset: `file.googleapis.com/Instance`

Details

Ensures Filestore instances have deletion protection enabled to prevent accidental data loss and service disruption from unintentional deletions. Disabling deletion protection on critical file shares increases the risk of operational errors that can lead to irreversible data loss. This setting is controlled by the deletionProtectionEnabled flag in the instance configuration.

  * ####  Filestore instance ha tiers link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, High Availability, Filestore, Resiliency

Asset: `file.googleapis.com/Instance`

Details

Ensures Google Cloud Filestore instances are configured with Regional availability tiers (ENTERPRISE or REGIONAL) to support high availability and resilience for critical workloads. Basic, High Scale SSD, and generic Zonal tiers are singlezone deployments and do not provide the multizonal resiliency required to protect against zonal failures.

  * ####  Filestore instance missing labels link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Filestore, Instance, Labels, FinOps, CSPR

Asset: `file.googleapis.com/Instance`

Details

Ensures Filestore instances have labels applied for resource organization, filtering, and potentially aiding in cost allocation analysis.

  * ####  Filestore instance missing resource tags link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Filestore, Instance, Tags, FinOps, CSPR, CoNa, MVSP

Asset: `file.googleapis.com/Instance`

Details

Ensures Filestore instances have Resource Manager tags applied for consistent governance, policy enforcement, and cost analysis across cloud resources.




### Google Cloud Best Practices - Firestore (1 results)

  * ####  Firestore database multi region link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, BCDR, High Availability

Asset: `firestore.googleapis.com/Database`

Details

Verifies that Firestore databases are configured to use multiregion locations (e.g., nam5, eur3). Multiregion deployments replicate data across distinct geographic areas, ensuring high availability and resilience against regional outages.




### Google Cloud Best Practices - Gemini Enterprise Agent Platform (18 results)

  * ####  Vertex ai endpoint min replicas link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, VertexAI, HighAvailability, Resiliency

Asset: `aiplatform.googleapis.com/Endpoint`

Details

Ensures deployed ML models on online endpoints have at least 2 replicas to maintain availability and prevent prediction downtime during single node failure.

  * ####  Vertex custom job CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance

Asset: `aiplatform.googleapis.com/CustomJob`

Details

Ensures Vertex AI custom training jobs are protected with customermanaged encryption keys (CMEK), providing granular control over data encryption for enhanced security and compliance. This rule checks that the encryptionSpec.kmsKeyName field is properly configured in the jobs specification.

  * ####  Vertex dataset CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance

Asset: `aiplatform.googleapis.com/Dataset`

Details

Ensures Vertex AI datasets are protected with customermanaged encryption keys (CMEK), providing granular control over data encryption for enhanced security and compliance. This rule checks that the encryptionSpec.kmsKeyName field is properly configured for the dataset.

  * ####  Vertex endpoint CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance

Asset: `aiplatform.googleapis.com/Endpoint`

Details

Ensures that Vertex AI Endpoints are encrypted with a customermanaged encryption key (CMEK), providing granular control over data encryption for deployed models and enhancing security. This setting is critical for compliance and protecting sensitive data at rest. This rule checks that the encryptionSpec.kmsKeyName field is properly configured on the endpoint.

  * ####  Vertex featurestore CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance

Asset: `aiplatform.googleapis.com/Featurestore`

Details

Ensures Vertex AI Featurestores are protected with customermanaged encryption keys (CMEK), providing granular control over data encryption for enhanced security and compliance. This rule checks that the encryptionSpec.kmsKeyName field is properly configured.

  * ####  Vertex hyperparameter tuning job CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance

Asset: `aiplatform.googleapis.com/HyperparameterTuningJob`

Details

Ensures Vertex AI hyperparameter tuning jobs are protected with customermanaged encryption keys (CMEK), providing granular control over data encryption for enhanced security and compliance. This rule checks that the encryptionSpec.kmsKeyName field is properly configured in the jobs specification.

  * ####  Vertex metadata store CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance

Asset: `aiplatform.googleapis.com/MetadataStore`

Details

Ensures Vertex AI Metadata Stores are protected with customermanaged encryption keys (CMEK) for greater control over data encryption. This rule verifies that the encryptionSpec.kmsKeyName field is present and configured, which is essential for compliance and enhancing data security by ensuring metadata is not just encrypted by default, but with a key that you control.

  * ####  Vertex model CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance

Asset: `aiplatform.googleapis.com/Model`

Details

Ensures Vertex AI models are protected with customermanaged encryption keys (CMEK) for enhanced control over data encryption and to meet compliance requirements. This rule verifies that the encryptionSpec.kmsKeyName field is properly configured in the models resource data.

  * ####  Vertex notebook runtime CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance, CoNa, MVSP

Asset: `aiplatform.googleapis.com/NotebookRuntime`

Details

Ensures Vertex AI Notebook Runtimes are protected with customermanaged encryption keys (CMEK), providing granular control over data encryption for enhanced security and compliance. A Notebook Runtime without CMEK uses Googlemanaged encryption keys by default.

  * ####  Vertex notebook runtime idle shutdown enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Cost, FinOps, Vertex AI, CoNa, MVSP

Asset: `aiplatform.googleapis.com/NotebookRuntime`

Details

Enforces automatic idle shutdown on Vertex AI Notebook Runtimes to optimize costs by terminating inactive resources. A misconfiguration occurs if the idleShutdownConfig is not defined or if the idleShutdownDisabled flag within it is set to true, leading to continuous resource billing even when not in use.

  * ####  Vertex notebook runtime no internet access link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, Networking, Data Exfiltration, CoNa, MVSP

Asset: `aiplatform.googleapis.com/NotebookRuntime`

Details

Ensures Vertex AI Notebook Runtimes do not have direct internet access to mitigate risks such as data exfiltration and unauthorized access to external resources. Disabling internet access enhances the security posture by isolating the runtime environment. Internet access is controlled by the networkSpec.enableInternetAccess setting.

  * ####  Vertex notebook runtime secure boot disabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, Shielded VM, Secure Boot, NIST-800-53-SI-7, CoNa, MVSP

Asset: `aiplatform.googleapis.com/NotebookRuntime`

Details

Ensures Secure Boot is enabled on Vertex AI Notebook Runtimes to protect against bootlevel threats. Secure Boot is a core Shielded VM feature that verifies the digital signature of all boot components, preventing the execution of unauthorized or malicious code during the boot process. This rule checks that the enableSecureBoot flag is explicitly set to true.

  * ####  Vertex notebook runtime template CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance, CoNa, MVSP

Asset: `aiplatform.googleapis.com/NotebookRuntimeTemplate`

Details

Ensures Vertex AI Notebook Runtimes are protected with customermanaged encryption keys (CMEK), providing granular control over data encryption for enhanced security and compliance. A Notebook Runtime without CMEK uses Googlemanaged encryption keys by default.

  * ####  Vertex notebook runtime template idle shutdown link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Cost, FinOps, Vertex AI, CoNa, MVSP

Asset: `aiplatform.googleapis.com/NotebookRuntimeTemplate`

Details

Enforces automatic idle shutdown on Vertex AI Notebook Runtime Templates to optimize costs by terminating inactive resources. A misconfiguration occurs if the idleShutdownConfig is not defined or if the idleShutdownDisabled flag within it is set to true, leading to continuous resource billing even when not in use.

  * ####  Vertex notebook runtime template internet access link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, Network, CoNa, MVSP

Asset: `aiplatform.googleapis.com/NotebookRuntimeTemplate`

Details

Ensures Vertex AI runtime templates are not exposed to the public internet, which reduces the external attack surface and helps prevent potential data exfiltration. This is violated when the enableInternetAccess setting is true.

  * ####  Vertex notebook runtime template secure boot link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, Notebooks, Compliance, CoNa, MVSP

Asset: `aiplatform.googleapis.com/NotebookRuntimeTemplate`

Details

Verifies that Vertex AI Notebook Runtime Templates have Secure Boot enabled to ensure operating system integrity and protect against unauthorized bootlevel code. Secure Boot is a critical security feature that helps prevent the execution of malicious code during the boot process. This setting is controlled by the enableSecureBoot flag within the shieldedVmConfig object.

  * ####  Vertex tensorboard CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance

Asset: `aiplatform.googleapis.com/Tensorboard`

Details

Ensures Vertex AI TensorBoard instances are protected with customermanaged encryption keys (CMEK), providing granular control over the encryption of experiment data and model visualizations for enhanced security and compliance. This rule checks that the encryptionSpec.kmsKeyName field is properly configured.

  * ####  Vertex training pipeline CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance

Asset: `aiplatform.googleapis.com/TrainingPipeline`

Details

Ensures Vertex AI training pipelines are protected with customermanaged encryption keys (CMEK), providing granular control over data encryption for enhanced security and compliance. This rule checks that the encryptionSpec.kmsKeyName field is properly configured in the pipelines specification.




### Google Cloud Best Practices - Gemini Enterprise Agent Platform Workbench (11 results)

  * ####  Vertex workbench auto upgrades enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Security, Reliability, Vertex AI, Notebooks, CoNa

Asset: `notebooks.googleapis.com/Instance`

Details

Ensures that Vertex AI Workbench instances have automatic environment upgrades enabled. Enabling automatic upgrades is crucial for keeping instances uptodate with the latest features, framework updates, and security patches, which enhances both security and reliability. This setting is controlled by the notebookupgradeschedule metadata key, which should be present and have a value defined.

  * ####  Vertex workbench CMEK enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Encryption, CMEK, Vertex AI, Compliance, NIST-800-53-SC-28

Asset: `notebooks.googleapis.com/Instance`

Details

Ensures that Vertex AI Workbench instances are encrypted using a CustomerManaged Encryption Key (CMEK), which is critical for maintaining control over data encryption and meeting specific compliance requirements. This policy verifies that the kmsKey property is configured for both the boot and data disks within the instances gceSetup.

  * ####  Vertex workbench default network disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Security, Network, Vertex AI

Asset: `notebooks.googleapis.com/Instance`

Details

Disabling the use of the default VPC network for Vertex AI Workbench instances is a key security measure to prevent exposure to overly permissive firewall rules. This misconfiguration is caused when a Workbench instance is attached to the network resource named default, bypassing a more secure, intentionally designed network architecture.

  * ####  Vertex workbench deletion protection enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Vertex AI, Notebooks, CoNa

Asset: `notebooks.googleapis.com/Instance`

Details

Ensures Vertex AI Workbench instances have deletion protection enabled, preventing accidental deletion of critical development environments and associated data. This protection is vital for maintaining operational reliability, as a misconfiguration can lead to irreversible loss of work. The deletionProtection flag must be explicitly set to true.

  * ####  Vertex workbench disable file downloads link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, Notebooks, Data Exfiltration, NIST-800-53-AC-3, CoNa

Asset: `notebooks.googleapis.com/Instance`

Details

To prevent data exfiltration, this policy ensures that file downloads from the JupyterLab interface in Vertex AI Workbench instances are disabled. A misconfiguration occurs if the notebookdisabledownloads metadata key is missing or not set to true, creating a potential vector for unauthorized data removal.

  * ####  Vertex workbench disable root access link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, Notebooks, Privilege Escalation

Asset: `notebooks.googleapis.com/Instance`

Details

Disabling root access on Vertex AI Workbench instances is a crucial security measure to prevent privilege escalation and unauthorized system modifications. This setting is controlled by the notebookdisableroot metadata key within the Compute Engine setup, which should be set to true.

  * ####  Vertex workbench integrity monitoring enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, Notebooks, Integrity Monitoring, NIST-800-53-SI-7

Asset: `notebooks.googleapis.com/Instance`

Details

Ensures Vertex AI Workbench instances have Shielded VM integrity monitoring enabled, providing a foundational layer of defense against bootlevel and kernellevel malware. A violation occurs if the enableIntegrityMonitoring flag within the instances Shielded VM configuration is missing, empty, or set to false.

  * ####  Vertex workbench no public IP link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, Networking

Asset: `notebooks.googleapis.com/Instance`

Details

Ensures Vertex AI Workbench instances do not have public IP addresses assigned by verifying the disablePublicIp setting is explicitly set to true. Disabling public IPs is a crucial security measure that reduces the instances exposure to the public internet, minimizing the risk of unauthorized access. A violation occurs if the disablePublicIp setting is missing, empty, or set to false.

  * ####  Vertex workbench restrict default service account link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, IAM, Service Account, NIST-800-53-AC-3, CSPR

Asset: `notebooks.googleapis.com/Instance`

Details

Ensures that Vertex AI Workbench instances do not use the default Compute Engine service account. Assigning dedicated, leastprivilege service accounts to Workbench instances is a critical security measure that minimizes the potential impact of a compromise by limiting the instances access to only necessary Google Cloud services. This check flags instances configured with a service account ending in compute@developer.gserviceaccount.com, which indicates the use of the overly permissive default service account.

  * ####  Vertex workbench secure boot enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, Notebooks, Shielded VM, CoNa

Asset: `notebooks.googleapis.com/Instance`

Details

Ensures Vertex AI Workbench instances have Secure Boot enabled, a critical security feature that verifies the digital signature of all boot components to protect against bootkits and rootkits. This setting, enableSecureBoot, is part of the instances Shielded VM configuration and must be set to true.

  * ####  Vertex workbench vtpm enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Security, Vertex AI, Notebooks, vTPM, Shielded VM

Asset: `notebooks.googleapis.com/Instance`

Details

Verifies that Vertex AI Workbench instances have the virtual trusted platform module (vTPM) enabled to ensure a secure and measured boot process. Activating vTPM is a critical component of Google Clouds Shielded VM capabilities, which protects instances from bootlevel malware and rootkits by providing verifiable integrity of the instances bootloader, kernel, and boot drivers. This setting is managed within the shieldedInstanceConfig of the instance.




### Google Cloud Best Practices - Google Kubernetes Engine (55 results)

  * ####  Google Kubernetes Engine alpha clusters enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: GKE, Security, CSPR, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Verifies that GKE Clusters do not have Alpha features enabled. Alpha clusters are not supported for production workloads and expire after 30 days.

  * ####  Google Kubernetes Engine Autopilot enabled link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Autopilot, Managed, Configuration, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if a Google Kubernetes Engine (Google Kubernetes Engine) cluster has Autopilot mode enabled. Google Kubernetes Engine Autopilot is a fully managed mode of operation that reduces operational overhead by managing the clusters infrastructure, including nodes and security configurations. This rule identifies clusters where the autopilot.enabled field is set to false or undefined. This policy is primarily informational, flagging clusters that are NOT running in Autopilot mode.

  * ####  Google Kubernetes Engine backup enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Kubernetes, Backup, DisasterRecovery, BCDR

Asset: `container.googleapis.com/Cluster`

Details

Verify that Backup for GKE is enabled on the GKE cluster to allow stateful application backup and disaster recovery.

  * ####  Google Kubernetes Engine basic auth enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Authentication, BasicAuth, ClientCertificate, Security, Configuration, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if a Google Kubernetes Engine cluster has both Basic Authentication (username/password) configured and Client Certificate issuance enabled. Having multiple static credential methods active simultaneously can increase the attack surface and management overhead. It is generally recommended to standardize on more secure and centrally managed authentication methods like IAM or OIDC. This rule flags clusters where masterAuth.username is not null/empty AND masterAuth.clientCertificateConfig.issueClientCertificate is true.

  * ####  Google Kubernetes Engine binary authorization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Security, CoNa, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Ensure Binary Authorization is enabled for Google Kubernetes Engine clusters.

  * ####  Google Kubernetes Engine cluster auto repair enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Google Kubernetes Engine, Governance, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Improves cluster resilience and reduces operational overhead by verifying Google Kubernetes Engine Standard node pools have autorepair enabled, ensuring automatic recovery from node failures to maintain application availability.

  * ####  Google Kubernetes Engine cluster auto upgrade enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Auto Upgrade, Security, Reliability, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Strengthens cluster security and reduces maintenance overhead by verifying Google Kubernetes Engine Standard node pools have autoupgrade enabled, ensuring they receive timely security patches and stability fixes.

  * ####  Google Kubernetes Engine cluster Private Google Access enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Private Google Access, subnetwork, security, CSPR

Asset: `container_Cluster_RESOURCE_2`

Details

Enhances security by verifying Private Google Access is enabled on the clusters subnetwork, allowing private Google Kubernetes Engine nodes to pull images and access Google APIs without requiring public IP addresses.

  * ####  Google Kubernetes Engine cluster using Container-Optimized OS images link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, COS, Security, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Enhances cluster security and stability by verifying all Google Kubernetes Engine node pools use Googles ContainerOptimized OS (COS), a purposebuilt, hardened operating system.

  * ####  Google Kubernetes Engine cluster zonal link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Cluster, Locations, Resiliency, Security, CSPR, CoNa

Asset: `container.googleapis.com/Cluster`

Details

Checks if a Google Kubernetes Engine cluster is zonal. Google Kubernetes Engine Clusters can be created in a single zone in which a single instance of the Control Plane/API Server is deployed. Alternatively, clusters can be created in a Google Cloud region which spreads three instances of the Control Plane/API Server evenly across three zones in that region. Regional clusters also spread the worker nodes evenly across those same three zones to reduce the impact of a Google Cloud zonal outage.

  * ####  Google Kubernetes Engine clusters not using cloud DNS link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Kubernetes, Cluster, DNS, CloudDNS, Networking, BestPractice, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if a Google Kubernetes Engine cluster is configured to use Cloud DNS for incluster DNS resolution. Using Cloud DNS for Google Kubernetes Engine provides a managed, highperformance, and scalable DNS service, and its a Google Kubernetes Engine best practice. This rule examines the dnsConfig.clusterDns field. A violation is generated if this field is missing, null, or has a value other than CLOUD_DNS, indicating the cluster might be using the legacy kubedns addon or is not configured for Cloud DNS.

  * ####  Google Kubernetes Engine confidential nodes link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Security, Compute, CSPR, CoNa

Asset: `container.googleapis.com/Cluster`

Details

Ensure Google Kubernetes Engine cluster is configured to use confidential nodes.

  * ####  Google Kubernetes Engine container native load balancer disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: GKE, Kubernetes, Cluster, LoadBalancing, Networking, Performance, CSPR, CoNa, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Verifies if container-native load balancing is enabled on a GKE cluster. Container-native load balancing allows load balancers to route traffic directly to pods, reducing latency and improving network visibility. A violation occurs if addonsConfig.httpLoadBalancing.disabled is true, which disables the Ingress controller and NEG support.

  * ####  Google Kubernetes Engine dashboard enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Addon, KubernetesDashboard, Security, Legacy, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if the legacy Kubernetes Dashboard addon is enabled for a Google Kubernetes Engine cluster. The Kubernetes Dashboard provides a webbased UI for managing cluster resources, but the legacy version has potential security implications and its use is generally discouraged in favor of gcloud, the Google Cloud console, or other more secure management tools. This rule examines the addonsConfig.kubernetesDashboard.disabled field. A violation is generated if kubernetesDashboard is present and its disabled field is NOT true (i.e., its missing or explicitly false), indicating the legacy dashboard is enabled.

  * ####  Google Kubernetes Engine database encryption CMEK link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Security, Encryption, CSPR, CoNa

Asset: `container.googleapis.com/Cluster`

Details

Ensure Google Kubernetes Engine cluster application secrets are encrypted using CMEK.

  * ####  Google Kubernetes Engine dataplane v2 disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: GKE, Kubernetes, Cluster, Dataplane, Networking, Security, Performance, CSPR, CoNa, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Verifies if Dataplane V2 is enabled on a GKE cluster. Dataplane V2 is an optimized data plane for GKE that uses eBPF for networking, providing improved performance, security, and observability. A violation occurs if networkConfig.datapathProvider is not set to ADVANCED_DATAPATH.

  * ####  Google Kubernetes Engine default service account admin link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Default Service Account, Admin, Security, CSPR, CoNa, MVSP

Asset: `container_Cluster_RESOURCE_IAM_POLICY_1`

Details

Mitigates a critical containertoproject privilege escalation risk by ensuring Google Kubernetes Engine node pools do not use the default service account when it has projectlevel Admin permissions, preventing a compromised pod from gaining control over all project resources.

  * ####  Google Kubernetes Engine default service account editor link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Default Service Account, Editor, Security, CSPR

Asset: `container_Cluster_RESOURCE_IAM_POLICY_1`

Details

Enforce least privilege on Google Kubernetes Engine nodes by disallowing default service accounts with editor roles, critically reducing security vulnerabilities to protect workloads and enhance cluster reliability.

  * ####  Google Kubernetes Engine default service account owner link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Default Service Account, Owner, Security, CSPR, MVSP

Asset: `container_Cluster_RESOURCE_IAM_POLICY_1`

Details

Ensures Google Kubernetes Engine nodes do not use the default Compute Engine service account with the highly privileged Owner role, enforcing least privilege to significantly reduce security risks and the potential impact of a node compromise.

  * ####  Google Kubernetes Engine default service account with permissions link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Security, Least Privilege, IAM

Asset: `container_Cluster_RESOURCE_IAM_POLICY_1`

Details

Ensure Google Kubernetes Engine node service accounts do not possess high-privilege primitive roles.

  * ####  Google Kubernetes Engine default service account writer link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Default Service Account, Writer, Security, CSPR

Asset: `container_Cluster_RESOURCE_IAM_POLICY_1`

Details

Enhance Google Kubernetes Engine security by ensuring default service accounts do not possess broad writer permissions, significantly reducing the risk of unauthorized cluster modifications and upholding the principle of least privilege.

  * ####  Google Kubernetes Engine default service account link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Default Service Account, Security, CSPR

Asset: `container_Cluster_RESOURCE_IAM_POLICY_1`

Details

Verify Google Kubernetes Engine node pools use dedicated, minimallypermissioned service accounts instead of the default Compute Engine service account to enhance cluster security posture by strictly adhering to the principle of least privilege.

  * ####  Google Kubernetes Engine google groups access link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Security, IAM, CSPR, CoNa, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Ensure Google Kubernetes Engine RBAC/cluster access is managed via Google Groups.

  * ####  Google Kubernetes Engine infranodevisibility enabled link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Networking, Observability, IntraNodeVisibility, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if Intranode visibility is enabled for a Google Kubernetes Engine cluster. Intranode visibility allows for network observability of traffic between pods on the same node. This can be useful for troubleshooting and security monitoring within a node. This rule examines the networkConfig.enableIntraNodeVisibility field. A violation is generated if this field is missing or set to false.

  * ####  Google Kubernetes Engine ipaliases disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Networking, IPAliases, VPCNative, PodNetworking

Asset: `container.googleapis.com/Cluster`

Details

Checks if IP Aliases (secondary IP ranges for pods) are disabled for a Google Kubernetes Engine cluster. IP Aliases allow pods to have their own routable IP addresses within the VPC network, enabling better network integration and avoiding NAT for podtopod communication across nodes. While not always strictly required, using IP Aliases is a Google Kubernetes Engine best practice for most networking scenarios. This rule examines the ipAllocationPolicy.useIpAliases field. A violation is generated if this field is missing or set to false.

  * ####  Google Kubernetes Engine issue client cert enabled link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Authentication, ClientCertificate, X509, Security, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if Client Certificate Authentication is enabled for a Google Kubernetes Engine clusters master. When enabled by setting masterAuth.clientCertificateConfig.issueClientCertificate to true, the cluster can issue client certificates for authentication. While X.509 client certificates are a valid authentication method, managing their lifecycle (issuance, revocation) can be complex. Organizations may prefer to rely solely on IAM or OIDC for more centralized control. This rule flags clusters where client certificate issuance is enabled.

  * ####  Google Kubernetes Engine logging enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Logging, Observability, Operations, CSPR, CoNa, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Checks if Cloud Logging (loggingService) are effectively enabled for a Google Kubernetes Engine cluster. These services are crucial for observability. This rule flags a cluster if loggingService is missing, empty, or set to none (or other disabled states), indicating the service is not active.

  * ####  Google Kubernetes Engine monitoring enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Monitoring, Observability, Operations, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if Cloud Monitoring (monitoringService) are effectively enabled for a Google Kubernetes Engine cluster. These services are crucial for observability. This rule flags a cluster if monitoringService is missing, empty, or set to none (or other disabled states), indicating the service is not active.

  * ####  Google Kubernetes Engine network policy enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Kubernetes, Cluster, NetworkPolicy, Security, Microsegmentation, Addon, CSPR, CoNa

Asset: `container.googleapis.com/Cluster`

Details

Checks if Network Policy enforcement is enabled for a Google Kubernetes Engine cluster. Network Policies provide microsegmentation for pods, controlling traffic flow between them based on labels and ports. Enabling Network Policy is a crucial security best practice for isolating workloads and reducing the attack surface within a cluster. This rule examines the networkPolicy.provider and addonsConfig.networkPolicyConfig.disabled fields. A violation is generated if Network Policy is not configured (provider is PROVIDER_UNSPECIFIED or missing) OR if the networkPolicyConfig addon is explicitly disabled.

  * ####  Google Kubernetes Engine no maintenance policy link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Container, Google Kubernetes Engine, Reliability, Operational Stability, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Ensure Google Kubernetes Engine (Google Kubernetes Engine) clusters have a defined maintenance policy to ensure automatic cluster upgrades occur during predictable, nondisruptive time slots. A defined policy with maintenance windows and exclusions prevents unexpected disruptions to critical workloads.

  * ####  Google Kubernetes Engine node autoprovisioning enabled link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Google Kubernetes Engine, Kubernetes, Cluster, NodeAutoprovisioning, Autoscaling, Management

Asset: `container.googleapis.com/Cluster`

Details

Checks if Node AutoProvisioning (NAP) is enabled for a Google Kubernetes Engine cluster. NAP automatically manages node pools based on workload requirements, creating and deleting them as needed. This can simplify cluster management and optimize resource usage. This rule examines the autoscaling.enableNodeAutoprovisioning field within the clusters configuration. A violation is generated if this field is missing or set to false, indicating NAP is not active.

  * ####  Google Kubernetes Engine node pool balanced loc policy link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, High Availability, Google Kubernetes Engine

Asset: `container.googleapis.com/NodePool`

Details

Verifies that Google Kubernetes Engine node pools utilize the BALANCED location policy, ensuring an even distribution of nodes across available zones to maximize high availability and resilience against zonal failures.

  * ####  Google Kubernetes Engine nodelocal dnscache disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: GKE, Kubernetes, Cluster, DNS, Networking, Performance, Scalability, CSPR, CoNa, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Verifies if NodeLocal DNSCache is enabled on a GKE cluster. NodeLocal DNSCache improves Cluster DNS performance by running a DNS caching agent on cluster nodes as a DaemonSet. This is a core GKE networking best practice for scalability and reliability. A violation occurs if addonsConfig.dnsCacheConfig.enabled is false or missing.

  * ####  Google Kubernetes Engine nodepool autoscaling enabled link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Google Kubernetes Engine, Kubernetes, Cluster, NodePool, Autoscaling, Performance, CostOptimization

Asset: `container.googleapis.com/NodePool`

Details

Checks if any node pool within a Google Kubernetes Engine cluster has autoscaling disabled. Node pool autoscaling automatically adjusts the number of nodes based on demand. This rule iterates through the nodePools array in the clusters configuration. A violation is generated if the cluster contains at least one node pool where the autoscaling.enabled field is missing or set to false.

  * ####  Google Kubernetes Engine nodepool CMEK enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Kubernetes, Cluster, NodePool, CMEK, KMS, Encryption, Security, BootDisk

Asset: `container.googleapis.com/NodePool`

Details

Checks if Google Kubernetes Engine cluster node pools are configured to use CustomerManaged Encryption Keys (CMEK) for their boot disks. Using CMEK allows for greater control over the encryption keys protecting node boot disks, enhancing security and compliance. This rule iterates through all nodePools in a cluster. For each node pool, it examines the config.bootDiskKmsKey field. A violation is generated for the cluster if any node pool is found where bootDiskKmsKey is missing or empty, indicating that node pools boot disks are not encrypted with CMEK.

  * ####  Google Kubernetes Engine nodepool kubelet readonly port disabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: GKE, NodePool, Kubelet, Security, CSPR, CoNa

Asset: `container.googleapis.com/NodePool`

Details

Checks if the GKE node pool has the insecure kubelet read-only port enabled. Enabling this port allows unauthenticated access to the kubelet API, which is a security risk. The port should be disabled (insecureKubeletReadonlyPortEnabled should be set to false).

  * ####  Google Kubernetes Engine nodepool multi zonal link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Kubernetes, HighAvailability, Resiliency

Asset: `container.googleapis.com/NodePool`

Details

Ensure GKE node pools span multiple zones (at least 3 recommended for regional clusters) to prevent capacity loss during zonal outages.

  * ####  Google Kubernetes Engine nodepool one zone link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Node Pool, Locations, Resiliency, Security, CSPR

Asset: `container.googleapis.com/NodePool`

Details

Checks if a Google Kubernetes Engine node pool have only one zone. Google Kubernetes Engine Clusters can be created in a single zone in which a single instance of the Control Plane/API Server is deployed. Alternatively, clusters can be created in a Google Cloud region which spreads three instances of the Control Plane/API Server evenly across three zones in that region. Regional clusters also spread the worker nodes evenly across those same three zones to reduce the impact of a Google Cloud zonal outage.

  * ####  Google Kubernetes Engine nodepool single zone link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, GKE, Kubernetes, CoNa

Asset: `container.googleapis.com/Cluster`

Details

Detects GKE node pools that are configured in a single zone in a regional cluster. Spanning node pools across multiple zones is essential for ensuring workload high availability and preventing outages during a single zonal failure.

  * ####  Google Kubernetes Engine nodepool two zones link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Node Pool, Locations, Resiliency, Security, CSPR

Asset: `container.googleapis.com/NodePool`

Details

Checks if a Google Kubernetes Engine node pool have only two zones. Google Kubernetes Engine Clusters can be created in a single zone in which a single instance of the Control Plane/API Server is deployed. Alternatively, clusters can be created in a Google Cloud region which spreads three instances of the Control Plane/API Server evenly across three zones in that region. Regional clusters also spread the worker nodes evenly across those same three zones to reduce the impact of a Google Cloud zonal outage.

  * ####  Google Kubernetes Engine only one cluster per project link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Project, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_1`

Details

This rule identifies projects with multiple Google Kubernetes Engine clusters, enabling proactive measures to simplify management, optimize resource utilization, and reduce costs associated with unnecessary cluster complexity.

  * ####  Google Kubernetes Engine pod notifications enabled link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Notifications, Pub/Sub, Monitoring, Operations, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if Pub/Sub notifications for Google Kubernetes Engine cluster events are enabled. This feature allows you to receive notifications about significant cluster lifecycle events (like upgrades, node pool changes) via a Pub/Sub topic, enabling proactive monitoring and automation. This rule examines the notificationConfig.pubsub.enabled field. A violation is generated if this field is missing or set to false.

  * ####  Google Kubernetes Engine pod pid limits link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Kubernetes, NodePool, PodPidsLimit, Security, ResourceManagement, Kubelet, CSPR

Asset: `container.googleapis.com/NodePool`

Details

Checks if a Google Kubernetes Engine cluster Node Pool has a Pod PID limit configured. Setting a Pod PID limit helps prevent resource exhaustion where a single pod consumes all available Process IDs on a node. This rule examines the config.kubeletConfig.podPidsLimit field directly on the NodePool resource. A violation is generated if podPidsLimit is missing, null, or not a positive number.

  * ####  Google Kubernetes Engine private control plane link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Security, Networking, DNS Endpoint, CSPR, CoNa, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Ensure Google Kubernetes Engine clusters allow external traffic to their DNS control plane endpoints.

  * ####  Google Kubernetes Engine private nodes enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Kubernetes, Cluster, PrivateNodes, Security, Networking, VPC, CSPR, CoNa

Asset: `container.googleapis.com/Cluster`

Details

Checks if private nodes are enabled for a Google Kubernetes Engine cluster. Enabling private nodes ensures that nodes in the cluster do not have external IP addresses, enhancing security by reducing their direct exposure to the internet. Communication with the control plane and other Google services typically occurs over private connections (e.g., Private Google Access or VPC Service Controls). This rule examines the privateClusterConfig.enablePrivateNodes field. A violation is generated if this field is missing or set to false.

  * ####  Google Kubernetes Engine public endpoint link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Autopilot, Managed, Configuration, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if a Google Kubernetes Engine (Google Kubernetes Engine) cluster is public. Ensure all Google Kubernetes Engine clusters as private clusters with the enableprivateendpoint flag. This is the highest level of restricted access wherein the clusters control plane node is inaccessible from the public internet.

  * ####  Google Kubernetes Engine regional cluster link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Reliability, High Availability, BCDR, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Ensure Google Kubernetes Engine clusters are configured as regional clusters to provide high availability by replicating the control plane and nodes across multiple zones. Zonal clusters are susceptible to singlezone outages, which can severely impact application availability and business continuity.

  * ####  Google Kubernetes Engine release channel unspecified link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, CLuster, Upgrade, Security, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if a release channel is set for Google Kubernetes Engine clusters. Subscribe to a release channel to automate version upgrades to the Google Kubernetes Engine cluster. Release channels also reduce version management complexity to the number of features and level of stability required.

  * ####  Google Kubernetes Engine sandbox gvisor link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Google Kubernetes Engine, Security, Compute, CoNa, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Ensure Google Kubernetes Engine clusters contain at least one GVISOR-enabled node pool.

  * ####  Google Kubernetes Engine shielded nodes disabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: GKE, Security, CSPR, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Verifies that GKE Node Pools have Shielded Instance Config enabled (Secure Boot and Integrity Monitoring).

  * ####  Google Kubernetes Engine vertical scaling enabled link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Google Kubernetes Engine, Kubernetes, Cluster, VPA, VerticalPodAutoscaling, Autoscaling, Optimization, CSPR

Asset: `container.googleapis.com/Cluster`

Details

Checks if Vertical Pod Autoscaling (VPA) is enabled for a Google Kubernetes Engine cluster. VPA automatically adjusts the CPU and memory requests for pods, optimizing resource allocation and potentially improving performance and costefficiency. This rule examines the verticalPodAutoscaling.enabled field within the clusters configuration. A violation is generated if this field is missing or set to false, indicating VPA is not active.

  * ####  Google Kubernetes Engine workload identity link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Security, IAM, CSPR, CoNa, MVSP

Asset: `container.googleapis.com/Cluster`

Details

Ensure Workload Identity is enabled on Google Kubernetes Engine clusters.

  * ####  K8s automatic container scanning enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Project, Container, Auto Scanning, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_2`

Details

Enable automated container scanning to proactively detect vulnerabilities, thereby bolstering application security, enhancing operational reliability, maintaining performance integrity, and mitigating costly breach risks.

  * ####  K8s container security enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Google Kubernetes Engine, Kubernetes, Cluster, Security, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_2`

Details

Checks if your are using the Google Kubernetes Engine Security Posture Dashboard.

  * ####  K8s on demand container scanning enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Project, Container, On Demand Scanning, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_2`

Details

Enable container ondemand scanning to proactively detect vulnerabilities in your container images, thereby safeguarding your applications, ensuring operational reliability, and preventing costly security incidents.




### Google Cloud Best Practices - IAM (75 results)

  * ####  Api keys missing restrictions link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Security, APIKey, CSPR, MVSP

Asset: `apikeys.googleapis.com/Key`

Details

Verifies that API keys have application or IP restrictions configured to prevent unauthorized use.

  * ####  IAM basic group on folder link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

This rule identifies groups assigned overly broad basic roles (e.g., Owner, Editor) at the folder level, enabling customers to enforce the principle of least privilege, which significantly reduces security risks from excessive permissions and simplifies access governance.

  * ####  IAM basic group on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

This rule identifies groups that are assigned the highly permissive basic roles (such as Owner or Editor) at the organization level. Its a critical check to prevent widespread security vulnerabilities and ensures adherence to the principle of least privilege across all your cloud resources.

  * ####  IAM basic group on project link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Reduce security risks and prevent unintended project alterations by identifying groups with overly broad basic roles (such as Owner or Editor), thereby enforcing least privilege for enhanced operational stability.

  * ####  IAM basic service account on folder link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

Identifies service accounts granted overly permissive basic roles (such as Owner or Editor) at the folder level, crucial for enforcing the principle of least privilege to bolster security, maintain operational reliability, and control costs.

  * ####  IAM basic service account on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Ensure service accounts at the organization level do not possess broad basic roles, a critical step to uphold the principle of least privilege, prevent widespread security breaches, and maintain operational reliability.

  * ####  IAM basic service account on project link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

This rule identifies service accounts that are granted overly permissive basic roles (such as Owner or Editor) at the project level. This rule enables proactive enforcement of the principle of least privilege to significantly reduce security risks and limit the potential impact of compromised credentials.

  * ####  IAM basic user on folder link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

Identifying users with overly permissive basic roles (e.g., Owner, Editor) at the folder level is crucial for enforcing least privilege, which directly enhances your security posture, improves operational stability by preventing unintended changes.

  * ####  IAM basic user on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Identifying individual users with broad basic roles at the organization level is critical to mitigate risks of widespread unauthorized access or accidental changes, safeguarding your cloud environments security, reliability, and costefficiency.

  * ####  IAM basic user on project link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Flagging direct assignment of broad basic roles to individual users at the project level enhances security and simplifies access management by encouraging adherence to the principle of least privilege via groupbased permissions.

  * ####  IAM billing admin principals on billing link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, admin, Security, CSPR, CoNa, MVSP

Asset: `cloudbilling.googleapis.com/BillingAccount`

Details

This rule enhances financial security by identifying principals with broad billing administrator privileges at the billing account level, and helps you prevent unauthorized spending and ensure robust cost governance.

  * ####  IAM billing admin principals on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, admin, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Strengthen financial governance and security by identifying principals with direct organizationlevel billing administrator privileges, crucial for preventing unauthorized widespread billing modifications and enforcing the principle of least privilege.

  * ####  IAM billing admin user on billing link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, admin, Security, CSPR, CoNa, MVSP

Asset: `cloudbilling.googleapis.com/BillingAccount`

Details

Detecting individual users with direct Billing Account Administrator privileges is crucial for mitigating financial risks and preventing service disruptions by enforcing the principle of least privilege.

  * ####  IAM billing admin user on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, admin, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Enhance security, reliability, and cost control by restricting broad billing administrator permissions for individual user accounts at the organization level, thereby minimizing risks of unauthorized changes, service disruptions, and financial impact.

  * ####  IAM billing costs manager principals on billing link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudbilling.googleapis.com/BillingAccount`

Details

Ensures only authorized individuals can view and export billing account cost data, safeguarding sensitive financial information and supporting stringent cost governance.

  * ####  IAM billing costs manager principals on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Identifies principals with organizationlevel billing cost manager roles, helping you enforce the principle of least privilege to safeguard sensitive, comprehensive billing data and maintain appropriate cost visibility controls.

  * ####  IAM billing costs manager user on billing link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudbilling.googleapis.com/BillingAccount`

Details

Ensure robust cost governance by restricting the Billing Costs Manager role for individual users at the billing account level, preventing potential budget misconfigurations and maintaining clear accountability for financial operations.

  * ####  IAM billing costs manager user on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Enhances financial security and cost control by identifying individual user accounts with organizationwide billing cost management permissions, thereby promoting least privilege and reducing risk.

  * ####  IAM billing creator domains on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Detects domains assigned the Billing Account Creator role at the organization level, a crucial check to prevent unauthorized billing account proliferation and maintain robust financial oversight.

  * ####  IAM billing creator principals on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

This rule identifies principals with organizationlevel billing creator privileges, crucial for preventing uncontrolled cloud spending and ensuring stringent financial governance over new billing account creation.

  * ####  IAM billing creator user on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

This rule identifies users with organizationlevel billing creation rights to prevent uncontrolled cloud spending and enforce critical financial governance.

  * ####  IAM billing user principals on billing link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudbilling.googleapis.com/BillingAccount`

Details

Preventing the assignment of the Billing Account User role to the overly broad principal identifier at the billing account level is critical to protect sensitive financial data and control spending by ensuring only specific, intended users or groups can manage billing.

  * ####  IAM billing user principals on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Ensures least privilege by identifying principals with the Billing Account User role at the organization level, crucial for safeguarding sensitive financial data and strengthening cost governance.

  * ####  IAM billing user user on billing link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudbilling.googleapis.com/BillingAccount`

Details

Identifies individual user accounts directly assigned billing user roles, promoting groupbased permissions for enhanced security, simplified administration, and robust cost control.

  * ####  IAM billing user user on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

This rule enhances security by identifying roles/billing.user assignments at the organization level, which prevents overly broad access to sensitive financial data and enforces the principle of least privilege.

  * ####  IAM billing viewer principals on billing link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudbilling.googleapis.com/BillingAccount`

Details

This rule enhances security by identifying principals with direct billing account viewer roles, ensuring adherence to least privilege to prevent unintended broad access to sensitive billing information.

  * ####  IAM billing viewer principals on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Secure sensitive financial data and enforce least privilege by identifying principals with organizationlevel billing viewer access, thereby minimizing risks of unauthorized information exposure.

  * ####  IAM billing viewer user on billing link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudbilling.googleapis.com/BillingAccount`

Details

Pinpoints users directly assigned billing viewer roles at the billing account level, enabling enforcement of least privilege to safeguard sensitive financial data and prevent unauthorized cost exposure.

  * ####  IAM billing viewer user on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, owner, organization, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

This rule enhances financial data security by identifying individual users with organizationwide Billing Viewer access, crucial for enforcing least privilege and minimizing sensitive cost exposure.

  * ####  IAM cross domain access link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Security, CSPR, MVSP

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that IAM policies do not grant access to allUsers or allAuthenticatedUsers.

  * ####  IAM group can create project at folder level link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, project creator, folder, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

Detects if groups possess project creator roles at the folder level, enabling proactive governance to prevent resource sprawl, enforce security baselines, and control costs.

  * ####  IAM group can create project at organization level link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, project creator, organization, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

This rule identifies groups with organizationwide project creation capabilities, helping you prevent uncontrolled project sprawl and associated costs while strengthening security and governance over resource provisioning.

  * ####  IAM organization admin link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, billing account, admin, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Identifying highly privileged Organization Administrator assignments enables you to secure your entire cloud environment by strictly controlling ultimate access, thereby preventing widespread security vulnerabilities and operational disruptions.

  * ####  IAM organization admin redundancy link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, organization, admin, redundancy, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Enforces organization admin redundancy. Avoid having a single organization administrator to prevent lockout scenarios and ensure administrative continuity. Ensure there are at least two administrators.

  * ####  IAM owner group on folder link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

This rule flags groups holding Owner permissions on folders, a critical check to prevent widespread security vulnerabilities and accidental operational disruptions by enforcing tighter access control.

  * ####  IAM owner group on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Identifies groups with organizationlevel owner permissions, crucial for preventing catastrophic security breaches and operational failures stemming from indirect, hardtoaudit privilege escalations through group membership changes.

  * ####  IAM owner group on project link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

This rule identifies Google Groups assigned the powerful owner role at the project level, which is crucial for mitigating security vulnerabilities from excessive permissions, preventing operational disruptions, and controlling unintended cloud expenditures.

  * ####  IAM owner service account on folder link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

This rule critically enhances security by identifying service accounts with highly permissive Owner roles at the folder level, essential for mitigating risks from excessive privileges and enforcing the principle of least privilege for robust resource control.

  * ####  IAM owner service account on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Safeguard your organization against critical security threats by detecting service accounts with excessive owner privileges at the organization level, preventing widespread unauthorized control and manipulation of all cloud resources.

  * ####  IAM owner service account on project link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

This rule identifies service accounts with projectlevel owner roles, a critical security risk. This rule help enforce the principle of least privilege, which is crucial for enhancing security, ensuring operational reliability, and preventing uncontrolled cloud spend.

  * ####  IAM owner user on folder link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

This check identifies userassigned Owner roles at the folder level, enabling proactive mitigation of security risks from excessive permissions and prevention of unintended, potentially costly or disruptive, resource modifications.

  * ####  IAM owner user on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Detects users assigned the organizationlevel owner role, a critical check to prevent broad, unintended changes that could compromise security, disrupt service reliability, impair performance, and lead to uncontrolled costs.

  * ####  IAM owner user on project link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, owner, organization, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Prevents unintended costs by identifying users assigned the owner role, thereby mitigating risks from excessive privileges.

  * ####  IAM personal gmail accounts disallowed project link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Identifies project-level IAM bindings that grant permissions to personal Gmail accounts (e.g., @gmail.com or @googlemail.com). Best practices dictate restricting access to corporate domain identities to minimize risk of data leakage and credential compromise.

  * ####  IAM project publicly exposed link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Tags: IAM, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Identifies project-level IAM bindings that grant permissions to allUsers or allAuthenticatedUsers. Publicly exposing projects allows unauthenticated access to project resources and structure, representing a critical security risk.

  * ####  IAM service account group token creator on folder link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

Strengthen security by preventing broad, groupbased impersonation of service accounts at the folder level, thus reducing the risk of privilege escalation and unauthorized resource access.

  * ####  IAM service account group token creator on organization link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

This rule identifies groups that are assigned organizationlevel Service Account User or Token Creator roles, and helps you mitigate critical security risks such as privilege escalation and broad resource compromise by enforcing least privilege principles.

  * ####  IAM service account group token creator on project link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Enhances project security by identifying groups with Service Account User or Token Creator roles, enabling proactive risk mitigation from overly broad impersonation capabilities and simplifying access audit trails.

  * ####  IAM service account principal token creator on folder link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

Check to detect service account user and token creator on principals at folder level

  * ####  IAM service account principal token creator on organization link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

This rule identifies principals with organizationlevel service account user or token creator roles, enabling proactive enforcement of least privilege to prevent widespread system compromise and significantly reduce security risk.

  * ####  IAM service account principal token creator on project link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

This rule detects principals with projectlevel Service Account User or Token Creator roles, which grant sweeping and highrisk impersonation capabilities over any service account. This role detection helps you enforce the principle of least privilege and drastically reduce the security risks.

  * ####  IAM service account principalset token creator on folder link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

Identifies principalSet assignments with Service Account User or Token Creator roles at the folder level, preventing excessive service account impersonation privileges to enhance security and enforce least privilege.

  * ####  IAM service account principalset token creator on organization link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Reduces organizational risk by identifying principalSets with overly broad service account impersonation or token creation privileges at the organization level, preventing potential widespread security breaches and unauthorized resource access.

  * ####  IAM service account principalset token creator on project link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Restricting service account user/token creator roles for broad principalSets (such as groups or domains) at the project level mitigates widespread privilege escalation risks and unauthorized impersonation, enhancing overall project security posture.

  * ####  IAM service account user token creator on folder link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

Check to detect service account user and token creator on users at folder level

  * ####  IAM service account user token creator on organization link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Check to detect service account user and token creator on users at organization level

  * ####  IAM service account user token creator on project link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

This rule identifies users with extensive projectlevel service account impersonation or token creation privileges, and helps preemptively neutralize major security vulnerabilities, such as privilege escalation via compromised accounts, thereby protecting vital assets and curtailing potential financial losses from breaches.

  * ####  IAM secret reader folder link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, secret, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

Strengthen data protection and helps you enforce the principle of least privilege by identifying and rectifying overly broad folderlevel permissions that grant widespread access to secrets, minimizing the risk of unauthorized exposure.

  * ####  IAM secret reader organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, secret, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

This rule identifies organizationlevel IAM roles granting broad secret access (such as Owner, Secret Manager Admin/Accessor), crucial for enforcing the principle of least privilege and minimizing the risk of widespread sensitive data exposure.

  * ####  IAM secret reader project link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, secret, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

This rule identifies projectlevel IAM bindings granting overly permissive roles (such as roles/owner, roles/secretmanager.admin, or roles/secretmanager.secretAccessor) with broad access to all secrets. This rule helps you enforce the principle of least privilege, thereby safeguarding sensitive data and reducing the risk of costly security incidents.

  * ####  IAM service account key expiration longer 90 days link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account key, Security, CSPR

Asset: `iam.googleapis.com/ServiceAccountKey`

Details

Enforcing a 90day rotation for usermanaged service account keys significantly reduces the risk of prolonged unauthorized access from compromised credentials, safeguarding your critical services and preventing costly security incidents.

  * ####  IAM service account key older 90 days link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account key, Security, CSPR

Asset: `iam.googleapis.com/ServiceAccountKey`

Details

Identifying active usermanaged service account keys older than 90 days enables proactive rotation, significantly reducing the attack surface and minimizing risks of unauthorized access or credential compromise.

  * ####  IAM service account key user managed link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account key, Security, CSPR

Asset: `iam.googleapis.com/ServiceAccountKey`

Details

Usermanaged service account keys lack automatic rotation, increasing security vulnerabilities and operational burden; migrating to Googlemanaged keys enhances security and simplifies key management.

  * ####  IAM service account no expiration date link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account key, Security, CSPR

Asset: `iam.googleapis.com/ServiceAccountKey`

Details

Define expiration dates for usermanaged service account keys to limit their active lifespan, which is crucial for minimizing security risks and protecting your resources from unauthorized access if a key is compromised.

  * ####  IAM service account user admin folder link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, service account, admin, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

This rule enhances security by detecting principals on a folder who can both use and fully manage service accounts, a critical overpermissioning that, if compromised, dramatically increases the risk of widespread unauthorized access and resource manipulation.

  * ####  IAM service account user admin organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, service account, admin, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

This rule identifies principals possessing both Service Account User and Admin roles at the organization level, a critical check to prevent significant privilege escalation and enforce least privilege, thereby safeguarding your resources and maintaining operational reliability.

  * ####  IAM service account user admin project link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, service account, admin, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Identifies principals with redundant Service Account User and Admin roles on a project to help you enforce the principle of least privilege, simplifying IAM and bolstering security.

  * ####  IAM service account user admin link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, service account, admin, Security, CSPR, CoNa, MVSP

Asset: `iam.googleapis.com/ServiceAccount`

Details

This rule identifies principals holding both Service Account User and Admin roles at the organization level, a critical check for enforcing least privilege to reduce the attack surface and minimize risks from excessive permissions.

  * ####  IAM service account with user managed key link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, service account key, Security, CSPR

Asset: `iam_ServiceAccount_RESOURCE_1`

Details

This rule identifies service accounts employing usermanaged keys, which necessitate manual rotation and pose a heightened security risk. This rule helps you strengthen the security posture by transitioning to Googlemanaged keys or implementing rigorous key lifecycle controls.

  * ####  IAM user can create project at folder level link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, project creator, folder, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

This rule identifies users with direct project creation privileges at the folder level, critical for preventing uncontrolled resource sprawl to safeguard budgets, enforce security policies, and maintain operational stability.

  * ####  IAM user can create project at organization level link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: IAM, project creator, folder, Security, CSPR, CoNa

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Validating that project creation rights are not granted to users directly at the organization level helps enforce least privilege, preventing uncontrolled resource sprawl to improve cost management, security, and overall governance.

  * ####  Pab policy wildcard permissions link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: PAB, policy, wildcard, permission, Security

Asset: `iam.googleapis.com/PrincipalAccessBoundaryPolicy`

Details

Flags Principal Access Boundary (PAB) policies that allow wildcard '*' permissions, which grants access to all permissions across all services, defeating the purpose of a boundary.

  * ####  Primitive roles disallowed folder link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Security, Least Privilege, CSPR

Asset: `cloudresourcemanager.googleapis.com/Folder`

Details

Flag disallowed primitive roles (owner, editor) in folder IAM policies

  * ####  Primitive roles disallowed organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Security, Least Privilege, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Flag disallowed primitive roles (owner, editor) in organization IAM policies

  * ####  Primitive roles disallowed project link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, Security, Least Privilege, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Flag disallowed primitive roles (owner, editor) in project IAM policies




### Google Cloud Best Practices - Memorystore for Memcache (2 results)

  * ####  Memorystore instance ha link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, High Availability, BCDR

Asset: `memcache.googleapis.com/Instance`

Details

Verifies that Memorystore instances are configured with multiple nodes to ensure high availability. Singlenode configurations lack redundancy, increasing the risk of service disruption during failures.

  * ####  Memorystore instance zonal ha link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, High Availability, BCDR, CoNa

Asset: `memcache.googleapis.com/Instance`

Details

Verifies that Memorystore Memcached instances are distributed across multiple distinct zones to ensure high availability. Relying on a single zone creates a single point of failure, risking service disruption during zonal outages.




### Google Cloud Best Practices - Memorystore for Redis (8 results)

  * ####  Memorystore instance persistence link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Redis, Memorystore, Reliability, DisasterRecovery, Persistence

Asset: `redis.googleapis.com/Instance`

Details

Checks if Memorystore for Redis Standard Tier instances have persistence enabled. Persistence ensures data recovery from disk. This rule flags Standard instances where persistenceMode is disabled or missing.

  * ####  Redis auth enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Redis, Memorystore, Instance, Security, Authentication, AccessControl

Asset: `redis.googleapis.com/Instance`

Details

Checks if Memorystore for Redis instances have Redis AUTH enabled. Redis AUTH requires clients to authenticate with a password before accessing the database. This is a fundamental security measure to prevent unauthorized access. This rule flags instances where authEnabled is false.

  * ####  Redis authorized network set link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Redis, Memorystore, Instance, Security, Network, AccessControl, VPC, CoNa

Asset: `redis.googleapis.com/Instance`

Details

Checks if Memorystore for Redis instances have an authorized network configured. Restricting access to a specific VPC network limits the potential attack surface. While this rule doesnt validate the specific network, it checks that some network restriction is in place. A more robust check would compare against a list of allowed networks (using parameters).

  * ####  Redis instance multi zone link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Cache, HighAvailability, Locations

Asset: `redis.googleapis.com/Instance`

Details

Checks if Memorystore Redis primary and replica are in different zones. In STANDARD_HA, placing replica in same zone removes zonal resiliency.

  * ####  Redis instance tier ha link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Cache, HighAvailability, Resiliency

Asset: `redis.googleapis.com/Instance`

Details

Checks if Memorystore for Redis instance is using the STANDARD_HA tier to ensure high availability with automatic failover to a replica.

  * ####  Redis maintenance window configured link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Redis, Memorystore, Instance, Availability, Reliability, Maintenance

Asset: `redis.googleapis.com/Instance`

Details

Checks if Memorystore for Redis instances have a maintenance window configured. A defined maintenance window allows you to control when potentially disruptive maintenance operations occur. Without a defined window, updates can happen at any time, which could impact application availability. This rule flags instances that do not have a maintenancePolicy defined.

  * ####  Redis no basic tier link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Redis, Memorystore, Instance, Availability, Reliability, HighAvailability, CSPR

Asset: `redis.googleapis.com/Instance`

Details

Checks if Memorystore for Redis instances are using the BASIC tier. The BASIC tier provides a single Redis node and does not offer replication or automatic failover. This makes it unsuitable for production workloads that require high availability. This rule flags any instance using the BASIC tier. Upgrading to STANDARD_HA is strongly recommended for production environments.

  * ####  Redis standard ha has replicas link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Redis, Memorystore, Instance, Availability, Reliability, HighAvailability, Performance, CSPR

Asset: `redis.googleapis.com/Instance`

Details

Checks if Memorystore for Redis instances is using the STANDARD_HA tier and has at least one replica. While STANDARD_HA provides high availability features, a replica count of zero eliminates the redundancy benefits. This rule flags instances not on STANDARD_HA and with zero replicas configured. Increasing the replica count to at least 1 (and ideally 2 or more, up to 5) is recommended for true high availability.




### Google Cloud Best Practices - Memorystore for Redis Cluster (3 results)

  * ####  Redis cluster ha link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Redis, Cluster, Reliability, HighAvailability, Resiliency

Asset: `redis.googleapis.com/Cluster`

Details

Checks if Memorystore for Redis Cluster instances are configured with Multizone availability. Singlezone deployments create a single point of failure and are not resilient to zonal outages.

  * ####  Redis cluster persistence link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Redis, Memorystore, Cluster, Reliability, DisasterRecovery, Persistence,

Asset: `redis.googleapis.com/Cluster`

Details

Checks if Memorystore for Redis Cluster resources have persistence enabled. Persistence (RDB or AOF) is critical for disaster recovery in the event of total cluster failure. This rule flags Redis Clusters where persistenceConfig.mode is not set to RDB or AOF.

  * ####  Redis cluster replica multi zone link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Cache, HighAvailability, Locations

Asset: `redis.googleapis.com/Cluster`

Details

Verifies Memorystore Redis Cluster replica placement is multi-zone and at least 1 replica per shard is configured.




### Google Cloud Best Practices - NetApp Volumes (1 results)

  * ####  Netapp volume snapshot policy enabled link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Reliability, Storage, NetApp, Backup, DataProtection

Asset: `netapp.googleapis.com/Volume`

Details

Directly validates scheduling configurations and snapshot policy state for Google Cloud NetApp Volumes to ensure point-in-time recovery is active.




### Google Cloud Best Practices - Networking (5 results)

  * ####  Compute default deny firewall logging link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Networking, Firewall, Security, CSPR, MVSP

Asset: `compute.googleapis.com/Firewall`

Details

Verifies that default deny firewall rules have logging enabled.

  * ####  Compute firewall iap tcp tunnel link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Networking, Firewall, Security, CSPR, IAP

Asset: `compute.googleapis.com/Firewall`

Details

Verifies that firewall rules allowing IAP TCP forwarding are restricted to the Google IAP IP range (35.235.240.0/20).

  * ####  Compute hierarchical firewall policies logging link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Networking, Firewall, Security, CSPR

Asset: `compute.googleapis.com/FirewallPolicy`

Details

Verifies that Hierarchical Firewall Policies have logging enabled.

  * ####  Compute load balancer missing source ranges link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Networking, Firewall, LB, Security, CSPR

Asset: `compute.googleapis.com/Firewall`

Details

Verifies that firewall rules associated with Load Balancers explicitly define source IP ranges.

  * ####  Compute region backend service cdn link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Networking, Security, CDN, CSPR

Asset: `compute.googleapis.com/RegionBackendService`

Details

Verifies that Regional Backend Services have Cloud CDN enabled.




### Google Cloud Best Practices - Organization Policy Service (58 results)

  * ####  Organization policy appengine disable code download link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Appengine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the appengine.disableCodeDownload organization policy is configured on the project or its parents to prevent unauthorized code downloads and protect against potential security risks.

  * ####  Organization policy cloudbuild allowed integrations link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Cloud Build, Security, CSPR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy cloudbuild.allowedIntegrations is configured on the project or any parent to restrict external services that can invoke build triggers.

  * ####  Organization policy cloudfunctions allowed ingress link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Cloud Functions, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the cloudfunctions.allowedIngressSettings organization policy is enforced on the project or any parent, restricting ingress traffic to Cloud Functions.

  * ####  Organization policy compute disable guest attributes access link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.disableGuestAttributesAccess organization policy is enforced on the project or any parent, preventing potential unauthorized access to guest attributes.

  * ####  Organization policy compute disable internet endpoint group link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.disableInternetNetworkEndpointGroup organization policy is enforced on the project or its parents, preventing potential security vulnerabilities.

  * ####  Organization policy compute disable nested virtualization link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Compute Engine, Security, CSPR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy compute.disableNestedVirtualization is configured on the project or any parent, preventing unauthorized use of nested virtualization.

  * ####  Organization policy compute disable serial port logging link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Compute Engine, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.disableSerialPortLogging organization policy is enforced on the project or any parent, preventing potential security risks from unauthorized serial port access.

  * ####  Organization policy compute disables serial port access link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.disableSerialPortAccess organization policy is enforced on the project or its parents, preventing unauthorized access to serial ports.

  * ####  Organization policy compute require os login link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.requireOsLogin organization policy is enforced to ensure OS Login is enabled on the project or its parents, preventing unauthorized access to virtual machines.

  * ####  Organization policy compute require shielded VM link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Compute Engine, Security, CSPR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy compute.requireShieldedVm is enforced on the project or its parents, ensuring that only shielded VMs are created, thus enhancing security.

  * ####  Organization policy compute restrict dedicated interconnect link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.restrictDedicatedInterconnectUsage organization policy is enforced on the project or any parent, preventing potential risks associated with unrestricted dedicated interconnect usage.

  * ####  Organization policy compute restrict load balancer creation link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.restrictLoadBalancerCreationForTypes organization policy is enforced to prevent the creation of insecure load balancers on the project or its parents.

  * ####  Organization policy compute restrict protocol forward creation link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy compute.restrictProtocolForwardingCreationForTypes is configured on the project or any parent, to prevent potential security vulnerabilities.

  * ####  Organization policy compute restrict shared VPC host projects link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy compute.restrictSharedVpcHostProjects is configured on the project or any parent, preventing potential security vulnerabilities.

  * ####  Organization policy compute restrict shared VPC subnetworks link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.restrictSharedVpcSubnetworks organization policy is enforced on the project or its parents, ensuring only approved subnets are used, thereby enhancing network security.

  * ####  Organization policy compute restrict VPC peering link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy compute.restrictVpcPeering is enforced on the project or its parents, preventing potential unauthorized VPC peering.

  * ####  Organization policy compute restrict vpn peer ips link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy compute.restrictVpnPeerIPs is configured on the project or any parent, preventing unauthorized VPN peer IP access.

  * ####  Organization policy compute restrict xpn project lien removal link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.restrictXpnProjectLienRemoval organization policy is enforced on the project or its parents, preventing unauthorized removal of project liens.

  * ####  Organization policy compute skip default network creation link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Compute Engine, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.skipDefaultNetworkCreation organization policy is enforced on the project or its parents, preventing potential security vulnerabilities.

  * ####  Organization policy compute Cloud Storage resource use restrictions link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Compute Engine, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy compute.storageResourceUseRestrictions is enforced to ensure that storage resource use restrictions are configured on the project or its parents, preventing potential security vulnerabilities.

  * ####  Organization policy compute trusted image projects link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy compute.trustedImageProjects is configured on the project or any parent, preventing the use of untrusted images.

  * ####  Organization policy compute VM can IP forward link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Compute Engine, Security, CSPR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.vmCanIpForward organization policy is configured on the project or its parents to allow VMs to forward IP traffic, ensuring proper network functionality.

  * ####  Organization policy compute VM external IP access link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Compute Engine, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.vmExternalIpAccess organization policy is enforced on the project or its parents, preventing potential security vulnerabilities.

  * ####  Organization policy essentialcontacts allowed domains link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Essential Contacts, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the essentialcontacts.allowedContactDomains organization policy is enforced on the project or any parent, restricting the domains allowed for essential contacts.

  * ####  Organization policy functions allowed VPC connector egress link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Cloud Function, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the cloudfunctions.allowedVpcConnectorEgressSettings organization policy is enforced on the project or its parents, preventing unauthorized egress settings for Cloud Functions, thereby enhancing security.

  * ####  Organization policy functions require VPC connector link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Cloud Function, Security, CSPR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the cloudfunctions.requireVPCConnector organization policy is enforced to ensure Cloud Functions use VPC connectors, enhancing network security.

  * ####  Organization policy Compute Engine disable psc creation link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Compute Engine, PSC, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy compute.disablePrivateServiceConnectCreationForConsumers is configured to prevent unauthorized Private Service Connect creation.

  * ####  Organization policy Google Cloud detailed audit logging mode link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Cloud Logging, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy gcp.detailedAuditLoggingMode is configured on the project or any parent to enable detailed audit logging, aiding in comprehensive security monitoring and compliance.

  * ####  Organization policy Google Cloud disable cloud logging link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Cloud Logging, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy gcp.disableCloudLogging is configured on the project or any parent to ensure that Cloud Logging is properly enforced.

  * ####  Organization policy Google Cloud resource locations link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the gcp.resourceLocations organization policy is enforced on the project or any parent, ensuring resources are created in the designated geographic locations, thereby meeting compliance requirements.

  * ####  Organization policy Google Cloud restrict non CMEK services link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, CMEK, KMS, Security, Encryption, CSPR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy gcp.restrictNonCmekServices is enforced on the project or its parents. This policy restricts the creation of resources without Customer-Managed Encryption Keys (CMEK), ensuring data-at-rest is encrypted according to organization standards.

  * ####  Organization policy Google Cloud restrict tls version link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Security, TLS, CSPR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy gcp.restrictTLSVersion is configured on the project or any parent to restrict the TLS versions supported by Google APIs.

  * ####  Organization policy IAM allow disable service account key creation link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, IAM, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Reduces your attack surface by identifying active ingress firewall rules that expose uncommon network protocols (not TCP, UDP, or ICMP) to the internet, preventing potential breaches through unmonitored services.

  * ####  Organization policy IAM allow service account credential lifetime extension link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, IAM, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy iam.allowServiceAccountCredentialLifetimeExtension is configured on the project or any parent, ensuring that service account credential lifetime extensions are managed to maintain security.

  * ####  Organization policy IAM allowed policy member domains link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Tags: Organization policy, IAM, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the iam.allowedPolicyMemberDomains organization policy is enforced on the project or its parents, ensuring only approved domains can be added as policy members, enhancing security by preventing unauthorized access.

  * ####  Organization policy IAM auto grants for default service account link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, IAM, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the iam.automaticIamGrantsForDefaultServiceAccounts organization policy is enforced on the project or any parent to ensure that the default service accounts are not automatically granted IAM roles, improving security.

  * ####  Organization policy IAM disable service account creation link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, IAM, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the iam.disableServiceAccountCreation organization policy is enforced to prevent the creation of service accounts, reducing the risk of unauthorized access and potential security breaches.

  * ####  Organization policy IAM disable service account key upload link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, IAM, Security, CSPR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the iam.disableServiceAccountKeyUpload organization policy is enforced on the project or any parent, preventing potential security risks associated with unauthorized service account key uploads.

  * ####  Organization policy IAM disable workload identity cluster link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, IAM, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the iam.disableWorkloadIdentityClusterCreation organization policy is enforced on the project or any parent, preventing the creation of workload identity clusters if the policy is not configured.

  * ####  Organization policy IAM workload identity pool providers link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, IAM, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the iam.workloadIdentityPoolProviders organization policy is enforced on the project or any parent, ensuring that workload identity pool providers are correctly configured to prevent unauthorized access.

  * ####  Organization policy restrict non confidential computing link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Compute Engine, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy compute.restrictNonConfidentialComputing is configured on the project or its parents, preventing the use of nonconfidential computing resources that could lead to data exposure.

  * ####  Organization policy restrict partner interconnect usage link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Compute Engine, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the compute.restrictPartnerInterconnectUsage organization policy is enforced on the project or any parent, preventing potential unauthorized usage of Partner Interconnect.

  * ####  Organization policy run allowed ingress link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Cloud Run, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the run.allowedIngress organization policy is enforced on the project or any parent, restricting ingress traffic to Cloud Run services.

  * ####  Organization policy serviceuser services link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Organization policy, Services, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the organization policy serviceuser.services is configured on the project or its parents, preventing potential security vulnerabilities.

  * ####  Organization policy sql restrict authorized networks link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Cloud Sql, Security, CSPR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the sql.restrictAuthorizedNetworks organization policy is enforced on the project or its parents, preventing unauthorized access to Cloud SQL instances from unapproved networks.

  * ####  Organization policy sql restrict public IP link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Cloud Sql, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the sql.restrictPublicIp organization policy is enforced on the project or its parents, preventing potential security vulnerabilities by restricting public IP access to Cloud SQL instances.

  * ####  Organization policy Cloud Storage public access prevention link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Cloud Storage, Storage, Security, CSPR

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the storage.publicAccessPrevention organization policy is enforced on the project or any parent, preventing public access to Cloud Storage buckets.

  * ####  Organization policy Cloud Storage retention policy seconds link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Organization policy, Cloud Storage, Security, CSPR, CoNa

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the storage.retentionPolicySeconds organization policy is enforced on the project or its parents to ensure data is protected from accidental or malicious deletion.

  * ####  Organization policy Cloud Storage uniform bucket level access link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Organization policy, Cloud Storage, Storage, Security, CSPR, CoNa, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_3`

Details

Verifies that the storage.uniformBucketLevelAccess organization policy is enforced on the project or any parent, ensuring consistent access control for all objects within a bucket and preventing potential data breaches.

  * ####  Organization policy allowed contact domains link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: OrgPolicy, Security, Compliance, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that the essentialcontacts.allowedContactDomains organization policy is enforced.

  * ####  Organization policy allowed ingress settings link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: OrgPolicy, Security, Compliance, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that the cloudfunctions.allowedIngressSettings organization policy is enforced.

  * ####  Organization policy allowed worker pools link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: OrgPolicy, Security, Compliance, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that the cloudbuild.allowedWorkerPools organization policy is enforced.

  * ####  Organization policy disable audit logging exemption link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: OrgPolicy, Security, Compliance, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that the iam.disableAuditLoggingExemption organization policy is enforced.

  * ####  Organization policy disable bq omni aws link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: OrgPolicy, Security, Compliance, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that the bigquery.disableBQOmniAWS organization policy is enforced.

  * ####  Organization policy disable bq omni azure link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: OrgPolicy, Security, Compliance, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that the bigquery.disableBQOmniAzure organization policy is enforced.

  * ####  Organization policy disable non fips machine types link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: OrgPolicy, Security, Compliance, FIPS, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that the compute.disableNonFIPSMachineTypes organization policy is enforced. This ensures that non-FIPS compliant machine types cannot be created.

  * ####  Organization policy restrict cloud nat usage link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: OrgPolicy, Security, Compliance, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that the compute.restrictCloudNATUsage organization policy is enforced.

  * ####  Organization policy restrict service usage link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: OrgPolicy, Security, Compliance, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that the gcp.restrictServiceUsage organization policy is enforced.




### Google Cloud Best Practices - Resource Manager (3 results)

  * ####  Essential contacts link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Essential Contacts, Management, Compliance, CSPR, MVSP

Asset: `cloudresourcemanager_Project_RESOURCE_4`

Details

Flags Google Cloud projects that do not have valid essential contacts configured

  * ####  Project no folder link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: project, resource management, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Identifies projects created directly under an organization, which bypasses folderlevel policy inheritance essential for consistent governance, security posture, and cost management.

  * ####  Resourcemanager host projects link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Tags: Compute, Project, SharedVPC, HostProject, Networking, Organization, CSPR

Asset: `compute.googleapis.com/Project`

Details

Checks if a Google Cloud project is configured as a Shared VPC Host Project. Shared VPC allows an organization to connect resources from multiple projects to a common VPC network, hosted in a designated Host Project. This allows for centralized network administration. This rule identifies host projects by checking the xpnProjectStatus field within the projects Compute Engine metadata. A status of HOST indicates its a Shared VPC Host Project. This policy is informational, identifying projects with this specific configuration.




### Google Cloud Best Practices - SecOps (1 results)

  * ####  IAM data access logs link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: SecOps, Logging, IAM, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Project`

Details

Verifies that Data Access Logs (ADMIN_READ, DATA_WRITE, DATA_READ) are enabled globally at the project level.




### Google Cloud Best Practices - Secret Manager (2 results)

  * ####  Secret manager 90d rotation link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: SecretManager, Secret, Rotation, Security, Age, CSPR, CoNa

Asset: `secretmanager.googleapis.com/SecretVersion`

Details

Checks if a Secret Manager secret is both enabled and older than 90 days since its creation time. Regularly rotating secrets is a security best practice to minimize the impact of potential compromise. This rule examines two fields 1. state Checks if the secret is in the ENABLED state. 2. createTime Checks if the secrets creation time is more than 90 days in the past. A violation is generated if both conditions are true the secret is enabled and its createTime indicates its older than 90 days. The rule uses time.now_ns() and time.parse_rfc3339_ns() for accurate time comparisons.

  * ####  Secret manager replication multiregion link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Reliability, Security, SecretManager, HighAvailability, BCDR, CSPR, CoNa

Asset: `secretmanager.googleapis.com/Secret`

Details

Verifies that Secret Manager secrets are configured with a multi-regional replication policy (either automatic replication or user-managed replication with at least 2 distinct regions). Replicating secrets across multiple regions ensures high availability and disaster recovery.




### Google Cloud Best Practices - Security Command Center (1 results)

  * ####  Security Command Center not enabled on organization link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: IAM, scc, Security, CSPR

Asset: `cloudresourcemanager.googleapis.com/Organization`

Details

Activating Security Command Center (SCC) at the organization level provides essential, centralized visibility into security findings and compliance status, enabling proactive risk mitigation to safeguard your Google Cloud resources.




### Google Cloud Best Practices - Sensitive Data Protection (1 results)

  * ####  Google Cloud dlp service enabled link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: DLP, Sensitive Data Protection, Security, ServiceUsage, Compliance, CoNa

Asset: `serviceusage.googleapis.com/Service`

Details

Checks if the Sensitive Data Protection (DLP) service (dlp.googleapis.com) is enabled. Sensitive Data Protection helps you discover, classify, and protect your sensitive data.




### MySQL: General (7 results)

  * ####  Check that the Google Cloud Agent for Compute Workloads is set up correctly on all instances in the evaluation scope link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

Instances in the evaluation scope must have the Google Cloud Agent for Compute Workloads configured to run Workload Manager evaluations. If you have not configured the agent correctly, evaluation results can be incomplete or inaccurate. The minimum recommended version is 1.2.

Last updated: August 27, 2025

  * ####  Enable automatic restart for VMs running MySQL workloads link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To ensure that the VM restarts automatically in the event of a failure, enable the Compute Engine automatic restart policy for any VM that is running a MySQL workload.

Last updated: August 27, 2025

  * ####  Provision Hyperdisk with minimum IOPS and throughput link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

The default provisioned IOPS and throughput values for small Hyperdisks can be too low to guarantee proper performance. We recommend that you raise these values to a minimum of 10,000 IOPS and 1 GiB/s throughput. From November 10th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [Default performance](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#default-perf).

Last updated: November 10, 2025

  * ####  Set VM maintenance policy to MIGRATE for MySQL workloads link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To prevent any platform maintenance events from stopping or restarting a VM that is running MySQL workloads, the onHostMaintenance parameter for the VM must be set to the recommended option MIGRATE.

For more information, see [Set VM host maintenance policy](https://cloud.google.com/compute/docs/instances/setting-vm-host-options).

Last updated: August 27, 2025

  * ####  Do not run MySQL workloads on PD Standard or Hyperdisk Throughput disk types link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Google Cloud recommends that you do not run MySQL workloads on PD Standard and Hyperdisk Throughput disk types, because these are hard disk-based disks and might lead to degraded performance. From November 10th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [Persistent disk types](https://cloud.google.com/compute/docs/disks/persistent-disks#disk-types), [Hyperdisks](https://cloud.google.com/compute/docs/disks/hyperdisks), and [Hyperdisk Throughput](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput).

Last updated: November 10, 2025

  * ####  Ensure replication is sent to a machine in a different zone or region link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

To maintain proper high availability, we strongly recommend that you send your replication to a machine in a different zone or region from the primary location. From November 10th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [Well-Architected Framework: Reliability pillar](https://cloud.google.com/architecture/framework/reliability).

Last updated: November 10, 2025

  * ####  Ensure innodb_buffer_pool_size occupies a majority of the memory for the machine link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

For optimized performance, Google Cloud recommends allocating the innodb_buffer_pool_size parameter a 50% or greater share of the machine's memory. This ensures that the buffer pool has enough memory to store data and improve performance. This guideline doesn't apply to smaller VMs with less than 4 GB of total memory where such an allocation might not be possible. From November 10th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

Last updated: November 10, 2025




### OpenShift: Cost Optimization (1 results)

  * ####  Check hd storagepool link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift

Asset: `Openshift_Cluster`

Details

When you're using Google Cloud Hyperdisk storage class with your OpenShift cluster, we recommend that you use storage pools. This helps you achieve more efficient management of disk resources, improved performance predictability, and simplified scaling of block storage within your OpenShift environment.




### OpenShift: Operational Efficiency (6 results)

  * ####  Check filestore link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift

Asset: `Openshift_Cluster`

Details

It is recommended to use Google Cloud Filestore for shared storage (RWX) workloads for seamless infrastructure integration, performance reliability, and automated lifecycle management on Google Cloud if your required capacity size is more than 90 GiB.

  * ####  Check gmp monitoring link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift, Observability, Operational Efficiency, GMP, Prometheus

Asset: `Openshift_Cluster`

Details

It is recommended to configure application metric scraping using Google Cloud

  * ####  Check managed block Cloud Storage link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift

Asset: `Openshift_Cluster`

Details

For seamless infrastructure integration, performance reliability, and automated lifecycle management, we recommend that you use Google Cloud managed block storage solutions with your OpenShift cluster.

  * ####  Check observability sidecar injection link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift, Observability, Operational Efficiency

Asset: `Openshift_Cluster`

Details

Deploy OpenTelemetry Collector in Sidecar mode for application telemetry to guarantee better metrics collection isolation between applications

  * ####  Check prod link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift

Asset: `Openshift_Cluster`

Details

To consistently implement policy, monitor alerts, and allocate cost for your OpenShift cluster, we recommend that you apply the label `production` or `non-production` to the cluster. This label helps convey whether your cluster runs in a production or non-production environment.

  * ####  Check secret management usage link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift

Asset: `Openshift_Cluster`

Details

To handle sensitive information within OpenShift clusters that run on Google Cloud, use Secret Manager. This service lets you centralize the lifecycle management of secrets and enhance security by providing Identity and Access Management (IAM) based access control.




### OpenShift: Reliability (5 results)

  * ####  Check filestore regional link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift

Asset: `Openshift_Cluster`

Details

If using Filestore Zonal, consider using Filestore Regional if cost permits. Filestore Regional replicates filestore data across zones and ensures data availability during zonal failures.

  * ####  Check filestore zonal link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift

Asset: `Openshift_Cluster`

Details

Prefer Filestore Zonal or Regional over Filestore Basic tiers. Filestore Zonal/Regional has no downtime during maintenance (while Basic tiers do) and supports NFSv4, Custom Performance, Instance replication, and Snapshots.

  * ####  Check ha control plane nodes multiple zones link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Tags: Openshift

Asset: `Openshift_Cluster`

Details

It is recommended to distribute OpenShift control plane nodes across at least three different zones within a Google Cloud region to ensure High Availability (HA) and management layer operations even during zonal outages.

  * ####  Check ha worker nodes multiple zones link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Tags: Openshift

Asset: `Openshift_Cluster`

Details

It is recommended to provision OpenShift worker nodes across at least three different zones within a region to build a resilient infrastructure that can withstand zonal disruptions without impacting the availability of hosted workloads.

  * ####  Check last metric timestamp link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift

Asset: `Openshift_Cluster`

Details

To ensure your evaluation results are accurate, the telemetry data collected from your OpenShift cluster must be fresh. If the collected telemetry is 24 hours or older, it is stale and WLM cannot use it for a reliable evaluation. Stale metrics usually indicate that the workload agent is misconfigured or cannot connect to Google Cloud.




### OpenShift: Security (6 results)

  * ####  Check block Cloud Storage CMEK link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift

Asset: `Openshift_Cluster`

Details

It is recommended to use Customer-Managed Encryption Keys (CMEK) for Google Cloud managed block storage for greater control over data encryption, supporting key revocation, rotation policies, and enhanced auditability to meet strict compliance requirements.

  * ####  Check eso etcd encryption link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Openshift

Asset: `Openshift_Cluster`

Details

If External Secrets Operator (ESO) is installed to use with Google Cloud Secret Manager, etcd encryption MUST be enabled. ESO pulls secrets from external sources and can sync them to Kubernetes Secrets. If etcd is not encrypted, these secrets are stored in plain text.

  * ####  Check secret manager node publish link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Tags: Openshift

Asset: `Openshift_Cluster`

Details

When you're using Secret Manager with the Secrets Store CSI Driver, you must not use the `ALLOW_NODE_PUBLISH_SECRET` option in the Secret Manager provider DaemonSet. To prevent token leakage, you need to use Security Token Service.

  * ####  Check secret provider class sync link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Tags: Openshift

Asset: `Openshift_Cluster`

Details

If using Google Cloud Secret Manager with the Secrets Store CSI Driver, it is recommended that SecretProviderClass resources do not contain a secretObjects block to ensure secrets only exist in tmpfs memory and do not touch the control plane datastore.

  * ####  Check wif authentication observability link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Tags: Openshift, Security

Asset: `Openshift_Cluster`

Details

It is recommended to use Workload Identity Federation (WIF) for OTLP/Google Cloud authentication. Static JSON keys (service account keys) are high-risk "long-lived" credentials. WIF replaces these with short-lived tokens projected directly into the pod.

  * ####  Check workload identity federation link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Tags: Openshift

Asset: `Openshift_Cluster`

Details

It is recommended to configure the OpenShift cluster to use Workload Identity Federation as the secure method for granting Kubernetes service accounts access to GCP resources without long-lived keys.




### Redis: General (7 results)

  * ####  Check that the Google Cloud Agent for Compute Workloads is set up correctly on all instances in the evaluation scope link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

Instances in the evaluation scope must have the Google Cloud Agent for Compute Workloads configured to run Workload Manager evaluations. If you have not configured the agent correctly, evaluation results can be incomplete or inaccurate. The minimum recommended version is 1.2.

Last updated: August 27, 2025

  * ####  Enable automatic restart for VMs running Redis workloads link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To ensure that the VM restarts automatically in the event of a failure, enable the Compute Engine automatic restart policy for any VM that is running a Redis workload.

Last updated: August 27, 2025

  * ####  Provision Hyperdisk with minimum IOPS and throughput link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

The default provisioned IOPS and throughput values for small Hyperdisks can be too low to guarantee proper performance. We recommend that you raise these values to a minimum of 10,000 IOPS and 1 GiB/s throughput. From November 10th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [Default performance](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#default-perf).

Last updated: November 10, 2025

  * ####  Set VM maintenance policy to MIGRATE for Redis workloads link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To prevent any platform maintenance events from stopping or restarting a VM that is running Redis workloads, the onHostMaintenance parameter for the VM must be set to the recommended option MIGRATE.

For more information, see [Set VM host maintenance policy](https://cloud.google.com/compute/docs/instances/setting-vm-host-options).

Last updated: August 27, 2025

  * ####  Do not run Redis workloads on PD Standard or Hyperdisk Throughput disk types link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Google Cloud recommends that you do not run Redis workloads on PD Standard and Hyperdisk Throughput disk types, because these are hard disk-based disks and might lead to degraded performance. From November 10th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [Persistent disk types](https://cloud.google.com/compute/docs/disks/persistent-disks#disk-types), [Hyperdisks](https://cloud.google.com/compute/docs/disks/hyperdisks), and [Hyperdisk Throughput](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput).

Last updated: November 10, 2025

  * ####  Ensure replication is sent to a machine in a different zone or region link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

To maintain proper high availability, we strongly recommend that you send your replication to a machine in a different zone or region from the primary location. From November 10th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [Well-Architected Framework: Reliability pillar](https://cloud.google.com/architecture/framework/reliability).

Last updated: November 10, 2025

  * ####  Do not use replication without persistence link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Persistence ensures that the system writes the data sent to the primary instance to a durable storage. In a replicated system, choosing the right persistence strategy is critical to prevent data loss in case of a failure. If you choose not to use any persistence options, Google Cloud recommends that you disable the systemd Redis service from automatically restarting to avoid potential data integrity issues. From November 10th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

Last updated: November 10, 2025




### SAP: General (14 results)

  * ####  DEPRECATED: Install Google Cloud's Agent for SAP on all VMs that run SAP workloads link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

This rule is deprecated. It has been replaced by the rule: ["Check that Google Cloud's Agent for SAP is set up correctly on all instances in the evaluation scope"](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices#agent-updated-on-sap-vm), which is provided by default at no charge. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

Last updated: October 27, 2025

  * ####  SAP General: Configure OS settings for X4 instances link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To ensure that X4 instances are optimized to support SAP workloads, you must run the command-line utility provided by Google Cloud's Agent for SAP to verify that the OS configuration matches best practice recommendations. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to Critical. This change also applies to existing evaluations that include this rule.

For more information, see [Post-deployment tasks](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#post-deployment_tasks) in the SAP HANA planning guide.

Last updated: October 27, 2025

  * ####  Check that Google Cloud's Agent for SAP is set up correctly on all instances in the evaluation scope link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

Instances in the evaluation scope must have the Agent for SAP configured for Workload Manager Evaluation. If the agent has not been set up correctly, then evaluation results might be incomplete or inaccurate. This check is included by default, at no charge.

For more information, see [Google Cloud's Agent for SAP planning guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning) and then [Verify the agent version](https://cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sap#verify-update-agent).

Last updated: March 18, 2026

  * ####  SAP General: Ensure that SAP application servers and SAP Central Services are in different zones link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

To guard against zonal failures, Google Cloud recommends that at least one instance hosting an SAP application server is running in a different zone than the SAP Central Services. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the [SAP HANA disaster recovery planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-dr-planning-guide).

Last updated: October 27, 2025

  * ####  SAP General: Allow full access to all Cloud APIs link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

Google Cloud recommends that for Compute Engine instances, the Cloud API access scope is set to `Allow full access to all Cloud APIs` and uses the IAM permissions of the instance service account to control access to Google Cloud resources. From **October 27th 2025** , the severity of this evaluation rule has been updated from Caution to Medium. This change also applies to existing evaluations that include this rule.

For more information, see the section titled [Enable access to Google Cloud APIs](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#enable_access_to_gc_apis) in the Agent for SAP installation guide.

Last updated: October 27, 2025

  * ####  SAP General: Enable deletion protection on all VMs that run SAP workloads link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Compute instances that have the `deletionProtection` option enabled are protected against accidental deletion. Google Cloud recommends enabling deletion protection for all instances that are critical to running SAP workloads. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [Prevent accidental VM deletion](https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion) in the Compute Engine documentation.

Last updated: October 27, 2025

  * ####  SAP General: SAP application server processes must not be running on Compute Engine instances serving as the (A)SCS or ERS link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

To mitigate potential performance issues and guard against certain failure scenarios in a Pacemaker-managed high-availability cluster, Google Cloud recommends that you don't run the SAP application server processes on the same compute instances that host the SAP Central Services or Enqueue Replication Server (ERS). This is because application servers are not managed by the Pacemaker cluster and are not migrated to a new VM in the event of an outage. From October 27th 2025, the severity of this evaluation rule has been updated from Caution to High. This change also applies to existing evaluations that include this rule.

For more information see the section titled [Distributed deployment with high availability](https://docs.cloud.google.com/sap/docs/architectures/sap-s4hana-on-gcp#distributed_deployment_with_ha) in the reference architecture for SAP on Google Cloud.

Last updated: October 27, 2025

  * ####  SAP General: Enable automatic restart for SAP workloads link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To ensure that the VM restarts automatically in the event of a failure, enable the Compute Engine automatic restart policy for any VM that is running an SAP workload.

For more information, see [Set VM host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options).

Last updated: April 18, 2025

  * ####  SAP General: Set VM maintenance policy to `MIGRATE` for SAP workloads link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

MIGRATE for SAP workloads">Details

To prevent any platform maintenance events from stopping or restarting a VM that is running SAP workloads, the `onHostMaintenance` parameter for the VM must be set to the recommended option `MIGRATE`. This recommendation does not apply to X4 or C3 Metal instances.

For more information, see [Set VM host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options).

Last updated: April 18, 2025

  * ####  SAP General: For Compute Engine instance migrations across machine series, set the CPU platform to Automatic. link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

For Compute Engine instance migrations across machine series, Google Cloud recommends setting the CPU platform to 'Automatic' before migrating. Setting a specific CPU platform is only advised if you want to use the same type for the target machine due to performance or advanced instruction set compatibility reasons. From October 27th 2025, the severity of this evaluation rule has been updated from Caution to Medium. This change also applies to existing evaluations that include this rule.

For more information, see the Compute Engine guides for [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms), how to [Specify a minimum CPU platform for VM instances](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform), and how to [Remove a minimum CPU platform setting](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#resetminplatform).

Last updated: October 27, 2025

  * ####  SAP General: UEFI enabled OS images are mandatory for newer generation servers link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Enable UEFI boot for the VM by creating a custom image with the `UEFI_COMPATIBLE` guest OS feature or selecting a pre-configured UEFI-compatible image. UEFI compatibility is a prerequisite for newer generation machine types in Google Cloud. From **October 27th 2025** , the severity of this evaluation rule has been updated from Caution to High. This change also applies to existing evaluations that include this rule.

For more information, see the Compute Engine guides for [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details), [Memory-optimized machine family for Compute Engine](https://docs.cloud.google.com/compute/docs/memory-optimized-machines), and [Enable guest operating system features](https://docs.cloud.google.com/compute/docs/images/create-custom#guest-os-features).

Last updated: October 27, 2025

  * ####  SAP General: Ensure that the swap space follows SAP recommendations link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Configuring the swap space on Linux-based SAP systems enhances performance by managing memory more efficiently. SAP recommendations for swap space are based on the available physical memory as well as the role of the system as part of the database or application layer. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the SAP notes for [Swap-space recommendation for Linux](https://service.sap.com/sap/support/notes/1597355) and [HANA services use large SWAP memory](https://service.sap.com/sap/support/notes/2779331).

Last updated: October 27, 2025

  * ####  SAP General: Check SELinux configuration for Compute Engine instances running SAP workloads link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

Linux can use SELinux for enhanced security, but it can interfere with SAP server components. For SAP implementations, set SELinux to `Disabled` or `Permissive` mode. Disabling SELinux requires a system reboot, while permissive mode can be set without rebooting. This configuration ensures compatibility with SAP tools that are not SELinux-aware.

For more information, see [SAP instance or Host Agent startup fails due to SELinux](https://me.sap.com/notes/3253160/E) and [Changing SELinux to permissive mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/using_selinux/changing-selinux-states-and-modes_using-selinux#changing-to-permissive-mode_changing-selinux-states-and-modes).

Last updated: June 12, 2025

  * ####  SAP General: Enable a system tuning solution on all VMs that run SAP workloads link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

On Linux, system tuning services can help optimize the performance and stability of SAP workloads by setting recommended parameters for the SAP system. Google Cloud recommends enabling the `sapconf` or `saptune` service on SUSE Linux Enterprise Server, or the `tuned` service on Red Hat Enterprise Linux. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see the SAP note [Red Hat tuned-profiles for SAP](https://me.sap.com/notes/0003427561).
    * For SLES, see the SUSE guide [Tuning systems with saptune](https://documentation.suse.com/en-us/sles-sap/15-SP3/html/SLES-SAP-guide/cha-tune.html).

Last updated: October 27, 2025




### SAP: HANA (10 results)

  * ####  SAP HANA: Use a certified OS link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To receive support from SAP and Google Cloud for SAP HANA on a Compute Engine VM, you must use an operating system version that is certified by SAP and Google Cloud for use with SAP HANA.

For more information, see [OS support for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-os-support).

Last updated: February 18, 2026

  * ####  SAP HANA: Use a certified custom VM type link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To receive support from SAP and Google Cloud for SAP HANA on a Compute Engine custom VM, you must use a custom VM type that is certified by SAP and Google Cloud for use with SAP HANA.

For more information, see [Certified custom machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#hana-cert-table-custom-vms).

Last updated: April 9, 2025

  * ####  SAP HANA: Map the SAP HANA data and log volumes to the same type of SSD-based persistent disk link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

For performance reasons, the SAP HANA `/hana/data` and `/hana/log` volumes must be mapped to the same type of SSD-based persistent disk. You can map both volumes to the same single persistent disk or, if the same persistent disk type is used for each, you can map each volume to a separate persistent disk.

For more information, see the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide).

Last updated: April 9, 2025

  * ####  SAP HANA: Use a certified VM type link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To receive support from SAP and Google Cloud for SAP HANA on a Compute Engine VM, you must use a VM type that is certified by SAP and Google Cloud for use with SAP HANA.

For more information, see [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#certified-vms).

Last updated: February 18, 2026

  * ####  SAP HANA: SAP Minimum allowable sizes for SSD-based persistent disk options link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

For block storage, SAP HANA requires a minimum throughput of 400 MB per second. If you are using SSD or balanced persistent disks, use the minimum size for that persistent disk type to provide the necessary throughput. If you are using extreme persistent disks, provision a minimum of 20,000 IOPS.

For more information, see [Persistent disk storage](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage) in the SAP HANA planning guide.

Last updated: April 18, 2025

  * ####  SAP HANA: Check for backups of the SAP HANA database link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

Creating backups regularly and implementing a proper backup strategy helps you recover your SAP HANA database in situations such as data corruption or data loss due to an unplanned outage or failure in your infrastructure. Google Cloud recommends following a backup strategy that includes creating at least one full system backup of your SAP HANA database weekly, and creating at least one delta backup or snapshot based backup of the SAP HANA data volume daily. Daily full system backups can also be used as a substitute for delta or snapshot based backups. More frequent backups may be necessary to meet specific RPO requirements.

For more information, see [Backup and recovery](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery) in the SAP HANA operations guide, or [Backup and recovery for SAP HANA on bare metal instances](https://docs.cloud.google.com/sap/docs/backup-recovery-for-hana-on-bare-metal-instances).

Last updated: April 18, 2025

  * ####  SAP HANA: Ensure that the SAP Primary and DR sites are in different regions link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

To protect against region-wide outages and maintain business continuity, the SAP HANA primary node and Disaster Recovery (DR) sites must be deployed in different geographical regions. This approach mitigates the risk of catastrophic events affecting the components deployed within a single region, reducing potential data loss and downtime beyond what zone-level redundancy can offer. From October 27th 2025, the severity of this evaluation rule has been updated from Critical to High. This change also applies to existing evaluations that include this rule.

For more information, see the [SAP HANA disaster recovery planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-dr-planning-guide).

  * ####  SAP HANA: Enable SAP HANA Fast Restart link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Compute Engine includes functionality based on Intel's Memory RAS that can significantly reduce the impact of all memory errors that would otherwise cause VM crashes. When combined with SAP HANA's fast restart capability (available since HANA 2.0 SP04), SAP HANA systems are able to recover from such failure events. This configuration is recommended on all Memory Optimized virtual machine families. From October 27th 2025, the severity of this evaluation rule has been updated from Critical to High. This change also applies to existing evaluations that include this rule.

For more information, see [SAP HANA Fast Restart option](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#sap-hana-fast-restart-on-gc).

Last updated: October 27, 2025

  * ####  SAP HANA: Use the recommended configuration settings for Hyperdisk link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To enable the best performance of the Hyperdisk volumes used with SAP HANA, you must set values recommended by Google Cloud for the following SAP HANA properties: `num_completion_queues`, `num_submit_queues`, `tables_preloaded_in_parallel`, and `load_table_numa_aware`.

For more information, see [Hyperdisk performance](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hyperdisk_performance) in the SAP HANA planning guide.

Last updated: April 18, 2025

  * ####  SAP HANA: Use a separate disk for each SAP HANA filesystem link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

For optimal performance of your SAP HANA system, Google Cloud recommends that you use a separate disk for each SAP HANA filesystem. Notably, the disks hosting the SAP HANA data and log volumes must not be used for any other function, such as serving as the installation path or system instance path. This recommendation also applies to the SAP HANA backup volume, if you save your backups to a disk. Hosting filesystems on separate disks is also recommended to be able to use data snapshots as a backup and recovery option. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the [Persistent disk storage](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage) section in the SAP HANA planning guide.

Last updated: October 27, 2025




### SAP: HANA Insights (18 results)

  * ####  SAP HANA Maintenance: Check for appropriate configuration of the `log_disk_usage_reclaim_threshold` parameter link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

log_disk_usage_reclaim_threshold parameter">Details

If the log partition file system disk usage ('usedDiskSpace' in percent of 'totalDiskSpace') is above the specified threshold, the logger will automatically trigger an internal 'log release' (0 = disabled). As default, the logger will keep all free log segments cached for reuse, segments will only be removed if a reclaim is triggered explicitly via 'ALTER SYSTEM RECLAIM LOG' or if a 'DiskFull'/'LogFull' event is hit on logger level. This threshold parameter can be used to trigger the reclaim internally before a 'DiskFull'/'LogFull' situation occurs. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [log_disk_usage_reclaim_threshold](https://help.sap.com/docs/SAP_HANA_PLATFORM/009e68bc5f3c440cb31823a3ec4bb95b/f1b759affa5f444992736273afb7d9fe.html#loiof1b759affa5f444992736273afb7d9fe__configSPS07_id_392) in the SAP HANA Configuration Parameter Reference.

Last updated: October 27, 2025

  * ####  SAP HANA Maintenance: Regular backup catalog housekeeping is needed to improve backup performance link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

The backup catalog can grow quite large over time, especially if it is not regularly cleaned up. This can lead to performance problems and can make it difficult to find the backups that are needed. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [SAP HANA multiple issue caused by large Log Backups due to large Backup Catalog size](https://me.sap.com/notes/3339034) in the SAP Knowledge Base.

Last updated: October 27, 2025

  * ####  SAP HANA High Availability and Disaster Recovery: Enable data and log compression link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Data and log compression can be used for the initial full data shipping, the subsequential delta data shipping, as well as for the continuous log shipping. Data and log compression can be configured to reduce the amount of traffic between systems, especially over long distances (for example, when using the ASYNC replication mode). From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [Data and Log Compression](https://help.sap.com/docs/SAP_HANA_PLATFORM/4e9b18c116aa42fc84c7dbfd02111aba/92447e0a105c4facad3553b28aaec318.html) in the SAP HANA System Replication guide.

Last updated: October 27, 2025

  * ####  SAP HANA High Availability and Disaster Recovery: Use the recommended value for the `datashipping_parallel_channels` parameter link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

datashipping_parallel_channels parameter">Details

The SAP HANA parameter `datashipping_parallel_channels` defines the number of network channels used by full or delta datashipping. The default value is `4`, which means that four network channels are used to ship data. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [datashipping_parallel_channels](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/0cd257970d514abd8ddf9ee1f45f3bca.html) in the SAP HANA Administration Guide.

Last updated: October 27, 2025

  * ####  SAP HANA Performance: Check for appropriate configuration of garbage collection parameters link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

In databases with more than 235 GB allocation limit, the `gc_unused_memory_threshold_rel` and `gc_unused_memory_threshold_abs` parameters have to be configured. These parameters help to reduce the risk of hiccups (e.g. due to MemoryReclaim waits) when garbage collection happens reactively. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [SAP HANA Garbage Collection](https://me.sap.com/notes/2169283) in the SAP Knowledge Base.

Last updated: October 27, 2025

  * ####  SAP HANA Performance: Enable the `load_table_numa_aware` parameter link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

load_table_numa_aware parameter">Details

To improve the performance of NUMA-based SAP HANA systems, enable the `load_table_numa_aware` parameter. When this parameter is enabled, SAP HANA optimizes data placement across NUMA nodes during table loading. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [SAP HANA Non-Uniform Memory Access (NUMA)](https://me.sap.com/notes/0002470289) in the SAP Knowledge Base.

Last updated: October 27, 2025

  * ####  SAP HANA Maintenance: Check the status of the HANA license link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

A permanent license key is required to operate on a HANA system. If a permanent license key expires, a (second) temporary license key is automatically generated and will be valid for 28 days. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [License Keys for SAP HANA Database](https://me.sap.com/notes/1644792) in the SAP Knowledge Base.

Last updated: October 27, 2025

  * ####  SAP HANA Maintenance: Check the log mode link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

If `log_mode` is set to 'normal', HANA creates regular log backups, allowing for point-in-time recovery (restoring up to the moment before a failure). If `log_mode` is set to 'overwrite' , no log backups are created; you can only recover the database to the last data backup. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to Critical. This change also applies to existing evaluations that include this rule.

For more information, see [Log Modes](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/c486a0a3bb571014ab46c0633224f02f.html) in the SAP HANA Administration Guide.

Last updated: October 27, 2025

  * ####  SAP HANA High Availability and Disaster Recovery: Set `logshipping_async_buffer_size` on the primary site link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

logshipping_async_buffer_size on the primary site">Details

If system replication is disconnected during a full data shipment, then replication has to start from scratch. In order to reduce the risk of buffer full situations, the `logshipping_async_buffer_size` parameter can be adjusted to a value of `1 GB` on the primary site. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [SAP HANA System Replication](https://me.sap.com/notes/1999880) in the SAP Knowledge Base.

Last updated: October 27, 2025

  * ####  SAP HANA High Availability and Disaster Recovery: Use the recommended value for the `logshipping_max_retention_size` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

logshipping_max_retention_size parameter">Details

In context of logreplay operations modes the `logshipping_max_retention_size` SAP HANA parameter defines the maximum amount of redo logs that are kept on primary site for synchronization with the secondary site (default: `1 TB`). If the underlying file system isn't large enough to hold the complete configured retention size, it can happen in the worst case that the file system runs full and the primary site comes to a standstill.

For more information, see [SAP HANA System Replication](https://me.sap.com/notes/1999880) in the SAP Knowledge Base.

Last updated: April 17, 2025

  * ####  SAP HANA Performance: Check for appropriate configuration of the `max_cpuload_for_parallel_merge` parameter link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

max_cpuload_for_parallel_merge parameter">Details

By default, multiple auto merges (up to `num_merge_threads`) of different tables or partitions can be executed up to a CPU utilization limit of 45%, but as soon as this limit is exceeded, a maximum of one auto merge is executed at any time. This can in the worst case result in an increased auto merge backlog although sufficient system resources for handling parallel auto merges would still be available. In this case you can consider increasing this parameter to a value that is both higher than the usual CPU utilization and lower than a critical limit that would allow auto merges to introduce resource bottlenecks. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [SAP HANA Delta Merges](https://me.sap.com/notes/2057046) in the SAP Knowledge Base.

Last updated: October 27, 2025

  * ####  SAP HANA Scaleout: Check to see that all hosts in a scale-out environment have a consistent OS version and Kernel version link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

In a scale-out SAP HANA environment, maintaining consistency in OS and kernel across all nodes within the system is crucial for optimal performance and stability. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to Critical. This change also applies to existing evaluations that include this rule.

For more information, see [SAP HANA: Supported Operating Systems](https://me.sap.com/notes/2235581) in the SAP Knowledge Base.

Last updated: October 27, 2025

  * ####  SAP HANA Performance: Check for appropriate configuration of the `parallel_merge_threads` parameter link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

parallel_merge_threads parameter">Details

If `parallel_merge_threads` is set to a specific value, this value is used for parallelism while `token_per_table` defines the number of consumed tokens. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [SAP HANA Delta Merges](https://me.sap.com/notes/2057046) in the SAP Knowledge Base.

Last updated: October 27, 2025

  * ####  SAP HANA Maintenance: Check for appropriate configuration of the `automatic_reorg_threshold` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

automatic_reorg_threshold parameter">Details

The `automatic_reorg_threshold` parameter specifies when automatic reorganization of row store tables is triggered. If the value is set to 30(default) automatic reorganization won't be triggered as often as it could be.

For more information, see [Incorrect SAP HANA Alert 71: 'Row store fragmentation'](https://me.sap.com/notes/2789255) in the SAP Knowledge Base.

Last updated: April 21, 2025

  * ####  SAP HANA Performance: Verify default and worker stack size parameters link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

The thread stack parameter `default_stack_size_kb` and `worker_stack_size_kb` determines the amount of data a newly created thread can access.

For more information, see [Indexserver Crash Due to STACK OVERFLOW in Evaluator::ExpressionParser](https://me.sap.com/notes/3002993) in the SAP Knowledge Base.

Last updated: April 22, 2025

  * ####  SAP HANA Maintenance: Verify the time of the last table consistency check link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Regular consistency checks are required to detect hidden corruptions as early as possible. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [SAP HANA Consistency Checks and Corruptions](https://me.sap.com/notes/2116157) in the SAP Knowledge Base.

Last updated: October 27, 2025

  * ####  SAP HANA Performance: Check for appropriate configuration of the `tables_preloaded_in_parallel` parameter in X4 VMs link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

tables_preloaded_in_parallel parameter in X4 VMs">Details

The `tables_preloaded_in_parallel` parameter lets you control the number of tables loaded in parallel after you start your SAP HANA system, providing flexibility for performance optimization. We recommend a minimum value of 32.

For more information, see [SAP HANA Loads and Unloads](https://me.sap.com/notes/2127458) in the SAP Knowledge Base.

Last updated: April 22, 2025

  * ####  SAP HANA Scaleout: Check to see that all hosts in a scale-out environment have a consistent timezone link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

In a scale-out SAP HANA environment, maintaining consistency in timezones is crucial to maintain system stability. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to Critical. This change also applies to existing evaluations that include this rule.

For more information, see [Check HANA DB for DST switch](https://me.sap.com/notes/2080216) in the SAP Knowledge Base.

Last updated: October 27, 2025




### SAP: HANA Security Best Practices (19 results)

  * ####  SAP HANA Security: Enable encryption for data and log backups link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Encryption protects backups from unauthorized access by encrypting the backup data before it is transferred to the backup location. This means that even if an unauthorized user gains access to the backup data, they cannot read it without the decryption key. This is applicable for both file-based backups and backups created using third-party backup tools. Google Cloud recommends that you enable backup encryption in the SAP HANA system. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [system backup encryption statement](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/edf132427f0043b08769774512504858.html)in the SAP HANA reference guide.

Last updated: October 27, 2025

  * ####  SAP HANA Security: Safeguard against users with `DEVELOPMENT` privileges in a production environment link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

DEVELOPMENT privileges in a production environment">Details

At least one user or role has the `DEVELOPMENT` privilege in the production database. Google Cloud recommends that you have no users with this privilege. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [DEVELOPMENT privilege section](https://help.sap.com/docs/SAP_HANA_PLATFORM/742945a940f240f4a2a0e39f93d3e2d4/45955420940c4e80a1379bc7270cead6.html#system-privilege%3A-development) in SAP HANA security checklists and recommendations.

Last updated: October 27, 2025

  * ####  SAP HANA Security: Require users to change their initial password link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

The `force_first_password_change` parameter in SAP HANA specifies whether users are required to change their password after they are created. Google Cloud recommends that you enable the `force_first_password_change` parameter.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#force_first_password_change) in the SAP HANA One security guide.

Last updated: April 23, 2025

  * ####  SAP HANA Security: Safeguard against users with `SAP_INTERNAL_HANA_SUPPORT` privileges in production environment link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

SAP_INTERNAL_HANA_SUPPORT privileges in production environment">Details

At least one account has the `SAP_INTERNAL_HANA_SUPPORT` role. Google Cloud recommends that you have no users with this privilege. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [`SAP_INTERNAL_HANA_SUPPORT`](https://help.sap.com/docs/SAP_HANA_PLATFORM/742945a940f240f4a2a0e39f93d3e2d4/45955420940c4e80a1379bc7270cead6.html#predefined-catalog-role-sap_internal_hana_support) role in SAP HANA security checklists and recommendations.

Last updated: October 27, 2025

  * ####  SAP HANA Security: Check for appropriate configuration of the `last_used_passwords` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

last_used_passwords parameter">Details

Password reuse is a common security vulnerability. The `last_used_passwords` parameter in SAP HANA prevents users from reusing their most recent passwords. The parameter specifies the number of past passwords that a user is not allowed to use when changing their current password. Google Cloud recommends that you set `last_used_passwords` to a value of `5` or higher.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#last_used_passwords) in the SAP HANA One security guide.

Last updated: April 23, 2025

  * ####  SAP HANA Security: Enable encryption of log volumes link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

Encryption protects SAP HANA logs from unauthorized access. One way to do this is to encrypt the logs at the operating system level. SAP HANA also supports encryption in the persistence layer, which can provide additional security. Google Cloud recommends that you encrypt log volumes. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [recommendations for data encryption](https://help.sap.com/docs/SAP_HANA_PLATFORM/742945a940f240f4a2a0e39f93d3e2d4/904911eb0fe54124b10dfaeadb5337ce.html#data-and-log-volume-encryption) in SAP HANA security checklists and recommendations.

Last updated: October 27, 2025

  * ####  SAP HANA Security: Check for appropriate configuration of the `maximum_invalid_connect_attempts` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

maximum_invalid_connect_attempts parameter">Details

The `maximum_invalid_connect_attempts` parameter in SAP HANA specifies the maximum number of failed logon attempts that are possible; the user is locked as soon as this number is reached. Google Cloud recommends that you set `maximum_invalid_connect_attempts` to a value of `6` or higher.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#maximum_invalid_connect_attempts) in the SAP HANA One security guide.

Last updated: April 23, 2025

  * ####  SAP HANA Security: Check for appropriate configuration of the `maximum_password_lifetime` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

maximum_password_lifetime parameter">Details

The `maximum_password_lifetime` parameter in SAP HANA specifies the number of days after which a user's password expires. The parameter will enforce security measures to change the user password periodically. Google Cloud recommends that you set `maximum_password_lifetime` to a value of `182` or lower.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#maximum_password_lifetime) in the SAP HANA One security guide.

Last updated: April 23, 2025

  * ####  SAP HANA Security: Check for appropriate configuration of the `maximum_unused_initial_password_lifetime` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

maximum_unused_initial_password_lifetime parameter">Details

The initial password is only meant to serve a temporary purpose. The `maximum_unused_initial_password_lifetime` parameter in SAP HANA specifies the number of days for which the initial password or any password set by a user administrator for a user is valid. Google Cloud recommends that you set `maximum_unused_initial_password_lifetime` to a value of `7` or lower.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#maximum_unused_initial_password_lifetime) in the SAP HANA One security guide.

Last updated: April 23, 2025

  * ####  SAP HANA Security: Check for appropriate configuration of the `maximum_unused_productive_password_lifetime` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

maximum_unused_productive_password_lifetime parameter">Details

The `maximum_unused_productive_password_lifetime` parameter in SAP HANA specifies the number of days after which a password expires if the user has not logged on. It helps in reducing the risk of compromised accounts due to prolonged password inactivity. Google Cloud recommends that you set `maximum_unused_productive_password_lifetime` to a value of `365` or lower.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#maximum_unused_productive_-password_lifetime) in the SAP HANA One security guide.

Last updated: April 23, 2025

  * ####  SAP HANA Security: Check for appropriate configuration of the `minimal_password_length` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

minimal_password_length parameter">Details

The `minimal_password_length` parameter in SAP HANA specifies the minimum number of characters a password must contain. It is important to note that the `minimal_password_length` parameter is critical to enhancing the security of SAP HANA. A password that is shorter than 8 characters is more likely to be guessed or cracked, which could allow an unauthorized user to access your system. To improve the security of your SAP HANA system, Google Cloud recommends that you increase the value of the `minimal_password_length` parameter to a value of `8` or more.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#minimum_password_lifetime) in the SAP HANA One security guide.

Last updated: April 23, 2025

  * ####  SAP HANA Security: Check for appropriate configuration of the `minimum_password_lifetime` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

minimum_password_lifetime parameter">Details

The `minimum_password_lifetime` parameter in SAP HANA specifies the minimum number of days that must elapse before a user can change their password. This parameter helps enforce password aging policies and improve system security by preventing users from frequently changing their passwords.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#minimum_password_lifetime) in the SAP HANA One security guide.

Last updated: April 25, 2025

  * ####  SAP HANA Security: Check for appropriate configuration of the `password_expire_warning_time` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

password_expire_warning_time parameter">Details

The `password_expire_warning_time` parameter in SAP HANA specifies the number of days before a password is due to expire that the user receives notification. It is important to notify users of password expiration times to ensure that they change their passwords before they expire. The default value for the password expiration warning time is 14 days.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#password_expire_warning_time) in the SAP HANA One security guide.

Last updated: April 25, 2025

  * ####  SAP HANA Security: Check for appropriate configuration of the `password_layout` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

password_layout parameter">Details

The `password_layout` parameter in SAP HANA specifies the character types that the password must contain at least one character of each selected character type is required.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#password_layout) in the SAP HANA One security guide.

Last updated: April 25, 2025

  * ####  SAP HANA Security: Check for appropriate configuration of the `password_lock_time` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

password_lock_time parameter">Details

The `password_lock_time` parameter in SAP HANA specifies the number of minutes for which a user is locked after the maximum number of failed logon attempts. Google Cloud recommends that you set password_lock_time to a value of `1440` or higher.

For more information, see [password policy configuration options](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/61662e3032ad4f8dbdb5063a21a7d706.html#password_lock_time) in the SAP HANA One security guide.

Last updated: April 25, 2025

  * ####  SAP HANA Security: Enable encryption of the persistent (data) volume link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

It is recommended to protect SAP HANA data from unauthorized access. One way to do this is to encrypt the data at the operating system level. SAP HANA also supports encryption in the persistence layer, which can provide additional security. We recommend that you encrypt data volumes. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [recommendations for data encryption](https://help.sap.com/docs/SAP_HANA_PLATFORM/742945a940f240f4a2a0e39f93d3e2d4/904911eb0fe54124b10dfaeadb5337ce.html#data-and-log-volume-encryption) in SAP HANA security checklists and recommendations.

Last updated: October 27, 2025

  * ####  SAP HANA Security: HANA versions affected by CVE-2019-0357 link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

CVE-2019-0357 is a vulnerability that allows database users with administrator privileges to run operating system commands as root on particular SAP HANA versions.

For more information, see [SAP security note for CVE-2019-0357](https://me.sap.com/notes/2829681).

Last updated: April 25, 2025

  * ####  SAP HANA Security: Safeguard against users with debug privileges in production environment link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

At least one user has the `DEBUG` or `ATTACH DEBUGGER` privilege in the system. Google Cloud recommends that you have no users with this privilege. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [recommendations for database users](https://help.sap.com/docs/SAP_HANA_PLATFORM/742945a940f240f4a2a0e39f93d3e2d4/45955420940c4e80a1379bc7270cead6.html#debug-privileges) in SAP HANA security checklists and recommendations.

Last updated: October 27, 2025

  * ####  SAP HANA Security: Restrict senders in system replication configuration link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

System replication is configured with `allowed_sender` when the listen interface is `global`. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [recommendations for network configurations](https://help.sap.com/docs/SAP_HANA_PLATFORM/742945a940f240f4a2a0e39f93d3e2d4/eccef06eabe545e68d5019bcb6d8e342.html#host-name-resolution-in-system-replication) in SAP HANA security checklists and recommendations.

Last updated: October 27, 2025




### SAP: High Availability (33 results)

  * ####  Corosync: Use the recommended value for the `consensus` parameter link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

consensus parameter">Details

In a Linux Pacemaker high-availability cluster for SAP on Google Cloud, the default value of the `consensus` parameter is set to 1.2 times the value of the `token` parameter. It is recommended not to modify this value. If you change the default value, make sure that it is at least 1.2 times the `token` value. From **October 27th 2025** , the severity of this evaluation rule has been updated from Caution to High. This change also applies to existing evaluations that include this rule.

For more information, see [Corosync configuration parameter values](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#corosync_configuration_parameter_values) in the SAP HANA high-availability planning guide.

Last updated: October 27, 2025

  * ####  Corosync: Use the recommended value for the `join` parameter link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

join parameter">Details

In a Linux Pacemaker high-availability cluster for SAP on Google Cloud, set the Corosync `join` parameter to a value of `60` to conform to Google Cloud best practices. From **October 27th 2025** , the severity of this evaluation rule has been updated from Caution to High. This change also applies to existing evaluations that include this rule.

For more information, see [Corosync configuration parameter values](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#corosync_configuration_parameter_values) in the SAP HANA high-availability planning guide.

Last updated: October 27, 2025

  * ####  Corosync: Use the recommended value for the `max_messages` parameter link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

max_messages parameter">Details

In a Linux Pacemaker high-availability cluster for SAP on Google Cloud, to avoid message flooding between cluster nodes during token processing, set the Corosync `max_messages` parameter to a value of `20`. From **October 27th 2025** , the severity of this evaluation rule has been updated from Caution to Medium. This change also applies to existing evaluations that include this rule.

For more information, see [Corosync configuration parameter values](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#corosync_configuration_parameter_values) in the SAP HANA high-availability planning guide.

Last updated: October 27, 2025

  * ####  Corosync: Use the recommended value for the `token_retransmits_before_loss_const` parameter link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

token_retransmits_before_loss_const parameter">Details

In a Linux Pacemaker high-availability cluster for SAP on Google Cloud, set the Corosync `token_retransmits_before_loss_const` parameter to a value of `10` or more to conform to Google Cloud best practices.

For more information, see [Corosync configuration parameter values](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#corosync_configuration_parameter_values) in the SAP HANA high-availability planning guide.

Last updated: April 14, 2025

  * ####  Corosync: Use the recommended value for the `token` parameter link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

token parameter">Details

In a Linux Pacemaker high-availability cluster for SAP on Google Cloud, set the value of the Corosync `token` parameter to the recommended timeout value of `20000` to conform to the Google Cloud best practice for failure detection.

For more information, see [Corosync configuration parameter values](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#corosync_configuration_parameter_values) in the SAP HANA high-availability planning guide.

Last updated: April 14, 2025

  * ####  Corosync: Use the recommended value for the `transport` parameter link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

transport parameter">Details

In a Linux Pacemaker high-availability cluster for SAP on Google Cloud, set the value of the Corosync `transport` protocol as appropriate for your Operating System. For Red Hat systems of version 8 and later, the parameter should be set to `knet`. For other supported Operating Systems, a value of `udpu` is expected.

For more information, see the guide for your OS: 

    * For RHEL, see [HA cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel).
    * For SLES, see [HA cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles).

Last updated: April 14, 2025

  * ####  Pacemaker: Set `pcmk_delay_max` on the fencing device cluster resource link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

pcmk_delay_max on the fencing device cluster resource">Details

To avoid fence race conditions in Linux Pacemaker high-availability clusters for SAP, the `pcmk_delay_max` parameter must be specified with a value of 30 or greater in the definition of the fencing resource.

For more information, see [Special Options for Fencing Resources](https://clusterlabs.org/pacemaker/doc/deprecated/en-US/Pacemaker/2.0/html/Pacemaker_Explained/_special_options_for_fencing_resources.html).

Last updated: April 14, 2025

  * ####  Pacemaker: Use the recommended timeout value for `SAPHana` operations link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

SAPHana operations">Details

The definition of the `SAPHana` resource in a Linux Pacemaker HA cluster contains a timeout value for the `stop`, `start`, `promote`, and `demote` operations. For Linux Pacemaker HA clusters for SAP on Google Cloud, we recommend a value of at least `3600` for each operation.

For more information, see the guide for your OS: 

    * For RHEL, see [HA cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel).
    * For SLES, see [HA cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles).

Last updated: April 14, 2025

  * ####  Pacemaker: Check that an alias IP implementation is not in use link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

In a Linux Pacemaker high availability cluster for SAP on Google Cloud, using alias IP addresses that move between Compute Engine instances is discouraged as a failover mechanism because it doesn't meet the high availability requirements. In certain failure scenarios, such as a zonal failure event, you might not be able to remove an alias IP address from a compute instance. Consequently, you might not be able to move the alias IP address to another compute instance, making failover impossible.

For more information, see [Alias IP VIP implementations](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#alias_ip_vip_implementations) in the SAP HANA high-availability planning guide.

Last updated: April 14, 2025

  * ####  Pacemaker: Ensure that all cluster resources are healthy link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To ensure high availability for your SAP system and to safeguard it from unforeseen host events, all resources in the Pacemaker managed cluster must be in the Started state.

For more information, see [Resource agent is stopped](https://cloud.google.com/sap/docs/troubleshooting/troubleshooting-sap-ha#resource_agent_is_stopped) in the Troubleshooting high-availability configurations for SAP guide.

Last updated: June 12, 2025

  * ####  Pacemaker: Use the recommended settings for Cluster Op Default timeout link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

In a Pacemaker cluster, the `timeout` parameter in `op_defaults` sets a global default for how long operations can take before being considered failed. If a specific timeout is configured for an individual resource it will override the global default. Google Cloud recommends to set a default timeout value of `600`. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [Set the cluster defaults](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#set_the_cluster_defaults).
    * For SLES, see [Cluster bootstrap and more](https://documentation.suse.com/sbp/sap-15/html/SLES4SAP-hana-sr-guide-PerfOpt-15/index.html#id-cluster-bootstrap-and-more).

Last updated: October 27, 2025

  * ####  Pacemaker: Use the recommended cluster properties for the ASCS resource link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

In a Linux Pacemaker high-availability cluster for SAP on Google Cloud, `meta_attributes` are configuration parameters that influence how a resource behaves within the cluster. For the ASCS resource, SUSE and Red Hat recommend to set `resource-stickiness` to a value of `5000`. Also, for ENSA1, set `migration-threshold` to a value of `1` and `failure-timeout` to a value of `60`. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to Critical. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [Creating resource for managing the (A)SCS instance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/configuring_ha_clusters_to_manage_sap_netweaver_or_sap_s4hana_application_server_instances_using_the_rhel_ha_add-on/asmb_set_cluster_v8-configuring-clusters-to-manage#con_creat_manag_v8-configuring-clusters-to-manage).
    * For SLES - ENSA1, see [Configuring the resources for the ASCS](https://documentation.suse.com/sbp/sap-15/html/SAP-nw740-sle15-setupguide/index.html#id-configuring-the-resources-for-the-ascs).
    * For SLES - ENSA2, see [Configuring the resources for the ASCS](https://documentation.suse.com/sbp/sap-12/html/SAP_S4HA10_SetupGuide-SLE12/index.html#id-configuring-resources-for-the-ascs-instance).

Last updated: October 27, 2025

  * ####  Pacemaker: Use the recommended ERS resource setting for ENSA1 link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

In a high availability SAP Central Services cluster (ABAP or Java), setting `IS_ERS=true` for the ERS resource is mandatory for an Enqueue Replication Server (ENSA1) configuration because it is used to identify the node where the ERS service is active. For an ENSA2 configuration, this setting is optional but recommended.

For more information, see the following guides: 

    * For RHEL, see [Creating resource for managing the ERS instance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/configuring_ha_clusters_to_manage_sap_netweaver_or_sap_s4hana_application_server_instances_using_the_rhel_ha_add-on/asmb_set_cluster_v8-configuring-clusters-to-manage#con_mng_ers_inst_v8-configuring-clusters-to-manage) or view the [Red Hat Knowledgebase](https://access.redhat.com/solutions/5474031).
    * For SLES, see [Configuring cluster resources](https://documentation.suse.com/sbp/sap-15/html/SAP-nw740-sle15-setupguide/index.html#id-configuring-cluster-resources).
    * For SAP NetWeaver Enqueue Replication 1 High Availability Cluster - SAP NetWeaver 7.40 and 7.50, see [Configuring the resources for the ERS](https://documentation.suse.com/sbp/sap-15/html/SAP-nw740-sle15-setupguide/index.html#id-configuring-the-resources-for-the-ers).
    * For SAP S/4 HANA - Enqueue Replication 2 High Availability Cluster, see [Configuring the resources for the ERS instance](https://documentation.suse.com/sbp/sap-15/html/SAP-S4HA10-setupguide-sle15/index.html#id-configuring-the-resources-for-the-ers-instance).

Last updated: April 15, 2025

  * ####  Pacemaker: Use the recommended resource defaults for the SAP CS cluster link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

In a Linux Pacemaker high-availability cluster, to help manage resource behavior and failover policies, the `rsc_defaults` primitive sets default `meta_attributes` for all resources. SUSE and Red Hat recommend to set `resource-stickiness` to a value of `1`, indicating a low preference for resources to remain on their current node, and a `migration-threshold` to a value of `3`, allowing up to three failures on a node before a resource is moved to another node. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL 9, see [Configuring general cluster properties](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/html/configuring_ha_clusters_to_manage_sap_netweaver_or_sap_s4hana_application_server_instances_using_the_rhel_ha_add-on/asmb_set_cluster_configuring-clusters-to-manage#con_config_general_cluster_configuring-clusters-to-manage).
    * For RHEL 8, see [Configuring general cluster properties](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/configuring_ha_clusters_to_manage_sap_netweaver_or_sap_s4hana_application_server_instances_using_the_rhel_ha_add-on/asmb_set_cluster_v8-configuring-clusters-to-manage#con_config_general_cluster_v8-configuring-clusters-to-manage).
    * For SLES, see [Configuring the cluster base](https://documentation.suse.com/sbp/sap-15/html/SAP-nw740-sle15-setupguide/index.html#id-configuring-the-cluster-base).

Last updated: October 27, 2025

  * ####  Pacemaker: Use the recommended NetWeaver HA SAPInstance automatic recover and monitor configuration link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

The `SAPInstance` primitive in Pacemaker manages SAP application instances, guaranteeing their correct starting, stopping, and monitoring. To enhance the stability of SAP Instances, Google Cloud recommends setting the instance attribute for `AUTOMATIC_RECOVER=false`. Additionally, it is recommended to set the `monitor` operation to have a `timeout` value of `60` and an interval value set to `11` for SLES and `20` for RHEL. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to Critical. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS:

    * For RHEL, see [Creating resource for managing the (A)SCS instance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/configuring_ha_clusters_to_manage_sap_netweaver_or_sap_s4hana_application_server_instances_using_the_rhel_ha_add-on/asmb_set_cluster_v8-configuring-clusters-to-manage#con_creat_manag_v8-configuring-clusters-to-manage).
    * For SLES, see [Configuring the resources for ASCS](https://documentation.suse.com/sbp/sap-15/html/SAP-nw740-sle15-setupguide/index.html#id-configuring-the-resources-for-the-ascs).

Last updated: October 27, 2025

  * ####  High Availability: Verify the virtual host name configured for SAP Central Services hosts link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To ensure high availability of SAP Central Services, in the `DEFAULT.PFL` file, values for the `serverhost` and `replicatorhost` parameters need to align with the Pacemaker cluster configuration. This configuration ensures continued operation even if one of the hosts experiences a failure, because the cluster can automatically failover to the other host. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to Critical. This change also applies to existing evaluations that include this rule.

For more information, view the profile parameters for the installed ENSA version: 

    * For ENSA1, see [Profile Parameters for the Enqueue Clients](https://help.sap.com/docs/ABAP_PLATFORM_NEW/3442894b64c6492890fa3d07bc767e20/47ea3ef600e83b8be10000000a421937.html)
    * For ENSA2, see [Profile Parameters of Enqueue Replicator 2](https://help.sap.com/docs/ABAP_PLATFORM_NEW/cff8531bc1d9416d91bb6781e628d4e0/f4fe6dde1cd1406893824fb2d1b70382.html)

Last updated: October 27, 2025

  * ####  Pacemaker: Migrate from legacy `gcpstonith` fence agent link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

gcpstonith fence agent">Details

The `gcpstonith` fencing module is deprecated. Migrate to the OS bundled `fence_gce` fencing agent for optimal reliability and functionality with your Pacemaker cluster on Google Cloud. `fence_gce` is included in supported Linux distributions with the High Availability (HA) extension or add-on. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the following guides: 

    * To set up fencing for an HA cluster on RHEL, see [Set up fencing](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#set_up_fencing).
    * To set up fencing for an HA cluster on SLES, see [Set up fencing](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#set_up_fencing).
    * To migrate from gcpstonith to fence_gce, see [Fence agent gcpstonith is deprecated](https://docs.cloud.google.com/sap/docs/troubleshooting/troubleshooting-sap-ha#fence_agent_gcpstonith_is_deprecated).

Last updated: October 27, 2025

  * ####  Pacemaker: Set the high-availability cluster `migration-threshold` parameter to the recommended value for SAP HANA link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

migration-threshold parameter to the recommended value for SAP HANA">Details

To migrate the SAP HANA resource to a new cluster node in the event of a failure in a Linux Pacemaker high-availability cluster, the SAP HANA resource definition must specify the `migration-threshold` parameter with the recommended value of `5000`. This parameter determines the number of errors before a failover occurs and marks the cluster node as ineligible to host the SAP HANA resource. From **October 27th 2025** , the severity of this evaluation rule has been updated from Caution to High. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [HA cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel).
    * For SLES, see [HA cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles).

Last updated: October 27, 2025

  * ####  Pacemaker: Use the recommended monitor settings for health check and ILB link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

In a Pacemaker configuration on Google Cloud Platform, the health check primitive and the Internal Load Balancer (ILB) primitive work together for high availability. The health check monitors the instance's status by listening on a specific port, while the ILB manages traffic routing. The recommended monitoring settings for health check are an `interval` of `10` seconds and a `timeout` of `20` seconds. The recommended monitoring settings for the ILB are an `interval` of `3600` seconds and a `timeout` of `60` seconds. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [Create a virtual IP address resource](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#create_a_virtual_ip_address_resource).
    * For SLES, see [Create a local cluster IP resource for the VIP address](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#create_a_local_cluster_ip_resource_for_the_vip_address).

Last updated: October 27, 2025

  * ####  Pacemaker: Update the resource location preference constraints link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

A Linux Pacemaker HA cluster contains a location preference constraint that has been set on one or more resources. For Linux Pacemaker HA clusters for SAP on Google Cloud, location constraints may prevent correct failover of cluster resources in the event of failure. These constraints often occur when a resource is manually moved between nodes in the cluster.

For more information, see the guide for your OS: 

    * For RHEL, see [Managing Cluster Resources](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/high_availability_add-on_reference/ch-manageresource-haar).
    * For SLES, see [Manual resource migration](https://www.suse.com/support/kb/doc/?id=000020246).

Last updated: April 16, 2025

  * ####  Pacemaker: Deactivate maintenance mode link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To allow a Linux Pacemaker high-availability cluster configuration to monitor and manage its application resources, the cluster nodes that host those resources must not be in the maintenance mode.

For more information, see the guide for your OS: 

    * For RHEL, see [Performing cluster maintenance](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_high_availability_clusters/assembly_cluster-maintenance-configuring-and-managing-high-availability-clusters).
    * For SLES, see [Enable and disable maintenance mode in a High Availability Cluster](https://www.suse.com/support/kb/doc/?id=000019250).

Last updated: April 16, 2025

  * ####  Pacemaker: Use the recommended value for the `resource-stickiness` parameter for SAP HANA link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

resource-stickiness parameter for SAP HANA">Details

In a Linux Pacemaker high-availability cluster for SAP HANA, set the `resource-stickiness` parameter to the recommended value of `1000`. This parameter defines how strongly a resource prefers to remain on its current node. The value of `1000` is high enough to minimize unnecessary migration of the resource to another node. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [Configuring general HA cluster properties](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/automating_sap_hana_scale-up_system_replication_using_the_rhel_ha_add-on/asmb_config_ha_cluster_automating-sap-hana-scale-up-system-replication#con_ha_cluster_properties_automating-sap-hana-scale-up-system-replication).
    * For SLES, see [Configuring cluster properties and resources](https://documentation.suse.com/sbp/sap-15/html/SLES4SAP-hana-sr-guide-PerfOpt-15/index.html#id-configuring-cluster-properties-and-resources).

Last updated: October 27, 2025

  * ####  Pacemaker: Use the recommended values for the SAP HANA primary and secondary resources link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

In a Linux Pacemaker high availability cluster for SAP HANA on Google Cloud, the meta attributes within the SAP HANA `msl` resource (classified as Primary or Secondary) determine how this resource is managed within the cluster. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [Creating Promotable SAPHana resource](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/automating_sap_hana_scale-up_system_replication_using_the_rhel_ha_add-on/asmb_config_ha_cluster_automating-sap-hana-scale-up-system-replication#con_promotable_res_automating-sap-hana-scale-up-system-replication).
    * For SLES, see [Create SAPHana resource](https://documentation.suse.com/sbp/sap-15/html/SLES4SAP-hana-sr-guide-PerfOpt-15/index.html#id-saphana).

Last updated: October 27, 2025

  * ####  Pacemaker: Use the recommended SAP HANA failover settings link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

In a Linux Pacemaker high availability cluster for SAP HANA on Google Cloud, the `SAPHana` resource contains configuration to control the availability and data protection of the SAP HANA System Replication that is managed by the HA cluster. Google Cloud recommends setting the values for the instance attributes as follows: `AUTOMATED_REGISTER=true`, `DUPLICATE_PRIMARY_TIMEOUT=7200`, and `PREFER_SITE_TAKEOVER=true`. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to Critical. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [Creating Promotable SAPHana resource](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/automating_sap_hana_scale-up_system_replication_using_the_rhel_ha_add-on/asmb_config_ha_cluster_automating-sap-hana-scale-up-system-replication#con_promotable_res_automating-sap-hana-scale-up-system-replication).
    * For SLES, see [Create SAPHana resource](https://documentation.suse.com/sbp/sap-15/html/SLES4SAP-hana-sr-guide-PerfOpt-15/index.html#id-saphana).

Last updated: October 27, 2025

  * ####  Pacemaker: Use the recommended values for the SAP HANA resource monitor operation link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

The `SAPHana` resource manages the instances that are part of the replicated SAP HANA pair. In the event of a failure to the SAP HANA primary replication instance, the `SAPHana` resource agent can trigger a takeover of SAP HANA System Replication based on how the resource agent parameters have been set. The `interval` and `timeout` values for the monitor operation should be set to the recommended values based upon the OS vendor. For Red Hat, the primary monitor should have an `interval` of `59` and a `timeout` of `700`, while the secondary monitor should have an `interval` of `61` and a `timeout` of `700`. For SUSE, the primary monitor should have an `interval` of `60` and a `timeout` of `700`, while the secondary monitor should have an `interval` of `61` and a `timeout` of `700`. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [Creating Promotable SAPHana resource](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/automating_sap_hana_scale-up_system_replication_using_the_rhel_ha_add-on/asmb_config_ha_cluster_automating-sap-hana-scale-up-system-replication#con_promotable_res_automating-sap-hana-scale-up-system-replication).
    * For SLES, see [Creating SAPHana resource](https://documentation.suse.com/sbp/sap-15/html/SLES4SAP-hana-sr-guide-PerfOpt-15/index.html#id-saphana).

Last updated: October 27, 2025

  * ####  Pacemaker: Upgrade the SUSE HA cluster and the SAP HANA HA/DR provider hooks to use **SAPHanaSR-angi** link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

To help ensure long-term support and stability for your SLES based HA cluster running SAP HANA, Google Cloud strongly recommends that you use the **SAPHanaSR-angi** resource agent package on SLES for SAP 15 SP6 or later. On SLES for SAP 16, **SAPHanaSR-angi** replaces the **SAPHana** and **SAPHanaSR-ScaleOut** packages.

For more information, see the following guides: 

    * [Upgrade to SAPHanaSR-angi in a scale-up HA cluster](https://docs.cloud.google.com/sap/docs/upgrade-suse-scale-up-to-angi).
    * SUSE articles for [What is SAPHanaSR-angi](https://www.suse.com/c/what-is-saphanasr-angi/) and [How to upgrade to SAPHanaSR-angi](https://www.suse.com/c/how-to-upgrade-to-saphanasr-angi/).

Last updated: March 12, 2026

  * ####  Pacemaker: Use the recommended settings for Stonith cluster property link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To preserve the integrity and high availability of the cluster, the Pacemaker configuration should enable STONITH to activate node fencing and have an appropriate timeout set to ensure the timely completion of STONITH operations. These settings are essential for isolating failed nodes and preventing them from disrupting the cluster's operations. It is recommended to set `stonith-enabled=true` and `stonith-timeout` to a value of `300` for optimal results. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to Critical. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [Set the cluster defaults](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#set_the_cluster_defaults).
    * For SLES, see [Configure the general cluster properties](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#configure_the_general_cluster_properties).

Last updated: October 27, 2025

  * ####  Pacemaker: Use the recommended values for the SAP HANA topology clone resource link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

In a Linux Pacemaker high availability cluster for SAP HANA on Google Cloud, the meta attributes within the SAP HANA topology clone resource determine how this resource is managed within the cluster. The recommended settings for a SAP HANA topology resource is a `clone_node_max` value of `1` and an `interleave` value of `true`. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [Creating cloned SAPHanaTopology resource](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/automating_sap_hana_scale-up_system_replication_using_the_rhel_ha_add-on/asmb_config_ha_cluster_automating-sap-hana-scale-up-system-replication#con_topology_res_automating-sap-hana-scale-up-system-replication).
    * For SLES, see [Creating SAPHanaTopology](https://documentation.suse.com/sbp/sap-15/html/SLES4SAP-hana-sr-guide-PerfOpt-15/index.html#id-saphanatopology).

Last updated: October 27, 2025

  * ####  Pacemaker: Use the recommended values for the SAP HANA topology monitor setting link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

A Linux Pacemaker HA cluster contains a `SAPHanaTopology` resource that includes a monitor operation which has an `interval` value and a `timeout` value. For Linux Pacemaker HA clusters for SAP on Google Cloud, we recommend a value between `10` and `60` seconds for the `interval`, and a value of `600` seconds for the `timeout`.

For more information, see the guide for your OS: 

    * For RHEL, see [Create the `SAPHanaTopology` resource](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#create_the_saphanatopology_resource).
    * For SLES, see [Create the `SAPHanaTopology` primitive resource](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#create_the_saphanatopology_primitive_resource).

Last updated: April 16, 2025

  * ####  Pacemaker: Use the recommended timeout values for the SAP HANA topology start/stop operation link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

The `timeout` parameter defines the maximum amount of time allowed for an operation (such as starting or stopping a resource) to complete. If the operation does not finish within this specified time, it is considered to have failed. The recommended settings for a SAP HANA topology resource is a `start` timeout value of `600` and a `stop` timeout value of `300`. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the guide for your OS: 

    * For RHEL, see [Create the SAPHanaTopology resource](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/automating_sap_hana_scale-up_system_replication_using_the_rhel_ha_add-on/asmb_config_ha_cluster_automating-sap-hana-scale-up-system-replication#con_topology_res_automating-sap-hana-scale-up-system-replication).
    * For SLES, see [SAPHanaTopology](https://documentation.suse.com/sbp/sap-15/html/SLES4SAP-hana-sr-guide-PerfOpt-15/index.html#id-saphanatopology).

Last updated: October 27, 2025

  * ####  High Availability: Use ENSA2 parameters for Enqueue Replicator link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

In systems where the SAP NetWeaver version supports ENSA2, but the `DEFAULT.PFL` file still contains ENSA1 parameters, this mismatch might cause issues with enqueue server functionality and cluster behavior. From **October 27th 2025** , the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see [Profile Parameters of Enqueue Replicator 2](https://help.sap.com/docs/ABAP_PLATFORM_NEW/cff8531bc1d9416d91bb6781e628d4e0/f4fe6dde1cd1406893824fb2d1b70382.html) in the SAP Help Portal.

Last updated: October 27, 2025

  * ####  High Availability: Ensure multi-zonal setup for SAP HANA link

**Severity:**

![Severity: High](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg)High

Details

To ensure resiliency of an SAP HANA high-availability configuration, the primary and secondary nodes must exist in different zones in the same region. From October 27th 2025, the severity of this evaluation rule has been updated from Medium to High. This change also applies to existing evaluations that include this rule.

For more information, see the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide).

Last updated: October 27, 2025

  * ####  High Availability: Set the system replication hook for SAP HANA link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

In an SAP HANA high availability configuration the HA/DR hooks monitor replication and individual services, such as the `indexserver`, provided by the Operating System vendor. These configurations impact SAP HANA from promptly reporting to the cluster if the secondary instance becomes out of sync or SAP HANA services crash.

For more information, see the guide for your OS: 

    * For RHEL, see [Enable the SAP HANA HA/DR provider hook](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#enable-hana-hadr-provider-hook).
    * For SLES, see [Enable the SAP HANA HA/DR provider hook](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#enable-hana-hadr-provider-hook).

Last updated: March 17, 2026




### SAP: NetWeaver (3 results)

  * ####  SAP NetWeaver: Use a certified custom VM type link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To receive support from SAP and Google Cloud for SAP NetWeaver on a Compute Engine custom VM, you must use a custom VM type that is certified by SAP and Google Cloud for use with SAP NetWeaver.

For more information, see [Certified machines](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#certified_machines) in the SAP NetWeaver planning guide.

Last updated: April 9, 2025

  * ####  SAP NetWeaver: Use a certified OS link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To receive support from SAP and Google Cloud for SAP NetWeaver on a Compute Engine VM, you must use an operating system version that is certified by SAP and Google Cloud for use with SAP NetWeaver.

For more information, see [OS support for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-os-support).

Last updated: February 18, 2026

  * ####  SAP NetWeaver: Use a certified VM type link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To receive support from SAP and Google Cloud for SAP NetWeaver on a Compute Engine VM, you must use a VM type and CPU platform that is certified by SAP and Google Cloud for use with SAP NetWeaver.

For more information, see [Machine types](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#machine_types) in the SAP NetWeaver planning guide.

Last updated: March 3, 2026




### SQL Server: Cost Optimization (2 results)

  * ####  SQL: 4-core consolidation link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

You might save SQL Server Per Core licensing costs by consolidating VMs with less than 4 cores. For more information, consult your licensing agreement.

[SQL Server Licensing](https://cloud.google.com/sql/pricing#sql-licensing).

Last updated: March 18, 2024

  * ####  SQL: Disable simultaneous multi-threading (SMT) link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

Disabling SMT reduces the number of vCPUs for each core by half, which might reduce your licensing costs. For more information, consult your licensing agreement. 

An industry best practice for an optimal TCO for most SQL Server workloads is to set the number of threads per core to one, and then to right-size the VM shape according to the workload requirements. Controlling the number of cores is further possible using custom visible cores. Consult your technical account manager for further details.

[how to set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

Last updated: February 7, 2024




### SQL Server: Failover Cluster (2 results)

  * ####  SQL: Enable failover clustering link

**Severity:**

![Severity: Critical](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg)Critical

Details

To enable failover clustering in the Compute Engine agent, you need to add the flag enable-wsfc=true to your VM metadata.

[Enabling failover clustering in Compute Engine](https://docs.cloud.google.com/compute/docs/tutorials/running-windows-server-failover-clustering#enabling_failover_clustering_in_compute_engine).

Last updated: January 11, 2024

  * ####  SQL: Network tags present link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Details

To allow clients to connect to SQL Server, allow communication between the WSFC nodes, and to enable the load balancer to perform health checks, firewall rules are applied to VMs with these network tags.

[Configure failover cluster instance](https://cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance#create_firewall_rules).

Last updated: October 6, 2025




### SQL Server: Performance (10 results)

  * ####  SQL: Enable the buffer pool extension link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

The buffer pool extension feature lets you push clean pages to a local SSD, instead of dropping them. This works along the same lines as virtual memory, which is to say, by swapping, and gives you access to the clean pages on the local SSD, which is faster than going to the regular disk to fetch the data.

[Enabling the buffer pool extension](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices#enabling_the_buffer_pool_extension) in Best practices for SQL Server VMs.

Last updated: January 11, 2024

  * ####  SQL: Format secondary disks link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

Formatting a disk with a 64 KB allocation unit lets SQL Server read and write extents more efficiently, which increases I/O performance from the disk.

Last updated: January 11, 2024

  * ####  SQL: Avoid index fragmentation link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

If one or more indexes are 95%+ fragmented, recommend scheduling defrag jobs.

Last updated: January 11, 2024

  * ####  SQL: Move data files and log files to a new disk link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

By default, the preconfigured image for SQL Server comes with everything installed on the boot persistent disk, which mounts as the `C:` drive. Consider attaching a secondary SSD persistent disk and moving the log files and data files to the new disk.

[Place data and log files on separate drives](https://learn.microsoft.com/en-us/sql/relational-databases/policy-based-management/place-data-and-log-files-on-separate-drives?view=sql-server-ver16) in SQL Server documentation.

Last updated: January 11, 2024

  * ####  SQL: Set the power profile to High-Performance link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

To configure SQL Server for optimal performance on Google Cloud, we recommend to set the power profile to High-Performance instead of Balanced.

[Setting the power profile](https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance#setting_the_power_profile).

Last updated: January 11, 2024

  * ####  SQL: Match max degree of parallelism to the number of CPUs on the server link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

The recommended default setting for max degree of parallelism is to match it to the number of CPUs on the server. In practice, 8 works as a good default value.

[Parallel query processing](https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance#setting_the_power_profile) in Best Practices for SQL Server VMs.

Last updated: January 11, 2024

  * ####  SQL: Use compressed tables link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

Compressing tables could make your system perform faster.

[Using compressed tables](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices#using_compressed_tables) in Best Practices for SQL Server VMs.

Last updated: January 11, 2024

  * ####  SQL: Use Local SSDs for tempDB link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Details

Create new SQL Server instances with one or more local SSDs to store the tempdb and Windows paging files.

Last updated: October 6, 2025

  * ####  SQL: Set log file to fixed amount and schedule regular backups link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

Consider disabling autogrowth and setting your log file to a fixed size.

Last updated: January 11, 2024

  * ####  SQL: Optimize Virtual Log Files link

**Severity:**

![Severity: Low](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg)Low

Details

Monitor Virtual Log File growth and take action to prevent log file fragmentation.

[Optimizing virtual log files](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices#optimizing_virtual_log_files) in Best Practices for SQL Server VMs.

Last updated: October 6, 2025




### SQL Server: Stability (3 results)

  * ####  SQL: Perform backup regularly link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

When taking regular database backups, be careful not to consume too many persistent disk IOPS. Use the local SSD to stage your backups and then push them to a Cloud Storage bucket.

[Backing up](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices#backing_up) in Best practices for SQL Server VMs.

Last updated: January 11, 2024

  * ####  SQL: Google Cloud Backup and Disaster Recovery agent not detected link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

Consider Google's backup and disaster recovery solutions for optimal protection.

[Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).

Last updated: June 25, 2024

  * ####  SQL: Match max server memory setting with available physical memory on the instance link

**Severity:**

![Severity: Medium](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg)Medium

Details

Max Server Memory setting matches available physical memory on the instance.

Last updated: January 11, 2024




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
