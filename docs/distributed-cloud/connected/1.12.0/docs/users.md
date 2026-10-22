---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/users/
title: Manage Distributed Cloud connected users \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:57.223035+00:00
---

# Manage Distributed Cloud connected users  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/users/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview)



Send feedback 

#  Manage Distributed Cloud connected users Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to manage users in a Distributed Cloud connected.

When you create a Distributed Cloud connected cluster, only the user account you used to create the cluster is granted access to that cluster. To grant more users access to the cluster, you can do one of the following:

  * Grant the required permissions using Kubernetes RBAC
  * Use connect gateway to access the cluster



## Grant the required permissions using Kubernetes RBAC

This section describes how to grant the permissions required by a user's business needs to the user's account using Kubernetes Role-Based Access Control (RBAC). These permissions are encapsulated by several roles. After you grant the appropriate role to a user account, you can add that account to the target Distributed Cloud connected cluster.

Distributed Cloud connected does not support Identity and Access Management groups or third-party identity providers for use with Kubernetes RBAC on Distributed Cloud connected clusters.

You need to use the following Kubernetes resources to grant roles to users:

  * `ClusterRole`: allows you to apply a set of permissions to any namespace in the cluster; also grants access to cluster-wide resources. 
  * `ClusterRoleBinding`: binds a `ClusterRole` resource to a user account.
  * `Role`: allows you to apply a set of permissions to a specific namespace.
  * `RoleBinding`: binds a `Role` or a `ClusterRole` resource to a user account in a specific namespace.



### Grant permissions for a cluster administrator

When you create a Distributed Cloud connected cluster, the user account you use to do so automatically becomes the cluster administrator. To grant cluster administrator permissions to additional users, bind the target user account to the `cluster-admin` role by creating a `ClusterRoleBinding` resource and apply it to the cluster:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: BINDING_NAME
    subjects:
      kind: User
      name: ACCOUNT_NAME
    roleRef:
      kind: ClusterRole
      name: cluster-admin
      apiGroup: rbac.authorization.k8s.io
    

Replace the following:

  * `BINDING_NAME`: a name that uniquely identifies this role binding.
  * `ACCOUNT_NAME`: the name of the target user account.



You can also use the following `kubectl` command:
    
    
    kubectl create clusterrolebinding "BINDING_NAME" \
      --clusterrole cluster-admin --user "ACCOUNT_NAME"
    

Replace the following:

  * `BINDING_NAME`: a name that uniquely identifies this role binding.
  * `ACCOUNT_NAME`: the name of the target user account.



## Grant permissions for an application developer

To grant an application developer the permissions necessary to deploy workloads on the target cluster, do the following:

  1. Create a `Role` resource that grants the permissions to create and manage Pods, Services, and deployments in the target namespace and apply it to the cluster:
         
         apiVersion: rbac.authorization.k8s.io/v1
          kind: Role
          metadata:
            namespace: NAMESPACE
            name: ROLE_NAME
          rules:
            apiGroups: ["apps", ""]
            resources: ["pods", "deployments", "services"]
            verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
         

Replace the following:

     * `NAMESPACE`: the name of the target namespace.
     * `ROLE_NAME`: a name that uniquely identifies this role.
  2. Create a `RoleBinding` resource that binds the target user accounts to the role you created in the previous step and apply to the cluster:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
          namespace: NAMESPACE
          name: BINDING_NAME
         subjects:
          kind: User
          name: ACCOUNT_NAME
          kind: User
          name: ACCOUNT_NAME
         roleRef:
          kind: Role
          name: ROLE_NAME
          apiGroup: rbac.authorization.k8s.io
         

Replace the following:

     * `BINDING_NAME`: a name that uniquely identifies this role binding.
     * `NAMESPACE`: the name of the target namespace.
     * `ACCOUNT_NAME`: the name of the target user account.
     * `ROLE_NAME`: the name of the target role.



### Grant permissions for a Cloud Build Service Agent

To grant a Cloud Build Service Agent the permissions necessary to deploy workloads on the target cluster, do the following:

  1. Create a `Role` resource that grants the permissions to create and manage Pods, Services, and deployments in the target namespace and apply it to the cluster:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
          namespace: NAMESPACE
          name: ROLE_NAME
         rules:
          apiGroups: ["apps", ""]
          resources: ["pods", "deployments", "services"]
          verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
         

Replace the following:

     * `NAMESPACE`: the name of the target namespace.
     * `ROLE_NAME`: a name that uniquely identifies this role.
  2. Create a `RoleBinding` resource that binds the target Cloud Build Service Agent account to the role you created in the previous step and apply to the cluster:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
          namespace: NAMESPACE
          name: BINDING_NAME
         subjects:
          kind: User
          name: PROJECT_ID@cloudbuild.gserviceaccount.com
         roleRef:
          kind: Role
          name: ROLE_NAME
          apiGroup: rbac.authorization.k8s.io
         

Replace the following:

     * `BINDING_NAME`: a name that uniquely identifies this role binding.
     * `NAMESPACE`: the name of the target namespace.
     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `ROLE_NAME`: the name of the target role.



If you need to grant a Cloud Build Service Agent permissions to deploy and manage workload across all namespaces on the target cluster, create a `ClusterRole` and a `ClusterRoleBinding` resource instead of the `Role` and `RoleBinding` resources.

## Grant permissions for viewing cluster information

To grant the permissions necessary to view detailed information about the cluster in the Google Cloud console, do the following:

  1. Create a `ClusterRole` resource that allows the Connect Agent to impersonate the user that needs to view the cluster information in the Google Cloud console:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
          name: ROLE_NAME
         rules:
          apiGroups: [""]
          resources: ["users"]
          verbs: ["impersonate"]
          resourceNames: ["ACCOUNT_NAME"]
         

Replace the following:

     * `ROLE_NAME`: the name of the target role.
     * `ACCOUNT_NAME`: the name of the target user account.
  2. Create a `ClusterRoleBinding` resource that binds the Connect Agent Service Agent account to the role you created in the previous step and apply to the cluster:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
          name: BINDING_NAME
         subjects:
          kind: ServiceAccount
          name: ACCOUNT_NAME
         roleRef:
          kind: ClusterRole
          name: ROLE_NAME
          apiGroup: rbac.authorization.k8s.io
         

Replace the following:

     * `BINDING_NAME`: a name that uniquely identifies this role binding.
     * `ACCOUNT_NAME`: the name of the target service user account.
     * `ROLE_NAME`: the name of the target role.



You must create a separate `ClusterRole` and `ClusterRoleBinding` resource pair for each affected user.

You can also use the `kubectl` command-line tool to grant the permissions necessary to view cluster information as follows:

  1. Create a `ClusterRole` resource that allows the Connect Agent to impersonate the user that needs to view the cluster information in the Google Cloud console:
         
         kubectl create clusterrole "ROLE_NAME" --verb impersonate \
          --resource users --resource-name "ACCOUNT_NAME"
         

Replace the following:

     * `ROLE_NAME`: the name of the target role.
     * `ACCOUNT_NAME`: the name of the target service user account.
  2. Create a `ClusterRoleBinding` resource that binds the Connect Agent Service Agent account to the role you created in the previous step and apply to the cluster:
         
         kubectl create clusterrolebinding "BINDING_NAME" --clusterrole \
          "ROLE_NAME" --serviceaccount "ACCOUNT_NAME"
         

Replace the following:

     * `BINDING_NAME`: a name that uniquely identifies this role binding.
     * `ACCOUNT_NAME`: the name of the target service user account.
     * `ROLE_NAME`: the name of the target role.



## Use connect gateway to access Distributed Cloud connected clusters

You have the option to use connect gateway to access your Distributed Cloud connected clusters. A connect gateway user needs one or more of the following roles depending on their business requirements:

  * **Connect Gateway Admin** (`roles/gkehub.gatewayAdmin`): grants access to the connect gateway API. This role enables the use of the `kubectl` command-line tool for managing the cluster.
  * **Connect Gateway Editor** (`roles/gkehub.gatewayEditor`): grants read and write access to the cluster.
  * **Connect Gateway Reader** (`roles/gkehub.gatewayReader`): grants read-only access to the cluster.
  * **GKE Hub Viewer** (`roles/gkehub.viewer`): grants the ability to retrieve kubeconfig files from the cluster.



For more information on using connect gateway, see the following:

  * [Setting up connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway/setup)
  * [Using connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway/using)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
