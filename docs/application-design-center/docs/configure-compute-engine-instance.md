---
url: https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance/
title: Configure a Compute Engine instance template \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:36.327341+00:00
---

# Configure a Compute Engine instance template  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Compute Engine instance template Stay organized with collections  Save and categorize content based on your preferences. 

In Application Design Center, you can configure a Compute Engine [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) to define the virtual machine (VM) configuration for creating identical VM instances and instance groups. You can customize the instance template for your specific component connections and configuration parameters. The configuration parameters are listed in the [instance_template](https://github.com/terraform-google-modules/terraform-google-vm/tree/main/modules/instance_template) Terraform module.

## Component connections

The following table includes the components that you can connect to a Compute Engine instance template, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Service Account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The Compute Engine instance template uses the connected service account instead of creating a new service account. The connected service account is used for authentication and authorization to other Google Cloud services.
  * The service account email and IAM information are added to the Compute Engine instance template.

| [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)  
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/application-design-center/docs/configure-alloydb) | 

  * The Compute Engine instances can connect to the AlloyDB for PostgreSQL instance.
  * The AlloyDB for PostgreSQL resource metadata information is added to the instance template.
  * The `roles/alloydb.admin` role is added to the Compute Engine instance template service account.

| [Connect from Compute Engine](https://docs.cloud.google.com/alloydb/docs/connect-psql)  
[BigQuery](https://docs.cloud.google.com/application-design-center/docs/configure-bigquery) | 

  * The Compute Engine instances can read and write data to the BigQuery dataset.
  * The BigQuery resource metadata is added to the Compute Engine instance template.
  * The `roles/bigquery.dataEditor` role is added to Compute Engine instance template service account.

| [BigQuery overview](https://docs.cloud.google.com/bigquery/docs/overview)  
[Bigtable](https://docs.cloud.google.com/application-design-center/docs/configure-bigtable) | 

  * The Compute Engine instances can access the Bigtable instance.
  * The Bigtable resource metadata information is added to the instance template.
  * The `roles/bigtable.admin` role is added to the Compute Engine instance template service account.

| [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)  
[Cloud SQL (MySQL)](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-mysql) | 

  * The Compute Engine instances can connect and read and write data to the Cloud SQL (MySQL) instance.
  * The Cloud SQL connection metadata is added to the Compute Engine instance template.
  * The `roles/cloudsql.instanceUser` and `roles/cloudsql.client` roles are added to the Compute Engine instance template service account.
  * The Compute Engine service account is added as an IAM user to the Cloud SQL instance.

| [Connect from Compute Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-compute-engine)  
[Cloud SQL (PostgreSQL)](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-postgresql) | 

  * The Compute Engine instances can connect and read and write data to the Cloud SQL (PostgreSQL) instance.
  * The Cloud SQL connection metadata is added to the Compute Engine instance template.
  * The `roles/cloudsql.instanceUser` and `roles/cloudsql.client` roles are added to the Compute Engine instance template service account.
  * The Compute Engine service account IAM information is added to the Cloud SQL instance.

| [Connect from Compute Engine](https://docs.cloud.google.com/sql/docs/postgres/connect-compute-engine)  
[Cloud Storage](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-storage) | 

  * The Compute Engine instances can control bucket objects, including listing, creating, viewing, and deleting objects.
  * The `roles/storage.objectAdmin` role is assigned to the Compute Engine instance template service account.

| [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)  
[Memorystore for Redis](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis) | 

  * The Compute Engine instances can manage and cache data in the Memorystore instance.
  * App Design Center populates the Memorystore for Redis connection information into the Compute Engine metadata.

| [Deployment options for Redis on Google Cloud](https://docs.cloud.google.com/compute/docs/redis/deployment-options)  
[Memorystore for Redis Cluster](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis-cluster) | 

  * The Compute Engine instances can manage and cache data in the Memorystore for Redis Cluster instance.
  * App Design Center populates the Memorystore for Redis Cluster connection information into the Compute Engine metadata.

| [Connect to a Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance)  
[Memorystore for Valkey](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-valkey) | 

  * The Compute Engine instances can manage and cache data in the Memorystore for Valkey instance.
  * App Design Center populates the Memorystore for Valkey connection information into the Compute Engine metadata.

| [Connect to a Memorystore for Valkey instance](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance)  
[Pub/Sub](https://docs.cloud.google.com/application-design-center/docs/configure-pubsub) | 

  * The Compute Engine instances can publish to and receive messages from the Pub/Sub topic.
  * The Pub/Sub topic ID is added to the Compute Engine instance template metadata.

| [Subscription overview](https://docs.cloud.google.com/pubsub/docs/subscription-overview)  
[Regional Cloud Load Balancing frontend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-frontend) | 

  * The Compute Engine instances can redirect traffic to the regional Cloud Load Balancing frontend.
  * The Cloud Load Balancing address is added to the Compute Engine instance template.

| [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
[Spanner](https://docs.cloud.google.com/application-design-center/docs/configure-spanner) | 

  * The Compute Engine instances can read and write data in the Spanner instance.
  * The `roles/spanner.databaseAdmin` role is added to the Compute Engine instance template service account.
  * The Compute Engine IAM information is added to the Spanner instance.

| [Using Spanner in a virtual machine instance](https://docs.cloud.google.com/spanner/docs/configure-virtual-machine-instance)  
[Vertex AI](https://docs.cloud.google.com/application-design-center/docs/configure-vertex-ai) | 

  * The Compute Engine instances can interact with Vertex AI services.
  * The `roles/aiplatform.user` role is added to the Compute Engine instance template service account.

| [Vertex AI access control with IAM](https://docs.cloud.google.com/vertex-ai/docs/general/access-control)  
[Compute Engine (MIG)](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-mig) | 

  * The Compute Engine instance template is used to create instances in the managed instance group.
  * The instance template self link is added to the Compute Engine MIG.

| [Basic scenarios for creating managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances)  
  
## Required configuration parameters

If your template includes a Compute Engine instance template component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to create the Compute Engine instance template. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Region** | The region where the instance template is created. | [Regional and global instance templates](https://docs.cloud.google.com/compute/docs/instance-templates#regional_and_global_instance_templates)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Name Prefix** | The name prefix for the instance template. | [name_prefix](https://github.com/terraform-google-modules/terraform-google-vm/blob/main/modules/instance_template/README.md#inputs)  
| **Machine Type** | [properties.machineType](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_5) | [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource)  
| **Spot** | [spot](https://github.com/terraform-google-modules/terraform-google-vm/blob/main/modules/instance_template/README.md#inputs) | [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)  
| **Description** | A description for the instance template. | [description](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.description)  
| **Instance Description** | A description for the instances generated by the template. | [properties.description](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField)  
| **Automatic Restart** | [properties.scheduling.automaticRestart](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_129) | [Maintenance and restart behaviors](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors)  
| **Threads Per Core** | [properties.advancedMachineFeatures.threadsPerCore](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_164) | [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core)  
| **Source Image** | [properties.disks[].initializeParams.sourceImage](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_57) | [OS images](https://docs.cloud.google.com/compute/docs/images)  
| **Source Image Project** | Project where the source image comes from. The default project contains Rocky Linux images. | [Image families](https://docs.cloud.google.com/compute/docs/images#image_families)  
| **Disk Size GB** | [properties.disks[].initializeParams.diskSizeGb](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_58) | [Create a customized boot disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks)  
| **Disk Type** | [properties.disks[].initializeParams.diskType](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_59) | [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks)  
| **Network** | [properties.networkInterfaces[].network](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_9) | [Networking overview for VMs](https://docs.cloud.google.com/compute/docs/networking/network-overview)  
| **Subnetwork** | [properties.networkInterfaces[].subnetwork](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_10) | [Networks and subnets](https://docs.cloud.google.com/compute/docs/networking/network-overview#subnets)  
| **Create Service Account** | [create_service_account](https://github.com/terraform-google-modules/terraform-google-vm/blob/main/modules/instance_template/README.md#inputs) | [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts)  
| **Min CPU Platform** | [properties.minCPUPlatform](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_148) | [Specify a minimum CPU platform for VM instances](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform)  
| **Can IP Forward** | [properties.canIpForward](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_6) | [Enable IP forwarding for instances](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward)  
| **Tags** | [properties.tags](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_1) | [Manage tags for resources](https://docs.cloud.google.com/compute/docs/tag-resources)  
Labels | **Key** | [properties.labels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_144) | [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources)  
**Value** | [properties.labels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_144) | [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources)  
| **Preemptible** | [properties.scheduling.preemptible](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_130) | [Preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible)  
| **Maintenance Interval** | The frequency of planned maintenance events. | [Enable advanced maintenance control on a sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control#opt-in)  
| **On Host Maintenance** | [properties.scheduling.onHostMaintenance](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_128) | [Set the host maintenance policy for a compute instance](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options)  
| **Spot Instance Termination Action** | [properties.scheduling.instanceTerminationAction](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_139) | [Preemption process](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-process)  
| **Enable Nested Virtualization** | [properties.advancedMachineFeatures.enableNestedVirtualization](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_163) | [About nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview)  
| **Resource Policies** | [properties.resourcePolicies[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_157) | [REST Resource: resourcePolicies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies)  
| **Source Image Family** | [properties.disks[].initializeParams.sourceImage](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_57) | [Image families](https://docs.cloud.google.com/compute/docs/images#image_families)  
Disk Labels | **Key** | [properties.disks[].initializeParams.labels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_66) | [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources)  
**Value** | [properties.disks[].initializeParams.labels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_66) | [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources)  
| **Disk Encryption Key** | [properties.disks[].diskEncryptionKey](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_90) | [Encrypt disks with customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption)  
| **Auto Delete** | [properties.disks[].autoDelete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_85) | [Set the auto-delete state of a Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete)  
[Additional Disks](https://github.com/terraform-google-modules/terraform-google-vm/blob/main/modules/instance_template/README.md#inputs) | **Boot** | [properties.disks[].boot](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_54) | [Create a customized boot disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks)  
**Device Name** | [properties.disks[].deviceName](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_52) | [Adding a non-boot disk to your VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk)  
**Disk Name** | [properties.disks[].initializeParams.diskName](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_56) | [Adding a non-boot disk to your VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk)  
**Interface** | [properties.disks[].interface](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_87) | [Storage interface types](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface)  
**Mode** | [properties.disks[].mode](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_49) | [Create a regional disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_create_disk)  
**Source** | [properties.disks[].source](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_51) | [Create a regional disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_create_disk)  
**Source Image** | The source image to create this disk. | [properties.disks[].initializeParams.sourceImage](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_57)  
**Source Snapshot** | The source snapshot to create this disk. | [properties.disks[].initializeParams.sourceSnapshot](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_67)  
| **Disk Resource Policies** | [properties.disks[].initializeParams.resourcePolicies[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_76) | [REST Resource: resourcePolicy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies)  
| **Subnetwork Project** | The ID of the project in which the subnetwork belongs. If it is not provided, the provider project is used. | [subnetwork_project](https://github.com/terraform-google-modules/terraform-google-vm/blob/main/modules/instance_template/README.md#inputs)  
| **Network IP** | [properties.networkInterfaces[].networkIP](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_76) | [Internal IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#networkaddresses)  
| **NIC Type** | [properties.networkInterfaces[].nicType](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_44) | [Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic)  
| **Stack Type** | [properties.networkInterfaces[].stackType](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_41) | [Stack types](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types)  
[Additional Networks](https://github.com/terraform-google-modules/terraform-google-vm/blob/main/modules/instance_template/README.md#inputs) | **Network** | [properties.networkInterfaces[].network](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_9) | [Networking overview for VMs](https://docs.cloud.google.com/compute/docs/networking/network-overview)  
**Subnetwork** | [properties.networkInterfaces[].subnetwork](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_10) | [Networks and subnets](https://docs.cloud.google.com/compute/docs/networking/network-overview#subnets)  
**Queue Count** | [properties.networkInterfaces[].queueCount](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_43) | [Default queue allocation](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx-equations)  
| **Total Egress Bandwidth Tier** | [properties.networkPerformanceConfig.totalEgressBandwidthTier](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_170) | [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth)  
| **Startup Script** | A script that executes when the instances start. | [About startup scripts](https://docs.cloud.google.com/compute/docs/instances/startup-scripts)  
Metadata | **Key** | [properties.metadata](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_112) | [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview#project_and_instance_metadata)  
**Value** | [properties.metadata](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_112) | [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview#project_and_instance_metadata)  
Service Account | **Email** | [email](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template#email-1) | [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts)  
**Service Account Project Roles** | [project_roles](https://github.com/terraform-google-modules/terraform-google-service-accounts#inputs) | [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts)  
| **Enable Shielded VM** | Select the checkbox to enable Shielded VM, if supported by the selected instance image. | [About Shielded VM](https://docs.cloud.google.com/compute/docs/about-shielded-vm)  
Shielded Instance Config | **Enable Secure Boot** | [properties.shieldedInstanceConfig.enableSecureBoot](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_154) | [Secure boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot)  
**Enable vTPM** | [properties.shieldedInstanceConfig.enableVtpm](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_155) | [Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm)  
**Enable Integrity Monitoring** | [properties.shieldedInstanceConfig.enableIntegrityMonitoring](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_156) | [Integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring)  
| **Enable Confidential VM** | [properties.confidentialInstanceConfig.enableConfidentialCompute](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_159) | [About Confidential VM](https://docs.cloud.google.com/compute/docs/about-confidential-vm)  
| **Confidential Instance Type** | [properties.confidentialInstanceConfig.confidentialInstanceType](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_160) | [Supported configurations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations)  
Access Config | **NAT IP** | [properties.networkInterfaces[].accessConfigs[].natIP](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_19) | [External IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses)  
**Network Tier** | [properties.networkInterfaces[].accessConfigs[].networkTier](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_24) | [Network Service Tiers](https://docs.cloud.google.com/compute/docs/networking/network-overview#network-tiers)  
IPv6 Access Config | **Network Tier** | [properties.networkInterfaces[].ipv6AccessConfigs[].networkTier](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_35) | [Network Service Tiers](https://docs.cloud.google.com/compute/docs/networking/network-overview#network-tiers)  
GPU | **Type** | [properties.guestAccelerators[].acceleratorType](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_146) | [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus)  
**Count** | [properties.guestAccelerators[].acceleratorCount](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_147) | [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus)  
Alias IP Range | **IP CIDR Range** | [properties.networkInterfaces[].aliasIpRanges[].ipCidrRange](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_38) | [IP addresses](https://docs.cloud.google.com/compute/docs/networking/network-overview#ip-addresses)  
**Subnetwork Range Name** | [properties.networkInterfaces[].aliasIpRanges[].subnetworkRangeName](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates#InstanceTemplate.FIELDS.inlinedField_39) | [Networks and subnets](https://docs.cloud.google.com/compute/docs/networking/network-overview#subnets)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
