---
url: https://docs.cloud.google.com/recommender/docs/recommenders/
title: Recommenders \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:54.809736+00:00
---

# Recommenders  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/recommenders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Recommenders

A [recommender](https://docs.cloud.google.com/recommender/docs/key-concepts#recommenders) is a service on Google Cloud that provides usage recommendations for Google Cloud resources. Recommenders are specific to a single Google Cloud product and resource type. A single product can have multiple recommenders, where each provides a different type of recommendation for a different resource.

Recommender has the following recommenders:

Value Category | Name | Recommender ID | Short Description | Included in [BigQuery Export](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq)  
---|---|---|---|---  
Cost | [BigQuery edition slot recommender](https://docs.cloud.google.com/bigquery/docs/slot-recommender) | `google.bigquery.capacityCommitments.Recommender` | Optimize BigQuery spend with slot commitments | No  
[Spend-based committed use discount recommender](https://docs.cloud.google.com/docs/cuds-recommender) | `google.cloudbilling.commitment.SpendBasedCommitmentRecommender` | Reduce costs through spend-based commitments | No  
[Spend-based committed use discount recommender](https://docs.cloud.google.com/docs/cuds-recommender) | `google.cloudbilling.commitment.SpendBasedCommitmentRecommender` | Reduce costs through spend-based commitments | No  
[BigQuery partitioning and clustering recommender](https://docs.cloud.google.com/bigquery/docs/view-partition-cluster-recommendations) | `google.bigquery.table.PartitionClusterRecommender` | Partition or cluster your tables  | Yes  
[Soft delete recommender](https://docs.cloud.google.com/storage/docs/soft-delete-recommender) | `google.storage.bucket.SoftDeleteRecommender` | Enable or disable soft delete based on costs and security | No  
[Cloud Run CPU allocation recommender](https://docs.cloud.google.com/run/docs/recommender) | `google.run.service.CostRecommender` | Switch to CPU always allocated  | Yes  
[Cloud SQL idle instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-idle) | `google.cloudsql.instance.IdleRecommender` | Remove unused SQL instances | Yes  
[Cloud SQL overprovisioned instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned) | `google.cloudsql.instance.OverprovisionedRecommender` | Resize overprovisioned SQL instances | Yes  
[Resource-based committed use discount recommender](https://docs.cloud.google.com/docs/cuds-recommender) | `google.compute.commitment.UsageCommitmentRecommender` | Reduce costs through Compute Engine resource-based commitments | Yes  
[Idle custom image recommender](https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations) | `google.compute.image.IdleResourceRecommender` | Remove unused images | Yes  
[Idle GKE cluster recommender](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/idle-clusters) | `google.container.DiagnosisRecommender` | Remove unused GKE clusters | Yes  
[Idle IP address recommender](https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations) | `google.compute.address.IdleResourceRecommender` | Remove unused IPs | Yes  
[Idle persistent disk recommender](https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations) | `google.compute.disk.IdleResourceRecommender` | Backup and remove unused disks | Yes  
[Idle VM recommender](https://docs.cloud.google.com/compute/docs/instances/idle-vm-recommendations-overview) | `google.compute.instance.IdleResourceRecommender` | Remove unused VMs | Yes  
[Idle reservations recommender](https://docs.cloud.google.com/compute/docs/instances/reservation-recommendations-overview) | `google.compute.IdleResourceRecommender` | Delete unused resource reservations | Yes  
[Underutilized reservations recommender](https://docs.cloud.google.com/compute/docs/instances/reservation-recommendations-overview) | `google.compute.RightSizeResourceRecommender` | Right-size underutilized reservations | Yes  
Security | [Identity and Access Management recommender](https://docs.cloud.google.com/iam/docs/recommender-overview) | `google.iam.policy.Recommender` | Remove excess permissions | Yes  
[Cloud Run Service Security recommenders](https://docs.cloud.google.com/run/docs/recommender) | `google.run.service.IdentityRecommender  
google.run.service.SecurityRecommender` | Increase Cloud Run Service security | Yes  
[Unattended project recommender](https://docs.cloud.google.com/recommender/docs/unattended-project-recommender) | `google.resourcemanager.projectUtilization.Recommender` | Reclaim or remove unused projects | Yes  
[Advisory Notifications recommender](https://docs.cloud.google.com/advisory-notifications/docs/recommendations-overview) | `google.cloud.security.GeneralRecommender` | Ensure that the right parties within your organization have access to view critical security and privacy notifications | Yes  
Cloud SQL security recommender  |  `google.cloudsql.instance.SecurityRecommender` |  Secure Cloud SQL instances 
* [Remove broad public IP ranges](https://docs.cloud.google.com/sql/docs/mysql/recommender-broad-address)
* [Disable public IP connection](https://docs.cloud.google.com/sql/docs/mysql/recommender-disable-public-ip)
* [Enable database auditing](https://docs.cloud.google.com/sql/docs/mysql/recommender-enable-db-audit)
* [Remove authorized networks](https://docs.cloud.google.com/sql/docs/mysql/recommender-remove-authorized-networks)
* [Require SSL for direct connections](https://docs.cloud.google.com/sql/docs/mysql/recommender-require-ssl)
* [Rotate server certificate](https://docs.cloud.google.com/sql/docs/mysql/recommender-rotate-cert)
* [Enable instance password policies](https://docs.cloud.google.com/sql/docs/mysql/recommender-set-password-policy)
* [Enable user password policies](https://docs.cloud.google.com/sql/docs/mysql/recommender-set-password-policy)
| Yes  
[ Cloud Firestore Security rules recommender ](https://cloud.google.com/firestore/docs/firestore-security-rules-recommender) | [ `google.firestore.database.FirebaseRulesRecommender` ](https://cloud.google.com/firestore/docs/firestore-security-rules-recommender) |  Improve Firestore database firebase rules security. It has the following subtypes: 
* Update insecure policy
| No  
[ VPC Service Controls recommender ](https://docs.cloud.google.com/vpc-service-controls/docs/recommender) ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  `google.accessContextManager.VpcScRecommender` |  Help protect Google Cloud resources from data exfiltration by optimizing service perimeters and aligning VPC accessible services configurations.  | Yes  
Performance | [Rapid Cache recommender](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache-recommender) | `google.storage.bucket.AnywhereCacheRecommender` | Cache your data in Cloud Storage with Rapid Cache | Yes  
[Managed instance group machine type recommender](https://docs.cloud.google.com/compute/docs/instance-groups/apply-machine-type-recommendations-managed-instance-groups) | `google.compute.instanceGroupManager.MachineTypeRecommender` | Resize MIG machine types | Yes  
[VM machine type recommender](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances) | `google.compute.instance.MachineTypeRecommender` | Resize VM machine types | Yes  
[Cloud Functions minimum instances recommender](https://docs.cloud.google.com/functions/docs/configuring/recommender) | `google.cloudfunctions.PerformanceRecommender` | Prevent cold starts for deployed functions | Yes  
Cloud SQL performance recommender  |  `google.cloudsql.instance.PerformanceRecommender` |  Improve Cloud SQL instance performance 
* [MySQL high number of open tables](https://docs.cloud.google.com/sql/docs/mysql/recommender-high-number-of-open-tables)
* [MySQL high number of tables](https://docs.cloud.google.com/sql/docs/mysql/recommender-high-number-of-tables)
* [PostgreSQL high transaction id utilization](https://docs.cloud.google.com/sql/docs/postgres/recommender-high-transactionid-utilization)
| Yes  
[Cloud SQL underprovisioned recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-underprovisioned) | `google.cloudsql.instance.UnderprovisionedRecommender` | Optimize underprovisioned Cloud SQL instances | Yes  
Reliability | [GKE diagnosis recommender](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders) | `google.container.DiagnosisRecommender` | Mitigate risks, troubleshoot and optimize your usage of GKE | Yes  
[Service limit (quota) recommender](https://docs.cloud.google.com/recommender/docs/service-limit-quota-recommender) | `google.resourcemanager.serviceLimit.Recommender` | Manage service and quota usage to avoid hitting limits | Yes  
[Cloud SQL Reliability recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-enable-ha) | `google.cloudsql.instance.ReliabilityRecommender` | Enable High Availability on Cloud SQL Instances | Yes  
[Cloud SQL out-of-disk recommender](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender) | `google.cloudsql.instance.OutOfDiskRecommender` | Prevent Cloud SQL out-of-disk outage | Yes  
[Change Risk Recommendations](https://docs.cloud.google.com/recommender/docs/change-risk-recommendations) | `google.resourcemanager.project.ChangeRiskRecommender  
google.iam.serviceAccount.ChangeRiskRecommender  
google.iam.policy.ChangeRiskRecommender` | Reduce risk of misconfigurations | No  
[Recent Change Recommendations](https://docs.cloud.google.com/recommender/docs/recent-change-recommendations) | `google.cloud.RecentChangeRecommender` | Reduce risk of misconfigurations | Yes  
[ Firestore Reliability recommender ](https://cloud.google.com/firestore/docs/reliability-recommender) |  `google.firestore.database.ReliabilityRecommender`  
[ Improve Firestore database disaster recovery plan. It has the following subtypes:](https://cloud.google.com/firestore/docs/reliability-recommender)   

* Enable scheduled backups
* Enable PITR
| No  
[ Compute Reliability Insights recommender ](https://docs.cloud.google.com/compute/docs/reliability-insights-overview) |  `google.compute.ReliabilityRiskRecommender` | [ Improve workload reliability by addressing misconfigurations on Compute Engine resources. It has the following subtypes:](https://docs.cloud.google.com/compute/docs/reliability-insights-overview)   

* GLOBAL_DNS
| No  
Manageability | [Deprecation and Breaking Changes recommender](https://docs.cloud.google.com/recommender/docs/deprecation-change-recommender) | `google.cloud.deprecation.GeneralRecommender` | Prevent service interruptions due to deprecations and breaking changes | Yes  
[Error Reporting notification recommender](https://docs.cloud.google.com/recommender/docs/error-reporting/notification-recommender) | `google.clouderrorreporting.Recommender` | Receive notifications for errors in your project | No  
[Google Maps Platform project management recommender](https://docs.cloud.google.com/recommender/docs/gmp-project-management-recommender) | `google.gmp.project.ManagementRecommender` | Restrict your API keys | No  
[Product suggestion recommender](https://docs.cloud.google.com/recommender/docs/product-suggestion-recommender) | `google.logging.productSuggestion.ContainerRecommender` | Explore more helpful products | No  
  
## What's next

  * For _Cloud Billing account managers_ , explore the [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub), which uses recommenders to provide cost-optimization recommendations for your Google Cloud resources.

  * For _developers and platform administrators_ , explore the Optimization page in [Cloud Hub](https://docs.cloud.google.com/hub/docs/optimize), which provides summary cost data, utilization data, and cost optimization recommendations for your Google Cloud resources.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
