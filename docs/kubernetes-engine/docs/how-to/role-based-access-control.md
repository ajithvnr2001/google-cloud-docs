---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control/
title: Authorize actions in clusters using role-based access control \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:02:23.484411+00:00
---

# Authorize actions in clusters using role-based access control  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Authorize actions in clusters using role-based access control Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to authorize actions on resources in your Google Kubernetes Engine (GKE) clusters using the built-in role-based access control (RBAC) mechanism in Kubernetes. Kubernetes RBAC is enabled by default, giving you fine-grained control over cluster access.

You'll learn how to define and assign precise permissions, create roles and role bindings to manage user access, verify API access to check the level of access, troubleshoot common issues, and understand limitations when working with RBAC in GKE.

This page is for Security specialists and Operators who want to use RBAC to improve security in their GKE clusters. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following concepts:

  * [Overview of Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
  * [Best practices for GKE RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac) for guidelines to improve the design of your RBAC policies.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Interaction with Identity and Access Management

You can use both [Identity and Access Management (IAM)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam) _and_ Kubernetes RBAC to control access to your GKE cluster:

  * IAM is not specific to Kubernetes; it provides identity management for multiple Google Cloud products, and operates primarily at the level of the Google Cloud project.

  * Kubernetes RBAC is a core component of Kubernetes and lets you create and grant roles (sets of permissions) for any object or type of object _within_ the cluster.

  * To authorize an action, GKE checks for an RBAC policy first. If there isn't an RBAC policy, GKE checks for IAM permissions.




In GKE, IAM and Kubernetes RBAC are integrated to authorize users to perform actions if they have sufficient permissions according to _either_ tool. This is an important part of bootstrapping a GKE cluster, since by default Google Cloud users do not have any Kubernetes RBAC RoleBindings.

To authorize users using Google Cloud accounts, the client must be correctly configured to authenticate using those accounts first. For example, if you are using `kubectl`, you must [configure the `kubectl` command to authenticate to Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl) before running any commands that require authorization.

**Note:** Many failures that appear to be due to authorization are actually caused because the cluster is unable to _authenticate_ the client. For example, there are special requirements for authenticating from Compute Engine instances, which are described in [Cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#authentication).

In almost all cases, Kubernetes RBAC can be used instead of IAM. GKE users require at minimum, the `container.clusters.get` IAM permission in the project that contains the cluster. This permission is included in the `container.clusterViewer` role, and in other more highly privileged roles. The `container.clusters.get` permission is required for users to _authenticate_ to the clusters in the project, but does not _authorize_ them to perform any actions inside those clusters. Authorization may then be provided by either IAM or Kubernetes RBAC.

## Define and assign permissions

You can define RBAC rules in `ClusterRole` and `Role` objects, and then assign those rules with `ClusterRoleBinding` and `RoleBinding` objects as follows:

  * **ClusterRole** : a cluster-level grouping of resources and allowed operations that you can assign to a user or a group using a `RoleBinding` or a `ClusterRoleBinding`.
  * **Role** : a namespaced grouping of resources and allowed operations that you can assign to a user or a group of users using a `RoleBinding`.
  * **ClusterRoleBinding** : assign a `ClusterRole` to a user or a group for all namespaces in the cluster.
  * **RoleBinding** : assign a `Role` or a `ClusterRole` to a user or a group within a specific namespace.



When you use a `RoleBinding` to assign a `ClusterRole` to a user or group, those users and groups can only access resources in the namespace you specify in the `RoleBinding`. If you want the users or groups to access resource across all namespaces, use a `ClusterRoleBinding` instead.

**Note:** RBAC roles are _additive_. There are no `deny` rules. When structuring your RBAC roles, think of each role as _granting_ access to resources.

### Define permissions using Roles or ClusterRoles

You define permissions within a Role or ClusterRole object. A Role defines access to resources within a single Namespace, while a ClusterRole defines access to resources in the entire cluster.

Roles and ClusterRoles have the same syntax. Each has a `rules` section, where you define the resources the rule applies to and allowed operations for the Role. For example, the following Role grants read access (`get`, `watch`, and `list`) to all pods in the `accounting` Namespace:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      namespace: accounting
      name: pod-reader
    rules:
    - apiGroups: [""] # "" indicates the core API group
      resources: ["pods"]
      verbs: ["get", "watch", "list"]
    

Refer to the [Role](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-v1/) and [ClusterRole](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/) API documentation for a full list of allowed fields.

**Note:** You cannot create a Role that defines permissions unless you already have the permissions defined in the Role. If you have been granted the [`cluster-admin` IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/container), this is sufficient.

#### `Role` vs. `ClusterRole`

Because permissions granted by a ClusterRole apply across the entire cluster, you can use ClusterRoles to control access to different kinds of resources than you can with Roles. These include:

  * Cluster-scoped resources such as nodes
  * Non-resource REST Endpoints such as `/healthz`
  * Namespaced resources _across all Namespaces_ (for example, all Pods across the entire cluster, regardless of Namespace)



### Assign Roles using RoleBindings or ClusterRoleBindings

After creating a Role or ClusterRole, you assign it to a user or group of users by creating a RoleBinding or ClusterRoleBinding. Users and groups are called `subjects`, and can be any of the following:

Subject type | Value for `kind` | Value for `name`  
---|---|---  
Google Cloud user account | `User` | Google Cloud registered email address  
Kubernetes service account | `ServiceAccount` | The name of a Kubernetes ServiceAccount object in the cluster  
IAM service account | `User` | Automatically generated IAM service account email address  
Google Group address on a verified domain | `Group` | Email address of a Google Workspace Group that is a member of the `gke-security-groups` group. For instructions to set up Google Groups for RBAC, refer to [Configure Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac).  
  
The following RoleBinding grants the `pod-reader` Role to a user, a Kubernetes service account, an IAM service account, and a Google Group:
    
    
    kind: RoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: pod-reader-binding
      namespace: accounting
    subjects:
    # Google Cloud user account
    - kind: User
      name: janedoe@example.com
    # Kubernetes service account
    - kind: ServiceAccount
      name: johndoe
    # IAM service account
    - kind: User
      name: test-account@test-project.iam.gserviceaccount.com
    # Google Group
    - kind: Group
      name: accounting-group@example.com
    roleRef:
      kind: Role
      name: pod-reader
      apiGroup: rbac.authorization.k8s.io
    

### Verify API access using `kubectl`

`kubectl` provides the `auth can-i` subcommand for quickly querying the API authorization layer. As a platform administrator, you might need to impersonate users to determine what actions they can perform. You can use the `auth can-i` and pass an additional `--as` flag.

When you run the command `kubectl auth can-i` without the `--as` flag, [Identity and Access Management (IAM)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam) performs the authorization. Whereas, when you append the `--as` flag, Kubernetes RBAC performs the authorization. Therefore, you will need to create the necessary `Role` and `RoleBinding` objects for RBAC.

For more information, see [Verifying API Access](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#checking-api-access).

### API Usage and Examples

For complete information on using the Kubernetes API to create the necessary `Role`, `ClusterRole`, `RoleBinding`, and `ClusterRoleBinding` objects for RBAC, see [Using Role-Based Access Control Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) in the Kubernetes documentation.

## Troubleshoot RBAC

To debug issues with RBAC, use the [Admin activity audit log](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging), which is enabled on all clusters by default. If access to a resource or operation is denied due to lack of sufficient permissions, the API server logs an `RBAC DENY` error, along with additional information such as the user's implicit and explicit group membership. If you are using Google Groups for RBAC, `google groups` appears in the log message.

## Limitations

The following sections describe interactions that might not seem obvious when working with Kubernetes RBAC and IAM.

### Default discovery roles

Clusters are created with a set of [default ClusterRoles and ClusterRoleBindings](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#discovery-roles). Requests made with valid credentials are placed in the `system:authenticated` group, whereas all other requests fall into `system:unauthenticated`.

The `system:basic-user` ClusterRole lets users make `SelfSubjectAccessReviews` to test their permissions in the cluster. The `system:discovery` role lets users read discovery APIs, which can reveal information about [`CustomResourceDefinitions`](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions) added to the cluster.

Anonymous users (`system:unauthenticated`) receive the `system:public-info-viewer` ClusterRole instead, which grants read-only access to `/healthz` and `/version` APIs.

To see the API endpoints allowed by the `system:discovery` ClusterRole, run the following command:
    
    
    kubectl get clusterroles system:discovery -o yaml
    

### Forbidden error for service accounts on Google Cloud VM instances

The following error can occur when the VM instance does not have the `userinfo-email` scope:
    
    
    Error from server (Forbidden): error when creating ... "role-name" is forbidden: attempt to grant extra privileges:...
    

For example, suppose the VM has `cloud-platform` scope but does not have `userinfo-email` scope. When the VM gets an access token, Google Cloud associates that token with the `cloud-platform` scope. When the Kubernetes API server asks Google Cloud for the identity associated with the access token, it receives the service account's unique ID, not the service account's email.

To authenticate successfully, either create a new VM with the `userinfo-email` scope or create a new role binding that uses the unique ID.

To create a new VM instance with the `userinfo-email` scope, run the following command:
    
    
    gcloud compute instances create INSTANCE_NAME \
        --service-account SERVICE_ACCOUNT_EMAIL \
        --scopes userinfo-email
    

To create a new role binding that uses the service account's unique ID for an existing VM, perform the following steps:

  1. Identify the service account's unique ID:
         
         gcloud iam service-accounts describe SERVICE_ACCOUNT_EMAIL
         

For example, the following output displays the `uniqueId` for the `my-iam-account@somedomain.com` service account:
         
         displayName: Some Domain IAM service account
         email: my-iam-account@somedomain.com
         etag: BwWWja0YfJA
         name: projects/project-name/serviceAccounts/my-iam-account@somedomain.com
         oauth2ClientId: '123456789012345678901'
         projectId: project-name
         uniqueId: '123456789012345678901'
         

  2. Create a role binding using the `uniqueId` of the service account:
         
         kubectl create clusterrolebinding CLUSTERROLEBINDING_NAME \
             --clusterrole cluster-admin \
             --user UNIQUE_ID
         




### Permission to create or update roles and role bindings

In Kubernetes, you can only create or update a role or a role binding with specific permissions if you meet the following conditions:

  * Create or update a role: You must already have the same permissions that you want to grant to the role. Alternatively, you must have authorization to perform the `escalate` verb on the role.
  * Create or update a role binding: You must already have the same permissions that are granted in the role being bound, with the same scope as the role binding. Alternatively, you must have authorization to perform the `bind` verb on the referenced role.



If the permissions that you're granting in the role were originally granted to you using an IAM allow policy instead of RBAC, your role or role binding request might fail. For example, consider the following role creation request, from a user who has been granted the IAM permissions `container.pods.*` and `container.roles.create`:
    
    
    kubectl create role allowed-to-view-pods --resource pods --verb list,get
    

If the user was only given the permissions using IAM, the following error could occur:
    
    
    Error from server (Forbidden): clusterroles.rbac.authorization.k8s.io "allowed-to-view-pods" is forbidden:
    user "caller@example.com" (groups=["system:authenticated"]) is attempting to grant RBAC permissions not currently held:
    {APIGroups:[""], Resources:["pods"], Verbs:["list" "get"]}
    

To mitigate this limitation, grant the caller the permissions in the role using RBAC instead of IAM.

You can alternatively use either RBAC or IAM to grant the caller the `escalate` verb, the `bind` verb, or both. However, GKE does not recommend this approach, because the caller can then grant _any_ permission to any role.

## What's next

  * Learn how to [configure Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac).
  * Learn how to [create IAM allow policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam).
  * Learn more about [access control](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control).
  * Learn more about [best practices for GKE RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac).
  * Learn how to [authenticate to the Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
