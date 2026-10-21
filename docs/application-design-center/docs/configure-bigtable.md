---
url: https://docs.cloud.google.com/application-design-center/docs/configure-bigtable/
title: Configure a Bigtable instance \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:54.351470+00:00
---

# Configure a Bigtable instance  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-bigtable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Bigtable instance Stay organized with collections  Save and categorize content based on your preferences. 

App Design Center lets you configure connections and parameters to provision [Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) instances based on the [terraform-google-bigtable](https://github.com/GoogleCloudPlatform/terraform-google-bigtable) Terraform module. This setup provides low-latency key-value and wide-column storage for high-throughput workloads such as clickstream data, IoT telemetry, and machine learning.

## Component connections

The following table lists components you can connect to a Bigtable instance and the resulting updates to your application and Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instances can connect to and manage the Bigtable instance.
  * The Bigtable resource metadata is added to the Compute Engine instance template.
  * The `roles/bigtable.admin` role is added to the Compute Engine instance template service account.

| [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can perform administrative functions on the Bigtable instance.
  * The Bigtable resource metadata is added to the Cloud Run environment variables.
  * The `roles/bigtable.admin` role is added to the Cloud Run service account.

| [What is Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)  
  
## Required configuration parameters

If your template includes a Bigtable component, you must configure the following Bigtable instance parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you deploy the Bigtable instance. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Name** | [name](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances#Instance.FIELDS.name) | [name](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_instance#name-2)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Subfeature | Parameter name | Description and constraint information | Background information  
---|---|---|---|---  
|  | **Display Name** | [displayName](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances#Instance.FIELDS.display_name) | [display_name](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_instance#display_name-1)  
Zones |  | **Key** | The `zones` map object key. | [zones](https://github.com/GoogleCloudPlatform/terraform-google-bigtable/tree/main?tab=readme-ov-file#inputs)  
| **Zone** | [location](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters#Cluster.FIELDS.location) | [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations)  
| **Cluster ID** | [clusterID](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters/create#body.QUERY_PARAMETERS.cluster_id) | [cluster_id](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_instance#cluster_id-1)  
| **Num Nodes** | [serveNodes](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters#Cluster.FIELDS.serve_nodes) | [Nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes)  
| **KMS Key Name** | [kmsKeyName](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters#EncryptionConfig.FIELDS.kms_key_name) | [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/bigtable/docs/cmek)  
Autoscaling Config | **Min Nodes** | [minServeNodes](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters#AutoscalingLimits.FIELDS.min_serve_nodes) | [Determine the minimum number of nodes](https://docs.cloud.google.com/bigtable/docs/autoscaling#determine-min)  
**Max Nodes** | [maxServeNodes](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters#AutoscalingLimits.FIELDS.max_serve_nodes) | [Determine the maximum number of nodes](https://docs.cloud.google.com/bigtable/docs/autoscaling#determine-max)  
**CPU Target** | [cpuUtilizationPercent](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters#AutoscalingTargets.FIELDS.cpu_utilization_percent) | [Determine the CPU utilization target](https://docs.cloud.google.com/bigtable/docs/autoscaling#determine-cpu)  
**Storage Target** | [storageUtilizationGibPerNode](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters#AutoscalingTargets.FIELDS.storage_utilization_gib_per_node) | [Determine the storage utilization target](https://docs.cloud.google.com/bigtable/docs/autoscaling#determine-storage-utilization)  
Tables |  | **Key** | The `tables` map object key. | [tables](https://github.com/GoogleCloudPlatform/terraform-google-bigtable/tree/main?tab=readme-ov-file#inputs)  
| **Table Name** | [name](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables#Table.FIELDS.name) | [name](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_table#name-3)  
| **Split Keys** | [split_keys](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_table#split_keys-2) | [Optional: Split the table by row key](https://docs.cloud.google.com/bigtable/docs/managing-tables#splits)  
| **Deletion Protection** | [deletion_protection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_table#deletion_protection-1) | [Modify deletion protection](https://docs.cloud.google.com/bigtable/docs/managing-tables#modify-deletion-protection)  
| **Change Stream Retention** | [retentionPeriod](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables#changestreamconfig) | [Change streams overview](https://docs.cloud.google.com/bigtable/docs/change-streams-overview)  
Automated Backup Policy | **Retention Period** | [retentionPeriod](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables#AutomatedBackupPolicy.FIELDS.retention_period) | [Use automated backup](https://docs.cloud.google.com/bigtable/docs/managing-backups#use-automated-backup)  
**Frequency** | [frequency](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables#AutomatedBackupPolicy.FIELDS.frequency) | [Use automated backup](https://docs.cloud.google.com/bigtable/docs/managing-backups#use-automated-backup)  
Column Family | **Key** | The `column_family` map object key, which is in the `tables` object. | [column_family](https://github.com/GoogleCloudPlatform/terraform-google-bigtable/tree/main?tab=readme-ov-file#inputs)  
**Family** | [family](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables#columnfamily) | [Column families](https://docs.cloud.google.com/bigtable/docs/schema-design#column-families)  
|  | **Deletion Protection** | When selected, a `terraform apply` or `terraform destroy` that would delete the instance fails. When not selected, the instance can be deleted. | [deletion_protection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_instance.html#deletion_protection-1)  
|  | **Storage Type** | [defaultStorageType](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters#Cluster.FIELDS.default_storage_type) | [Choose between SSD and HDD storage](https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd)  
Labels |  | **Key** | [labels](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances#Instance.FIELDS.labels) | [Create and manage instance labels](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels)  
| **Value** | [labels](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances#Instance.FIELDS.labels) | [Create and manage instance labels](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
