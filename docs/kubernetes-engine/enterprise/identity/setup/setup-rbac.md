---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/setup-rbac/
title: Set up RBAC policies for third-party identities \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:45.891038+00:00
---

# Set up RBAC policies for third-party identities  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/setup-rbac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Set up RBAC policies for third-party identities Stay organized with collections  Save and categorize content based on your preferences. 

Authentication is often combined with [Kubernetes role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) to provide more finely grained access control to clusters for authenticated users and service accounts. It is recommended to create RBAC policies that use group names instead of user identifiers. By linking your RBAC policies explicitly to groups, you can manage user access privileges entirely with your identity provider, so the cluster doesn't need to be updated every time user privileges change. Note that to configure access control based on membership of security groups with OIDC, you must ensure that your cluster is set up to support getting group membership information from your identity provider. This document applies only to fleet member clusters.

## Example

If you want certain authenticated users to have access to the cluster's [Pods](https://kubernetes.io/docs/concepts/workloads/pods/), create a `ClusterRole` that grants access to these resources, as in the following example:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: pod-reader
    rules:
    - apiGroups: [""]
      # The resource type for which access is granted
      resources: ["pods"]
      # The permissions granted by the ClusterRole
      verbs: ["get", "watch", "list"]
    

You then create a corresponding `ClusterRoleBinding` to grant the permissions in the `ClusterRole` to the relevant users—in this case, members of the `us-east1-cluster-admins` security group and the user with ID `u98523-4509823`:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: read-pods-admins
    subjects:
      # Grants anyone in the "us-east1-cluster-admins" group
      # read access to Pods in any namespace within this cluster.
    - kind: Group
      name: gid-us-east1-cluster-admins # Name is case-sensitive
      apiGroup: rbac.authorization.k8s.io
      # Grants this specific user read access to Pods in any
      # namespace within this cluster
    - kind: User
      name: uid-u98523-4509823
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: ClusterRole
      name: pod-reader
      apiGroup: rbac.authorization.k8s.io
    

**Note:** If your identity provider returns a group name that contains double backslash characters, then one of the backslash characters should be omitted when you reference the group name in the `ClusterRoleBinding` resource. For example, if you have created a group named `corp\\my-group`, reference it in the `ClusterRoleBinding` resource as `corp\my-group`. This is because the first backslash character is treated as an escape character.

In the following example, this `ClusterRoleBinding` grants permissions in the `ClusterRole` to the relevant group with ID `12345678-BBBb-cCCCC-0000-123456789012`. Note that this setting is relevant only for Azure AD providers and is available for Google Distributed Cloud clusters. 
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: pod-reader-binding
    subjects:
      # Retrieves group information for the group ID mentioned
    - kind: Group
      name: 12345678-BBBb-cCCCC-0000-123456789012
      apiGroup: rbac.authorization.k8s.io
    

For more information about using RBAC, see [Configure role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) and [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

## Create an RBAC role for Google Cloud console access

Users authenticated using OIDC providers can [log in to clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console) as well as the command line.

Authenticated users who want to access a cluster's resources in the Google Cloud console need to have the relevant Kubernetes permissions to do so. If you don't want to grant those users more extensive permissions, such as those of a cluster admin, you can create a custom RBAC role that includes the minimum permissions to view the cluster's nodes, persistent volumes, pods, and storage classes. You can define this set of permissions by creating a `ClusterRole` [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) resource, `cloud-console-reader`, in the cluster.

`cloud-console-reader` grants its users the `get`, `list`, and `watch` permissions on the cluster's nodes, persistent volumes, pods and storage classes, which allow them to see details about these resources.

###  kubectl 

To create the `cloud-console-reader` `ClusterRole` and apply it to the cluster, run the following command:
    
    
    cat <<EOF > cloud-console-reader.yaml
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: cloud-console-reader
    rules:
    - apiGroups: [""]
      resources: ["nodes", "persistentvolumes", "pods"]
      verbs: ["get", "list", "watch"]
    - apiGroups: ["storage.k8s.io"]
      resources: ["storageclasses"]
      verbs: ["get", "list", "watch"]
    EOF
    kubectl apply -f cloud-console-reader.yaml
    

You can then grant this `ClusterRole` to users when setting up your permission policies, as described in the previous section. Note that users also need [IAM permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console#required_roles) to view clusters in the Google Cloud console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
