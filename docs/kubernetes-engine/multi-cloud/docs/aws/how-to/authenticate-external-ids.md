---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/authenticate-external-ids/
title: Authenticate to GKE on AWS with external identities \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:08.920381+00:00
---

# Authenticate to GKE on AWS with external identities  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/authenticate-external-ids/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Authenticate to GKE on AWS with external identities Stay organized with collections  Save and categorize content based on your preferences. 

Workforce identity federation grants non-Google identities access to Google Cloud services. In the context of GKE on AWS, this means you can use pre-existing external identities to create or access a GKE cluster without relying on Google credentials.

The benefits of using workforce identity federation are the following:

  * You eliminate the need for duplicate accounts across different platforms or providers.
  * You set permissions just once, bypassing the need for configurations on multiple platforms.
  * You simplify user access, because fewer logins and passwords are required.



## Before you begin

Before you can enable external users or groups to access GKE clusters, you need to perform the following steps:

  1. So that external users or groups can use the GKE on AWS API, configure workforce identity federation.:

     * For Azure users, see [Configure workforce identity federation with Azure AD](https://docs.cloud.google.com/iam/docs/workforce-sign-in-azure-ad).
     * For Okta users, see [Configure workforce identity federation with Okta](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta).
     * For users from other platforms, see [Configure workforce identity federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation).
  2. Assign your external users or groups the `gkemulticloud.viewer` role so that they can access clusters. Assign the `container.clusterViewer` role to view clusters in the Google Cloud console.

Note that roles are collections of permissions. When you assign a role to an entity (user, group, or service account), you're giving that entity all the permissions that the role contains.

###  Users 

For individual users, you need to assign the `gkemulticloud.viewer` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --role="roles/gkemulticloud.viewer" \
           --member="principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject/SUBJECT_VALUE"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `WORKFORCE_POOL_ID`: the ID that uniquely identifies your [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools) in Google Cloud. When formatting the ID, ensure that you follow the recommended guidelines provided in the IAM documentation under [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters).
     * `SUBJECT_VALUE`: the ID that uniquely identifies an external user. For example, the ID can be an email address such as `alex@cymbalgroup.com`.

###  Groups 

For groups, you need to assign the `gkemulticloud.viewer` role:
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --role="roles/gkemulticloud.viewer" \
      --member="principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID"
    

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `WORKFORCE_POOL_ID`: the ID that uniquely identifies your [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools) in Google Cloud. When formatting the ID, ensure that you follow the recommended guidelines provided in the IAM documentation under [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters).
     * `GROUP_ID`: an ID that uniquely identifies an external group.

  3. Optional: Assign your external users or groups the appropriate Identity and Access Management (IAM) roles. This step is only necessary if you want to grant users or groups the ability to create or update clusters; **it's not required for simply accessing a cluster**.

###  Users 

For individual users, you need to assign the `gkemulticloud.admin` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --role="roles/gkemulticloud.admin" \
           --member="principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject/SUBJECT_VALUE"
         

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




For more information about which API roles and permissions are required for GKE on AWS, see [API roles and permissions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/api-permissions).

## Grant external access to GKE clusters

There are two methods of setting up workforce identity federation so that external users or groups can access your GKE clusters.

Method #1 requires you to define an RBAC file and apply it to the cluster. This method offers fine-tuned control over permissions, such as allowing users read-only access to resources without granting them broader access.

Method #2 requires you to specify access for external identities when creating or updating a cluster. This method grants full administrative privileges to the specified users or groups.

Choose the method that best aligns with your desired level of access control: method #1 for more granular permissions, or method #2 for granting full cluster admin rights.

### Method #1: use an RBAC file

The first method of granting external access to GKE clusters involves the use of an RBAC file. Follow these steps:

  1. Define an RBAC YAML file that includes the subjects (users or groups) and the permissions you want to grant them within the GKE cluster. Here are example RBAC YAML configurations for individual users and for groups:

###  Users 
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: gateway-cluster-admin-user
         subjects:
         - kind: User
           name: principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject/SUBJECT_VALUE
         roleRef:
           kind: ClusterRole
           name: cluster-admin
           apiGroup: rbac.authorization.k8s.io
         

Replace the following:

     * `WORKFORCE_POOL_ID`: the ID that uniquely identifies your [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools) in Google Cloud. When formatting the ID, ensure that you follow the recommended guidelines provided in the IAM documentation under [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters).
     * `SUBJECT_VALUE`: the ID that uniquely identifies an external user. For example, the ID can be an email address such as `alex@cymbalgroup.com`.

###  Groups 
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: gateway-cluster-admin-group
    subjects:
    - kind: Group
      name: principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID
    roleRef:
      kind: ClusterRole
      name: cluster-admin
      apiGroup: rbac.authorization.k8s.io
    

Replace the following:

     * `WORKFORCE_POOL_ID`: the ID that uniquely identifies your [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools) in Google Cloud. When formatting the ID, ensure that you follow the recommended guidelines provided in the IAM documentation under [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters).
     * `GROUP_ID`: an ID that uniquely identifies an external group.

  2. Identify the GKE cluster you want to configure and set it as the active context using the following command:
         
         kubectl config use-context CLUSTER_CONTEXT
         

Replace `CLUSTER_CONTEXT` with the appropriate context name for your cluster.

  3. With the desired GKE cluster set as the active context, apply the RBAC configuration to the cluster using the following command:
         
         kubectl apply -f RBAC_PATH
         

Replace `RBAC_PATH` with the path to the RBAC file you created or edited.

When you run this command, the specified users or groups in the RBAC configuration now have the permissions to access and manage the targeted GKE cluster, as defined in the RBAC rules.

  4. If you need to make any subsequent changes to the permissions, modify the RBAC file and reapply it to the cluster by repeating the preceding steps.




### Method #2: give access to external identities during cluster creation or update

Method #2 grants access to external identities during the cluster creation or update process.

To create a cluster, follow the steps in [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster). To update a cluster, follow the steps in [Update a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-cluster).

When running the `gcloud` command to create or update a cluster, specify the `admin-users` and/or `admin-groups` parameters as follows:
    
    
    gcloud container aws clusters [create|update] CLUSTER_NAME \
        --location=LOCATION
        --admin-users=principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject SUBJECT_VALUE \
        --admin-groups=principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `LOCATION`: the Google Cloud region where your cluster is managed.
  * `WORKFORCE_POOL_ID`: the ID that uniquely identifies your [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools) in Google Cloud. When formatting the ID, ensure that you follow the recommended guidelines provided in the IAM documentation under [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters).
  * `SUBJECT_VALUE`: the ID that uniquely identifies an external user. For example, the ID can be an email address such as `alex@cymbalgroup.com`.
  * `GROUP_ID`: an ID that uniquely identifies an external group.



## Summary of granting external IDs access to GKE clusters

After performing either method #1 or method #2, the specified external users or groups can [use Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/connect-and-authenticate-to-your-cluster#use-google-cloud-console) to connect and view cluster details. Alternatively, they can [use `kubectl` with identity from the gcloud CLI](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/connect-and-authenticate-to-your-cluster#use-kubectl-with-identity-from-the-gcloud-cli) to manage, manipulate, and communicate with the cluster.

To execute `kubectl` commands against GKE clusters, see how to [generate a `kubeconfig` entry](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cluster-access-for-kubectl#generate_kubeconfig_entry).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
