---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication/
title: Authenticate to the Kubernetes API server \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:28.314888+00:00
---

# Authenticate to the Kubernetes API server  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Authenticate to the Kubernetes API server Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page guides you through authenticating securely to the Kubernetes API server from GKE clusters. You can secure your cluster by ensuring that only authorized users and applications access your Kubernetes resources. You'll learn about available authentication methods, the recommended authentication method, and how to authenticate users, applications, and legacy systems.

For information on authenticating Kubernetes workloads to Google Cloud APIs, refer to [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

This page is for Security specialists and Operators who must authenticate securely to the Kubernetes API server from GKE clusters. This page provides essential information on available authentication methods and how to implement them. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following concepts:

  * [General overview of authentication in Google Cloud](https://docs.cloud.google.com/docs/authentication)
  * [General overview of IAM and role-based access control (RBAC) in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control)
  * [General overview of Kubernetes methods for authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Authenticate users

GKE manages end-user authentication for you through the Google Cloud CLI. The gcloud CLI authenticates users to Google Cloud, sets up the Kubernetes configuration, gets an OAuth access token for the cluster, and keeps the access token up-to-date.

All GKE clusters are configured to accept Google Cloud user and service account identities, by validating the credentials presented by `kubectl` and retrieving the email address associated with the user or service account identity. As a result, the credentials for those accounts must include the `userinfo.email` OAuth scope to successfully authenticate.

When you use `gcloud` to [set up your environment's `kubeconfig`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#store_info) for a new or existing cluster, `gcloud` gives `kubectl` the same credentials used by `gcloud` itself. For example, if you use `gcloud auth login`, your personal credentials are provided to `kubectl`, including the `userinfo.email` scope. This allows the GKE cluster to authenticate the `kubectl` client.

Alternatively, you may choose to configure `kubectl` to use the credentials of a Google Cloud service account, while running on a Compute Engine instance. However, by default, the `userinfo.email` scope is _not_ included in credentials created by Compute Engine instances. Therefore, you **must** add this scope explicitly, such as by using the `--scopes` flag when the Compute Engine instance is created.

You can authorize actions in your cluster using [Identity and Access Management (IAM) or Kubernetes Role Based Access Control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control).

**Note:** Before OAuth integration with GKE, the pre-provisioned X.509 certificate or a static password were the only available authentication methods. These methods are no longer recommended and are disabled by default on all new clusters. If you use legacy authentication methods, we recommend that you migrate to newer authentication methods.

### Authenticate with OAuth

To authenticate to your cluster using the OAuth method, perform the following:

  1. Sign in to the gcloud CLI using your credentials. This opens a web browser to complete the authentication process to Google Cloud:
         
         gcloud auth login
         

**Caution:** Don't perform this on a Compute Engine VM where all users have access to `root`. Use a service account for authentication. For details, see the Applications within Google Cloud section.
  2. Retrieve the Kubernetes credentials for a specific cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  3. Verify that you are authenticated:
         
         kubectl cluster-info
         




Once users or Google Cloud service accounts are authenticated, they must also be _authorized_ to perform any action on a GKE cluster. For more information on how to configure authorization, see [role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

## Authenticate applications

You can also authenticate to the API server from an application in a Pod without user interaction, such as from a script in your CI/CD pipeline. How you achieve this depends on the environment where your application is running.

### Application in the same cluster

If your application is running in the same GKE cluster, use a Kubernetes service account to authenticate.

  1. Create a [Kubernetes service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) and attach it to your Pod. If your Pod already has a Kubernetes service account, or if you want to use the namespace's default service account, skip this step.

  2. Use Kubernetes RBAC to grant the Kubernetes service account the permissions that your application requires.

The following example grants `view` permissions to resources in the `prod` namespace to a service account named `cicd` in the `cicd-ns` namespace:
         
         kubectl create rolebinding cicd-secret-viewer \
             --namespace=prod \
             --clusterrole=view \
             --serviceaccount=cicd-ns:cicd
         

  3. At runtime, when your application sends a Kubernetes API request, the API server authenticates the service account credentials.




### Applications within Google Cloud

If your application runs inside Google Cloud but outside the target cluster (for example, a Compute Engine VM or another GKE cluster), you should authenticate to the API server using the IAM service account credentials available in the environment.

  1. Assign an IAM service account to your environment. If your application is running inside a Compute Engine VM, [assign an IAM service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#user-managed_service_accounts) to the instance. If your application is running in a different GKE cluster, use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to configure your Pod to run as an IAM service account.

The examples that follow use `ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com` as the IAM service account.

  2. Grant the IAM service account access to the cluster.

The following example grants the `roles/container.developer` IAM role, which provides access to Kubernetes API objects inside clusters:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/container.developer
         

Alternatively, you can use RBAC to grant the IAM service account access to the cluster. Run the `kubectl create rolebinding` command from Applications in the same cluster and use `--user=ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com` instead of the `--service-account` flag.

  3. Retrieve the cluster credentials:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Your application is automatically authenticated using the IAM service account set on the environment.




### Applications in other environments

If your application is authenticating from an environment outside Google Cloud, it cannot access managed IAM service account credentials. To retrieve cluster credentials, you can create an IAM service account, download its key, and use the key at runtime from your service to retrieve cluster credentials with the gcloud CLI.

**Caution:** IAM service account keys are long-lived credentials. Anyone with access to the key can use it to perform authorized actions in your Google Cloud project. Managing keys can be difficult at scale. Consider using [_workload identity federation_](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation), which configures credentials issued by external identity providers to impersonate IAM service accounts and access Google Cloud resources.

  1. Create an IAM service account for your application. If you already have an IAM service account, skip this step.

The following command creates an IAM service account named `ci-cd-pipeline`:
         
         gcloud iam service-accounts create ci-cd-pipeline
         

  2. Grant the IAM service account access to your cluster.

The following command grants the `roles/container.developer` IAM role to the `ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com` IAM service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/container.developer
         

You can also use RBAC to grant the IAM service account access to the cluster. Run the `kubectl create rolebinding` command from Applications in the same cluster and use `--user=ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com` instead of the `--service-account` flag.

  3. Create and download a key for your IAM service account. Make it available to your application at runtime:
         
         gcloud iam service-accounts keys create gsa-key.json \
             --iam-account=ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com
         

  4. At runtime, in the environment running your application, authenticate to the gcloud CLI by using your IAM service account key:
         
         gcloud auth activate-service-account ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com \
             --key-file=gsa-key.json
         

  5. Use the gcloud CLI to retrieve the cluster credentials:
         
         gcloud config set project PROJECT_ID
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         




### Environments without gcloud

Using the gcloud CLI to retrieve cluster credentials is recommended because this method is resilient to cluster events like a control plane [IP rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation) or [credential rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation). However, if you cannot install the gcloud CLI in your environment, you can still create a static kubeconfig file to authenticate to the cluster:

  1. Create an IAM service account for your application. If you already have an IAM service account, skip this step.

The following command creates an IAM service account named `ci-cd-pipeline`:
         
         gcloud iam service-accounts create ci-cd-pipeline
         

  2. Grant the IAM service account access to your cluster.

The following command grants the `roles/container.developer` IAM role to the `ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com` IAM service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/container.developer
         

You can also create a [custom IAM role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) for fine-grained control over the permissions that you grant.

  3. Create and download a key for your IAM service account.

In the following example, the key file is named `gsa-key.json`:
         
         gcloud iam service-accounts keys create gsa-key.json \
             --iam-account=ci-cd-pipeline@PROJECT_ID.iam.gserviceaccount.com
         

  4. Get the control plane endpoint for the cluster:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --format="value(endpoint)"
         

  5. If you use the IP-based endpoint for control plane access, then get the base-64 encoded public certificate of the cluster root certificate authority (CA). If you use the DNS-based endpoint, then you can skip this step.
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --format="value(masterAuth.clusterCaCertificate)"
         

  6. Create a `kubeconfig.yaml` file. Use one of following formats, depending on how your application accesses the control plane:

     * **DNS-based endpoint** :
           
           apiVersion: v1
           kind: Config
           clusters:
           - name: CLUSTER_NAME
             cluster:
               server: https://ENDPOINT
           users:
           - name: ci-cd-pipeline-gsa
             user:
               exec:
                 apiVersion: client.authentication.k8s.io/v1beta1
                 args:
                 - --use_application_default_credentials
                 command: gke-gcloud-auth-plugin
                 installHint: Install gke-gcloud-auth-plugin for kubectl by following
                   https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin
                 provideClusterInfo: true
           contexts:
           - context:
               cluster: CLUSTER_NAME
               user: ci-cd-pipeline-gsa
             name: CLUSTER_NAME-ci-cd
           current-context: CLUSTER_NAME-ci-cd
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `ENDPOINT`: the value you obtained for `endpoint` from the previous step.

When you use the DNS-based endpoint, the Google Front End (GFE) service that hosts the DNS-based endpoint presents a certificate that's signed by a public Google CA. Your client can validate this certificate by using built-in libraries. For more information, see [Transport security for control plane connections](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#tls-control-plane).

     * **IP-based endpoint** :
           
           apiVersion: v1
           kind: Config
           clusters:
           - name: CLUSTER_NAME
             cluster:
               server: https://ENDPOINT
               certificate-authority-data: CLUSTER_CA_CERTIFICATE
           users:
               - name: ci-cd-pipeline-gsa
                 user:
                   exec:
                     apiVersion: client.authentication.k8s.io/v1beta1
                     args:
                     - --use_application_default_credentials
                     command: gke-gcloud-auth-plugin
                     installHint: Install gke-gcloud-auth-plugin for kubectl by following
                       https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin
                     provideClusterInfo: true
               contexts:
               - context:
                   cluster: CLUSTER_NAME
                   user: ci-cd-pipeline-gsa
                 name: CLUSTER_NAME-ci-cd
               current-context: CLUSTER_NAME-ci-cd
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `ENDPOINT`: the value in the `endpoint` field, from the output of the previous step.
       * `CLUSTER_CA_CERTICATE`: the base64-encoded public certificate of the cluster.

When you use the IP-based endpoints, the API server presents a certificate that's signed by the cluster root CA. Your client uses the public CA certificate in the `certificate-authority-data` field to validate the API server certificate. For more information, see [Transport security for control plane connections](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#tls-control-plane).

  7. Deploy `kubeconfig.yaml` and `gsa-key.json` alongside your application in your environment. At runtime, in the environment running your application, set these environment variables:
         
         export KUBECONFIG=path/to/kubeconfig.yaml
         export GOOGLE_APPLICATION_CREDENTIALS=path/to/gsa-key.json
         

  8. Your application can now send requests to the Kubernetes API and will be authenticated as the IAM service account.




## Update legacy authentication methods

**Note:** For GKE Autopilot clusters, legacy authentication methods cannot be used.**Note:** Basic authentication is deprecated and has been removed in GKE 1.19 and later.

Before OAuth integration with GKE, the pre-provisioned X.509 certificate or a static password were the only available authentication methods, but are no longer recommended and should be disabled. These methods present a wider surface of attack for cluster compromise and are disabled by default on clusters running GKE version 1.12 and later. If you use legacy authentication methods, we recommend that you turn them off.

If enabled, a user with the`container.clusters.getCredentials` permission can retrieve the client certificate and static password. The `roles/container.admin`, `roles/owner`, and`roles/editor` roles all have this permission, so use those roles wisely. Read more about [IAM roles in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam).

### Disable authentication with a static password

A static password is a username and password combination that the API server validates. In GKE, this authentication method is referred to as basic authentication.

**Note:** Basic authentication is deprecated and has been removed in GKE 1.19 and later.

To update an existing cluster and remove the static password:
    
    
    gcloud container clusters update CLUSTER_NAME \
         --location=CONTROL_PLANE_LOCATION \
         --no-enable-basic-auth
    

### Disable authentication with a client certificate

With certificate authentication, a client presents a certificate that the API server verifies with the specified certificate authority. In GKE, the [cluster root Certificate Authority (CA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-trust) signs client certificates.

Client certificate authentication has implications on authorization to the Kubernetes API server. If legacy [Attribute Based Access Control (ABAC)](https://kubernetes.io/docs/reference/access-authn-authz/abac/) authorization is enabled on the cluster, by default, client certificates can authenticate and perform any action on the API server. On the other hand, with Role Based Access Control (RBAC) enabled, client certificates must be granted specific authorization to Kubernetes resources.

**Note:** In GKE 1.8 and later, legacy ABAC is disabled by default, and the client certificate is not granted permissions.

To create a cluster without generating a client certificate, use the `--no-issue-client-certificate` flag:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
        --no-issue-client-certificate
    

Currently, there is no way to remove a client certificate from an existing cluster. To stop using client certificate authentication on an existing cluster, ensure you have RBAC enabled on the cluster, and that the client certificate does not have any authorization on the cluster.

**Note:** The `--no-issue-client-certificate` flag only disables legacy GKE client certificate issuance. It does not disable the [Kubernetes certificates API](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/), which is used to operate the cluster and cannot be disabled.

## What's next

  * Learn about [Google Cloud Authentication](https://docs.cloud.google.com/docs/authentication).
  * Learn about [Access Control in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control).
  * Learn about [Google service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts).
  * Learn about [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).
  * Learn about [Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
