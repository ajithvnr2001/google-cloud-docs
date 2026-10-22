---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/bearer-token-auth/
title: Authenticate using a bearer token \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:02.005636+00:00
---

# Authenticate using a bearer token  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/bearer-token-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Authenticate using a bearer token Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to set up authentication by using a bearer token to log in to registered clusters outside of Google Cloud. After the setup, cluster administrators will be able to log on to clusters from the Google Cloud console. Many kinds of bearer tokens, as specified in [Kubernetes Authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#authentication-strategies), are supported. The easiest method is to create a Kubernetes service account (KSA) in the cluster, and [use its bearer token to log in](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console#log_in_using_a_bearer_token).

## Other authentication methods

As an alternative to setting up authentication using a bearer token, you can set up one of the following authentication methods depending on the needs of your organization:

  * [Google Identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console#set_up_google_cloud_identity), which lets users log in using their Google Cloud identity. Use this option if your users already have access to Google Cloud with a Google Identity.

  * If your cluster is configured to use an OIDC identity provider, you can use this to authenticate to the cluster from the Google Cloud console. You can find out how to set up OIDC for GKE clusters in the following guides:

    * [Configure clusters for GKE Identity Service with OIDC](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster). This guide shows you how to set up OIDC authentication on a cluster by cluster basis for all GKE cluster types.
    * [Set up GKE Identity Service for a fleet](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet). This option lets you set up OIDC at the fleet level for supported cluster types. Fleet-level setup is supported for GKE clusters on Google Cloud and all GKE clusters types.



If these Google-provided authentication methods aren't suitable for your organization, follow the instructions on this page to set up authentication using a bearer token.

## Grant IAM roles for access through the Google Cloud console

Users who want to view connected clusters [using the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console) need the following IAM roles at minimum:

  * `roles/container.viewer`. This role lets users view container resources in the Google Cloud console, including the GKE Clusters page.. For details about the permissions included in this role, see [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) in the IAM documentation.

  * `roles/gkehub.viewer`. This role lets users view the clusters outside Google Cloud in the Google Cloud console. Users don't need this role if your fleet doesn't include clusters outside Google Cloud. For details about the permissions included in this role, see [GKE Hub roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) in the IAM documentation.




Run the following commands to grant these roles:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='user:EMAIL_ADDRESS' \
        --role=roles/container.viewer
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='user:EMAIL_ADDRESS' \
        --role=roles/gkehub.viewer
    

Replace the following:

  * `PROJECT_ID`: the project ID of the fleet host project.

  * `EMAIL_ADDRESS`: the email address associated with the user's Google Cloud account.




For more information about granting IAM roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation.

## Configure role-based access control

Access to clusters is controlled using Kubernetes role-based access control (RBAC).

We recommend that you or a cluster administrator create a KSA for each user logging in to the cluster. Using a bearer token is like using a password, so each user should have their own account. Logging in with the KSA's bearer token causes all operations to be executed as the KSA, restricted by the RBAC roles held by the KSA.

The KSA needs to hold at least the following RBAC roles in the cluster to access it through the console:

  * [`view`](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles)
  * `cloud-console-reader`



### Create and apply the `cloud-console-reader` RBAC role

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
    

You can then grant this role to KSAs as described in the next section.

### Create and authorize a KSA

###  kubectl 

To create a KSA and bind permissions to it, follow these steps:

  1. Create the KSA and [`ClusterRoleBinding`](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding) resources to bind the `view` and `cloud-console-reader` Kubernetes RBAC `ClusterRoles` to the KSA:
         
         KSA_NAME=KSA_NAME
         kubectl create serviceaccount ${KSA_NAME}
         kubectl create clusterrolebinding VIEW_BINDING_NAME \
            --clusterrole view --serviceaccount default:${KSA_NAME}
         kubectl create clusterrolebinding CLOUD_CONSOLE_READER_BINDING_NAME \
            --clusterrole cloud-console-reader --serviceaccount default:${KSA_NAME}
         

Replace the following:

     * `KSA_NAME`: the name that you choose for the KSA
     * `VIEW_BINDING_NAME`: the name that you choose for the `view` `ClusterRoleBinding` resource; you can name it anything you want, but you might find it easiest to name it after the KSA
     * `CLOUD_CONSOLE_READER_BINDING_NAME`: the name that you choose for the `cloud-console-reader` `ClusterRoleBinding` resource; you can also name this anything you want
  2. Depending on what access the service account should have, bind additional roles to the KSA. For options, see the Kubernetes [default roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings).

For example, if you want to deploy a Kubernetes application from Cloud Marketplace, bind the `cluster-admin` role to the KSA:
         
         kubectl create clusterrolebinding BINDING_NAME \
            --clusterrole cluster-admin --serviceaccount default:KSA_NAME
         

Replace `BINDING_NAME` with the name of the cluster role binding for the service account.




### Authorize other accounts

###  kubectl 

For every other user or service account gaining access to the cluster, create `ClusterRoleBinding` resources to bind the `view` and `cloud-console-reader` roles to their account:

  1. Bind the `view` and `cloud-console-reader` `ClusterRoles`:
         
         ACCOUNT_NAME=ACCOUNT_NAME
         kubectl create clusterrolebinding VIEW_BINDING_NAME \
            --clusterrole view --serviceaccount default:${ACCOUNT_NAME}
         kubectl create clusterrolebinding CLOUD_CONSOLE_READER_BINDING_NAME \
            --clusterrole cloud-console-reader --serviceaccount default:${ACCOUNT_NAME}
         

Replace the following:

     * `ACCOUNT_NAME`: the Kubernetes service account
     * `VIEW_BINDING_NAME`: the name that you choose for the `view` `ClusterRoleBinding` resource; you can name it anything you want, but you might find it easiest to name it after the user or service account
     * `CLOUD_CONSOLE_READER_BINDING_NAME`: the name that you choose for the `view` `ClusterRoleBinding` resource; you can also name this anything you want
  2. Bind additional roles, depending on what access the account should have. For options, see the Kubernetes [default roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings).

For example, to bind the `cluster-admin` role, run the following command:
         
         kubectl create clusterrolebinding BINDING_NAME \
            --clusterrole cluster-admin --serviceaccount default:ACCOUNT_NAME
         

Replace `BINDING_NAME` with the name of the cluster role binding for the service account.




## Get the KSA's bearer token

###  kubectl 

To acquire the KSA's bearer token, run the following command:
    
    
    SECRET_NAME=KSA_NAME-token
    
    kubectl apply -f - << __EOF__
    apiVersion: v1
    kind: Secret
    metadata:
      name: "${SECRET_NAME}"
      annotations:
        kubernetes.io/service-account.name: "${KSA_NAME}"
    type: kubernetes.io/service-account-token
    __EOF__
    
    until [[ $(kubectl get -o=jsonpath="{.data.token}" "secret/${SECRET_NAME}") ]]; do
      echo "waiting for token..." >&2;
      sleep 1;
    done
    
    kubectl get secret ${SECRET_NAME} -o jsonpath='{$.data.token}' | base64 --decode
    

Replace `KSA_NAME` with the name that you choose for the KSA.

From this command's output, copy the token and save it so that users can use the token to [log in to the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console#log_in_using_a_bearer_token).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
