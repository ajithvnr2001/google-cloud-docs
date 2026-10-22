---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/authentication/
title: Authentication overview \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:41.900438+00:00
---

# Authentication overview  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/authentication/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authentication overview

This page describes how GKE on Azure handles authentication to Google Cloud and user authentication to your clusters.

## How GKE on Azure connects to Azure

The GKE Multi-Cloud API authenticates to Azure with an _AzureClient_ object. When you create a client, Google generates an [X.509](https://wikipedia.org/wiki/X.509) key pair. You upload the public key to Azure Active Directory (Azure AD).

For more information, see [Create an AzureClient](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-client).

## Authentication

### GKE Multi-Cloud API authentication

You use the GKE Multi-Cloud API to create, update, and delete clusters and node pools. As with other Google Cloud APIs, you can use this API with REST, Google Cloud CLI, or the Google Cloud console.

For more information, see [Google Cloud authentication overview](https://docs.cloud.google.com/docs/authentication) and the [GKE Multi-Cloud API](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest) reference documentation.

### Kubernetes API authentication

You can use the `kubectl` command-line tool to perform cluster operations such as deploying a workload and configuring a load balancer. The `kubectl` tool connects to the Kubernetes API on your cluster's control plane. To call this API, you need to authenticate with authorized credentials.

To get credentials, you can use one of the following methods:

  * [Google Identity](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster#google-identity), which lets users log in using their Google Cloud identity. Use this option if your users already have access to Google Cloud with a Google Identity.

  * [GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/anthos-identity-service), which lets users log in using OpenID Connect (OIDC).




GKE Identity Service lets you use identity providers such as [Okta](https://www.okta.com/), [Active Directory Federation Services (ADFS)](https://docs.microsoft.com/windows-server/identity/active-directory-federation-services), or any [OIDC](https://openid.net/connect/) compliant identity provider.

## Authorization

GKE on Azure has two methods for access control, the GKE Multi-Cloud API and [role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/). This section describes the differences between these methods.

It's best to take a layered approach to protecting your clusters and workloads. You can apply the [principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege) to the level of access that you provide to your users and workloads. You might need to make tradeoffs to allow the right level of flexibility and security.

### GKE Multi-Cloud API access control

The GKE Multi-Cloud API lets cluster administrators create, update, and delete clusters and node pools. You manage permissions for the API with Identity and Access Management (IAM). To use the API, users must have the appropriate permissions. For the permissions necessary for each operation, see [API roles and permissions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/api-permissions). IAM lets you define [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) and assign them to [principals](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity). A role is a collection of permissions, and when assigned to a principal, controls access to one or more Google Cloud [resources](https://docs.cloud.google.com/iam/docs/overview#resource).

When you create a cluster or node pool in an organization, folder, or project, users with appropriate permissions in that organization, folder, or project can modify it. For example, if you give a user a cluster deletion permission at a Google Cloud project level, that user can delete any cluster in that project. For more information, see [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) and [Creating IAM policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam).

### Kubernetes API access control

The Kubernetes API lets you manage [Kubernetes objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/). To manage access control on the Kubernetes API, you use role-based access control (RBAC). For more information, see [Configuring role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) in the GKE documentation.

#### Administrator access

When you use the gcloud CLI to create a cluster, by default the GKE Multi-Cloud API adds your user account as an administrator and creates appropriate RBAC policies that grant you full administrative access to the cluster. To configure different users, pass the [`--admin-users`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--admin-users) flag when you create or update a cluster. When you use the `--admin-users` flag, you must include all users that can administer the cluster. The gcloud CLI doesn't include the user that creates the cluster.

You can also add admin users using the Google Cloud console. For more information, see [Update your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-cluster#update_your_cluster).

**Note:** When you add admin users, the GKE Multi-Cloud API applies the Kubernetes RBAC policies to the cluster to grant the users the same administrative access that you were granted when you created the cluster. These policies grant users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces.

To see the configuration of your cluster's access, run the following command:
    
    
    kubectl describe clusterrolebinding gke-multicloud-cluster-admin
    

In addition to the RBAC policies to access the Kubernetes API server, if an admin user isn't a project owner, you need to grant specific IAM roles that let the admin users authenticate using their Google identity. For more information about how to connect to the cluster, see [Connect and authenticate to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster).

## What's next

  * To set up OIDC, see [Manage identity with GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/anthos-identity-service).
  * [Connect and authenticate to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
