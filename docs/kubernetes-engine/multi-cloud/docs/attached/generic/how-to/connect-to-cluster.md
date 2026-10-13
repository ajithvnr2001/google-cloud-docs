---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/connect-to-cluster/
title: Connect to your CNCF conformant cluster \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:23.886049+00:00
---

# Connect to your CNCF conformant cluster  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/connect-to-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/concepts/overview)



Send feedback 

#  Connect to your CNCF conformant cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document describes three methods of connecting to your CNCF conformant attached cluster:

  * Method #1 connects to your cluster as a [Google user](https://docs.cloud.google.com/iam/docs/user-identities).
  * Method #2 connects to your cluster as a member of a [Google group](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console).
  * Method #3 connects to your cluster as a non-Google user or group.



These three methods of connecting to a registered cluster are enabled by a Google service called connect gateway. For details about connect gateway, see [Connecting to registered clusters with the Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).

This page is for IT administrators and Operators who want to set up, monitor, and manage cloud infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before you perform any of the methods, ensure that you've attached your cluster. For details, see [Attach your CNCF conformant cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/attach-cluster).

Before proceeding with method #2 or method #3, you need to satisfy additional prerequisites. For details, see the following sections.

### Before you begin method #2

To use method #2 of connecting to your attached cluster, ensure that you have the following prerequisites:

  * Latest version of Google Cloud CLI. For information on updating gcloud CLI, see [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update).
  * Attached cluster versions 1.26.0-gke.8, 1.27.0-gke.5, 1.28.0-gke.2 or later.



### Before you begin method #3

To use method #3 of connecting to your attached cluster, ensure that you have the following prerequisites:

  1. Ensure that you have the latest version of Google Cloud CLI. For information on updating gcloud CLI, see [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update).

  2. Ensure that you're using attached cluster versions 1.27.0-gke.5, 1.28.0-gke.2 or later.

  3. Configure workforce identity federation (so that external users or groups can use the GKE attached clusters API):

     * For Azure users, see [Configure workforce identity federation with Azure AD](https://docs.cloud.google.com/iam/docs/workforce-sign-in-azure-ad).
     * For Okta users, see [Configure workforce identity federation with Okta](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta).
     * For users from other platforms, see [Configure workforce identity federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation).
  4. Optional: Assign your external users or groups the appropriate Identity and Access Management (IAM) roles. This step is only necessary if you want to grant users or groups the ability to create or update clusters; **it's not required for simply accessing a cluster**.

Note that roles are collections of permissions. When you assign a role to an entity (user, group, or service account), you're giving that entity all the permissions that the role contains.

###  Users 

For individual users, you need to assign the `gkemulticloud.admin` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --role="roles/gkemulticloud.admin" \
           --member="principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject SUBJECT_VALUE"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `WORKFORCE_POOL_ID`: the ID that uniquely identifies your [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools) in Google Cloud. When formatting the ID, ensure that you follow the recommended guidelines provided in the IAM documentation under [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters).
     * `SUBJECT_VALUE`: the ID that uniquely identifies an external user. For example, the ID can be an email address such as `alex@cymbalgroup.com`.

###  Groups 

For groups, you need to assign the `gkemulticloud.admin` role:
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --role="roles/gkemulticloud.admin" \
      --member="principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID"
    

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `WORKFORCE_POOL_ID`: the ID that uniquely identifies your [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools) in Google Cloud. When formatting the ID, ensure that you follow the recommended guidelines provided in the IAM documentation under [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters).
     * `GROUP_ID`: an ID that uniquely identifies an external group.

For more information about which API roles and permissions are required for GKE attached clusters, see [API roles and permissions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/genericreference/api-permissions).




## Method #1: connect to your attached cluster as a Google user

To connect to an attached cluster as a Google user, follow these steps:

  1. Enable the `connectgateway` and `cloudresourcemanager` APIs with the following command:
         
         gcloud services enable --project=PROJECT_ID \
              connectgateway.googleapis.com \
              cloudresourcemanager.googleapis.com
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  2. Set up and apply RBAC rules either automatically or manually:

     * **Automatic method** : If, when you attached your cluster, you specified Google users in the `--admin-users` field of the `gcloud container attached clusters register` command, these users were automatically granted administrator privileges on the cluster. You can therefore skip this step.

     * **Manual method** : Manually set up RBAC rules for individual Google users by creating a Kubernetes YAML manifest. For details, see [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

  3. Obtain a Kubernetes `kubeconfig` configuration file with the following command:
         
         gcloud container fleet memberships get-credentials CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of the cluster whose connection credentials you want.




Once you've performed these steps, you can connect to your attached cluster as a Google user.

## Method #2: connect to your attached cluster with Google groups

This method enables you to connect to an attached cluster as a member of a Google group. In other words, you grant a Google group access to a cluster and any users belonging to that Google group have access to the cluster.

Using Google Groups to grant cluster access is more efficient than creating separate authorizations for individual users. For example, let's say you want to add 50 users to the cluster Administrator group, 75 users to an Editor group, and 100 users to a Reader group. Method #1, described in this document, would require you to create RBAC rules in the Kubernetes manifest file for 225 users. Method #2, however, saves you time because you only need to create RBAC rules for three Google groups.

To authorize Google groups to connect to an attached cluster, follow these steps:

  1. Enable the `connectgateway` and `cloudresourcemanager` APIs with the following command:
         
         gcloud services enable --project=PROJECT_ID \
               connectgateway.googleapis.com \
               cloudresourcemanager.googleapis.com
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  2. Create a group called `gke-security-groups` as a group in your project's domain if it doesn't exist.

  3. Create one or more sub-groups within the `gke-security-groups` group for cluster authentication.

  4. Add users to the newly created sub-groups.

  5. Grant IAM roles to Google Groups:

     1. Select an appropriate role for a group. This role determines how the group interacts with the connect gateway. The role can be one of the following: `roles/gkehub.gatewayAdmin`, `roles/gkehub.gatewayEditor`, `roles/gkehub.gatewayReader`. (Note that you're not granting permissions over the attached cluster here - that step comes later. Here, you're just determining how users of the group can manipulate the connect gateway).

     2. Run the following command to grant the role to the group:
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
              --member=group:GROUP_NAME@DOMAIN \
              --role=GATEWAY_ROLE
            

Replace the following:

        * `PROJECT_ID`: your Google project ID
        * `GROUP_NAME`: the name of the group to grant access to
        * `DOMAIN`: your Google Workspace domain
        * `GATEWAY_ROLE`: the selected role. For example `roles/gkehub.gatewayAdmin`, `roles/gkehub.gatewayEditor`, or `roles/gkehub.gatewayReader`.
  6. In a Kubernetes manifest, define what kind of permission each Google group has on the cluster. For example, the following manifest grants the Google Group `cluster-admin-team` the role of cluster administrator:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: gateway-cluster-admin-group
         subjects:
         - kind: Group
           name: cluster-admin-team@example.com
         roleRef:
           kind: ClusterRole
           name: cluster-admin
           apiGroup: rbac.authorization.k8s.io
         

  7. Save the manifest to a file and apply it to the cluster by running the following command:
         
         kubectl apply -kubeconfig=KUBECONFIG_PATH -f FILENAME
         

Replace the following:

     * `KUBECONFIG_PATH`: the path to your `kubeconfig` file.
     * `FILENAME`: the name of the manifest file you created.



Once you've performed these steps, users belonging to certain Google groups can connect to the attached cluster. In the given example, users belonging to the Google Group `cluster-admin-team` can connect to the cluster as administrators.

## Method #3: give access to external identities when attaching or updating a cluster

Method #3 grants access to external identities when you attach or update a cluster.

To attach an CNCF conformant cluster, follow the steps in [Attach your CNCF conformant cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/attach-cluster). To update an CNCF conformant cluster, follow the steps in [Update your CNCF conformant cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/update-cluster).

When running the gcloud CLI command to register or update a cluster, specify the `admin-users` and/or `admin-groups` parameters as follows:
    
    
    gcloud container attached clusters [register|update] CLUSTER_NAME \
        --admin-users=principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject SUBJECT_VALUE \
        --admin-groups=principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `WORKFORCE_POOL_ID`: the ID that uniquely identifies your [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools) in Google Cloud. When formatting the ID, ensure that you follow the recommended guidelines provided in the IAM documentation under [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters).
  * `SUBJECT_VALUE`: the ID that uniquely identifies an external user. For example, the ID can be an email address such as `alex@cymbalgroup.com`.
  * `GROUP_ID`: an ID that uniquely identifies an external group.



## What's next

To manage the cluster from the Google Cloud console with your Cloud Identity, see [Log in using your Google Cloud identity](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in#log_in_using_your_identity).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
