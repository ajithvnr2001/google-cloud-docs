---
url: https://docs.cloud.google.com/build/docs/private-pools/access-private-gke-clusters-identity-service/
title: Access private Google Kubernetes Engine clusters from Cloud Build private pools using Identity Service for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:02.592954+00:00
---

# Access private Google Kubernetes Engine clusters from Cloud Build private pools using Identity Service for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/private-pools/access-private-gke-clusters-identity-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Access private Google Kubernetes Engine clusters from Cloud Build private pools using Identity Service for GKE Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Starting on July 1, 2026, Identity Service for GKE is deprecated and is unsupported in GKE version 1.37 and later. Use Workforce Identity Federation instead. For more information, see [Identity Service for GKE deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/identity-service).

This tutorial describes how to access the control plane of a [private Google Kubernetes Engine (GKE) cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#private_cp) using [Cloud Build private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview). This access lets you use Cloud Build to deploy applications and manage resources on a private GKE cluster. This tutorial is intended for platform administrators, cluster administrators, and developers. It assumes that you're familiar with GKE, Cloud Build, [OpenID Connect](https://openid.net/connect/), and the `gcloud` command-line tool.

Cloud Build private pools and [GKE cluster control planes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane) both run in Google-owned [Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs). These VPC networks are [peered](https://docs.cloud.google.com/vpc/docs/vpc-peering) to your own VPC network on Google Cloud. However, VPC Network Peering [doesn't support transitive peering](https://docs.cloud.google.com/vpc/docs/vpc-peering#restrictions), which can be a restriction when you use Cloud Build private pools. This tutorial presents a solution that uses [Identity Service for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc) to enable workers in a Cloud Build private pool to access the control plane of a private GKE cluster.

## Architecture overview

Identity Service for GKE is an authentication proxy for GKE cluster control planes. It proxies requests to the API server and validates [ID tokens](https://google.aip.dev/auth/4116) that are issued by [OpenID Connect (OIDC)](https://openid.net/connect/) identity providers. After the proxy successfully validates an ID token, the proxy adds [user impersonation HTTP headers](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) to the original request and forwards it to the API server. The proxy runs as a Kubernetes service account that has permissions to impersonate users and groups.

The Identity Service for GKE proxy runs as pods on cluster nodes. A Kubernetes service of type `LoadBalancer` exposes the proxy outside the cluster. If Identity Service for GKE is enabled on a private cluster, the installer adds an annotation to the Kubernetes service to provision an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing). The proxy can be accessed through the load balancer over a VPC Network Peering connection, such as from a Cloud Build private pool, because the proxy runs on cluster nodes in your VPC network.

You can configure Google as an OpenID Connect identity provider in Identity Service for GKE because Google's OAuth 2.0 authentication system [conforms to the OpenID Connect specification](https://developers.google.com/identity/protocols/oauth2/openid-connect). To obtain ID tokens for a Google service account, you can use the [`generateIdToken`](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateIdToken) method of the [Service Account Credentials API API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest). The ID tokens are issued and signed by Google.

Putting it all together, this solution enables access to the private GKE cluster control plane by using the Identity Service for GKE proxy. Builds that run on a Cloud Build private pool connect to the proxy over a VPC Network Peering connection. The build that's running on the Cloud Build private pool runs as a Google service account. This Google service account can obtain an ID token to authenticate to the proxy from the Service Account Credentials API.

The following diagram shows the architecture that's described in the preceding text:

![Access private GKE clusters using Identity Service for GKE](https://docs.cloud.google.com/static/build/images/access-private-gke-cluster-identity-service.png)

All the communication in this solution takes place over internal IP address space. The workers in the private pool do not need public internet connectivity.

Identity and Access Management (IAM) permissions that are granted to user accounts and Google service accounts do not apply when they authenticate using Identity Service for GKE. Instead, you use [Kubernetes role-based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) to manage cluster permissions for these accounts. 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Build, GKE, Identity-Aware Proxy (IAP), and Service Networking APIs APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudbuild.googleapis.com container.googleapis.com iap.googleapis.com servicenetworking.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Cloud Build, GKE, Identity-Aware Proxy (IAP), and Service Networking APIs APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudbuild.googleapis.com container.googleapis.com iap.googleapis.com servicenetworking.googleapis.com




## Create a private GKE cluster

  1. In Cloud Shell, create a GKE cluster that has no client access to the public endpoint of the control plane, and that has Identity Service for GKE installed:
         
         gcloud container clusters create CLUSTER  \
           --enable-identity-service \
           --enable-ip-alias \
           --enable-master-authorized-networks \
           --enable-private-endpoint \
           --enable-private-nodes \
           --master-ipv4-cidr CONTROL_PLANE_CIDR \
           --network NETWORK\
           --release-channel regular \
           --scopes cloud-platform \
           --subnetwork SUBNET \
           --tags NODE_TAGS \
           --workload-pool PROJECT_ID.svc.id.goog \
           --zone ZONE
         

Replace the following:

     * CLUSTER: the name of the cluster. For this tutorial, use `private-cluster`.
     * CONTROL_PLANE_CIDR: the IP address range of the control plane. It must have a `/28` prefix. For this tutorial, you can use `172.16.0.32/28`.
     * NETWORK: the VPC network that the control plane connects to. For this tutorial, use `default`.
     * SUBNET: the subnet that the GKE cluster control plane connects to. The subnet must belong to the VPC network that's specified by NETWORK. For this tutorial, use `default`.
     * NODE_TAGS: a comma-separated list of [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) to apply to the nodes. For this tutorial, use `private-cluster-node`.
     * PROJECT_ID: your Google Cloud project ID.
     * ZONE: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for the GKE cluster. For this tutorial, use `us-central1-f`.

Note the following about the command:

     * The `--enable-identity-service` flag enables Identity Service for GKE on the cluster. In your own environment, you can [enable Identity Service for GKE on an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc#enabling_on_an_existing_cluster).

     * The `--enable-private-endpoint` flag configures the control plane to be accessible only by using internal IP addresses.

     * The `--enable-private-nodes` flag configures the cluster nodes to have only internal IP addresses.

     * The `--enable-master-authorized-networks` and `--enable-private-nodes` flags allow access to the API server only from the private networks that are specified by the `--network` flag.

     * The optional `--workload-pool` flag enables [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity). It's not required for this tutorial.

  2. Add a firewall rule that allows the GKE cluster control plane to connect to the validating admission webhook for ClientConfig resources:
         
         gcloud compute firewall-rules create allow-control-plane-clientconfig-webhook \
           --allow tcp:15000 \
           --network NETWORK\
           --source-ranges CONTROL_PLANE_CIDR\
           --target-tags NODE_TAGS
         

ClientConfig is a Kubernetes custom resource type (CRD) that Identity Service for GKE uses to configure how to interact with identity providers.




## Register Identity Service for GKE as an OAuth 2.0 client application

In this section, you register Identity Service for GKE as a client application using Google's OAuth 2.0 authentication system.

  1. Open the **Credentials** page in the Google Cloud console.

[Open the Credentials page](https://console.cloud.google.com/apis/credentials)

  2. Click **Create Credentials**.

  3. Select **OAuth Client ID**.

If the consent screen hasn't already been configured for the Google Cloud project, click **Configure consent screen**. Follow the documentation on [configuring the consent screen](https://support.google.com/cloud/answer/6158849). For this tutorial, set the following values:

     * **User Type** can be either **Internal** or **External**. For this tutorial, you can select Internal.
     * The values for **App name** , **User support email** , and **Developer contact information** are required and can be of any value.
     * You do not need to add any scopes for this tutorial.

When you are done configuring the consent screen, click Back to dashboard, and then start again from step 1 of the current procedure.

  4. In the **Application type** list, select **Web application**.

  5. In the **Name** field, enter a name for the client ID. For this tutorial, use `Identity Service for GKE`.

  6. Click **Create**.

A dialog appears. Copy the value of **Your Client ID** ; you need it later in this procedure.

  7. Click **OK** to close the dialog box.

  8. In Cloud Shell, create a directory underneath your home directory called `cloud-build-private-pools-gke-tutorial` and then go to that directory:

mkdir -p ~/cloud-build-private-pools-gke-tutorial cd ~/cloud-build-private-pools-gke-tutorial

  9. In the new directory, create a YAML file called `client-config-patch.yaml` that has values that you need later to patch the Identity Service for GKE ClientConfig resource:
         
         cat << EOF > client-config-patch.yaml
         spec:
           authentication:
           - name: google-oidc
             oidc:
               clientID: CLIENT_ID
               cloudConsoleRedirectURI: https://console.cloud.google.com/kubernetes/oidc
               extraParams: prompt=consent,access_type=offline
               issuerURI: https://accounts.google.com
               kubectlRedirectURI: http://localhost:10000/callback
               scopes: email
               userClaim: email
               userPrefix: '-'
         EOF
         

Replace CLIENT_ID with the OAuth client ID from the earlier step.

Note the following about the patch:

     * ID tokens that are issued by Google's OAuth 2.0 authentication system contain a unique numeric identifier in the sub (subject) claim. Using this opaque identifier in role bindings makes it difficult to identify the subject of a role binding. This patch therefore configures Identity Service for GKE to use the email claim from the ID tokens to identify users instead of using the default sub claim.

     * The email scope is added so that the issued ID tokens include the email claim.

     * The `cloudConsoleRedirectURI`, `extraParams`, `kubectlRedirectURI`, and scopes fields are used when [developers authenticate to the cluster using Identity Service for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc#logging_in_and_authenticating_to_the_cluster). They are not used when Google service accounts authenticate to the cluster. The kubectlRedirectURI field is mandatory.

     * The `userPrefix` field is a prefix for users who authenticate using the configured identity provider. The value `'-'` means no prefix.

     * The `spec.authentication` field is an array. You can use multiple OpenID Connect identity providers with Identity Service for GKE. For instance, you can use Google as the identity provider to authenticate Google service accounts, and a different identity provider to authenticate developers.

For more information about the fields in this configuration, see [Use external identity providers to authenticate to GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc#configuring_on_a_cluster).




## Create a Google service account to configure Identity Service for GKE

  1. In Cloud Shell, create a Google service account:
         
         gcloud iam service-accounts create ISG_GSA \
           --display-name "Configure Identity Service for GKE"
         

Replace ISG_GSA with the name that you want to use for the Google service account. For this tutorial, use `identity-service-for-gke`.

You assign this Google service account to a Compute Engine VM instance in order to configure Identity Service for GKE and Kubernetes role-based access control on the cluster.

  2. Grant the [Kubernetes Engine Admin](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#predefined) role on the project to the Google service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member serviceAccount:ISG_GSA@PROJECT_ID.iam.gserviceaccount.com \
           --role roles/container.admin
         

This role provides the permissions that are required in order to do the following tasks in this tutorial:

     * Configure Identity Service for GKE settings on clusters in the project.
     * Create role bindings and cluster role bindings in the cluster.



## Configure Identity Service for GKE

To configure Identity Service for GKE, you must have access to the cluster control plane. In this tutorial, you create a Compute Engine VM instance to access the control plane.

You need SSH access to the VM instance. To enable authenticated and authorized SSH access from outside the VPC network to the VM instance, you use TCP forwarding with Identity-Aware Proxy (IAP). This feature enables SSH access without requiring the VM instance to have a public IP address.

  1. In Cloud Shell, create a firewall rule that allows SSH access using IAP TCP forwarding to any VM instances that have the `ssh-iap` network tag:
         
         gcloud compute firewall-rules create allow-ssh-ingress-from-iap \
           --allow tcp:22 \
           --description "Allow SSH tunneling using Identity-Aware Proxy" \
           --network NETWORK \
           --source-ranges 35.235.240.0/20 \
           --target-tags ssh-iap
         

The source range contains the IP addresses that IAP uses for TCP forwarding.

  2. Create a Compute Engine VM instance in the same VPC network as the GKE cluster:
         
         gcloud compute instances create VM \
           --metadata enable-oslogin=TRUE \
           --network NETWORK \
           --no-address \
           --scopes cloud-platform,userinfo-email \
           --service-account ISG_GSA@PROJECT_ID.iam.gserviceaccount.com \
           --subnet SUBNET  \
           --tags ssh-iap \
           --zone ZONE
         

Replace VM with the name you want to use for the VM instance. For this tutorial, use `identity-service-for-gke-configuration`.

Note the following about the command above:

     * The `--service-account` flag attaches the Google service account to the VM instance.

     * The `cloud-platform` scope is required in order to access the Service Account Credentials API.

     * The `userinfo-email` scope is [helpful when creating a VM instance for managing Kubernetes role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#forbidden_error_for_service_accounts_on_vm_instances). It is optional for this tutorial.

     * The `--no-address` flag means that the VM instance is created without an external IP address.

     * The optional `enable-oslogin` instance metadata value enables [OS Login](https://docs.cloud.google.com/compute/docs/oslogin) on the VM instance. OS Login enables management of SSH access to VM instances using IAM.

  3. Copy the ClientConfig patch file to the VM instance:
         
         gcloud compute scp client-config-patch.yaml VM:~ --tunnel-through-iap --zone ZONE
         

The `--tunnel-through-iap` flag instructs `gcloud` to tunnel the connection through IAP.

  4. Connect to the VM instance using SSH:
         
         gcloud compute ssh VM --tunnel-through-iap --zone ZONE
         

You run the rest of the commands in this section from the SSH session.

  5. Install the `kubectl` command-line tool and the [gke-gcloud-auth-plugin binary](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin) in the VM instance:
         
         sudo apt-get install -y kubectl google-cloud-sdk-gke-gcloud-auth-plugin
         

  6. Fetch credentials for the GKE cluster:
         
         export USE_GKE_GCLOUD_AUTH_PLUGIN=True
         gcloud container clusters get-credentials CLUSTER --zone ZONE
         

  7. Patch the default ClientConfig resource:
         
         kubectl patch clientconfig default \
             --namespace kube-public \
             --patch-file client-config-patch.yaml \
             --type merge
         

  8. Extract the `certificateAuthorityData` field from the patched default ClientConfig resource and store it in a file called `certificateAuthorityData.pem`:
         
         kubectl get clientconfig default \
              --namespace kube-public \
              --output jsonpath='{.spec.certificateAuthorityData}' \
              | base64 --decode > certificateAuthorityData.pem
         

  9. Extract the server field from the patched default ClientConfig resource and store it in a file called `server.txt`:
         
         kubectl get clientconfig default \
              --namespace kube-public \
              --output jsonpath='{.spec.server}' > server.txt
         

  10. Leave the SSH session:
         
         exit
         




## (Optional) Verify the cluster configuration

Before you proceed, you can verify that Identity Service for GKE has been set up correctly on the cluster. You verify the setup by using the Google service account attached to the VM instance to authenticate to the cluster using Identity Service for GKE.

  1. In Cloud Shell, grant the [Service Account OpenID Connect Identity Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) on the Google service account to the service account itself:
         
         gcloud iam service-accounts add-iam-policy-binding \
           ISG_GSA@PROJECT_ID.iam.gserviceaccount.com \
           --member serviceAccount:ISG_GSA@PROJECT_ID.iam.gserviceaccount.com \
           --role roles/iam.serviceAccountOpenIdTokenCreator
         

This role provides the `iam.serviceAccounts.getOpenIdToken` permission that's required in order to request ID tokens for the service account from the Service Account Credentials API.

  2. Connect to the VM instance using SSH:
         
         gcloud compute ssh VM --tunnel-through-iap --zone ZONE
         

You run the rest of the commands in this section from the SSH session.

  3. Request an [OAuth 2.0 access token](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth) from the [metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview) for the Google service account that's attached to the VM instance, using the OAuth client ID as the requested `aud` (audience) claim:
         
         ACCESS_TOKEN=$(curl --silent --header "Metadata-Flavor: Google" \
         http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token \
                | python3 -c 'import json, sys; print(json.load(sys.stdin).get("access_token"))')
         

The response body from the metadata server is a JSON document. The command uses an inline Python script to extract the `access_token` field from the response body.

  4. Request an [ID token](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oidc) from the Service Account Credentials API for the Google service account that's attached to the VM instance:
         
         ID_TOKEN=$(curl --silent --request POST \
             --data '{"audience": "CLIENT_ID", "includeEmail": true}' \
             --header "Authorization: Bearer $ACCESS_TOKEN" \
             --header "Content-Type: application/json; charset=utf-8" \
         "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/ISG_GSA@PROJECT_ID.iam.gserviceaccount.com:generateIdToken" \
                | python3 -c 'import json, sys; print(json.load(sys.stdin).get("token"))')
         

Note the following about the command above:

     * The `audience` field in the request body JSON specifies the requested `aud` (audience) claim of the ID token.
     * The access token from the previous step is used to authenticate to the API.
  5. View the claims in the ID token:
         
         echo $ID_TOKEN \
             | cut -d. -f2 \
             | base64 --decode --ignore-garbage 2> /dev/null \
             | python3 -m json.tool
         

Verify that the `email` claim contains the email address of the Google service account.

  6. Use the ID token to authenticate to the control plane by using Identity Service for GKE:
         
         kubectl get namespaces \
             --certificate-authority certificateAuthorityData.pem \
             --server $(cat server.txt) \
             --token $ID_TOKEN
         

The output resembles the following:
         
         Error from server (Forbidden): namespaces is forbidden: User "ISG_GSA@PROJECT_ID.iam.gserviceaccount.com" cannot list resource "namespaces" in API group "" at the cluster scope
         

This error is expected. Although the Google service account was granted IAM permissions on GKE clusters in the project, IAM permissions do not apply when you authenticate by using Identity Service for GKE. Instead, you configure access using Kubernetes role-based access control (RBAC).

  7. Create a cluster role binding that grants the `view` cluster role to the Google service account when the service account authenticates to the cluster by using Google's OpenID Connect provider:
         
         kubectl create clusterrolebinding ISG_GSA-cluster-view \
             --clusterrole view \
             --user ISG_GSA@PROJECT_ID.iam.gserviceaccount.com
         

If you set a `userPrefix` value other than `-` in the ClientConfig in your own environment, add the prefix to the value of the `--user` flag in this command.

  8. Access the GKE cluster by using Identity Service for GKE:
         
         kubectl get namespaces \
             --certificate-authority certificateAuthorityData.pem \
             --server $(cat server.txt) \
             --token $ID_TOKEN
         

The output resembles the following:
         
         NAME                      STATUS   AGE
         anthos-identity-service   Active   1h
         default                   Active   1h
         kube-node-lease           Active   1h
         kube-public               Active   1h
         kube-system               Active   1h
         

  9. Leave the SSH session:
         
         exit
         




## Create a context for the `kubectl` tool

The `kubectl` command can use a [kubeconfig file](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) to configure access to clusters. A kubeconfig file contains one or more contexts. Each context has a name, and optionally includes cluster connectivity information, credentials that are used to authenticate to the cluster, and a default namespace.

In this section, you create a kubeconfig file that has a context. The context includes connectivity details of the Identity Service for GKE proxy for your cluster. You do not add any user credentials to the kubeconfig file.

  1. In Cloud Shell, copy the files that contains the certificate authority data and server URL from the VM instance to the current directory:
         
         gcloud compute scp VM:~/certificateAuthorityData.pem VM:~/server.txt . \
             --tunnel-through-iap --zone ZONE
         

  2. Create a context and a cluster configuration that you will use later to connect to the GKE cluster from Cloud Build:
         
         kubectl config set-context private-cluster \
             --cluster private-cluster \
             --kubeconfig kubeconfig
         

The `--kubeconfig` flag creates the context and cluster configuration in a new file called kubeconfig in the current directory.

This command uses the GKE cluster name as the cluster configuration name for the context. In your own environment, you can use a different cluster configuration name in the context.

  3. Set the `certificateAuthorityData` field on the cluster configuration:
         
         kubectl config set-cluster private-cluster \
             --certificate-authority certificateAuthorityData.pem \
             --embed-certs \
             --kubeconfig kubeconfig
         

  4. Set the `server` field on the cluster configuration:
         
         kubectl config set-cluster private-cluster \
             --kubeconfig kubeconfig \
             --server $(cat server.txt)
         




## Create a Google service account for Cloud Build

  1. In the Cloud Shell, create a Google service account to run builds on the Cloud Build private pool:
         
         gcloud iam service-accounts create CB_GSA \
           --description "Runs builds on Cloud Build private pools" \
           --display-name "Cloud Build private pool"
         

Replace CB_GSA with the name that you want to use for the Google service account. For this tutorial, use `cloud-build-private-pool`.

  2. Grant the [Cloud Build Service Account role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild) on the project to the Google service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member serviceAccount:CB_GSA@PROJECT_ID.iam.gserviceaccount.com \
             --role roles/cloudbuild.builds.builder
         

This role provides the [default permissions of the Google-managed Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).

  3. Grant the [Service Account OpenID Connect Identity Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) on the Google service account to the service account itself:
         
         gcloud iam service-accounts add-iam-policy-binding \
             CB_GSA@PROJECT_ID.iam.gserviceaccount.com \
             --member serviceAccount:CB_GSA@PROJECT_ID.iam.gserviceaccount.com \
             --role roles/iam.serviceAccountOpenIdTokenCreator
         

This role provides the `iam.serviceAccounts.getOpenIdToken` permission that's required in order to request ID tokens for the service account from the Service Account Credentials API.

  4. Connect to the VM instance using SSH:
         
         gcloud compute ssh VM --tunnel-through-iap --zone ZONE
         

You run the rest of the commands in this section from the SSH session.

  5. In the SSH session, create a Kubernetes cluster role binding that grants the `cluster-admin` cluster role to the Google service account when the service account authenticates to the cluster by using Google's OpenID Connect provider:
         
         kubectl create clusterrolebinding CB_GSA-cluster-admin \
             --clusterrole cluster-admin \
             --user CB_GSA@PROJECT_ID.iam.gserviceaccount.com
         

The `cluster-admin` cluster role grants extensive cluster-wide permissions. In your own environment, you can use a cluster role that provides only the permissions that are necessary for the tasks that Cloud Build performs. You can also use role bindings to grant permissions only to specific namespaces.

If you set a `userPrefix` in the ClientConfig in your own environment, you must add that prefix to the value of the `--user` flag in this command.

  6. Leave the SSH session:
         
         exit
         




## Create a Cloud Build private pool

  1. In Cloud Shell, allocate an IP address range in your VPC network for the connection with the private pool:
         
         gcloud compute addresses create RESERVED_RANGE_NAME \
         --addresses RESERVED_RANGE_START_IP\
             --description "Cloud Build private pool reserved range" \
             --global \
             --network NETWORK \
             --prefix-length RESERVED_RANGE_PREFIX_LENGTH \
             --purpose VPC_PEERING
         

Replace the following:

     * RESERVED_RANGE_NAME: the name of the allocated IP address range that hosts the Cloud Build private pool. For this tutorial, use `cloud-build-private-pool`.
     * RESERVED_RANGE_START_IP: the first IP address of the allocated IP address range. For this tutorial, use `192.168.12.0`.
     * RESERVED_RANGE_PREFIX_LENGTH: the prefix length (subnet mask) of the allocated IP address range. The prefix length must be `/23` or a lower number, for example `/22` or `/21`. A lower number means a larger address range. For this tutorial, use `23`, and do not enter the leading `/` (slash).
  2. Create a firewall rule to allow inbound traffic from the reserved IP address range to other resources in your VPC network:
         
         gcloud compute firewall-rules create allow-private-pools-ingress \
             --allow all \
             --network NETWORK \
             --source-ranges RESERVED_RANGE_START_IP/RESERVED_RANGE_PREFIX_LENGTH
         

  3. Create a private service connection to connect your VPC network to the Service Networking service:
         
         gcloud services vpc-peerings connect \
             --network NETWORK \
             --ranges RESERVED_RANGE_NAME \
             --service servicenetworking.googleapis.com
         

Cloud Build private pools run workers using Service Networking. The private service connection enables your VPC network to communicate with the private pool on the allocated range of internal IP addresses, using a VPC Network Peering connection.

It can take a few minutes to create the private service connection.

If you use a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) in your own environment, for information about additional steps to create the private service connection, see [Set up your environment](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment#gcloud).

  4. Create a Cloud Build private pool in a Google-owned VPC network that is peered with your VPC network:
         
         gcloud builds worker-pools create PRIVATE_POOL_NAME \
            --no-public-egress \
            --peered-network projects/PROJECT_ID/global/networks/NETWORK \
            --region REGION
         

Replace the following:

     * PRIVATE_POOL_NAME: the name of the private pool. For this tutorial, use `private-pool`.
     * REGION: the [region](https://docs.cloud.google.com/build/docs/locations) to use for the private pool. For this tutorial, use `us-central1`.

The `--no-public-egress` flag means that workers in the private pool do not have public IP addresses. In your own environment, you can remove this flag if you want workers in the private pool to have internet connectivity using public IP addresses.

For information about additional configuration options, such as machine type and disk size for the workers in the private pool, see [Create and manage private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools#gcloud).




## Verify the solution

In this section, you verify the solution by running a build on the Cloud Build private pool. The build accesses the private GKE cluster.

  1. In Cloud Shell, create a Cloud Storage bucket to store build logs from Cloud Build:
         
         gcloud storage buckets create gs://PROJECT_ID-build-logs --location=REGION
         

  2. Create a [build configuration file](https://docs.cloud.google.com/build/docs/build-config-file-schema) for Cloud Build:
         
         cat << "EOF" > cloudbuild.yaml
         steps:
         - id: list-services
           name: gcr.io/google.com/cloudsdktool/google-cloud-cli
           entrypoint: bash
           args:
           - -eEuo
           - pipefail
           - -c
           - |-
             kubectl config use-context $_KUBECTL_CONTEXT
         
             ACCESS_TOKEN=$$(curl --silent \
                 --header "Metadata-Flavor: Google" \
                 http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token \
                 | python3 -c 'import json, sys; print(json.load(sys.stdin).get("access_token"))')
         
             ID_TOKEN=$$(curl --silent --request POST \
                 --data '{"audience": "CLIENT_ID", "includeEmail": true}' \
                 --header "Authorization: Bearer $$ACCESS_TOKEN" \
                 --header "Content-Type: application/json; charset=utf-8" \
                 "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/$_SERVICE_ACCOUNT:generateIdToken" \
                 | python3 -c 'import json, sys; print(json.load(sys.stdin).get("token"))')
         
             kubectl get services --namespace $_NAMESPACE --token $$ID_TOKEN
         
         logsBucket: gs://PROJECT_ID-build-logs
         
         options:
           env:
           - KUBECONFIG=/workspace/$_KUBECONFIG
         
         substitutions:
           _KUBECONFIG: kubeconfig
           _KUBECTL_CONTEXT: private-cluster
           _NAMESPACE: default
         
         serviceAccount: projects/$PROJECT_ID/serviceAccounts/$_SERVICE_ACCOUNT
         EOF
         

The step in the build configuration file does the following:

     1. Switches to the `kubectl` context that's specified by the `_KUBECTL_CONTEXT` substitution. The default substitution value is `private-cluster`.

     2. Retrieves an access token from the metadata server. The access token is issued to the Google service account that runs the build.

     3. Generates an ID token by using the Service Account Credentials API. The request to generate the ID token is authenticated by using the access token. The requested `aud` (audience) claim of the ID token is the OAuth 2.0 client ID that's specified by the `_CLIENT_ID` substitution.

     4. Lists the Kubernetes services in the namespace that's specified by the `_NAMESPACE` substitution. The default substitution value is `default`. The request is authenticated by using the ID token that was generated in the previous command.

Note the following about the build configuration file:

     * The `$` character is the prefix for [substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values). `$$` is used for bash parameter expansion and command substitution.

     * The substitutions `_KUBECONFIG` and `_KUBECTL_CONTEXT` enable different kubeconfig files and different contexts to be specified when you run a build. These substitutions enable you to manage multiple cluster configurations by using either a single kubeconfig file with multiple contexts, or by using multiple kubeconfig files.

     * The substitution `_SERVICE_ACCOUNT` does not have a default value. You must provide a value for this substitution when you run a build.

     * The `options` block sets the `KUBECONFIG` environment variable for all steps in the build.

     * The build step uses the `gcr.io/google.com/cloudsdktool/google-cloud-cli` builder image. This is a large container image, and it takes some time to pull it from the registry to the private pool worker. To reduce the time it takes to pull the builder image, you can [create a custom builder image](https://docs.cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders#creating_a_custom_builder) that contains only the required tools for the build step, such as `curl`, `kubectl`, and Python.

For more information about inline shell scripts in build configuration files, see [Running bash scripts](https://docs.cloud.google.com/build/docs/configuring-builds/run-bash-scripts).

  3. Run a build using the build configuration file and the files in the current directory:
         
         gcloud builds submit \
             --config cloudbuild.yaml \
             --region REGION \
             --substitutions _SERVICE_ACCOUNT=CB_GSA@PROJECT_ID.iam.gserviceaccount.com \
             --worker-pool projects/PROJECT_ID/locations/REGION/workerPools/PRIVATE_POOL_NAME
         

The command uploads all files that are in the current directory to Cloud Storage for use by Cloud Build. The build step uses the kubeconfig file to connect to the GKE cluster.

Near the end of the output, you see lines that resemble the following:
         
         NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
         kubernetes   ClusterIP   10.0.0.1     <none>        443/TCP   2h
         

This output shows that the private pool worker has connected to the cluster control plane by using the Identity Service for GKE authentication proxy.




## Troubleshooting

If you are unable to connect to the VM instance using SSH, add the `--troubleshoot` flag to help discover the cause of the connectivity issues:
    
    
    gcloud compute ssh VM --tunnel-through-iap --zone ZONE --troubleshoot
    

If you get the message `Error from server (NotFound): clientconfigs.authentication.gke.io "default" not found` when you patch the default ClientConfig on the GKE cluster, ensure that you have created the firewall rule as described in the section [Creating a private GKE cluster](https://docs.cloud.google.com/build/docs/private-pools/access-private-gke-clusters-service-identity#create_a_private_cluster). Verify that the firewall rule exists:
    
    
    gcloud compute firewall-rules describe allow-control-plane-clientconfig-webhook
    

If you cannot authenticate to the Identity Service for GKE proxy, look for errors in the logs of the pods in the `gke-oidc-service` deployment:
    
    
    gcloud compute ssh VM --tunnel-through-iap --zone ZONE --command \
        'kubectl logs deployment/gke-oidc-service \
             --namespace anthos-identity-service --all-containers'
    

If you run into other problems with this tutorial, we recommend that you review these documents:

  * [GKE troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting)
  * [Troubleshooting Kubernetes clusters](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-cluster/)



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete the resources

If you want to keep the project you used in this tutorial, delete the individual resources:

  1. In Cloud Shell, delete the Cloud Build private pool:
         
         gcloud builds worker-pools delete PRIVATE_POOL_NAME --region REGION --quiet
         

  2. Delete the private service connection to Service Networking:
         
         gcloud services vpc-peerings delete --network NETWORK \
           --service servicenetworking.googleapis.com --quiet --async
         

  3. Delete the IP address range allocated to Cloud Build private pools:
         
         gcloud compute addresses delete RESERVED_RANGE_NAME --global --quiet
         

  4. Delete the Cloud Storage bucket and all of its contents:
         
         gcloud storage rm gs://PROJECT_ID-build-logs --recursive
         

  5. Delete the GKE cluster:
         
         gcloud container clusters delete CLUSTER --zone ZONE --quiet --async
         

  6. Delete the Compute Engine VM instance:
         
         gcloud compute instances delete VM --zone ZONE --quiet
         

  7. Delete the firewall rules:
         
         gcloud compute firewall-rules delete allow-private-pools-ingress --quiet
         
         gcloud compute firewall-rules delete allow-ssh-ingress-from-iap --quiet
         
         gcloud compute firewall-rules delete allow-control-plane-clientconfig-webhook --quiet
         

  8. Remove the IAM role bindings:
         
         gcloud projects remove-iam-policy-binding PROJECT_ID \
             --member serviceAccount:CB_GSA@PROJECT_ID.iam.gserviceaccount.com \
             --role roles/cloudbuild.builds.builder
         
         gcloud projects remove-iam-policy-binding PROJECT_ID \
             --member serviceAccount:ISG_GSA@PROJECT_ID.iam.gserviceaccount.com \
             --role roles/container.admin
         
         gcloud iam service-accounts remove-iam-policy-binding \
             CB_GSA@PROJECT_ID.iam.gserviceaccount.com \
             --member serviceAccount:CB_GSA@PROJECT_ID.iam.gserviceaccount.com \
             --role roles/iam.serviceAccountOpenIdTokenCreator
         
         gcloud iam service-accounts remove-iam-policy-binding \
             ISG_GSA@PROJECT_ID.iam.gserviceaccount.com \
             --member serviceAccount:ISG_GSA@PROJECT_ID.iam.gserviceaccount.com \
             --role roles/iam.serviceAccountOpenIdTokenCreator
         

  9. Delete the Google service accounts:
         
         gcloud iam service-accounts delete CB_GSA@PROJECT_ID.iam.gserviceaccount.com \
            --quiet
         
         gcloud iam service-accounts delete ISG_GSA@PROJECT_ID.iam.gserviceaccount.com \
            --quiet
         




### Delete the OAuth 2.0 client ID

  1. Go to the **Credentials** page in Google Cloud console:

[Open the Credentials page](https://console.cloud.google.com/apis/credentials)

  2. Select your project from the project selector list.

  3. In the table of **OAuth 2.0 Client IDs** , find the row for **Identity Service for GKE** and then click the **Delete OAuth client** icon.

  4. In the dialog, click **Delete**.




## What's next

  * Learn how to [access Anthos clusters from Cloud Build with the connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway/tutorials/cloud-build-integration).
  * Learn how to [access private GKE clusters with Cloud Build private pools using Cloud VPN](https://docs.cloud.google.com/build/docs/private-pools/accessing-private-gke-clusters-with-cloud-build-private-pools).
  * Learn how to [create GKE private clusters with network proxies for control plane access](https://docs.cloud.google.com/architecture/creating-kubernetes-engine-private-clusters-with-net-proxies).
  * Learn how to [access external resources in a private network using a static external IP](https://docs.cloud.google.com/build/docs/private-pools/access-external-resources-using-static-external-ip).
  * Discover [GKE Identity Service](https://docs.cloud.google.com/anthos/identity). GKE Identity Service enables you to manage external identity provider authentication across a fleet of Anthos clusters.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
