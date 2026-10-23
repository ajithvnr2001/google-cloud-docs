---
url: https://docs.cloud.google.com/migrate/kf/docs/2.5/reference/kubernetes-roles/
title: Kubernetes Roles \u00a0|\u00a0 Kf 2.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:40.239810+00:00
---

# Kubernetes Roles  |  Kf 2.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.5/reference/kubernetes-roles/

Version 2.5

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.5 ](https://docs.cloud.google.com/migrate/kf/docs/2.5)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.5/reference)



Send feedback 

#  Kubernetes Roles Stay organized with collections  Save and categorize content based on your preferences. 

The following sections describe the [Kubernetes ClusterRoles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) that are created by Kf and lists the permissions that are contained in each ClusterRole.

## Space developer role

The Space developer role aggregates permissions application developers use to deploy and manage applications within a Kf Space.

You can retrieve the permissions granted to Space developers on your cluster using the following command.
    
    
    kubectl describe clusterrole space-developer

The default installation of Kf provides the following permissions:
    
    
    PolicyRule:
      Resources                               Non-Resource URLs  Resource Names  Verbs
      ---------                               -----------------  --------------  -----
      events                                  []                 []              [*]
      secrets                                 []                 []              [*]
      *.kf.dev                                []                 []              [*]
      networkpolicies.networking.k8s.io       []                 []              [*]
      pods/exec                               []                 []              [create]
      *.upload.kf.dev                         []                 []              [create]
      pods/log                                []                 []              [get list watch]
      pods                                    []                 []              [get list watch]
      rolebindings.rbac.authorization.k8s.io  []                 []              [get list watch]
    

## Space auditor role

The Space auditor role aggregates read-only permissions that auditors and automated tools use to validate applications within a Kf Space.

You can retrieve the permissions granted to Space auditors on your cluster using the following command.
    
    
    kubectl describe clusterrole space-auditor

The default installation of Kf provides the following permissions:
    
    
    PolicyRule:
      Resources                               Non-Resource URLs  Resource Names  Verbs
      ---------                               -----------------  --------------  -----
      events                                  []                 []              [*]
      apps.kf.dev                             []                 []              [get list watch]
      rolebindings.rbac.authorization.k8s.io  []                 []              [get list watch]
    

## Space manager role

The Space manager role aggregates permissions that allow delegation of duties to others within a Kf Space.

You can retrieve the permissions granted to Space managers on your cluster using the following command.
    
    
    kubectl describe clusterrole space-manager

The default installation of Kf provides the following permissions:
    
    
    PolicyRule:
      Resources                               Non-Resource URLs  Resource Names     Verbs
      ---------                               -----------------  --------------     -----
      clusterroles.rbac.authorization.k8s.io  []                 [space-auditor]    [bind]
      clusterroles.rbac.authorization.k8s.io  []                 [space-developer]  [bind]
      clusterroles.rbac.authorization.k8s.io  []                 [space-manager]    [bind]
      rolebindings.rbac.authorization.k8s.io  []                 []                 [get list update patch watch]
      apps.kf.dev                             []                 []                 [get list watch]
    

**Note:** Subjects bound to the `space-manager` ClusterRole within a Kf Space are also granted write access to that Space.

## Dynamic Space manager role

Each Kf Space creates a ClusterRole with the name `SPACE_NAME-manager`, where `SPACE_NAME-manager` is called the dynamic manager role.

Kf automatically grants all subjects with the `space-manager` role within the Space the dynamic manager role at the cluster scope. The permissions for the dynamic manager role allow Space managers to update settings on the Space with the given name.

You can retrieve the permissions granted to the dynamic manager role for any Space on your cluster using the following command.
    
    
    kubectl describe clusterrole SPACE_NAME-manager

The default installation of Kf provides the following permissions:
    
    
    PolicyRule:
      Resources      Non-Resource URLs  Resource Names  Verbs
      ---------      -----------------  --------------  -----
      spaces.kf.dev  []                 [SPACE_NAME]    [get list watch update patch]
    

## Kf cluster reader role

Kf automatically grants the `kf-cluster-reader` role to all users on a cluster that already have the `space-developer`, `space-auditor`, or `space-manager` role within a Space.

You can retrieve the permissions granted to Space Kf cluster readers on your cluster using the following command.
    
    
    kubectl describe clusterrole kf-cluster-reader

The default installation of Kf provides the following permissions:
    
    
    PolicyRule:
      Resources                     Non-Resource URLs  Resource Names  Verbs
      ---------                     -----------------  --------------  -----
      namespaces                    []                 [kf]            [get list watch]
      clusterservicebrokers.kf.dev  []                 []              [get list watch]
      spaces.kf.dev                 []                 []              [get list watch]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
