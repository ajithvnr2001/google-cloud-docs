---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/anthos-ui/
title: Manage clusters from the Google Cloud console \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:52.514364+00:00
---

# Manage clusters from the Google Cloud console  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/anthos-ui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Manage clusters from the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to make admin and user clusters created with Distributed Cloud software only for bare metal available for management in the Google Cloud console. Cluster management capabilities include being able to log in to clusters, view workloads, upgrade, update, and delete clusters.

## Fleet members and the console

All clusters must be members of a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)—a unified way to view and manage multiple clusters and their workloads. Each fleet of clusters is associated with a [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project).

All clusters are registered to a fleet at creation time:

  * When you create a cluster using `bmctl`, you specify your fleet host project in the `gkeConnect` section of the cluster configuration file. The cluster becomes a fleet member of the specified project.

  * When you create an admin or user cluster with a standard GKE On-Prem API client (the console, the Google Cloud CLI, or Terraform), the cluster becomes a fleet member in the specified project.




Fleet members outside of Google Cloud, like Google Distributed Cloud, are displayed in the console in your fleet host project, along with other fleet clusters such as GKE on Google Cloud. The extent to which you can manage bare metal clusters from the console depends on the following:

  * If you have set up authentication, you can log in to your clusters and view their workloads and other details.

  * If you have enabled cluster lifecycle management for the cluster, you can upgrade admin and users clusters by using the console, and you can use the console to update and delete user clusters. If this feature isn't enabled, you can only manage cluster lifecycle using `bmctl` on your admin workstation.




## View registered clusters

All your clusters are displayed on the [GKE clusters](https://console.cloud.google.com/kubernetes/list/overview) page in the console. This both gives you an overview of your entire fleet and, for Google Distributed Cloud, lets you see which clusters are managed by the GKE On-Prem API.

To view your fleet clusters:

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project.

     * If **Bare metal** is displayed in the **Type** column, the cluster is managed by the GKE On-Prem API. Note, only admin and user clusters can be managed by the GKE On-Prem API.

     * If **External** is displayed in the **Type** column, the cluster isn't managed by the GKE On-Prem API.




To see more details about a cluster, you need to log in and authenticate to the cluster. To do this, you need to do the following steps:

  * Set up an authentication method
  * Grant users specific Identity and Access Management roles



### Set up authentication

As described previously, all clusters appear in the GKE clusters page in the console. However, to see more details such as nodes and workloads (and to do cluster lifecycle management tasks if the feature is enabled), you need to log in and authenticate to the cluster. To do this, your clusters must be set up with one of the following authentication methods:

  * **Google identity** : This option lets you log in using your Google Cloud identity, which is the email address associated with your Google Cloud account. Use this option if users already have access to Google Cloud with their Google identity. If you created the cluster in the console, you can log in to the cluster using your Google identity, but you will need to configure authentication for other users.

Login with Google identity is the simplest approach to authentication in the console, so we've described how to set this up in more detail in Set up Google identity authentication.

  * **OpenID Connect (OIDC)** : This option lets you log in to clusters from the console using their identity from a third-party OIDC identity provider such as Okta or Microsoft AD FS. You might want to use this option if your users have existing usernames, passwords, and security group memberships from your provider. You can find out how to set up third-party OIDC authentication for your clusters in the following guides:

    * [Configure clusters for GKE Identity Service with OIDC](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster): This guide shows you how to set up OIDC authentication on a cluster by cluster basis.

    * [Set up GKE Identity Service for a fleet](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet): This option lets you set up OIDC at the fleet level.

  * **Bearer token** : If the preceding Google-provided solutions aren't suitable for your organization, you can set up authentication using a Kubernetes service account and using its bearer token to log in. For details, see [Set up using a bearer token](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/bearer-token-auth).




### Grant required roles

Access to the console is controlled by Identity and Access Management (IAM). To manage the cluster lifecycle in the console you need to grant some IAM roles to users who aren't project owners:

  * To let users access the console, at a minimum, you need to grant the following roles:

    * `roles/container.viewer`: This role lets users view the GKE Clusters page and other container resources in the console. For details about the permissions included in this role, or to grant a role with read and write permissions, see [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) in the IAM documentation.

    * `roles/gkehub.viewer`: This role lets users view clusters outside Google Cloud in the console. For details about the permissions included in this role, or to grant a role with read and write permissions, see [GKE Hub roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) in the IAM documentation.

  * To let users manage the cluster lifecycle in the console, grant the `roles/gkeonprem.admin` IAM role. The `roles/gkeonprem.admin` role gives users administrative access to the GKE On-Prem API, which the console uses to manage the cluster lifecycle. For details on the permissions included in this role, see [GKE on-prem roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem) in the IAM documentation.




The following commands shows how to grant the minimal roles needed to manage cluster lifecycle in the console:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=MEMBER \
        --role=roles/container.viewer
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=MEMBER \
        --role=roles/gkehub.viewer
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=MEMBER \
        --role=roles/gkeonprem.admin
    

where:

  * `PROJECT_ID` is the fleet host project. For clusters created using `bmctl`, this is the project that you configured in the `gkeConnect` section of the user cluster's configuration file. For clusters created in the console, this is the project that you chose when the cluster was created.

  * `MEMBER` is the user's email address in the format `user:emailID`, for example: `user:alice@example.com`




### Enable cluster lifecycle management in the console

Admin and user clusters created by using standard tools (the console, the gcloud CLI, or Terraform) are automatically enrolled in the GKE On-Prem API, which lets you perform cluster lifecycle management tasks in the console. In Google Distributed Cloud 1.16 and higher, when you create user and admin clusters using `bmctl`, they are enrolled in the GKE On-Prem API by default. If you need to enroll a cluster in the GKE On-Prem API, follow the steps in [Configure a cluster to be managed by the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster).

**Note:** If your cluster is enrolled in the GKE On-Prem API, you can use also use `bmctl` on your admin workstation to manage the cluster lifecycle.

## Set up Google identity authentication

To let users log in to the cluster using their Google identity, you need to configure the following:

  * Users need specific Identity and Access Management (IAM) roles to be able to see and interact with clusters in the console on the [GKE clusters](https://console.cloud.google.com/kubernetes/list/overview) page.

  * Users need to be added to the Kubernetes role-based access control (RBAC) policies that the [connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway) needs to access the cluster's Kubernetes API server using the [Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent).




### Configure RBAC authorization

Each cluster's Kubernetes API server needs to be able to authorize requests that come from the console. To configure authorization, you need to configure Kubernetes role-based access control (RBAC) policies for users on each cluster. Your Google Account is added as an administrator with full access to a user cluster in the following cases:

  * You created the user cluster in the console.

  * You created the user cluster using the gcloud CLI, and your Google Account was specified in the `--admin-users` flag in the cluster create command.

  * You created the user cluster using Terraform and your Google Account was specified in the `authorization.admin_users.username` field.

  * You created the user cluster using `bmctl` and configured your Google Account in the [clusterSecurity.authorization.clusterAdmin.gcpAccounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clustersecurity-authorization-clusteradmin-gcpaccounts).




You can add others as administrators after the cluster is created. You can use any of the following ways to grant administrative access to the cluster. Two different `gcloud` commands are provided.

  * The `gcloud ... generate-gateway-rbac` command needs to be run on your admin workstation because the command requires access to the cluster's kubeconfig and context (which are typically only on your admin workstation). The `generate-gateway-rbac` command lets you customize the RBAC policies, but the user email addresses won't be displayed as administrators in the **Cluster Details** section in the console.

  * The `gcloud ... update` command can be run on either your admin workstation or any computer that has access to the GKE On-Prem API.




Note that if you created an admin cluster in the Google Cloud console, you are granted read-only access to the cluster. If you want to be granted the `clusterrole/cluster-admin` role, someone with that role will need to add you using the `gcloud ... generate-gateway-rbac` command.

### `generate-gateway-rbac`

To apply the RBAC policies to users, do the following steps on your admin workstation:

  1. Run the following command to update components (if needed):
         
         gcloud components update
         

  2. Generate and apply the RBAC policies to your cluster for users and service accounts:
         
         gcloud container fleet memberships generate-gateway-rbac  \
             --membership=MEMBERSHIP_NAME \
             --role=ROLE \
             --users=USERS \
             --project=PROJECT_ID \
             --kubeconfig=KUBECONFIG_PATH \
             --context=KUBECONFIG_CONTEXT \
             --apply
         

Replace the following:

     * MEMBERSHIP_NAME: the name used to uniquely represent the cluster in its fleet. In Google Distributed Cloud, the membership name and the cluster name are the same.
     * ROLE: the Kubernetes role you want to grant to the users on the cluster. To grant users full access to every resource in the cluster in all namespaces, specify `clusterrole/cluster-admin`. To provide read-only access, specify `clusterrole/view`. To restrict access, create a custom role, for example: `role/mynamespace/namespace-reader`. The custom role must already exist before you run the command.
     * USERS: the email addresses of the users (user accounts or service accounts) to whom you want to grant the permissions, as a comma-separated list. For example: `--users=222larabrown@gmail.com,test-acct@test-project.iam.gserviceaccount.com`.
     * PROJECT_ID: the project ID of the fleet host project.
     * KUBECONFIG_PATH: the local path of your kubeconfig file that contains an entry for the cluster.
     * KUBECONFIG_CONTEXT: the context of the cluster as it appears in the kubeconfig file. You can get the current context from the command line by running `kubectl config current-context`. Whether you use the current context or not, make sure that it works for accessing the cluster by running a command such as:
           
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
    

This is the context for accessing the cluster through the [connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway).

For more details on the `generate-gateway-rbac` command, see the [gcloud CLI reference guide](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac).




### `update`

  1. Run the following command to update components:
         
         gcloud components update
         

  2. For each user that needs to be granted the `clusterrole/cluster-admin` role, include the `--admin-users` flag and run the following command. You can't specify multiple users in a single flag. Be sure to include your Google Account in the command because the command overwrites the grant list with the users that you specify in the command.
         
         gcloud container bare-metal clusters update USER_CLUSTER_NAME \
           --admin-users YOUR_GOOGLE_ACCOUNT \
           --admin-users ADMIN_GOOGLE_ACCOUNT_1 \
         




In addition to granting the Kubernetes `clusterrole/cluster-admin` role, the command grants the RBAC policies the users need to access the cluster through the [Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway).

### bmctl

To apply the RBAC policies to users, do the following steps on your admin workstation:

  1. Add the [`clusterSecurity.authorization`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clustersecurity-authorization) section to your cluster configuration file. Specify your email address and the email address of other users who need to administer the cluster. For example:
         
         ...
         clusterSecurity:
           authorization:
             clusterAdmin:
               gcpAccounts: [alex@example.com,hao@example.com,sasha@example.com]
         ...
         

**Note:** This field only applies to clusters that can run workloads. You can't specify `gcpAccounts` for admin clusters.
  2. Update the cluster:
         
         bmctl update cluster \
             -c CLUSTER_NAME \
             --kubeconfig=KUBECONFIG
         

Make the following changes:

     * Replace CLUSTER_NAME with the name of the cluster you want to update.
     * If the cluster is a self-managing cluster (such as admin or standalone cluster), replace KUBECONFIG with the path to the cluster's kubeconfig file. If the cluster is a user cluster, replace KUBECONFIG with the path to the **admin** cluster's kubeconfig file.



###  Console 

To apply the RBAC policies to users, do the following steps in the console:

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the cluster list, click the name of the cluster, and then click **View details** in the **Details** panel.

  4. In the **Authorization section** , click the **Admin users** field and enter the email address of each user.

  5. When you are finished adding users, click **Done**.


**Note:** When you add admin users, the GKE On-Prem API applies the Kubernetes RBAC policies to the cluster to grant the users the same administrative access that you were granted when you created the cluster. These policies grant users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces.

## More information

  * [Fleet management overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts)
  * [Work with clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console)
  * [Connect overview](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway)
  * [Connect Agent overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
