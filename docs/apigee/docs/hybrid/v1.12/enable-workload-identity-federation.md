---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/enable-workload-identity-federation/
title: Enabling Workload Identity Federation on AKS and EKS \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:04:22.473936+00:00
---

# Enabling Workload Identity Federation on AKS and EKS  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/enable-workload-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enabling Workload Identity Federation on AKS and EKS Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

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



This topic explains how to enable Workload Identity for Apigee hybrid installations on **AKS** and **EKS** platforms. 

## Overview

Workload identity federation lets applications running outside Google Cloud impersonate a Google Cloud Platform service account by using credentials from an external identity provider. 

Using workload identity federation can help you improve security by letting applications use the authentication mechanisms that the external environment provides and can help [replace service account keys](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#using_service_accounts). 

For an overview, see [Best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation). 

**Note:** The `apige-logger` component does not support Workload Identity Federation. See the [known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues#hybrid-apigee-logger-wif).

##  Set up Workload Identity Federation 

To use Workload Identity Federation with Apigee hybrid, first configure you cluster and then apply the feature to your Apigee hybrid installation. 

###  Configure your cluster to use Workload Identity Federation. 

Follow the Google Cloud instructions to [Configure Workload Identity Federation for Kubernetes](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes), with the following modifications:

  * List your IAM service accounts and Kubernetes service accounts with the following commands: 
    * **IAM service accounts:** You most likely have already created the IAM service accounts (also called "Google service accounts") during initial installation of Apigee hybrid with the [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/create-service-account) tool. See [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/sa-about#recommended-sas) for a list of IAM service accounts needed by Apigee hybrid. 

You can see a list of IAM service accounts in your project with the following command: 
          
          gcloud iam service-accounts list --project PROJECT_ID

    * **Kubernetes service accounts:** The Apigee hybrid charts create the necessary Kubernetes service accounts for each component when you run the `helm install` or `helm update` command. 

You can see the Kubernetes service accounts in your cluster with the `kubectl get sa` commands: 
          
          kubectl get sa -n APIGEE_NAMESPACE
          kubectl get sa -n apigee-system

  * In the step [Configure Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes#configure), the default audience for created Workload Identity pools and providers is as follows. Use this default or set a custom expected audience, and save this value for later use. 
        
        https://iam.googleapis.com/projects/PROJECT_NUM/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID

  * Stop after **step 1** under [Deploy a Kubernetes workload](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes#deploy). There will be one credential configuration file for each Google service account. Save each credential configuration file and save the path entered for the `--credential-source-file` parameter, for example: `/var/run/service-account/token`. **Tip:** You can also find the values for `audience` and `credentialSourceFile` in the credential configuration json file, under the paths `.audience` and `.credential_source.file` respectively. You will need these values for the overrides file to configure Apigee hybrid. 



###  Configure Apigee hybrid to use Workload Identity Federation 

**Tip:** You can configure your hybrid installation to use Workload Identity Federation for any or all components. For example UDCA can use Workload Identity Federation while Synchronizer uses Google IAM service accounts or vice versa. 

  1. Copy the credential source file and the output file (`credential-configuration.json`) into the following chart directories. These were the values you provided in **step 1** under [Deploy a Kubernetes workload](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes#deploy). 
     * `apigee-datastore/`
     * `apigee-env`
     * `apigee-org/`
     * `apigee-telemetry/`
**Tip:** You can use a subdirectory for these files, for example: `apigee-datastore/fwi/`
  2. Make the following global changes to your cluster's overrides file: 
         
         gcp:
           workloadIdentity:
             enabled: **false** # must be set to false to use Workload Identity Federation
           federatedWorkloadIdentity:
             enabled: **true**
             audience: "AUDIENCE"
             credentialSourceFile: "CREDENTIAL_SOURCE_FILE"
         

Where: 

     * AUDIENCE is the allowed audience of the Workload Identity Provider, the value under `.audience` in the credential configuration json file you configured in **step 1** under [Deploy a Kubernetes workload](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes#deploy). 
     * CREDENTIAL_SOURCE_FILE is the filename and path to the credential source file used by Workload Identity Federation to obtain the credentials for the service accounts. This is the value you provide for `credential-source-file` when you configure Workload Identity Federation with the `create-cred-config` command in **step 1** under [Deploy a Kubernetes workload](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes#deploy). For example: 

For example:
    
    gcp:
      workloadIdentity:
        enabled: false
      federatedWorkloadIdentity:
        enabled: true
        audience: "//iam.googleapis.com/projects/123456789012/locations/global/workloadIdentityPools/aws-pool/providers/aws-provider"
        credentialSourceFile: "/var/run/service-account/token"
    

  3. Configure the overrides for each component using Workload Identity Federation. Select the instructions for cert files, Kubernetes secrets, or Vault as appropriate for your installation. 

### Cert file

Replace the value of `serviceAccountPath` with the credential source file. This must be the path relative to the chart directory. For example:
         
         udca:
           serviceAccountPath: fwi/credential-configuration.json
         

### K8s Secret

     1. Create a new Kubernetes secret using for the credential source file. 
            
            kubectl create secret -n apigee generic SECRET_NAME --from-file="client_secret.json=CREDENTIAL_CONFIGURATION_FILE"

For example:
            
            kubectl create secret -n apigee generic udca-fwi-secret --from-file="client_secret.json=./fwi/credential-configuration.json"

     2. Replace the value of `serviceAccountRef` with the new secret. For example: 
            
            udca:
              serviceAccountRef: udca-fwi-secret
            

### Vault

Update the service account key, `SAKEY` in Vault with the credential source file. For example, for UDCA (the procedure is similar for all components): 
    
    SAKEY=$(cat ./fwi/credential-configuration.json); kubectl -n apigee exec vault-0 -- vault kv patch secret/apigee/orgsakeys udca="$SAKEY"

  4. Apply the changes to each affected component with the `helm update` command: 

If you are using Vault for the first time with this cluster, update the `apigee-operator` chart: 
         
         helm upgrade operator apigee-operator/ \
           --namespace apigee-system \
           --atomic \
           -f overrides.yaml
         

Update the rest of the affected charts in the following order: 
         
         helm upgrade datastore apigee-datastore/ \
           --namespace apigee \
           --atomic \
           -f overrides.yaml
         
         
         helm upgrade telemetry apigee-telemetry/ \
           --namespace apigee \
           --atomic \
           -f overrides.yaml
         
         
         helm upgrade $ORG_NAME apigee-org/ \
           --namespace apigee \
           --atomic \
           -f overrides.yaml
         

Update the `apigee-env` chart for each env, replacing ENV_NAME each time: 
         
         helm upgrade $ENV_NAME apigee-env/ \
           --namespace apigee \
           --atomic \
           --set env=$ENV_NAME \
           -f overrides.yaml
         

See the [Apigee hybrid Helm reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/helm-reference) for a list of components and their corresponding charts.




For more information about Workload Identity Federation and best practices, see [Best practices for using workload identity federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
