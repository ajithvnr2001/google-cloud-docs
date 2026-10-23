---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/connect-and-authenticate-to-your-cluster/
title: Connect and authenticate to your cluster \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:03.668277+00:00
---

# Connect and authenticate to your cluster  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/connect-and-authenticate-to-your-cluster/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Connect and authenticate to your cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect and authenticate to GKE on AWS.

You have multiple options to authenticate to GKE clusters. All of the following options assume that the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway) or the user is able to connect to your cluster's control plane:

  * Google identity: The default authentication option provided by GKE on AWS without additional configuration.

  * Open ID Connect (OIDC) or AWS IAM: Supported by [GKE Identity Service](https://docs.cloud.google.com/anthos/identity)




## Google identity authentication

By default, the GKE Multi-Cloud API grants the user who creates the cluster the Kubernetes [role-based access control](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) (RBAC) policies that lets the user authenticate with the cluster using their Google identity. The user who created the cluster can add other users as [admin users](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/authentication#kubernetes_api_access_control) with full administrative access to the cluster.

In addition to the RBAC permissions policy that grants the `clusterrole/cluster-admin` role to admin users, the GKE Multi-Cloud API configures an [impersonation policy](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) that authorizes the [Connect agent](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent) to send requests to the Kubernetes API server on behalf of an admin user.

You can authenticate to your cluster with your Google identity in the following ways:

### Use kubectl with identity from the gcloud CLI

You can use the Google Cloud CLI to create a `kubeconfig` that uses the identity of the user authenticated with `gcloud auth login`. You can then use `kubectl` to access the cluster. 

For `kubectl` access when using the Connect gateway, if an admin user isn't a project owner, minimally, the user must be granted the following roles in the project:

  * `roles/gkehub.gatewayAdmin`: This role lets a user access the Connect gateway API to use `kubectl` to manage the cluster.

    * If a user only needs read-only access to connected clusters, you can grant `roles/gkehub.gatewayReader` instead.

    * If a user needs read / write access to connected clusters, you can grant `roles/gkehub.gatewayEditor`.

  * `roles/gkehub.viewer`: This role lets a user retrieve cluster `kubeconfigs`.




For details about the permissions included in these roles, see [GKE Hub roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) in the IAM documentation.

You can find out more about granting IAM permissions and roles in [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

After an admin user has the required roles, follow the steps in [Configure cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cluster-access-for-kubectl).

### Use Google Cloud console

Admin users who aren't project owners and want to interact with clusters using the console need the following roles at a minimum:

  * `roles/container.viewer`. This role lets users view the GKE Clusters page and other container resources in the Google Cloud console. For details about the permissions included in this role, see [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) in the IAM documentation.

  * `roles/gkehub.viewer`. This role lets users view clusters outside Google Cloud in the Google Cloud console. Note that this is one of the roles required for `kubectl` access. If you already granted this role to a user, you don't need to grant it again. For details about the permissions included in this role, see [GKE Hub roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) in the IAM documentation.




You can find out more about granting IAM permissions and roles in [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

For information on logging in to the cluster from the console, see [Log in using your Google Cloud identity](https://docs.cloud.google.com/anthos/fleet-management/docs/console#log_in_using_your_identity).

### Use Google Groups

To connect to your cluster as a member of a Google group, see [Connect Google groups to GKE on AWS](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/connect-google-groups).

## Authenticate with OIDC

For information on authenticating to your cluster with OIDC, see [Manage identity with GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/anthos-identity-service#oidc).

## Authenticate with AWS IAM

For information on authenticating to your cluster with AWS IAM, see [Manage identity with GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/anthos-identity-service#aws-iam). 

## Authenticate with external identities

For information on authenticating to your cluster with external identities, see [Authenticate with external identities](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/authenticate-external-ids).

## Connect to your cluster's control plane

All GKE on AWS are created in private subnets. All the underlying cluster infrastructure (for example, nodes and load balancer endpoints) is provisioned with private [RFC 1918](https://tools.ietf.org/html/rfc1918) IP addresses only.

To manage your cluster directly, you must be able to connect to the control plane load balancer of your cluster. If your cluster can't connect directly to your control plane but can make outbound connections, you can connect to the control plane through Connect gateway, a Google-hosted reverse proxy to your cluster. For more information, see [Connecting to registered clusters with the Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway). 

You can also connect through [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
