---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-federation/
title: Enabling Workload Identity Federation on AKS and EKS \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:59:49.689250+00:00
---

# Enabling Workload Identity Federation on AKS and EKS  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enabling Workload Identity Federation on AKS and EKS Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-federation.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/enable-workload-identity-federation.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/enable-workload-identity-federation.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/enable-workload-identity-federation.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/enable-workload-identity-federation.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enable-workload-identity-federation.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/enable-workload-identity-federation.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/enable-workload-identity-federation.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/enable-workload-identity-federation.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/enable-workload-identity-federation.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/enable-workload-identity-federation.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/enable-workload-identity-federation.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/enable-workload-identity-federation.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/enable-workload-identity-federation.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/enable-workload-identity-federation.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/enable-workload-identity-federation.html)



This topic explains how to enable Workload Identity Federation for Apigee hybrid installations on **AKS** and **EKS** platforms using Kubernetes Projected Service Account Tokens. 

**Note:** If your Kubernetes platform does not support Projected Service Account Tokens, or if you need to integrate with a custom Identity Provider, you can use an alternative sidecar-based method to enable Workload Identity Federation. See [Use sidecar authentication for Workload Identity Federation for AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/use-sidecar-for-wif).

For installations on **GKE** , follow the instructions in [Enabling Workload Identity Federation for GKE on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-gke). 

## Overview

Workload Identity Federation lets applications running outside Google Cloud impersonate a Google Cloud Platform service account by using credentials from an external identity provider. 

Using Workload Identity Federation can help you improve security by letting applications use the authentication mechanisms that the external environment provides and can help [replace service account keys](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#using_service_accounts). 

For an overview, see [Best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation). 

**Note:** The `apigee-logger` component does not support Workload Identity Federation. See the [known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues#hybrid-apigee-logger-wif).

##  Set up Workload Identity Federation 

To use Workload Identity Federation with Apigee hybrid, first configure your cluster and then apply the feature to your Apigee hybrid installation. 

**Note:** Although granting Identity and Access Management (IAM) roles directly to a federated principal (`principal://`) is the recommended best practice for [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation), Apigee hybrid requires IAM service account impersonation because the hybrid Helm charts and control plane synchronization APIs require IAM service account email addresses.

###  Before you begin 

These instructions assume you have already set up your Apigee hybrid installation. The IAM service accounts and Kubernetes service accounts are created during initial installation. See [The Big Picture](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/big-picture) for an overview of installing Apigee hybrid. 

For installations on **AKS** , Make sure you have enabled the [OpenID Connect (OIDC) issuer](https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer). You must enable this feature so that Workload Identity Federation can access the OpenID Connect metadata and the JSON Web Key Set (JWKS) for the cluster. 

**Note:** If the cluster gets deleted for any reason, the IAM provider will need to be recreated.

###  Configure your cluster to use Workload Identity Federation. 

  1. Check that the current `gcloud` configuration is set to your Google Cloud project ID with the following command: 
         
         gcloud config get project

If needed, set the current `gcloud` configuration:
    
    gcloud config set project PROJECT_ID

  2. Enable the Security Token Service API: 

Check that the Security Token Service API is enabled with the following command: 
         
         gcloud services list --enabled --project PROJECT_ID | grep sts.googleapis.com

If the API is not enabled: 

### Console

Enable the Security Token Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sts.googleapis.com&redirect=https%3A//console.cloud.google.com)

### Command line

Enable the API with the following command: 
         
         gcloud services enable sts.googleapis.com --project PROJECT_ID

  3. Create the workload identity pool and provider. 

#### Required roles

To get the permissions that you need to configure Workload Identity Federation, ask your administrator to grant you the following IAM roles on the project: 

     * [Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Alternatively, the IAM Owner (`roles/owner`) basic role also includes permissions to configure identity federation. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

To create a workload identity pool and provider, do the following: 

     1. Determine the issuer URL of your AKS cluster: 

### AKS
            
            az aks show -n NAME -g RESOURCE_GROUP --query "oidcIssuerProfile.issuerUrl" -otsv

Replace the following: 

        * `NAME`: The name of the cluster.
        * `RESOURCE_GROUP`: The resource group of the cluster.

The command outputs the issuer URL. You will need the issuer URL in one of the following steps. 

If the command doesn't return an issuer URL, verify that you've enabled the [OIDC issuer](https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer) feature. 

### EKS
    
    aws eks describe-cluster --name NAME --query "cluster.identity.oidc.issuer" --output text
    

Replace `NAME` with the name of the cluster. 

The command outputs the issuer URL. You need the issuer URL in one of the following steps. 

### Other Kubernetes

Connect to your Kubernetes cluster and use `kubectl` to determine your cluster's issuer URL:
    
    kubectl get --raw /.well-known/openid-configuration | jq -r .issuer
    

You need the issuer URL in one of the following steps. 

     2. **Optional:** If your OIDC issuer is not publicly accessible, download the cluster's JSON Web Key Set (JWKS): **Note:** This step requires kubectl access to your cluster. **Tip:** When using the JWKS file, you will need to upload a new JWKS file whenever you rotate the signing keys for the cluster. 
            
            kubectl get --raw /openid/v1/jwks > cluster-jwks.json
            

To check if your OIDC provider is publicly available, you should be able to access your provider URL with a CURL command and receive a 200 response. 

     3. Create a new workload identity pool: 
            
            gcloud iam workload-identity-pools create POOL_ID \
              --location="global" \
              --description="DESCRIPTION" \
              --display-name="DISPLAY_NAME"
                        

Replace the following: 

        * `POOL_ID`: The unique ID for the pool.
        * `DISPLAY_NAME`: (Optional) The name of the pool.
        * `DESCRIPTION`: (Optional) A description of the pool that you choose. This description appears when you grant access to pool identities.

For example:
    
    gcloud iam workload-identity-pools create my-wi-pool --display-name="My workload pool" --description="My workload pool description"

     4. Add the cluster as a workload identity pool provider. Choose the command to create the provider depending on whether your OIDC issuer is **publicly accessible** or **not publicly accessible** : 

### Publicly accessible

If your OIDC issuer is publicly accessible, create the provider with the following command: 
            
            gcloud iam workload-identity-pools providers create-oidc WORKLOAD_PROVIDER_ID \
              --location="global" \
              --workload-identity-pool="POOL_ID" \
              --issuer-uri="ISSUER" \
              --attribute-mapping="google.subject=assertion.sub"

### Not publicly accessible

If your OIDC issuer is not publicly accessible, create the provider with the following command: 
            
            gcloud iam workload-identity-pools providers create-oidc WORKLOAD_PROVIDER_ID \
              --location="global" \
              --workload-identity-pool="POOL_ID" \
              --issuer-uri="ISSUER" \
              --jwks-file="cluster-jwks.json" \
              --attribute-mapping="google.subject=assertion.sub"

**Note:** If you rotate your keys, you must [upload the new JWKS](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#manage-oidc-keys) with each key rotation. 

The command doesn't validate the cluster's JWKS. If the JWKS is malformed or expired, subsequent authentication attempts might fail with an error message `Error connecting to the given credential's issuer`.

Replace the following: 

        * `WORKLOAD_PROVIDER_ID`: A unique workload identity pool provider ID of your choice.
        * `POOL_ID`: The workload identity pool ID that you created earlier.
        * `ISSUER`: Use the issuer URL you determined earlier for the issuer URI . 

`attribute-mapping="google.subject=assertion.sub"` maps the Kubernetes subject to the IAM subject. 




###  Create the credential configuration files 

To deploy a Kubernetes workload that can access Google Cloud resources, You first need to create a credential configuration file for each IAM service account: 

  1. List the **IAM service accounts** (_also called "Google service accounts"_) with the following command: 
         
         gcloud iam service-accounts list --project PROJECT_ID

**Note:** You most likely have already created the IAM service accounts (also called "Google service accounts") during initial installation of Apigee hybrid with the [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/create-service-account) tool. See [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-about#recommended-sas) for a list of IAM service accounts needed by Apigee hybrid. See [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts) for the installation guide procedure to create the IAM service accounts. 

You will need to create the credential configuration files for the following IAM service accounts: 

###  Prod 

For production environments:
         
         DISPLAY NAME          EMAIL                                                       DISABLED
         apigee-cassandra      apigee-cassandra@my_project_id.iam.gserviceaccount.com      False
         apigee-guardrails     apigee-guardrails@my_project_id.iam.gserviceaccount.com     False
         apigee-mart           apigee-mart@my_project_id.iam.gserviceaccount.com           False
         apigee-metrics        apigee-metrics@my_project_id.iam.gserviceaccount.com        False
         apigee-runtime        apigee-runtime@my_project_id.iam.gserviceaccount.com        False
         apigee-synchronizer   apigee-synchronizer@my_project_id.iam.gserviceaccount.com   False
         apigee-watcher        apigee-watcher@my_project_id.iam.gserviceaccount.com        False
         

If you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid), you will also need to create the credential configuration file for the `apigee-mint-task-scheduler` service account.
         
         DISPLAY NAME                 EMAIL                                                              DISABLED
         ...
         apigee-mint-task-scheduler   apigee-mint-task-scheduler@my_project_id.iam.gserviceaccount.com   False
         ...

###  Non-prod 

For non-production environments:
         
         DISPLAY NAME         EMAIL                                                      DISABLED
         apigee-non-prod      apigee-non-prod@my-project.iam.gserviceaccount.com      False
         

**Tip:** If you have custom names for your service accounts that do not correspond easily with the names of the Apigee components, you can determine the role of each service account by checking the roles assigned to it and comparing the roles with the roles recommended in [**About service accounts**](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-about#recommended-sas). 

Use the following command to check the roles assigned to a service account:
         
         gcloud projects get-iam-policy PROJECT_ID  \
           --flatten="bindings[].members" \
           --format='table(bindings.role)' \
           --filter="SERVICE_ACCOUNT_NAME"

Note which custom service account corresponds to each IAM SA listed in the previous list.

  2. Create a credential configuration file for each IAM service account in the previous list. You will need these credential configuration files to configure Apigee hybrid to use Workload Identity Federation: 

###  Code 
         
         gcloud iam workload-identity-pools create-cred-config \
           projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
           --service-account=SERVICE_ACCOUNT_EMAIL \
           --credential-source-file=/var/run/service-account/token \
           --credential-source-type=text \
           --output-file=SERVICE_ACCOUNT_NAME-credential-configuration.json
           

###  Example 
         
         gcloud iam workload-identity-pools create-cred-config \
           projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider \
           --service-account=apigee-cassandra@myhybridporg.iam.gserviceaccount.com \
           --credential-source-file=/var/run/service-account/token \
           --credential-source-type=text \
           --output-file=apigee-cassandra-credential-configuration.json
           

Where: 

     * `PROJECT_NUMBER`: The project number of the project containing the workload identity pool. This must be the project number instead of the project ID. **Tip:** You can find the project number by using the following command: 
           
           gcloud projects describe PROJECT_ID --format="value(projectNumber)"

     * `POOL_ID`: The ID of the workload identity pool 
     * `WORKLOAD_PROVIDER_ID`: The ID of the workload identity pool provider
     * `SERVICE_ACCOUNT_EMAIL`: Email address of the service account, if you configured your Kubernetes ServiceAccount to use IAM service account impersonation. 
**Important:** `credential-source-type` must be set to `text`. **Note:** Do not create a credential configuration file for the `apigee-logger` service account. 

The credential configuration file lets the [Cloud Client Libraries](/apis/docs/cloud-client-libraries), the gcloud CLI, and Terraform determine the following: 

     * Where to obtain external credentials from
     * Which workload identity pool and provider to use
     * Which service account to impersonate
**Note:** Unlike a [service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys), a credential configuration file doesn't contain a private key and doesn't need to be kept confidential. Details about the credential configuration file are available at <https://google.aip.dev/auth/4117>. 



###  Configure Apigee hybrid to use Workload Identity Federation 

**Tip:** You can configure your hybrid installation to use Workload Identity Federation for any or all components. For example UDCA can use Workload Identity Federation while Synchronizer uses Google IAM service accounts or vice versa. 

  1. Copy or move each output file (`SERVICE_ACCOUNT_NAME-credential-configuration.json`) into the following chart directories (or subdirectories thereof). These were the files you created in the Create the credential configuration files step. 

### Prod

Service account | Apigee Helm chart directory  
---|---  
`apigee-cassandra` | `apigee-datastore/`  
`apigee-guardrails` | `apigee-operator/`  
`apigee-mart` | `apigee-org/`  
`apigee-metrics` | `apigee-telemetry/`  
`apigee-mint-task-scheduler`  
(If using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)) | `apigee-org/`  
`apigee-runtime` | `apigee-env/`  
`apigee-synchronizer` | `apigee-env/`  
`apigee-watcher` | `apigee-org/`  
  
### Non-prod

Service account | Apigee Helm chart  
---|---  
`apigee-non-prod` | `apigee-operator/`  
`apigee-datastore/`  
`apigee-telemetry/`  
`apigee-org/`  
`apigee-env/`  
  2. Make the following global changes to your cluster's overrides file: 

### Code
         
         gcp:
           workloadIdentity:
             enabled: **false** # must be set to false to use Workload Identity Federation
           federatedWorkloadIdentity:
             enabled: **true**
             audience: "AUDIENCE"
             credentialSourceFile: "/var/run/service-account/token"
         

### Example
         
         gcp:
           workloadIdentity:
             enabled: false
           federatedWorkloadIdentity:
             enabled: true
             audience: "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider"
             credentialSourceFile: "/var/run/service-account/token"
         

**Note:** See 
     * [`gcp.workloadIdentity.enabled`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-workloadidentity-enabled)
     * [`gcp.federatedWorkloadIdentity.enabled`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-enabled)
     * [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-audience)
     * [`gcp.federatedworkloadIdentity.credentialSourceFile`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-credentialsourcefile)

Where: AUDIENCE is the allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. 

For example, in the following sample `apigee-udca-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider",
      "subject_token_type": "urn:ietf:params:oauth: token-type:jwt",
      "token_url": "https://sts.googleapis.com/v1/token",
      "service
      "impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/apigee-udca@my-project.iam.gserviceaccount.com:generateAccessToken",
      "credential_source": {
        "file": "/var/run/service-account/token",
        "format": {
          "type": "text"
        }
      }
    }

The audience value is `//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider`.

  3. Configure the overrides for each component using Workload Identity Federation. Select the instructions for JSON files, Kubernetes secrets, or Vault as appropriate for your installation. 

### Cert file

Replace the value of `serviceAccountPath` with the credential source file for the corresponding IAM service account. This must be the path relative to the chart directory. For example:
         
         envs:
         - name: ENVIRONMENT_NAME
           serviceAccountPaths:
             synchronizer: apigee-synchronizer-credential-configuration.json
             runtime: apigee-runtime-credential-configuration.json
         
         guardrails:
           serviceAccountPath: apigee-guardrails-credential-configuration.json
         
         mart:
           serviceAccountPath: apigee-mart-credential-configuration.json
         
         connectAgent:
           serviceAccountPath: apigee-mart-credential-configuration.json
         
         metrics:
           serviceAccountPath: apigee-metrics-credential-configuration.json
         
         mintTaskScheduler: # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)
           serviceAccountPath: apigee-mint-task-scheduler-credential-configuration.json
         
         watcher:
           serviceAccountPath: apigee-watcher-credential-configuration.json
         

### K8s Secret

     1. Create a new Kubernetes secret using the credential source file for each credential configuration file. 
            
            kubectl create secret -n APIGEE_NAMESPACE generic SECRET_NAME --from-file="client_secret.json=CREDENTIAL_CONFIGURATION_FILE"

For example:
            
            kubectl create secret -n apigee generic synchronizer-workload-identity-secret --from-file="client_secret.json=./apigee-synchronizer-credential-configuration.json"

     2. Replace the value of `serviceAccountRef` with the new secret. For example: 
            
            envs:
            - name: ENVIRONMENT_NAME
              serviceAccountRefs:
                **runtime: runtime-workload-identity-secret**
                **synchronizer: synchronizer-workload-identity-secret**
            

### Vault

Update the service account key, `SAKEY` for each service account in Vault with the corresponding credential source file. The procedure is similar for all components. For example, for Synchronizer: 
    
    SAKEY=$(cat .apigee-synchronizer-credential-configuration.json); kubectl -n APIGEE_NAMESPACE exec vault-0 -- vault kv patch secret/apigee/orgsakeys synchronizer="$SAKEY"

See [`Storing service account keys in Hashicorp Vault`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-vault) for more information.

  4. Apply the changes to each affected component with the `helm upgrade` command: 

If you updated the Vault service account keys, update the `apigee-operator` chart. 
         
         helm upgrade operator apigee-operator/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         

Update the rest of the affected charts in the following order: 
         
         helm upgrade datastore apigee-datastore/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         
         
         helm upgrade telemetry apigee-telemetry/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         
         
         helm upgrade $ORG_NAME apigee-org/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         

Update the `apigee-env` chart for each env, replacing $ENV_RELEASE_NAME abdENV_NAME each time: 
         
         helm upgrade $ENV_RELEASE_NAME apigee-env/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           --set env=$ENV_NAME \
           -f overrides.yaml
         

See the [Apigee hybrid Helm reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/helm-reference) for a list of components and their corresponding charts.




### Grant the access to the Kubernetes service accounts

  1. List the **Kubernetes service accounts** with the following command: 
         
         kubectl get sa -n APIGEE_NAMESPACE

**Note:** The Apigee hybrid charts created the necessary Kubernetes service accounts for each component when you ran the `helm upgrade` commands. **Important:** You will not be using every Kubernetes service account that is listed by this command. 
  2. Grant the Kubernetes service accounts access to impersonate the associated IAM service accounts as shown in the following table. The table shows the default Apigee IAM service account names. If you are using custom service account names, use the corresponding IAM service accounts: Kubernetes service accounts | IAM service account  
---|---  
**Org-level Kubernetes service accounts**  
`apigee-connect-agent-ORG_NAME-ORG_HASH_ID` | `apigee-mart`  
`apigee-operator-guardrails-sa` | `apigee-guardrails`  
`apigee-mart-ORG_NAME-ORG_HASH_ID` | `apigee-mart`  
`apigee-metrics-apigee-telemetry` | `apigee-metrics`  
`apigee-open-telemetry-collector-apigee-telemetry` | `apigee-metrics`  
`apigee-mint-task-scheduler-ORG_NAME-ORG_HASH_ID`  
(If using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)) | `apigee-mint-task-scheduler`  
`apigee-watcher-ORG_NAME-ORG_HASH_ID` | `apigee-watcher`  
**Env-level Kubernetes service accounts**  
`apigee-runtime-ORG_NAME-ENV_NAME-ENV_HASH_ID` | `apigee-runtime`  
`apigee-synchronizer-ORG_NAME-ENV_NAME-ENV_HASH_ID` | `apigee-synchronizer`  
**Cassandra backup and restore (if enabled)**  
`apigee-cassandra-backup-sa` | `apigee-cassandra`  
`apigee-cassandra-restore-sa` | `apigee-cassandra`  
  
Where:

     * `ORG_NAME`: The first 15 characters of the name of your organization.
     * `ORG_HASH_ID`: A unique hash ID of your full organization name.
     * `ENV_NAME`: The first 15 characters of the name of your environment.
     * `ENV_HASH_ID`: A unique hash ID of your organization and environment names.

For example: 

     * `apigee-connect-agent-myhybridorg-123abcd`
     * `apigee-runtime-myhybridorg-prodenv-234bcde`
**Important:** You will need to repeat this step for each environment. 

Grant each Kubernetes service account access to impersonate the appropriate IAM service account with the following command:
    
    gcloud iam service-accounts add-iam-policy-binding \
      IAM_SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
        --role=roles/iam.workloadIdentityUser

Where:

     * `IAM_SA_NAME`: the name of the service account.
     * `PROJECT_ID`: the ID of the project that is associated with the Apigee Org.
     * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project where you created the workload identity pool.
     * `POOL_ID`: the workload identity pool ID.
     * `MAPPED_SUBJECT`: the Kubernetes ServiceAccount from the claim in your ID token that you mapped to `google.subject`. For example, if you mapped `google.subject=assertions.sub` and your ID token contains `"sub": "system:serviceaccount:default:my-kubernetes-serviceaccount"`, then `MAPPED_SUBJECT` is `system:serviceaccount:default:my-kubernetes-serviceaccount`. 
**Note:** You must use the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) in the member identifier. Using the project ID is not supported. 



For more information about Workload Identity Federation and best practices, see [Best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
