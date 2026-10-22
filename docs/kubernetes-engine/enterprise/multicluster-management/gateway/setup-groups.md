---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups/
title: Set up the Connect gateway with Google Groups \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:39.337804+00:00
---

# Set up the Connect gateway with Google Groups  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Set up the Connect gateway with Google Groups Stay organized with collections  Save and categorize content based on your preferences. 

This guide is for platform administrators who need to set up the connect gateway for use by their project's user accounts, using Google Groups for authorization. Before reading this page, ensure that you're familiar with the concepts in our [overview](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway). To authorize individual accounts, see the [default setup](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup).

This setup lets users log in to configured fleet clusters using the Google Cloud CLI, the connect gateway, and the Google Cloud console.

This feature uses Google Groups associated with [Google Workspace](https://workspace.google.com/) or any edition of [Cloud Identity](https://docs.cloud.google.com/identity/docs/overview).

## Supported cluster types

You can set up access control with Google Groups through the connect gateway for the following cluster types:

  * GKE on Google Cloud: all available versions. To set up the connect gateway, [configure Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac), and then grant IAM roles to Google Groups.
  * Google Distributed Cloud (software only) on VMware and bare metal: all available versions.
  * Google Distributed Cloud connected: all available versions.
  * GKE attached clusters: version 1.28.0-gke.2 and later.
  * GKE on AWS and GKE on Azure: all available versions.

**Caution:** GKE on AWS and GKE on Azure are deprecated. For more information, see [GKE on AWS deprecation announcement](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and [GKE on Azure deprecation announcement](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement).



To use this feature with environments that aren't in the preceding list, contact [Cloud Customer Care](https://docs.cloud.google.com/support/docs/customer-care-procedures) or [the connect gateway team](mailto:connect-gateway-feedback@google.com).

## How it works

As described in the [overview](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway), it's often useful to be able to give users access to clusters on the basis of their membership of _Google Groups_ , that is, groups created in Google Workspace. Authorizing based on group membership means you don't have to set up separate authorization for each account, making policies simpler to manage and easier to audit. So, for example, you can easily share cluster access to a team, removing the need to manually add/remove individual users from clusters when they join or leave the team. You can configure the connect gateway to get Google Groups membership information for each user that logs into the cluster. You can then use this information in your access control policies.

**Note:** Service accounts (accounts ending in `gserviceaccount.com`) are not supported in the Google Groups functionality.

The following shows the typical flow for a user authenticating to and running commands against a cluster with this service enabled. For this flow to be successful, an RBAC policy must exist on the cluster for a group that:

  1. Contains the user `alice@example.com` as a member.

  2. Is a nested group of `gke-security-groups@example.com`.




![Diagram showing the gateway Google Groups flow](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/docs/images/connect-gateway-groups-flow.svg)

  1. The user `alice@example.com` logs in using their Google identity and, if they plan to use the cluster from the command line, gets the cluster's gateway `kubeconfig` as described in [Using the connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using).
  2. The user sends a request by running a `kubectl` command or opening the Google Kubernetes Engine **Workloads** or **Object Browser** pages in the Google Cloud console.
  3. The request is received by the Connect service, which performs an authorization check with [IAM](https://docs.cloud.google.com/iam/docs/overview).
  4. The Connect service forwards the request to the Connect Agent running on the cluster. The request is accompanied with the user's credential information for use in authentication and authorization on the cluster.
  5. The Connect Agent forwards the request to the Kubernetes API server.
  6. The Kubernetes API server forwards the request to the `anthos-identity-service` Pod in the cluster, which validates the request.
  7. The `anthos-identity-service` Pod returns the user and group information to the Kubernetes API server. The Kubernetes API server can then use this information to authorize the request based on the cluster's configured RBAC policies.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. Verify that you have the permissions required to complete this guide. 

  6. Enable the Connect Gateway, GKE Connect, GKE Hub, Anthos Identity Service, and Cloud Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable connectgateway.googleapis.com gkeconnect.googleapis.com gkehub.googleapis.com anthosidentityservice.googleapis.com cloudresourcemanager.googleapis.com

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. Verify that you have the permissions required to complete this guide. 

  11. Enable the Connect Gateway, GKE Connect, GKE Hub, Anthos Identity Service, and Cloud Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable connectgateway.googleapis.com gkeconnect.googleapis.com gkehub.googleapis.com anthosidentityservice.googleapis.com cloudresourcemanager.googleapis.com

  12. For clusters outside of Google Cloud, the authentication components in your cluster must call the Cloud Identity API. Check whether you have network policies that require egress traffic from your cluster to go through a proxy.



### Required roles

To get the permissions that you need to configure the connect gateway and your clusters, ask your administrator to grant you the [Editor ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set up users and groups

Ensure that the groups that you want to use with this feature are set up as follows:

  1. Ensure there is a group in your organization's Google Workspace with the format `gke-security-groups@YOUR-DOMAIN`. If you don't have such a group, follow the instructions in [Create a group in your organization](https://support.google.com/a/answer/9400082) to create the group using the Google Admin console.
  2. Follow the instructions in [Add a group to another group](https://support.google.com/a/answer/167100) to add the groups you want to use for access control as nested groups of `gke-security-groups`. Do not add individual users as members of `gke-security-groups`.



User accounts that you want to use with this feature should use the same domain name as that of their group.

**Note:** The number of groups that are returned for a user under the `gke-security-groups` group is limited by the 8 KB HTTP header size limit. Though there is no hard limit on the number of groups, long group names can cause the request to exceed this limit and result in errors that might require you to restructure the group hierarchy.

## Configure support for groups

The connect gateway uses authentication components in your cluster to retrieve group membership information. To enable the required components, see one of the following documents depending on your cluster type:

  * **GKE on Google Cloud** : [configure Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac), and then skip to the Grant IAM roles to groups section.
  * **GKE attached clusters** : 
    * [Connect to your EKS attached cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/connect-to-cluster)
    * [Connect to your AKS attached cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/connect-to-cluster)
    * [Connect to your other cluster types](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/connect-to-cluster)
  * **Google Distributed Cloud** : enable support for groups by updating the ClientConfig custom resource in your cluster. Distributed Cloud automatically creates a ClientConfig named `default` in the `kube-public` namespace in every cluster. To verify that this custom resource exists, run the following command:
        
        kubectl --kubeconfig CLUSTER_KUBECONFIG get ClientConfig default -n kube-public
        

Replace `CLUSTER_KUBECONFIG` with the path to the cluster's kubeconfig.




The following sections show you how to update the ClientConfig custom resource to enable group support. These sections apply only to Google Distributed Cloud clusters. For other types of clusters, such as GKE on Google Cloud; GKE on AWS; and GKE on Azure, skip to the Grant IAM roles to groups section.

For Distributed Cloud, you can configure support for groups for individual clusters or for a fleet. The type of cluster that you use determines how you configure groups support, as follows:

  * **Distributed Cloud connected** : individual clusters only. Fleet-level configuration isn't supported.
  * **Google Distributed Cloud (software only) on VMware and bare metal** : individual clusters or fleets.



### Configure group support by using the GKE Fleet API

For Google Distributed Cloud (software only) on VMware and bare metal, you can configure group support at the fleet level. If you previously configured fleet-level authentication, such as for a different identity provider, group authentication is already enabled. However, if your network policy requires egress traffic to pass through a proxy, you must update the existing configuration with information about that proxy.

To configure group support at the fleet level, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **GKE Identity Service** page.

[Go to GKE Identity Service](https://console.cloud.google.com/kubernetes/identityservice)

  2. Click **Enable Identity Service**.

  3. Select the Google Distributed Cloud (software only) on VMware and bare metal clusters that you want to configure.

  4. Click **Update configuration**. The **Edit Identity Service Clusters Config** pane opens.

  5. In the **Configure Identity Providers** section, you can choose to retain, add, update, or remove an identity provider.

  6. Click **Continue** to go to the next configuration step. If you've selected at least one eligible cluster for this setup, the **Google Authentication** section is displayed.

  7. Select **Enable** to enable Google authentication for the selected clusters. If you need to access the Google identity provider through a proxy, enter the **Proxy** details.

  8. Click **Update Configuration**. This applies the identity configuration on your selected clusters.




### gcloud

  1. Enable the fleet-level identity service feature and configure the clusters, as described in [Set up fleet-level authentication management](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster).
  2. In the `auth-config.yaml` file that contains your ClientConfig specification, add the following field:
         
         spec:
           authentication:
           **- name: google-authentication-method
             google:
               disable: false**
         

The value of `false` in the `google.disable` field enables group support. To disable group support, modify this value to `true`.

  3. Optional: If you need to access the Google identity provider through a proxy, add the `proxy` field to the preceding configuration:
         
         spec:
           authentication:
           - name: google-authentication-method
             google:
               disable: false
             proxy: PROXY_URL
         

Replace `PROXY_URL` with the proxy server address to connect to the Google identity. For example: `http://user:password@10.10.10.10:8888`

  4. Apply the configuration to a cluster in your fleet:
         
         gcloud container fleet identity-service apply \
         --membership=CLUSTER_NAME \
         --config=/path/to/auth-config.yaml

Replace `CLUSTER_NAME` with your cluster's unique membership name within the fleet.




After you set up group support at the fleet level, the fleet controller manages the configuration. The fleet-level configuration overwrites any local changes that you make to the configuration in a specific cluster.

### Configure group support for individual clusters

For all Distributed Cloud clusters, including Distributed Cloud connected, enable group support by updating the `default` ClientConfig in each cluster:

  1. Get your cluster's membership details:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get memberships membership -o yaml
         

Replace `USER_CLUSTER_KUBECONFIG` with the path to the kubeconfig file for the cluster. If there are multiple contexts in the kubeconfig, the current context is used. You might need to reset the current context to the correct cluster before running the command.

In the response, refer to the `spec.owner.id` field to retrieve the cluster's membership details. The membership identifier has the format `//gkehub.googleapis.com/projects/PROJECT_NUMBER/locations/global/memberships/MEMBERSHIP`.

The output is similar to the following:
         
         id: //gkehub.googleapis.com/projects/123456789/locations/global/memberships/xy-ab12cd34ef
         

  2. Open the `default` ClientConfig in your cluster for editing:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG -n kube-public edit clientconfig default
         

  3. To enable group support, add the `google` field to the `spec.authentication` field:
         
         spec:
           internalServer: https://kubernetes.default.svc
           authentication:
           - google:
               audiences:
               - "CLUSTER_IDENTIFIER"
             name: google-authentication-method
         

Replace `CLUSTER_IDENTIFIER` with the membership details of your cluster.

Ensure that the `internalServer` field has a value of `https://kubernetes.default.svc`.

  4. Optional: If you need to access the Google identity provider through a proxy, add the `proxy` field to the preceding configuration:
         
         spec:
           internalServer: https://kubernetes.default.svc
           authentication:
           - google:
               audiences:
               - "CLUSTER_IDENTIFIER"
             name: google-authentication-method
             proxy: PROXY_URL
         

Replace `PROXY_URL` with the proxy server address to connect to the Google identity. For example: `http://user:password@10.10.10.10:8888`




## Grant IAM roles to Google Groups

**Note:** When managing access for users in [external identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), replace instances of Google Account principal identifiers—like `user:kiran@example.com`, `group:support@example.com`, and `domain:example.com`—with appropriate [Workforce Identity Federation principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). 

Groups need the following additional Google Cloud roles to interact with connected clusters through the gateway:

  * `roles/gkehub.gatewayAdmin`. This role allows group members to access the connect gateway API. 
    * If group members only need read-only access to connected clusters, `roles/gkehub.gatewayReader` can be used instead.
    * If group members need read/write access to connected clusters, `roles/gkehub.gatewayEditor` can be used instead.
  * `roles/gkehub.viewer`. This role allows group members to view registered cluster memberships.



You grant these roles using the `gcloud projects add-iam-policy-binding` command, as follows:
    
    
    gcloud projects add-iam-policy-binding --member=group:GROUP_NAME@DOMAIN --role=GATEWAY_ROLE PROJECT_ID
    gcloud projects add-iam-policy-binding --member=group:GROUP_NAME@DOMAIN --role=roles/gkehub.viewer PROJECT_ID
    

where

  * GROUP_NAME is the Google Group you want to grant the role
  * DOMAIN is your Google Workspace domain
  * GROUP_NAME@DOMAIN is a nested group under gke-security-groups@DOMAIN
  * GATEWAY_ROLE is one of `roles/gkehub.gatewayAdmin`, `roles/gkehub.gatewayReader` or `gkehub.gatewayEditor`.
  * PROJECT_ID is your project



You can find out more about granting IAM permissions and roles in [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure role-based access control (RBAC) policies

Finally, each cluster's Kubernetes API server needs to be able to authorize `kubectl` commands that come through the gateway from your specified groups. For each cluster, you need to add an RBAC **permissions policy** that specifies which permissions the group has on the cluster.

In the following example, you'll see how to grant members of the `cluster-admin-team` group `cluster-admin` permissions on the cluster, save the policy file as /tmp/admin-permission.yaml and apply it to the cluster associated with the current context. Be sure to also include the `cluster-admin-team` group under the `gke-security-groups` group.
    
    
    cat <<EOF > /tmp/admin-permission.yaml
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
    EOF
    # Apply permission policy to the cluster.
    kubectl apply --kubeconfig=KUBECONFIG_PATH -f /tmp/admin-permission.yaml
    

You can find out more about specifying RBAC permissions in [Using RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

**Note:** While our examples show applying policy updates directly with `kubectl`, for real-life use we strongly recommend using [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) to create and manage policies with [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview) to sync those policies and other configurations across your clusters.

## What's next?

  * Learn how to [use the connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using) to connect to clusters from the command line.
  * See an example of how to use the connect gateway as part of your DevOps automation in our [Integrating with Cloud Build](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/tutorials/cloud-build-integration) tutorial.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
