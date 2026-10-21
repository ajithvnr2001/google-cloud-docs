---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup/
title: Set up the Connect gateway \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:14.223601+00:00
---

# Set up the Connect gateway  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Set up the Connect gateway Stay organized with collections  Save and categorize content based on your preferences. 

This guide is for platform administrators who need to set up the Connect gateway for use by their project's users and service accounts. This setup lets users:

  * Use the Google Cloud console to log in to registered clusters outside Google Cloud with their Google Cloud identity.

  * Use `kubectl` to access clusters through the Connect gateway.




This setup only allows for authentication of users and services based on their individual IDs, not their membership of Google Groups. To set up additional group support, see [Set up the Connect gateway with Google Groups](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups).

If you are unfamiliar with the Connect gateway, see our [overview](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway) for an explanation of the basic concepts and how it works.

## Before you begin

  1. Ensure that you have the following command line tools installed:

     * The latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), the command line tool for interacting with Google Cloud.
     * `kubectl` for running commands against Kubernetes clusters. If you need to install `kubectl`, follow these [instructions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl)

If you are using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

  2. Either [initialize](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with your project, or run the following commands to authorize the gcloud CLI and set your project as the default:
         
         gcloud auth login
         gcloud config set project PROJECT_ID
         




## Required IAM roles for the setup

This guide assumes that you have the `roles/owner` permission in your project. If you aren't a project owner, ask a project owner to grant you additional permissions on the project so that you can do the following tasks:

  * To enable APIs, you need the `serviceusage.services.enable` permission, which is included in the [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage) role (`roles/serviceusage.serviceUsageAdmin`). A project owner can either create a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with the `serviceusage.services.enable` permission enabled, or grant you `roles/serviceusage.serviceUsageAdmin`, as follows:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
           --member user:USER_EMAIL_ADDRESS \
           --role='roles/serviceusage.serviceUsageAdmin'
        

  * To grant IAM permissions to users and service accounts so that they can use the Connect gateway, you need the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager) role (`roles/resourcemanager.projectIamAdmin`), which a project owner can grant with the following command:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
           --member user:USER_EMAIL_ADDRESS \
           --role='roles/resourcemanager.projectIamAdmin'
        




## Enable APIs

To add the gateway to your project, enable the Connect gateway API and its required dependency APIs. If your users only want to authenticate to clusters using the Google Cloud console you don't need to enable `connectgateway.googleapis.com`, but you do need to enable the other APIs.
    
    
    gcloud services enable --project=PROJECT_ID  \
        connectgateway.googleapis.com \
        gkeconnect.googleapis.com \
        gkehub.googleapis.com \
        cloudresourcemanager.googleapis.com
    

## Verify registered clusters

Only clusters registered to your project fleet can be accessed through the Connect gateway. GKE clusters on premises and on other public clouds are automatically registered when they are created. However, GKE clusters on Google Cloud and [attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached) must be registered separately. If you need to register a cluster, follow the instructions in our [cluster registration guides](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation). Note that GKE clusters must be [registered to the fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke) to use the gateway.

To verify that clusters have been registered, run the following command:
    
    
    gcloud container fleet memberships list
    

You should see a list of all your registered clusters, as in this example output:
    
    
    NAME         EXTERNAL_ID
    cluster-1    0192893d-ee0d-11e9-9c03-42010a8001c1
    cluster-2    f0e2ea35-ee0c-11e9-be79-42010a8400c2
    

## Grant IAM roles to users

Access to clusters is controlled by Identity and Access Management (IAM). The required IAM roles to access clusters using `kubectl` differ slightly from the roles to access clusters in the Google Cloud console, as explained in the following sections.

### Grant roles for access through `kubectl`

Minimally, users and [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) need the following IAM roles to use `kubectl` to interact with clusters through the Connect gateway, unless the user has `roles/owner` in the project:

  * `roles/gkehub.gatewayAdmin`: This role lets a user access the Connect gateway API to use `kubectl` to manage the cluster. This role includes the `gkehub.gateway.stream` permission, which lets users run the the `attach`, `cp`, and `exec` `kubectl` commands. For additional requirements to run those commands, see [Preview support for the commands](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using#kubectl_execcpattachport-forward_commands).

    * If a user only needs read-only access to connected clusters, you can grant `roles/gkehub.gatewayReader` instead.

    * If a user needs read / write access to connected clusters, you can grant `roles/gkehub.gatewayEditor`.

  * `roles/gkehub.viewer`: This role lets a user retrieve cluster `kubeconfigs`.




For details about the permissions included in these roles, see [GKE Hub roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) in the IAM documentation.

You can use the following commands to grant these roles:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=MEMBER \
        --role=GATEWAY_ROLE
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=MEMBER \
        --role=roles/gkehub.viewer
    

where:

  * `MEMBER` is the user or service account, which is in the format `user|serviceAccount:emailID`, for example:

    * `user:alice@example.com`
    * `serviceAccount:test_sa@example-project.iam.gserviceaccount.com`
  * `GATEWAY_ROLE` is either `roles/gkehub.gatewayAdmin`, `roles/gkehub.gatewayReader` or `roles/gkehub.gatewayEditor`.




You can find out more about granting IAM permissions and roles in [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Grant roles for access through the Google Cloud console

Users who want to interact with clusters outside of Google Cloud using the Google Cloud console need the following IAM roles at minimum to view clusters:

  * `roles/container.viewer`. This role lets users view the GKE Clusters page and other container resources in the Google Cloud console. For details about the permissions included in this role, see [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) in the IAM documentation.

  * `roles/gkehub.viewer`. This role lets users view clusters outside Google Cloud in the Google Cloud console. Note that this is one of the roles required for `kubectl` access. If you already granted this role to a user, you don't need to grant it again. For details about the permissions included in this role, see [GKE Hub roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) in the IAM documentation.

In the following commands, replace `PROJECT_ID` with the project ID of the fleet host project. Also, replace `MEMBER` with the user's email address or service account using the format `user|serviceAccount:emailID`, for example:

    * `user:alice@example.com`
    * `serviceAccount:test_sa@example-project.iam.gserviceaccount.com`
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=MEMBER \
        --role=roles/container.viewer
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=MEMBER \
        --role=roles/gkehub.viewer
    




For more information about granting IAM roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation.

## Configure RBAC authorization

Each cluster's Kubernetes API server needs to be able to authorize requests that come from the Google Cloud console or from `kubectl` commands that come through the Connect gateway from your specified users and service accounts. To ensure this, you need to update the role-based access control (RBAC) policies on each cluster that you want to make accessible through the gateway. You need to add or update the following policies:

  * An [**impersonation policy**](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) that authorizes the [Connect agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent) to send requests to the Kubernetes API server on behalf of a user.
  * A **permissions policy** that specifies which permissions the user has on the cluster. This can be a cluster-level role like `clusterrole/cluster-admin` or `clusterrole/cloud-console-reader`, or a namespace-level role such as `role/default/pod-reader`.



### (Optional) Create a `cloud-console-reader` role

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
    

You can then grant this role to users when setting up your permission policies, as described in the next section.

### Create and apply required RBAC policies

The following shows how to create and apply the required RBAC policies. The simplest way to do this is to use the gcloud CLI to generate and apply the appropriate policies for you. Alternatively, if you prefer, you can create an RBAC policy file and apply it with `kubectl`.

### gcloud

To generate and apply the policies to your chosen cluster with the gcloud CLI, run the following command:
    
    
    gcloud container fleet memberships generate-gateway-rbac  \
        --membership=MEMBERSHIP_NAME \
        --role=ROLE \
        --users=USERS \
        --project=PROJECT_ID \
        --kubeconfig=KUBECONFIG_PATH \
        --context=KUBECONFIG_CONTEXT \
        --apply
    

Replace the following:

  * MEMBERSHIP_NAME: the name used to uniquely represent the cluster in its fleet. You can find out how to check your cluster's membership name in [Get fleet membership status](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/get-fleet-status#gcloud).
  * ROLE: the Kubernetes role you want to grant to the users on the cluster, for example, `clusterrole/cluster-admin`, `clusterrole/cloud-console-reader`, or `role/mynamespace/namespace-reader`. This role must already exist before you run the command.
  * USERS: the email addresses of the users (user accounts or service accounts) to whom you want to grant the permissions, as a comma-separated list. For example: `--users=dana@example.com,test-acct@test-project.iam.gserviceaccount.com`.
  * PROJECT_ID: the project ID where the cluster is registered.
  * KUBECONFIG_PATH: the local filepath where your kubeconfig containing an entry for the cluster is stored. In most cases it's `$HOME/.kube/config`.
  * KUBECONFIG_CONTEXT: the context of the cluster as it appears in the kubeconfig file. You can get the current context from the command line by running `kubectl config current-context`. Whether you use the current context or not, make sure that it works for accessing the cluster by running the following command:
        
        kubectl get namespaces \
          --kubeconfig=KUBECONFIG_PATH \
          --context=KUBECONFIG_CONTEXT




After running `gcloud container fleet memberships generate-gateway-rbac`, you see something like the following at the end of the output, which is truncated for readability
    
    
    Validating input arguments.
    Specified Cluster Role is: clusterrole/cluster-admin
    Generated RBAC policy is:
    --------------------------------------------
    ...
    ---
    Applying the generate RBAC policy to cluster with kubeconfig: artifacts/kubeconfig, context: example-cluster-admin@example-cluster
    Writing RBAC policy for user: 222larabrown@gmail.com to cluster.
    Successfully applied the RBAC policy to cluster.
    

This is the context for accessing the cluster through the Connect gateway.

For more details on the `generate-gateway-rbac` command, see the [gcloud CLI reference guide](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/memberships/generate-gateway-rbac).

### kubectl

The following example shows how to create appropriate policies for a user (`dana@example.com`) and a service account (`test@example-project.iam.gserviceaccount.com`), giving them both `cluster-admin` permissions on the cluster and saving the policy file as `/tmp/gateway-rbac.yaml`. The policies are then applied to the cluster associated with the current context:
    
    
    cat <<EOF > /tmp/gateway-rbac.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: gateway-impersonate
    rules:
    - apiGroups:
      - ""
      resourceNames:
      - dana@example.com
      - test@example-project.iam.gserviceaccount.com
      resources:
      - users
      verbs:
      - impersonate
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: gateway-impersonate
    roleRef:
      kind: ClusterRole
      name: gateway-impersonate
      apiGroup: rbac.authorization.k8s.io
    subjects:
    - kind: ServiceAccount
      name: connect-agent-sa
      namespace: gke-connect
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: gateway-cluster-admin
    subjects:
    - kind: User
      name: dana@example.com
    - kind: User
      name: test@example-project.iam.gserviceaccount.com
    roleRef:
      kind: ClusterRole
      name: cluster-admin
      apiGroup: rbac.authorization.k8s.io
    EOF
    # Apply policies to the cluster.
    kubectl apply --kubeconfig=KUBECONFIG_PATH  -f /tmp/gateway-rbac.yaml
    

You can find out more about specifying RBAC permissions in [Using RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

**Note:** While our examples show applying policy updates directly with `kubectl`, for real-life use we strongly recommend using [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) to create and manage policies with [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview) to sync those policies and other configurations across your clusters. If you want to use Policy Controller while using `generate-gateway-rbac` to generate the policies, you can run the command in ["dry run" mode](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/memberships/generate-gateway-rbac) to output the policies rather than applying them. You can then use Config Sync to sync the generated policies to all your clusters.

## VPC Service Controls support

VPC Service Controls provides an additional layer of security defense for Google Cloud services that is independent of Identity and Access Management (IAM). While IAM enables granular _identity-based access control_ , VPC Service Controls enables broader _context-based perimeter security_ , including controlling data egress across the perimeter—for example, you can specify that only certain projects can access your BigQuery data. You can find more about how VPC Service Controls works to protect your data in the VPC Service Controls [Overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

You can use VPC Service Controls with the Connect gateway for extra data security, once you ensure that the necessary APIs to use the gateway can be accessed from within your specified service perimeter.

## What's next?

  * Learn how to [use the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using) to connect to clusters from the command line.
  * See an example of how to use the Connect gateway as part of your DevOps automation in our [Integrating with Cloud Build](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/tutorials/cloud-build-integration) tutorial.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
