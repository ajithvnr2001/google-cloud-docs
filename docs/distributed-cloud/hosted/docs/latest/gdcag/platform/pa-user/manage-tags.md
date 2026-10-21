---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-tags/
title: Manage project tags \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:41.110903+00:00
---

# Manage project tags  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage project tags Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This is a Preview feature that is available as-is and is not recommended for production environments. Google provides no Service-Level agreements (SLA) or technical support commitments for Preview features. For more information, see [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

This document explains how to manage your existing tag key-value pairs that organize your projects in Google Distributed Cloud (GDC) air-gapped. Tags are viewable by administrators with the use of Identity and Access Management (IAM) permissions. You can set permissions for your tag key-value pairs to enforce who can view them when they are bound to a project. You can also view existing tag attributes to help track how your tags are applied in your organization, such as the following:

  * Tag key namespace
  * Tag value namespace
  * Existing tags for a project



For more information about tags, see [Tags overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-tags).

This document is for IT administrators within the platform administrator group, who are responsible for organizing and managing projects in a GDC universe. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

  * To get the permissions you need to grant other users tag permissions or inspect tag key-value pair namespaces, ask your Organization IAM Admin to grant you the Tag Admin role (`tag-admin`).

  * To get the permissions you need to list a project with a tag, ask your Organization IAM Admin to grant you the Project Viewer role (`project-viewer`).




## Apply permissions to your tag key-value pair

Each tag key and tag value requires specific role bindings for users to access and manage them.

Set the appropriate roles for your tag keys and values to apply permissions.

  1. Identify your intended role name and required namespaces to apply that role. For more information, see [Tag usage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-tags#tag-usage).

  2. Grant the role permissions for a tag by applying the `RoleBinding` resource for each defined namespace:
         
         kubectl apply -f - <<EOF
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: BINDING_NAME
           namespace: NAMESPACE
         subjects:
         - kind: GROUP_SUBJECT
           name: GROUP_NAME
           apiGroup: rbac.authorization.k8s.io
         roleRef:
           kind: Role
           name: TAG_ROLE_NAME
           apiGroup: rbac.authorization.k8s.io
         EOF
         

Replace the following:

     * `BINDING_NAME`: the custom name for the role binding.

     * `NAMESPACE`: the namespace to apply the role binding to, such as `platform`, the tag key's management namespace, or the tag value's policy namespace.

     * `GROUP_SUBJECT`: the kind of subject to apply the role permissions to. This value can be `User`, `Group`, or `ServiceAccount`. For more information, see [Referring to subjects](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-subjects) Kubernetes documentation.

     * `GROUP_NAME`: the custom group name.

     * `TAG_ROLE_NAME`: the name of the tag role to apply, such as `tag-admin` or `tag-KEY_NAME-admin`.

For example, to grant the `tag-admin` role permission to a user for a tag key-value pair, deploy the following `RoleBinding` custom resources to the `platform` namespace, tag key's `managementNamespace`, and tag value's `policyNamespace`:
    
    kubectl apply -f - <<EOF
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: tag-admin-binding
      namespace: platform
    subjects:
    - kind: User
      name: user-1
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: Role
      name: tag-admin
      apiGroup: rbac.authorization.k8s.io
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: tag-admin-mgmt-binding
      namespace: g-t-tag-key-1
    subjects:
    - kind: User
      name: user-1
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: Role
      name: tag-admin
      apiGroup: rbac.authorization.k8s.io
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: tag-admin-policy-binding
      namespace: g-t-tag-value-1
    subjects:
    - kind: User
      name: user-1
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: Role
      name: tag-admin
      apiGroup: rbac.authorization.k8s.io
    EOF
    




## Find the management namespace

A management namespace is the system-generated namespace created for a tag key.

  * Find the management namespace of the specific tag key:
        
        kubectl get tagkey TAG_KEY_NAME --namespace platform \
            -o jsonpath='{.status.managementNamespace}'
        

Replace `TAG_KEY_NAME` with the name of your tag key.




## Find the policy namespace

A policy namespace is the system-generated namespace created for a tag value.

  * Find the policy namespace of the specific tag value:
        
        kubectl get tagvalue TAG_VALUE_NAME --namespace MANAGEMENT_NAMESPACE \
            -o jsonpath='{.status.policyNamespace}'
        

Replace the following:

    * `TAG_VALUE_NAME`: the name of the tag value.
    * `MANAGEMENT_NAMESPACE`: the name of the management namespace for the tag value's corresponding tag key. For more information, see Find the management namespace.



## List projects with a tag

To list all projects that are bound with a specific key-value pair, complete the following:

  * List all projects that match your tag key-value pair:
        
        kubectl get project --namespace platform --label tag.resourcemanager.gdc.goog/TAG_KEY_NAME=TAG_VALUE_NAME
        

Replace the following:

    * `TAG_KEY_NAME`: the name of the tag key.
    * `TAG_VALUE_NAME`: the name of the tag value.

The output is similar to the following:
    
    NAME            AGE
    project-1       17d
    project-2       10d
    project-3       4d
    




## What's next

  * [Resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy)
  * [Authenticate with service accounts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/service-identity)
  * [Design permissioning setup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/permissions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
