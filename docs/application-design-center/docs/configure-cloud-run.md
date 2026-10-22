---
url: https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run/
title: Configure a Cloud Run service \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:36.251144+00:00
---

# Configure a Cloud Run service  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Cloud Run service Stay organized with collections  Save and categorize content based on your preferences. 

In Application Design Center, you can configure a [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) service to run stateless containers directly on Google's scalable, fully managed infrastructure. You can customize the service for your specific component connections and configuration parameters. The configuration parameters are listed in the [terraform-google-cloud-run](https://github.com/GoogleCloudPlatform/terraform-google-cloud-run/tree/main/modules/v2) Terraform module.

## Component connections

The following table includes the components that you can connect to a Cloud Run service, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Secret Manager](https://docs.cloud.google.com/application-design-center/docs/configure-secret-manager) | 

  * The Cloud Run service can reference the secret data.
  * The Secret Manager **Secret Data** field is referenced by the Cloud Run `env_secret_vars` field.
  * The `roles/secretmanager.secretAccessor` role is added to the Cloud Run service account.

| [Configure secrets for services](https://docs.cloud.google.com/run/docs/configuring/services/secrets)  
[Service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The Cloud Run service uses the service account as a [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity).
  * The `roles/run.invoker` role is added to the service account.
  * The service account email and IAM information are added to the Cloud Run environment variables.

| [Authenticating service-to-service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service)  
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/application-design-center/docs/configure-alloydb) | 

  * The Cloud Run service can connect to the AlloyDB for PostgreSQL instance.
  * The AlloyDB for PostgreSQL resource metadata is added to the Cloud Run environment variables.
  * The AlloyDB for PostgreSQL `roles/alloydb.admin` role is added to the Cloud Run service account.

| [Connect from Cloud Run](https://docs.cloud.google.com/alloydb/docs/quickstart/integrate-cloud-run)  
[BigQuery](https://docs.cloud.google.com/application-design-center/docs/configure-bigquery) | 

  * The Cloud Run service can interact with the BigQuery dataset.
  * The BigQuery resource metadata is added to the Cloud Run environment variables.
  * The BigQuery `roles/bigquery.dataEditor` role is added to the Cloud Run service account.

| [BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction)  
[Bigtable](https://docs.cloud.google.com/application-design-center/docs/configure-bigtable) | 

  * The Cloud Run service can perform administrative functions on the Bigtable instance.
  * The Bigtable resource metadata information is added to the Cloud Run environment variables.
  * The `roles/bigtable.admin` role is added to the Cloud Run service account.

| [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)  
Another Cloud Run service | 

  * The source Cloud Run service can send traffic to the destination Cloud Run service.
  * The source Cloud Run service contains the destination Cloud Run service URI in its environment variables.

| [What is Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)  
[Cloud SQL (MySQL)](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-mysql) | 

  * The Cloud Run service can read and write data to the Cloud SQL (MySQL) instance.
  * The Cloud SQL connection metadata is added to the Cloud Run service.
  * The `roles/cloudsql.instanceUser` and `roles/cloudsql.client` roles are added to the Cloud Run service account.
  * The Cloud Run service account is added as an IAM user to the Cloud SQL instance.

| [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)  
[Cloud SQL (PostgreSQL)](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-postgresql) | 

  * The Cloud Run service can read and write data to the Cloud SQL (PostgreSQL) instance.
  * The Cloud SQL connection metadata is added to the Cloud Run service.
  * The `roles/cloudsql.instanceUser` and `roles/cloudsql.client` roles are added to the Cloud Run service account.
  * The Cloud Run service account is added as an IAM user to the Cloud SQL instance.

| [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run)  
[Cloud Storage](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-storage) | 

  * The Cloud Run service can manage objects in the Cloud Storage bucket.
  * The Cloud Run service account IAM information is added to the Cloud Storage bucket.
  * The `roles/storage.objectAdmin` role is assigned to the Cloud Run service account.

| [Connect to Google Cloud services](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services)  
[Global Cloud Load Balancing backend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-backend) | 

  * The load balancer can distribute incoming traffic to the Cloud Run service.
  * The Cloud Run service is added as a backend endpoint in the Cloud Load Balancing serverless NEG backends configuration.

| [Set up a global external Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless)  
[Memorystore for Redis](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis) | 

  * The Cloud Run service can cache data in the Memorystore for Redis instance.
  * The Memorystore for Redis connection information is added to the Cloud Run environment variables.
  * The `roles/redis.editor` role is added to the Cloud Run service account.

| [Connecting to a Redis instance from a Cloud Run service](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run)  
[Memorystore for Redis Cluster](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis-cluster) | 

  * The Cloud Run service can cache data in the Memorystore for Redis Cluster.
  * The Memorystore for Redis Cluster connection information is added to the Cloud Run environment variables.
  * App Design Center adds the `roles/redis.dbConnectionUser` role to the Cloud Run service account.

| [Connect to a Memorystore for Redis Cluster instance](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance)  
[Memorystore for Valkey](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-valkey) | 

  * The Cloud Run service can cache data in the Memorystore for Valkey instance.
  * App Design Center adds the Memorystore for Valkey connection information to the Cloud Run environment variables.
  * App Design Center adds the `roles/memorystore.dbConnectionUser` role to the Cloud Run service account.

| [Connect to a Memorystore for Valkey instance](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance)  
[Pub/Sub](https://docs.cloud.google.com/application-design-center/docs/configure-pubsub) | 

  * The Cloud Run service can receive messages or publish to the Pub/Sub topic.
  * The Pub/Sub topic ID is added to the Cloud Run environment variables.
  * The `roles/pubsub.publisher` and `roles/pubsub.subscriber` roles are added to the Cloud Run service account.
  * The Cloud Run service is added to the Pub/Sub push and pull subscription fields.

| [Use Pub/Sub with Cloud Run tutorial](https://docs.cloud.google.com/run/docs/tutorials/pubsub)  
[Regional Cloud Load Balancing backend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-backend) | 

  * The load balancer can distribute incoming traffic to the Cloud Run service.
  * The Cloud Run service is added as a backend endpoint in the Cloud Load Balancing serverless NEG backends configuration.

| [Set up a regional external Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless)  
[Regional Cloud Load Balancing frontend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-frontend) | 

  * The HTTP and HTTPS IP addresses of the load balancer are available to the application running in the Cloud Run container.
  * The Cloud Load Balancing address metadata is added to the Cloud Run environment variables.

| [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
[Spanner](https://docs.cloud.google.com/application-design-center/docs/configure-spanner) | 

  * The Cloud Run service can manage the Spanner instance.
  * The Spanner connection details are added to the Cloud Run environment variables.
  * The `roles/spanner.databaseAdmin` role is added to the Cloud Run service account.
  * The Cloud Run service account IAM information is added to the Spanner instance.

| [Connect to Google Cloud services](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services)  
[Vertex AI](https://docs.cloud.google.com/application-design-center/docs/configure-vertex-ai) | 

  * The Cloud Run service can interact with Vertex AI services.
  * The `roles/aiplatform.user` role is added to the Cloud Run service account.

| [Host AI apps and agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents)  
  
## Required configuration parameters

If your template includes a Cloud Run component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Cloud Run resource. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Region** | The Cloud Run service deployment location. | [Cloud Run locations](https://docs.cloud.google.com/run/docs/locations)  
**Service Name** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#Service.FIELDS.name) | [Cloud Run service](https://docs.cloud.google.com/run/docs/resource-model#services)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Subfeature | Parameter name | Description and constraint information | Background information  
---|---|---|---|---  
Containers |  | **Container Name** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#FIELDS.name) | [Building containers](https://docs.cloud.google.com/run/docs/building/containers)  
| **Container Image** | [image](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#FIELDS.image) | [Deploying container images to Cloud Run](https://docs.cloud.google.com/run/docs/deploying)  
| **Working Dir** | The container's working directory. If not specified, the container runtime's default is used, which might be configured in the container image. | [workingDir](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#FIELDS.workingDir)  
| **Depends on Container** | [dependsOn[]](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#FIELDS.depends_on) | [Configure container start order for sidecar deployments](https://docs.cloud.google.com/run/docs/configuring/services/containers#container-ordering)  
| **Container Args** | [args[]](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#FIELDS.args) | [Configure containers for services](https://docs.cloud.google.com/run/docs/configuring/services/containers)  
| **Container Command** | [command](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#FIELDS.command) | [Configure containers for services](https://docs.cloud.google.com/run/docs/configuring/services/containers)  
Env Vars | **Key** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#EnvVar.FIELDS.name) | [Environment variables for services](https://docs.cloud.google.com/run/docs/configuring/services/overview-environment-variables)  
**Value** | [value](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#EnvVar.FIELDS.value) | [Environment variables for services](https://docs.cloud.google.com/run/docs/configuring/services/overview-environment-variables)  
Env Secret Vars | **Key** | [EnvVarSource](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#envvarsource) | [Manage secrets](https://docs.cloud.google.com/run/docs/configuring/services/overview-environment-variables#manage_secrets)  
**Secret** | [secret](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#SecretKeySelector.FIELDS.secret) | [Manage secrets](https://docs.cloud.google.com/run/docs/configuring/services/overview-environment-variables#manage_secrets)  
**Version** | [version](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#SecretKeySelector.FIELDS.version) | [Manage secrets](https://docs.cloud.google.com/run/docs/configuring/services/overview-environment-variables#manage_secrets)  
Volume Mounts | **Name** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#VolumeMount.FIELDS.name) | [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)  
**Mount Path** | [mountPath](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#VolumeMount.FIELDS.mount_path) | [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)  
Ports | **Name** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#ContainerPort.FIELDS.name) | [Use HTTP/2 for services](https://docs.cloud.google.com/run/docs/configuring/http2#terraform)  
**Container Port** | [containerPort](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#ContainerPort.FIELDS.container_port) | [Use HTTP/2 for services](https://docs.cloud.google.com/run/docs/configuring/http2#terraform)  
Resources | **CPU** | [limits](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#ResourceRequirements.FIELDS.limits) | [Configure CPU limits for services](https://docs.cloud.google.com/run/docs/configuring/cpu)  
**Memory** | [limits](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#ResourceRequirements.FIELDS.limits) | [Configure memory limits for services](https://docs.cloud.google.com/run/docs/configuring/memory-limits)  
**CPU Idle** | Whether CPU is only allocated during requests. | [cpuIdle](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#ResourceRequirements.FIELDS.cpu_idle)  
**Startup CPU Boost** | [startupCPUBoost](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#ResourceRequirements.FIELDS.startup_cpu_boost) | [Set startup CPU boost](https://docs.cloud.google.com/run/docs/configuring/services/cpu#startup-boost)  
Startup Probe | **Failure Threshold** | [failureThreshold](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#Probe.FIELDS.failure_threshold) | [Configure container health checks for services](https://docs.cloud.google.com/run/docs/configuring/healthchecks)  
**Initial Delay Seconds** | [initialDelaySeconds](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#Probe.FIELDS.initial_delay_seconds) | [Configure probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#configure-probes)  
**Timeout Seconds** | [timeoutSeconds](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#Probe.FIELDS.timeout_seconds) | [Configure probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#configure-probes)  
**Period Seconds** | [periodSeconds](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#Probe.FIELDS.period_seconds) | [Configure probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#configure-probes)  
**HTTP Get Path** | [path](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#HTTPGetAction.FIELDS.path) | [Configure probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#configure-probes)  
**HTTP Get Port** | [port](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#HTTPGetAction.FIELDS.port) | [Configure probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#configure-probes)  
**HTTP Headers Name** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#HTTPHeader.FIELDS.name) | [Configure probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#configure-probes)  
**HTTP Headers Value** | [value](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#HTTPHeader.FIELDS.value) | [Configure probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#configure-probes)  
**TCP Socket Port** | [port](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#TCPSocketAction.FIELDS.port) | [The default TCP startup probe](https://docs.cloud.google.com/run/docs/configuring/healthchecks#tcp-startup-probe)  
**GRPC Port** | [port](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#GRPCAction.FIELDS.port) | [Configure probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#configure-probes)  
**GRPC Service** | [service](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#GRPCAction.FIELDS.service) | [Configure probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#configure-probes)  
| **Liveness Probe** | [livenessProbe](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#FIELDS.liveness_probe) | [Use cases](https://docs.cloud.google.com/run/docs/configuring/healthchecks#use_cases)  
|  | **Description** | [description](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#Service.FIELDS.description) | [Set service descriptions](https://docs.cloud.google.com/run/docs/configuring/description)  
|  | **Create Service Account** | Create a new service account for the Cloud Run service. | [Configure service identity for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity)  
|  | **Service Account Project Roles** | Roles to grant to the newly created service account. Enable **Create Service Account** and don't provide input for **Service Account**. | [Configure service identity for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity)  
|  | **Ingress** | [IngressTraffic](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#Service.FIELDS.ingress) | [Restrict network ingress for Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress)  
|  | **Members** | Users and service accounts that can invoke the service. For public access, enter `allUsers`. For access by logged-in Google users, enter `allAuthenticatedUsers`, or enter a list of specific users and service accounts. For more information, see [members](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service_iam#member/members-1). | [Configure service identity for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity)  
VPC Access |  | **Connector** | [connector](https://docs.cloud.google.com/run/docs/reference/rest/v2/VpcAccess#FIELDS.connector) | [VPC with connectors](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors)  
| **Egress** | [egress](https://docs.cloud.google.com/run/docs/reference/rest/v2/VpcAccess#FIELDS.egress) | [Control egress service traffic](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#egress-service)  
Network Interfaces | **Network** | [network](https://docs.cloud.google.com/run/docs/reference/rest/v2/VpcAccess#NetworkInterface.FIELDS.network) | [Deploy a service](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-service)  
**Subnetwork** | [subnetwork](https://docs.cloud.google.com/run/docs/reference/rest/v2/VpcAccess#NetworkInterface.FIELDS.subnetwork) | [Deploy a service](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-service)  
**Tags** | [tags](https://docs.cloud.google.com/run/docs/reference/rest/v2/VpcAccess#NetworkInterface.FIELDS.tags) | [Deploy a service](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-service)  
|  | **Cloud Run Deletion Protection** | Prevents Terraform from destroying or recreating Cloud Run jobs and services. | [deletion_protection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service#deletion_protection-1)  
|  | **Enable Prometheus Sidecar** | Enable Prometheus sidecar in the Cloud Run instance. | [Write Prometheus metrics by using the Prometheus sidecar](https://docs.cloud.google.com/run/docs/monitoring-managed-prometheus-sidecar#add-sidecar)  
Volumes |  | **Name** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#FIELDS.name) | [Configure an in-memory volume](https://docs.cloud.google.com/run/docs/configuring/services/in-memory-volume-mounts#configure-volume)  
Secret | **Secret** | [secret](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#FIELDS.secret) | [Make a secret accessible to Cloud Run](https://docs.cloud.google.com/run/docs/configuring/services/secrets#access-secrets)  
**Default Mode** | [defaultMode](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#SecretVolumeSource.FIELDS.default_mode) | [](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run/)  
**Path** | [path](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#VersionToPath.FIELDS.path) | [Make a secret available to Cloud Run](https://docs.cloud.google.com/run/docs/configuring/services/secrets#access-secrets)  
**Version** | [version](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#VersionToPath.FIELDS.version) | [Make a secret available to Cloud Run](https://docs.cloud.google.com/run/docs/configuring/services/secrets#access-secrets)  
**Mode** | [mode](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#VersionToPath.FIELDS.mode) | [Make a secret available to Cloud Run](https://docs.cloud.google.com/run/docs/configuring/services/secrets#access-secrets)  
Cloud SQL Instance | **Instances** | [instances[]](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#cloudsqlinstance) | [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run#terraform)  
Empty Dir | **Medium** | [medium](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#EmptyDirVolumeSource.FIELDS.medium) | [Configure in-memory volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/services/in-memory-volume-mounts)  
**Size Limit** | [sizeLimit](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#EmptyDirVolumeSource.FIELDS.size_limit) | [Configure in-memory volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/services/in-memory-volume-mounts)  
GCS | **Bucket** | [bucket](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#GCSVolumeSource.FIELDS.bucket) | [Configure Cloud Storage volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts)  
**Read Only** | [readOnly](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#GCSVolumeSource.FIELDS.read_only) | [Configure Cloud Storage volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts)  
NFS | **Server** | [server](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#NFSVolumeSource.FIELDS.server) | [Configure NFS volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/services/nfs-volume-mounts)  
**Path** | [path](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#NFSVolumeSource.FIELDS.path) | [Configure NFS volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/services/nfs-volume-mounts)  
**Read Only** | [readOnly](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#NFSVolumeSource.FIELDS.read_only) | [Configure NFS volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/services/nfs-volume-mounts)  
Service Scaling |  | **Min Instance Count** | [minInstanceCount](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#ServiceScaling.FIELDS.min_instance_count) | [Set minimum instances for services](https://docs.cloud.google.com/run/docs/configuring/min-instances)  
|  | **Revision** | [revision](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#RevisionTemplate.FIELDS.revision) | [Cloud Run service revisions](https://docs.cloud.google.com/run/docs/resource-model#revisions)  
Template Scaling |  | **Min Instance Count** | [minInstanceCount](https://docs.cloud.google.com/run/docs/reference/rest/v2/RevisionScaling#FIELDS.min_instance_count) | [Set minimum instances for services](https://docs.cloud.google.com/run/docs/configuring/min-instances)  
| **Max Instance Count** | [maxInstanceCount](https://docs.cloud.google.com/run/docs/reference/rest/v2/RevisionScaling#FIELDS.max_instance_count) | [About maximum instances](https://docs.cloud.google.com/run/docs/configuring/max-instances-limits)  
|  | **Encryption Key** | [encryptionKey](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#RevisionTemplate.FIELDS.encryption_key) | [Using customer managed encryption keys](https://docs.cloud.google.com/run/docs/securing/using-cmek)  
|  | **Max Instance Request Concurrency** | [maxInstanceRequestConcurrency](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#ServiceScaling.FIELDS.max_instance_request_concurrency) | [Maximum concurrent requests for services](https://docs.cloud.google.com/run/docs/about-concurrency)  
|  | **Session Affinity** | [sessionAffinity](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#RevisionTemplate.FIELDS.session_affinity) | [Set session affinity for services](https://docs.cloud.google.com/run/docs/configuring/session-affinity)  
|  | **Execution Environment** | [executionEnvironment](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#RevisionTemplate.FIELDS.execution_environment) | [About service execution environments ](https://docs.cloud.google.com/run/docs/about-execution-environments)  
Traffic |  | **Type** | [type](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#TrafficTarget.FIELDS.type) | [Rollbacks, gradual rollouts, and traffic migration](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#terraform)  
| **Percent** | [percent](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#TrafficTarget.FIELDS.percent) | [Rollbacks, gradual rollouts, and traffic migration](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#terraform)  
| **Revision** | [revision](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#TrafficTarget.FIELDS.revision) | [Rollbacks, gradual rollouts, and traffic migration](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#terraform)  
| **Tag** | [tag](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#TrafficTarget.FIELDS.tag) | [Rollbacks, gradual rollouts, and traffic migration](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#terraform)  
Service Labels |  | **Key** | [labels](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#Service.FIELDS.labels) | [Configure labels for services](https://docs.cloud.google.com/run/docs/configuring/labels)  
| **Value** | [labels](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#Service.FIELDS.labels) | [Configure labels for services](https://docs.cloud.google.com/run/docs/configuring/labels)  
Service Annotations |  | **Key** | [annotations](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#Service.FIELDS.annotations) | [annotations](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service#annotations-2)  
| **Value** | [annotations](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#Service.FIELDS.annotations) | [annotations](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service#annotations-2)  
Client |  | **Name** | Arbitrary identifier for the API client. | [client](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services)  
| **Version** | Arbitrary identifier for the version identifier. | [clientVersion](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services)  
|  | **Launch Stage** | [LaunchStage](https://docs.cloud.google.com/run/docs/reference/rest/v2/LaunchStage) | [Product launch stages](https://cloud.google.com/products#product-launch-stages)  
|  | **Custom Audiences** | [customAudience](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#Service.FIELDS.custom_audiences) | [Set custom audiences for services](https://docs.cloud.google.com/run/docs/configuring/custom-audiences)  
Binary Authorization |  | **Breakglass Justification** | [breakglassJustification](https://docs.cloud.google.com/run/docs/reference/rest/v2/BinaryAuthorization#FIELDS.breakglass_justification) | [Use breakglass](https://docs.cloud.google.com/binary-authorization/docs/using-breakglass)  
| **Use Default** | [useDefault](https://docs.cloud.google.com/run/docs/reference/rest/v2/BinaryAuthorization#BinaryAuthorization.Fields.use_default) | [Use Binary Authorization](https://docs.cloud.google.com/run/docs/securing/binary-authorization)  
Template Labels |  | **Key** | [labels](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#RevisionTemplate.FIELDS.labels) | [Configuring labels for services](https://docs.cloud.google.com/run/docs/configuring/labels)  
| **Value** | [labels](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#RevisionTemplate.FIELDS.labels) | [Configuring labels for services](https://docs.cloud.google.com/run/docs/configuring/labels)  
Template Annotations |  | **Key** | [annotations](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#RevisionTemplate.FIELDS.annotations) | [annotations](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service#annotations)  
| **Value** | [annotations](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#RevisionTemplate.FIELDS.annotations) | [annotations](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service#annotations)  
|  | **Timeout** | [timeout](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#RevisionTemplate.FIELDS.timeout) | [Set request timeout for services](https://docs.cloud.google.com/run/docs/configuring/request-timeout)  
|  | **Service Account** | [serviceAccount](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#RevisionTemplate.FIELDS.service_account) | [Configure service identity for services](https://docs.cloud.google.com/run/docs/configuring/services/service-identity)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
