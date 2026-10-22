---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/iam-serverless/
title: Managed Service for Apache Spark serverless permissions and roles \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:44.709638+00:00
---

# Managed Service for Apache Spark serverless permissions and roles  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/iam-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark serverless permissions and roles Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) lets you control access to your project's resources. This document focuses on the IAM permissions relevant to Managed Service for Apache Spark serverless deployments and the IAM roles that grant those permissions.

## Managed Service for Apache Spark serverless permissions

Managed Service for Apache Spark permissions allow users and [service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts), to perform actions on Managed Service for Apache Spark resources. For example, the `dataproc.batches.create` permission lets you create batch workloads in a project.

You don't directly give users permissions; instead, you grant them IAM roles, which have one or more permissions bundled within them. You can grant [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined) that contain a list of permissions, or you can create and grant [custom roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom) that contain one or more permissions that you include in the custom role.

The following tables list the basic permissions necessary to call Dataproc APIs (methods) that create or access Managed Service for Apache Spark resources. The tables are organized according to the APIs associated with each Managed Service for Apache Spark resource, which include `batches`, `sessions`, `sessionTemplates`, and `operations`.

Examples:

  * `dataproc.batches.create` allows the creation of batches in the containing project.
  * `dataproc.sessions.create` allows the creation of interactive sessions in the containing project.

**Note:** For a complete listing of Managed Service for Apache Spark permissions and roles, see Lookup Managed Service for Apache Spark roles and permissions.

### Batch permissions

Method | Required Permission(s)  
---|---  
projects.locations.batches.create | dataproc.batches.create 1  
projects.locations.batches.delete | dataproc.batches.delete  
projects.locations.batches.get | dataproc.batches.get  
projects.locations.batches.list | dataproc.batches.list  
  
1`dataproc.batches.create` also requires `dataproc.batches.get` and `dataproc.operations.get` permissions to allow it to get status updates from the `gcloud` command-line tool.

### Session permissions

Method | Required Permission(s)  
---|---  
projects.locations.sessions.create | dataproc.sessions.create 1  
projects.locations.sessions.delete | dataproc.sessions.delete  
projects.locations.sessions.get | dataproc.sessions.get  
projects.locations.sessions.list | dataproc.sessions.list  
projects.locations.sessions.terminate | dataproc.sessions.terminate  
  
1`dataproc.sessions.create` also requires `dataproc.sessions.get` and `dataproc.operations.get` permissions to allow it to get status updates from the `gcloud` command-line tool.

### Session template permissions

Method | Required Permission(s)  
---|---  
projects.locations.sessionTemplates.create | dataproc.sessionTemplates.create 1  
projects.locations.sessionTemplates.delete | dataproc.sessionTemplates.delete  
projects.locations.sessionTemplates.get | dataproc.sessionTemplates.get  
projects.locations.sessionTemplates.list | dataproc.sessionTemplates.list  
projects.locations.sessionTemplates.update | dataproc.sessionTemplates.update  
  
1`dataproc.sessionTemplates.create` also requires `dataproc.sessionTemplates.get` and `dataproc.operations.get` permissions to allow it to get status updates from the `gcloud` command-line tool.

### Operations permissions

Method | Required Permission(s)  
---|---  
projects.regions.operations.get | dataproc.operations.get  
projects.regions.operations.list | dataproc.operations.list  
projects.regions.operations.cancel 1 | dataproc.operations.cancel  
projects.regions.operations.delete | dataproc.operations.delete  
projects.regions.operations.getIamPolicy | dataproc.operations.getIamPolicy  
projects.regions.operations.setIamPolicy | dataproc.operations.setIamPolicy  
  
1 To cancel batch operations, `dataproc.operations.cancel` also requires `dataproc.batches.cancel` permission.

### Managed Service for Apache Spark 3.0+ runtime permissions

The following permissions apply to Managed Service for Apache Spark `3.0` and later runtimes.

#### Workloads permissions

Method | Required Permission(s)  
---|---  
dataprocrm.v1.dataprocrm.projects.locations.workloads.create | dataprocrm.workloads.create  
dataprocrm.v1.dataprocrm.projects.locations.workloads.cancel | dataprocrm.workloads.cancel  
dataprocrm.v1.dataprocrm.projects.locations.workloads.delete | dataprocrm.workloads.delete  
dataprocrm.v1.dataprocrm.projects.locations.workloads.get | dataprocrm.workloads.get  
dataprocrm.v1.dataprocrm.projects.locations.workloads.list | dataprocrm.workloads.list  
dataprocrm.v1.dataprocrm.projects.locations.workloads.use | dataprocrm.workloads.use  
  
#### NodePools permissions

Method | Required Permission(s)  
---|---  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.create | dataprocrm.nodePools.create  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.delete | dataprocrm.nodePools.delete  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.resize | dataprocrm.nodePools.resize  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.deleteNodes | dataprocrm.nodePools.deleteNodes  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.update | dataprocrm.nodePools.update  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.get | dataprocrm.nodePools.get  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.list | dataprocrm.nodePools.list  
  
#### Nodes permissions

Method | Required Permission(s)  
---|---  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.nodes.create | dataprocrm.nodes.create  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.nodes.delete | dataprocrm.nodes.delete  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.nodes.update | dataprocrm.nodes.update  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.nodes.heartbeat | dataprocrm.nodes.heartbeat  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.nodes.get | dataprocrm.nodes.get  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.nodes.list | dataprocrm.nodes.list  
dataprocrm.v1.dataprocrm.projects.locations.workloads.nodePools.nodes.mintOAuthToken | dataprocrm.nodes.mintOAuthToken  
  
#### Operations permissions

Method | Required Permission(s)  
---|---  
dataprocrm.v1.dataprocrm.projects.locations.operations.get | dataprocrm.operations.get  
dataprocrm.v1.dataprocrm.projects.locations.operations.list | dataprocrm.operations.list  
  
## Managed Service for Apache Spark serverless deployments roles

The following table lists roles that contain the permissions required to manage batch workloads and sessions. The requirements can vary depending on the batch or session [runtime version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions) and whether the batch or session is running with service account or end-user credentials (EUC).

Runtime version | IAM roles  
---|---  
pre-`3.0` | Grant users the following roles:  


  * **Dataproc Editor** role to run batches or sessions or the **Dataproc Viewer** role to get and list batches and sessions.
  * **Service Account User** role on the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or a custom service account.

Grant the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or a custom service account the **Dataproc Worker** role.  
`3.0`+ | Grant users the following roles:  


  * **Dataproc Serverless Editor** role to submit batches and sessions or the **Dataproc Serverless Viewer** role to get and list batches and sessions.
  * If you select _Service Account credentials_ instead of accepting the default `3.0`\+ runtime _End User Credentials_ (EUC), grant users the **Service Account User** role on a user-specified custom service account, and grant the user-specified custom service account the **Dataproc Serverless Node** role and **Dataproc Resource Manager Node Service Agent** role.

.  
  
Notes:

  * When submitting a batch workload or creating an interactive session with the a `3.0+` runtime and end user credentials (the 3.0+ default), dataplane system operations are executed by the Dataproc Resource Manager Node Service Agent. For more information, see [3.0+ runtime service agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account#3.0-service-agent).

  * For backward compatibility, the legacy **Dataproc Editor** and **Dataproc Viewer** roles can be granted with `3.0+` runtimes instead of the **Dataproc Serverless Editor** and **Dataproc Serverless Viewer** roles. Also, the **Dataproc Worker** role can be granted instead of the **Dataproc Serverless Node** role.

  * If a service account has been granted the project **Editor** role, it contains the permissions included in the **Dataproc Worker** role.

  * For more information: see [Serverless for Apache Spark service accounts](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account).




### Do you need to grant roles?

Depending on your organization policy, a required role may already have been granted.

#### Check roles granted to users

To see if a user has been granted a role, follow the instructions in [Manage access to projects, folders, and organizations > View current access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#view-access).

#### Check roles granted to service accounts

To see if the a service account has been granted a role, see [View and manage IAM service account roles](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account#view-and-manage-iam-service-account-roles).

**Note:** In some projects, the batch workload or session service account may have been automatically granted the project **Editor** role, which includes the **Dataproc Worker** role permissions plus additional permissions not specifically needed by Managed Service for Apache Spark for routine operations. To follow the security best practice principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege), replace the service account **Editor** role with the **Managed Service for Apache Spark Worker** or, for runtime version `3.0+`, the **Dataproc Serverless Node** role.

#### Check roles granted on a service account

To see if a user has been granted a role on a service account, follow the instructions in [Manage access to service accounts > View current access](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#view-access).

## Lookup roles and permissions

You can use the following sections to lookup Managed Service for Apache Spark roles and permissions.

Role | Permissions  
---|---  
  
#### Dataproc Administrator 

(`roles/dataproc.admin`) Full control of Dataproc resources.  |  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.networks.get` `compute.networks.list` `compute.projects.get` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dataproc.agents.*`

  * `dataproc.agents.create`
  * `dataproc.agents.delete`
  * `dataproc.agents.get`
  * `dataproc.agents.list`
  * `dataproc.agents.update`

`dataproc.autoscalingPolicies.*`

  * `dataproc.autoscalingPolicies.create`
  * `dataproc.autoscalingPolicies.delete`
  * `dataproc.autoscalingPolicies.get`
  * `dataproc.autoscalingPolicies.getIamPolicy`
  * `dataproc.autoscalingPolicies.list`
  * `dataproc.autoscalingPolicies.setIamPolicy`
  * `dataproc.autoscalingPolicies.update`
  * `dataproc.autoscalingPolicies.use`

`dataproc.batches.analyze` `dataproc.batches.cancel` `dataproc.batches.create` `dataproc.batches.delete` `dataproc.batches.get` `dataproc.batches.list` `dataproc.batches.sparkApplicationRead` `dataproc.batches.sparkApplicationWrite` `dataproc.clusters.*`

  * `dataproc.clusters.create`
  * `dataproc.clusters.delete`
  * `dataproc.clusters.get`
  * `dataproc.clusters.getIamPolicy`
  * `dataproc.clusters.list`
  * `dataproc.clusters.repair`
  * `dataproc.clusters.setIamPolicy`
  * `dataproc.clusters.start`
  * `dataproc.clusters.stop`
  * `dataproc.clusters.update`
  * `dataproc.clusters.use`

`dataproc.jobs.*`

  * `dataproc.jobs.cancel`
  * `dataproc.jobs.create`
  * `dataproc.jobs.delete`
  * `dataproc.jobs.get`
  * `dataproc.jobs.getIamPolicy`
  * `dataproc.jobs.list`
  * `dataproc.jobs.setIamPolicy`
  * `dataproc.jobs.update`

`dataproc.nodeGroups.*`

  * `dataproc.nodeGroups.create`
  * `dataproc.nodeGroups.get`
  * `dataproc.nodeGroups.update`

`dataproc.operations.*`

  * `dataproc.operations.cancel`
  * `dataproc.operations.delete`
  * `dataproc.operations.get`
  * `dataproc.operations.getIamPolicy`
  * `dataproc.operations.list`
  * `dataproc.operations.setIamPolicy`

`dataproc.sessionTemplates.*`

  * `dataproc.sessionTemplates.create`
  * `dataproc.sessionTemplates.delete`
  * `dataproc.sessionTemplates.get`
  * `dataproc.sessionTemplates.list`
  * `dataproc.sessionTemplates.update`

`dataproc.sessions.*`

  * `dataproc.sessions.create`
  * `dataproc.sessions.delete`
  * `dataproc.sessions.get`
  * `dataproc.sessions.list`
  * `dataproc.sessions.sparkApplicationRead`
  * `dataproc.sessions.sparkApplicationWrite`
  * `dataproc.sessions.terminate`

`dataproc.tasks.*`

  * `dataproc.tasks.lease`
  * `dataproc.tasks.listInvalidatedLeases`
  * `dataproc.tasks.reportStatus`

`dataproc.workflowTemplates.*`

  * `dataproc.workflowTemplates.create`
  * `dataproc.workflowTemplates.delete`
  * `dataproc.workflowTemplates.get`
  * `dataproc.workflowTemplates.getIamPolicy`
  * `dataproc.workflowTemplates.instantiate`
  * `dataproc.workflowTemplates.instantiateInline`
  * `dataproc.workflowTemplates.list`
  * `dataproc.workflowTemplates.setIamPolicy`
  * `dataproc.workflowTemplates.update`

`dataprocrm.nodePools.*`

  * `dataprocrm.nodePools.create`
  * `dataprocrm.nodePools.delete`
  * `dataprocrm.nodePools.deleteNodes`
  * `dataprocrm.nodePools.get`
  * `dataprocrm.nodePools.list`
  * `dataprocrm.nodePools.resize`

`dataprocrm.nodes.get` `dataprocrm.nodes.heartbeat` `dataprocrm.nodes.list` `dataprocrm.nodes.update` `dataprocrm.operations.get` `dataprocrm.operations.list` `dataprocrm.workloads.*`

  * `dataprocrm.workloads.cancel`
  * `dataprocrm.workloads.create`
  * `dataprocrm.workloads.delete`
  * `dataprocrm.workloads.get`
  * `dataprocrm.workloads.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataproc Editor 

(`roles/dataproc.editor`) Provides the permissions necessary for viewing the resources required to manage Managed Service for Apache Spark, including machine types, networks, projects, and zones.  Lowest-level resources where you can grant this role:

  * Cluster 

|  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.networks.get` `compute.networks.list` `compute.projects.get` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dataproc.agents.*`

  * `dataproc.agents.create`
  * `dataproc.agents.delete`
  * `dataproc.agents.get`
  * `dataproc.agents.list`
  * `dataproc.agents.update`

`dataproc.autoscalingPolicies.create` `dataproc.autoscalingPolicies.delete` `dataproc.autoscalingPolicies.get` `dataproc.autoscalingPolicies.getIamPolicy` `dataproc.autoscalingPolicies.list` `dataproc.autoscalingPolicies.update` `dataproc.autoscalingPolicies.use` `dataproc.batches.analyze` `dataproc.batches.cancel` `dataproc.batches.create` `dataproc.batches.delete` `dataproc.batches.get` `dataproc.batches.list` `dataproc.batches.sparkApplicationRead` `dataproc.batches.sparkApplicationWrite` `dataproc.clusters.create` `dataproc.clusters.delete` `dataproc.clusters.get` `dataproc.clusters.getIamPolicy` `dataproc.clusters.list` `dataproc.clusters.repair` `dataproc.clusters.start` `dataproc.clusters.stop` `dataproc.clusters.update` `dataproc.clusters.use` `dataproc.jobs.cancel` `dataproc.jobs.create` `dataproc.jobs.delete` `dataproc.jobs.get` `dataproc.jobs.getIamPolicy` `dataproc.jobs.list` `dataproc.jobs.update` `dataproc.nodeGroups.*`

  * `dataproc.nodeGroups.create`
  * `dataproc.nodeGroups.get`
  * `dataproc.nodeGroups.update`

`dataproc.operations.cancel` `dataproc.operations.delete` `dataproc.operations.get` `dataproc.operations.getIamPolicy` `dataproc.operations.list` `dataproc.sessionTemplates.*`

  * `dataproc.sessionTemplates.create`
  * `dataproc.sessionTemplates.delete`
  * `dataproc.sessionTemplates.get`
  * `dataproc.sessionTemplates.list`
  * `dataproc.sessionTemplates.update`

`dataproc.sessions.*`

  * `dataproc.sessions.create`
  * `dataproc.sessions.delete`
  * `dataproc.sessions.get`
  * `dataproc.sessions.list`
  * `dataproc.sessions.sparkApplicationRead`
  * `dataproc.sessions.sparkApplicationWrite`
  * `dataproc.sessions.terminate`

`dataproc.tasks.*`

  * `dataproc.tasks.lease`
  * `dataproc.tasks.listInvalidatedLeases`
  * `dataproc.tasks.reportStatus`

`dataproc.workflowTemplates.create` `dataproc.workflowTemplates.delete` `dataproc.workflowTemplates.get` `dataproc.workflowTemplates.getIamPolicy` `dataproc.workflowTemplates.instantiate` `dataproc.workflowTemplates.instantiateInline` `dataproc.workflowTemplates.list` `dataproc.workflowTemplates.update` `dataprocrm.nodePools.*`

  * `dataprocrm.nodePools.create`
  * `dataprocrm.nodePools.delete`
  * `dataprocrm.nodePools.deleteNodes`
  * `dataprocrm.nodePools.get`
  * `dataprocrm.nodePools.list`
  * `dataprocrm.nodePools.resize`

`dataprocrm.nodes.get` `dataprocrm.nodes.heartbeat` `dataprocrm.nodes.list` `dataprocrm.nodes.update` `dataprocrm.operations.get` `dataprocrm.operations.list` `dataprocrm.workloads.*`

  * `dataprocrm.workloads.cancel`
  * `dataprocrm.workloads.create`
  * `dataprocrm.workloads.delete`
  * `dataprocrm.workloads.get`
  * `dataprocrm.workloads.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataproc Viewer 

(`roles/dataproc.viewer`) Provides read-only access to Managed Service for Apache Spark resources.  Lowest-level resources where you can grant this role:

  * Cluster 

|  `compute.machineTypes.get` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dataproc.agents.get` `dataproc.agents.list` `dataproc.autoscalingPolicies.get` `dataproc.autoscalingPolicies.getIamPolicy` `dataproc.autoscalingPolicies.list` `dataproc.autoscalingPolicies.use` `dataproc.batches.analyze` `dataproc.batches.get` `dataproc.batches.list` `dataproc.batches.sparkApplicationRead` `dataproc.clusters.get` `dataproc.clusters.getIamPolicy` `dataproc.clusters.list` `dataproc.jobs.get` `dataproc.jobs.getIamPolicy` `dataproc.jobs.list` `dataproc.nodeGroups.get` `dataproc.operations.get` `dataproc.operations.getIamPolicy` `dataproc.operations.list` `dataproc.sessionTemplates.get` `dataproc.sessionTemplates.list` `dataproc.sessions.get` `dataproc.sessions.list` `dataproc.sessions.sparkApplicationRead` `dataproc.tasks.listInvalidatedLeases` `dataproc.workflowTemplates.get` `dataproc.workflowTemplates.getIamPolicy` `dataproc.workflowTemplates.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataproc Hub Agent 

(`roles/dataproc.hubAgent`) Allows management of Dataproc resources. Intended for service accounts running Dataproc Hub instances.  |  `compute.instances.get` `compute.instances.setMetadata` `compute.instances.setTags` `compute.zoneOperations.get` `compute.zones.list` `dataproc.autoscalingPolicies.get` `dataproc.autoscalingPolicies.list` `dataproc.autoscalingPolicies.use` `dataproc.clusters.create` `dataproc.clusters.delete` `dataproc.clusters.get` `dataproc.clusters.list` `dataproc.clusters.repair` `dataproc.clusters.update` `dataproc.operations.cancel` `dataproc.operations.delete` `dataproc.operations.get` `dataproc.operations.list` `iam.serviceAccounts.actAs` `iam.serviceAccounts.get` `iam.serviceAccounts.list` `logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.exclusions.get` `logging.exclusions.list` `logging.links.get` `logging.links.list` `logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logEntries.create` `logging.logEntries.list` `logging.logEntries.route` `logging.logMetrics.get` `logging.logMetrics.list` `logging.logScopes.get` `logging.logScopes.list` `logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.notificationRules.get` `logging.notificationRules.list` `logging.operations.get` `logging.operations.list` `logging.queries.getShared` `logging.queries.listShared` `logging.queries.usePrivate` `logging.settings.get` `logging.sinks.get` `logging.sinks.list` `logging.usage.get` `logging.views.get` `logging.views.getIamPolicy` `logging.views.list` `observability.scopes.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.buckets.get` `storage.objects.get` `storage.objects.list`  
  
#### Dataproc Serverless Editor 

(`roles/dataproc.serverlessEditor`) Permissions needed to run serverless sessions and batches as a user  |  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `compute.projects.get` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dataproc.batches.analyze` `dataproc.batches.cancel` `dataproc.batches.create` `dataproc.batches.delete` `dataproc.batches.get` `dataproc.batches.list` `dataproc.batches.sparkApplicationRead` `dataproc.batches.sparkApplicationWrite` `dataproc.operations.cancel` `dataproc.operations.delete` `dataproc.operations.get` `dataproc.operations.list` `dataproc.sessionTemplates.*`

  * `dataproc.sessionTemplates.create`
  * `dataproc.sessionTemplates.delete`
  * `dataproc.sessionTemplates.get`
  * `dataproc.sessionTemplates.list`
  * `dataproc.sessionTemplates.update`

`dataproc.sessions.*`

  * `dataproc.sessions.create`
  * `dataproc.sessions.delete`
  * `dataproc.sessions.get`
  * `dataproc.sessions.list`
  * `dataproc.sessions.sparkApplicationRead`
  * `dataproc.sessions.sparkApplicationWrite`
  * `dataproc.sessions.terminate`

`dataprocrm.nodePools.*`

  * `dataprocrm.nodePools.create`
  * `dataprocrm.nodePools.delete`
  * `dataprocrm.nodePools.deleteNodes`
  * `dataprocrm.nodePools.get`
  * `dataprocrm.nodePools.list`
  * `dataprocrm.nodePools.resize`

`dataprocrm.nodes.get` `dataprocrm.nodes.heartbeat` `dataprocrm.nodes.list` `dataprocrm.nodes.update` `dataprocrm.operations.get` `dataprocrm.operations.list` `dataprocrm.workloads.*`

  * `dataprocrm.workloads.cancel`
  * `dataprocrm.workloads.create`
  * `dataprocrm.workloads.delete`
  * `dataprocrm.workloads.get`
  * `dataprocrm.workloads.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataproc Serverless Node. 

(`roles/dataproc.serverlessNode`) Node access to Dataproc Serverless sessions and batches. Intended for service accounts.  |  `dataproc.batches.computeTuningConfig` `dataproc.batches.sparkApplicationWrite` `dataproc.sessions.sparkApplicationRead` `dataproc.sessions.sparkApplicationWrite` `dataprocrm.nodePools.*`

  * `dataprocrm.nodePools.create`
  * `dataprocrm.nodePools.delete`
  * `dataprocrm.nodePools.deleteNodes`
  * `dataprocrm.nodePools.get`
  * `dataprocrm.nodePools.list`
  * `dataprocrm.nodePools.resize`

`dataprocrm.nodes.list` `dataprocrm.operations.get`  
  
#### Dataproc Serverless Viewer 

(`roles/dataproc.serverlessViewer`) Permissions needed to view serverless sessions and batches  |  `compute.projects.get` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dataproc.batches.get` `dataproc.batches.list` `dataproc.sessionTemplates.get` `dataproc.sessionTemplates.list` `dataproc.sessions.get` `dataproc.sessions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataproc Worker 

(`roles/dataproc.worker`) Provides worker access to Managed Service for Apache Spark resources. Intended for service accounts.  |  `cloudprofiler.profiles.create` `cloudprofiler.profiles.update` `datalineage.locations.processOpenLineageMessage` `dataproc.agents.*`

  * `dataproc.agents.create`
  * `dataproc.agents.delete`
  * `dataproc.agents.get`
  * `dataproc.agents.list`
  * `dataproc.agents.update`

`dataproc.batches.computeTuningConfig` `dataproc.batches.sparkApplicationWrite` `dataproc.sessions.sparkApplicationWrite` `dataproc.tasks.*`

  * `dataproc.tasks.lease`
  * `dataproc.tasks.listInvalidatedLeases`
  * `dataproc.tasks.reportStatus`

`dataprocrm.nodePools.*`

  * `dataprocrm.nodePools.create`
  * `dataprocrm.nodePools.delete`
  * `dataprocrm.nodePools.deleteNodes`
  * `dataprocrm.nodePools.get`
  * `dataprocrm.nodePools.list`
  * `dataprocrm.nodePools.resize`

`dataprocrm.nodes.get` `dataprocrm.nodes.heartbeat` `dataprocrm.nodes.list` `dataprocrm.nodes.mintOAuthToken` `dataprocrm.operations.get` `logging.logEntries.create` `logging.logEntries.route` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `storage.buckets.get` `storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.managedFolders.create` `storage.managedFolders.delete` `storage.managedFolders.get` `storage.managedFolders.list` `storage.managedFolders.update` `storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.create` `storage.objects.createContext` `storage.objects.delete` `storage.objects.deleteContext` `storage.objects.get` `storage.objects.getIamPolicy` `storage.objects.list` `storage.objects.overrideUnlockedRetention` `storage.objects.restore` `storage.objects.setIamPolicy` `storage.objects.setRetention` `storage.objects.update` `storage.objects.updateContext`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Dataproc Service Agent 

(`roles/dataproc.serviceAgent`) Gives Dataproc Service Account access to service accounts, compute resources, storage resources, and kubernetes resources. Includes access to service accounts.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `backupdr.backupPlanAssociations.createForComputeDisk` `backupdr.backupPlanAssociations.createForComputeInstance` `backupdr.backupPlanAssociations.deleteForComputeDisk` `backupdr.backupPlanAssociations.deleteForComputeInstance` `backupdr.backupPlanAssociations.fetchForComputeDisk` `backupdr.backupPlanAssociations.getForComputeDisk` `backupdr.backupPlanAssociations.list` `backupdr.backupPlanAssociations.triggerBackupForComputeDisk` `backupdr.backupPlanAssociations.triggerBackupForComputeInstance` `backupdr.backupPlanAssociations.updateForComputeDisk` `backupdr.backupPlanAssociations.updateForComputeInstance` `backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupPlans.useForComputeDisk` `backupdr.backupPlans.useForComputeInstance` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.locations.list` `backupdr.operations.get` `backupdr.operations.list` `backupdr.serviceConfig.initialize` `biglake.catalogs.get` `cloudaicompanion.instances.completeTask` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.createInternal` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.addresses.use` `compute.addresses.useInternal` `compute.autoscalers.*`

  * `compute.autoscalers.create`
  * `compute.autoscalers.delete`
  * `compute.autoscalers.get`
  * `compute.autoscalers.list`
  * `compute.autoscalers.update`

`compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.create` `compute.disks.createSnapshot` `compute.disks.createTagBinding` `compute.disks.delete` `compute.disks.get` `compute.disks.list` `compute.disks.resize` `compute.disks.setLabels` `compute.disks.startAsyncReplication` `compute.disks.stopAsyncReplication` `compute.disks.stopGroupAsyncReplication` `compute.disks.update` `compute.disks.updateKmsKey` `compute.disks.use` `compute.disks.useReadOnly` `compute.firewalls.get` `compute.firewalls.list` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalAddresses.use` `compute.globalNetworkEndpointGroups.*`

  * `compute.globalNetworkEndpointGroups.attachNetworkEndpoints`
  * `compute.globalNetworkEndpointGroups.create`
  * `compute.globalNetworkEndpointGroups.createTagBinding`
  * `compute.globalNetworkEndpointGroups.delete`
  * `compute.globalNetworkEndpointGroups.deleteTagBinding`
  * `compute.globalNetworkEndpointGroups.detachNetworkEndpoints`
  * `compute.globalNetworkEndpointGroups.get`
  * `compute.globalNetworkEndpointGroups.list`
  * `compute.globalNetworkEndpointGroups.listEffectiveTags`
  * `compute.globalNetworkEndpointGroups.listTagBindings`
  * `compute.globalNetworkEndpointGroups.use`

`compute.globalOperations.get` `compute.globalOperations.list` `compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.images.get` `compute.images.getFromFamily` `compute.images.list` `compute.images.useReadOnly` `compute.instanceGroupManagers.*`

  * `compute.instanceGroupManagers.create`
  * `compute.instanceGroupManagers.createTagBinding`
  * `compute.instanceGroupManagers.delete`
  * `compute.instanceGroupManagers.deleteTagBinding`
  * `compute.instanceGroupManagers.get`
  * `compute.instanceGroupManagers.list`
  * `compute.instanceGroupManagers.listEffectiveTags`
  * `compute.instanceGroupManagers.listTagBindings`
  * `compute.instanceGroupManagers.update`
  * `compute.instanceGroupManagers.use`

`compute.instanceGroups.*`

  * `compute.instanceGroups.create`
  * `compute.instanceGroups.createTagBinding`
  * `compute.instanceGroups.delete`
  * `compute.instanceGroups.deleteTagBinding`
  * `compute.instanceGroups.get`
  * `compute.instanceGroups.list`
  * `compute.instanceGroups.listEffectiveTags`
  * `compute.instanceGroups.listTagBindings`
  * `compute.instanceGroups.update`
  * `compute.instanceGroups.use`

`compute.instanceSettings.get` `compute.instanceTemplates.*`

  * `compute.instanceTemplates.create`
  * `compute.instanceTemplates.delete`
  * `compute.instanceTemplates.get`
  * `compute.instanceTemplates.getIamPolicy`
  * `compute.instanceTemplates.list`
  * `compute.instanceTemplates.setIamPolicy`
  * `compute.instanceTemplates.useReadOnly`

`compute.instances.*`

  * `compute.instances.addAccessConfig`
  * `compute.instances.addNetworkInterface`
  * `compute.instances.addResourcePolicies`
  * `compute.instances.attachDisk`
  * `compute.instances.create`
  * `compute.instances.createTagBinding`
  * `compute.instances.delete`
  * `compute.instances.deleteAccessConfig`
  * `compute.instances.deleteNetworkInterface`
  * `compute.instances.deleteTagBinding`
  * `compute.instances.detachDisk`
  * `compute.instances.get`
  * `compute.instances.getEffectiveFirewalls`
  * `compute.instances.getGuestAttributes`
  * `compute.instances.getIamPolicy`
  * `compute.instances.getScreenshot`
  * `compute.instances.getSerialPortOutput`
  * `compute.instances.getShieldedInstanceIdentity`
  * `compute.instances.getShieldedVmIdentity`
  * `compute.instances.getVmExtensionState`
  * `compute.instances.list`
  * `compute.instances.listEffectiveTags`
  * `compute.instances.listReferrers`
  * `compute.instances.listTagBindings`
  * `compute.instances.listVmExtensionStates`
  * `compute.instances.osAdminLogin`
  * `compute.instances.osLogin`
  * `compute.instances.performMaintenance`
  * `compute.instances.pscInterfaceCreate`
  * `compute.instances.removeResourcePolicies`
  * `compute.instances.reset`
  * `compute.instances.resume`
  * `compute.instances.sendDiagnosticInterrupt`
  * `compute.instances.setDeletionProtection`
  * `compute.instances.setDiskAutoDelete`
  * `compute.instances.setIamPolicy`
  * `compute.instances.setLabels`
  * `compute.instances.setMachineResources`
  * `compute.instances.setMachineType`
  * `compute.instances.setMetadata`
  * `compute.instances.setMinCpuPlatform`
  * `compute.instances.setName`
  * `compute.instances.setScheduling`
  * `compute.instances.setSecurityPolicy`
  * `compute.instances.setServiceAccount`
  * `compute.instances.setShieldedInstanceIntegrityPolicy`
  * `compute.instances.setShieldedVmIntegrityPolicy`
  * `compute.instances.setTags`
  * `compute.instances.simulateMaintenanceEvent`
  * `compute.instances.start`
  * `compute.instances.startWithEncryptionKey`
  * `compute.instances.stop`
  * `compute.instances.suspend`
  * `compute.instances.troubleshoot`
  * `compute.instances.update`
  * `compute.instances.updateAccessConfig`
  * `compute.instances.updateDisplayDevice`
  * `compute.instances.updateNetworkInterface`
  * `compute.instances.updateSecurity`
  * `compute.instances.updateShieldedInstanceConfig`
  * `compute.instances.updateShieldedVmConfig`
  * `compute.instances.use`
  * `compute.instances.useReadOnly`

`compute.licenses.get` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.machineImages.*`

  * `compute.machineImages.create`
  * `compute.machineImages.createTagBinding`
  * `compute.machineImages.delete`
  * `compute.machineImages.deleteTagBinding`
  * `compute.machineImages.get`
  * `compute.machineImages.getIamPolicy`
  * `compute.machineImages.list`
  * `compute.machineImages.listEffectiveTags`
  * `compute.machineImages.listTagBindings`
  * `compute.machineImages.setIamPolicy`
  * `compute.machineImages.setLabels`
  * `compute.machineImages.useReadOnly`

`compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.multiMig.*`

  * `compute.multiMig.create`
  * `compute.multiMig.delete`
  * `compute.multiMig.get`
  * `compute.multiMig.list`

`compute.multiMigMembers.*`

  * `compute.multiMigMembers.get`
  * `compute.multiMigMembers.list`

`compute.networkEndpointGroups.*`

  * `compute.networkEndpointGroups.attachNetworkEndpoints`
  * `compute.networkEndpointGroups.create`
  * `compute.networkEndpointGroups.createTagBinding`
  * `compute.networkEndpointGroups.delete`
  * `compute.networkEndpointGroups.deleteTagBinding`
  * `compute.networkEndpointGroups.detachNetworkEndpoints`
  * `compute.networkEndpointGroups.get`
  * `compute.networkEndpointGroups.list`
  * `compute.networkEndpointGroups.listEffectiveTags`
  * `compute.networkEndpointGroups.listTagBindings`
  * `compute.networkEndpointGroups.use`

`compute.networks.create` `compute.networks.createTagBinding` `compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listTagBindings` `compute.networks.setFirewallPolicy` `compute.networks.use` `compute.networks.useExternalIp` `compute.nodeGroups.get` `compute.nodeTypes.get` `compute.projects.get` `compute.regionFirewallPolicies.create` `compute.regionFirewallPolicies.createTagBinding` `compute.regionFirewallPolicies.delete` `compute.regionFirewallPolicies.deleteTagBinding` `compute.regionFirewallPolicies.get` `compute.regionFirewallPolicies.update` `compute.regionFirewallPolicies.use` `compute.regionNetworkEndpointGroups.*`

  * `compute.regionNetworkEndpointGroups.attachNetworkEndpoints`
  * `compute.regionNetworkEndpointGroups.create`
  * `compute.regionNetworkEndpointGroups.createTagBinding`
  * `compute.regionNetworkEndpointGroups.delete`
  * `compute.regionNetworkEndpointGroups.deleteTagBinding`
  * `compute.regionNetworkEndpointGroups.detachNetworkEndpoints`
  * `compute.regionNetworkEndpointGroups.get`
  * `compute.regionNetworkEndpointGroups.list`
  * `compute.regionNetworkEndpointGroups.listEffectiveTags`
  * `compute.regionNetworkEndpointGroups.listTagBindings`
  * `compute.regionNetworkEndpointGroups.use`

`compute.regionOperations.get` `compute.regionOperations.list` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.reservationBlocks.get` `compute.reservationBlocks.list` `compute.reservationConsumedInstances.list` `compute.reservationSlots.*`

  * `compute.reservationSlots.get`
  * `compute.reservationSlots.list`
  * `compute.reservationSlots.update`

`compute.reservationSubBlocks.*`

  * `compute.reservationSubBlocks.get`
  * `compute.reservationSubBlocks.list`
  * `compute.reservationSubBlocks.performMaintenance`
  * `compute.reservationSubBlocks.reportFaulty`

`compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.list` `compute.resourcePolicies.useReadOnly` `compute.storagePools.get` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.storagePools.use` `compute.subnetworks.create` `compute.subnetworks.createTagBinding` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.subnetworks.setPrivateIpGoogleAccess` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.zoneOperations.get` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`container.clusterRoleBindings.*`

  * `container.clusterRoleBindings.create`
  * `container.clusterRoleBindings.delete`
  * `container.clusterRoleBindings.get`
  * `container.clusterRoleBindings.list`
  * `container.clusterRoleBindings.update`

`container.clusterRoles.*`

  * `container.clusterRoles.bind`
  * `container.clusterRoles.create`
  * `container.clusterRoles.delete`
  * `container.clusterRoles.escalate`
  * `container.clusterRoles.get`
  * `container.clusterRoles.list`
  * `container.clusterRoles.update`

`container.clusters.connect` `container.clusters.get` `container.clusters.update` `container.customResourceDefinitions.create` `container.customResourceDefinitions.delete` `container.customResourceDefinitions.get` `container.customResourceDefinitions.list` `container.customResourceDefinitions.update` `container.namespaces.create` `container.namespaces.delete` `container.namespaces.get` `container.namespaces.list` `container.namespaces.update` `container.operations.get` `container.roleBindings.*`

  * `container.roleBindings.create`
  * `container.roleBindings.delete`
  * `container.roleBindings.get`
  * `container.roleBindings.list`
  * `container.roleBindings.update`

`container.roles.bind` `container.roles.escalate` `dataproc.autoscalingPolicies.create` `dataproc.autoscalingPolicies.delete` `dataproc.autoscalingPolicies.get` `dataproc.autoscalingPolicies.getIamPolicy` `dataproc.autoscalingPolicies.list` `dataproc.autoscalingPolicies.update` `dataproc.autoscalingPolicies.use` `dataproc.clusters.*`

  * `dataproc.clusters.create`
  * `dataproc.clusters.delete`
  * `dataproc.clusters.get`
  * `dataproc.clusters.getIamPolicy`
  * `dataproc.clusters.list`
  * `dataproc.clusters.repair`
  * `dataproc.clusters.setIamPolicy`
  * `dataproc.clusters.start`
  * `dataproc.clusters.stop`
  * `dataproc.clusters.update`
  * `dataproc.clusters.use`

`dataproc.jobs.*`

  * `dataproc.jobs.cancel`
  * `dataproc.jobs.create`
  * `dataproc.jobs.delete`
  * `dataproc.jobs.get`
  * `dataproc.jobs.getIamPolicy`
  * `dataproc.jobs.list`
  * `dataproc.jobs.setIamPolicy`
  * `dataproc.jobs.update`

`dataproc.nodeGroups.*`

  * `dataproc.nodeGroups.create`
  * `dataproc.nodeGroups.get`
  * `dataproc.nodeGroups.update`

`dataproc.operations.cancel` `dataproc.sessionTemplates.get` `dataproc.sessions.*`

  * `dataproc.sessions.create`
  * `dataproc.sessions.delete`
  * `dataproc.sessions.get`
  * `dataproc.sessions.list`
  * `dataproc.sessions.sparkApplicationRead`
  * `dataproc.sessions.sparkApplicationWrite`
  * `dataproc.sessions.terminate`

`dataprocrm.nodePools.*`

  * `dataprocrm.nodePools.create`
  * `dataprocrm.nodePools.delete`
  * `dataprocrm.nodePools.deleteNodes`
  * `dataprocrm.nodePools.get`
  * `dataprocrm.nodePools.list`
  * `dataprocrm.nodePools.resize`

`dataprocrm.nodes.*`

  * `dataprocrm.nodes.get`
  * `dataprocrm.nodes.heartbeat`
  * `dataprocrm.nodes.list`
  * `dataprocrm.nodes.mintOAuthToken`
  * `dataprocrm.nodes.update`

`dataprocrm.operations.cancel` `dataprocrm.operations.get` `dataprocrm.operations.list` `dataprocrm.workloads.*`

  * `dataprocrm.workloads.cancel`
  * `dataprocrm.workloads.create`
  * `dataprocrm.workloads.delete`
  * `dataprocrm.workloads.get`
  * `dataprocrm.workloads.list`

`firebase.projects.get` `iam.serviceAccounts.actAs` `iam.serviceAccounts.getAccessToken` `metastore.services.get` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`orgpolicy.policy.get` `recommender.iamPolicyInsights.*`

  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyInsights.update`

`recommender.iamPolicyRecommendations.*`

  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyRecommendations.update`

`recommender.storageBucketSoftDeleteInsights.*`

  * `recommender.storageBucketSoftDeleteInsights.get`
  * `recommender.storageBucketSoftDeleteInsights.list`
  * `recommender.storageBucketSoftDeleteInsights.update`

`recommender.storageBucketSoftDeleteRecommendations.*`

  * `recommender.storageBucketSoftDeleteRecommendations.get`
  * `recommender.storageBucketSoftDeleteRecommendations.list`
  * `recommender.storageBucketSoftDeleteRecommendations.update`

`resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.list` `resourcemanager.tagKeys.create` `resourcemanager.tagKeys.get` `resourcemanager.tagKeys.getIamPolicy` `resourcemanager.tagKeys.setIamPolicy` `resourcemanager.tagValueBindings.*`

  * `resourcemanager.tagValueBindings.create`
  * `resourcemanager.tagValueBindings.delete`

`resourcemanager.tagValues.create` `resourcemanager.tagValues.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

  * `storage.anywhereCaches.create`
  * `storage.anywhereCaches.disable`
  * `storage.anywhereCaches.get`
  * `storage.anywhereCaches.list`
  * `storage.anywhereCaches.pause`
  * `storage.anywhereCaches.resume`
  * `storage.anywhereCaches.update`

`storage.bucketOperations.*`

  * `storage.bucketOperations.cancel`
  * `storage.bucketOperations.get`
  * `storage.bucketOperations.list`

`storage.buckets.*`

  * `storage.buckets.create`
  * `storage.buckets.createTagBinding`
  * `storage.buckets.delete`
  * `storage.buckets.deleteTagBinding`
  * `storage.buckets.enableObjectRetention`
  * `storage.buckets.get`
  * `storage.buckets.getIamPolicy`
  * `storage.buckets.getIpFilter`
  * `storage.buckets.getObjectInsights`
  * `storage.buckets.list`
  * `storage.buckets.listEffectiveTags`
  * `storage.buckets.listTagBindings`
  * `storage.buckets.relocate`
  * `storage.buckets.restore`
  * `storage.buckets.setIamPolicy`
  * `storage.buckets.setIpFilter`
  * `storage.buckets.update`
  * `storage.buckets.viewIntelligenceDetails`
  * `storage.buckets.viewSecurityIntelligenceDetails`

`storage.featureConfigs.*`

  * `storage.featureConfigs.create`
  * `storage.featureConfigs.delete`
  * `storage.featureConfigs.get`
  * `storage.featureConfigs.list`
  * `storage.featureConfigs.update`

`storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.intelligenceConfigs.*`

  * `storage.intelligenceConfigs.get`
  * `storage.intelligenceConfigs.update`

`storage.managedFolders.*`

  * `storage.managedFolders.create`
  * `storage.managedFolders.delete`
  * `storage.managedFolders.get`
  * `storage.managedFolders.getIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.setIamPolicy`
  * `storage.managedFolders.update`

`storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.*`

  * `storage.objects.create`
  * `storage.objects.createContext`
  * `storage.objects.delete`
  * `storage.objects.deleteContext`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.list`
  * `storage.objects.move`
  * `storage.objects.overrideUnlockedRetention`
  * `storage.objects.restore`
  * `storage.objects.setIamPolicy`
  * `storage.objects.setRetention`
  * `storage.objects.update`
  * `storage.objects.updateContext`

`storagebatchoperations.*`

  * `storagebatchoperations.bucketOperations.get`
  * `storagebatchoperations.bucketOperations.list`
  * `storagebatchoperations.jobs.cancel`
  * `storagebatchoperations.jobs.create`
  * `storagebatchoperations.jobs.delete`
  * `storagebatchoperations.jobs.get`
  * `storagebatchoperations.jobs.list`
  * `storagebatchoperations.locations.get`
  * `storagebatchoperations.locations.list`
  * `storagebatchoperations.operations.cancel`
  * `storagebatchoperations.operations.delete`
  * `storagebatchoperations.operations.get`
  * `storagebatchoperations.operations.list`

  
  
## Project roles

You can also set permissions at the project level by using IAM **Project** roles. The following table summarizes the permissions associated with IAM project roles:

Project Role | Permissions  
---|---  
Project Viewer | All project permissions for read-only actions that preserve state (get, list)  
Project Editor | All Project Viewer permissions plus all project permissions for actions that modify state (create, delete, update, use, cancel, stop, start)  
Project Owner | All Project Editor permissions plus permissions to manage access control for the project (get/set IamPolicy) and to set up project billing  
  
## What's next

  * Learn how to [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
