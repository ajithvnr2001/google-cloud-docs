---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/setup-teams/
title: Set up teams for your fleet \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:31.152491+00:00
---

# Set up teams for your fleet  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/setup-teams/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Set up teams for your fleet Stay organized with collections  Save and categorize content based on your preferences. 

This page is for platform admins who want to set up and manage fleet usage for a team.

Before reading this page, ensure that you're familiar with [Fleet team management](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management).

## Team setup overview

You can set up teams using the Google Cloud CLI, the Google Cloud console or Terraform.

The general procedure for setting up a team is as follows:

  1. Select or create the fleet where you want to set up team access, and ensure that you have the correct permissions and APIs to complete setup.
  2. (Optional but recommended) Set up access control for Google Groups on your fleet clusters.
  3. Decide which users make up the team. A team can include Google Groups (recommended) and/or individual accounts.
  4. Choose the level of access to the fleet and team resources that you want for each team member.
  5. Create a team scope for the team.
  6. Add one or more (or all) fleet member clusters to the team scope.
  7. Define fleet-level namespaces and associate them with the team scope.
  8. (Optional) Use Config Sync to sync Kubernetes resources to team scopes and namespaces.



The team can then get credentials to access their clusters using the Connect Gateway.

## Set up the Google Cloud CLI

Even if you create team scopes using the Google Cloud console, you may still need to set up the gcloud CLI to complete some prerequisites while setting up your fleet, such as enabling required APIs.

  1. Ensure that you have [the latest version of the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), including the Google Cloud CLI [alpha component](https://docs.cloud.google.com/sdk/docs/components). You need at least version 419.0.0 to use fleet team management commands.

  2. Run the following command to log in to Google Cloud:
         
         gcloud auth login
         

  3. Either [initialize](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with your chosen fleet's host project, or run the following command to set the fleet host project as the default:
         
         gcloud config set project PROJECT_ID
         

You can use the `--project` flag with any of the following commands to specify a different fleet host project, if required.




## Set up your fleet

Select or create the fleet where you want to set up a new team. For guidelines and examples to help you structure your fleets, see [Fleet examples](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/examples) and the other guides in **Plan your fleet**.

If you want to create a new named fleet in a project that doesn't already have one, run the following command (you'll need to set up the Google Cloud CLI first):
    
    
      gcloud container fleet create \
        --display-name=NAME \
        --project=FLEET_HOST_PROJECT_ID
    

If you don't specify a `display-name`, the new fleet is created with a default display name based on the fleet host project name.

### Required IAM roles

If you don't have `roles/owner` in the fleet host project, you need [`roles/gkehub.admin`](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) to create and configure team scopes and namespaces. A project owner can grant this role with the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member user:USER_EMAIL_ADDRESS \
        --role='roles/gkehub.admin'
    

### Enable APIs

Ensure that your fleet host project has all the required APIs enabled, including the GKE API:
    
    
    gcloud services enable --project=PROJECT_ID \
       gkehub.googleapis.com \
       container.googleapis.com \
       connectgateway.googleapis.com \
       cloudresourcemanager.googleapis.com \
       iam.googleapis.com \
       container.googleapis.com
    
    

If you disable the GKE API after configuring fleet team management, some aspects of the feature will continue to work, but you will be unable to update or create team scopes or fleet namespaces.

### Configure clusters for access control with Google Groups

While you can configure a team's access using RBAC to fleet member clusters on a user-by-user basis without any additional cluster configuration, we recommend giving team members access to clusters on the basis of their membership of a team Google Group. Authorizing based on group membership means you don't have to set up separate authorization for each account, making policies simpler to manage and easier to audit, and removing the need to manually add/remove individual users from clusters when they join or leave the team. Use the following guides to ensure that the clusters you want to assign to team scopes can use Google Groups with the Connect Gateway for access control:

  * For **GKE clusters on Google Cloud** , follow the instructions in [Configure Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac).
  * For **fleet member clusters outside Google Cloud** , follow the instructions in [Set up the Connect Gateway with Google Groups](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups).



## Set up a new team

The following instructions show you how to create a new team scope for a team.

### Choose team access permissions

First, decide or discover which users make up your team. An important part of team setup is granting these team members access to the fleet, including the ability to view clusters in the Google Cloud console and view logs across their team scope. Depending on the team member's role, you may also want to delegate the ability to create namespaces within their team scope to them (available in gkehub.ScopeAdmin or gkehub.ScopeEditor), or let them update RBAC role bindings (gkehub.ScopeAdmin only).

To make this setup simpler, fleet team management provides three predefined permission personas to choose from that include a full set of IAM and Kubernetes RBAC permissions that a team scope admin, editor, or viewer might need when working with their scope. Alternatively, you can select a custom role persona with custom RBAC permissions on a cluster. You can then assign these personas to team members when setting up your team, as described in the following section.

The following table shows which permissions of each type are granted to each persona:

Description | Type | Scope Admin persona | Scope Editor persona | Scope Viewer persona | Custom Role persona  
---|---|---|---|---|---  
Access to the team scope and its namespaces. | IAM Binding on team scope | [roles/gkehub.scopeAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) | [roles/gkehub.scopeEditor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditor) | [roles/gkehub.scopeViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewer) | [roles/gkehub.scopeViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewer)  
Access to the fleet host project, including metrics, long-running operations, and Connect gateway. | IAM Binding on fleet host project | [roles/gkehub.scopeEditorProjectLevel](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel) | [roles/gkehub.scopeEditorProjectLevel](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel) | [roles/gkehub.scopeViewerProjectLevel](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewerProjectLevel) | [roles/gkehub.scopeEditorProjectLevel](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel)  
Access to the team scope's log bucket. | IAM Binding on fleet host project (with condition that the resource accessed is the bucket name). | [roles/logging.viewAccessor](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) | [roles/logging.viewAccessor](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) | [roles/logging.viewAccessor](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) | [roles/logging.viewAccessor](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor)  
Access to Kubernetes resources inside the scope's clusters. | RBAC Binding on the scope that is applied to the team scope's namespaces. | [Kubernetes default role: admin](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) | [Kubernetes default role: edit](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) | [Kubernetes default role: view](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) | [User-defined ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#clusterrole-example)  
  
As mentioned in the previous section, we recommend that you grant team members access to their resources on the basis of Google Group membership, although team management also lets you grant access to individual users.

If these personas don't fully meet your needs, you can also individually bind IAM (using [`gcloud container fleet scopes add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/add-iam-policy-binding)) and RBAC (using [`gcloud container fleet scopes rbacrolebindings create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/rbacrolebindings/create)) roles. See the [Google Cloud CLI reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/scopes) for more commands that you can use to manage these bindings.

### Set up a team scope

### gcloud

### Create a team scope

To create a new team scope in a fleet, run the following command, where SCOPE_NAME is the unique identifying name that you have chosen for your new scope:
    
    
    gcloud container fleet scopes create SCOPE_NAME
    

### Add clusters to a team scope

Only existing fleet members can be added to team scopes. These instructions assume that the cluster you want to add to the scope is already a fleet member. If you need to add the cluster to your fleet, follow the instructions for your cluster type in [Create your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation) to register the cluster. Ensure that the newly registered cluster is configured to use Google Groups for access control, as described earlier.

A fleet member cluster can be added to any number of team scopes in its fleet host project.

To add a cluster to a team scope, run the following command:
    
    
    gcloud container fleet memberships bindings create BINDING_NAME \
      --membership MEMBERSHIP_NAME \
      --scope  SCOPE_NAME \
      --location MEMBERSHIP_LOCATION
    

Replace the following:

  * BINDING_NAME: a name that represents the relationship between the cluster and the team scope. We suggest using MEMBERSHIP_NAME-SCOPE_NAME.
  * MEMBERSHIP_NAME: the cluster's [unique identifier within the fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership) (typically the cluster name).
  * (optional) MEMBERSHIP_LOCATION: the cluster's membership location. If you omit this the value is `global`, which is the default for cluster registrations.



### Create fleet namespaces

To create a namespace in a team scope, run the following command:
    
    
    gcloud container fleet scopes namespaces create NAMESPACE_NAME --scope=SCOPE_NAME
    

Replace the following:

  * NAMESPACE_NAME: the unique name you have chosen for the namespace within the fleet. Ensure that NAMESPACE_NAME does not conflict with the fleet namespace naming restrictions.
  * SCOPE_NAME: the team scope where you want to use the namespace.



This command creates a Kubernetes namespace called NAMESPACE_NAME in each cluster in the team scope. Team members can use NAMESPACE_NAME like any other Kubernetes namespace after you have granted them access to their scope. If you already have an existing Kubernetes namespace called NAMESPACE_NAME in the team scope, it is considered part of the new fleet namespace. This is sometimes referred to as _onboarding_ the namespace.

### Grant team members access to the team scope

### Using predefined roles

Next, ensure that the relevant Google Groups have the appropriate IAM and RBAC permissions configured to work with the new scope:
    
    
    gcloud beta container fleet scopes add-app-operator-binding SCOPE_ID
            --role=ROLE --group=TEAM_EMAIL --project PROJECT_ID
    

  * PROJECT_ID is the ID of your fleet host project
  * TEAM_EMAIL is the email address for a team's Google Group.
  * SCOPE_ID is the id of the scope that was created
  * ROLE is the permission persona that the group has in the team scope. Values for this parameter can be `admin` (Scope Admin), `edit` (Scope Editor), or `view` (Scope Viewer).



If you need to grant an individual user access to the scope, run the following command instead, where USER_EMAIL is the user's Google ID email address:
    
    
    gcloud beta container fleet scopes add-app-operator-binding SCOPE_ID
            --role=ROLE --user=USER_EMAIL --project PROJECT_ID
    

### Using custom roles

To use a custom role, you first need to add the custom role to the `rbacrolebindingactuation` fleet feature:
    
    
    gcloud container fleet rbacrolebindingactuation update --allowed-custom-roles CUSTOM_ROLE --project PROJECT_ID
    

Next, ensure that the relevant Google Groups have the appropriate IAM and RBAC permissions configured to work with the new scope:
    
    
    gcloud beta container fleet scopes add-app-operator-binding SCOPE_ID
            --custom-role=CUSTOM_ROLE --group=TEAM_EMAIL --project PROJECT_ID
    

Replace the following:

  * PROJECT_ID: the ID of your fleet host project.
  * TEAM_EMAIL: the email address for a team's Google Group.
  * SCOPE_ID : the ID of the scope that was created.
  * CUSTOM_ROLE: a Kubernetes ClusterRole which has been added to the allowlist in the `rbacrolebindingactuation` feature. For the feature to work as intended, the ClusterRole should exist on each cluster added to the scope. However, resources are still created even when the ClusterRole is not present.

**Note:** You can add a maximum of 20 custom roles to the `rbacrolebindingactuation` allowlist. You can remove custom roles from the allowlist only if they are no longer in use by the scope rbacrolebindings.

If you need to grant an individual user access to the scope, run the following command instead, where USER_EMAIL is the user's Google ID email address:
    
    
    gcloud beta container fleet scopes add-app-operator-binding SCOPE_ID
            --custom-role=CUSTOM_ROLE --user=USER_EMAIL --project PROJECT_ID
    

### Console

### Create a team scope

  1. With your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project) selected, go to the **Teams** section in the Google Cloud console.

[Go to Teams](https://console.cloud.google.com/kubernetes/teams/)

  2. At the top of the page, click **Create Team Scope**.

  3. In the **Team Basics** page, for **Name** , enter a unique name for your team scope. You won't be able to change this name once the team scope is created.

  4. To add team members to the scope, click **Add Team Member**.

     * For **Type** , select **User** to add an individual team member, or **Group** to add a Google Group (recommended).
     * For **User or Group** , type in the email address of the team member or group.
     * For **Role** , select **Scope Admin** , **Scope Editor** or **Scope Viewer** , which configure multiple IAM and RBAC bindings on the scope and fleet, as described in Choose team access permissions.
  5. To create the team scope without adding clusters and namespaces at this stage, click **Create Team Scope**. Otherwise, continue to the following section to add clusters to the scope.




### Add clusters to the team scope

To associate a cluster with a team scope, the cluster must be an existing fleet member. If you need to add the cluster to your fleet, follow the instructions for your cluster type in [Create your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation) to register the cluster. Ensure that the newly registered cluster is configured to use Google Groups for access control, as described earlier.

A fleet member cluster can be added to any number of team scopes in its fleet host project, which lets different teams run workloads on the same cluster.

  1. In the **Team Basics** page, after adding team members to your scope, click **Continue**.
  2. In the **Clusters** page, you can select the fleet clusters to associate with this team scope. In the **Clusters** drop-down, check the clusters you want to add, and click **OK**.



### Create fleet namespaces

Team members can use fleet namespaces like any other Kubernetes namespace. When you create a fleet namespace, a corresponding Kubernetes namespace is created in all clusters in the team scope, if it doesn't exist already.

  1. In the **Clusters** page, after adding clusters to your team scope, click **Continue**.
  2. In the **Namespaces** page, click **Add Namespace**. 
     * For **Name** , enter a unique name for the namespace within the fleet, or the name of an existing namespace if you want to onboard that namespace. Ensure that the name does not conflict with the fleet namespace naming restrictions.
  3. To add more fleet namespaces to the scope, repeat the preceding step.
  4. To create the team scope, click **Create Team Scope**. Once the team scope is created, you can view and edit your team scope if necessary by clicking on its name in the **Teams** section.



### Terraform

This section shows you how to set up a new team using Terraform. For more information and other examples, see the reference documentation for the following resources:

  * [`google_gke_hub_scope`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_scope)
  * [`google_gke_hub_membership_binding`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_membership_binding)
  * [`google_gke_hub_namespace`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_namespace)
  * [`google_gke_hub_scope_rbac_role_binding`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_scope_rbac_role_binding)
  * [`google_gke_hub_feature_rbacrolebindingactuation`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature#example-usage---gkehub-feature-rbacrolebinding-actuation)



### Create a team scope

To create a team scope, you can use the following block in your Terraform configuration.
    
    
      resource "google_gke_hub_scope" "TF_SCOPE_RESOURCE_NAME" {
        scope_id = "SCOPE_NAME"
      }
    

Replace the following:

  * TF_SCOPE_RESOURCE_NAME: the name that you choose to uniquely identify the Terraform `google_gke_hub_scope` resource created by this block.
  * SCOPE_NAME: a unique identifying name for your team scope.



### Add clusters to the scope

Only existing fleet members can be added to team scopes. If you need to add the cluster to your fleet, follow the instructions for your cluster type in [Create your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation) to register the cluster. Ensure that the newly registered cluster is configured to use Google Groups for access control, as described earlier.

To add a cluster to a team scope, use the following block in your configuration:
    
    
      resource "google_gke_hub_membership_binding" "TF_MEMBERSHIP_BINDING_RESOURCE_NAME" {
        membership_binding_id = "BINDING_NAME"
        scope = SCOPE_NAME
        membership_id = MEMBERSHIP_NAME
        location = "MEMBERSHIP_LOCATION"
      }
    

Replace the following:

  * TF_MEMBERSHIP_BINDING_RESOURCE_NAME: a name to identify the `google_gke_hub_membership_binding` resource created by this block.
  * BINDING_NAME: a name that represents the relationship between the cluster and the scope. We suggest using MEMBERSHIP_NAME-SCOPE_NAME.
  * SCOPE_NAME: the name of your team scope.
  * MEMBERSHIP_NAME: the cluster's [unique identifier within the fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership) (typically the cluster name).
  * MEMBERSHIP_LOCATION: the cluster's membership location.



### Create fleet namespaces

Team members can use fleet namespaces like any other Kubernetes namespace. You can create a new namespace, or onboard an existing one. When you create a fleet namespace, a corresponding Kubernetes namespace is created in all clusters in the team scope, if it doesn't exist already.

To create a fleet namespace, use the following block in your configuration:
    
    
      resource "google_gke_hub_namespace" "TF_NAMESPACE_RESOURCE_NAME" {
        scope_namespace_id = "NAMESPACE_NAME"
        scope_id = SCOPE_NAME
        scope = SCOPE_NAME
      }
    

Replace the following:

  * TF_NAMESPACE_RESOURCE_NAME: a name to identify the `google_gke_hub_namespace` resource created by this block.
  * NAMESPACE_NAME: a unique name that you have chosen for the fleet namespace. Ensure that this name does not conflict with the fleet namespace naming restrictions.
  * SCOPE_NAME: the name of the team scope in which the fleet namespace is created.



### Grant scope access

### Using predefined roles

As described in the previous section, team members can be granted access to their scope using permission personas that include both IAM and RBAC permissions. For example, here is a configuration to grant an individual user access to a team scope:
    
    
    module "TF_SCOPE_RESOURCE_NAME_USER_EMAIL" {
      source           = "terraform-google-modules/kubernetes-engine/google//modules/fleet-app-operator-binding"
    
      scope_id = "SCOPE_NAME"
      user = "USER_EMAIL"
      role = "ROLE"
    }
    

Replace the following:

  * TF_SCOPE_RESOURCE_NAME: the name of the scope.
  * BINDING_NAME: a name to represent this binding.
  * SCOPE_NAME: the name of the team scope.
  * USER_EMAIL: the user's email address.
  * ROLE: the persona you want to grant to the user, which can be [`ADMIN`, `EDIT`, or `VIEW`](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine/tree/master/modules/fleet-app-operator-permissions).



To grant a Google Group access to a team scope, use `group` instead of `user` in the preceding configuration, and use the email address for the team's Google Group.

### Using custom roles

To use a custom role, you first need to add the custom role to the `rbacrolebindingactuation` fleet feature:
    
    
    resource "google_gke_hub_feature" "rbacrolebindingactuation" {
      name = "rbacrolebindingactuation"
      location = "global"
      spec {
        rbacrolebindingactuation {
          allowed_custom_roles = ["CUSTOM_ROLE"]
        }
      }
    }
    

The following configuration grants individual user RBAC access to a team scope:
    
    
    resource "google_gke_hub_scope_rbac_role_binding" "BINDING_NAME" {
      scope_id = "SCOPE_NAME"
      user = "USER_EMAIL"
      role {
        custom_role = "CUSTOM_ROLE"
      }
      depends_on = [google_gke_hub_feature.rbacrolebindingactuation]
    }
    

Replace the following:

  * BINDING_NAME: a name to represent this binding.
  * SCOPE_NAME: the name of the team scope.
  * USER_EMAIL: the user's email address.
  * CUSTOM_ROLE: the Kubernetes ClusterRole which has been added to the allowlist in the `rbacrolebindingactuation` feature. For the feature to work as intended, the ClusterRole should exist on each cluster added to the scope. However, resources are still created even when the ClusterRole is not present.

**Note:** You can add a maximum of 20 custom roles to the `rbacrolebindingactuation` allowlist. You can remove custom roles from the allowlist only if they are no longer in use by the scope rbacrolebindings.

Additional project-level and scope-level IAM permissions are required and can be added by following the [operator binding terraform examples](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine/blob/9dce230539a2c2ddee452489d604df34006a625f/modules/fleet-app-operator-permissions/main.tf).

## Access fleet namespaces

Once the setup is complete, team members can access the namespaces in their scope by getting the relevant cluster credentials. To get credentials for a fleet member cluster using the Connect Gateway, run the following command, where MEMBERSHIP_NAME is the cluster's fleet membership name:
    
    
       gcloud container fleet memberships get-credentials  MEMBERSHIP_NAME
    

For more details, see [Using the Connect Gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using).

## Manage team scopes

Use the following commands to manage team scopes.

### gcloud

### List team scopes

To list all scopes in a fleet, run the following command:
    
    
    gcloud container fleet scopes list
    

To list all scopes associated with a cluster, run the following command:
    
    
    gcloud container fleet memberships bindings list --membership MEMBERSHIP_NAME
    

### Remove clusters from team scopes

To remove a cluster from a scope, run the following command:
    
    
    gcloud container fleet memberships bindings delete BINDING_NAME --membership MEMBERSHIP_NAME
    

### Delete a team scope

To delete a scope from your fleet, run the following command:
    
    
    gcloud container fleet scopes delete SCOPE_NAME
    

### Console

### List team scopes

To view all scopes in a fleet, with your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project) selected, go to the **Teams** section in the Google Cloud console.

[Go to Teams](https://console.cloud.google.com/kubernetes/teams/)

The **Teams** page shows you a list of all team scopes created for your fleet. For each scope, you can see a summary of its resource utilization over the specified time period, as well as its estimated monthly cost, the number of errors, and the number of container restarts.

You can view more detailed [cost-related utilization metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics) by clicking **Cost Optimization**.

### View team scope details

For each team scope, you can view details including the labels associated with that scope, team members, and team-scoped logs.

  1. On the **Teams** page, click the team scope whose details you want to view.
  2. In the **Team** tab, you can see the scope labels, if any, and view team members.
  3. Click the **Monitoring** tab to [view resource utilization metrics](https://docs.cloud.google.com/fleet-management/docs/team-management-overview) for the team.
  4. Click the **Clusters** tab to view the team scope's clusters.
  5. Click the **Namespaces** tab to view fleet namespaces in this team scope.
  6. Click the **Logs** tab to [view team scope logs](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-logs).



### Add or delete clusters in a team scope

To add or delete clusters in an existing team scope:

  1. Go to the **Teams** page in the Google Cloud console:

[Go to Teams](https://console.cloud.google.com/kubernetes/teams/)

  2. Select the team scope in which you want to add or delete clusters. The **Clusters** tab shows you a list of the clusters currently bound to the scope.




To add clusters to a team scope:

  1. At the top of the page, click **Add Clusters**.
  2. In the **Clusters** drop-down, select the clusters you want to add to the scope, and click **OK**.
  3. Click **Update Team Scope**.



To delete clusters from a team scope:

  1. Select the **Clusters** tab which shows you a list of the clusters currently bound to the scope.
  2. Click the Trash icon next to the cluster you want to delete, and click **Remove** to confirm the deletion.



### Delete a scope

  1. Go to the **Teams** page in the Google Cloud console:

[Go to Teams](https://console.cloud.google.com/kubernetes/teams/)

  2. Select the team scope you want to delete.

  3. To delete the scope, at the top of the page, click **Delete**.

  4. Confirm the deletion by entering the name of your scope, and click **Delete** again.




## Manage fleet namespaces

### gcloud

Use the following commands to manage namespaces within team scopes.

### List fleet namespaces

To list all the namespaces created using `fleet scopes namespaces create` in a scope, run the following command:
    
    
    gcloud container fleet scopes namespaces list --scope=SCOPE_NAME
    

### Delete a fleet namespace

To delete a fleet namespace, run the following command:
    
    
    gcloud container fleet scopes namespaces delete NAMESPACE_NAME --scope=SCOPE_NAME
    

Note that what happens when you delete a fleet namespace depends on how you added the namespace:

  * If you **created a new fleet namespace:** This command deletes the fleet namespace. It also deletes any Kubernetes namespaces created as a result of creating the fleet namespace, together with their workloads.
  * If you **onboarded an existing Kubernetes namespace:** This command deletes the fleet namespace. The original namespace that you onboarded is _not_ deleted.



### Console

To manage fleet namespaces in your team scope:

  1. Go to the **Teams** page in the Google Cloud console:

[Go to Teams](https://console.cloud.google.com/kubernetes/teams/)

  2. Select the team scope whose fleet namespaces you want to manage.




### List fleet namespaces

In your team scope, select the **Namespaces** tab which shows you a list of the namespaces created in this scope.

### View namespace details

For each fleet namespace, you can view the labels associated with that namespace, and workloads and logs filtered by namespace.

  1. Select the **Namespaces** tab which shows you a list of the fleet namespaces created in the team scope.
  2. Click the fleet namespace whose details you want to view.
  3. In the **Details** tab, you can see the fleet namespace and scope labels. 
     * To view workloads for this namespace, click **View Workloads**.
     * In the **Workloads** page, you can see the workloads already filtered by the namespace and clusters associated with the team scope for that namespace.
  4. In the **Logs** tab, you can [view fleet scope logs by namespace](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-logs).



### Add fleet namespaces to a team scope

  1. To add a new fleet namespace, at the top of the page, click **Add Namespaces**.
  2. Enter the name of the new fleet namespace, ensuring that the name does not conflict with the fleet namespace naming restrictions. To add more namespaces, click **Add Namespace**.
  3. Click **Update Team Scope**.



### Delete a fleet namespace

  1. Select the **Namespaces** tab which shows you a list of the fleet namespaces created in the team scope.
  2. Click the Trash icon next to the namespace you want to delete.
  3. Confirm the deletion by entering the name of your namespace, and click **Delete** again.



Note that what happens when you do this depends on how you added the namespace:

  * If you **created a new fleet namespace:** The fleet namespace is deleted. Any Kubernetes namespaces created as a result of creating the fleet namespace are also deleted, together with their workloads.
  * If you **onboarded an existing Kubernetes namespace:** The fleet namespace is deleted. However, the original namespace that you onboarded is _not_ deleted.



### Update a fleet namespace name

You cannot edit a fleet namespace once it's been created. If you need to update a fleet namespace name, delete the namespace, and create a new one in the team scope.

## Manage team access

### gcloud

### List team members

To list all team members granted access to the team scope with the `add-app-operator-binding` command, together with their permission personas, use the following command:
    
    
    gcloud beta container fleet scopes list-app-operator-bindings SCOPE_NAME
    

Replace the following:

  * SCOPE_NAME: the team scope's unique identifier.



### Remove team members

To remove a team member's scope access (granted with `add-app-operator-binding`), use the following command:
    
    
    gcloud beta container fleet scopes remove-app-operator-binding SCOPE_NAME \
       --group=TEAM_EMAIL
    

or
    
    
    gcloud beta container fleet scopes remove-app-operator-binding SCOPE_NAME \
       --user=USER_EMAIL
    

Replace the following:

  * SCOPE_NAME: the team scope's unique identifier.
  * TEAM_EMAIL or USER_EMAIL: the email address of the group or user you want to remove from the team.



If the team member was granted access with the `rbacrolebindings create` command, use the [`rbacrolebindings delete`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/scopes/rbacrolebindings/delete) command instead to remove the team member.

### Update team scope access

To update team scope access (for example, to grant team members a different role, or to update a group email address), remove the team member from the scope as described in the previous section, then grant them access again with their new details.

If the team member was granted access with the `rbacrolebindings create` command, you can use the [`rbacrolebindings update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/scopes/rbacrolebindings/update) command instead to update the member's access.

### Console

### Add or remove team members

To manage team members in a team scope:

  1. Go to the **Teams** page in the Google Cloud console:

[Go to Teams](https://console.cloud.google.com/kubernetes/teams/)

  2. Select the team scope whose members you want to manage.




To add new team members to the scope:

  1. At the top of the page, click **Add Team Members**. Follow the instructions as detailed in the Create a team scope section.
  2. Click **Update Team Scope**.



To remove team members from the scope:

  1. In the **Team** tab, click on the Trash icon next to the team member you want to remove from the team scope.
  2. Click **Delete** to confirm the deletion.



You cannot edit a team member's details in the Google Cloud console. To update scope access in the Google Cloud console (for example, to grant team members a different role, or to update a group email address), remove the team member from the scope, and add them again with the new details.

## Fleet namespace naming restrictions

The following names are reserved and forbidden for use when you create a fleet namespace in a team scope:

  * `default`
  * `kube-system`
  * `gke-connect`
  * `kube-node-lease`
  * `kube-public`
  * `istio-system`
  * `gatekeeper-system`
  * `asm-system`
  * `config-management-system`
  * `anthos-creds`
  * `anthos-identity-service`
  * `capi-kubeadm-bootstrap-system`
  * `capi-system`
  * `cert-manager`
  * `gke-managed-metrics-server`
  * `gke-system`
  * `config-management-monitoring`
  * `istio-gateway`
  * `knative-serving`
  * `resource-group-system`
  * `gke-mcs`
  * `appdevexperience`
  * `vm-system`
  * `gmp-system`
  * `gmp-public`
  * `gke-gmp-system`
  * `gke-managed-filestorecsi`
  * `apigee`
  * `apigee-system`



## Manage labels

To help you identify and manage your scopes, you can use the Google Cloud CLI to create and manage labels for your fleet namespaces and team scopes.

Labels added to a team scope are inherited by all fleet namespaces in the scope, which means they are attached to all Kubernetes namespaces in the scope's clusters. Labels added directly to a fleet namespace are attached only to its corresponding Kubernetes namespaces. If a team scope label and fleet namespace label have the same key, the team scope label takes precedence.

You can work on multiple key-value pairs at once by adding a comma-separated list of key-value pairs.

### Manage fleet namespace labels

#### Create a fleet namespace with labels

To create a fleet namespace with labels, run the following command:
    
    
    gcloud container fleet scopes namespaces create NAMESPACE_NAME \
        --scope SCOPE_NAME \
        --namespace-labels KEY=VALUE
    

Replace the following:

  * `NAMESPACE_NAME`: the unique name you have chosen for the namespace within the fleet.
  * `SCOPE_NAME`: the team scope where you want to use the namespace.
  * `KEY`: the key for the label's key-value pair.
  * `VALUE`: the value for the label's key-value pair.



#### Add or update labels for existing fleet namespaces

To add or update labels for an existing namespace run the following command:
    
    
    gcloud container fleet scopes namespaces update NAMESPACE_NAME \
        --scope SCOPE_NAME \
        --update-namespace-labels KEY=VALUE
    

#### Delete fleet namespace labels

To delete a specific fleet namespace label, run the following command:
    
    
    gcloud container fleet scopes namespaces update NAMESPACE_NAME \
        --scope SCOPE_NAME \
        --remove-namespace-labels KEY
    

Replace `KEY` with a comma separated list of the keys for the labels that you want to remove.

To delete all fleet namespace labels, run the following command:
    
    
    gcloud container fleet scopes namespaces update NAMESPACE_NAME \
        --scope SCOPE_NAME \
        --clear-namespace-labels
    

### Manage team scope labels

#### Create a team scope with labels

To create a scope with a label, run the following command:
    
    
    gcloud container fleet scopes create SCOPE_NAME \
        --namespace-labels KEY=VALUE
    

Replace the following:

  * `SCOPE_NAME`: the unique identifying name that you have chosen for your new team scope.
  * `KEY`: the key for the label's key-value pair.
  * `VALUE`: the value for the label's key-value pair.



#### Add or update labels for existing team scopes

To add or update labels for an existing scope run the following command:
    
    
    gcloud container fleet scopes update SCOPE_NAME \
        --update-namespace-labels KEY=VALUE
    

#### Delete team scope labels

To delete specific labels, run the following command:
    
    
    gcloud container fleet scopes update SCOPE_NAME \
         --remove-namespace-labels KEY
    

Replace `KEY` with a comma separated list of the keys for the labels that you want to remove.

To delete all labels, run the following command:
    
    
    gcloud container fleet scopes update SCOPE_NAME \
        --clear-namespace-labels
    

## What's next?

  * Learn how to view team-level metrics and other team-specific information in [Use the team overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management-overview).
  * Learn how to [use Config Sync to sync Kubernetes resources to team scopes and namespaces](https://docs.cloud.google.com/anthos-config-management/docs/how-to/fleet-tenancy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
