---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control/
title: Access control \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:08.837921+00:00
---

# Access control  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Access control Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes the differences between Identity and Access Management (IAM) and Kubernetes role-based access control (RBAC) in Google Kubernetes Engine to help you manage access to resources within your project. This document assumes that you know about the following:

  * [Overview of IAM in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam)
  * [Overview of Kubernetes RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control)



This document is for Security specialists who control access to permissions and want to understand the differences and overlap between IAM and RBAC. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks) .

## Manage access to GKE resources

When you create a Google Cloud project, you are the only user on the project. By default, no other users have access to your project or its resources, including Google Kubernetes Engine (GKE) resources. GKE supports multiple options for managing access to resources within your project and its clusters using role-based access control (RBAC).

These mechanisms have some functional overlap, but are targeted to different types of resources. Each is explained in a dedicated section on this page, but in brief:

  * Kubernetes RBAC is built into Kubernetes, and grants granular permissions to objects within Kubernetes clusters. Permissions exist as ClusterRole or Role objects within the cluster. RoleBinding objects grant Roles to Kubernetes users, Google Cloud users, IAM service accounts, or [Google Groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#google-groups-for-gke). 

If you primarily use GKE, and need fine-grained permissions for every object and operation within your cluster, Kubernetes RBAC is the best choice.

  * IAM manages Google Cloud resources, including clusters, and types of objects within clusters. Permissions are assigned to IAM _principals_.

There is no mechanism for granting permissions for specific Kubernetes objects within IAM. For instance, you can grant a user permission to create CustomResourceDefinitions (CRDs), but you can't grant the user permission to create only one specific CustomResourceDefinition, or limit creation to a specific Namespace or to a specific cluster in the project. An IAM role grants privileges across all clusters in the project, or all clusters in all child projects if the role is applied at the folder level.

If you use multiple Google Cloud components and you don't need to manage granular Kubernetes-specific permissions, IAM is a good choice.




## Kubernetes RBAC

Kubernetes has built-in support for RBAC that lets you create fine-grained Roles, which exist within the Kubernetes cluster. A Role can be scoped to a specific Kubernetes object or a type of Kubernetes object, and defines which actions (called verbs) the Role grants in relation to that object. A RoleBinding is also a Kubernetes object, and grants Roles to users. A GKE user can be any of:

  * Google Cloud user 
  * IAM service account
  * Kubernetes ServiceAccount 
  * Google Workspace user 
  * Google Workspace Google Group 
  * Users authenticated using [X509 client certificates](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#x509-client-certs)



To learn more, refer to [Role-Based Access Control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

## IAM

IAM lets you grant _roles_ to _principals_. A role is a collection of permissions, and when granted to a principal, allows that principal to access one or more Google Cloud _resources_. For more information about principals, roles, and other IAM terminology, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

In GKE, a principal can be any of the following:

  * User account
  * Service account 
  * Google Workspace Google Group 
  * Google Workspace domain 
  * Cloud Identity domain 



For more information about using IAM to control access in GKE, see [Create IAM allow policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam).

### IAM policy types

IAM supports the following policy types:

  * **Allow policies** : grant roles to principals. For details, see [Allow policy](https://docs.cloud.google.com/iam/docs/overview#cloud-iam-policy).
  * **Deny policies** : prevent principals from using specific IAM permissions regardless of the roles that those principals are granted. For details, see [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview).



Use deny policies to restrict specific principals from performing specific actions in your project, folder, or organization even if an IAM allow policy grants those principals a role that contains the relevant permissions.

### IAM recommendations

Consider using the following IAM predefined roles to facilitate common scenarios:

  * [Kubernetes Engine Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterViewer) (`roles/container.clusterViewer`): DevOps, engineers, and application developers who only need to connect to the cluster.
  * [Kubernetes Engine Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`): Platform administrators and cluster operators who need to manage one or more clusters in a Google Cloud project.



For a list of the available predefined IAM roles, refer to [Predefined GKE roles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#predefined).

GKE uses IAM service accounts that are attached to your nodes to run system tasks like logging and monitoring. At a minimum, these _node service accounts_ must have the [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`) role on your project. By default, GKE uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which is automatically created in your project, as the node service account. 

**Best practice:** Instead of using the Compute Engine default service account, create a _custom service account_ for your nodes to use and give it only the permissions that GKE needs to run system tasks. For more information, see [Configure a custom node service account](https://docs.cloud.google.com/kubernetes-engine/security/configure-node-service-accounts#configure-custom-account). 

## IAM interaction with Kubernetes RBAC

IAM and Kubernetes RBAC work together to help manage access to your cluster. RBAC controls access on a cluster and namespace level, while IAM works on the project level. An entity must have sufficient permissions at either level to work with resources in your cluster.

## What's next

  * [Read the GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
  * [Learn how to use Kubernetes RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).
  * [Learn how to create IAM policies for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam).
  * [Learn how to use IAM Conditions for load balancers](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
