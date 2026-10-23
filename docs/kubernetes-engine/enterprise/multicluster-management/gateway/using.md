---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using/
title: Using the Connect gateway \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:54.065158+00:00
---

# Using the Connect gateway  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Using the Connect gateway Stay organized with collections  Save and categorize content based on your preferences. 

This page tells you how to use the Connect gateway to connect to a registered cluster. Before reading this page, ensure that you're familiar with the concepts in our [overview](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway). The guide assumes that your project administrator has already [set up](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup) the gateway, and given you the necessary roles and permissions.

## Before you begin

  * Ensure that you have the following command line tools installed:

    * The latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), the command line tool for interacting with Google Cloud.
    * [`kubectl`](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl)

If you are using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

  * Ensure that you have [initialized](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with your project.




### Required roles

To get the permissions that you need to use the connect gateway to connect to clusters and run commands, ask your administrator to grant you the following IAM roles on the cluster project: 

  * Get the kubeconfig file for the cluster: [Connect Gateway Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayReader) (`roles/gkehub.gatewayReader`) 
  * Run `kubectl` CLI commands: [Connect Gateway Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin) (`roles/gkehub.gatewayAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

The Connect Gateway Admin (`roles/gkehub.gatewayAdmin`) role is the only predefined role that contains the `gkehub.gateway.stream` permission, which is required to run `kubectl` CLI commands like `attach`, `exec`, `port-forward`, and `cp`. 

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Log in to your Google Cloud account

You can use your own Google Cloud account or a Google Cloud [service account](https://docs.cloud.google.com/iam/docs/service-accounts) to interact with connected clusters via Gateway API.

Follow the instructions in [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate) to log in to your user account. The Connect gateway supports [service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation), so even if you're logged in to your own user account you can use a service account to interact with clusters, as you'll see in the following sections.

## Select a registered cluster

If you don't know the name of the cluster you want to access, you can see all your current fleet's registered clusters by running the following command:
    
    
    gcloud container fleet memberships list
    

This lists all your fleet's clusters, including their **membership names** and external IDs. Each cluster in a fleet has a unique membership name. For GKE clusters, the membership name generally matches the name you gave it when you created the cluster, unless the cluster's name was not unique within its project at [registration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke).

## Get the cluster's gateway `kubeconfig`

Use the following command to get the `kubeconfig` you need to interact with your specified cluster:
    
    
    gcloud container fleet memberships get-credentials MEMBERSHIP_NAME
    

Replace `MEMBERSHIP_NAME` with your cluster's fleet membership name.

This command returns a special **Connect gateway-specific`kubeconfig`** that lets you connect to the cluster through the Connect gateway.

If you want to use a service account rather than your own Google Cloud account, use `gcloud config` to set `auth/impersonate_service_account` to the service account email address.

To fetch the cluster credential used to interact with the Connect gateway using a service account, run the following commands: Note the following:

  * Google Distributed Cloud (software only) clusters on bare metal and VMware: The membership name is the same as the cluster name.
  * GKE on AWS: Use `gcloud container aws clusters get-credentials`.

  * GKE on Azure: Use `gcloud container azure clusters get-credentials`.




You can find out more about letting users impersonate a service account in [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).
    
    
    gcloud config set auth/impersonate_service_account SA_EMAIL_ADDRESS
    gcloud container fleet memberships get-credentials MEMBERSHIP_NAME
    

Replace `SA_EMAIL_ADDRESS` with the email address of the service account. You can find out more about letting users impersonate a service account in [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

## Run commands against the cluster

Once you have the necessary credentials, you can run commands using `kubectl` or a `go-client` as you normally would for any Kubernetes cluster. Your output should look something like the following:
    
    
    # Get namespaces in the Cluster.
    kubectl get namespaces
    NAME              STATUS   AGE
    default           Active   59d
    gke-connect       Active   4d
    

### kubectl exec/cp/attach/port-forward commands

The following `kubectl` commands are streaming commands and have additional requirements:

  * `attach`
  * `cp`
  * `exec`
  * `port-forward`



To run these commands, you must meet the following requirements:

  * Clusters must be at version 1.30 or later for the `attach`, `cp`, and `exec` commands, and at version 1.31 or later for the `port-forward` command.

  * The `kubectl` client must be at version 1.31 or later. To check your client version, look at the output of the `kubectl version` command. To install a newer version of `kubectl`, see [Install tools](https://kubernetes.io/docs/tasks/tools/#kubectl).

  * Users and service accounts must have the following additional access to the Kubernetes API through IAM or RBAC:

    * **IAM** : grant a role that includes the `gkehub.gateway.stream` permission. The `roles/gkehub.gatewayAdmin` predefined role includes this permission. You can also assign this permission to a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#edit-role).
    * **RBAC** : grant a Role or ClusterRole that includes `get` access to the `pods/exec`, `pods/portforward`, and `pods/attach` API subresources, like in the following example Role and RoleBinding:
          
          apiVersion: rbac.authorization.k8s.io/v1
          kind: Role
          metadata:
            name: stream-role
            namespace: NAMESPACE # Specify the namespace
          rules:
          - apiGroups: ["*"]
            resources: ["pods/exec", "pods/attach", "pods/portforward"]
            verbs: ["get"]
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: RoleBinding
          metadata:
            name: stream-rolebinding
            namespace: NAMESPACE # Specify the namespace
          roleRef:
            apiGroup: "rbac.authorization.k8s.io"
            kind: Role
            name: stream-role
          subjects:
          - kind: Group
            name: EMAIL # Specify the group that should have stream access
          

Replace the following:

      * `NAMESPACE`: the namespace for the Role and RoleBinding.
      * `EMAIL`: the email address of the group that should have stream access, if the cluster supports [RBAC with groups](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups).

The `cluster-admin` default ClusterRole also includes these permissions.




## Troubleshooting

If you're having problems connecting to a cluster through the gateway, you or your administrator can check for the following common issues.

  * **The server doesn't have a resource type** : You may see this error message when the command `kubectl get ns` fails. There are multiple potential reasons for this error. Run your `kubectl` commands in verbose mode to see more details, for example `kubectl get ns -v 10`.
  * **Cannot find active connections for cluster(project: 12345, membership: my-cluster)** : You may see this error when Connect Agent loses connectivity or isn't installed properly (clusters outside Google Cloud only). To resolve this issue, you need to verify if `gke-connect` namespace exists on the cluster. If the `gke-connect` namespace exists on the cluster, see the [Connect Troubleshooting page](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/troubleshooting) to fix the connectivity issues.
  * **The requested URL was not found on this server** : You may see this error when the `kubeconfig` contains an incorrect server address. Make sure the Google Cloud CLI version you're using is the [latest version](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using#before_you_begin) and retry to generate the gateway `kubeconfig`. Don't manually edit the `kubeconfig` file, which will cause unexpected errors.
  * **The user identity does not have sufficient permissions to use the gateway API** : You need the `roles/gkehub.gatewayAdmin` `roles/gkehub.gatewayReader` or `roles/gkehub.gatewayEditor` role to use the API. See [Grant IAM roles to users](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup#grant_iam_roles_to_users) in the gateway setup guide for more details.
  * **The Connect agent is not authorized to send the user’s requests** : The Connect agent needs to be allowed to forward requests on your behalf, which is specified using an impersonation policy on the cluster. See [Configure RBAC authorization](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup#configure_rbac_authorization) in the gateway setup guide for an example of adding a user to the `gateway-impersonate` role.
  * **The user identity does not have sufficient RBAC permissions to perform the operation** : You must have appropriate permissions on the cluster to run your chosen operations. See [Configure RBAC authorization](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup#configure_rbac_authorization) in the gateway setup guide for an example of adding a user to the appropriate `ClusterRole`.
  * **The user identity does not have sufficient permissions to perform the operation when using Google Groups or third-party support** : See [Collecting GKE Identity Service logs](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/troubleshooting#gke_id_service_logs) for instructions on how to inspect logs related to identity information.
  * **The Connect agent is unhealthy** : See the [Connect Troubleshooting page](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/troubleshooting) to make sure your cluster is connected.
  * **executable gke-gcloud-auth-plugin not found** or **no Auth Provider found for name gcp** : kubectl versions 1.26 and later may display this error due to [changes to kubectl authentication](https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke) starting with GKE v1.26. Install `gke-gcloud-auth-plugin` and re-run `gcloud container fleet memberships get-credentials MEMBERSHIP_NAME` with the latest version of Google Cloud CLI.
  * **Connections to the gateway fail with older versions of the Google Cloud CLI** : For GKE clusters, the Connect agent is no longer required for the gateway to function so it does not get installed by default during membership registration. Earlier versions of the Google Cloud CLI (399.0.0 and below) assume the existence of the Connect agent on the cluster. Attempting to use the gateway with these earlier versions may fail on clusters registered with a newer version of the Google Cloud CLI. To resolve this, either upgrade your Google Cloud CLI client to a newer version or re-run the membership registration command with the `--install-connect-agent` flag.
  * **The size of groups returned under the`gke-security-groups` group exceeds the 8 KB HTTP header size limit. Reorganize the group hierarchy and try again**: Though there is no hard limit on the number of groups, long group names can cause the request to exceed the 8 KB HTTP header size limit and result in errors that might require you to restructure the group hierarchy.



### kubectl exec/cp/attach/port-forward troubleshooting

**Note:** `kubectl` versions that are earlier than 1.32 don't log sufficient information for debugging. We recommend that you upgrade your `kubectl` client to version 1.32 or later.

The error returned from running the command is often a generic `400 Bad Request` error which is not clear enough to debug the issue. To return more detailed error messages, use the `kubectl` client version 1.32 or later to run the command with a verbosity of level 4 or higher, for example: `kubectl exec -v 4 ...`.

In the returned logs, search for the log that contains the following responses:

  * **For the`kubectl exec/cp/attach` command**: `RemoteCommand fallback:`
  * **For the`kubectl port-forward` command**: `fallback to secondary dialer from primary dialer err:`



For troubleshooting some of the common error messages that you might receive from the `kubectl exec -v 4 ...` command, see the following section.

#### Missing IAM permissions

If the error message contains `generic::permission_denied: Permission'gkehub.gateway.stream' denied on resource`, this could indicate that you haven't been granted the required IAM permissions to run the command. This feature requires users to have the `gkehub.gateway.stream` IAM permission, which is included by default in the `roles/gkehub.gatewayAdmin` role. See the [IAM permission section](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using#grant_an_additional_permission_if_needed) for instructions.

#### Missing required RBAC permissions

If the error message contains `...generic::failed_precondition: failed to connect to the cluster's API Server with response (status=403 Forbidden...`, it indicates that you're missing RBAC permissions. You need a set of RBAC permissions in the cluster to run these `kubectl` commands. For more information about setting up the required RBAC permissions, see [Create and apply additional RBAC policies if needed](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using#create_and_apply_additional_rbac_policies_if_needed).

#### Error message generic::resource_exhausted: Gateway's active_streams quota exhausted

There is a quota limit of 10 active streams per fleet host project. This is defined under the `connectgateway.googleapis.com/active_streams` quota. See [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage) for instructions on managing your quotas.

#### Error message generic::failed_precondition: error encountered within the cluster

If you get the error `generic::failed_precondition: error encountered within the cluster`, check the Connect Agent logs in the cluster to identify the underlying cause:
    
    
    kubectl logs -n gke-connect -l app=gke-connect-agent --tail -1
    

The log to look for in the Connect Agent is `failed to create the websocket connection...`.

#### Error message generic::failed_precondition: connection to Agent failed/terminated

If you encounter this error immediately when running the command, there is an issue with the cluster's connection to Google. See the general [troubleshooting guide](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using#troubleshooting) for more information.

If you encounter this error after the session is active for about 20 to 30 minutes, it is an expected limitation due to security reasons. The connection needs to be re-established.

### `kubectl --raw` troubleshooting

Using a shortened endpoint (such as `kubectl get --raw /version`) might result in the following error: `Error from server (NotFound): the server could not find the requested resource`. You must provide the full server address.

Fetch the endpoint from your `kubeconfig`:
    
    
    # e.g. https://connectgateway.googleapis.com/v1/projects/1234567/locations/global/gkeMemberships/my-membership
    FULL_GATEWAY_ENDPOINT=$(kubectl config view --minify -o jsonpath='{.clusters[*].cluster.server}')
    echo $FULL_GATEWAY_ENDPOINT
    

Then use the endpoint for your command, for example, with `/version`:
    
    
    kubectl get --raw $FULL_GATEWAY_ENDPOINT/version
    

## What's next?

  * See an example of how to use the Connect gateway as part of your DevOps automation in our [Integrating with Cloud Build](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/tutorials/cloud-build-integration) tutorial.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
