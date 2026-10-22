---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console/
title: Manage clusters from the Google Cloud console \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:17.556892+00:00
---

# Manage clusters from the Google Cloud console  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Manage clusters from the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to make clusters created with Google Distributed Cloud software for VMware available for management in the Google Cloud console. This includes basic management such as being able to log in to clusters and view their workloads, as well as how to enable cluster lifecycle management so that you can upgrade, update, and delete clusters.

## Fleet members and the console

All Google Distributed Cloud clusters must be members of a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)—a unified way to view and manage multiple clusters and their workloads. Each fleet of clusters is associated with a [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project).

In Google Distributed Cloud, an admin cluster is registered to a fleet at creation time by specifying your fleet host project in the `gkeConnect` section of the cluster configuration file. Google Distributed Cloud uses that information to register your cluster to the specified fleet project. If the registration failed, you can re-attempt the registration by running `gkectl update credentials register`.

Note that when re-attempting the registration, you don't need to update the [connect-register service account key](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account). In other words, you can continue using your original connect-register service account. For more information about the command, see [Rotatiing service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys).

In Google Distributed Cloud, a user cluster is registered to a fleet at creation time:

  * When you create a user cluster using `gkectl`, you specify your fleet host project in the `gkeConnect` section of the cluster configuration file. Google Distributed Cloud uses that information to register your cluster to the specified fleet project.

  * When you create a user cluster by using a standard tool (the console, the Google Cloud CLI or Terraform) the cluster automatically becomes a fleet member in the project that you specify.




Fleet members outside of Google Cloud like Google Distributed Cloud are displayed in the console in your fleet host project, along with other fleet clusters such as GKE on Google Cloud. The extent to which you can manage Google Distributed Cloud from the console depends on the following:

  * If you have set up authentication, you can log in to your clusters and view their workloads and other details.

  * If you have enabled cluster lifecycle management for the cluster, you can also upgrade, update, or delete user clusters by using the console. If this feature isn't enabled, you can only manage cluster lifecycle using `gkectl` on your admin workstation.




## View registered clusters

All your fleet clusters are displayed on the [Google Kubernetes Engine clusters overview](https://console.cloud.google.com/kubernetes/list/overview) page in the console. This both gives you an overview of your entire fleet and, for Google Distributed Cloud, lets you see which clusters are managed by the GKE On-Prem API.

To view your fleet clusters:

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project.

     * If **vm Google Distributed Cloud** is displayed in the **Type** column, the cluster is managed by the GKE On-Prem API.

     * If **External** is displayed in the **Type** column, the cluster isn't managed by the GKE On-Prem API.




To see more details about a cluster, users need to log in and authenticate to the cluster. To do this, you need to:

  * Set up an authentication method
  * Grant users specific Identity and Access Management roles



### Set up authentication

As described previously, all fleet clusters appear in the GKE clusters lists in the console. However, to see more details such as nodes and workloads (and to perform cluster lifecycle management tasks if the feature is enabled), users need to log in and authenticate to the cluster. To do this, your registered clusters must be set up with one of the following authentication methods:

  * **Google identity** : This option lets users log in using their Google Cloud identity, which is the email address associated with your Google Cloud account. Use this option if users already have access to Google Cloud with their Google identity. If you created the cluster in the console, you can log in to the cluster using your Google identity, but you will need to configure authentication for other users.

Login with Google identity is the simplest approach to authentication in the console, particularly if you are trying out Google Distributed Cloud with a minimal installation, and so we have described how to set this up in more detail below in Set up Google identity authentication.

  * **OpenID Connect (OIDC)** : This option lets users log in to clusters from the console using their identity from a third-party OIDC identity provider such as Okta or Microsoft AD FS. You might want to use this option if your users have existing usernames, passwords, and security group memberships from your provider. You can find out how to set up third-party OIDC authentication for your clusters in the following guides:

    * [Configure clusters for GKE Identity Service with OIDC](https://docs.cloud.google.com/anthos/identity/setup/per-cluster): This guide shows you how to set up OIDC authentication on a cluster by cluster basis.

    * [Set up GKE Identity Service for a fleet](https://docs.cloud.google.com/anthos/identity/setup/fleet): This option lets you set up OIDC at the fleet level.

  * **Bearer token** : If the preceding Google-provided solutions aren't suitable for your organization, you can set up authentication using a Kubernetes service account and using its bearer token to log in. For details, see [Set up using a bearer token](https://docs.cloud.google.com/anthos/identity/setup/bearer-token-auth).




### Grant required roles

Access to the console is controlled by Identity and Access Management (IAM). These IAM roles are required no matter which authentication method you choose. To manage the cluster lifecycle in the console you need to grant some IAM roles.

  * To let users access the console, at a minimum, you need to grant the following roles:

    * `roles/container.viewer`. This role lets users view the GKE Clusters page and other container resources in the console. For details about the permissions included in this role, or to grant a role with read/write permissions, see [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) in the IAM documentation.

    * `roles/gkehub.viewer`. This role lets users view clusters outside Google Cloud in the console. For details about the permissions included in this role, or to grant a role with read/write permissions, see [GKE Hub roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) in the IAM documentation.

  * To let users manage the cluster lifecycle in the console, grant the `roles/gkeonprem.admin` IAM role. The `roles/gkeonprem.admin` role gives users administrative access to the GKE On-Prem API, which the console uses to manage the cluster lifecycle. For details on the permissions included in this role, see [GKE on-prem roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem) in the IAM documentation.




The following commands shows how to grant the minimal roles needed to manage cluster lifecycle in the console:
    
    
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member=MEMBER \
        --role=roles/container.viewer
    
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member=MEMBER \
        --role=roles/gkehub.viewer
    
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member=MEMBER \
        --role=roles/gkeonprem.admin
    

where:

  * `FLEET_HOST_PROJECT_ID` is the fleet host project. For clusters created using `gkectl`, this is the project that you configured in the `gkeConnect` section of the user cluster's configuration file. For clusters created in the console, this is the project that you chose when the cluster was created.

  * `MEMBER` is the user's email address in the format `user:emailID`, for example: `user:alice@example.com`




### Enable cluster lifecycle management in the console

User clusters created by using standard tools (the console, the gcloud CLI, or Terraform) are automatically enrolled in the GKE On-Prem API, and let you perform cluster lifecycle management tasks in the console. If you want to enable this feature for user clusters created using `gkectl`, follow the steps in [Configure a user cluster to be managed by the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster). When cluster lifecycle management is enabled, you can do the following tasks from the console:

  * [Upgrade user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading)
  * [Resize user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resizing-a-user-cluster)
  * [Create and manage node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools)
  * [Delete user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-a-user-cluster)

**Note:** If you prefer not to manage cluster lifecycle from Google Cloud, the same tasks can all be performed by using the admin workstation and `gkectl`.

## Set up Google identity authentication

To let users log in to the cluster using their Google identity, you need to configure the following:

  * Users need specific Identity and Access Management (IAM) roles to be able to see and interact with clusters in the console on the [GKE Clusters list](https://console.cloud.google.com/kubernetes/list).

  * Users need to be added to the Kubernetes role-based access control (RBAC) policies that the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway) needs to access the cluster's Kubernetes API server via the [Connect agent](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent).




### Configure RBAC authorization

Each cluster's Kubernetes API server needs to be able to authorize requests that come from the console. To configure authorization, you need to configure Kubernetes role-based access control (RBAC) policies on each cluster.

If you used a standard tool to create the user cluster, you might already be granted the appropriate RBAC policies that grant you full administrative access to the cluster. The GKE On-Prem API adds your Google Account automatically as an administrator in the following cases:

  * You created the user cluster in the console.

  * You created the user cluster using the gcloud CLI, and your Google Account was specified in the `--admin-users` flag in the cluster create command.

  * You created the user cluster using Terraform and you Google Account was specified in the `authorization.admin_users.username` field.




User clusters created using `gkectl` don't grant you the RBAC policies to administer the cluster using the console. You need to add yourself after the cluster is created. No matter which tool that you used to create the cluster, you can add others as administrators after the cluster is created.

You can use any of the following ways to grant administrative access to the cluster. Two different `gcloud` commands are provided.

  * The `gcloud ... generate-gateway-rbac` command needs to be run on your admin workstation because the command requires access to the cluster's kubeconfig and context (which are typically only on your admin workstation). The `generate-gateway-rbac` command lets you customize the RBAC policies, but the user email addresses won't be displayed as administrators in the **Cluster Details** section in the console.

  * The `gcloud ... update` command can be run on either your admin workstation or any computer that has access to the GKE On-Prem API.




### `generate-gateway-rbac`

  1. Connect to your admin workstation.

  2. Run the following command to update components:
         
         gcloud components update
         

  3. Generate and apply the RBAC policies to your cluster for users and service accounts:
         
         gcloud container fleet memberships generate-gateway-rbac  \
             --membership=MEMBERSHIP_NAME \
             --role=ROLE \
             --users=USERS \
             --project=FLEET_HOST_PROJECT_ID \
             --kubeconfig=KUBECONFIG_PATH \
             --context=KUBECONFIG_CONTEXT \
             --apply
         

Replace the following:

     * MEMBERSHIP_NAME: the name used to uniquely represent the cluster in its fleet. In Google Distributed Cloud, the membership name and the cluster name are the same.
     * ROLE: the Kubernetes role you want to grant to the users on the cluster. To grant users full access to every resource in the cluster in all namespaces, specify `clusterrole/cluster-admin`. To provide read-only access, specify `clusterrole/view`. You can also, create a custom role, for example: `role/mynamespace/namespace-reader`. The custom role must already exist before you run the command.
     * USERS: the email addresses of the users (user accounts or service accounts) to whom you want to grant the permissions, as a comma-separated list. For example: `--users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com`.
     * FLEET_HOST_PROJECT_ID: the project ID of the fleet host project.
     * KUBECONFIG_PATH: the local path where your kubeconfig containing an entry for the cluster is stored.
     * KUBECONFIG_CONTEXT: the context of the cluster as it appears in the kubeconfig file. You can get the current context from the command line by running `kubectl config current-context`. Whether you use the current context or not, make sure that it works for accessing the cluster by running a simple command such as:
           
           kubectl get namespaces \
             --kubeconfig=KUBECONFIG_PATH \
             --context=KUBECONFIG_CONTEXT

After running `gcloud container fleet memberships generate-gateway-rbac`, you see something like the following at the end of the output, which is truncated for readability:
    
    Validating input arguments.
    Specified Cluster Role is: clusterrole/cluster-admin
    Generated RBAC policy is:
    --------------------------------------------
    ...
    Applying the generate RBAC policy to cluster with kubeconfig: /usr/local/google/home/foo/.kube/config, context: kind-kind
    Writing RBAC policy for user: foo@example.com to cluster.
    Successfully applied the RBAC policy to cluster.
    

This is the context for accessing the cluster through the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).

For more details on the `generate-gateway-rbac` command, see the [gcloud CLI reference guide](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac).




### `update`

  1. Run the following command to update components:
         
         gcloud components update
         

  2. For each user that needs to be granted the `clusterrole/cluster-admin` role, include the `--admin-users` flag and run the following command. You can't specify multiple users in a single flag. Be sure to include your Google Account in the command because the command overwrites the grant list with the users that you specify in the command.
         
         gcloud container vmware clusters update USER_CLUSTER_NAME \
           --admin-users YOUR_GOOGLE_ACCOUNT \
           --admin-users ADMIN_GOOGLE_ACCOUNT_1 \
         




In addition to granting the Kubernetes `clusterrole/cluster-admin` role, the command grants the RBAC policies the users need to access the cluster through the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).

### Console

To apply the RBAC policies to users, do the following steps in the console:

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the cluster list, click the name of the cluster to display its details.

  4. In the **Authorization** section, click the **Admin users** edit button.

  5. Enter the email address of the user you want to add as a cluster admin in the **Edit authorization** panel. To add additional admin users, click **Add admin user**.

  6. When you are finished adding users, click **Save changes**.


**Note:** When you add admin users, the GKE On-Prem API applies the Kubernetes RBAC policies to the cluster to grant the users the same administrative access that you were granted when you created the cluster. These policies grant users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces.

## More information

  * [Fleet management overview](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts)
  * [Work with clusters from the Google Cloud console](https://docs.cloud.google.com/anthos/fleet-management/docs/console)
  * [Connect overview](https://docs.cloud.google.com/anthos/multicluster-management/gateway)
  * [Connect Agent overview](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
