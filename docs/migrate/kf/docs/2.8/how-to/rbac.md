---
url: https://docs.cloud.google.com/migrate/kf/docs/2.8/how-to/rbac/
title: Configure role-based access control \u00a0|\u00a0 Kf 2.8 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:58:59.190387+00:00
---

# Configure role-based access control  |  Kf 2.8  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.8/how-to/rbac/

Version 2.8

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
  * [ 2.8 ](https://docs.cloud.google.com/migrate/kf/docs/2.8)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.8/getting-started)



Send feedback 

#  Configure role-based access control Stay organized with collections  Save and categorize content based on your preferences. 

The following steps guide you through configuring role-based access control (RBAC) in a Kf Space. 

## Before you begin

Please follow the [GKE RBAC guide](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) before continuing with the following steps.

## Configure Identity and Access Management (IAM)

In addition to permissions granted through Kf RBAC, users, groups, or service accounts must also be authenticated to view GKE clusers at the project level. This requirement is the same as for configuring GKE RBAC, meaning users/groups must have at least the `container.clusters.get` IAM permission in the project containing the cluster. This permission is included by the `container.clusterViewer` role, and other more privilleged roles. For more information, review [Interaction with Identity and Access Management](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#iam-interaction).

Assign `container.clusterViewer` to a user or group.
    
    
    gcloud projects add-iam-policy-binding ${CLUSTER_PROJECT_ID} \
      --role="container.clusterViewer" \
      --member="${MEMBER}"

Example member values are:

  * user:test-user@gmail.com
  * group:admins@example.com
  * serviceAccount:test123@example.domain.com



## Manage Space membership as SpaceManager

The cluster admin role, or members with **SpaceManager** role, can assign role to a user, group or service account.
    
    
    kf set-space-role MEMBER -t [Group|ServiceAccount|User]

The cluster admin role, or members with **SpaceManager** role, can remove a member from a role.
    
    
    kf unset-space-role MEMBER -t [Group|ServiceAccount|User]

You can view members and their roles within a Space.
    
    
    kf space-users

### Examples

Assign **SpaceDeveloper** role to a user.
    
    
    kf set-space-role alice@example.com SpaceDeveloper

Assign **SpaceDeveloper** role to a group.
    
    
    kf set-space-role devs@example.com SpaceDeveloper -t Group

Assign **SpaceDeveloper** role to a Service Account.
    
    
    kf set-space-role sa-dev@example.domain.com SpaceDeveloper -t ServiceAccount

## App development as SpaceDeveloper

Members with **SpaceDeveloper** role can perform Kf App development operations within the Space.

To push an App:
    
    
    kf push app_name -p [PATH_TO_APP_ROOT_DIRECTORY]

To view logs of an App: `posix-terminal kf logs app_name`

SSH into a Kubernetes Pod running the App: `posix-terminal kf ssh app_name`

View available service brokers:
    
    
    kf marketplace

## View Apps as SpaceManager or SpaceAuditor

Members with **SpaceManager** or **SpaceAuditor** role could view available Apps within the Space:
    
    
    kf apps

## View Kf Spaces within a cluster

All roles (**SpaceManager** , **SpaceDeveloper** , and **SpaceAuditor**) can view available Kf Spaces within a cluster:
    
    
    kf spaces

View Space members and their roles within a Space.
    
    
    kf space-users

## Impersonation flags

To verify a member's permission, a member with more priviliaged permission can test another member's permissions using the impersonation flags: `--as` and `--as-group`.

For example, as a cluster admin, you can verify if a user (username: bob) has permission to push an App.
    
    
    kf push APP_NAME --as bob

Verify a group (manager-group@example.com) has permission to assign permission to other members.
    
    
    kf set-space-role bob SpaceDeveloper --as-group manager-group@example.com

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
