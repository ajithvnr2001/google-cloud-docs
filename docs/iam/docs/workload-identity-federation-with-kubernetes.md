---
url: https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes/
title: Configure Workload Identity Federation with Kubernetes \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:03.636856+00:00
---

# Configure Workload Identity Federation with Kubernetes  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure Workload Identity Federation with Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to use Workload Identity Federation to let workloads that run on Azure Kubernetes Service (AKS), Amazon Elastic Kubernetes Service, or on a self-hosted Kubernetes cluster authenticate to Google Cloud.

Kubernetes lets you configure a cluster so that workloads can obtain Kubernetes ServiceAccount tokens [from a projected volume](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection). By setting up Workload Identity Federation, you can let workloads use these Kubernetes ServiceAccount tokens to authenticate to Google Cloud.

If you're using GKE, use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) instead of configuring Workload Identity Federation.

## Before you begin

Before you configure Workload Identity Federation, make sure that your Kubernetes cluster meets the following criteria:

###  GKE 

For Google Kubernetes Engine (GKE) users, see [Authenticate to Google Cloud APIs from GKE workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

###  AKS 

Make sure your cluster meets the following criteria:

  * You've enabled the [OIDC issuer](https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer) feature.

You must enable this feature so that Workload Identity Federation can access the OpenID Connect metadata and the JSON Web Key Set (JWKS) for the cluster.




###  EKS 

You don't need to make any changes in your EKS configuration.

###  Kubernetes 

Make sure your cluster meets the following criteria:

  * You're running Kubernetes 1.20 or later.

Previous versions of Kubernetes used a different ServiceAccount token format that is not compatible with the instructions in this document.

  * You configured `kube-apiserver` so that it [supports `ServiceAccount` token volume projections](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection).




The cluster doesn't need to be accessible over the internet.

## Configure Workload Identity Federation

You only need to perform these steps once for each Kubernetes cluster. You can then use the same workload identity pool and provider for multiple Kubernetes pods and across multiple Google Cloud projects.

To start configuring Workload Identity Federation, do the following:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

We recommend that you [ use a dedicated project to manage workload identity pools and providers](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#dedicated-project). 
  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the IAM, Resource Manager, Service Account Credentials, and Security Token Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com,iamcredentials.googleapis.com,sts.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Define an attribute mapping and condition

Kubernetes ServiceAccount tokens contain multiple claims, including the following:

  * `sub`: Contains the namespace and name of the ServiceAccount-for example, `system:serviceaccount:NAMESPACE:KSA_NAME`, where `NAMESPACE` is the namespace of the ServiceAccount and `KSA_NAME` is the name of the ServiceAccount.
  * `"kubernetes.io".namespace`: Contains the namespace of the ServiceAccount.
  * `"kubernetes.io".serviceaccount.name`: Contains the name of the ServiceAccount.
  * `"kubernetes.io".pod.name`: Contains the name of the pod.



To use `sub` as subject identifier (`google.subject`) in Google Cloud, use the following mapping:
    
    
    google.subject=assertion.sub
    

Optionally, you can [map additional attributes](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping). You can then refer to these attributes when granting access to resources. For example:
    
    
    google.subject=assertion.sub,
    attribute.namespace=assertion['kubernetes.io']['namespace'],
    attribute.service_account_name=assertion['kubernetes.io']['serviceaccount']['name'],
    attribute.pod=assertion['kubernetes.io']['pod']['name']
    

Optionally, define an [attribute condition](https://docs.cloud.google.com/iam/docs/workload-identity-federation#conditions). Attribute conditions are CEL expressions that can check assertion attributes and target attributes. If the attribute condition evaluates to `true` for a given credential, the credential is accepted. Otherwise, the credential is rejected.

You can use an attribute condition to restrict which Kubernetes ServiceAccounts can use Workload Identity Federation to obtain short-lived Google Cloud tokens. For example, the following condition restricts access to Kubernetes ServiceAccounts from the `backend` and `monitoring` namespaces:
    
    
    assertion['kubernetes.io']['namespace'] in ['backend', 'monitoring']
    

### Create the workload identity pool and provider

#### Required roles

To get the permissions that you need to configure Workload Identity Federation, ask your administrator to grant you the following IAM roles on the project: 

  * [Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Alternatively, the IAM Owner (`roles/owner`) basic role also includes permissions to configure identity federation. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

To create a workload identity pool and provider, do the following:

###  AKS 

  1. Determine the issuer URL of your AKS cluster:
         
         az aks show -n NAME -g RESOURCE_GROUP --query "oidcIssuerProfile.issuerUrl" -otsv
         

Replace the following:

     * `NAME`: The name of the cluster
     * `RESOURCE_GROUP`: The resource group of the cluster

The command outputs the issuer URL. You need the issuer URL in one of the following steps.

If the command doesn't return an issuer URL, verify that you've enabled the [OIDC issuer](https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer) feature.

  2. Create a new workload identity pool:
         
         gcloud iam workload-identity-pools create POOL_ID \
             --location="global" \
             --description="DESCRIPTION" \
             --display-name="DISPLAY_NAME"
         

Replace the following:

     * `POOL_ID`: The unique ID for the pool.
     * `DISPLAY_NAME`: The name of the pool.
     * `DESCRIPTION`: A description of the pool that you choose. This description appears when you grant access to pool identities.
  3. Add the AKS cluster as a workload identity pool provider:
         
         gcloud iam workload-identity-pools providers create-oidc WORKLOAD_PROVIDER_ID \
             --location="global" \
             --workload-identity-pool="POOL_ID" \
             --issuer-uri="ISSUER" \
             --attribute-mapping="MAPPINGS" \
             --attribute-condition="CONDITIONS"
         

Replace the following:

     * `WORKLOAD_PROVIDER_ID`: A unique workload identity pool provider ID of your choice.
     * `POOL_ID`: The workload identity pool ID that you created earlier.
     * `ISSUER`: The issuer URI that you determined earlier.
     * `MAPPINGS`: A comma-separated list of attribute mappings that you created earlier in this guide.
     * `CONDITIONS`: An optional attribute condition that you created earlier in this guide. Remove the parameter if you don't have an attribute condition.



###  EKS 

  1. Determine the issuer URL of your EKS cluster:
         
         aws eks describe-cluster --name NAME --query "cluster.identity.oidc.issuer" --output text
         

Replace `NAME` with the name of the cluster.

The command outputs the issuer URL. You need the issuer URL in one of the following steps.

  2. Create a new workload identity pool:
         
         gcloud iam workload-identity-pools create POOL_ID \
             --location="global" \
             --description="DESCRIPTION" \
             --display-name="DISPLAY_NAME"
         

Replace the following:

     * `POOL_ID`: The unique ID for the pool.
     * `DISPLAY_NAME`: The name of the pool.
     * `DESCRIPTION`: A description of the pool that you choose. This description appears when you grant access to pool identities.
  3. Add the EKS cluster as a workload identity pool provider:
         
         gcloud iam workload-identity-pools providers create-oidc WORKLOAD_PROVIDER_ID \
             --location="global" \
             --workload-identity-pool="POOL_ID" \
             --issuer-uri="ISSUER" \
             --attribute-mapping="MAPPINGS" \
             --attribute-condition="CONDITIONS"
         

Replace the following:

     * `WORKLOAD_PROVIDER_ID`: A unique workload identity pool provider ID of your choice.
     * `POOL_ID`: The workload identity pool ID that you created earlier.
     * `ISSUER`: The issuer URI that you determined earlier.
     * `MAPPINGS`: A comma-separated list of attribute mappings that you created earlier in this guide.
     * `CONDITIONS`: An optional attribute condition that you created earlier in this guide. Remove the parameter if you don't have an attribute condition.



###  Kubernetes 

  1. Connect to your Kubernetes cluster and use `kubectl` to determine your cluster's issuer URL:
         
         kubectl get --raw /.well-known/openid-configuration | jq -r .issuer
         

You need the issuer URL in one of the following steps.

  2. Download the cluster's JSON Web Key Set (JWKS):
         
         kubectl get --raw /openid/v1/jwks > cluster-jwks.json
         

In one of the following steps, you upload the JWKS so that Workload Identity Federation can verify the authenticity of the Kubernetes ServiceAccount tokens issued by your cluster.

  3. Create a new workload identity pool:
         
         gcloud iam workload-identity-pools create POOL_ID \
             --location="global" \
             --description="DESCRIPTION" \
             --display-name="DISPLAY_NAME"
         

Replace the following:

     * `POOL_ID`: The unique ID for the pool.
     * `DISPLAY_NAME`: The name of the pool.
     * `DESCRIPTION`: A description of the pool that you choose. This description appears when you grant access to pool identities.
  4. Add the Kubernetes cluster as a workload identity pool provider and upload the cluster's JWKS:
         
         gcloud iam workload-identity-pools providers create-oidc WORKLOAD_PROVIDER_ID \
             --location="global" \
             --workload-identity-pool="POOL_ID" \
             --issuer-uri="ISSUER" \
             --attribute-mapping="MAPPINGS" \
             --attribute-condition="CONDITIONS" \
             --jwk-json-path="cluster-jwks.json"
         

Replace the following:

     * `WORKLOAD_PROVIDER_ID`: Enter a unique ID for the workload identity pool provider.
     * `POOL_ID`: The workload identity pool ID that you created earlier.
     * `ISSUER`: The issuer URI that you determined earlier.
     * `MAPPINGS`: A comma-separated list of attribute mappings that you created earlier in this guide.
     * `CONDITIONS`: An optional attribute condition that you created earlier in this guide. Remove the parameter if you don't have an attribute condition.
**Note:** The command doesn't validate the cluster's JWKS. If the JWKS is malformed or expired, subsequent authentication attempts might fail with an error message `Error connecting to the given credential's issuer`.



## Grant access to a Kubernetes workload

This section describes how to configure a Kubernetes workload to access Google Cloud APIs by using either Workload Identity Federation direct resource access or service account impersonation.

You must perform these steps once for each Kubernetes workload that needs access to Google Cloud.

We recommend that you use Workload Identity Federation. However, when using identity federation, certain API methods might have limitations. For a list of limitations, see [Identity federation: products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).

If the methods that your workload uses have such limitations, you can instead use IAM impersonation.

### Use Workload Identity Federation to grant direct resource access

In this section, you use Workload Identity Federation to grant an IAM role to a Kubernetes ServiceAccount so that it can directly access Google Cloud resources.

To create a Kubernetes ServiceAccount and grant it a role, do the following:

  1. Create a Kubernetes ServiceAccount:
         
         kubectl create serviceaccount KSA_NAME --namespace NAMESPACE
         

Replace the following:

     * `KSA_NAME`: a name for the ServiceAccount.
     * `NAMESPACE`: the namespace in which to create the ServiceAccount.
  2. Grant IAM access to the Kubernetes ServiceAccount for a Google Cloud resource.

Following the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege), we recommend that you grant only roles that are specific to the resources that your application must access.

In the following example, the command grants the [Kubernetes Engine Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterViewer) (`roles/container.clusterViewer`) role to the ServiceAccount that you created. The command uses the subject that you mapped earlier in this document.
         
         gcloud projects add-iam-policy-binding projects/PROJECT_ID \
             --role=roles/container.clusterViewer \
             --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT \
             --condition=None
         

Replace the following:

     * `PROJECT_ID`: the ID of the Google Cloud project on which to grant access.
     * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the project that contains the workload identity pool.
     * `POOL_ID`: the ID of the workload identity pool.
     * `MAPPED_SUBJECT`: the Kubernetes ServiceAccount from the claim in your ID token that you mapped to `google.subject`. For example, if you mapped `google.subject=assertion.sub` and your ID token contains `"sub": "system:serviceaccount:default:my-kubernetes-serviceaccount"`, then `MAPPED_SUBJECT` is `system:serviceaccount:default:my-kubernetes-serviceaccount`.

You can grant roles on any Google Cloud resource that supports IAM allow policies. The syntax of the principal identifier depends on the Kubernetes resource. For a list of supported identifiers, see [Principal identifiers for Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#principal-id-examples).




You can now deploy a workload that uses the Kubernetes ServiceAccount to access the Google Cloud resources to which you granted access.

### Alternative: Use IAM service account impersonation to grant access

To configure your Kubernetes ServiceAccount to use IAM service account impersonation, do the following:

  1. Create a Kubernetes ServiceAccount, if you haven't already:
         
         kubectl create serviceaccount KSA_NAME --namespace NAMESPACE
         

Replace the following:

     * `KSA_NAME`: a name for the ServiceAccount.
     * `NAMESPACE`: the namespace in which to create the ServiceAccount.
  2. Create an IAM [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that represents the workload.

The service account doesn't need to be in the same project as the workload identity pool, but you must specify the project that contains the service account when referring to it.
         
         gcloud iam service-accounts create IAM_SA_NAME \
             --project=IAM_SA_PROJECT_ID
         

Replace the following:

     * `IAM_SA_NAME`: the name of the service account.
     * `IAM_SA_PROJECT_ID`: the project ID of the service account.
  3. [Grant your IAM service account access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to the specific Google Cloud resources that you want the Kubernetes workload to access.
         
         gcloud projects add-iam-policy-binding IAM_SA_PROJECT_ID \
             --member="serviceAccount:IAM_SA_NAME@IAM_SA_PROJECT_ID.iam.gserviceaccount.com" \
             --role="ROLE"
         

Replace the following:

     * `IAM_SA_PROJECT_ID`: the ID of the project where you created your service account.
     * `IAM_SA_NAME`: the name of the service account.
     * `ROLE`: the name of the role to grant—for example, `roles/container.clusterViewer`.
  4. Grant the Kubernetes ServiceAccount access to impersonate the IAM service account:
         
         gcloud iam service-accounts add-iam-policy-binding \
           IAM_SA_NAME@IAM_SA_PROJECT_ID.iam.gserviceaccount.com \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
             --role=roles/iam.workloadIdentityUser
         
         

Replace the following:

     * `IAM_SA_NAME`: the name of the service account.
     * `IAM_SA_PROJECT_ID`: the ID of the project where you created your service account.
     * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the project that contains the workload identity pool.
     * `POOL_ID`: the ID of the workload identity pool.
     * `MAPPED_SUBJECT`: the Kubernetes ServiceAccount from the claim in your ID token that you mapped to `google.subject`. For example, if you mapped `google.subject=assertion.sub` and your ID token contains `"sub": "system:serviceaccount:default:my-kubernetes-serviceaccount"`, then `MAPPED_SUBJECT` is `system:serviceaccount:default:my-kubernetes-serviceaccount`.

For information on authorizing IAM service accounts to access Google Cloud APIs, see [Understanding service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts).




You can now deploy a workload that uses the Kubernetes ServiceAccount and the IAM service account to access the Google Cloud resources to which you granted access.

### Deploy the Kubernetes workload

To deploy a Kubernetes workload that can access Google Cloud resources, do the following:

  1. Create a credential configuration file:
         
         gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
             --service-account=SERVICE_ACCOUNT_EMAIL \
             --credential-source-file=/var/run/service-account/token \
             --credential-source-type=text \
             --sts-location=REGION \
             --output-file=credential-configuration.json

Replace the following:

     * `PROJECT_NUMBER`: The project number of the project that contains the workload identity pool
     * `POOL_ID`: The ID of the workload identity pool
     * `WORKLOAD_PROVIDER_ID`: The ID of the workload identity pool provider
     * `SERVICE_ACCOUNT_EMAIL`: Email address of the service account, if you configured your Kubernetes ServiceAccount to use IAM service account impersonation. Omit this flag if you configured your Kubernetes ServiceAccount to use direct resource access.
     * `REGION`: Optional. Specify the region of the [regional Security Token Service endpoints](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints), if they are available.

The credential configuration file lets the [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries), the gcloud CLI, and Terraform determine the following:

     * Where to obtain external credentials from
     * Which workload identity pool and provider to use
     * Which service account to impersonate
**Note:** Unlike a [service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys), a credential configuration file doesn't contain a private key and doesn't need to be kept confidential. Details about the credential configuration file are available at <https://google.aip.dev/auth/4117>.
  2. Import the credential configuration file as a [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
         
         kubectl create configmap CONFIGMAP_NAME \
           --from-file credential-configuration.json \
           --namespace NAMESPACE
         

Replace the following:

     * `CONFIGMAP_NAME`: The name of the ConfigMap.
     * `NAMESPACE`: The namespace in which to create the ConfigMap.
  3. Deploy a workload and let it use the Kubernetes ServiceAccount and ConfigMap.

Create a manifest and configure as follows:

     * Mount a [projected token volume](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection) so that the workload can obtain a Kubernetes ServiceAccount token from a local file. Configure the volume so that the Kubernetes ServiceAccount token uses the audience expected by your workload identity pool provider.
     * Mount the ConfigMap that contains the credential configuration file so that the workload can access the necessary configuration for using Workload Identity Federation.
     * Add an environment variable `GOOGLE_APPLICATION_CREDENTIALS` that contains the path of the credential configuration file so that workloads can find the file.

The following is an example manifest that uses the Kubernetes ServiceAccount and ConfigMap to let the Google Cloud CLI authenticate to Google Cloud:
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example
      namespace: NAMESPACE
    spec:
      containers:
      - name: example
        image: google/cloud-sdk:alpine
        command: ["/bin/sh", "-c", "gcloud auth login --cred-file $GOOGLE_APPLICATION_CREDENTIALS && gcloud auth list && sleep 600"]
        volumeMounts:
        - name: token
          mountPath: "/var/run/service-account"
          readOnly: true
        - name: workload-identity-credential-configuration
          mountPath: "/etc/workload-identity"
          readOnly: true
        env:
        - name: GOOGLE_APPLICATION_CREDENTIALS
          value: "/etc/workload-identity/credential-configuration.json"
    
      serviceAccountName: KSA_NAME
      volumes:
      - name: token
        projected:
          sources:
          - serviceAccountToken:
              audience: https://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID
              expirationSeconds: 3600
              path: token
      - name: workload-identity-credential-configuration
        configMap:
          name: CONFIGMAP_NAME

You can follow the same approach to let tools and workloads that use one of the following client libraries [find credentials automatically](https://docs.cloud.google.com/docs/authentication/client-libraries):

###  C++ 

The [Google Cloud Client Libraries for C++](https://docs.cloud.google.com/cpp/docs) support Workload Identity Federation since version [v2.6.0](https://github.com/googleapis/google-cloud-cpp/releases/tag/v2.6.0). To use Workload Identity Federation, you must build the client libraries with version 1.36.0 or later of gRPC.

###  Go 

Client libraries for Go support Workload Identity Federation if they use version v0.0.0-20210218202405-ba52d332ba99 or later of the `golang.org/x/oauth2` module.

To check which version of this module your client library uses, run the following commands:
    
    cd $GOPATH/src/cloud.google.com/go
    go list -m golang.org/x/oauth2
    

###  Java 

Client libraries for Java support Workload Identity Federation if they use version 0.24.0 or later of the [`com.google.auth:google-auth-library-oauth2-http` artifact](https://search.maven.org/artifact/com.google.auth/google-auth-library-oauth2-http).

To check which version of this artifact your client library uses, run the following Maven command in your application directory:
    
    mvn dependency:list -DincludeArtifactIds=google-auth-library-oauth2-http
    

###  Node.js 

Client libraries for Node.js support Workload Identity Federation if they use version 7.0.2 or later of the [`google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs).

To check which version of this package your client library uses, run the following command in your application directory:
    
    npm list google-auth-library
    

When you create a `GoogleAuth` object, you can specify a project ID, or you can allow `GoogleAuth` to find the project ID automatically. To find the project ID automatically, the service account in the configuration file must have the Browser role (`roles/browser`), or a role with equivalent permissions, on your project. For details, see the [`README` for the `google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs#using-external-identities).

###  Python 

Client libraries for Python support Workload Identity Federation if they use version 1.27.0 or later of the [`google-auth` package](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth).

To check which version of this package your client library uses, run the following command in the environment where the package is installed:
    
    pip show google-auth
    

To specify a project ID for the authentication client, you can set the `GOOGLE_CLOUD_PROJECT` environment variable, or you can allow the client to find the project ID automatically. To find the project ID automatically, the service account in the configuration file must have the Browser role (`roles/browser`), or a role with equivalent permissions, on your project. For details, see the [user guide for the `google-auth` package](https://github.com/googleapis/google-cloud-python/blob/main/packages/google-auth/docs/user-guide.rst#using-external-identities).

###  gcloud 

To authenticate using Workload Identity Federation, use the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command:
    
    gcloud auth login --cred-file=FILEPATH.json
    

Replace `FILEPATH` with the path to the credential configuration file.

Support for Workload Identity Federation in gcloud CLI is available in [version 363.0.0 and later versions of the gcloud CLI](https://docs.cloud.google.com/sdk/docs/components#updating_components).

###  Terraform 

The [Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) supports Workload Identity Federation if you use version 3.61.0 or later:
    
    terraform {
      required_providers {
        google = {
          source  = "hashicorp/google"
          version = "~> 3.61.0"
        }
      }
    }
    

###  bq 

To authenticate using Workload Identity Federation, use the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command, as follows:
    
    gcloud auth login --cred-file=FILEPATH.json
    

Replace `FILEPATH` with the path to the credential configuration file.

Support for Workload Identity Federation in bq is available in [version 390.0.0 and later versions of the gcloud CLI](https://docs.cloud.google.com/sdk/docs/components#updating_components).

  4. Optionally, verify that authentication works correctly by running the following command:
         
         kubectl exec example --namespace NAMESPACE -- gcloud auth print-access-token




## What's next

  * Read more about [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  * Learn about [best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation).
  * See how you can [manage workload identity pools and providers](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
