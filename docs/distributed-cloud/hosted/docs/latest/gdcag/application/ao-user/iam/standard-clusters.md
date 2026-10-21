---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/standard-clusters/
title: Manage access to standard clusters \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:06:59.242300+00:00
---

# Manage access to standard clusters  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/standard-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage access to standard clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

This document explains how to grant access and manage permissions within standard clusters in Google Distributed Cloud (GDC) air-gapped. Standard clusters are project-scoped, configurable Kubernetes environments with minimal default services that offer greater flexibility and control for custom workloads.

For information about managing standard cluster lifecycles, such as creating or deleting clusters, see [Create a standard cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-standard-cluster) and [Delete a standard cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-standard-cluster).

For more information about standard clusters and other cluster types, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

This document is for audiences within the application operator group, such as developer operations or data scientists, who need to manage and secure resources within GDC projects. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before managing access to standard clusters, you must have the necessary permissions and prepare your environment.

### Request IAM roles

To get the permissions you need to manage access to standard clusters, request the following roles based on the tasks you need to perform:

  * To grant and manage project-level IAM policy bindings for standard clusters, contact your IAM Org Admin to request the **IAM Project Admin** (`project-iam-admin`) role.
  * To manage in-cluster Kubernetes role-based access control (RBAC) and deploy workloads within a standard cluster, ask your IAM Project Admin to grant you the **Cluster Admin** (`cluster-admin`) role.



### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).




## Grant permissions for standard cluster access

A user with the IAM Project Admin (`project-iam-admin`) role can grant other users the necessary roles for managing access within standard clusters:

  1. [Sign in with your configured identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#sign-in-with-idp) using the gdcloud CLI.

  2. Grant the user the Cluster Admin (`cluster-admin`) role for the project. This command binds the user to the role, allowing them to manage access within the standard cluster.

See [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-descriptions) and [Role definitions for projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-definitions) for more information about the roles.
         
         gdcloud projects add-iam-policy-binding PROJECT \
           --role=ROLE \
           --member=user:USER_ACCOUNT
         

Replace the following variables:

     * `PROJECT`: the name of the project where the standard cluster exists.
     * `ROLE`: the name of the role you want to grant (such as `cluster-admin`).
     * `USER_ACCOUNT`: the user account for which you want to grant the role, including the identity provider prefix associated with your organization (such as `idpprefix-user@example.com`). The specific prefix used depends on your organization's IdP configuration. See [Connect to an identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/connect-identity) for more information.

The following example grants the Cluster Admin role to `user@example.com`, assuming the identity provider prefix is `fop-` for project `foo`:
    
    gdcloud projects add-iam-policy-binding foo \
      --role=cluster-admin \
      --member=user:fop-user@example.com
    




## Manage access within the standard cluster

A user with the Cluster Admin (`cluster-admin`) role can grant access within a standard cluster:

  1. [Sign in with your configured identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#sign-in-with-idp) using the gdcloud CLI.

  2. Generate a kubeconfig file for a standard cluster using the `--standard` flag. This flag is required to target a standard cluster.
         
         export KUBECONFIG=KUBECONFIG_FILE
         gdcloud clusters get-credentials STANDARD_CLUSTER_NAME --standard --project=PROJECT
         

Replace the following variables:

     * `KUBECONFIG_FILE`: the path to the kubeconfig file such as `standard-cluster-kubeconfig.yaml`.
     * `STANDARD_CLUSTER_NAME`: the name of the standard cluster.
     * `PROJECT`: the name of the project where the standard cluster exists.
  3. Define permissions within the standard cluster using `kubectl`.

Users with `cluster-admin` permissions can create custom `Role` and `ClusterRole` objects. To grant these permissions, they can create the corresponding `Rolebinding` and `ClusterRoleBinding` objects to bind the roles to specific subjects, such as users or service accounts.

**Note:** Users can only grant permissions they already possess. They can't use this access to escalate their own permissions.

The following example uses `kubectl` to create a sample custom `Role` named `test-role` in the `test` namespace:
         
         kubectl apply -f - <<EOF
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: test-role
           namespace: test
         rules:
         - apiGroups:
           - ""
           resources:
           - configmaps
           verbs:
           - get
         EOF
         

The following example creates the `RoleBinding` for the `Role` named `test-role` in the `test` namespace. It grants permissions to the user alice@example.com with the identity provider prefix `fop-`, as well as to a `ServiceAccount` named `my-service-account` in the `default` namespace:
         
         kubectl apply -f - <<EOF
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: test-role-binding
           namespace: test
         subjects:
         - kind: User
           name: fop-alice@example.com
           apiGroup: rbac.authorization.k8s.io
         - kind: ServiceAccount
           name: my-service-account
           namespace: default
         roleRef:
           kind: Role
           name: test-role
           apiGroup: rbac.authorization.k8s.io
         EOF
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
