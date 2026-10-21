---
url: https://docs.cloud.google.com/composer/docs/composer-2/access-control/
title: Access control with IAM \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:02:13.462491+00:00
---

# Access control with IAM  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/access-control/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/access-control "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/access-control "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes the access control options available to you in Managed Airflow and explains how to grant roles.

For information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

With [Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-2/airflow-rbac), you can control permissions for the Airflow UI and DAG UI beyond enabling or disabling access to it.

If you want to set up access for external identities through [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), see [Access environments with workforce identity federation](https://docs.cloud.google.com/composer/docs/composer-2/access-environments-with-workforce-identity-federation).

## About Identity and Access Management in Managed Airflow

Managed Airflow uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) for access control.

You control access to different Managed Airflow features by granting roles and permissions both for [IAM service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) and for user accounts in your Google Cloud project.

Managed Airflow uses two types of IAM service accounts:

  * Managed Airflow Service Agent account
  * Environment's service account



In addition to these two types of service account, [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) runs internal Google processes on your behalf.

## Grant roles to Managed Airflow Service Agent account

In your Google Cloud project, Managed Airflow service creates a service agent, the _Managed Airflow Service Agent_ , to manage resources related to Managed Airflow.

The Managed Airflow Service Agent is used for all environments in your project. By default, the Managed Airflow Service Agent account has only the **Cloud Composer API Service Agent** role. Keep this role on this service account.

**Note:** The Google APIs Service Agent account (also known as Cloud Services Service Account) runs internal Google processes on your behalf. We [recommend to keep the default permissions](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) on this Service Agent account, which is the Project Editor role.

Managed Airflow (Gen 2) uses [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview), which requires [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). To support Workload Identity, the service account of your environment must have bindings to the Kubernetes service account that runs your environment's cluster. These bindings are needed so that pods of your environment cluster can access resources of your Google Cloud project. For example, to read DAG definition files from the environment's bucket.

To create bindings between your environment's service account and the Kubernetes service account of your environment's cluster, the Composer Service Agent account must have enough permissions to do so. This requires `iam.serviceAccounts.getIamPolicy` and `iam.serviceAccounts.setIamPolicy` permissions, which are provided by the **Cloud Composer v2 API Service Agent Extension** (`roles/composer.ServiceAgentV2Ext`) role.

**This role is not granted automatically**. You must grant it manually. For instructions on granting this role, see [Grant required permissions to Managed Airflow service account](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#grant-permissions).

**Warning:** After you grant this role, the Composer Service Agent account **can modify the IAM policy of your environment's service account**. Managed Airflow uses these permissions to create bindings between your environment's service account and the Kubernetes service account of your environment's cluster.

## Grant roles to an environment's service account

**Warning:** Before you specify a service account for an environment, make sure to get familiar with all security considerations that apply to environment service accounts.

When you create an environment, you specify a service account. This service account is called _environment's service account_. You cannot change the specified service account after an environment is created.

Your environment uses this service account to perform most of the operations, for example:

  * Running Pods with different [environment components](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture), such as Airflow workers and schedulers, in your environment's cluster.

  * Executing DAGs on behalf of this service account. For example, if a DAG accesses another Google service, this is done on behalf of the service account.

  * Building the images of Airflow components when custom PyPI packages are installed in the environment.

  * Reading and writing objects in the environment's bucket. For example, when synchronizing files between the environment's bucket and Airflow components.

  * Running Pods launched through KubernetesPodOperator and GKEStartPodOperator.




Managed Airflow binds this service account to the Kubernetes service account of your environment. Nodes in your environment's cluster run as the Kubernetes service account and use the bindings to access resources in your Google Cloud project, such as DAG files in your environment's bucket. Thus, if you want your environment to access other resources in your Google Cloud project, grant permissions to the service account of your environment (IAM service account), and not to the Kubernetes service account.

**Caution:** If you delete an environment's service account, all environments that use it stop working and cannot be recovered. Even if a service account with the same name is created again, it is not possible to recover the affected environments. It is still possible to access data stored in the affected environment's buckets.

### Existing and custom service accounts for your environment

We strongly recommend to set up a **user-managed service account** and use it for Managed Airflow environments. To do so:

  1. [Create a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating) as described in the Identity and Access Management documentation.

  2. Grant it the **Composer Worker** (`composer.worker`) role.

  3. If your environment [uses resource location restrictions](https://docs.cloud.google.com/composer/docs/composer-2/configure-resource-location-restrictions), or installs PyPI packages [from an Artifact Registry repository](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies#install-ar-repo) or [from a private repository](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies#install-private-repo), then grant the **Service Account User** (`iam.serviceAccountUser`) role to the **user-managed service account** that runs your environment on itself (both the principal and the resource are the same service account).

  4. To access other resources in your Google Cloud project, grant extra permissions to access those resources to this service account. The **Composer Worker** (`composer.worker`) role provides this required set of permissions in most cases. Add extra permissions to this service account only when it's necessary for the operation of your DAGs.




### Security considerations for environment service accounts

**Warning:** Your environment's service account can have **too broad permissions on your project**. Because your environment runs DAGs on behalf of your environment's service account, users who can add and modify DAGs and other files in your environment's bucket or modify Artifact Registry repositories in your project **can run their code on behalf of the environment's service account** and **exercise all permissions of this account**.

  * We strongly recommend to set up a user-managed service account for Managed Airflow environments that has only the required set of permissions that are necessary to run the environment and perform operations defined in your DAGs. The **Composer Worker** (`composer.worker`) role provides this required set of permissions in most cases. Add extra permissions to this service account only when it's necessary for the operation of your DAGs.

  * It is possible to create Managed Airflow environments that use the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). This account usually has more more permissions than it's necessary to run Managed Airflow environments or DAGs. Because your environment runs DAGs on behalf of its service account, this creates a risk of DAGs using broader permissions than intended. At the same time, it's often not possible to reduce permissions of this service account without impacting other services that might use it in your project. Instead, set up a user-managed service account.

  * Make sure to grant read-write access to your environment's bucket only to trusted users.

Because the environment's service account is used to run DAGs, users who can add and modify DAGs (or other objects such as Python dependencies) in the environment's bucket can run their code on behalf of the environment's service account and get access to all its permissions through deploying their own versions of DAGs. This might happen even if their user accounts don't have explicit Managed Airflow-related roles and permissions that allow such actions.

  * Make sure to grant access to Artifact Registry repositories in your project only to trusted users.

Airflow components of your environment use container images stored in these repositories and it's possible to use a custom container image with KubernetesPodOperator, GKEPodOperator, or GKEStartPodOperator from a DAG. These users can either deploy their own versions of container images for Airflow components of your environment (such as Airflow workers), or run a DAG that uses one of the listed operators to run an uploaded container image. As a result, these users can run their code on behalf of the environment's service account and get access to all its permissions.

  * Make sure to allow only trusted users to update environments in your project.

The `composer.environments.update` permission can be used beyond just applying configuration changes. It provides broad control over Managed Airflow resources, including code execution on behalf of the environment's service account, which can exercise all permissions that this service account has. For example, the installation of PyPI packages involves executing Python code from the package. As another example, environment variables might be used to store the code to be executed by a DAG, or point to a location with such code.

  * Make sure to allow only trusted users to [run Airflow CLI commands](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-cli) in your project.

The `composer.environments.executeairflowcommand` permission can be used to execute Python code available to Airflow components on behalf of environment's service account.




## Grant roles to users

To trigger an environment operation, a user must have enough permissions. For example, if you want to create a new environment, you must have the `composer.environments.create` permission.

For Managed Airflow, individual permissions are grouped into predefined roles. You can grant these roles to principals.

**Note:** For a list of permissions in predefined roles for Managed Airflow, see Roles.

If your user account has the **Project Editor** role, then you can execute all environment operations. However, this role has broad permissions. For users that work with environments, we recommend to use roles that are specific to Managed Airflow. In this way, you can narrow the scope of permissions and provide different access levels to different principals. For example, one user can have permissions to create, update, upgrade, and delete environments, while another user can only view environments and access the Airflow web interface.

Depending on the level of access that you want to provide for Managed Airflow environments, grant the following permissions to principals.

### Manage environments and environment buckets

For a user that can view, create, update, upgrade, hibernate, and delete environments, manage objects (such as DAG files) in the environment buckets, access the Airflow web interface, run Airflow CLI commands, view and trigger DAGs from the [DAG UI](https://docs.cloud.google.com/composer/docs/composer-2/view-dags):

  1. Grant the **Environment and Storage Object Administrator** (`composer.environmentAndStorageObjectAdmin`) role.

  2. Grant the **Service Account User** (`iam.serviceAccountUser`) role.

To narrow down permissions for a user, grant this role only on the service account of your environment. For more information, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

  3. Grant the `iam.serviceAccounts.actAs` permission on the service account of your environment.




### Manage environments

For a user that can view, create, update, upgrade, hibernate, and delete environments, access the Airflow web interface, run Airflow CLI commands, view and trigger DAGs from the [DAG UI](https://docs.cloud.google.com/composer/docs/composer-2/view-dags):

  1. Grant the **Composer Administrator** (`composer.admin`) role.

  2. Grant the **Service Account User** (`iam.serviceAccountUser`) role.

To narrow down permissions for a user, grant this role only on the service account of your environment. For more information, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

  3. Grant the `iam.serviceAccounts.actAs` permission on the service account of your environment.




### View environments and manage environment buckets

For a user that can view environments, access the Airflow web interface, view and trigger DAGs from the [DAG UI](https://docs.cloud.google.com/composer/docs/composer-2/view-dags), and manage objects in the environment buckets (for example, to upload new DAG files):

  1. Grant the **Environment User and Storage Object Viewer** (`composer.environmentAndStorageObjectViewer`) role.

  2. Grant the **Storage Object Admin** (`storage.objectAdmin`) role.




### View environments and environment buckets

For a user that can view environments, access the Airflow web interface, view and trigger DAGs from the [DAG UI](https://docs.cloud.google.com/composer/docs/composer-2/view-dags), and view objects in environment buckets, grant the **Environment User and Storage Object Viewer** (`composer.environmentAndStorageObjectViewer`) role.

### View environments

For a user that can view environments, view and trigger DAGs from the [DAG UI](https://docs.cloud.google.com/composer/docs/composer-2/view-dags) and access the Airflow web interface, grant the **Composer User** (`composer.user`) role.

## Roles

Role | Permissions  
---|---  
  
#### Composer Administrator 

(`roles/composer.admin`) Provides full control of Managed Airflow resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `composer.*`

  * `composer.dags.execute`
  * `composer.dags.get`
  * `composer.dags.getSourceCode`
  * `composer.dags.list`
  * `composer.environments.create`
  * `composer.environments.createTagBinding`
  * `composer.environments.delete`
  * `composer.environments.deleteTagBinding`
  * `composer.environments.executeAirflowCommand`
  * `composer.environments.get`
  * `composer.environments.list`
  * `composer.environments.listEffectiveTags`
  * `composer.environments.listTagBindings`
  * `composer.environments.update`
  * `composer.imageversions.list`
  * `composer.operations.delete`
  * `composer.operations.get`
  * `composer.operations.list`
  * `composer.userworkloadsconfigmaps.create`
  * `composer.userworkloadsconfigmaps.delete`
  * `composer.userworkloadsconfigmaps.get`
  * `composer.userworkloadsconfigmaps.list`
  * `composer.userworkloadsconfigmaps.update`
  * `composer.userworkloadssecrets.create`
  * `composer.userworkloadssecrets.delete`
  * `composer.userworkloadssecrets.get`
  * `composer.userworkloadssecrets.list`
  * `composer.userworkloadssecrets.update`

`serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Composer Editor 

(`roles/composer.editor`) Editor role for Composer  |  `composer.dags.*`

  * `composer.dags.execute`
  * `composer.dags.get`
  * `composer.dags.getSourceCode`
  * `composer.dags.list`

`composer.environments.create` `composer.environments.delete` `composer.environments.executeAirflowCommand` `composer.environments.get` `composer.environments.list` `composer.environments.listEffectiveTags` `composer.environments.listTagBindings` `composer.environments.update` `composer.imageversions.list` `composer.operations.*`

  * `composer.operations.delete`
  * `composer.operations.get`
  * `composer.operations.list`

`composer.userworkloadsconfigmaps.*`

  * `composer.userworkloadsconfigmaps.create`
  * `composer.userworkloadsconfigmaps.delete`
  * `composer.userworkloadsconfigmaps.get`
  * `composer.userworkloadsconfigmaps.list`
  * `composer.userworkloadsconfigmaps.update`

`composer.userworkloadssecrets.*`

  * `composer.userworkloadssecrets.create`
  * `composer.userworkloadssecrets.delete`
  * `composer.userworkloadssecrets.get`
  * `composer.userworkloadssecrets.list`
  * `composer.userworkloadssecrets.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Composer User 

(`roles/composer.user`) Provides the permissions necessary to list and get Managed Airflow environments and operations.  Lowest-level resources where you can grant this role:

  * Project 

|  `composer.dags.*`

  * `composer.dags.execute`
  * `composer.dags.get`
  * `composer.dags.getSourceCode`
  * `composer.dags.list`

`composer.environments.get` `composer.environments.list` `composer.imageversions.list` `composer.operations.get` `composer.operations.list` `composer.userworkloadsconfigmaps.get` `composer.userworkloadsconfigmaps.list` `composer.userworkloadssecrets.get` `composer.userworkloadssecrets.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Composer Viewer 

(`roles/composer.viewer`) Viewer role for Composer  |  `composer.dags.get` `composer.dags.getSourceCode` `composer.dags.list` `composer.environments.get` `composer.environments.list` `composer.environments.listEffectiveTags` `composer.environments.listTagBindings` `composer.imageversions.list` `composer.operations.get` `composer.operations.list` `composer.userworkloadsconfigmaps.get` `composer.userworkloadsconfigmaps.list` `composer.userworkloadssecrets.get` `composer.userworkloadssecrets.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Composer v2 API Service Agent Extension 

(`roles/composer.ServiceAgentV2Ext`) Cloud Composer v2 API Service Agent Extension is a supplementary role required to manage Composer v2 environments.  |  `iam.serviceAccounts.getIamPolicy` `iam.serviceAccounts.setIamPolicy`  
  
#### Environment and Storage Object Administrator 

(`roles/composer.environmentAndStorageObjectAdmin`) Provides full control of Managed Airflow resources and of the objects in all project buckets.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `composer.*`

  * `composer.dags.execute`
  * `composer.dags.get`
  * `composer.dags.getSourceCode`
  * `composer.dags.list`
  * `composer.environments.create`
  * `composer.environments.createTagBinding`
  * `composer.environments.delete`
  * `composer.environments.deleteTagBinding`
  * `composer.environments.executeAirflowCommand`
  * `composer.environments.get`
  * `composer.environments.list`
  * `composer.environments.listEffectiveTags`
  * `composer.environments.listTagBindings`
  * `composer.environments.update`
  * `composer.imageversions.list`
  * `composer.operations.delete`
  * `composer.operations.get`
  * `composer.operations.list`
  * `composer.userworkloadsconfigmaps.create`
  * `composer.userworkloadsconfigmaps.delete`
  * `composer.userworkloadsconfigmaps.get`
  * `composer.userworkloadsconfigmaps.list`
  * `composer.userworkloadsconfigmaps.update`
  * `composer.userworkloadssecrets.create`
  * `composer.userworkloadssecrets.delete`
  * `composer.userworkloadssecrets.get`
  * `composer.userworkloadssecrets.list`
  * `composer.userworkloadssecrets.update`

`monitoring.timeSeries.create` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.folders.*`

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

  
  
#### Environment and Storage Object User 

(`roles/composer.environmentAndStorageObjectUser`) Read and use access to Cloud Composer resources and read access to Cloud Storage objects.  |  `composer.dags.*`

  * `composer.dags.execute`
  * `composer.dags.get`
  * `composer.dags.getSourceCode`
  * `composer.dags.list`

`composer.environments.get` `composer.environments.list` `composer.imageversions.list` `composer.operations.get` `composer.operations.list` `composer.userworkloadsconfigmaps.get` `composer.userworkloadsconfigmaps.list` `composer.userworkloadssecrets.get` `composer.userworkloadssecrets.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.folders.get` `storage.folders.list` `storage.managedFolders.get` `storage.managedFolders.list` `storage.objects.get` `storage.objects.list`  
  
#### Environment and Storage Object Viewer 

(`roles/composer.environmentAndStorageObjectViewer`) Provides the permissions necessary to list and get Managed Airflow environments and operations. Provides read-only access to objects in all project buckets.  Lowest-level resources where you can grant this role:

  * Project 

|  `composer.dags.*`

  * `composer.dags.execute`
  * `composer.dags.get`
  * `composer.dags.getSourceCode`
  * `composer.dags.list`

`composer.environments.get` `composer.environments.list` `composer.imageversions.list` `composer.operations.get` `composer.operations.list` `composer.userworkloadsconfigmaps.get` `composer.userworkloadsconfigmaps.list` `composer.userworkloadssecrets.get` `composer.userworkloadssecrets.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.folders.get` `storage.folders.list` `storage.managedFolders.get` `storage.managedFolders.list` `storage.objects.get` `storage.objects.list`  
  
#### Composer Shared VPC Agent 

(`roles/composer.sharedVpcAgent`) Role that should be assigned to Composer Agent service account in Shared VPC host project  |  `compute.networkAttachments.create` `compute.networkAttachments.delete` `compute.networkAttachments.get` `compute.networkAttachments.update` `compute.networks.access` `compute.networks.addPeering` `compute.networks.get` `compute.networks.list` `compute.networks.listPeeringRoutes` `compute.networks.removePeering` `compute.networks.updatePeering` `compute.networks.use` `compute.networks.useExternalIp` `compute.projects.get` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dns.managedZones.get` `dns.managedZones.list` `dns.networks.targetWithPeeringZone`  
  
#### Composer Worker 

(`roles/composer.worker`) Provides the permissions necessary to run a Managed Airflow environment VM. Intended for service accounts.  Lowest-level resources where you can grant this role:

  * Project 

|  `artifactregistry.*`

  * `artifactregistry.aptartifacts.create`
  * `artifactregistry.attachments.create`
  * `artifactregistry.attachments.delete`
  * `artifactregistry.attachments.get`
  * `artifactregistry.attachments.list`
  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`
  * `artifactregistry.files.delete`
  * `artifactregistry.files.download`
  * `artifactregistry.files.get`
  * `artifactregistry.files.list`
  * `artifactregistry.files.update`
  * `artifactregistry.files.upload`
  * `artifactregistry.kfpartifacts.create`
  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`
  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`
  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`
  * `artifactregistry.packages.delete`
  * `artifactregistry.packages.get`
  * `artifactregistry.packages.list`
  * `artifactregistry.packages.update`
  * `artifactregistry.projectconfigs.get`
  * `artifactregistry.projectconfigs.update`
  * `artifactregistry.projectsettings.get`
  * `artifactregistry.projectsettings.update`
  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`
  * `artifactregistry.repositories.create`
  * `artifactregistry.repositories.createOnPush`
  * `artifactregistry.repositories.createTagBinding`
  * `artifactregistry.repositories.delete`
  * `artifactregistry.repositories.deleteArtifacts`
  * `artifactregistry.repositories.deleteTagBinding`
  * `artifactregistry.repositories.downloadArtifacts`
  * `artifactregistry.repositories.exportArtifacts`
  * `artifactregistry.repositories.get`
  * `artifactregistry.repositories.getIamPolicy`
  * `artifactregistry.repositories.list`
  * `artifactregistry.repositories.listEffectiveTags`
  * `artifactregistry.repositories.listTagBindings`
  * `artifactregistry.repositories.readViaVirtualRepository`
  * `artifactregistry.repositories.setIamPolicy`
  * `artifactregistry.repositories.update`
  * `artifactregistry.repositories.uploadArtifacts`
  * `artifactregistry.rules.create`
  * `artifactregistry.rules.delete`
  * `artifactregistry.rules.get`
  * `artifactregistry.rules.list`
  * `artifactregistry.rules.update`
  * `artifactregistry.tags.create`
  * `artifactregistry.tags.delete`
  * `artifactregistry.tags.get`
  * `artifactregistry.tags.list`
  * `artifactregistry.tags.update`
  * `artifactregistry.versions.delete`
  * `artifactregistry.versions.get`
  * `artifactregistry.versions.list`
  * `artifactregistry.versions.update`
  * `artifactregistry.yumartifacts.create`

`cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.builds.update` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudbuild.workerpools.use` `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `composer.environments.get` `compute.images.create` `container.*`

  * `container.apiServices.create`
  * `container.apiServices.delete`
  * `container.apiServices.get`
  * `container.apiServices.getStatus`
  * `container.apiServices.list`
  * `container.apiServices.update`
  * `container.apiServices.updateStatus`
  * `container.auditSinks.create`
  * `container.auditSinks.delete`
  * `container.auditSinks.get`
  * `container.auditSinks.list`
  * `container.auditSinks.update`
  * `container.backendConfigs.create`
  * `container.backendConfigs.delete`
  * `container.backendConfigs.get`
  * `container.backendConfigs.list`
  * `container.backendConfigs.update`
  * `container.bindings.create`
  * `container.bindings.delete`
  * `container.bindings.get`
  * `container.bindings.list`
  * `container.bindings.update`
  * `container.certificateSigningRequests.approve`
  * `container.certificateSigningRequests.create`
  * `container.certificateSigningRequests.delete`
  * `container.certificateSigningRequests.get`
  * `container.certificateSigningRequests.getStatus`
  * `container.certificateSigningRequests.list`
  * `container.certificateSigningRequests.update`
  * `container.certificateSigningRequests.updateStatus`
  * `container.clusterRoleBindings.create`
  * `container.clusterRoleBindings.delete`
  * `container.clusterRoleBindings.get`
  * `container.clusterRoleBindings.list`
  * `container.clusterRoleBindings.update`
  * `container.clusterRoles.bind`
  * `container.clusterRoles.create`
  * `container.clusterRoles.delete`
  * `container.clusterRoles.escalate`
  * `container.clusterRoles.get`
  * `container.clusterRoles.list`
  * `container.clusterRoles.update`
  * `container.clusters.connect`
  * `container.clusters.create`
  * `container.clusters.createTagBinding`
  * `container.clusters.delete`
  * `container.clusters.deleteTagBinding`
  * `container.clusters.get`
  * `container.clusters.getCredentials`
  * `container.clusters.impersonate`
  * `container.clusters.list`
  * `container.clusters.listEffectiveTags`
  * `container.clusters.listTagBindings`
  * `container.clusters.update`
  * `container.componentStatuses.get`
  * `container.componentStatuses.list`
  * `container.configMaps.create`
  * `container.configMaps.delete`
  * `container.configMaps.get`
  * `container.configMaps.list`
  * `container.configMaps.update`
  * `container.controllerRevisions.create`
  * `container.controllerRevisions.delete`
  * `container.controllerRevisions.get`
  * `container.controllerRevisions.list`
  * `container.controllerRevisions.update`
  * `container.cronJobs.create`
  * `container.cronJobs.delete`
  * `container.cronJobs.get`
  * `container.cronJobs.getStatus`
  * `container.cronJobs.list`
  * `container.cronJobs.update`
  * `container.cronJobs.updateStatus`
  * `container.csiDrivers.create`
  * `container.csiDrivers.delete`
  * `container.csiDrivers.get`
  * `container.csiDrivers.list`
  * `container.csiDrivers.update`
  * `container.csiNodeInfos.create`
  * `container.csiNodeInfos.delete`
  * `container.csiNodeInfos.get`
  * `container.csiNodeInfos.list`
  * `container.csiNodeInfos.update`
  * `container.csiNodes.create`
  * `container.csiNodes.delete`
  * `container.csiNodes.get`
  * `container.csiNodes.list`
  * `container.csiNodes.update`
  * `container.customResourceDefinitions.create`
  * `container.customResourceDefinitions.delete`
  * `container.customResourceDefinitions.get`
  * `container.customResourceDefinitions.getStatus`
  * `container.customResourceDefinitions.list`
  * `container.customResourceDefinitions.update`
  * `container.customResourceDefinitions.updateStatus`
  * `container.daemonSets.create`
  * `container.daemonSets.delete`
  * `container.daemonSets.get`
  * `container.daemonSets.getStatus`
  * `container.daemonSets.list`
  * `container.daemonSets.update`
  * `container.daemonSets.updateStatus`
  * `container.deployments.create`
  * `container.deployments.delete`
  * `container.deployments.get`
  * `container.deployments.getScale`
  * `container.deployments.getStatus`
  * `container.deployments.list`
  * `container.deployments.rollback`
  * `container.deployments.update`
  * `container.deployments.updateScale`
  * `container.deployments.updateStatus`
  * `container.endpointSlices.create`
  * `container.endpointSlices.delete`
  * `container.endpointSlices.get`
  * `container.endpointSlices.list`
  * `container.endpointSlices.update`
  * `container.endpoints.create`
  * `container.endpoints.delete`
  * `container.endpoints.get`
  * `container.endpoints.list`
  * `container.endpoints.update`
  * `container.events.create`
  * `container.events.delete`
  * `container.events.get`
  * `container.events.list`
  * `container.events.update`
  * `container.frontendConfigs.create`
  * `container.frontendConfigs.delete`
  * `container.frontendConfigs.get`
  * `container.frontendConfigs.list`
  * `container.frontendConfigs.update`
  * `container.horizontalPodAutoscalers.create`
  * `container.horizontalPodAutoscalers.delete`
  * `container.horizontalPodAutoscalers.get`
  * `container.horizontalPodAutoscalers.getStatus`
  * `container.horizontalPodAutoscalers.list`
  * `container.horizontalPodAutoscalers.update`
  * `container.horizontalPodAutoscalers.updateStatus`
  * `container.hostServiceAgent.use`
  * `container.ingresses.create`
  * `container.ingresses.delete`
  * `container.ingresses.get`
  * `container.ingresses.getStatus`
  * `container.ingresses.list`
  * `container.ingresses.update`
  * `container.ingresses.updateStatus`
  * `container.initializerConfigurations.create`
  * `container.initializerConfigurations.delete`
  * `container.initializerConfigurations.get`
  * `container.initializerConfigurations.list`
  * `container.initializerConfigurations.update`
  * `container.jobs.create`
  * `container.jobs.delete`
  * `container.jobs.get`
  * `container.jobs.getStatus`
  * `container.jobs.list`
  * `container.jobs.update`
  * `container.jobs.updateStatus`
  * `container.leases.create`
  * `container.leases.delete`
  * `container.leases.get`
  * `container.leases.list`
  * `container.leases.update`
  * `container.limitRanges.create`
  * `container.limitRanges.delete`
  * `container.limitRanges.get`
  * `container.limitRanges.list`
  * `container.limitRanges.update`
  * `container.localSubjectAccessReviews.create`
  * `container.localSubjectAccessReviews.list`
  * `container.managedCertificates.create`
  * `container.managedCertificates.delete`
  * `container.managedCertificates.get`
  * `container.managedCertificates.list`
  * `container.managedCertificates.update`
  * `container.mutatingWebhookConfigurations.create`
  * `container.mutatingWebhookConfigurations.delete`
  * `container.mutatingWebhookConfigurations.get`
  * `container.mutatingWebhookConfigurations.list`
  * `container.mutatingWebhookConfigurations.update`
  * `container.namespaces.create`
  * `container.namespaces.delete`
  * `container.namespaces.finalize`
  * `container.namespaces.get`
  * `container.namespaces.getStatus`
  * `container.namespaces.list`
  * `container.namespaces.update`
  * `container.namespaces.updateStatus`
  * `container.networkPolicies.create`
  * `container.networkPolicies.delete`
  * `container.networkPolicies.get`
  * `container.networkPolicies.list`
  * `container.networkPolicies.update`
  * `container.nodes.create`
  * `container.nodes.delete`
  * `container.nodes.get`
  * `container.nodes.getStatus`
  * `container.nodes.list`
  * `container.nodes.proxy`
  * `container.nodes.update`
  * `container.nodes.updateStatus`
  * `container.operations.get`
  * `container.operations.list`
  * `container.persistentVolumeClaims.create`
  * `container.persistentVolumeClaims.delete`
  * `container.persistentVolumeClaims.get`
  * `container.persistentVolumeClaims.getStatus`
  * `container.persistentVolumeClaims.list`
  * `container.persistentVolumeClaims.update`
  * `container.persistentVolumeClaims.updateStatus`
  * `container.persistentVolumes.create`
  * `container.persistentVolumes.delete`
  * `container.persistentVolumes.get`
  * `container.persistentVolumes.getStatus`
  * `container.persistentVolumes.list`
  * `container.persistentVolumes.update`
  * `container.persistentVolumes.updateStatus`
  * `container.petSets.create`
  * `container.petSets.delete`
  * `container.petSets.get`
  * `container.petSets.list`
  * `container.petSets.update`
  * `container.petSets.updateStatus`
  * `container.podDisruptionBudgets.create`
  * `container.podDisruptionBudgets.delete`
  * `container.podDisruptionBudgets.get`
  * `container.podDisruptionBudgets.getStatus`
  * `container.podDisruptionBudgets.list`
  * `container.podDisruptionBudgets.update`
  * `container.podDisruptionBudgets.updateStatus`
  * `container.podPresets.create`
  * `container.podPresets.delete`
  * `container.podPresets.get`
  * `container.podPresets.list`
  * `container.podPresets.update`
  * `container.podSecurityPolicies.create`
  * `container.podSecurityPolicies.delete`
  * `container.podSecurityPolicies.get`
  * `container.podSecurityPolicies.list`
  * `container.podSecurityPolicies.update`
  * `container.podSecurityPolicies.use`
  * `container.podTemplates.create`
  * `container.podTemplates.delete`
  * `container.podTemplates.get`
  * `container.podTemplates.list`
  * `container.podTemplates.update`
  * `container.pods.attach`
  * `container.pods.create`
  * `container.pods.delete`
  * `container.pods.evict`
  * `container.pods.exec`
  * `container.pods.get`
  * `container.pods.getLogs`
  * `container.pods.getStatus`
  * `container.pods.initialize`
  * `container.pods.list`
  * `container.pods.portForward`
  * `container.pods.proxy`
  * `container.pods.update`
  * `container.pods.updateStatus`
  * `container.priorityClasses.create`
  * `container.priorityClasses.delete`
  * `container.priorityClasses.get`
  * `container.priorityClasses.list`
  * `container.priorityClasses.update`
  * `container.replicaSets.create`
  * `container.replicaSets.delete`
  * `container.replicaSets.get`
  * `container.replicaSets.getScale`
  * `container.replicaSets.getStatus`
  * `container.replicaSets.list`
  * `container.replicaSets.update`
  * `container.replicaSets.updateScale`
  * `container.replicaSets.updateStatus`
  * `container.replicationControllers.create`
  * `container.replicationControllers.delete`
  * `container.replicationControllers.get`
  * `container.replicationControllers.getScale`
  * `container.replicationControllers.getStatus`
  * `container.replicationControllers.list`
  * `container.replicationControllers.update`
  * `container.replicationControllers.updateScale`
  * `container.replicationControllers.updateStatus`
  * `container.resourceQuotas.create`
  * `container.resourceQuotas.delete`
  * `container.resourceQuotas.get`
  * `container.resourceQuotas.getStatus`
  * `container.resourceQuotas.list`
  * `container.resourceQuotas.update`
  * `container.resourceQuotas.updateStatus`
  * `container.roleBindings.create`
  * `container.roleBindings.delete`
  * `container.roleBindings.get`
  * `container.roleBindings.list`
  * `container.roleBindings.update`
  * `container.roles.bind`
  * `container.roles.create`
  * `container.roles.delete`
  * `container.roles.escalate`
  * `container.roles.get`
  * `container.roles.list`
  * `container.roles.update`
  * `container.runtimeClasses.create`
  * `container.runtimeClasses.delete`
  * `container.runtimeClasses.get`
  * `container.runtimeClasses.list`
  * `container.runtimeClasses.update`
  * `container.scheduledJobs.create`
  * `container.scheduledJobs.delete`
  * `container.scheduledJobs.get`
  * `container.scheduledJobs.list`
  * `container.scheduledJobs.update`
  * `container.scheduledJobs.updateStatus`
  * `container.secrets.create`
  * `container.secrets.delete`
  * `container.secrets.get`
  * `container.secrets.list`
  * `container.secrets.update`
  * `container.selfSubjectAccessReviews.create`
  * `container.selfSubjectAccessReviews.list`
  * `container.selfSubjectRulesReviews.create`
  * `container.serviceAccounts.create`
  * `container.serviceAccounts.createToken`
  * `container.serviceAccounts.delete`
  * `container.serviceAccounts.get`
  * `container.serviceAccounts.list`
  * `container.serviceAccounts.update`
  * `container.services.create`
  * `container.services.delete`
  * `container.services.get`
  * `container.services.getStatus`
  * `container.services.list`
  * `container.services.proxy`
  * `container.services.update`
  * `container.services.updateStatus`
  * `container.statefulSets.create`
  * `container.statefulSets.delete`
  * `container.statefulSets.get`
  * `container.statefulSets.getScale`
  * `container.statefulSets.getStatus`
  * `container.statefulSets.list`
  * `container.statefulSets.update`
  * `container.statefulSets.updateScale`
  * `container.statefulSets.updateStatus`
  * `container.storageClasses.create`
  * `container.storageClasses.delete`
  * `container.storageClasses.get`
  * `container.storageClasses.list`
  * `container.storageClasses.update`
  * `container.storageStates.create`
  * `container.storageStates.delete`
  * `container.storageStates.get`
  * `container.storageStates.getStatus`
  * `container.storageStates.list`
  * `container.storageStates.update`
  * `container.storageStates.updateStatus`
  * `container.storageVersionMigrations.create`
  * `container.storageVersionMigrations.delete`
  * `container.storageVersionMigrations.get`
  * `container.storageVersionMigrations.getStatus`
  * `container.storageVersionMigrations.list`
  * `container.storageVersionMigrations.update`
  * `container.storageVersionMigrations.updateStatus`
  * `container.subjectAccessReviews.create`
  * `container.subjectAccessReviews.list`
  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`
  * `container.thirdPartyResources.create`
  * `container.thirdPartyResources.delete`
  * `container.thirdPartyResources.get`
  * `container.thirdPartyResources.list`
  * `container.thirdPartyResources.update`
  * `container.tokenReviews.create`
  * `container.updateInfos.create`
  * `container.updateInfos.delete`
  * `container.updateInfos.get`
  * `container.updateInfos.list`
  * `container.updateInfos.update`
  * `container.validatingWebhookConfigurations.create`
  * `container.validatingWebhookConfigurations.delete`
  * `container.validatingWebhookConfigurations.get`
  * `container.validatingWebhookConfigurations.list`
  * `container.validatingWebhookConfigurations.update`
  * `container.volumeAttachments.create`
  * `container.volumeAttachments.delete`
  * `container.volumeAttachments.get`
  * `container.volumeAttachments.getStatus`
  * `container.volumeAttachments.list`
  * `container.volumeAttachments.update`
  * `container.volumeAttachments.updateStatus`
  * `container.volumeSnapshotClasses.create`
  * `container.volumeSnapshotClasses.delete`
  * `container.volumeSnapshotClasses.get`
  * `container.volumeSnapshotClasses.list`
  * `container.volumeSnapshotClasses.update`
  * `container.volumeSnapshotContents.create`
  * `container.volumeSnapshotContents.delete`
  * `container.volumeSnapshotContents.get`
  * `container.volumeSnapshotContents.getStatus`
  * `container.volumeSnapshotContents.list`
  * `container.volumeSnapshotContents.update`
  * `container.volumeSnapshotContents.updateStatus`
  * `container.volumeSnapshots.create`
  * `container.volumeSnapshots.delete`
  * `container.volumeSnapshots.get`
  * `container.volumeSnapshots.getStatus`
  * `container.volumeSnapshots.list`
  * `container.volumeSnapshots.update`
  * `container.volumeSnapshots.updateStatus`

`containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `datalineage.events.create` `datalineage.locations.processOpenLineageMessage` `datalineage.processRevisions.insert` `datalineage.processes.create` `datalineage.processes.get` `datalineage.processes.markAsDeleted` `datalineage.processes.update` `datalineage.runs.create` `datalineage.runs.get` `datalineage.runs.update` `logging.logEntries.create` `logging.logEntries.list` `logging.logEntries.route` `logging.views.access` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`orgpolicy.policy.get` `pubsub.messageTransforms.validate` `pubsub.schemas.attach` `pubsub.schemas.commit` `pubsub.schemas.create` `pubsub.schemas.delete` `pubsub.schemas.get` `pubsub.schemas.getIamPolicy` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.rollback` `pubsub.schemas.validate` `pubsub.snapshots.create` `pubsub.snapshots.createTagBinding` `pubsub.snapshots.delete` `pubsub.snapshots.deleteTagBinding` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.snapshots.seek` `pubsub.snapshots.update` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.createTagBinding` `pubsub.subscriptions.delete` `pubsub.subscriptions.deleteTagBinding` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.createTagBinding` `pubsub.topics.delete` `pubsub.topics.deleteTagBinding` `pubsub.topics.detachSubscription` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `pubsub.topics.publish` `pubsub.topics.update` `pubsub.topics.updateTag` `recommender.containerDiagnosisInsights.*`

  * `recommender.containerDiagnosisInsights.get`
  * `recommender.containerDiagnosisInsights.list`
  * `recommender.containerDiagnosisInsights.update`

`recommender.containerDiagnosisRecommendations.*`

  * `recommender.containerDiagnosisRecommendations.get`
  * `recommender.containerDiagnosisRecommendations.list`
  * `recommender.containerDiagnosisRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.networkAnalyzerGkeConnectivityInsights.*`

  * `recommender.networkAnalyzerGkeConnectivityInsights.get`
  * `recommender.networkAnalyzerGkeConnectivityInsights.list`
  * `recommender.networkAnalyzerGkeConnectivityInsights.update`

`recommender.networkAnalyzerGkeIpAddressInsights.*`

  * `recommender.networkAnalyzerGkeIpAddressInsights.get`
  * `recommender.networkAnalyzerGkeIpAddressInsights.list`
  * `recommender.networkAnalyzerGkeIpAddressInsights.update`

`remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `source.repos.get` `source.repos.list` `storage.buckets.create` `storage.buckets.get` `storage.buckets.list` `storage.folders.*`

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

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Composer API Service Agent 

(`roles/composer.serviceAgent`) Cloud Composer API service agent can manage environments.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.applications.update` `appengine.instances.*`

  * `appengine.instances.delete`
  * `appengine.instances.enableDebug`
  * `appengine.instances.get`
  * `appengine.instances.list`

`appengine.memcache.addKey` `appengine.memcache.flush` `appengine.memcache.get` `appengine.memcache.update` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.runtimes.actAsAdmin` `appengine.services.*`

  * `appengine.services.delete`
  * `appengine.services.get`
  * `appengine.services.list`
  * `appengine.services.update`

`appengine.versions.create` `appengine.versions.delete` `appengine.versions.exportAppImage` `appengine.versions.get` `appengine.versions.list` `appengine.versions.update` `artifactregistry.projectsettings.get` `artifactregistry.repositories.create` `artifactregistry.repositories.delete` `artifactregistry.repositories.deleteArtifacts` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.update` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.get` `backupdr.backupPlanAssociations.createForCloudSqlInstance` `backupdr.backupPlanAssociations.createForComputeDisk` `backupdr.backupPlanAssociations.createForComputeInstance` `backupdr.backupPlanAssociations.deleteForCloudSqlInstance` `backupdr.backupPlanAssociations.deleteForComputeDisk` `backupdr.backupPlanAssociations.deleteForComputeInstance` `backupdr.backupPlanAssociations.fetchForCloudSqlInstance` `backupdr.backupPlanAssociations.fetchForComputeDisk` `backupdr.backupPlanAssociations.getForCloudSqlInstance` `backupdr.backupPlanAssociations.getForComputeDisk` `backupdr.backupPlanAssociations.list` `backupdr.backupPlanAssociations.triggerBackupForCloudSqlInstance` `backupdr.backupPlanAssociations.triggerBackupForComputeDisk` `backupdr.backupPlanAssociations.triggerBackupForComputeInstance` `backupdr.backupPlanAssociations.updateForCloudSqlInstance` `backupdr.backupPlanAssociations.updateForComputeDisk` `backupdr.backupPlanAssociations.updateForComputeInstance` `backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupPlans.useForCloudSqlInstance` `backupdr.backupPlans.useForComputeDisk` `backupdr.backupPlans.useForComputeInstance` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.bvbackups.fetchForCloudSqlInstance` `backupdr.bvbackups.useReadOnlyForCloudSqlInstance` `backupdr.bvdataSources.useReadOnlyForCloudSqlInstance` `backupdr.dataSourceReferences.fetchForCloudSqlInstance` `backupdr.dataSourceReferences.getForCloudSqlInstance` `backupdr.locations.list` `backupdr.operations.get` `backupdr.operations.list` `backupdr.serviceConfig.initialize` `cloudaicompanion.companions.*`

  * `cloudaicompanion.companions.generateChat`
  * `cloudaicompanion.companions.generateCode`

`cloudaicompanion.entitlements.get` `cloudaicompanion.instances.completeCode` `cloudaicompanion.instances.completeTask` `cloudaicompanion.instances.generateCode` `cloudnotifications.activities.list` `cloudsql.*`

  * `cloudsql.backupRuns.create`
  * `cloudsql.backupRuns.delete`
  * `cloudsql.backupRuns.export`
  * `cloudsql.backupRuns.get`
  * `cloudsql.backupRuns.list`
  * `cloudsql.backupRuns.update`
  * `cloudsql.blueGreenDeployments.create`
  * `cloudsql.blueGreenDeployments.delete`
  * `cloudsql.blueGreenDeployments.get`
  * `cloudsql.blueGreenDeployments.list`
  * `cloudsql.blueGreenDeployments.switchover`
  * `cloudsql.databases.create`
  * `cloudsql.databases.delete`
  * `cloudsql.databases.get`
  * `cloudsql.databases.list`
  * `cloudsql.databases.update`
  * `cloudsql.instances.addEntraIdCertificate`
  * `cloudsql.instances.addServerCa`
  * `cloudsql.instances.addServerCertificate`
  * `cloudsql.instances.cancelAgentSession`
  * `cloudsql.instances.clone`
  * `cloudsql.instances.connect`
  * `cloudsql.instances.create`
  * `cloudsql.instances.createBackupDrBackup`
  * `cloudsql.instances.createTagBinding`
  * `cloudsql.instances.createTestingAgentSession`
  * `cloudsql.instances.delete`
  * `cloudsql.instances.deleteTagBinding`
  * `cloudsql.instances.demoteMaster`
  * `cloudsql.instances.executeSql`
  * `cloudsql.instances.export`
  * `cloudsql.instances.failover`
  * `cloudsql.instances.get`
  * `cloudsql.instances.getAgentSession`
  * `cloudsql.instances.getDiskShrinkConfig`
  * `cloudsql.instances.import`
  * `cloudsql.instances.list`
  * `cloudsql.instances.listAgentSessions`
  * `cloudsql.instances.listEffectiveTags`
  * `cloudsql.instances.listEntraIdCertificates`
  * `cloudsql.instances.listServerCas`
  * `cloudsql.instances.listServerCertificates`
  * `cloudsql.instances.listTagBindings`
  * `cloudsql.instances.login`
  * `cloudsql.instances.manageEncryption`
  * `cloudsql.instances.migrate`
  * `cloudsql.instances.performDiskShrink`
  * `cloudsql.instances.preCheckMajorVersionUpgrade`
  * `cloudsql.instances.promoteReplica`
  * `cloudsql.instances.reencrypt`
  * `cloudsql.instances.resetReplicaSize`
  * `cloudsql.instances.resetSslConfig`
  * `cloudsql.instances.restart`
  * `cloudsql.instances.restoreBackup`
  * `cloudsql.instances.rotateEntraIdCertificate`
  * `cloudsql.instances.rotateServerCa`
  * `cloudsql.instances.rotateServerCertificate`
  * `cloudsql.instances.startReplica`
  * `cloudsql.instances.stopReplica`
  * `cloudsql.instances.truncateLog`
  * `cloudsql.instances.update`
  * `cloudsql.instances.updateBackupDrConfig`
  * `cloudsql.schemas.view`
  * `cloudsql.sslCerts.create`
  * `cloudsql.sslCerts.delete`
  * `cloudsql.sslCerts.get`
  * `cloudsql.sslCerts.list`
  * `cloudsql.users.create`
  * `cloudsql.users.delete`
  * `cloudsql.users.get`
  * `cloudsql.users.list`
  * `cloudsql.users.update`
  * `cloudsql.workloadCaptures.list`
  * `cloudsql.workloadCaptures.start`
  * `cloudsql.workloadCaptures.startReplay`
  * `cloudsql.workloadCaptures.stop`
  * `cloudsql.workloadCaptures.stopReplay`

`composer.dags.get` `composer.environments.get` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.*`

  * `compute.addresses.create`
  * `compute.addresses.createInternal`
  * `compute.addresses.createTagBinding`
  * `compute.addresses.delete`
  * `compute.addresses.deleteInternal`
  * `compute.addresses.deleteTagBinding`
  * `compute.addresses.get`
  * `compute.addresses.list`
  * `compute.addresses.listEffectiveTags`
  * `compute.addresses.listTagBindings`
  * `compute.addresses.setLabels`
  * `compute.addresses.use`
  * `compute.addresses.useInternal`

`compute.autoscalers.*`

  * `compute.autoscalers.create`
  * `compute.autoscalers.delete`
  * `compute.autoscalers.get`
  * `compute.autoscalers.list`
  * `compute.autoscalers.update`

`compute.backendBuckets.*`

  * `compute.backendBuckets.addSignedUrlKey`
  * `compute.backendBuckets.create`
  * `compute.backendBuckets.createTagBinding`
  * `compute.backendBuckets.delete`
  * `compute.backendBuckets.deleteSignedUrlKey`
  * `compute.backendBuckets.deleteTagBinding`
  * `compute.backendBuckets.get`
  * `compute.backendBuckets.getIamPolicy`
  * `compute.backendBuckets.list`
  * `compute.backendBuckets.listEffectiveTags`
  * `compute.backendBuckets.listTagBindings`
  * `compute.backendBuckets.setIamPolicy`
  * `compute.backendBuckets.setSecurityPolicy`
  * `compute.backendBuckets.update`
  * `compute.backendBuckets.use`

`compute.backendServices.*`

  * `compute.backendServices.addSignedUrlKey`
  * `compute.backendServices.create`
  * `compute.backendServices.createTagBinding`
  * `compute.backendServices.delete`
  * `compute.backendServices.deleteSignedUrlKey`
  * `compute.backendServices.deleteTagBinding`
  * `compute.backendServices.get`
  * `compute.backendServices.getIamPolicy`
  * `compute.backendServices.list`
  * `compute.backendServices.listEffectiveTags`
  * `compute.backendServices.listTagBindings`
  * `compute.backendServices.setIamPolicy`
  * `compute.backendServices.setSecurityPolicy`
  * `compute.backendServices.update`
  * `compute.backendServices.use`

`compute.crossSiteNetworks.*`

  * `compute.crossSiteNetworks.create`
  * `compute.crossSiteNetworks.delete`
  * `compute.crossSiteNetworks.get`
  * `compute.crossSiteNetworks.list`
  * `compute.crossSiteNetworks.update`

`compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.*`

  * `compute.disks.addResourcePolicies`
  * `compute.disks.create`
  * `compute.disks.createSnapshot`
  * `compute.disks.createTagBinding`
  * `compute.disks.delete`
  * `compute.disks.deleteTagBinding`
  * `compute.disks.get`
  * `compute.disks.getIamPolicy`
  * `compute.disks.list`
  * `compute.disks.listEffectiveTags`
  * `compute.disks.listTagBindings`
  * `compute.disks.removeResourcePolicies`
  * `compute.disks.resize`
  * `compute.disks.setIamPolicy`
  * `compute.disks.setLabels`
  * `compute.disks.startAsyncReplication`
  * `compute.disks.stopAsyncReplication`
  * `compute.disks.stopGroupAsyncReplication`
  * `compute.disks.update`
  * `compute.disks.updateKmsKey`
  * `compute.disks.use`
  * `compute.disks.useReadOnly`

`compute.externalVpnGateways.*`

  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.createTagBinding`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.deleteTagBinding`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.listEffectiveTags`
  * `compute.externalVpnGateways.listTagBindings`
  * `compute.externalVpnGateways.setLabels`
  * `compute.externalVpnGateways.use`

`compute.firewallPolicies.get` `compute.firewallPolicies.list` `compute.firewallPolicies.listEffectiveTags` `compute.firewallPolicies.listTagBindings` `compute.firewallPolicies.use` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.forwardingRules.*`

  * `compute.forwardingRules.create`
  * `compute.forwardingRules.createTagBinding`
  * `compute.forwardingRules.delete`
  * `compute.forwardingRules.deleteTagBinding`
  * `compute.forwardingRules.get`
  * `compute.forwardingRules.list`
  * `compute.forwardingRules.listEffectiveTags`
  * `compute.forwardingRules.listTagBindings`
  * `compute.forwardingRules.pscCreate`
  * `compute.forwardingRules.pscDelete`
  * `compute.forwardingRules.pscSetLabels`
  * `compute.forwardingRules.pscUpdate`
  * `compute.forwardingRules.setLabels`
  * `compute.forwardingRules.setTarget`
  * `compute.forwardingRules.update`
  * `compute.forwardingRules.use`

`compute.globalAddresses.*`

  * `compute.globalAddresses.create`
  * `compute.globalAddresses.createInternal`
  * `compute.globalAddresses.createTagBinding`
  * `compute.globalAddresses.delete`
  * `compute.globalAddresses.deleteInternal`
  * `compute.globalAddresses.deleteTagBinding`
  * `compute.globalAddresses.get`
  * `compute.globalAddresses.list`
  * `compute.globalAddresses.listEffectiveTags`
  * `compute.globalAddresses.listTagBindings`
  * `compute.globalAddresses.setLabels`
  * `compute.globalAddresses.use`

`compute.globalForwardingRules.*`

  * `compute.globalForwardingRules.create`
  * `compute.globalForwardingRules.createTagBinding`
  * `compute.globalForwardingRules.delete`
  * `compute.globalForwardingRules.deleteTagBinding`
  * `compute.globalForwardingRules.get`
  * `compute.globalForwardingRules.list`
  * `compute.globalForwardingRules.listEffectiveTags`
  * `compute.globalForwardingRules.listTagBindings`
  * `compute.globalForwardingRules.pscCreate`
  * `compute.globalForwardingRules.pscDelete`
  * `compute.globalForwardingRules.pscSetLabels`
  * `compute.globalForwardingRules.pscUpdate`
  * `compute.globalForwardingRules.setLabels`
  * `compute.globalForwardingRules.setTarget`
  * `compute.globalForwardingRules.update`

`compute.globalFrontendSettings.*`

  * `compute.globalFrontendSettings.get`
  * `compute.globalFrontendSettings.update`

`compute.globalNetworkEndpointGroups.*`

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

`compute.globalOperations.get` `compute.globalOperations.list` `compute.globalPublicDelegatedPrefixes.delete` `compute.globalPublicDelegatedPrefixes.get` `compute.globalPublicDelegatedPrefixes.list` `compute.globalPublicDelegatedPrefixes.updatePolicy` `compute.healthChecks.*`

  * `compute.healthChecks.create`
  * `compute.healthChecks.createTagBinding`
  * `compute.healthChecks.delete`
  * `compute.healthChecks.deleteTagBinding`
  * `compute.healthChecks.get`
  * `compute.healthChecks.list`
  * `compute.healthChecks.listEffectiveTags`
  * `compute.healthChecks.listTagBindings`
  * `compute.healthChecks.update`
  * `compute.healthChecks.use`
  * `compute.healthChecks.useReadOnly`

`compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.httpHealthChecks.*`

  * `compute.httpHealthChecks.create`
  * `compute.httpHealthChecks.createTagBinding`
  * `compute.httpHealthChecks.delete`
  * `compute.httpHealthChecks.deleteTagBinding`
  * `compute.httpHealthChecks.get`
  * `compute.httpHealthChecks.list`
  * `compute.httpHealthChecks.listEffectiveTags`
  * `compute.httpHealthChecks.listTagBindings`
  * `compute.httpHealthChecks.update`
  * `compute.httpHealthChecks.use`
  * `compute.httpHealthChecks.useReadOnly`

`compute.httpsHealthChecks.*`

  * `compute.httpsHealthChecks.create`
  * `compute.httpsHealthChecks.createTagBinding`
  * `compute.httpsHealthChecks.delete`
  * `compute.httpsHealthChecks.deleteTagBinding`
  * `compute.httpsHealthChecks.get`
  * `compute.httpsHealthChecks.list`
  * `compute.httpsHealthChecks.listEffectiveTags`
  * `compute.httpsHealthChecks.listTagBindings`
  * `compute.httpsHealthChecks.update`
  * `compute.httpsHealthChecks.use`
  * `compute.httpsHealthChecks.useReadOnly`

`compute.images.*`

  * `compute.images.create`
  * `compute.images.createTagBinding`
  * `compute.images.delete`
  * `compute.images.deleteTagBinding`
  * `compute.images.deprecate`
  * `compute.images.get`
  * `compute.images.getFromFamily`
  * `compute.images.getIamPolicy`
  * `compute.images.list`
  * `compute.images.listEffectiveTags`
  * `compute.images.listTagBindings`
  * `compute.images.setIamPolicy`
  * `compute.images.setLabels`
  * `compute.images.update`
  * `compute.images.useReadOnly`

`compute.instanceGroupManagers.*`

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

`compute.instanceSettings.*`

  * `compute.instanceSettings.get`
  * `compute.instanceSettings.update`

`compute.instanceTemplates.*`

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

`compute.instantSnapshotGroups.*`

  * `compute.instantSnapshotGroups.create`
  * `compute.instantSnapshotGroups.delete`
  * `compute.instantSnapshotGroups.get`
  * `compute.instantSnapshotGroups.getIamPolicy`
  * `compute.instantSnapshotGroups.list`
  * `compute.instantSnapshotGroups.setIamPolicy`
  * `compute.instantSnapshotGroups.useReadOnly`

`compute.instantSnapshots.create` `compute.instantSnapshots.delete` `compute.instantSnapshots.export` `compute.instantSnapshots.get` `compute.instantSnapshots.getIamPolicy` `compute.instantSnapshots.list` `compute.instantSnapshots.listEffectiveTags` `compute.instantSnapshots.listTagBindings` `compute.instantSnapshots.setIamPolicy` `compute.instantSnapshots.setLabels` `compute.instantSnapshots.useReadOnly` `compute.interconnectAttachmentGroups.*`

  * `compute.interconnectAttachmentGroups.create`
  * `compute.interconnectAttachmentGroups.delete`
  * `compute.interconnectAttachmentGroups.get`
  * `compute.interconnectAttachmentGroups.list`
  * `compute.interconnectAttachmentGroups.patch`

`compute.interconnectAttachments.*`

  * `compute.interconnectAttachments.create`
  * `compute.interconnectAttachments.createTagBinding`
  * `compute.interconnectAttachments.delete`
  * `compute.interconnectAttachments.deleteTagBinding`
  * `compute.interconnectAttachments.get`
  * `compute.interconnectAttachments.list`
  * `compute.interconnectAttachments.listEffectiveTags`
  * `compute.interconnectAttachments.listTagBindings`
  * `compute.interconnectAttachments.setLabels`
  * `compute.interconnectAttachments.update`
  * `compute.interconnectAttachments.use`

`compute.interconnectGroups.*`

  * `compute.interconnectGroups.create`
  * `compute.interconnectGroups.delete`
  * `compute.interconnectGroups.get`
  * `compute.interconnectGroups.list`
  * `compute.interconnectGroups.patch`

`compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.*`

  * `compute.interconnects.create`
  * `compute.interconnects.createTagBinding`
  * `compute.interconnects.delete`
  * `compute.interconnects.deleteTagBinding`
  * `compute.interconnects.get`
  * `compute.interconnects.getMacsecConfig`
  * `compute.interconnects.list`
  * `compute.interconnects.listEffectiveTags`
  * `compute.interconnects.listTagBindings`
  * `compute.interconnects.setLabels`
  * `compute.interconnects.setName`
  * `compute.interconnects.update`
  * `compute.interconnects.use`

`compute.licenseCodes.*`

  * `compute.licenseCodes.get`
  * `compute.licenseCodes.getIamPolicy`
  * `compute.licenseCodes.list`
  * `compute.licenseCodes.setIamPolicy`

`compute.licenses.create` `compute.licenses.delete` `compute.licenses.get` `compute.licenses.getIamPolicy` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.licenses.setIamPolicy` `compute.licenses.update` `compute.machineImages.create` `compute.machineImages.delete` `compute.machineImages.get` `compute.machineImages.getIamPolicy` `compute.machineImages.list` `compute.machineImages.listEffectiveTags` `compute.machineImages.listTagBindings` `compute.machineImages.setIamPolicy` `compute.machineImages.setLabels` `compute.machineImages.useReadOnly` `compute.machineTypes.*`

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

`compute.networkAttachments.*`

  * `compute.networkAttachments.create`
  * `compute.networkAttachments.createTagBinding`
  * `compute.networkAttachments.delete`
  * `compute.networkAttachments.deleteTagBinding`
  * `compute.networkAttachments.get`
  * `compute.networkAttachments.getIamPolicy`
  * `compute.networkAttachments.list`
  * `compute.networkAttachments.listEffectiveTags`
  * `compute.networkAttachments.listTagBindings`
  * `compute.networkAttachments.setIamPolicy`
  * `compute.networkAttachments.update`
  * `compute.networkAttachments.use`

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

`compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.*`

  * `compute.networks.access`
  * `compute.networks.addPeering`
  * `compute.networks.create`
  * `compute.networks.createTagBinding`
  * `compute.networks.delete`
  * `compute.networks.deleteTagBinding`
  * `compute.networks.get`
  * `compute.networks.getEffectiveFirewalls`
  * `compute.networks.getRegionEffectiveFirewalls`
  * `compute.networks.list`
  * `compute.networks.listEffectiveTags`
  * `compute.networks.listPeeringRoutes`
  * `compute.networks.listTagBindings`
  * `compute.networks.mirror`
  * `compute.networks.removePeering`
  * `compute.networks.setFirewallPolicy`
  * `compute.networks.setNetworkPolicy`
  * `compute.networks.switchToCustomMode`
  * `compute.networks.update`
  * `compute.networks.updatePeering`
  * `compute.networks.updatePolicy`
  * `compute.networks.use`
  * `compute.networks.useExternalIp`

`compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.packetMirrorings.listEffectiveTags` `compute.packetMirrorings.listTagBindings` `compute.projects.get` `compute.projects.setCommonInstanceMetadata` `compute.publicDelegatedPrefixes.delete` `compute.publicDelegatedPrefixes.get` `compute.publicDelegatedPrefixes.list` `compute.publicDelegatedPrefixes.listEffectiveTags` `compute.publicDelegatedPrefixes.listTagBindings` `compute.publicDelegatedPrefixes.update` `compute.publicDelegatedPrefixes.updatePolicy` `compute.recoverableSnapshots.*`

  * `compute.recoverableSnapshots.delete`
  * `compute.recoverableSnapshots.get`
  * `compute.recoverableSnapshots.getIamPolicy`
  * `compute.recoverableSnapshots.list`
  * `compute.recoverableSnapshots.recover`
  * `compute.recoverableSnapshots.setIamPolicy`

`compute.regionBackendBuckets.*`

  * `compute.regionBackendBuckets.create`
  * `compute.regionBackendBuckets.createTagBinding`
  * `compute.regionBackendBuckets.delete`
  * `compute.regionBackendBuckets.deleteTagBinding`
  * `compute.regionBackendBuckets.get`
  * `compute.regionBackendBuckets.getIamPolicy`
  * `compute.regionBackendBuckets.list`
  * `compute.regionBackendBuckets.listEffectiveTags`
  * `compute.regionBackendBuckets.listTagBindings`
  * `compute.regionBackendBuckets.setIamPolicy`
  * `compute.regionBackendBuckets.update`
  * `compute.regionBackendBuckets.use`

`compute.regionBackendServices.*`

  * `compute.regionBackendServices.create`
  * `compute.regionBackendServices.createTagBinding`
  * `compute.regionBackendServices.delete`
  * `compute.regionBackendServices.deleteTagBinding`
  * `compute.regionBackendServices.get`
  * `compute.regionBackendServices.getIamPolicy`
  * `compute.regionBackendServices.list`
  * `compute.regionBackendServices.listEffectiveTags`
  * `compute.regionBackendServices.listTagBindings`
  * `compute.regionBackendServices.setIamPolicy`
  * `compute.regionBackendServices.setSecurityPolicy`
  * `compute.regionBackendServices.update`
  * `compute.regionBackendServices.use`

`compute.regionCompositeHealthChecks.*`

  * `compute.regionCompositeHealthChecks.create`
  * `compute.regionCompositeHealthChecks.delete`
  * `compute.regionCompositeHealthChecks.get`
  * `compute.regionCompositeHealthChecks.list`
  * `compute.regionCompositeHealthChecks.update`

`compute.regionFirewallPolicies.get` `compute.regionFirewallPolicies.list` `compute.regionFirewallPolicies.listEffectiveTags` `compute.regionFirewallPolicies.listTagBindings` `compute.regionFirewallPolicies.use` `compute.regionHealthAggregationPolicies.*`

  * `compute.regionHealthAggregationPolicies.create`
  * `compute.regionHealthAggregationPolicies.delete`
  * `compute.regionHealthAggregationPolicies.get`
  * `compute.regionHealthAggregationPolicies.list`
  * `compute.regionHealthAggregationPolicies.update`

`compute.regionHealthCheckServices.*`

  * `compute.regionHealthCheckServices.create`
  * `compute.regionHealthCheckServices.delete`
  * `compute.regionHealthCheckServices.get`
  * `compute.regionHealthCheckServices.list`
  * `compute.regionHealthCheckServices.update`
  * `compute.regionHealthCheckServices.use`

`compute.regionHealthChecks.*`

  * `compute.regionHealthChecks.create`
  * `compute.regionHealthChecks.createTagBinding`
  * `compute.regionHealthChecks.delete`
  * `compute.regionHealthChecks.deleteTagBinding`
  * `compute.regionHealthChecks.get`
  * `compute.regionHealthChecks.list`
  * `compute.regionHealthChecks.listEffectiveTags`
  * `compute.regionHealthChecks.listTagBindings`
  * `compute.regionHealthChecks.update`
  * `compute.regionHealthChecks.use`
  * `compute.regionHealthChecks.useReadOnly`

`compute.regionHealthSources.*`

  * `compute.regionHealthSources.create`
  * `compute.regionHealthSources.delete`
  * `compute.regionHealthSources.get`
  * `compute.regionHealthSources.list`
  * `compute.regionHealthSources.update`

`compute.regionNetworkEndpointGroups.*`

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

`compute.regionNetworkPolicies.*`

  * `compute.regionNetworkPolicies.create`
  * `compute.regionNetworkPolicies.delete`
  * `compute.regionNetworkPolicies.get`
  * `compute.regionNetworkPolicies.list`
  * `compute.regionNetworkPolicies.update`
  * `compute.regionNetworkPolicies.use`

`compute.regionNotificationEndpoints.*`

  * `compute.regionNotificationEndpoints.create`
  * `compute.regionNotificationEndpoints.delete`
  * `compute.regionNotificationEndpoints.get`
  * `compute.regionNotificationEndpoints.list`
  * `compute.regionNotificationEndpoints.update`
  * `compute.regionNotificationEndpoints.use`

`compute.regionOperations.get` `compute.regionOperations.list` `compute.regionSecurityPolicies.get` `compute.regionSecurityPolicies.list` `compute.regionSecurityPolicies.listEffectiveTags` `compute.regionSecurityPolicies.listTagBindings` `compute.regionSecurityPolicies.use` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.*`

  * `compute.regionSslPolicies.create`
  * `compute.regionSslPolicies.createTagBinding`
  * `compute.regionSslPolicies.delete`
  * `compute.regionSslPolicies.deleteTagBinding`
  * `compute.regionSslPolicies.get`
  * `compute.regionSslPolicies.getIamPolicy`
  * `compute.regionSslPolicies.list`
  * `compute.regionSslPolicies.listAvailableFeatures`
  * `compute.regionSslPolicies.listEffectiveTags`
  * `compute.regionSslPolicies.listTagBindings`
  * `compute.regionSslPolicies.setIamPolicy`
  * `compute.regionSslPolicies.update`
  * `compute.regionSslPolicies.use`

`compute.regionTargetHttpProxies.*`

  * `compute.regionTargetHttpProxies.create`
  * `compute.regionTargetHttpProxies.createTagBinding`
  * `compute.regionTargetHttpProxies.delete`
  * `compute.regionTargetHttpProxies.deleteTagBinding`
  * `compute.regionTargetHttpProxies.get`
  * `compute.regionTargetHttpProxies.list`
  * `compute.regionTargetHttpProxies.listEffectiveTags`
  * `compute.regionTargetHttpProxies.listTagBindings`
  * `compute.regionTargetHttpProxies.setUrlMap`
  * `compute.regionTargetHttpProxies.use`

`compute.regionTargetHttpsProxies.*`

  * `compute.regionTargetHttpsProxies.create`
  * `compute.regionTargetHttpsProxies.createTagBinding`
  * `compute.regionTargetHttpsProxies.delete`
  * `compute.regionTargetHttpsProxies.deleteTagBinding`
  * `compute.regionTargetHttpsProxies.get`
  * `compute.regionTargetHttpsProxies.list`
  * `compute.regionTargetHttpsProxies.listEffectiveTags`
  * `compute.regionTargetHttpsProxies.listTagBindings`
  * `compute.regionTargetHttpsProxies.setSslCertificates`
  * `compute.regionTargetHttpsProxies.setUrlMap`
  * `compute.regionTargetHttpsProxies.update`
  * `compute.regionTargetHttpsProxies.use`

`compute.regionTargetTcpProxies.*`

  * `compute.regionTargetTcpProxies.attach`
  * `compute.regionTargetTcpProxies.create`
  * `compute.regionTargetTcpProxies.createTagBinding`
  * `compute.regionTargetTcpProxies.delete`
  * `compute.regionTargetTcpProxies.deleteTagBinding`
  * `compute.regionTargetTcpProxies.get`
  * `compute.regionTargetTcpProxies.list`
  * `compute.regionTargetTcpProxies.listEffectiveTags`
  * `compute.regionTargetTcpProxies.listTagBindings`
  * `compute.regionTargetTcpProxies.use`

`compute.regionUrlMaps.*`

  * `compute.regionUrlMaps.create`
  * `compute.regionUrlMaps.createTagBinding`
  * `compute.regionUrlMaps.delete`
  * `compute.regionUrlMaps.deleteTagBinding`
  * `compute.regionUrlMaps.get`
  * `compute.regionUrlMaps.invalidateCache`
  * `compute.regionUrlMaps.list`
  * `compute.regionUrlMaps.listEffectiveTags`
  * `compute.regionUrlMaps.listTagBindings`
  * `compute.regionUrlMaps.update`
  * `compute.regionUrlMaps.use`
  * `compute.regionUrlMaps.validate`

`compute.regions.*`

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

`compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.*`

  * `compute.resourcePolicies.create`
  * `compute.resourcePolicies.delete`
  * `compute.resourcePolicies.get`
  * `compute.resourcePolicies.getIamPolicy`
  * `compute.resourcePolicies.list`
  * `compute.resourcePolicies.setIamPolicy`
  * `compute.resourcePolicies.update`
  * `compute.resourcePolicies.use`
  * `compute.resourcePolicies.useReadOnly`

`compute.routers.*`

  * `compute.routers.create`
  * `compute.routers.createTagBinding`
  * `compute.routers.delete`
  * `compute.routers.deleteRoutePolicy`
  * `compute.routers.deleteTagBinding`
  * `compute.routers.get`
  * `compute.routers.getRoutePolicy`
  * `compute.routers.list`
  * `compute.routers.listBgpRoutes`
  * `compute.routers.listEffectiveTags`
  * `compute.routers.listRoutePolicies`
  * `compute.routers.listTagBindings`
  * `compute.routers.update`
  * `compute.routers.updateRoutePolicy`
  * `compute.routers.use`

`compute.routes.*`

  * `compute.routes.create`
  * `compute.routes.createTagBinding`
  * `compute.routes.delete`
  * `compute.routes.deleteTagBinding`
  * `compute.routes.get`
  * `compute.routes.list`
  * `compute.routes.listEffectiveTags`
  * `compute.routes.listTagBindings`

`compute.securityPolicies.get` `compute.securityPolicies.list` `compute.securityPolicies.listEffectiveTags` `compute.securityPolicies.listTagBindings` `compute.securityPolicies.use` `compute.serviceAttachments.*`

  * `compute.serviceAttachments.create`
  * `compute.serviceAttachments.createTagBinding`
  * `compute.serviceAttachments.delete`
  * `compute.serviceAttachments.deleteTagBinding`
  * `compute.serviceAttachments.get`
  * `compute.serviceAttachments.getIamPolicy`
  * `compute.serviceAttachments.list`
  * `compute.serviceAttachments.listEffectiveTags`
  * `compute.serviceAttachments.listTagBindings`
  * `compute.serviceAttachments.setIamPolicy`
  * `compute.serviceAttachments.update`
  * `compute.serviceAttachments.use`

`compute.snapshotGroups.*`

  * `compute.snapshotGroups.create`
  * `compute.snapshotGroups.delete`
  * `compute.snapshotGroups.get`
  * `compute.snapshotGroups.getIamPolicy`
  * `compute.snapshotGroups.list`
  * `compute.snapshotGroups.setIamPolicy`
  * `compute.snapshotGroups.useReadOnly`

`compute.snapshots.*`

  * `compute.snapshots.create`
  * `compute.snapshots.createTagBinding`
  * `compute.snapshots.delete`
  * `compute.snapshots.deleteTagBinding`
  * `compute.snapshots.get`
  * `compute.snapshots.getEffectiveRecycleBinRule`
  * `compute.snapshots.getIamPolicy`
  * `compute.snapshots.list`
  * `compute.snapshots.listEffectiveTags`
  * `compute.snapshots.listTagBindings`
  * `compute.snapshots.setIamPolicy`
  * `compute.snapshots.setLabels`
  * `compute.snapshots.updateKmsKey`
  * `compute.snapshots.useReadOnly`

`compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.*`

  * `compute.sslPolicies.create`
  * `compute.sslPolicies.createTagBinding`
  * `compute.sslPolicies.delete`
  * `compute.sslPolicies.deleteTagBinding`
  * `compute.sslPolicies.get`
  * `compute.sslPolicies.getIamPolicy`
  * `compute.sslPolicies.list`
  * `compute.sslPolicies.listAvailableFeatures`
  * `compute.sslPolicies.listEffectiveTags`
  * `compute.sslPolicies.listTagBindings`
  * `compute.sslPolicies.setIamPolicy`
  * `compute.sslPolicies.update`
  * `compute.sslPolicies.use`

`compute.storagePools.get` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.storagePools.use` `compute.subnetworks.*`

  * `compute.subnetworks.create`
  * `compute.subnetworks.createTagBinding`
  * `compute.subnetworks.delete`
  * `compute.subnetworks.deleteTagBinding`
  * `compute.subnetworks.expandIpCidrRange`
  * `compute.subnetworks.get`
  * `compute.subnetworks.getIamPolicy`
  * `compute.subnetworks.list`
  * `compute.subnetworks.listEffectiveTags`
  * `compute.subnetworks.listTagBindings`
  * `compute.subnetworks.mirror`
  * `compute.subnetworks.setIamPolicy`
  * `compute.subnetworks.setPrivateIpGoogleAccess`
  * `compute.subnetworks.update`
  * `compute.subnetworks.use`
  * `compute.subnetworks.useExternalIp`
  * `compute.subnetworks.usePeerMigration`

`compute.targetGrpcProxies.*`

  * `compute.targetGrpcProxies.create`
  * `compute.targetGrpcProxies.createTagBinding`
  * `compute.targetGrpcProxies.delete`
  * `compute.targetGrpcProxies.deleteTagBinding`
  * `compute.targetGrpcProxies.get`
  * `compute.targetGrpcProxies.list`
  * `compute.targetGrpcProxies.listEffectiveTags`
  * `compute.targetGrpcProxies.listTagBindings`
  * `compute.targetGrpcProxies.update`
  * `compute.targetGrpcProxies.use`

`compute.targetHttpProxies.*`

  * `compute.targetHttpProxies.create`
  * `compute.targetHttpProxies.createTagBinding`
  * `compute.targetHttpProxies.delete`
  * `compute.targetHttpProxies.deleteTagBinding`
  * `compute.targetHttpProxies.get`
  * `compute.targetHttpProxies.list`
  * `compute.targetHttpProxies.listEffectiveTags`
  * `compute.targetHttpProxies.listTagBindings`
  * `compute.targetHttpProxies.setUrlMap`
  * `compute.targetHttpProxies.update`
  * `compute.targetHttpProxies.use`

`compute.targetHttpsProxies.*`

  * `compute.targetHttpsProxies.create`
  * `compute.targetHttpsProxies.createTagBinding`
  * `compute.targetHttpsProxies.delete`
  * `compute.targetHttpsProxies.deleteTagBinding`
  * `compute.targetHttpsProxies.get`
  * `compute.targetHttpsProxies.list`
  * `compute.targetHttpsProxies.listEffectiveTags`
  * `compute.targetHttpsProxies.listTagBindings`
  * `compute.targetHttpsProxies.setCertificateMap`
  * `compute.targetHttpsProxies.setQuicOverride`
  * `compute.targetHttpsProxies.setSslCertificates`
  * `compute.targetHttpsProxies.setSslPolicy`
  * `compute.targetHttpsProxies.setUrlMap`
  * `compute.targetHttpsProxies.update`
  * `compute.targetHttpsProxies.use`

`compute.targetInstances.*`

  * `compute.targetInstances.create`
  * `compute.targetInstances.createTagBinding`
  * `compute.targetInstances.delete`
  * `compute.targetInstances.deleteTagBinding`
  * `compute.targetInstances.get`
  * `compute.targetInstances.list`
  * `compute.targetInstances.listEffectiveTags`
  * `compute.targetInstances.listTagBindings`
  * `compute.targetInstances.setSecurityPolicy`
  * `compute.targetInstances.use`

`compute.targetPools.*`

  * `compute.targetPools.addHealthCheck`
  * `compute.targetPools.addInstance`
  * `compute.targetPools.create`
  * `compute.targetPools.createTagBinding`
  * `compute.targetPools.delete`
  * `compute.targetPools.deleteTagBinding`
  * `compute.targetPools.get`
  * `compute.targetPools.list`
  * `compute.targetPools.listEffectiveTags`
  * `compute.targetPools.listTagBindings`
  * `compute.targetPools.removeHealthCheck`
  * `compute.targetPools.removeInstance`
  * `compute.targetPools.setSecurityPolicy`
  * `compute.targetPools.update`
  * `compute.targetPools.use`

`compute.targetSslProxies.*`

  * `compute.targetSslProxies.create`
  * `compute.targetSslProxies.createTagBinding`
  * `compute.targetSslProxies.delete`
  * `compute.targetSslProxies.deleteTagBinding`
  * `compute.targetSslProxies.get`
  * `compute.targetSslProxies.list`
  * `compute.targetSslProxies.listEffectiveTags`
  * `compute.targetSslProxies.listTagBindings`
  * `compute.targetSslProxies.setBackendService`
  * `compute.targetSslProxies.setCertificateMap`
  * `compute.targetSslProxies.setProxyHeader`
  * `compute.targetSslProxies.setSslCertificates`
  * `compute.targetSslProxies.setSslPolicy`
  * `compute.targetSslProxies.update`
  * `compute.targetSslProxies.use`

`compute.targetTcpProxies.*`

  * `compute.targetTcpProxies.attach`
  * `compute.targetTcpProxies.create`
  * `compute.targetTcpProxies.createTagBinding`
  * `compute.targetTcpProxies.delete`
  * `compute.targetTcpProxies.deleteTagBinding`
  * `compute.targetTcpProxies.get`
  * `compute.targetTcpProxies.list`
  * `compute.targetTcpProxies.listEffectiveTags`
  * `compute.targetTcpProxies.listTagBindings`
  * `compute.targetTcpProxies.update`
  * `compute.targetTcpProxies.use`

`compute.targetVpnGateways.*`

  * `compute.targetVpnGateways.create`
  * `compute.targetVpnGateways.createTagBinding`
  * `compute.targetVpnGateways.delete`
  * `compute.targetVpnGateways.deleteTagBinding`
  * `compute.targetVpnGateways.get`
  * `compute.targetVpnGateways.list`
  * `compute.targetVpnGateways.listEffectiveTags`
  * `compute.targetVpnGateways.listTagBindings`
  * `compute.targetVpnGateways.setLabels`
  * `compute.targetVpnGateways.use`

`compute.urlMaps.*`

  * `compute.urlMaps.create`
  * `compute.urlMaps.createTagBinding`
  * `compute.urlMaps.delete`
  * `compute.urlMaps.deleteTagBinding`
  * `compute.urlMaps.get`
  * `compute.urlMaps.invalidateCache`
  * `compute.urlMaps.list`
  * `compute.urlMaps.listEffectiveTags`
  * `compute.urlMaps.listTagBindings`
  * `compute.urlMaps.update`
  * `compute.urlMaps.use`
  * `compute.urlMaps.validate`

`compute.vpnGateways.*`

  * `compute.vpnGateways.create`
  * `compute.vpnGateways.createTagBinding`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.deleteTagBinding`
  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.listEffectiveTags`
  * `compute.vpnGateways.listTagBindings`
  * `compute.vpnGateways.setLabels`
  * `compute.vpnGateways.use`

`compute.vpnTunnels.*`

  * `compute.vpnTunnels.create`
  * `compute.vpnTunnels.createTagBinding`
  * `compute.vpnTunnels.delete`
  * `compute.vpnTunnels.deleteTagBinding`
  * `compute.vpnTunnels.get`
  * `compute.vpnTunnels.list`
  * `compute.vpnTunnels.listEffectiveTags`
  * `compute.vpnTunnels.listTagBindings`
  * `compute.vpnTunnels.setLabels`

`compute.wireGroups.*`

  * `compute.wireGroups.create`
  * `compute.wireGroups.delete`
  * `compute.wireGroups.get`
  * `compute.wireGroups.list`
  * `compute.wireGroups.update`

`compute.zoneOperations.get` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`container.*`

  * `container.apiServices.create`
  * `container.apiServices.delete`
  * `container.apiServices.get`
  * `container.apiServices.getStatus`
  * `container.apiServices.list`
  * `container.apiServices.update`
  * `container.apiServices.updateStatus`
  * `container.auditSinks.create`
  * `container.auditSinks.delete`
  * `container.auditSinks.get`
  * `container.auditSinks.list`
  * `container.auditSinks.update`
  * `container.backendConfigs.create`
  * `container.backendConfigs.delete`
  * `container.backendConfigs.get`
  * `container.backendConfigs.list`
  * `container.backendConfigs.update`
  * `container.bindings.create`
  * `container.bindings.delete`
  * `container.bindings.get`
  * `container.bindings.list`
  * `container.bindings.update`
  * `container.certificateSigningRequests.approve`
  * `container.certificateSigningRequests.create`
  * `container.certificateSigningRequests.delete`
  * `container.certificateSigningRequests.get`
  * `container.certificateSigningRequests.getStatus`
  * `container.certificateSigningRequests.list`
  * `container.certificateSigningRequests.update`
  * `container.certificateSigningRequests.updateStatus`
  * `container.clusterRoleBindings.create`
  * `container.clusterRoleBindings.delete`
  * `container.clusterRoleBindings.get`
  * `container.clusterRoleBindings.list`
  * `container.clusterRoleBindings.update`
  * `container.clusterRoles.bind`
  * `container.clusterRoles.create`
  * `container.clusterRoles.delete`
  * `container.clusterRoles.escalate`
  * `container.clusterRoles.get`
  * `container.clusterRoles.list`
  * `container.clusterRoles.update`
  * `container.clusters.connect`
  * `container.clusters.create`
  * `container.clusters.createTagBinding`
  * `container.clusters.delete`
  * `container.clusters.deleteTagBinding`
  * `container.clusters.get`
  * `container.clusters.getCredentials`
  * `container.clusters.impersonate`
  * `container.clusters.list`
  * `container.clusters.listEffectiveTags`
  * `container.clusters.listTagBindings`
  * `container.clusters.update`
  * `container.componentStatuses.get`
  * `container.componentStatuses.list`
  * `container.configMaps.create`
  * `container.configMaps.delete`
  * `container.configMaps.get`
  * `container.configMaps.list`
  * `container.configMaps.update`
  * `container.controllerRevisions.create`
  * `container.controllerRevisions.delete`
  * `container.controllerRevisions.get`
  * `container.controllerRevisions.list`
  * `container.controllerRevisions.update`
  * `container.cronJobs.create`
  * `container.cronJobs.delete`
  * `container.cronJobs.get`
  * `container.cronJobs.getStatus`
  * `container.cronJobs.list`
  * `container.cronJobs.update`
  * `container.cronJobs.updateStatus`
  * `container.csiDrivers.create`
  * `container.csiDrivers.delete`
  * `container.csiDrivers.get`
  * `container.csiDrivers.list`
  * `container.csiDrivers.update`
  * `container.csiNodeInfos.create`
  * `container.csiNodeInfos.delete`
  * `container.csiNodeInfos.get`
  * `container.csiNodeInfos.list`
  * `container.csiNodeInfos.update`
  * `container.csiNodes.create`
  * `container.csiNodes.delete`
  * `container.csiNodes.get`
  * `container.csiNodes.list`
  * `container.csiNodes.update`
  * `container.customResourceDefinitions.create`
  * `container.customResourceDefinitions.delete`
  * `container.customResourceDefinitions.get`
  * `container.customResourceDefinitions.getStatus`
  * `container.customResourceDefinitions.list`
  * `container.customResourceDefinitions.update`
  * `container.customResourceDefinitions.updateStatus`
  * `container.daemonSets.create`
  * `container.daemonSets.delete`
  * `container.daemonSets.get`
  * `container.daemonSets.getStatus`
  * `container.daemonSets.list`
  * `container.daemonSets.update`
  * `container.daemonSets.updateStatus`
  * `container.deployments.create`
  * `container.deployments.delete`
  * `container.deployments.get`
  * `container.deployments.getScale`
  * `container.deployments.getStatus`
  * `container.deployments.list`
  * `container.deployments.rollback`
  * `container.deployments.update`
  * `container.deployments.updateScale`
  * `container.deployments.updateStatus`
  * `container.endpointSlices.create`
  * `container.endpointSlices.delete`
  * `container.endpointSlices.get`
  * `container.endpointSlices.list`
  * `container.endpointSlices.update`
  * `container.endpoints.create`
  * `container.endpoints.delete`
  * `container.endpoints.get`
  * `container.endpoints.list`
  * `container.endpoints.update`
  * `container.events.create`
  * `container.events.delete`
  * `container.events.get`
  * `container.events.list`
  * `container.events.update`
  * `container.frontendConfigs.create`
  * `container.frontendConfigs.delete`
  * `container.frontendConfigs.get`
  * `container.frontendConfigs.list`
  * `container.frontendConfigs.update`
  * `container.horizontalPodAutoscalers.create`
  * `container.horizontalPodAutoscalers.delete`
  * `container.horizontalPodAutoscalers.get`
  * `container.horizontalPodAutoscalers.getStatus`
  * `container.horizontalPodAutoscalers.list`
  * `container.horizontalPodAutoscalers.update`
  * `container.horizontalPodAutoscalers.updateStatus`
  * `container.hostServiceAgent.use`
  * `container.ingresses.create`
  * `container.ingresses.delete`
  * `container.ingresses.get`
  * `container.ingresses.getStatus`
  * `container.ingresses.list`
  * `container.ingresses.update`
  * `container.ingresses.updateStatus`
  * `container.initializerConfigurations.create`
  * `container.initializerConfigurations.delete`
  * `container.initializerConfigurations.get`
  * `container.initializerConfigurations.list`
  * `container.initializerConfigurations.update`
  * `container.jobs.create`
  * `container.jobs.delete`
  * `container.jobs.get`
  * `container.jobs.getStatus`
  * `container.jobs.list`
  * `container.jobs.update`
  * `container.jobs.updateStatus`
  * `container.leases.create`
  * `container.leases.delete`
  * `container.leases.get`
  * `container.leases.list`
  * `container.leases.update`
  * `container.limitRanges.create`
  * `container.limitRanges.delete`
  * `container.limitRanges.get`
  * `container.limitRanges.list`
  * `container.limitRanges.update`
  * `container.localSubjectAccessReviews.create`
  * `container.localSubjectAccessReviews.list`
  * `container.managedCertificates.create`
  * `container.managedCertificates.delete`
  * `container.managedCertificates.get`
  * `container.managedCertificates.list`
  * `container.managedCertificates.update`
  * `container.mutatingWebhookConfigurations.create`
  * `container.mutatingWebhookConfigurations.delete`
  * `container.mutatingWebhookConfigurations.get`
  * `container.mutatingWebhookConfigurations.list`
  * `container.mutatingWebhookConfigurations.update`
  * `container.namespaces.create`
  * `container.namespaces.delete`
  * `container.namespaces.finalize`
  * `container.namespaces.get`
  * `container.namespaces.getStatus`
  * `container.namespaces.list`
  * `container.namespaces.update`
  * `container.namespaces.updateStatus`
  * `container.networkPolicies.create`
  * `container.networkPolicies.delete`
  * `container.networkPolicies.get`
  * `container.networkPolicies.list`
  * `container.networkPolicies.update`
  * `container.nodes.create`
  * `container.nodes.delete`
  * `container.nodes.get`
  * `container.nodes.getStatus`
  * `container.nodes.list`
  * `container.nodes.proxy`
  * `container.nodes.update`
  * `container.nodes.updateStatus`
  * `container.operations.get`
  * `container.operations.list`
  * `container.persistentVolumeClaims.create`
  * `container.persistentVolumeClaims.delete`
  * `container.persistentVolumeClaims.get`
  * `container.persistentVolumeClaims.getStatus`
  * `container.persistentVolumeClaims.list`
  * `container.persistentVolumeClaims.update`
  * `container.persistentVolumeClaims.updateStatus`
  * `container.persistentVolumes.create`
  * `container.persistentVolumes.delete`
  * `container.persistentVolumes.get`
  * `container.persistentVolumes.getStatus`
  * `container.persistentVolumes.list`
  * `container.persistentVolumes.update`
  * `container.persistentVolumes.updateStatus`
  * `container.petSets.create`
  * `container.petSets.delete`
  * `container.petSets.get`
  * `container.petSets.list`
  * `container.petSets.update`
  * `container.petSets.updateStatus`
  * `container.podDisruptionBudgets.create`
  * `container.podDisruptionBudgets.delete`
  * `container.podDisruptionBudgets.get`
  * `container.podDisruptionBudgets.getStatus`
  * `container.podDisruptionBudgets.list`
  * `container.podDisruptionBudgets.update`
  * `container.podDisruptionBudgets.updateStatus`
  * `container.podPresets.create`
  * `container.podPresets.delete`
  * `container.podPresets.get`
  * `container.podPresets.list`
  * `container.podPresets.update`
  * `container.podSecurityPolicies.create`
  * `container.podSecurityPolicies.delete`
  * `container.podSecurityPolicies.get`
  * `container.podSecurityPolicies.list`
  * `container.podSecurityPolicies.update`
  * `container.podSecurityPolicies.use`
  * `container.podTemplates.create`
  * `container.podTemplates.delete`
  * `container.podTemplates.get`
  * `container.podTemplates.list`
  * `container.podTemplates.update`
  * `container.pods.attach`
  * `container.pods.create`
  * `container.pods.delete`
  * `container.pods.evict`
  * `container.pods.exec`
  * `container.pods.get`
  * `container.pods.getLogs`
  * `container.pods.getStatus`
  * `container.pods.initialize`
  * `container.pods.list`
  * `container.pods.portForward`
  * `container.pods.proxy`
  * `container.pods.update`
  * `container.pods.updateStatus`
  * `container.priorityClasses.create`
  * `container.priorityClasses.delete`
  * `container.priorityClasses.get`
  * `container.priorityClasses.list`
  * `container.priorityClasses.update`
  * `container.replicaSets.create`
  * `container.replicaSets.delete`
  * `container.replicaSets.get`
  * `container.replicaSets.getScale`
  * `container.replicaSets.getStatus`
  * `container.replicaSets.list`
  * `container.replicaSets.update`
  * `container.replicaSets.updateScale`
  * `container.replicaSets.updateStatus`
  * `container.replicationControllers.create`
  * `container.replicationControllers.delete`
  * `container.replicationControllers.get`
  * `container.replicationControllers.getScale`
  * `container.replicationControllers.getStatus`
  * `container.replicationControllers.list`
  * `container.replicationControllers.update`
  * `container.replicationControllers.updateScale`
  * `container.replicationControllers.updateStatus`
  * `container.resourceQuotas.create`
  * `container.resourceQuotas.delete`
  * `container.resourceQuotas.get`
  * `container.resourceQuotas.getStatus`
  * `container.resourceQuotas.list`
  * `container.resourceQuotas.update`
  * `container.resourceQuotas.updateStatus`
  * `container.roleBindings.create`
  * `container.roleBindings.delete`
  * `container.roleBindings.get`
  * `container.roleBindings.list`
  * `container.roleBindings.update`
  * `container.roles.bind`
  * `container.roles.create`
  * `container.roles.delete`
  * `container.roles.escalate`
  * `container.roles.get`
  * `container.roles.list`
  * `container.roles.update`
  * `container.runtimeClasses.create`
  * `container.runtimeClasses.delete`
  * `container.runtimeClasses.get`
  * `container.runtimeClasses.list`
  * `container.runtimeClasses.update`
  * `container.scheduledJobs.create`
  * `container.scheduledJobs.delete`
  * `container.scheduledJobs.get`
  * `container.scheduledJobs.list`
  * `container.scheduledJobs.update`
  * `container.scheduledJobs.updateStatus`
  * `container.secrets.create`
  * `container.secrets.delete`
  * `container.secrets.get`
  * `container.secrets.list`
  * `container.secrets.update`
  * `container.selfSubjectAccessReviews.create`
  * `container.selfSubjectAccessReviews.list`
  * `container.selfSubjectRulesReviews.create`
  * `container.serviceAccounts.create`
  * `container.serviceAccounts.createToken`
  * `container.serviceAccounts.delete`
  * `container.serviceAccounts.get`
  * `container.serviceAccounts.list`
  * `container.serviceAccounts.update`
  * `container.services.create`
  * `container.services.delete`
  * `container.services.get`
  * `container.services.getStatus`
  * `container.services.list`
  * `container.services.proxy`
  * `container.services.update`
  * `container.services.updateStatus`
  * `container.statefulSets.create`
  * `container.statefulSets.delete`
  * `container.statefulSets.get`
  * `container.statefulSets.getScale`
  * `container.statefulSets.getStatus`
  * `container.statefulSets.list`
  * `container.statefulSets.update`
  * `container.statefulSets.updateScale`
  * `container.statefulSets.updateStatus`
  * `container.storageClasses.create`
  * `container.storageClasses.delete`
  * `container.storageClasses.get`
  * `container.storageClasses.list`
  * `container.storageClasses.update`
  * `container.storageStates.create`
  * `container.storageStates.delete`
  * `container.storageStates.get`
  * `container.storageStates.getStatus`
  * `container.storageStates.list`
  * `container.storageStates.update`
  * `container.storageStates.updateStatus`
  * `container.storageVersionMigrations.create`
  * `container.storageVersionMigrations.delete`
  * `container.storageVersionMigrations.get`
  * `container.storageVersionMigrations.getStatus`
  * `container.storageVersionMigrations.list`
  * `container.storageVersionMigrations.update`
  * `container.storageVersionMigrations.updateStatus`
  * `container.subjectAccessReviews.create`
  * `container.subjectAccessReviews.list`
  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`
  * `container.thirdPartyResources.create`
  * `container.thirdPartyResources.delete`
  * `container.thirdPartyResources.get`
  * `container.thirdPartyResources.list`
  * `container.thirdPartyResources.update`
  * `container.tokenReviews.create`
  * `container.updateInfos.create`
  * `container.updateInfos.delete`
  * `container.updateInfos.get`
  * `container.updateInfos.list`
  * `container.updateInfos.update`
  * `container.validatingWebhookConfigurations.create`
  * `container.validatingWebhookConfigurations.delete`
  * `container.validatingWebhookConfigurations.get`
  * `container.validatingWebhookConfigurations.list`
  * `container.validatingWebhookConfigurations.update`
  * `container.volumeAttachments.create`
  * `container.volumeAttachments.delete`
  * `container.volumeAttachments.get`
  * `container.volumeAttachments.getStatus`
  * `container.volumeAttachments.list`
  * `container.volumeAttachments.update`
  * `container.volumeAttachments.updateStatus`
  * `container.volumeSnapshotClasses.create`
  * `container.volumeSnapshotClasses.delete`
  * `container.volumeSnapshotClasses.get`
  * `container.volumeSnapshotClasses.list`
  * `container.volumeSnapshotClasses.update`
  * `container.volumeSnapshotContents.create`
  * `container.volumeSnapshotContents.delete`
  * `container.volumeSnapshotContents.get`
  * `container.volumeSnapshotContents.getStatus`
  * `container.volumeSnapshotContents.list`
  * `container.volumeSnapshotContents.update`
  * `container.volumeSnapshotContents.updateStatus`
  * `container.volumeSnapshots.create`
  * `container.volumeSnapshots.delete`
  * `container.volumeSnapshots.get`
  * `container.volumeSnapshots.getStatus`
  * `container.volumeSnapshots.list`
  * `container.volumeSnapshots.update`
  * `container.volumeSnapshots.updateStatus`

`databasesconsole.locations.*`

  * `databasesconsole.locations.get`
  * `databasesconsole.locations.list`

`databasesconsole.studioQueries.*`

  * `databasesconsole.studioQueries.create`
  * `databasesconsole.studioQueries.delete`
  * `databasesconsole.studioQueries.get`
  * `databasesconsole.studioQueries.list`
  * `databasesconsole.studioQueries.search`
  * `databasesconsole.studioQueries.update`

`deploymentmanager.compositeTypes.*`

  * `deploymentmanager.compositeTypes.create`
  * `deploymentmanager.compositeTypes.delete`
  * `deploymentmanager.compositeTypes.get`
  * `deploymentmanager.compositeTypes.list`
  * `deploymentmanager.compositeTypes.update`

`deploymentmanager.deployments.cancelPreview` `deploymentmanager.deployments.create` `deploymentmanager.deployments.delete` `deploymentmanager.deployments.get` `deploymentmanager.deployments.list` `deploymentmanager.deployments.stop` `deploymentmanager.deployments.update` `deploymentmanager.manifests.*`

  * `deploymentmanager.manifests.get`
  * `deploymentmanager.manifests.list`

`deploymentmanager.operations.*`

  * `deploymentmanager.operations.get`
  * `deploymentmanager.operations.list`

`deploymentmanager.resources.*`

  * `deploymentmanager.resources.get`
  * `deploymentmanager.resources.list`

`deploymentmanager.typeProviders.*`

  * `deploymentmanager.typeProviders.create`
  * `deploymentmanager.typeProviders.delete`
  * `deploymentmanager.typeProviders.get`
  * `deploymentmanager.typeProviders.getType`
  * `deploymentmanager.typeProviders.list`
  * `deploymentmanager.typeProviders.listTypes`
  * `deploymentmanager.typeProviders.update`

`deploymentmanager.types.*`

  * `deploymentmanager.types.create`
  * `deploymentmanager.types.delete`
  * `deploymentmanager.types.get`
  * `deploymentmanager.types.list`
  * `deploymentmanager.types.update`

`dns.managedZones.get` `dns.managedZones.list` `dns.networks.targetWithPeeringZone` `firebase.projects.get` `iam.serviceAccounts.actAs` `iam.serviceAccounts.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `iam.serviceAccounts.list` `logging.buckets.create` `logging.buckets.createTagBinding` `logging.buckets.delete` `logging.buckets.deleteTagBinding` `logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.buckets.undelete` `logging.buckets.update` `logging.exclusions.*`

  * `logging.exclusions.create`
  * `logging.exclusions.delete`
  * `logging.exclusions.get`
  * `logging.exclusions.list`
  * `logging.exclusions.update`

`logging.links.*`

  * `logging.links.create`
  * `logging.links.delete`
  * `logging.links.get`
  * `logging.links.list`

`logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logEntries.create` `logging.logEntries.route` `logging.logMetrics.*`

  * `logging.logMetrics.create`
  * `logging.logMetrics.delete`
  * `logging.logMetrics.get`
  * `logging.logMetrics.list`
  * `logging.logMetrics.update`

`logging.logScopes.*`

  * `logging.logScopes.create`
  * `logging.logScopes.delete`
  * `logging.logScopes.get`
  * `logging.logScopes.list`
  * `logging.logScopes.update`

`logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.notificationRules.*`

  * `logging.notificationRules.create`
  * `logging.notificationRules.delete`
  * `logging.notificationRules.get`
  * `logging.notificationRules.list`
  * `logging.notificationRules.update`

`logging.operations.*`

  * `logging.operations.cancel`
  * `logging.operations.get`
  * `logging.operations.list`

`logging.settings.*`

  * `logging.settings.get`
  * `logging.settings.update`

`logging.sinks.*`

  * `logging.sinks.create`
  * `logging.sinks.delete`
  * `logging.sinks.get`
  * `logging.sinks.list`
  * `logging.sinks.update`

`logging.sqlAlerts.*`

  * `logging.sqlAlerts.create`
  * `logging.sqlAlerts.update`

`logging.views.create` `logging.views.delete` `logging.views.get` `logging.views.getIamPolicy` `logging.views.list` `logging.views.update` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `networkconnectivity.internalRanges.*`

  * `networkconnectivity.internalRanges.create`
  * `networkconnectivity.internalRanges.delete`
  * `networkconnectivity.internalRanges.get`
  * `networkconnectivity.internalRanges.getIamPolicy`
  * `networkconnectivity.internalRanges.list`
  * `networkconnectivity.internalRanges.setIamPolicy`
  * `networkconnectivity.internalRanges.update`

`networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.operations.*`

  * `networkconnectivity.operations.cancel`
  * `networkconnectivity.operations.delete`
  * `networkconnectivity.operations.get`
  * `networkconnectivity.operations.list`

`networkconnectivity.policyBasedRoutes.*`

  * `networkconnectivity.policyBasedRoutes.create`
  * `networkconnectivity.policyBasedRoutes.delete`
  * `networkconnectivity.policyBasedRoutes.get`
  * `networkconnectivity.policyBasedRoutes.getIamPolicy`
  * `networkconnectivity.policyBasedRoutes.list`
  * `networkconnectivity.policyBasedRoutes.setIamPolicy`

`networkconnectivity.regionalEndpoints.*`

  * `networkconnectivity.regionalEndpoints.create`
  * `networkconnectivity.regionalEndpoints.delete`
  * `networkconnectivity.regionalEndpoints.get`
  * `networkconnectivity.regionalEndpoints.list`

`networkconnectivity.serviceClasses.*`

  * `networkconnectivity.serviceClasses.create`
  * `networkconnectivity.serviceClasses.delete`
  * `networkconnectivity.serviceClasses.get`
  * `networkconnectivity.serviceClasses.list`
  * `networkconnectivity.serviceClasses.update`
  * `networkconnectivity.serviceClasses.use`

`networkconnectivity.serviceConnectionMaps.*`

  * `networkconnectivity.serviceConnectionMaps.create`
  * `networkconnectivity.serviceConnectionMaps.delete`
  * `networkconnectivity.serviceConnectionMaps.get`
  * `networkconnectivity.serviceConnectionMaps.list`
  * `networkconnectivity.serviceConnectionMaps.update`

`networkconnectivity.serviceConnectionPolicies.*`

  * `networkconnectivity.serviceConnectionPolicies.create`
  * `networkconnectivity.serviceConnectionPolicies.delete`
  * `networkconnectivity.serviceConnectionPolicies.get`
  * `networkconnectivity.serviceConnectionPolicies.list`
  * `networkconnectivity.serviceConnectionPolicies.update`

`networkmanagement.connectivitytests.get` `networkmanagement.connectivitytests.list` `networksecurity.addressGroups.*`

  * `networksecurity.addressGroups.create`
  * `networksecurity.addressGroups.delete`
  * `networksecurity.addressGroups.get`
  * `networksecurity.addressGroups.getIamPolicy`
  * `networksecurity.addressGroups.list`
  * `networksecurity.addressGroups.setIamPolicy`
  * `networksecurity.addressGroups.update`
  * `networksecurity.addressGroups.use`

`networksecurity.authorizationPolicies.*`

  * `networksecurity.authorizationPolicies.create`
  * `networksecurity.authorizationPolicies.createTagBinding`
  * `networksecurity.authorizationPolicies.delete`
  * `networksecurity.authorizationPolicies.deleteTagBinding`
  * `networksecurity.authorizationPolicies.get`
  * `networksecurity.authorizationPolicies.getIamPolicy`
  * `networksecurity.authorizationPolicies.list`
  * `networksecurity.authorizationPolicies.listEffectiveTags`
  * `networksecurity.authorizationPolicies.listTagBindings`
  * `networksecurity.authorizationPolicies.setIamPolicy`
  * `networksecurity.authorizationPolicies.update`
  * `networksecurity.authorizationPolicies.use`

`networksecurity.authzPolicies.*`

  * `networksecurity.authzPolicies.create`
  * `networksecurity.authzPolicies.delete`
  * `networksecurity.authzPolicies.get`
  * `networksecurity.authzPolicies.getIamPolicy`
  * `networksecurity.authzPolicies.list`
  * `networksecurity.authzPolicies.setIamPolicy`
  * `networksecurity.authzPolicies.update`

`networksecurity.backendAuthenticationConfigs.*`

  * `networksecurity.backendAuthenticationConfigs.create`
  * `networksecurity.backendAuthenticationConfigs.delete`
  * `networksecurity.backendAuthenticationConfigs.get`
  * `networksecurity.backendAuthenticationConfigs.list`
  * `networksecurity.backendAuthenticationConfigs.update`
  * `networksecurity.backendAuthenticationConfigs.use`

`networksecurity.clientTlsPolicies.*`

  * `networksecurity.clientTlsPolicies.create`
  * `networksecurity.clientTlsPolicies.createTagBinding`
  * `networksecurity.clientTlsPolicies.delete`
  * `networksecurity.clientTlsPolicies.deleteTagBinding`
  * `networksecurity.clientTlsPolicies.get`
  * `networksecurity.clientTlsPolicies.getIamPolicy`
  * `networksecurity.clientTlsPolicies.list`
  * `networksecurity.clientTlsPolicies.listEffectiveTags`
  * `networksecurity.clientTlsPolicies.listTagBindings`
  * `networksecurity.clientTlsPolicies.setIamPolicy`
  * `networksecurity.clientTlsPolicies.update`
  * `networksecurity.clientTlsPolicies.use`

`networksecurity.firewallEndpointAssociations.*`

  * `networksecurity.firewallEndpointAssociations.create`
  * `networksecurity.firewallEndpointAssociations.delete`
  * `networksecurity.firewallEndpointAssociations.get`
  * `networksecurity.firewallEndpointAssociations.list`
  * `networksecurity.firewallEndpointAssociations.update`

`networksecurity.firewallEndpoints.*`

  * `networksecurity.firewallEndpoints.create`
  * `networksecurity.firewallEndpoints.createVerdictChangeRequest`
  * `networksecurity.firewallEndpoints.delete`
  * `networksecurity.firewallEndpoints.get`
  * `networksecurity.firewallEndpoints.getVerdictChangeRequest`
  * `networksecurity.firewallEndpoints.getWildfireReport`
  * `networksecurity.firewallEndpoints.getWildfireSample`
  * `networksecurity.firewallEndpoints.list`
  * `networksecurity.firewallEndpoints.listVerdictChangeRequests`
  * `networksecurity.firewallEndpoints.submitVerdictChangeRequest`
  * `networksecurity.firewallEndpoints.update`
  * `networksecurity.firewallEndpoints.use`
  * `networksecurity.firewallEndpoints.useWildfire`

`networksecurity.gatewaySecurityPolicies.*`

  * `networksecurity.gatewaySecurityPolicies.create`
  * `networksecurity.gatewaySecurityPolicies.delete`
  * `networksecurity.gatewaySecurityPolicies.get`
  * `networksecurity.gatewaySecurityPolicies.list`
  * `networksecurity.gatewaySecurityPolicies.update`
  * `networksecurity.gatewaySecurityPolicies.use`

`networksecurity.gatewaySecurityPolicyRules.*`

  * `networksecurity.gatewaySecurityPolicyRules.create`
  * `networksecurity.gatewaySecurityPolicyRules.delete`
  * `networksecurity.gatewaySecurityPolicyRules.get`
  * `networksecurity.gatewaySecurityPolicyRules.list`
  * `networksecurity.gatewaySecurityPolicyRules.update`
  * `networksecurity.gatewaySecurityPolicyRules.use`

`networksecurity.locations.*`

  * `networksecurity.locations.get`
  * `networksecurity.locations.list`

`networksecurity.operations.*`

  * `networksecurity.operations.cancel`
  * `networksecurity.operations.delete`
  * `networksecurity.operations.get`
  * `networksecurity.operations.list`

`networksecurity.sacAttachments.*`

  * `networksecurity.sacAttachments.create`
  * `networksecurity.sacAttachments.delete`
  * `networksecurity.sacAttachments.get`
  * `networksecurity.sacAttachments.list`

`networksecurity.sacRealms.*`

  * `networksecurity.sacRealms.create`
  * `networksecurity.sacRealms.delete`
  * `networksecurity.sacRealms.get`
  * `networksecurity.sacRealms.list`

`networksecurity.securityProfileGroups.*`

  * `networksecurity.securityProfileGroups.create`
  * `networksecurity.securityProfileGroups.delete`
  * `networksecurity.securityProfileGroups.get`
  * `networksecurity.securityProfileGroups.list`
  * `networksecurity.securityProfileGroups.update`
  * `networksecurity.securityProfileGroups.use`

`networksecurity.securityProfiles.*`

  * `networksecurity.securityProfiles.create`
  * `networksecurity.securityProfiles.delete`
  * `networksecurity.securityProfiles.get`
  * `networksecurity.securityProfiles.list`
  * `networksecurity.securityProfiles.update`
  * `networksecurity.securityProfiles.use`

`networksecurity.serverTlsPolicies.*`

  * `networksecurity.serverTlsPolicies.create`
  * `networksecurity.serverTlsPolicies.createTagBinding`
  * `networksecurity.serverTlsPolicies.delete`
  * `networksecurity.serverTlsPolicies.deleteTagBinding`
  * `networksecurity.serverTlsPolicies.get`
  * `networksecurity.serverTlsPolicies.getIamPolicy`
  * `networksecurity.serverTlsPolicies.list`
  * `networksecurity.serverTlsPolicies.listEffectiveTags`
  * `networksecurity.serverTlsPolicies.listTagBindings`
  * `networksecurity.serverTlsPolicies.setIamPolicy`
  * `networksecurity.serverTlsPolicies.update`
  * `networksecurity.serverTlsPolicies.use`

`networksecurity.tlsInspectionPolicies.*`

  * `networksecurity.tlsInspectionPolicies.create`
  * `networksecurity.tlsInspectionPolicies.delete`
  * `networksecurity.tlsInspectionPolicies.get`
  * `networksecurity.tlsInspectionPolicies.list`
  * `networksecurity.tlsInspectionPolicies.update`
  * `networksecurity.tlsInspectionPolicies.use`

`networksecurity.urlLists.*`

  * `networksecurity.urlLists.create`
  * `networksecurity.urlLists.delete`
  * `networksecurity.urlLists.get`
  * `networksecurity.urlLists.list`
  * `networksecurity.urlLists.update`
  * `networksecurity.urlLists.use`

`networkservices.*`

  * `networkservices.agentGateways.create`
  * `networkservices.agentGateways.delete`
  * `networkservices.agentGateways.get`
  * `networkservices.agentGateways.list`
  * `networkservices.agentGateways.update`
  * `networkservices.agentGateways.use`
  * `networkservices.authzExtensions.create`
  * `networkservices.authzExtensions.delete`
  * `networkservices.authzExtensions.get`
  * `networkservices.authzExtensions.list`
  * `networkservices.authzExtensions.update`
  * `networkservices.authzExtensions.use`
  * `networkservices.endpointConfigSelectors.createTagBinding`
  * `networkservices.endpointConfigSelectors.deleteTagBinding`
  * `networkservices.endpointConfigSelectors.listEffectiveTags`
  * `networkservices.endpointConfigSelectors.listTagBindings`
  * `networkservices.endpointPolicies.create`
  * `networkservices.endpointPolicies.delete`
  * `networkservices.endpointPolicies.get`
  * `networkservices.endpointPolicies.list`
  * `networkservices.endpointPolicies.update`
  * `networkservices.gateways.create`
  * `networkservices.gateways.createTagBinding`
  * `networkservices.gateways.delete`
  * `networkservices.gateways.deleteTagBinding`
  * `networkservices.gateways.get`
  * `networkservices.gateways.list`
  * `networkservices.gateways.listEffectiveTags`
  * `networkservices.gateways.listTagBindings`
  * `networkservices.gateways.update`
  * `networkservices.gateways.use`
  * `networkservices.googleTagGatewayPolicies.create`
  * `networkservices.googleTagGatewayPolicies.delete`
  * `networkservices.googleTagGatewayPolicies.get`
  * `networkservices.googleTagGatewayPolicies.list`
  * `networkservices.googleTagGatewayPolicies.update`
  * `networkservices.grpcRoutes.create`
  * `networkservices.grpcRoutes.delete`
  * `networkservices.grpcRoutes.get`
  * `networkservices.grpcRoutes.list`
  * `networkservices.grpcRoutes.update`
  * `networkservices.httpFilters.create`
  * `networkservices.httpFilters.createTagBinding`
  * `networkservices.httpFilters.delete`
  * `networkservices.httpFilters.deleteTagBinding`
  * `networkservices.httpFilters.get`
  * `networkservices.httpFilters.list`
  * `networkservices.httpFilters.listEffectiveTags`
  * `networkservices.httpFilters.listTagBindings`
  * `networkservices.httpFilters.update`
  * `networkservices.httpRoutes.create`
  * `networkservices.httpRoutes.delete`
  * `networkservices.httpRoutes.get`
  * `networkservices.httpRoutes.list`
  * `networkservices.httpRoutes.update`
  * `networkservices.httpfilters.create`
  * `networkservices.httpfilters.delete`
  * `networkservices.httpfilters.get`
  * `networkservices.httpfilters.getIamPolicy`
  * `networkservices.httpfilters.list`
  * `networkservices.httpfilters.setIamPolicy`
  * `networkservices.httpfilters.update`
  * `networkservices.httpfilters.use`
  * `networkservices.lbEdgeExtensions.create`
  * `networkservices.lbEdgeExtensions.delete`
  * `networkservices.lbEdgeExtensions.get`
  * `networkservices.lbEdgeExtensions.list`
  * `networkservices.lbEdgeExtensions.update`
  * `networkservices.lbRouteExtensions.create`
  * `networkservices.lbRouteExtensions.delete`
  * `networkservices.lbRouteExtensions.get`
  * `networkservices.lbRouteExtensions.list`
  * `networkservices.lbRouteExtensions.update`
  * `networkservices.lbTcpExtensions.createForNetwork`
  * `networkservices.lbTcpExtensions.deleteForNetwork`
  * `networkservices.lbTcpExtensions.getForNetwork`
  * `networkservices.lbTcpExtensions.listForNetwork`
  * `networkservices.lbTcpExtensions.updateForNetwork`
  * `networkservices.lbTrafficExtensions.create`
  * `networkservices.lbTrafficExtensions.delete`
  * `networkservices.lbTrafficExtensions.get`
  * `networkservices.lbTrafficExtensions.list`
  * `networkservices.lbTrafficExtensions.update`
  * `networkservices.locations.get`
  * `networkservices.locations.list`
  * `networkservices.meshes.create`
  * `networkservices.meshes.createTagBinding`
  * `networkservices.meshes.delete`
  * `networkservices.meshes.deleteTagBinding`
  * `networkservices.meshes.get`
  * `networkservices.meshes.list`
  * `networkservices.meshes.listEffectiveTags`
  * `networkservices.meshes.listTagBindings`
  * `networkservices.meshes.update`
  * `networkservices.meshes.use`
  * `networkservices.operations.cancel`
  * `networkservices.operations.delete`
  * `networkservices.operations.get`
  * `networkservices.operations.list`
  * `networkservices.route_views.get`
  * `networkservices.route_views.list`
  * `networkservices.serviceBindings.create`
  * `networkservices.serviceBindings.delete`
  * `networkservices.serviceBindings.get`
  * `networkservices.serviceBindings.list`
  * `networkservices.serviceBindings.update`
  * `networkservices.serviceLbPolicies.create`
  * `networkservices.serviceLbPolicies.delete`
  * `networkservices.serviceLbPolicies.get`
  * `networkservices.serviceLbPolicies.list`
  * `networkservices.serviceLbPolicies.update`
  * `networkservices.swpSecurityExtensions.create`
  * `networkservices.swpSecurityExtensions.delete`
  * `networkservices.swpSecurityExtensions.get`
  * `networkservices.swpSecurityExtensions.list`
  * `networkservices.swpSecurityExtensions.update`
  * `networkservices.tcpRoutes.create`
  * `networkservices.tcpRoutes.delete`
  * `networkservices.tcpRoutes.get`
  * `networkservices.tcpRoutes.list`
  * `networkservices.tcpRoutes.update`
  * `networkservices.tlsRoutes.create`
  * `networkservices.tlsRoutes.delete`
  * `networkservices.tlsRoutes.get`
  * `networkservices.tlsRoutes.list`
  * `networkservices.tlsRoutes.update`
  * `networkservices.wasmPlugins.create`
  * `networkservices.wasmPlugins.delete`
  * `networkservices.wasmPlugins.get`
  * `networkservices.wasmPlugins.list`
  * `networkservices.wasmPlugins.update`
  * `networkservices.wasmPlugins.use`

`observability.scopes.get` `opsconfigmonitoring.resourceMetadata.list` `orgpolicy.policy.get` `pubsub.messageTransforms.validate` `pubsub.schemas.*`

  * `pubsub.schemas.attach`
  * `pubsub.schemas.commit`
  * `pubsub.schemas.create`
  * `pubsub.schemas.delete`
  * `pubsub.schemas.get`
  * `pubsub.schemas.getIamPolicy`
  * `pubsub.schemas.list`
  * `pubsub.schemas.listRevisions`
  * `pubsub.schemas.rollback`
  * `pubsub.schemas.setIamPolicy`
  * `pubsub.schemas.validate`

`pubsub.snapshots.create` `pubsub.snapshots.delete` `pubsub.snapshots.get` `pubsub.snapshots.getIamPolicy` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.snapshots.seek` `pubsub.snapshots.setIamPolicy` `pubsub.snapshots.update` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.subscriptions.getIamPolicy` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.subscriptions.setIamPolicy` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.delete` `pubsub.topics.detachSubscription` `pubsub.topics.get` `pubsub.topics.getIamPolicy` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `pubsub.topics.publish` `pubsub.topics.setIamPolicy` `pubsub.topics.update` `pubsub.topics.updateTag` `recommender.appengineVersionCostInsights.*`

  * `recommender.appengineVersionCostInsights.get`
  * `recommender.appengineVersionCostInsights.list`
  * `recommender.appengineVersionCostInsights.update`

`recommender.appengineVersionCostRecommendations.*`

  * `recommender.appengineVersionCostRecommendations.get`
  * `recommender.appengineVersionCostRecommendations.list`
  * `recommender.appengineVersionCostRecommendations.update`

`recommender.cloudsqlIdleInstanceRecommendations.*`

  * `recommender.cloudsqlIdleInstanceRecommendations.get`
  * `recommender.cloudsqlIdleInstanceRecommendations.list`
  * `recommender.cloudsqlIdleInstanceRecommendations.update`

`recommender.cloudsqlInstanceActivityInsights.*`

  * `recommender.cloudsqlInstanceActivityInsights.get`
  * `recommender.cloudsqlInstanceActivityInsights.list`
  * `recommender.cloudsqlInstanceActivityInsights.update`

`recommender.cloudsqlInstanceCpuUsageInsights.*`

  * `recommender.cloudsqlInstanceCpuUsageInsights.get`
  * `recommender.cloudsqlInstanceCpuUsageInsights.list`
  * `recommender.cloudsqlInstanceCpuUsageInsights.update`

`recommender.cloudsqlInstanceDiskUsageTrendInsights.*`

  * `recommender.cloudsqlInstanceDiskUsageTrendInsights.get`
  * `recommender.cloudsqlInstanceDiskUsageTrendInsights.list`
  * `recommender.cloudsqlInstanceDiskUsageTrendInsights.update`

`recommender.cloudsqlInstanceMemoryUsageInsights.*`

  * `recommender.cloudsqlInstanceMemoryUsageInsights.get`
  * `recommender.cloudsqlInstanceMemoryUsageInsights.list`
  * `recommender.cloudsqlInstanceMemoryUsageInsights.update`

`recommender.cloudsqlInstanceOomProbabilityInsights.*`

  * `recommender.cloudsqlInstanceOomProbabilityInsights.get`
  * `recommender.cloudsqlInstanceOomProbabilityInsights.list`
  * `recommender.cloudsqlInstanceOomProbabilityInsights.update`

`recommender.cloudsqlInstanceOutOfDiskRecommendations.*`

  * `recommender.cloudsqlInstanceOutOfDiskRecommendations.get`
  * `recommender.cloudsqlInstanceOutOfDiskRecommendations.list`
  * `recommender.cloudsqlInstanceOutOfDiskRecommendations.update`

`recommender.cloudsqlInstancePerformanceInsights.*`

  * `recommender.cloudsqlInstancePerformanceInsights.get`
  * `recommender.cloudsqlInstancePerformanceInsights.list`
  * `recommender.cloudsqlInstancePerformanceInsights.update`

`recommender.cloudsqlInstancePerformanceRecommendations.*`

  * `recommender.cloudsqlInstancePerformanceRecommendations.get`
  * `recommender.cloudsqlInstancePerformanceRecommendations.list`
  * `recommender.cloudsqlInstancePerformanceRecommendations.update`

`recommender.cloudsqlInstanceReliabilityInsights.*`

  * `recommender.cloudsqlInstanceReliabilityInsights.get`
  * `recommender.cloudsqlInstanceReliabilityInsights.list`
  * `recommender.cloudsqlInstanceReliabilityInsights.update`

`recommender.cloudsqlInstanceReliabilityRecommendations.*`

  * `recommender.cloudsqlInstanceReliabilityRecommendations.get`
  * `recommender.cloudsqlInstanceReliabilityRecommendations.list`
  * `recommender.cloudsqlInstanceReliabilityRecommendations.update`

`recommender.cloudsqlInstanceSecurityInsights.*`

  * `recommender.cloudsqlInstanceSecurityInsights.get`
  * `recommender.cloudsqlInstanceSecurityInsights.list`
  * `recommender.cloudsqlInstanceSecurityInsights.update`

`recommender.cloudsqlInstanceSecurityRecommendations.*`

  * `recommender.cloudsqlInstanceSecurityRecommendations.get`
  * `recommender.cloudsqlInstanceSecurityRecommendations.list`
  * `recommender.cloudsqlInstanceSecurityRecommendations.update`

`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.*`

  * `recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.get`
  * `recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.list`
  * `recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.update`

`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.*`

  * `recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.get`
  * `recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.list`
  * `recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.update`

`recommender.cloudsqlOverprovisionedInstanceRecommendations.*`

  * `recommender.cloudsqlOverprovisionedInstanceRecommendations.get`
  * `recommender.cloudsqlOverprovisionedInstanceRecommendations.list`
  * `recommender.cloudsqlOverprovisionedInstanceRecommendations.update`

`recommender.cloudsqlUnderProvisionedInstanceRecommendations.*`

  * `recommender.cloudsqlUnderProvisionedInstanceRecommendations.get`
  * `recommender.cloudsqlUnderProvisionedInstanceRecommendations.list`
  * `recommender.cloudsqlUnderProvisionedInstanceRecommendations.update`

`recommender.containerDiagnosisInsights.*`

  * `recommender.containerDiagnosisInsights.get`
  * `recommender.containerDiagnosisInsights.list`
  * `recommender.containerDiagnosisInsights.update`

`recommender.containerDiagnosisRecommendations.*`

  * `recommender.containerDiagnosisRecommendations.get`
  * `recommender.containerDiagnosisRecommendations.list`
  * `recommender.containerDiagnosisRecommendations.update`

`recommender.iamPolicyInsights.*`

  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyInsights.update`

`recommender.iamPolicyRecommendations.*`

  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.networkAnalyzerGkeConnectivityInsights.*`

  * `recommender.networkAnalyzerGkeConnectivityInsights.get`
  * `recommender.networkAnalyzerGkeConnectivityInsights.list`
  * `recommender.networkAnalyzerGkeConnectivityInsights.update`

`recommender.networkAnalyzerGkeIpAddressInsights.*`

  * `recommender.networkAnalyzerGkeIpAddressInsights.get`
  * `recommender.networkAnalyzerGkeIpAddressInsights.list`
  * `recommender.networkAnalyzerGkeIpAddressInsights.update`

`recommender.storageBucketSoftDeleteInsights.*`

  * `recommender.storageBucketSoftDeleteInsights.get`
  * `recommender.storageBucketSoftDeleteInsights.list`
  * `recommender.storageBucketSoftDeleteInsights.update`

`recommender.storageBucketSoftDeleteRecommendations.*`

  * `recommender.storageBucketSoftDeleteRecommendations.get`
  * `recommender.storageBucketSoftDeleteRecommendations.list`
  * `recommender.storageBucketSoftDeleteRecommendations.update`

`resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `servicedirectory.namespaces.create` `servicedirectory.namespaces.delete` `servicedirectory.services.create` `servicedirectory.services.delete` `servicenetworking.operations.get` `servicenetworking.services.addPeering` `servicenetworking.services.createPeeredDnsDomain` `servicenetworking.services.deleteConnection` `servicenetworking.services.deletePeeredDnsDomain` `servicenetworking.services.disableVpcServiceControls` `servicenetworking.services.enableVpcServiceControls` `servicenetworking.services.get` `servicenetworking.services.getVpcServiceControls` `servicenetworking.services.listPeeredDnsDomains` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

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

`trafficdirector.*`

  * `trafficdirector.networks.getConfigs`
  * `trafficdirector.networks.reportMetrics`

  
  
### Roles for service agents

**Note:** **Cloud Composer v2 API Service Agent Extension** is an additional role for Cloud Composer API Service Agent in Managed Airflow (Gen 2). It is not granted automatically.Role | Permissions  
---|---  
  
#### Cloud Composer API Service Agent 

(`roles/composer.serviceAgent`) Cloud Composer API service agent can manage environments.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.applications.update` `appengine.instances.*`

  * `appengine.instances.delete`
  * `appengine.instances.enableDebug`
  * `appengine.instances.get`
  * `appengine.instances.list`

`appengine.memcache.addKey` `appengine.memcache.flush` `appengine.memcache.get` `appengine.memcache.update` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.runtimes.actAsAdmin` `appengine.services.*`

  * `appengine.services.delete`
  * `appengine.services.get`
  * `appengine.services.list`
  * `appengine.services.update`

`appengine.versions.create` `appengine.versions.delete` `appengine.versions.exportAppImage` `appengine.versions.get` `appengine.versions.list` `appengine.versions.update` `artifactregistry.projectsettings.get` `artifactregistry.repositories.create` `artifactregistry.repositories.delete` `artifactregistry.repositories.deleteArtifacts` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.update` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.get` `backupdr.backupPlanAssociations.createForCloudSqlInstance` `backupdr.backupPlanAssociations.createForComputeDisk` `backupdr.backupPlanAssociations.createForComputeInstance` `backupdr.backupPlanAssociations.deleteForCloudSqlInstance` `backupdr.backupPlanAssociations.deleteForComputeDisk` `backupdr.backupPlanAssociations.deleteForComputeInstance` `backupdr.backupPlanAssociations.fetchForCloudSqlInstance` `backupdr.backupPlanAssociations.fetchForComputeDisk` `backupdr.backupPlanAssociations.getForCloudSqlInstance` `backupdr.backupPlanAssociations.getForComputeDisk` `backupdr.backupPlanAssociations.list` `backupdr.backupPlanAssociations.triggerBackupForCloudSqlInstance` `backupdr.backupPlanAssociations.triggerBackupForComputeDisk` `backupdr.backupPlanAssociations.triggerBackupForComputeInstance` `backupdr.backupPlanAssociations.updateForCloudSqlInstance` `backupdr.backupPlanAssociations.updateForComputeDisk` `backupdr.backupPlanAssociations.updateForComputeInstance` `backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupPlans.useForCloudSqlInstance` `backupdr.backupPlans.useForComputeDisk` `backupdr.backupPlans.useForComputeInstance` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.bvbackups.fetchForCloudSqlInstance` `backupdr.bvbackups.useReadOnlyForCloudSqlInstance` `backupdr.bvdataSources.useReadOnlyForCloudSqlInstance` `backupdr.dataSourceReferences.fetchForCloudSqlInstance` `backupdr.dataSourceReferences.getForCloudSqlInstance` `backupdr.locations.list` `backupdr.operations.get` `backupdr.operations.list` `backupdr.serviceConfig.initialize` `cloudaicompanion.companions.*`

  * `cloudaicompanion.companions.generateChat`
  * `cloudaicompanion.companions.generateCode`

`cloudaicompanion.entitlements.get` `cloudaicompanion.instances.completeCode` `cloudaicompanion.instances.completeTask` `cloudaicompanion.instances.generateCode` `cloudnotifications.activities.list` `cloudsql.*`

  * `cloudsql.backupRuns.create`
  * `cloudsql.backupRuns.delete`
  * `cloudsql.backupRuns.export`
  * `cloudsql.backupRuns.get`
  * `cloudsql.backupRuns.list`
  * `cloudsql.backupRuns.update`
  * `cloudsql.blueGreenDeployments.create`
  * `cloudsql.blueGreenDeployments.delete`
  * `cloudsql.blueGreenDeployments.get`
  * `cloudsql.blueGreenDeployments.list`
  * `cloudsql.blueGreenDeployments.switchover`
  * `cloudsql.databases.create`
  * `cloudsql.databases.delete`
  * `cloudsql.databases.get`
  * `cloudsql.databases.list`
  * `cloudsql.databases.update`
  * `cloudsql.instances.addEntraIdCertificate`
  * `cloudsql.instances.addServerCa`
  * `cloudsql.instances.addServerCertificate`
  * `cloudsql.instances.cancelAgentSession`
  * `cloudsql.instances.clone`
  * `cloudsql.instances.connect`
  * `cloudsql.instances.create`
  * `cloudsql.instances.createBackupDrBackup`
  * `cloudsql.instances.createTagBinding`
  * `cloudsql.instances.createTestingAgentSession`
  * `cloudsql.instances.delete`
  * `cloudsql.instances.deleteTagBinding`
  * `cloudsql.instances.demoteMaster`
  * `cloudsql.instances.executeSql`
  * `cloudsql.instances.export`
  * `cloudsql.instances.failover`
  * `cloudsql.instances.get`
  * `cloudsql.instances.getAgentSession`
  * `cloudsql.instances.getDiskShrinkConfig`
  * `cloudsql.instances.import`
  * `cloudsql.instances.list`
  * `cloudsql.instances.listAgentSessions`
  * `cloudsql.instances.listEffectiveTags`
  * `cloudsql.instances.listEntraIdCertificates`
  * `cloudsql.instances.listServerCas`
  * `cloudsql.instances.listServerCertificates`
  * `cloudsql.instances.listTagBindings`
  * `cloudsql.instances.login`
  * `cloudsql.instances.manageEncryption`
  * `cloudsql.instances.migrate`
  * `cloudsql.instances.performDiskShrink`
  * `cloudsql.instances.preCheckMajorVersionUpgrade`
  * `cloudsql.instances.promoteReplica`
  * `cloudsql.instances.reencrypt`
  * `cloudsql.instances.resetReplicaSize`
  * `cloudsql.instances.resetSslConfig`
  * `cloudsql.instances.restart`
  * `cloudsql.instances.restoreBackup`
  * `cloudsql.instances.rotateEntraIdCertificate`
  * `cloudsql.instances.rotateServerCa`
  * `cloudsql.instances.rotateServerCertificate`
  * `cloudsql.instances.startReplica`
  * `cloudsql.instances.stopReplica`
  * `cloudsql.instances.truncateLog`
  * `cloudsql.instances.update`
  * `cloudsql.instances.updateBackupDrConfig`
  * `cloudsql.schemas.view`
  * `cloudsql.sslCerts.create`
  * `cloudsql.sslCerts.delete`
  * `cloudsql.sslCerts.get`
  * `cloudsql.sslCerts.list`
  * `cloudsql.users.create`
  * `cloudsql.users.delete`
  * `cloudsql.users.get`
  * `cloudsql.users.list`
  * `cloudsql.users.update`
  * `cloudsql.workloadCaptures.list`
  * `cloudsql.workloadCaptures.start`
  * `cloudsql.workloadCaptures.startReplay`
  * `cloudsql.workloadCaptures.stop`
  * `cloudsql.workloadCaptures.stopReplay`

`composer.dags.get` `composer.environments.get` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.*`

  * `compute.addresses.create`
  * `compute.addresses.createInternal`
  * `compute.addresses.createTagBinding`
  * `compute.addresses.delete`
  * `compute.addresses.deleteInternal`
  * `compute.addresses.deleteTagBinding`
  * `compute.addresses.get`
  * `compute.addresses.list`
  * `compute.addresses.listEffectiveTags`
  * `compute.addresses.listTagBindings`
  * `compute.addresses.setLabels`
  * `compute.addresses.use`
  * `compute.addresses.useInternal`

`compute.autoscalers.*`

  * `compute.autoscalers.create`
  * `compute.autoscalers.delete`
  * `compute.autoscalers.get`
  * `compute.autoscalers.list`
  * `compute.autoscalers.update`

`compute.backendBuckets.*`

  * `compute.backendBuckets.addSignedUrlKey`
  * `compute.backendBuckets.create`
  * `compute.backendBuckets.createTagBinding`
  * `compute.backendBuckets.delete`
  * `compute.backendBuckets.deleteSignedUrlKey`
  * `compute.backendBuckets.deleteTagBinding`
  * `compute.backendBuckets.get`
  * `compute.backendBuckets.getIamPolicy`
  * `compute.backendBuckets.list`
  * `compute.backendBuckets.listEffectiveTags`
  * `compute.backendBuckets.listTagBindings`
  * `compute.backendBuckets.setIamPolicy`
  * `compute.backendBuckets.setSecurityPolicy`
  * `compute.backendBuckets.update`
  * `compute.backendBuckets.use`

`compute.backendServices.*`

  * `compute.backendServices.addSignedUrlKey`
  * `compute.backendServices.create`
  * `compute.backendServices.createTagBinding`
  * `compute.backendServices.delete`
  * `compute.backendServices.deleteSignedUrlKey`
  * `compute.backendServices.deleteTagBinding`
  * `compute.backendServices.get`
  * `compute.backendServices.getIamPolicy`
  * `compute.backendServices.list`
  * `compute.backendServices.listEffectiveTags`
  * `compute.backendServices.listTagBindings`
  * `compute.backendServices.setIamPolicy`
  * `compute.backendServices.setSecurityPolicy`
  * `compute.backendServices.update`
  * `compute.backendServices.use`

`compute.crossSiteNetworks.*`

  * `compute.crossSiteNetworks.create`
  * `compute.crossSiteNetworks.delete`
  * `compute.crossSiteNetworks.get`
  * `compute.crossSiteNetworks.list`
  * `compute.crossSiteNetworks.update`

`compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.*`

  * `compute.disks.addResourcePolicies`
  * `compute.disks.create`
  * `compute.disks.createSnapshot`
  * `compute.disks.createTagBinding`
  * `compute.disks.delete`
  * `compute.disks.deleteTagBinding`
  * `compute.disks.get`
  * `compute.disks.getIamPolicy`
  * `compute.disks.list`
  * `compute.disks.listEffectiveTags`
  * `compute.disks.listTagBindings`
  * `compute.disks.removeResourcePolicies`
  * `compute.disks.resize`
  * `compute.disks.setIamPolicy`
  * `compute.disks.setLabels`
  * `compute.disks.startAsyncReplication`
  * `compute.disks.stopAsyncReplication`
  * `compute.disks.stopGroupAsyncReplication`
  * `compute.disks.update`
  * `compute.disks.updateKmsKey`
  * `compute.disks.use`
  * `compute.disks.useReadOnly`

`compute.externalVpnGateways.*`

  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.createTagBinding`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.deleteTagBinding`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.listEffectiveTags`
  * `compute.externalVpnGateways.listTagBindings`
  * `compute.externalVpnGateways.setLabels`
  * `compute.externalVpnGateways.use`

`compute.firewallPolicies.get` `compute.firewallPolicies.list` `compute.firewallPolicies.listEffectiveTags` `compute.firewallPolicies.listTagBindings` `compute.firewallPolicies.use` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.forwardingRules.*`

  * `compute.forwardingRules.create`
  * `compute.forwardingRules.createTagBinding`
  * `compute.forwardingRules.delete`
  * `compute.forwardingRules.deleteTagBinding`
  * `compute.forwardingRules.get`
  * `compute.forwardingRules.list`
  * `compute.forwardingRules.listEffectiveTags`
  * `compute.forwardingRules.listTagBindings`
  * `compute.forwardingRules.pscCreate`
  * `compute.forwardingRules.pscDelete`
  * `compute.forwardingRules.pscSetLabels`
  * `compute.forwardingRules.pscUpdate`
  * `compute.forwardingRules.setLabels`
  * `compute.forwardingRules.setTarget`
  * `compute.forwardingRules.update`
  * `compute.forwardingRules.use`

`compute.globalAddresses.*`

  * `compute.globalAddresses.create`
  * `compute.globalAddresses.createInternal`
  * `compute.globalAddresses.createTagBinding`
  * `compute.globalAddresses.delete`
  * `compute.globalAddresses.deleteInternal`
  * `compute.globalAddresses.deleteTagBinding`
  * `compute.globalAddresses.get`
  * `compute.globalAddresses.list`
  * `compute.globalAddresses.listEffectiveTags`
  * `compute.globalAddresses.listTagBindings`
  * `compute.globalAddresses.setLabels`
  * `compute.globalAddresses.use`

`compute.globalForwardingRules.*`

  * `compute.globalForwardingRules.create`
  * `compute.globalForwardingRules.createTagBinding`
  * `compute.globalForwardingRules.delete`
  * `compute.globalForwardingRules.deleteTagBinding`
  * `compute.globalForwardingRules.get`
  * `compute.globalForwardingRules.list`
  * `compute.globalForwardingRules.listEffectiveTags`
  * `compute.globalForwardingRules.listTagBindings`
  * `compute.globalForwardingRules.pscCreate`
  * `compute.globalForwardingRules.pscDelete`
  * `compute.globalForwardingRules.pscSetLabels`
  * `compute.globalForwardingRules.pscUpdate`
  * `compute.globalForwardingRules.setLabels`
  * `compute.globalForwardingRules.setTarget`
  * `compute.globalForwardingRules.update`

`compute.globalFrontendSettings.*`

  * `compute.globalFrontendSettings.get`
  * `compute.globalFrontendSettings.update`

`compute.globalNetworkEndpointGroups.*`

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

`compute.globalOperations.get` `compute.globalOperations.list` `compute.globalPublicDelegatedPrefixes.delete` `compute.globalPublicDelegatedPrefixes.get` `compute.globalPublicDelegatedPrefixes.list` `compute.globalPublicDelegatedPrefixes.updatePolicy` `compute.healthChecks.*`

  * `compute.healthChecks.create`
  * `compute.healthChecks.createTagBinding`
  * `compute.healthChecks.delete`
  * `compute.healthChecks.deleteTagBinding`
  * `compute.healthChecks.get`
  * `compute.healthChecks.list`
  * `compute.healthChecks.listEffectiveTags`
  * `compute.healthChecks.listTagBindings`
  * `compute.healthChecks.update`
  * `compute.healthChecks.use`
  * `compute.healthChecks.useReadOnly`

`compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.httpHealthChecks.*`

  * `compute.httpHealthChecks.create`
  * `compute.httpHealthChecks.createTagBinding`
  * `compute.httpHealthChecks.delete`
  * `compute.httpHealthChecks.deleteTagBinding`
  * `compute.httpHealthChecks.get`
  * `compute.httpHealthChecks.list`
  * `compute.httpHealthChecks.listEffectiveTags`
  * `compute.httpHealthChecks.listTagBindings`
  * `compute.httpHealthChecks.update`
  * `compute.httpHealthChecks.use`
  * `compute.httpHealthChecks.useReadOnly`

`compute.httpsHealthChecks.*`

  * `compute.httpsHealthChecks.create`
  * `compute.httpsHealthChecks.createTagBinding`
  * `compute.httpsHealthChecks.delete`
  * `compute.httpsHealthChecks.deleteTagBinding`
  * `compute.httpsHealthChecks.get`
  * `compute.httpsHealthChecks.list`
  * `compute.httpsHealthChecks.listEffectiveTags`
  * `compute.httpsHealthChecks.listTagBindings`
  * `compute.httpsHealthChecks.update`
  * `compute.httpsHealthChecks.use`
  * `compute.httpsHealthChecks.useReadOnly`

`compute.images.*`

  * `compute.images.create`
  * `compute.images.createTagBinding`
  * `compute.images.delete`
  * `compute.images.deleteTagBinding`
  * `compute.images.deprecate`
  * `compute.images.get`
  * `compute.images.getFromFamily`
  * `compute.images.getIamPolicy`
  * `compute.images.list`
  * `compute.images.listEffectiveTags`
  * `compute.images.listTagBindings`
  * `compute.images.setIamPolicy`
  * `compute.images.setLabels`
  * `compute.images.update`
  * `compute.images.useReadOnly`

`compute.instanceGroupManagers.*`

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

`compute.instanceSettings.*`

  * `compute.instanceSettings.get`
  * `compute.instanceSettings.update`

`compute.instanceTemplates.*`

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

`compute.instantSnapshotGroups.*`

  * `compute.instantSnapshotGroups.create`
  * `compute.instantSnapshotGroups.delete`
  * `compute.instantSnapshotGroups.get`
  * `compute.instantSnapshotGroups.getIamPolicy`
  * `compute.instantSnapshotGroups.list`
  * `compute.instantSnapshotGroups.setIamPolicy`
  * `compute.instantSnapshotGroups.useReadOnly`

`compute.instantSnapshots.create` `compute.instantSnapshots.delete` `compute.instantSnapshots.export` `compute.instantSnapshots.get` `compute.instantSnapshots.getIamPolicy` `compute.instantSnapshots.list` `compute.instantSnapshots.listEffectiveTags` `compute.instantSnapshots.listTagBindings` `compute.instantSnapshots.setIamPolicy` `compute.instantSnapshots.setLabels` `compute.instantSnapshots.useReadOnly` `compute.interconnectAttachmentGroups.*`

  * `compute.interconnectAttachmentGroups.create`
  * `compute.interconnectAttachmentGroups.delete`
  * `compute.interconnectAttachmentGroups.get`
  * `compute.interconnectAttachmentGroups.list`
  * `compute.interconnectAttachmentGroups.patch`

`compute.interconnectAttachments.*`

  * `compute.interconnectAttachments.create`
  * `compute.interconnectAttachments.createTagBinding`
  * `compute.interconnectAttachments.delete`
  * `compute.interconnectAttachments.deleteTagBinding`
  * `compute.interconnectAttachments.get`
  * `compute.interconnectAttachments.list`
  * `compute.interconnectAttachments.listEffectiveTags`
  * `compute.interconnectAttachments.listTagBindings`
  * `compute.interconnectAttachments.setLabels`
  * `compute.interconnectAttachments.update`
  * `compute.interconnectAttachments.use`

`compute.interconnectGroups.*`

  * `compute.interconnectGroups.create`
  * `compute.interconnectGroups.delete`
  * `compute.interconnectGroups.get`
  * `compute.interconnectGroups.list`
  * `compute.interconnectGroups.patch`

`compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.*`

  * `compute.interconnects.create`
  * `compute.interconnects.createTagBinding`
  * `compute.interconnects.delete`
  * `compute.interconnects.deleteTagBinding`
  * `compute.interconnects.get`
  * `compute.interconnects.getMacsecConfig`
  * `compute.interconnects.list`
  * `compute.interconnects.listEffectiveTags`
  * `compute.interconnects.listTagBindings`
  * `compute.interconnects.setLabels`
  * `compute.interconnects.setName`
  * `compute.interconnects.update`
  * `compute.interconnects.use`

`compute.licenseCodes.*`

  * `compute.licenseCodes.get`
  * `compute.licenseCodes.getIamPolicy`
  * `compute.licenseCodes.list`
  * `compute.licenseCodes.setIamPolicy`

`compute.licenses.create` `compute.licenses.delete` `compute.licenses.get` `compute.licenses.getIamPolicy` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.licenses.setIamPolicy` `compute.licenses.update` `compute.machineImages.create` `compute.machineImages.delete` `compute.machineImages.get` `compute.machineImages.getIamPolicy` `compute.machineImages.list` `compute.machineImages.listEffectiveTags` `compute.machineImages.listTagBindings` `compute.machineImages.setIamPolicy` `compute.machineImages.setLabels` `compute.machineImages.useReadOnly` `compute.machineTypes.*`

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

`compute.networkAttachments.*`

  * `compute.networkAttachments.create`
  * `compute.networkAttachments.createTagBinding`
  * `compute.networkAttachments.delete`
  * `compute.networkAttachments.deleteTagBinding`
  * `compute.networkAttachments.get`
  * `compute.networkAttachments.getIamPolicy`
  * `compute.networkAttachments.list`
  * `compute.networkAttachments.listEffectiveTags`
  * `compute.networkAttachments.listTagBindings`
  * `compute.networkAttachments.setIamPolicy`
  * `compute.networkAttachments.update`
  * `compute.networkAttachments.use`

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

`compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.*`

  * `compute.networks.access`
  * `compute.networks.addPeering`
  * `compute.networks.create`
  * `compute.networks.createTagBinding`
  * `compute.networks.delete`
  * `compute.networks.deleteTagBinding`
  * `compute.networks.get`
  * `compute.networks.getEffectiveFirewalls`
  * `compute.networks.getRegionEffectiveFirewalls`
  * `compute.networks.list`
  * `compute.networks.listEffectiveTags`
  * `compute.networks.listPeeringRoutes`
  * `compute.networks.listTagBindings`
  * `compute.networks.mirror`
  * `compute.networks.removePeering`
  * `compute.networks.setFirewallPolicy`
  * `compute.networks.setNetworkPolicy`
  * `compute.networks.switchToCustomMode`
  * `compute.networks.update`
  * `compute.networks.updatePeering`
  * `compute.networks.updatePolicy`
  * `compute.networks.use`
  * `compute.networks.useExternalIp`

`compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.packetMirrorings.listEffectiveTags` `compute.packetMirrorings.listTagBindings` `compute.projects.get` `compute.projects.setCommonInstanceMetadata` `compute.publicDelegatedPrefixes.delete` `compute.publicDelegatedPrefixes.get` `compute.publicDelegatedPrefixes.list` `compute.publicDelegatedPrefixes.listEffectiveTags` `compute.publicDelegatedPrefixes.listTagBindings` `compute.publicDelegatedPrefixes.update` `compute.publicDelegatedPrefixes.updatePolicy` `compute.recoverableSnapshots.*`

  * `compute.recoverableSnapshots.delete`
  * `compute.recoverableSnapshots.get`
  * `compute.recoverableSnapshots.getIamPolicy`
  * `compute.recoverableSnapshots.list`
  * `compute.recoverableSnapshots.recover`
  * `compute.recoverableSnapshots.setIamPolicy`

`compute.regionBackendBuckets.*`

  * `compute.regionBackendBuckets.create`
  * `compute.regionBackendBuckets.createTagBinding`
  * `compute.regionBackendBuckets.delete`
  * `compute.regionBackendBuckets.deleteTagBinding`
  * `compute.regionBackendBuckets.get`
  * `compute.regionBackendBuckets.getIamPolicy`
  * `compute.regionBackendBuckets.list`
  * `compute.regionBackendBuckets.listEffectiveTags`
  * `compute.regionBackendBuckets.listTagBindings`
  * `compute.regionBackendBuckets.setIamPolicy`
  * `compute.regionBackendBuckets.update`
  * `compute.regionBackendBuckets.use`

`compute.regionBackendServices.*`

  * `compute.regionBackendServices.create`
  * `compute.regionBackendServices.createTagBinding`
  * `compute.regionBackendServices.delete`
  * `compute.regionBackendServices.deleteTagBinding`
  * `compute.regionBackendServices.get`
  * `compute.regionBackendServices.getIamPolicy`
  * `compute.regionBackendServices.list`
  * `compute.regionBackendServices.listEffectiveTags`
  * `compute.regionBackendServices.listTagBindings`
  * `compute.regionBackendServices.setIamPolicy`
  * `compute.regionBackendServices.setSecurityPolicy`
  * `compute.regionBackendServices.update`
  * `compute.regionBackendServices.use`

`compute.regionCompositeHealthChecks.*`

  * `compute.regionCompositeHealthChecks.create`
  * `compute.regionCompositeHealthChecks.delete`
  * `compute.regionCompositeHealthChecks.get`
  * `compute.regionCompositeHealthChecks.list`
  * `compute.regionCompositeHealthChecks.update`

`compute.regionFirewallPolicies.get` `compute.regionFirewallPolicies.list` `compute.regionFirewallPolicies.listEffectiveTags` `compute.regionFirewallPolicies.listTagBindings` `compute.regionFirewallPolicies.use` `compute.regionHealthAggregationPolicies.*`

  * `compute.regionHealthAggregationPolicies.create`
  * `compute.regionHealthAggregationPolicies.delete`
  * `compute.regionHealthAggregationPolicies.get`
  * `compute.regionHealthAggregationPolicies.list`
  * `compute.regionHealthAggregationPolicies.update`

`compute.regionHealthCheckServices.*`

  * `compute.regionHealthCheckServices.create`
  * `compute.regionHealthCheckServices.delete`
  * `compute.regionHealthCheckServices.get`
  * `compute.regionHealthCheckServices.list`
  * `compute.regionHealthCheckServices.update`
  * `compute.regionHealthCheckServices.use`

`compute.regionHealthChecks.*`

  * `compute.regionHealthChecks.create`
  * `compute.regionHealthChecks.createTagBinding`
  * `compute.regionHealthChecks.delete`
  * `compute.regionHealthChecks.deleteTagBinding`
  * `compute.regionHealthChecks.get`
  * `compute.regionHealthChecks.list`
  * `compute.regionHealthChecks.listEffectiveTags`
  * `compute.regionHealthChecks.listTagBindings`
  * `compute.regionHealthChecks.update`
  * `compute.regionHealthChecks.use`
  * `compute.regionHealthChecks.useReadOnly`

`compute.regionHealthSources.*`

  * `compute.regionHealthSources.create`
  * `compute.regionHealthSources.delete`
  * `compute.regionHealthSources.get`
  * `compute.regionHealthSources.list`
  * `compute.regionHealthSources.update`

`compute.regionNetworkEndpointGroups.*`

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

`compute.regionNetworkPolicies.*`

  * `compute.regionNetworkPolicies.create`
  * `compute.regionNetworkPolicies.delete`
  * `compute.regionNetworkPolicies.get`
  * `compute.regionNetworkPolicies.list`
  * `compute.regionNetworkPolicies.update`
  * `compute.regionNetworkPolicies.use`

`compute.regionNotificationEndpoints.*`

  * `compute.regionNotificationEndpoints.create`
  * `compute.regionNotificationEndpoints.delete`
  * `compute.regionNotificationEndpoints.get`
  * `compute.regionNotificationEndpoints.list`
  * `compute.regionNotificationEndpoints.update`
  * `compute.regionNotificationEndpoints.use`

`compute.regionOperations.get` `compute.regionOperations.list` `compute.regionSecurityPolicies.get` `compute.regionSecurityPolicies.list` `compute.regionSecurityPolicies.listEffectiveTags` `compute.regionSecurityPolicies.listTagBindings` `compute.regionSecurityPolicies.use` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.*`

  * `compute.regionSslPolicies.create`
  * `compute.regionSslPolicies.createTagBinding`
  * `compute.regionSslPolicies.delete`
  * `compute.regionSslPolicies.deleteTagBinding`
  * `compute.regionSslPolicies.get`
  * `compute.regionSslPolicies.getIamPolicy`
  * `compute.regionSslPolicies.list`
  * `compute.regionSslPolicies.listAvailableFeatures`
  * `compute.regionSslPolicies.listEffectiveTags`
  * `compute.regionSslPolicies.listTagBindings`
  * `compute.regionSslPolicies.setIamPolicy`
  * `compute.regionSslPolicies.update`
  * `compute.regionSslPolicies.use`

`compute.regionTargetHttpProxies.*`

  * `compute.regionTargetHttpProxies.create`
  * `compute.regionTargetHttpProxies.createTagBinding`
  * `compute.regionTargetHttpProxies.delete`
  * `compute.regionTargetHttpProxies.deleteTagBinding`
  * `compute.regionTargetHttpProxies.get`
  * `compute.regionTargetHttpProxies.list`
  * `compute.regionTargetHttpProxies.listEffectiveTags`
  * `compute.regionTargetHttpProxies.listTagBindings`
  * `compute.regionTargetHttpProxies.setUrlMap`
  * `compute.regionTargetHttpProxies.use`

`compute.regionTargetHttpsProxies.*`

  * `compute.regionTargetHttpsProxies.create`
  * `compute.regionTargetHttpsProxies.createTagBinding`
  * `compute.regionTargetHttpsProxies.delete`
  * `compute.regionTargetHttpsProxies.deleteTagBinding`
  * `compute.regionTargetHttpsProxies.get`
  * `compute.regionTargetHttpsProxies.list`
  * `compute.regionTargetHttpsProxies.listEffectiveTags`
  * `compute.regionTargetHttpsProxies.listTagBindings`
  * `compute.regionTargetHttpsProxies.setSslCertificates`
  * `compute.regionTargetHttpsProxies.setUrlMap`
  * `compute.regionTargetHttpsProxies.update`
  * `compute.regionTargetHttpsProxies.use`

`compute.regionTargetTcpProxies.*`

  * `compute.regionTargetTcpProxies.attach`
  * `compute.regionTargetTcpProxies.create`
  * `compute.regionTargetTcpProxies.createTagBinding`
  * `compute.regionTargetTcpProxies.delete`
  * `compute.regionTargetTcpProxies.deleteTagBinding`
  * `compute.regionTargetTcpProxies.get`
  * `compute.regionTargetTcpProxies.list`
  * `compute.regionTargetTcpProxies.listEffectiveTags`
  * `compute.regionTargetTcpProxies.listTagBindings`
  * `compute.regionTargetTcpProxies.use`

`compute.regionUrlMaps.*`

  * `compute.regionUrlMaps.create`
  * `compute.regionUrlMaps.createTagBinding`
  * `compute.regionUrlMaps.delete`
  * `compute.regionUrlMaps.deleteTagBinding`
  * `compute.regionUrlMaps.get`
  * `compute.regionUrlMaps.invalidateCache`
  * `compute.regionUrlMaps.list`
  * `compute.regionUrlMaps.listEffectiveTags`
  * `compute.regionUrlMaps.listTagBindings`
  * `compute.regionUrlMaps.update`
  * `compute.regionUrlMaps.use`
  * `compute.regionUrlMaps.validate`

`compute.regions.*`

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

`compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.*`

  * `compute.resourcePolicies.create`
  * `compute.resourcePolicies.delete`
  * `compute.resourcePolicies.get`
  * `compute.resourcePolicies.getIamPolicy`
  * `compute.resourcePolicies.list`
  * `compute.resourcePolicies.setIamPolicy`
  * `compute.resourcePolicies.update`
  * `compute.resourcePolicies.use`
  * `compute.resourcePolicies.useReadOnly`

`compute.routers.*`

  * `compute.routers.create`
  * `compute.routers.createTagBinding`
  * `compute.routers.delete`
  * `compute.routers.deleteRoutePolicy`
  * `compute.routers.deleteTagBinding`
  * `compute.routers.get`
  * `compute.routers.getRoutePolicy`
  * `compute.routers.list`
  * `compute.routers.listBgpRoutes`
  * `compute.routers.listEffectiveTags`
  * `compute.routers.listRoutePolicies`
  * `compute.routers.listTagBindings`
  * `compute.routers.update`
  * `compute.routers.updateRoutePolicy`
  * `compute.routers.use`

`compute.routes.*`

  * `compute.routes.create`
  * `compute.routes.createTagBinding`
  * `compute.routes.delete`
  * `compute.routes.deleteTagBinding`
  * `compute.routes.get`
  * `compute.routes.list`
  * `compute.routes.listEffectiveTags`
  * `compute.routes.listTagBindings`

`compute.securityPolicies.get` `compute.securityPolicies.list` `compute.securityPolicies.listEffectiveTags` `compute.securityPolicies.listTagBindings` `compute.securityPolicies.use` `compute.serviceAttachments.*`

  * `compute.serviceAttachments.create`
  * `compute.serviceAttachments.createTagBinding`
  * `compute.serviceAttachments.delete`
  * `compute.serviceAttachments.deleteTagBinding`
  * `compute.serviceAttachments.get`
  * `compute.serviceAttachments.getIamPolicy`
  * `compute.serviceAttachments.list`
  * `compute.serviceAttachments.listEffectiveTags`
  * `compute.serviceAttachments.listTagBindings`
  * `compute.serviceAttachments.setIamPolicy`
  * `compute.serviceAttachments.update`
  * `compute.serviceAttachments.use`

`compute.snapshotGroups.*`

  * `compute.snapshotGroups.create`
  * `compute.snapshotGroups.delete`
  * `compute.snapshotGroups.get`
  * `compute.snapshotGroups.getIamPolicy`
  * `compute.snapshotGroups.list`
  * `compute.snapshotGroups.setIamPolicy`
  * `compute.snapshotGroups.useReadOnly`

`compute.snapshots.*`

  * `compute.snapshots.create`
  * `compute.snapshots.createTagBinding`
  * `compute.snapshots.delete`
  * `compute.snapshots.deleteTagBinding`
  * `compute.snapshots.get`
  * `compute.snapshots.getEffectiveRecycleBinRule`
  * `compute.snapshots.getIamPolicy`
  * `compute.snapshots.list`
  * `compute.snapshots.listEffectiveTags`
  * `compute.snapshots.listTagBindings`
  * `compute.snapshots.setIamPolicy`
  * `compute.snapshots.setLabels`
  * `compute.snapshots.updateKmsKey`
  * `compute.snapshots.useReadOnly`

`compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.*`

  * `compute.sslPolicies.create`
  * `compute.sslPolicies.createTagBinding`
  * `compute.sslPolicies.delete`
  * `compute.sslPolicies.deleteTagBinding`
  * `compute.sslPolicies.get`
  * `compute.sslPolicies.getIamPolicy`
  * `compute.sslPolicies.list`
  * `compute.sslPolicies.listAvailableFeatures`
  * `compute.sslPolicies.listEffectiveTags`
  * `compute.sslPolicies.listTagBindings`
  * `compute.sslPolicies.setIamPolicy`
  * `compute.sslPolicies.update`
  * `compute.sslPolicies.use`

`compute.storagePools.get` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.storagePools.use` `compute.subnetworks.*`

  * `compute.subnetworks.create`
  * `compute.subnetworks.createTagBinding`
  * `compute.subnetworks.delete`
  * `compute.subnetworks.deleteTagBinding`
  * `compute.subnetworks.expandIpCidrRange`
  * `compute.subnetworks.get`
  * `compute.subnetworks.getIamPolicy`
  * `compute.subnetworks.list`
  * `compute.subnetworks.listEffectiveTags`
  * `compute.subnetworks.listTagBindings`
  * `compute.subnetworks.mirror`
  * `compute.subnetworks.setIamPolicy`
  * `compute.subnetworks.setPrivateIpGoogleAccess`
  * `compute.subnetworks.update`
  * `compute.subnetworks.use`
  * `compute.subnetworks.useExternalIp`
  * `compute.subnetworks.usePeerMigration`

`compute.targetGrpcProxies.*`

  * `compute.targetGrpcProxies.create`
  * `compute.targetGrpcProxies.createTagBinding`
  * `compute.targetGrpcProxies.delete`
  * `compute.targetGrpcProxies.deleteTagBinding`
  * `compute.targetGrpcProxies.get`
  * `compute.targetGrpcProxies.list`
  * `compute.targetGrpcProxies.listEffectiveTags`
  * `compute.targetGrpcProxies.listTagBindings`
  * `compute.targetGrpcProxies.update`
  * `compute.targetGrpcProxies.use`

`compute.targetHttpProxies.*`

  * `compute.targetHttpProxies.create`
  * `compute.targetHttpProxies.createTagBinding`
  * `compute.targetHttpProxies.delete`
  * `compute.targetHttpProxies.deleteTagBinding`
  * `compute.targetHttpProxies.get`
  * `compute.targetHttpProxies.list`
  * `compute.targetHttpProxies.listEffectiveTags`
  * `compute.targetHttpProxies.listTagBindings`
  * `compute.targetHttpProxies.setUrlMap`
  * `compute.targetHttpProxies.update`
  * `compute.targetHttpProxies.use`

`compute.targetHttpsProxies.*`

  * `compute.targetHttpsProxies.create`
  * `compute.targetHttpsProxies.createTagBinding`
  * `compute.targetHttpsProxies.delete`
  * `compute.targetHttpsProxies.deleteTagBinding`
  * `compute.targetHttpsProxies.get`
  * `compute.targetHttpsProxies.list`
  * `compute.targetHttpsProxies.listEffectiveTags`
  * `compute.targetHttpsProxies.listTagBindings`
  * `compute.targetHttpsProxies.setCertificateMap`
  * `compute.targetHttpsProxies.setQuicOverride`
  * `compute.targetHttpsProxies.setSslCertificates`
  * `compute.targetHttpsProxies.setSslPolicy`
  * `compute.targetHttpsProxies.setUrlMap`
  * `compute.targetHttpsProxies.update`
  * `compute.targetHttpsProxies.use`

`compute.targetInstances.*`

  * `compute.targetInstances.create`
  * `compute.targetInstances.createTagBinding`
  * `compute.targetInstances.delete`
  * `compute.targetInstances.deleteTagBinding`
  * `compute.targetInstances.get`
  * `compute.targetInstances.list`
  * `compute.targetInstances.listEffectiveTags`
  * `compute.targetInstances.listTagBindings`
  * `compute.targetInstances.setSecurityPolicy`
  * `compute.targetInstances.use`

`compute.targetPools.*`

  * `compute.targetPools.addHealthCheck`
  * `compute.targetPools.addInstance`
  * `compute.targetPools.create`
  * `compute.targetPools.createTagBinding`
  * `compute.targetPools.delete`
  * `compute.targetPools.deleteTagBinding`
  * `compute.targetPools.get`
  * `compute.targetPools.list`
  * `compute.targetPools.listEffectiveTags`
  * `compute.targetPools.listTagBindings`
  * `compute.targetPools.removeHealthCheck`
  * `compute.targetPools.removeInstance`
  * `compute.targetPools.setSecurityPolicy`
  * `compute.targetPools.update`
  * `compute.targetPools.use`

`compute.targetSslProxies.*`

  * `compute.targetSslProxies.create`
  * `compute.targetSslProxies.createTagBinding`
  * `compute.targetSslProxies.delete`
  * `compute.targetSslProxies.deleteTagBinding`
  * `compute.targetSslProxies.get`
  * `compute.targetSslProxies.list`
  * `compute.targetSslProxies.listEffectiveTags`
  * `compute.targetSslProxies.listTagBindings`
  * `compute.targetSslProxies.setBackendService`
  * `compute.targetSslProxies.setCertificateMap`
  * `compute.targetSslProxies.setProxyHeader`
  * `compute.targetSslProxies.setSslCertificates`
  * `compute.targetSslProxies.setSslPolicy`
  * `compute.targetSslProxies.update`
  * `compute.targetSslProxies.use`

`compute.targetTcpProxies.*`

  * `compute.targetTcpProxies.attach`
  * `compute.targetTcpProxies.create`
  * `compute.targetTcpProxies.createTagBinding`
  * `compute.targetTcpProxies.delete`
  * `compute.targetTcpProxies.deleteTagBinding`
  * `compute.targetTcpProxies.get`
  * `compute.targetTcpProxies.list`
  * `compute.targetTcpProxies.listEffectiveTags`
  * `compute.targetTcpProxies.listTagBindings`
  * `compute.targetTcpProxies.update`
  * `compute.targetTcpProxies.use`

`compute.targetVpnGateways.*`

  * `compute.targetVpnGateways.create`
  * `compute.targetVpnGateways.createTagBinding`
  * `compute.targetVpnGateways.delete`
  * `compute.targetVpnGateways.deleteTagBinding`
  * `compute.targetVpnGateways.get`
  * `compute.targetVpnGateways.list`
  * `compute.targetVpnGateways.listEffectiveTags`
  * `compute.targetVpnGateways.listTagBindings`
  * `compute.targetVpnGateways.setLabels`
  * `compute.targetVpnGateways.use`

`compute.urlMaps.*`

  * `compute.urlMaps.create`
  * `compute.urlMaps.createTagBinding`
  * `compute.urlMaps.delete`
  * `compute.urlMaps.deleteTagBinding`
  * `compute.urlMaps.get`
  * `compute.urlMaps.invalidateCache`
  * `compute.urlMaps.list`
  * `compute.urlMaps.listEffectiveTags`
  * `compute.urlMaps.listTagBindings`
  * `compute.urlMaps.update`
  * `compute.urlMaps.use`
  * `compute.urlMaps.validate`

`compute.vpnGateways.*`

  * `compute.vpnGateways.create`
  * `compute.vpnGateways.createTagBinding`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.deleteTagBinding`
  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.listEffectiveTags`
  * `compute.vpnGateways.listTagBindings`
  * `compute.vpnGateways.setLabels`
  * `compute.vpnGateways.use`

`compute.vpnTunnels.*`

  * `compute.vpnTunnels.create`
  * `compute.vpnTunnels.createTagBinding`
  * `compute.vpnTunnels.delete`
  * `compute.vpnTunnels.deleteTagBinding`
  * `compute.vpnTunnels.get`
  * `compute.vpnTunnels.list`
  * `compute.vpnTunnels.listEffectiveTags`
  * `compute.vpnTunnels.listTagBindings`
  * `compute.vpnTunnels.setLabels`

`compute.wireGroups.*`

  * `compute.wireGroups.create`
  * `compute.wireGroups.delete`
  * `compute.wireGroups.get`
  * `compute.wireGroups.list`
  * `compute.wireGroups.update`

`compute.zoneOperations.get` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`container.*`

  * `container.apiServices.create`
  * `container.apiServices.delete`
  * `container.apiServices.get`
  * `container.apiServices.getStatus`
  * `container.apiServices.list`
  * `container.apiServices.update`
  * `container.apiServices.updateStatus`
  * `container.auditSinks.create`
  * `container.auditSinks.delete`
  * `container.auditSinks.get`
  * `container.auditSinks.list`
  * `container.auditSinks.update`
  * `container.backendConfigs.create`
  * `container.backendConfigs.delete`
  * `container.backendConfigs.get`
  * `container.backendConfigs.list`
  * `container.backendConfigs.update`
  * `container.bindings.create`
  * `container.bindings.delete`
  * `container.bindings.get`
  * `container.bindings.list`
  * `container.bindings.update`
  * `container.certificateSigningRequests.approve`
  * `container.certificateSigningRequests.create`
  * `container.certificateSigningRequests.delete`
  * `container.certificateSigningRequests.get`
  * `container.certificateSigningRequests.getStatus`
  * `container.certificateSigningRequests.list`
  * `container.certificateSigningRequests.update`
  * `container.certificateSigningRequests.updateStatus`
  * `container.clusterRoleBindings.create`
  * `container.clusterRoleBindings.delete`
  * `container.clusterRoleBindings.get`
  * `container.clusterRoleBindings.list`
  * `container.clusterRoleBindings.update`
  * `container.clusterRoles.bind`
  * `container.clusterRoles.create`
  * `container.clusterRoles.delete`
  * `container.clusterRoles.escalate`
  * `container.clusterRoles.get`
  * `container.clusterRoles.list`
  * `container.clusterRoles.update`
  * `container.clusters.connect`
  * `container.clusters.create`
  * `container.clusters.createTagBinding`
  * `container.clusters.delete`
  * `container.clusters.deleteTagBinding`
  * `container.clusters.get`
  * `container.clusters.getCredentials`
  * `container.clusters.impersonate`
  * `container.clusters.list`
  * `container.clusters.listEffectiveTags`
  * `container.clusters.listTagBindings`
  * `container.clusters.update`
  * `container.componentStatuses.get`
  * `container.componentStatuses.list`
  * `container.configMaps.create`
  * `container.configMaps.delete`
  * `container.configMaps.get`
  * `container.configMaps.list`
  * `container.configMaps.update`
  * `container.controllerRevisions.create`
  * `container.controllerRevisions.delete`
  * `container.controllerRevisions.get`
  * `container.controllerRevisions.list`
  * `container.controllerRevisions.update`
  * `container.cronJobs.create`
  * `container.cronJobs.delete`
  * `container.cronJobs.get`
  * `container.cronJobs.getStatus`
  * `container.cronJobs.list`
  * `container.cronJobs.update`
  * `container.cronJobs.updateStatus`
  * `container.csiDrivers.create`
  * `container.csiDrivers.delete`
  * `container.csiDrivers.get`
  * `container.csiDrivers.list`
  * `container.csiDrivers.update`
  * `container.csiNodeInfos.create`
  * `container.csiNodeInfos.delete`
  * `container.csiNodeInfos.get`
  * `container.csiNodeInfos.list`
  * `container.csiNodeInfos.update`
  * `container.csiNodes.create`
  * `container.csiNodes.delete`
  * `container.csiNodes.get`
  * `container.csiNodes.list`
  * `container.csiNodes.update`
  * `container.customResourceDefinitions.create`
  * `container.customResourceDefinitions.delete`
  * `container.customResourceDefinitions.get`
  * `container.customResourceDefinitions.getStatus`
  * `container.customResourceDefinitions.list`
  * `container.customResourceDefinitions.update`
  * `container.customResourceDefinitions.updateStatus`
  * `container.daemonSets.create`
  * `container.daemonSets.delete`
  * `container.daemonSets.get`
  * `container.daemonSets.getStatus`
  * `container.daemonSets.list`
  * `container.daemonSets.update`
  * `container.daemonSets.updateStatus`
  * `container.deployments.create`
  * `container.deployments.delete`
  * `container.deployments.get`
  * `container.deployments.getScale`
  * `container.deployments.getStatus`
  * `container.deployments.list`
  * `container.deployments.rollback`
  * `container.deployments.update`
  * `container.deployments.updateScale`
  * `container.deployments.updateStatus`
  * `container.endpointSlices.create`
  * `container.endpointSlices.delete`
  * `container.endpointSlices.get`
  * `container.endpointSlices.list`
  * `container.endpointSlices.update`
  * `container.endpoints.create`
  * `container.endpoints.delete`
  * `container.endpoints.get`
  * `container.endpoints.list`
  * `container.endpoints.update`
  * `container.events.create`
  * `container.events.delete`
  * `container.events.get`
  * `container.events.list`
  * `container.events.update`
  * `container.frontendConfigs.create`
  * `container.frontendConfigs.delete`
  * `container.frontendConfigs.get`
  * `container.frontendConfigs.list`
  * `container.frontendConfigs.update`
  * `container.horizontalPodAutoscalers.create`
  * `container.horizontalPodAutoscalers.delete`
  * `container.horizontalPodAutoscalers.get`
  * `container.horizontalPodAutoscalers.getStatus`
  * `container.horizontalPodAutoscalers.list`
  * `container.horizontalPodAutoscalers.update`
  * `container.horizontalPodAutoscalers.updateStatus`
  * `container.hostServiceAgent.use`
  * `container.ingresses.create`
  * `container.ingresses.delete`
  * `container.ingresses.get`
  * `container.ingresses.getStatus`
  * `container.ingresses.list`
  * `container.ingresses.update`
  * `container.ingresses.updateStatus`
  * `container.initializerConfigurations.create`
  * `container.initializerConfigurations.delete`
  * `container.initializerConfigurations.get`
  * `container.initializerConfigurations.list`
  * `container.initializerConfigurations.update`
  * `container.jobs.create`
  * `container.jobs.delete`
  * `container.jobs.get`
  * `container.jobs.getStatus`
  * `container.jobs.list`
  * `container.jobs.update`
  * `container.jobs.updateStatus`
  * `container.leases.create`
  * `container.leases.delete`
  * `container.leases.get`
  * `container.leases.list`
  * `container.leases.update`
  * `container.limitRanges.create`
  * `container.limitRanges.delete`
  * `container.limitRanges.get`
  * `container.limitRanges.list`
  * `container.limitRanges.update`
  * `container.localSubjectAccessReviews.create`
  * `container.localSubjectAccessReviews.list`
  * `container.managedCertificates.create`
  * `container.managedCertificates.delete`
  * `container.managedCertificates.get`
  * `container.managedCertificates.list`
  * `container.managedCertificates.update`
  * `container.mutatingWebhookConfigurations.create`
  * `container.mutatingWebhookConfigurations.delete`
  * `container.mutatingWebhookConfigurations.get`
  * `container.mutatingWebhookConfigurations.list`
  * `container.mutatingWebhookConfigurations.update`
  * `container.namespaces.create`
  * `container.namespaces.delete`
  * `container.namespaces.finalize`
  * `container.namespaces.get`
  * `container.namespaces.getStatus`
  * `container.namespaces.list`
  * `container.namespaces.update`
  * `container.namespaces.updateStatus`
  * `container.networkPolicies.create`
  * `container.networkPolicies.delete`
  * `container.networkPolicies.get`
  * `container.networkPolicies.list`
  * `container.networkPolicies.update`
  * `container.nodes.create`
  * `container.nodes.delete`
  * `container.nodes.get`
  * `container.nodes.getStatus`
  * `container.nodes.list`
  * `container.nodes.proxy`
  * `container.nodes.update`
  * `container.nodes.updateStatus`
  * `container.operations.get`
  * `container.operations.list`
  * `container.persistentVolumeClaims.create`
  * `container.persistentVolumeClaims.delete`
  * `container.persistentVolumeClaims.get`
  * `container.persistentVolumeClaims.getStatus`
  * `container.persistentVolumeClaims.list`
  * `container.persistentVolumeClaims.update`
  * `container.persistentVolumeClaims.updateStatus`
  * `container.persistentVolumes.create`
  * `container.persistentVolumes.delete`
  * `container.persistentVolumes.get`
  * `container.persistentVolumes.getStatus`
  * `container.persistentVolumes.list`
  * `container.persistentVolumes.update`
  * `container.persistentVolumes.updateStatus`
  * `container.petSets.create`
  * `container.petSets.delete`
  * `container.petSets.get`
  * `container.petSets.list`
  * `container.petSets.update`
  * `container.petSets.updateStatus`
  * `container.podDisruptionBudgets.create`
  * `container.podDisruptionBudgets.delete`
  * `container.podDisruptionBudgets.get`
  * `container.podDisruptionBudgets.getStatus`
  * `container.podDisruptionBudgets.list`
  * `container.podDisruptionBudgets.update`
  * `container.podDisruptionBudgets.updateStatus`
  * `container.podPresets.create`
  * `container.podPresets.delete`
  * `container.podPresets.get`
  * `container.podPresets.list`
  * `container.podPresets.update`
  * `container.podSecurityPolicies.create`
  * `container.podSecurityPolicies.delete`
  * `container.podSecurityPolicies.get`
  * `container.podSecurityPolicies.list`
  * `container.podSecurityPolicies.update`
  * `container.podSecurityPolicies.use`
  * `container.podTemplates.create`
  * `container.podTemplates.delete`
  * `container.podTemplates.get`
  * `container.podTemplates.list`
  * `container.podTemplates.update`
  * `container.pods.attach`
  * `container.pods.create`
  * `container.pods.delete`
  * `container.pods.evict`
  * `container.pods.exec`
  * `container.pods.get`
  * `container.pods.getLogs`
  * `container.pods.getStatus`
  * `container.pods.initialize`
  * `container.pods.list`
  * `container.pods.portForward`
  * `container.pods.proxy`
  * `container.pods.update`
  * `container.pods.updateStatus`
  * `container.priorityClasses.create`
  * `container.priorityClasses.delete`
  * `container.priorityClasses.get`
  * `container.priorityClasses.list`
  * `container.priorityClasses.update`
  * `container.replicaSets.create`
  * `container.replicaSets.delete`
  * `container.replicaSets.get`
  * `container.replicaSets.getScale`
  * `container.replicaSets.getStatus`
  * `container.replicaSets.list`
  * `container.replicaSets.update`
  * `container.replicaSets.updateScale`
  * `container.replicaSets.updateStatus`
  * `container.replicationControllers.create`
  * `container.replicationControllers.delete`
  * `container.replicationControllers.get`
  * `container.replicationControllers.getScale`
  * `container.replicationControllers.getStatus`
  * `container.replicationControllers.list`
  * `container.replicationControllers.update`
  * `container.replicationControllers.updateScale`
  * `container.replicationControllers.updateStatus`
  * `container.resourceQuotas.create`
  * `container.resourceQuotas.delete`
  * `container.resourceQuotas.get`
  * `container.resourceQuotas.getStatus`
  * `container.resourceQuotas.list`
  * `container.resourceQuotas.update`
  * `container.resourceQuotas.updateStatus`
  * `container.roleBindings.create`
  * `container.roleBindings.delete`
  * `container.roleBindings.get`
  * `container.roleBindings.list`
  * `container.roleBindings.update`
  * `container.roles.bind`
  * `container.roles.create`
  * `container.roles.delete`
  * `container.roles.escalate`
  * `container.roles.get`
  * `container.roles.list`
  * `container.roles.update`
  * `container.runtimeClasses.create`
  * `container.runtimeClasses.delete`
  * `container.runtimeClasses.get`
  * `container.runtimeClasses.list`
  * `container.runtimeClasses.update`
  * `container.scheduledJobs.create`
  * `container.scheduledJobs.delete`
  * `container.scheduledJobs.get`
  * `container.scheduledJobs.list`
  * `container.scheduledJobs.update`
  * `container.scheduledJobs.updateStatus`
  * `container.secrets.create`
  * `container.secrets.delete`
  * `container.secrets.get`
  * `container.secrets.list`
  * `container.secrets.update`
  * `container.selfSubjectAccessReviews.create`
  * `container.selfSubjectAccessReviews.list`
  * `container.selfSubjectRulesReviews.create`
  * `container.serviceAccounts.create`
  * `container.serviceAccounts.createToken`
  * `container.serviceAccounts.delete`
  * `container.serviceAccounts.get`
  * `container.serviceAccounts.list`
  * `container.serviceAccounts.update`
  * `container.services.create`
  * `container.services.delete`
  * `container.services.get`
  * `container.services.getStatus`
  * `container.services.list`
  * `container.services.proxy`
  * `container.services.update`
  * `container.services.updateStatus`
  * `container.statefulSets.create`
  * `container.statefulSets.delete`
  * `container.statefulSets.get`
  * `container.statefulSets.getScale`
  * `container.statefulSets.getStatus`
  * `container.statefulSets.list`
  * `container.statefulSets.update`
  * `container.statefulSets.updateScale`
  * `container.statefulSets.updateStatus`
  * `container.storageClasses.create`
  * `container.storageClasses.delete`
  * `container.storageClasses.get`
  * `container.storageClasses.list`
  * `container.storageClasses.update`
  * `container.storageStates.create`
  * `container.storageStates.delete`
  * `container.storageStates.get`
  * `container.storageStates.getStatus`
  * `container.storageStates.list`
  * `container.storageStates.update`
  * `container.storageStates.updateStatus`
  * `container.storageVersionMigrations.create`
  * `container.storageVersionMigrations.delete`
  * `container.storageVersionMigrations.get`
  * `container.storageVersionMigrations.getStatus`
  * `container.storageVersionMigrations.list`
  * `container.storageVersionMigrations.update`
  * `container.storageVersionMigrations.updateStatus`
  * `container.subjectAccessReviews.create`
  * `container.subjectAccessReviews.list`
  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`
  * `container.thirdPartyResources.create`
  * `container.thirdPartyResources.delete`
  * `container.thirdPartyResources.get`
  * `container.thirdPartyResources.list`
  * `container.thirdPartyResources.update`
  * `container.tokenReviews.create`
  * `container.updateInfos.create`
  * `container.updateInfos.delete`
  * `container.updateInfos.get`
  * `container.updateInfos.list`
  * `container.updateInfos.update`
  * `container.validatingWebhookConfigurations.create`
  * `container.validatingWebhookConfigurations.delete`
  * `container.validatingWebhookConfigurations.get`
  * `container.validatingWebhookConfigurations.list`
  * `container.validatingWebhookConfigurations.update`
  * `container.volumeAttachments.create`
  * `container.volumeAttachments.delete`
  * `container.volumeAttachments.get`
  * `container.volumeAttachments.getStatus`
  * `container.volumeAttachments.list`
  * `container.volumeAttachments.update`
  * `container.volumeAttachments.updateStatus`
  * `container.volumeSnapshotClasses.create`
  * `container.volumeSnapshotClasses.delete`
  * `container.volumeSnapshotClasses.get`
  * `container.volumeSnapshotClasses.list`
  * `container.volumeSnapshotClasses.update`
  * `container.volumeSnapshotContents.create`
  * `container.volumeSnapshotContents.delete`
  * `container.volumeSnapshotContents.get`
  * `container.volumeSnapshotContents.getStatus`
  * `container.volumeSnapshotContents.list`
  * `container.volumeSnapshotContents.update`
  * `container.volumeSnapshotContents.updateStatus`
  * `container.volumeSnapshots.create`
  * `container.volumeSnapshots.delete`
  * `container.volumeSnapshots.get`
  * `container.volumeSnapshots.getStatus`
  * `container.volumeSnapshots.list`
  * `container.volumeSnapshots.update`
  * `container.volumeSnapshots.updateStatus`

`databasesconsole.locations.*`

  * `databasesconsole.locations.get`
  * `databasesconsole.locations.list`

`databasesconsole.studioQueries.*`

  * `databasesconsole.studioQueries.create`
  * `databasesconsole.studioQueries.delete`
  * `databasesconsole.studioQueries.get`
  * `databasesconsole.studioQueries.list`
  * `databasesconsole.studioQueries.search`
  * `databasesconsole.studioQueries.update`

`deploymentmanager.compositeTypes.*`

  * `deploymentmanager.compositeTypes.create`
  * `deploymentmanager.compositeTypes.delete`
  * `deploymentmanager.compositeTypes.get`
  * `deploymentmanager.compositeTypes.list`
  * `deploymentmanager.compositeTypes.update`

`deploymentmanager.deployments.cancelPreview` `deploymentmanager.deployments.create` `deploymentmanager.deployments.delete` `deploymentmanager.deployments.get` `deploymentmanager.deployments.list` `deploymentmanager.deployments.stop` `deploymentmanager.deployments.update` `deploymentmanager.manifests.*`

  * `deploymentmanager.manifests.get`
  * `deploymentmanager.manifests.list`

`deploymentmanager.operations.*`

  * `deploymentmanager.operations.get`
  * `deploymentmanager.operations.list`

`deploymentmanager.resources.*`

  * `deploymentmanager.resources.get`
  * `deploymentmanager.resources.list`

`deploymentmanager.typeProviders.*`

  * `deploymentmanager.typeProviders.create`
  * `deploymentmanager.typeProviders.delete`
  * `deploymentmanager.typeProviders.get`
  * `deploymentmanager.typeProviders.getType`
  * `deploymentmanager.typeProviders.list`
  * `deploymentmanager.typeProviders.listTypes`
  * `deploymentmanager.typeProviders.update`

`deploymentmanager.types.*`

  * `deploymentmanager.types.create`
  * `deploymentmanager.types.delete`
  * `deploymentmanager.types.get`
  * `deploymentmanager.types.list`
  * `deploymentmanager.types.update`

`dns.managedZones.get` `dns.managedZones.list` `dns.networks.targetWithPeeringZone` `firebase.projects.get` `iam.serviceAccounts.actAs` `iam.serviceAccounts.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `iam.serviceAccounts.list` `logging.buckets.create` `logging.buckets.createTagBinding` `logging.buckets.delete` `logging.buckets.deleteTagBinding` `logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.buckets.undelete` `logging.buckets.update` `logging.exclusions.*`

  * `logging.exclusions.create`
  * `logging.exclusions.delete`
  * `logging.exclusions.get`
  * `logging.exclusions.list`
  * `logging.exclusions.update`

`logging.links.*`

  * `logging.links.create`
  * `logging.links.delete`
  * `logging.links.get`
  * `logging.links.list`

`logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logEntries.create` `logging.logEntries.route` `logging.logMetrics.*`

  * `logging.logMetrics.create`
  * `logging.logMetrics.delete`
  * `logging.logMetrics.get`
  * `logging.logMetrics.list`
  * `logging.logMetrics.update`

`logging.logScopes.*`

  * `logging.logScopes.create`
  * `logging.logScopes.delete`
  * `logging.logScopes.get`
  * `logging.logScopes.list`
  * `logging.logScopes.update`

`logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.notificationRules.*`

  * `logging.notificationRules.create`
  * `logging.notificationRules.delete`
  * `logging.notificationRules.get`
  * `logging.notificationRules.list`
  * `logging.notificationRules.update`

`logging.operations.*`

  * `logging.operations.cancel`
  * `logging.operations.get`
  * `logging.operations.list`

`logging.settings.*`

  * `logging.settings.get`
  * `logging.settings.update`

`logging.sinks.*`

  * `logging.sinks.create`
  * `logging.sinks.delete`
  * `logging.sinks.get`
  * `logging.sinks.list`
  * `logging.sinks.update`

`logging.sqlAlerts.*`

  * `logging.sqlAlerts.create`
  * `logging.sqlAlerts.update`

`logging.views.create` `logging.views.delete` `logging.views.get` `logging.views.getIamPolicy` `logging.views.list` `logging.views.update` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `networkconnectivity.internalRanges.*`

  * `networkconnectivity.internalRanges.create`
  * `networkconnectivity.internalRanges.delete`
  * `networkconnectivity.internalRanges.get`
  * `networkconnectivity.internalRanges.getIamPolicy`
  * `networkconnectivity.internalRanges.list`
  * `networkconnectivity.internalRanges.setIamPolicy`
  * `networkconnectivity.internalRanges.update`

`networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.operations.*`

  * `networkconnectivity.operations.cancel`
  * `networkconnectivity.operations.delete`
  * `networkconnectivity.operations.get`
  * `networkconnectivity.operations.list`

`networkconnectivity.policyBasedRoutes.*`

  * `networkconnectivity.policyBasedRoutes.create`
  * `networkconnectivity.policyBasedRoutes.delete`
  * `networkconnectivity.policyBasedRoutes.get`
  * `networkconnectivity.policyBasedRoutes.getIamPolicy`
  * `networkconnectivity.policyBasedRoutes.list`
  * `networkconnectivity.policyBasedRoutes.setIamPolicy`

`networkconnectivity.regionalEndpoints.*`

  * `networkconnectivity.regionalEndpoints.create`
  * `networkconnectivity.regionalEndpoints.delete`
  * `networkconnectivity.regionalEndpoints.get`
  * `networkconnectivity.regionalEndpoints.list`

`networkconnectivity.serviceClasses.*`

  * `networkconnectivity.serviceClasses.create`
  * `networkconnectivity.serviceClasses.delete`
  * `networkconnectivity.serviceClasses.get`
  * `networkconnectivity.serviceClasses.list`
  * `networkconnectivity.serviceClasses.update`
  * `networkconnectivity.serviceClasses.use`

`networkconnectivity.serviceConnectionMaps.*`

  * `networkconnectivity.serviceConnectionMaps.create`
  * `networkconnectivity.serviceConnectionMaps.delete`
  * `networkconnectivity.serviceConnectionMaps.get`
  * `networkconnectivity.serviceConnectionMaps.list`
  * `networkconnectivity.serviceConnectionMaps.update`

`networkconnectivity.serviceConnectionPolicies.*`

  * `networkconnectivity.serviceConnectionPolicies.create`
  * `networkconnectivity.serviceConnectionPolicies.delete`
  * `networkconnectivity.serviceConnectionPolicies.get`
  * `networkconnectivity.serviceConnectionPolicies.list`
  * `networkconnectivity.serviceConnectionPolicies.update`

`networkmanagement.connectivitytests.get` `networkmanagement.connectivitytests.list` `networksecurity.addressGroups.*`

  * `networksecurity.addressGroups.create`
  * `networksecurity.addressGroups.delete`
  * `networksecurity.addressGroups.get`
  * `networksecurity.addressGroups.getIamPolicy`
  * `networksecurity.addressGroups.list`
  * `networksecurity.addressGroups.setIamPolicy`
  * `networksecurity.addressGroups.update`
  * `networksecurity.addressGroups.use`

`networksecurity.authorizationPolicies.*`

  * `networksecurity.authorizationPolicies.create`
  * `networksecurity.authorizationPolicies.createTagBinding`
  * `networksecurity.authorizationPolicies.delete`
  * `networksecurity.authorizationPolicies.deleteTagBinding`
  * `networksecurity.authorizationPolicies.get`
  * `networksecurity.authorizationPolicies.getIamPolicy`
  * `networksecurity.authorizationPolicies.list`
  * `networksecurity.authorizationPolicies.listEffectiveTags`
  * `networksecurity.authorizationPolicies.listTagBindings`
  * `networksecurity.authorizationPolicies.setIamPolicy`
  * `networksecurity.authorizationPolicies.update`
  * `networksecurity.authorizationPolicies.use`

`networksecurity.authzPolicies.*`

  * `networksecurity.authzPolicies.create`
  * `networksecurity.authzPolicies.delete`
  * `networksecurity.authzPolicies.get`
  * `networksecurity.authzPolicies.getIamPolicy`
  * `networksecurity.authzPolicies.list`
  * `networksecurity.authzPolicies.setIamPolicy`
  * `networksecurity.authzPolicies.update`

`networksecurity.backendAuthenticationConfigs.*`

  * `networksecurity.backendAuthenticationConfigs.create`
  * `networksecurity.backendAuthenticationConfigs.delete`
  * `networksecurity.backendAuthenticationConfigs.get`
  * `networksecurity.backendAuthenticationConfigs.list`
  * `networksecurity.backendAuthenticationConfigs.update`
  * `networksecurity.backendAuthenticationConfigs.use`

`networksecurity.clientTlsPolicies.*`

  * `networksecurity.clientTlsPolicies.create`
  * `networksecurity.clientTlsPolicies.createTagBinding`
  * `networksecurity.clientTlsPolicies.delete`
  * `networksecurity.clientTlsPolicies.deleteTagBinding`
  * `networksecurity.clientTlsPolicies.get`
  * `networksecurity.clientTlsPolicies.getIamPolicy`
  * `networksecurity.clientTlsPolicies.list`
  * `networksecurity.clientTlsPolicies.listEffectiveTags`
  * `networksecurity.clientTlsPolicies.listTagBindings`
  * `networksecurity.clientTlsPolicies.setIamPolicy`
  * `networksecurity.clientTlsPolicies.update`
  * `networksecurity.clientTlsPolicies.use`

`networksecurity.firewallEndpointAssociations.*`

  * `networksecurity.firewallEndpointAssociations.create`
  * `networksecurity.firewallEndpointAssociations.delete`
  * `networksecurity.firewallEndpointAssociations.get`
  * `networksecurity.firewallEndpointAssociations.list`
  * `networksecurity.firewallEndpointAssociations.update`

`networksecurity.firewallEndpoints.*`

  * `networksecurity.firewallEndpoints.create`
  * `networksecurity.firewallEndpoints.createVerdictChangeRequest`
  * `networksecurity.firewallEndpoints.delete`
  * `networksecurity.firewallEndpoints.get`
  * `networksecurity.firewallEndpoints.getVerdictChangeRequest`
  * `networksecurity.firewallEndpoints.getWildfireReport`
  * `networksecurity.firewallEndpoints.getWildfireSample`
  * `networksecurity.firewallEndpoints.list`
  * `networksecurity.firewallEndpoints.listVerdictChangeRequests`
  * `networksecurity.firewallEndpoints.submitVerdictChangeRequest`
  * `networksecurity.firewallEndpoints.update`
  * `networksecurity.firewallEndpoints.use`
  * `networksecurity.firewallEndpoints.useWildfire`

`networksecurity.gatewaySecurityPolicies.*`

  * `networksecurity.gatewaySecurityPolicies.create`
  * `networksecurity.gatewaySecurityPolicies.delete`
  * `networksecurity.gatewaySecurityPolicies.get`
  * `networksecurity.gatewaySecurityPolicies.list`
  * `networksecurity.gatewaySecurityPolicies.update`
  * `networksecurity.gatewaySecurityPolicies.use`

`networksecurity.gatewaySecurityPolicyRules.*`

  * `networksecurity.gatewaySecurityPolicyRules.create`
  * `networksecurity.gatewaySecurityPolicyRules.delete`
  * `networksecurity.gatewaySecurityPolicyRules.get`
  * `networksecurity.gatewaySecurityPolicyRules.list`
  * `networksecurity.gatewaySecurityPolicyRules.update`
  * `networksecurity.gatewaySecurityPolicyRules.use`

`networksecurity.locations.*`

  * `networksecurity.locations.get`
  * `networksecurity.locations.list`

`networksecurity.operations.*`

  * `networksecurity.operations.cancel`
  * `networksecurity.operations.delete`
  * `networksecurity.operations.get`
  * `networksecurity.operations.list`

`networksecurity.sacAttachments.*`

  * `networksecurity.sacAttachments.create`
  * `networksecurity.sacAttachments.delete`
  * `networksecurity.sacAttachments.get`
  * `networksecurity.sacAttachments.list`

`networksecurity.sacRealms.*`

  * `networksecurity.sacRealms.create`
  * `networksecurity.sacRealms.delete`
  * `networksecurity.sacRealms.get`
  * `networksecurity.sacRealms.list`

`networksecurity.securityProfileGroups.*`

  * `networksecurity.securityProfileGroups.create`
  * `networksecurity.securityProfileGroups.delete`
  * `networksecurity.securityProfileGroups.get`
  * `networksecurity.securityProfileGroups.list`
  * `networksecurity.securityProfileGroups.update`
  * `networksecurity.securityProfileGroups.use`

`networksecurity.securityProfiles.*`

  * `networksecurity.securityProfiles.create`
  * `networksecurity.securityProfiles.delete`
  * `networksecurity.securityProfiles.get`
  * `networksecurity.securityProfiles.list`
  * `networksecurity.securityProfiles.update`
  * `networksecurity.securityProfiles.use`

`networksecurity.serverTlsPolicies.*`

  * `networksecurity.serverTlsPolicies.create`
  * `networksecurity.serverTlsPolicies.createTagBinding`
  * `networksecurity.serverTlsPolicies.delete`
  * `networksecurity.serverTlsPolicies.deleteTagBinding`
  * `networksecurity.serverTlsPolicies.get`
  * `networksecurity.serverTlsPolicies.getIamPolicy`
  * `networksecurity.serverTlsPolicies.list`
  * `networksecurity.serverTlsPolicies.listEffectiveTags`
  * `networksecurity.serverTlsPolicies.listTagBindings`
  * `networksecurity.serverTlsPolicies.setIamPolicy`
  * `networksecurity.serverTlsPolicies.update`
  * `networksecurity.serverTlsPolicies.use`

`networksecurity.tlsInspectionPolicies.*`

  * `networksecurity.tlsInspectionPolicies.create`
  * `networksecurity.tlsInspectionPolicies.delete`
  * `networksecurity.tlsInspectionPolicies.get`
  * `networksecurity.tlsInspectionPolicies.list`
  * `networksecurity.tlsInspectionPolicies.update`
  * `networksecurity.tlsInspectionPolicies.use`

`networksecurity.urlLists.*`

  * `networksecurity.urlLists.create`
  * `networksecurity.urlLists.delete`
  * `networksecurity.urlLists.get`
  * `networksecurity.urlLists.list`
  * `networksecurity.urlLists.update`
  * `networksecurity.urlLists.use`

`networkservices.*`

  * `networkservices.agentGateways.create`
  * `networkservices.agentGateways.delete`
  * `networkservices.agentGateways.get`
  * `networkservices.agentGateways.list`
  * `networkservices.agentGateways.update`
  * `networkservices.agentGateways.use`
  * `networkservices.authzExtensions.create`
  * `networkservices.authzExtensions.delete`
  * `networkservices.authzExtensions.get`
  * `networkservices.authzExtensions.list`
  * `networkservices.authzExtensions.update`
  * `networkservices.authzExtensions.use`
  * `networkservices.endpointConfigSelectors.createTagBinding`
  * `networkservices.endpointConfigSelectors.deleteTagBinding`
  * `networkservices.endpointConfigSelectors.listEffectiveTags`
  * `networkservices.endpointConfigSelectors.listTagBindings`
  * `networkservices.endpointPolicies.create`
  * `networkservices.endpointPolicies.delete`
  * `networkservices.endpointPolicies.get`
  * `networkservices.endpointPolicies.list`
  * `networkservices.endpointPolicies.update`
  * `networkservices.gateways.create`
  * `networkservices.gateways.createTagBinding`
  * `networkservices.gateways.delete`
  * `networkservices.gateways.deleteTagBinding`
  * `networkservices.gateways.get`
  * `networkservices.gateways.list`
  * `networkservices.gateways.listEffectiveTags`
  * `networkservices.gateways.listTagBindings`
  * `networkservices.gateways.update`
  * `networkservices.gateways.use`
  * `networkservices.googleTagGatewayPolicies.create`
  * `networkservices.googleTagGatewayPolicies.delete`
  * `networkservices.googleTagGatewayPolicies.get`
  * `networkservices.googleTagGatewayPolicies.list`
  * `networkservices.googleTagGatewayPolicies.update`
  * `networkservices.grpcRoutes.create`
  * `networkservices.grpcRoutes.delete`
  * `networkservices.grpcRoutes.get`
  * `networkservices.grpcRoutes.list`
  * `networkservices.grpcRoutes.update`
  * `networkservices.httpFilters.create`
  * `networkservices.httpFilters.createTagBinding`
  * `networkservices.httpFilters.delete`
  * `networkservices.httpFilters.deleteTagBinding`
  * `networkservices.httpFilters.get`
  * `networkservices.httpFilters.list`
  * `networkservices.httpFilters.listEffectiveTags`
  * `networkservices.httpFilters.listTagBindings`
  * `networkservices.httpFilters.update`
  * `networkservices.httpRoutes.create`
  * `networkservices.httpRoutes.delete`
  * `networkservices.httpRoutes.get`
  * `networkservices.httpRoutes.list`
  * `networkservices.httpRoutes.update`
  * `networkservices.httpfilters.create`
  * `networkservices.httpfilters.delete`
  * `networkservices.httpfilters.get`
  * `networkservices.httpfilters.getIamPolicy`
  * `networkservices.httpfilters.list`
  * `networkservices.httpfilters.setIamPolicy`
  * `networkservices.httpfilters.update`
  * `networkservices.httpfilters.use`
  * `networkservices.lbEdgeExtensions.create`
  * `networkservices.lbEdgeExtensions.delete`
  * `networkservices.lbEdgeExtensions.get`
  * `networkservices.lbEdgeExtensions.list`
  * `networkservices.lbEdgeExtensions.update`
  * `networkservices.lbRouteExtensions.create`
  * `networkservices.lbRouteExtensions.delete`
  * `networkservices.lbRouteExtensions.get`
  * `networkservices.lbRouteExtensions.list`
  * `networkservices.lbRouteExtensions.update`
  * `networkservices.lbTcpExtensions.createForNetwork`
  * `networkservices.lbTcpExtensions.deleteForNetwork`
  * `networkservices.lbTcpExtensions.getForNetwork`
  * `networkservices.lbTcpExtensions.listForNetwork`
  * `networkservices.lbTcpExtensions.updateForNetwork`
  * `networkservices.lbTrafficExtensions.create`
  * `networkservices.lbTrafficExtensions.delete`
  * `networkservices.lbTrafficExtensions.get`
  * `networkservices.lbTrafficExtensions.list`
  * `networkservices.lbTrafficExtensions.update`
  * `networkservices.locations.get`
  * `networkservices.locations.list`
  * `networkservices.meshes.create`
  * `networkservices.meshes.createTagBinding`
  * `networkservices.meshes.delete`
  * `networkservices.meshes.deleteTagBinding`
  * `networkservices.meshes.get`
  * `networkservices.meshes.list`
  * `networkservices.meshes.listEffectiveTags`
  * `networkservices.meshes.listTagBindings`
  * `networkservices.meshes.update`
  * `networkservices.meshes.use`
  * `networkservices.operations.cancel`
  * `networkservices.operations.delete`
  * `networkservices.operations.get`
  * `networkservices.operations.list`
  * `networkservices.route_views.get`
  * `networkservices.route_views.list`
  * `networkservices.serviceBindings.create`
  * `networkservices.serviceBindings.delete`
  * `networkservices.serviceBindings.get`
  * `networkservices.serviceBindings.list`
  * `networkservices.serviceBindings.update`
  * `networkservices.serviceLbPolicies.create`
  * `networkservices.serviceLbPolicies.delete`
  * `networkservices.serviceLbPolicies.get`
  * `networkservices.serviceLbPolicies.list`
  * `networkservices.serviceLbPolicies.update`
  * `networkservices.swpSecurityExtensions.create`
  * `networkservices.swpSecurityExtensions.delete`
  * `networkservices.swpSecurityExtensions.get`
  * `networkservices.swpSecurityExtensions.list`
  * `networkservices.swpSecurityExtensions.update`
  * `networkservices.tcpRoutes.create`
  * `networkservices.tcpRoutes.delete`
  * `networkservices.tcpRoutes.get`
  * `networkservices.tcpRoutes.list`
  * `networkservices.tcpRoutes.update`
  * `networkservices.tlsRoutes.create`
  * `networkservices.tlsRoutes.delete`
  * `networkservices.tlsRoutes.get`
  * `networkservices.tlsRoutes.list`
  * `networkservices.tlsRoutes.update`
  * `networkservices.wasmPlugins.create`
  * `networkservices.wasmPlugins.delete`
  * `networkservices.wasmPlugins.get`
  * `networkservices.wasmPlugins.list`
  * `networkservices.wasmPlugins.update`
  * `networkservices.wasmPlugins.use`

`observability.scopes.get` `opsconfigmonitoring.resourceMetadata.list` `orgpolicy.policy.get` `pubsub.messageTransforms.validate` `pubsub.schemas.*`

  * `pubsub.schemas.attach`
  * `pubsub.schemas.commit`
  * `pubsub.schemas.create`
  * `pubsub.schemas.delete`
  * `pubsub.schemas.get`
  * `pubsub.schemas.getIamPolicy`
  * `pubsub.schemas.list`
  * `pubsub.schemas.listRevisions`
  * `pubsub.schemas.rollback`
  * `pubsub.schemas.setIamPolicy`
  * `pubsub.schemas.validate`

`pubsub.snapshots.create` `pubsub.snapshots.delete` `pubsub.snapshots.get` `pubsub.snapshots.getIamPolicy` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.snapshots.seek` `pubsub.snapshots.setIamPolicy` `pubsub.snapshots.update` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.subscriptions.getIamPolicy` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.subscriptions.setIamPolicy` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.delete` `pubsub.topics.detachSubscription` `pubsub.topics.get` `pubsub.topics.getIamPolicy` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `pubsub.topics.publish` `pubsub.topics.setIamPolicy` `pubsub.topics.update` `pubsub.topics.updateTag` `recommender.appengineVersionCostInsights.*`

  * `recommender.appengineVersionCostInsights.get`
  * `recommender.appengineVersionCostInsights.list`
  * `recommender.appengineVersionCostInsights.update`

`recommender.appengineVersionCostRecommendations.*`

  * `recommender.appengineVersionCostRecommendations.get`
  * `recommender.appengineVersionCostRecommendations.list`
  * `recommender.appengineVersionCostRecommendations.update`

`recommender.cloudsqlIdleInstanceRecommendations.*`

  * `recommender.cloudsqlIdleInstanceRecommendations.get`
  * `recommender.cloudsqlIdleInstanceRecommendations.list`
  * `recommender.cloudsqlIdleInstanceRecommendations.update`

`recommender.cloudsqlInstanceActivityInsights.*`

  * `recommender.cloudsqlInstanceActivityInsights.get`
  * `recommender.cloudsqlInstanceActivityInsights.list`
  * `recommender.cloudsqlInstanceActivityInsights.update`

`recommender.cloudsqlInstanceCpuUsageInsights.*`

  * `recommender.cloudsqlInstanceCpuUsageInsights.get`
  * `recommender.cloudsqlInstanceCpuUsageInsights.list`
  * `recommender.cloudsqlInstanceCpuUsageInsights.update`

`recommender.cloudsqlInstanceDiskUsageTrendInsights.*`

  * `recommender.cloudsqlInstanceDiskUsageTrendInsights.get`
  * `recommender.cloudsqlInstanceDiskUsageTrendInsights.list`
  * `recommender.cloudsqlInstanceDiskUsageTrendInsights.update`

`recommender.cloudsqlInstanceMemoryUsageInsights.*`

  * `recommender.cloudsqlInstanceMemoryUsageInsights.get`
  * `recommender.cloudsqlInstanceMemoryUsageInsights.list`
  * `recommender.cloudsqlInstanceMemoryUsageInsights.update`

`recommender.cloudsqlInstanceOomProbabilityInsights.*`

  * `recommender.cloudsqlInstanceOomProbabilityInsights.get`
  * `recommender.cloudsqlInstanceOomProbabilityInsights.list`
  * `recommender.cloudsqlInstanceOomProbabilityInsights.update`

`recommender.cloudsqlInstanceOutOfDiskRecommendations.*`

  * `recommender.cloudsqlInstanceOutOfDiskRecommendations.get`
  * `recommender.cloudsqlInstanceOutOfDiskRecommendations.list`
  * `recommender.cloudsqlInstanceOutOfDiskRecommendations.update`

`recommender.cloudsqlInstancePerformanceInsights.*`

  * `recommender.cloudsqlInstancePerformanceInsights.get`
  * `recommender.cloudsqlInstancePerformanceInsights.list`
  * `recommender.cloudsqlInstancePerformanceInsights.update`

`recommender.cloudsqlInstancePerformanceRecommendations.*`

  * `recommender.cloudsqlInstancePerformanceRecommendations.get`
  * `recommender.cloudsqlInstancePerformanceRecommendations.list`
  * `recommender.cloudsqlInstancePerformanceRecommendations.update`

`recommender.cloudsqlInstanceReliabilityInsights.*`

  * `recommender.cloudsqlInstanceReliabilityInsights.get`
  * `recommender.cloudsqlInstanceReliabilityInsights.list`
  * `recommender.cloudsqlInstanceReliabilityInsights.update`

`recommender.cloudsqlInstanceReliabilityRecommendations.*`

  * `recommender.cloudsqlInstanceReliabilityRecommendations.get`
  * `recommender.cloudsqlInstanceReliabilityRecommendations.list`
  * `recommender.cloudsqlInstanceReliabilityRecommendations.update`

`recommender.cloudsqlInstanceSecurityInsights.*`

  * `recommender.cloudsqlInstanceSecurityInsights.get`
  * `recommender.cloudsqlInstanceSecurityInsights.list`
  * `recommender.cloudsqlInstanceSecurityInsights.update`

`recommender.cloudsqlInstanceSecurityRecommendations.*`

  * `recommender.cloudsqlInstanceSecurityRecommendations.get`
  * `recommender.cloudsqlInstanceSecurityRecommendations.list`
  * `recommender.cloudsqlInstanceSecurityRecommendations.update`

`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.*`

  * `recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.get`
  * `recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.list`
  * `recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.update`

`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.*`

  * `recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.get`
  * `recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.list`
  * `recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.update`

`recommender.cloudsqlOverprovisionedInstanceRecommendations.*`

  * `recommender.cloudsqlOverprovisionedInstanceRecommendations.get`
  * `recommender.cloudsqlOverprovisionedInstanceRecommendations.list`
  * `recommender.cloudsqlOverprovisionedInstanceRecommendations.update`

`recommender.cloudsqlUnderProvisionedInstanceRecommendations.*`

  * `recommender.cloudsqlUnderProvisionedInstanceRecommendations.get`
  * `recommender.cloudsqlUnderProvisionedInstanceRecommendations.list`
  * `recommender.cloudsqlUnderProvisionedInstanceRecommendations.update`

`recommender.containerDiagnosisInsights.*`

  * `recommender.containerDiagnosisInsights.get`
  * `recommender.containerDiagnosisInsights.list`
  * `recommender.containerDiagnosisInsights.update`

`recommender.containerDiagnosisRecommendations.*`

  * `recommender.containerDiagnosisRecommendations.get`
  * `recommender.containerDiagnosisRecommendations.list`
  * `recommender.containerDiagnosisRecommendations.update`

`recommender.iamPolicyInsights.*`

  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyInsights.update`

`recommender.iamPolicyRecommendations.*`

  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.networkAnalyzerGkeConnectivityInsights.*`

  * `recommender.networkAnalyzerGkeConnectivityInsights.get`
  * `recommender.networkAnalyzerGkeConnectivityInsights.list`
  * `recommender.networkAnalyzerGkeConnectivityInsights.update`

`recommender.networkAnalyzerGkeIpAddressInsights.*`

  * `recommender.networkAnalyzerGkeIpAddressInsights.get`
  * `recommender.networkAnalyzerGkeIpAddressInsights.list`
  * `recommender.networkAnalyzerGkeIpAddressInsights.update`

`recommender.storageBucketSoftDeleteInsights.*`

  * `recommender.storageBucketSoftDeleteInsights.get`
  * `recommender.storageBucketSoftDeleteInsights.list`
  * `recommender.storageBucketSoftDeleteInsights.update`

`recommender.storageBucketSoftDeleteRecommendations.*`

  * `recommender.storageBucketSoftDeleteRecommendations.get`
  * `recommender.storageBucketSoftDeleteRecommendations.list`
  * `recommender.storageBucketSoftDeleteRecommendations.update`

`resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `servicedirectory.namespaces.create` `servicedirectory.namespaces.delete` `servicedirectory.services.create` `servicedirectory.services.delete` `servicenetworking.operations.get` `servicenetworking.services.addPeering` `servicenetworking.services.createPeeredDnsDomain` `servicenetworking.services.deleteConnection` `servicenetworking.services.deletePeeredDnsDomain` `servicenetworking.services.disableVpcServiceControls` `servicenetworking.services.enableVpcServiceControls` `servicenetworking.services.get` `servicenetworking.services.getVpcServiceControls` `servicenetworking.services.listPeeredDnsDomains` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

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

`trafficdirector.*`

  * `trafficdirector.networks.getConfigs`
  * `trafficdirector.networks.reportMetrics`

  
  
### Basic roles

**Note:** Basic roles of **Owner** , **Editor** , and **Viewer** include permissions for other Google Cloud services. If you grant one of these roles to a principal, then you also provide extra permissions for other Google Cloud services.

Basic roles work with Managed Airflow in the following way:

  * **Owner** (`owner`): allows full control of Managed Airflow resources.
  * **Editor** (`editor`): allows full control of Managed Airflow resources.
  * **Viewer** (`viewer`): allows a user to list and get Managed Airflow resources.



See [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/roles-overview#basic) for more information about basic roles and Managed Airflow permissions included in them.

## Permissions for API methods

The following table lists permissions that the caller must have to call each API method in the Managed Service for Apache Airflow API or to perform tasks using Google Cloud tools that use the API (such as Google Cloud console or Google Cloud CLI).

You can create your own custom roles that include individual permissions. For more information, see [Creating a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).

Method | Permission  
---|---  
`environments.create` | `composer.environments.create`, and `iam.serviceAccounts.actAs` on the environment's service account.  
`environments.delete` | `composer.environments.delete`  
`environments.get` | `composer.environments.get`  
`environments.list` | `composer.environments.list`  
`environments.update` | `composer.environments.update`  
`environments.executeAirflowCommand` | `composer.environments.executeairflowcommand`  
`environments.stopAirflowCommand` | `composer.environments.executeairflowcommand`  
`environments.pollAirflowCommand` | `composer.environments.executeairflowcommand`  
`operations.delete` | `composer.operations.delete`  
`operations.get` | `composer.operations.get`  
`operations.list` | `composer.operations.list`  
  
### Permissions for using gcloud CLI with environments

To use `gcloud` with Managed Airflow environments, you need the following permissions:

  * `composer.environments.get`
  * `container.clusters.get`
  * `container.clusters.list`
  * `container.clusters.getCredentials`



If you want to manage environments or environment buckets with `gcloud composer` commands, you also must have a role that has enough permissions to do so.

If you want to run Airflow CLI commands, you need the following, additional permissions:

  * `container.namespaces.list`
  * `container.pods.get`
  * `container.pods.list`

  * _(Managed Airflow 2.4.0 and later)_ `composer.environments.executeAirflowCommand`

  * _(Managed Airflow versions earlier than 2.4.0)_ `container.pods.exec`




### Permissions for working with DAGs from Google Cloud console

The following permissions cover working with DAGs from Google Cloud console, through the [DAG UI](https://docs.cloud.google.com/composer/docs/composer-2/view-dags):

Permission | Description  
---|---  
`composer.dags.list` | View the list of DAGs on the Environment details page.  
`composer.dags.get` | Get detailed information about DAGs, DAG runs, and tasks on the DAG details page.  
`composer.dags.getSourceCode` | Get source code of DAGs on the DAG details page.  
`composer.dags.execute` | Pause, unpause and trigger DAGs from the DAG details page.  
**Important:** These permissions only affect Google Cloud console.

You can use [Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-2/airflow-rbac) to further control DAG permissions for user accounts. DAG UI requires both IAM and Airflow UI Access Control permissions to allow a specific action on a DAG. At the same time, Airflow UI validates user access only against Airflow UI Access Control permissions, skipping IAM permissions.

For example, if a user has the `composer.dags.execute` permission and the `Viewer` Airflow role, then this user cannot trigger DAGs from Google Cloud console. As an opposite example, if a user does not have the `composer.dags.list` permission, this user can still view the list of DAGs in the [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface).

## Permissions and roles for Shared VPC networking

Shared VPC networking requires additional roles and permissions for service accounts in service and host projects. For more information about configuring these roles and permissions, see [Configuring Shared VPC networking](https://docs.cloud.google.com/composer/docs/composer-2/configure-shared-vpc).

## Using a service account from another project

If you want a Managed Airflow environment in one project to use a user-managed service account from a different project, then configure the user-managed service account in the following way:

  1. Make sure that the org policy of the project where your user-managed service account is located [permits service account impersonation across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

  2. [Enable the Composer API](https://docs.cloud.google.com/composer/docs/composer-2/enable-composer-service) in the project where your user-managed service account is located. For more information about why it's needed, see [Where to create service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview#locations).

  3. Assign IAM roles as described in the following table.

  4. [Create your environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments) with a cross-project service account. You can use Google Cloud CLI, API or Terraform. In Google Cloud console, it is not possible to select a service account from a different project.


**Note:** `SERVICE_PROJECT_NUMBER` is the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of a project where you create your Managed Airflow environment.

The following table describes the required IAM roles and principals for your user-managed service account.

Project | Resource | Principal | Role  
---|---|---|---  
Project where your user-managed service account is located  |  Your user-managed service account  |  Cloud Composer Service Agent account of the project where your environment is located (`service-SERVICE_PROJECT_NUMBER@cloudcomposer-accounts.iam.gserviceaccount.com`).  |  **Service Account User** (`iam.serviceAccountUser`)  
_(Managed Airflow (Gen 2) only)_ Project where your user-managed service account is located  |  Your user-managed service account  |  Managed Airflow Service Agent account of the project where your environment is located (`service-SERVICE_PROJECT_NUMBER@cloudcomposer-accounts.iam.gserviceaccount.com`).  |  **Cloud Composer v2 API Service Agent Extension** (`roles/composer.ServiceAgentV2Ext`).   
See Grant roles to Managed Airflow Service Agent account for more information about how this role is used.  
Project where your user-managed service account is located  |  Your user-managed service account  |  Kubernetes Engine Service Agent of the project where your environment is located (`service-SERVICE_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com`)  |  **Service Account User** (`iam.serviceAccountUser`)  
Project where your user-managed service account is located  |  Your user-managed service account  |  Google APIs Service Agent of the project where your environment is located (`SERVICE_PROJECT_NUMBER@cloudservices.gserviceaccount.com`)  |  **Service Account User** (`iam.serviceAccountUser`)  
Project where your user-managed service account is located  |  Your user-managed service account  |  Compute Engine Service Agent of the project where your environment is located (`service-SERVICE_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`)  |  **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`)  
Project where your environment is located  |  Project  |  Your user-managed service account  |  Grant the required roles to your user-managed service account, as described in Grant roles to a user-managed service account. For example, in a Public IP configuration, your user-managed service account requires the **Composer Worker** role.  
  
## Allow access to Airflow UI

The following sections describe how to enable access to Airflow UI in various scenarios.

### Allow access to Airflow UI in Google Workspace

If the **API Controls** > **Unconfigured third-party apps** > **Don't allow users to access any third-party apps** option is enabled in Google Workspace and the Apache Airflow in Managed Airflow app is not explicitly allowed, users are not able to access the Airflow UI unless they explicitly allow the application.

To allow access to the Apache Airflow in Managed Airflow app, do the following:

  1. In Admin console, go to **Menu** (menu) > **Security** > **Access and data control** > **API Controls**.

  2. Click **Manage Third-Party App Access** to view your configured apps.

  3. Click **Configure new app**.

  4. Search for the app's OAuth Client ID: `431403837536-q0odo3nmtfjocv7q291cnmedr0hnlbkh.apps.googleusercontent.com`

  5. Select the Apache Airflow in Managed Airflow app.

  6. Select the scope of users to configure access for and click **Continue**.

  7. In the **Access to Google data** , select **Limited** and click **Continue**.

  8. Review the information and click **Finish**.




For more information about configuring third-party app access, see [Control which third-party and internal apps access Google Workspace data](https://support.google.com/a/answer/7281227).

### Allow access to Airflow UI in Context-Aware Access bindings

If Chrome Enterprise Premium [Context-Aware Access bindings](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-console-and-apis) are used with access levels that rely on [device attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#device-policy) or [location attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#regions), and the Apache Airflow in Managed Airflow app is not exempted, then it's not possible to access the Airflow UI because of a login loop.

To allow access, add an exemption for the Apache Airflow in Managed Airflow app, as described in the following steps. Adding the exemption relaxes the original restriction. However, access from devices and locations that don't match the original access level condition is still expected to be blocked when authenticating to Airflow UI. If the previously allowed access is cached in the web browser, it must expire before the access can be blocked.

For more information about applying different access levels in Context-Aware Access bindings, see [Define configurations for specific applications](https://docs.cloud.google.com/chrome-enterprise-premium/docs/apply-policies-to-user-groups#define_configurations_for_specific_applications).

To allow access to the Apache Airflow in Managed Airflow app:

  1. When assigning access levels to apps, check that the **Exempt allowlisted apps so they can always access APIs for specific Google services, regardless of access levels** option is selected. This option is required to exempt the Airflow API from checks. For more information, see [Assign access levels to an app](https://knowledge.workspace.google.com/admin/security/assign-context-aware-access-levels-to-apps#assign_caa_levels) in the Google Workspace documentation.

  2. In Access Context Manager, create a [custom access level](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level) that is equivalent to the access level currently bound in the Context-Aware Access settings, but with removed conditions that rely on device and location attributes. If the original access level had no conditions besides device or location attributes, create a custom access level with a CEL expression set to `true`.

  3. Create an empty file named `binding.yaml` on your local computer. In later steps, you will use it to update the existing binding that relies on device or location attributes.

  4. Find the existing access binding that uses the access level that relies on device or location attributes.

You can list all bindings with the following command in Google Cloud CLI:
         
         gcloud access-context-manager cloud-bindings list \
           --organization ORGANIZATION_ID
         

Replace the following:

     * `ORGANIZATION_ID`: [Organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) of the organization where access bindings are defined for your users.
  5. Copy the entire `scopedAccessSettings` section from the binding that relies on device or location attributes to the `binding.yaml` file.

**Warning:** If you don't preserve the existing `scopedAccessSettings` section in this step, then **your existing binding's configuration can be lost** when you overwrite it in later steps with the updated configuration.

If the binding doesn't have this section, paste an empty section to this file:
         
         scopedAccessSettings:
         

  6. Append the following list item to the `binding.yaml` file. It exempts the Apache Airflow in Managed Airflow OAuth client from device and location attributes checks:
         
         - scope:
             clientScope:
               restrictedClientApplication:
                 clientId: 431403837536-q0odo3nmtfjocv7q291cnmedr0hnlbkh.apps.googleusercontent.com
           activeSettings:
             accessLevels:
             - ACCESS_LEVEL_WITHOUT_DEVICE_AND_LOCATION_ATTRIBUTES
         

Replace the following:

     * `ACCESS_LEVEL_WITHOUT_DEVICE_AND_LOCATION_ATTRIBUTES`: the fully qualified name of the custom access level that you created earlier, in the format: `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
  7. Update the binding that relies on device or location attributes using the `binding.yaml` file.
         
         gcloud access-context-manager cloud-bindings update \
           --binding=BINDING_ID \
           --binding-file='binding.yaml'
         

Replace the following:

     * `BINDING_ID`: fully qualified identifier of the access binding that uses the access level that relies on device or location attributes. Use the following format: `organizations/ORGANIZATION/gcpUserAccessBindings/BINDING_NAME`.



### Allow access to Airflow UI in VPC Service Controls ingress rules

If [ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) are configured in a VPC Service Controls perimeter that protects the project, and the ingress rule that allows access to the Managed Airflow service uses `ANY_SERVICE_ACCOUNT` or `ANY_USER_ACCOUNT` identity type, then users can't access the Airflow UI, ending up in a login loop.

It isn't possible to use ingress rules with these identity types for the Managed Airflow service and retain access to the Airflow UI. To unblock access to the Airflow UI, you must either change the ingress rule to use the `ANY_IDENTITY` identity type or a list of specific identities and groups. As an alternative, you can configure an [access level](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) that allows additional access to the perimeter.

For a full list of features that aren't supported for ingress rules, see [Unsupported features](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#unsupported-features).

## What's next

  * [Creating environments](https://docs.cloud.google.com/composer/docs/composer-2/create-environments)
  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-environment-creation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
