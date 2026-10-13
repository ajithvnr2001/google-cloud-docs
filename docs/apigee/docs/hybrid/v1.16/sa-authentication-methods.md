---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-authentication-methods/
title: Service account authentication methods in Apigee hybrid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:03.874959+00:00
---

# Service account authentication methods in Apigee hybrid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-authentication-methods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Service account authentication methods in Apigee hybrid Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-authentication-methods.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-authentication-methods.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/sa-authentication-methods.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/sa-authentication-methods.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/sa-authentication-methods.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/sa-authentication-methods.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/sa-authentication-methods.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/sa-authentication-methods.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/sa-authentication-methods.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/sa-authentication-methods.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/sa-authentication-methods.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/sa-authentication-methods.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/sa-authentication-methods.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/sa-authentication-methods.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/sa-authentication-methods.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/sa-authentication-methods.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/sa-authentication-methods.html)



## Choosing service account authentication methods in Apigee hybrid

Apigee hybrid requires service accounts for secure communication with Google Cloud services. Choose an authentication method for these service accounts that aligns with your security and operational requirements. This guide provides a brief overview of the available options. 

## Understand service account authentication

Apigee hybrid uses Google Cloud service accounts to authenticate and authorize components running in your Kubernetes cluster. These service accounts access Google Cloud resources, such as Cloud Storage buckets and Cloud Logging. Each service account requires specific Identity and Access Management (IAM) roles to perform its functions. 

  * Learn more about Google Cloud Identity and Access Management service accounts: [Service accounts overview](https://docs.cloud.google.com/iam/docs/service-account-overview). 
  * Learn more about service accounts in Apigee hybrid: [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about). 



## Authentication Method Options

Apigee hybrid supports several methods for authenticating service accounts. Each method manages service account keys differently, offering various levels of security and operational complexity. Consider your platform, security posture, and existing infrastructure when selecting a method. 

The following table summarizes the available authentication methods: 

Method | Key Storage Location | Platform Compatibility | Key Management  
---|---|---|---  
Kubernetes secrets | Kubernetes cluster secrets | Any Kubernetes platform | Kubernetes manages secrets, manual rotation  
Service account JSON key files | Local file system | Any Kubernetes platform | Manual rotation and distribution  
Vault | HashiCorp Vault | Any Kubernetes platform | Vault manages secrets, manual rotation  
Workload Identity Federation for GKE | Google Cloud IAM | Google Kubernetes Engine (GKE) | Google Cloud manages, no key files needed  
Workload Identity Federation on other platforms | Google Cloud IAM | AKS, EKS, OpenShift, or other Kubernetes platforms | Google Cloud manages, no key files needed  
  
### Store service account keys in Kubernetes secrets

Store service account keys as Kubernetes secrets within your cluster. This method leverages the built-in secret management capabilities in Kubernetes. Kubernetes secrets can provide a more secure way to manage keys than direct file storage. You still manage key rotation manually.

Hybrid components reference these secrets using the `serviceAccountRef` and `envs[].serviceAccountRefs` properties in the `overrides.yaml` file. Kubernetes manages the distribution of these secrets to the appropriate pods. 

For example:
    
    
    logger:
      serviceAccountRef: "my-project-apigee-logger-key"

To use this method, see [Store service account keys in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-k8s-secrets).

### Service account JSON key files

This method involves creating a JSON key file for each service account and storing these files directly on a file system. This approach offers simplicity for initial setup. However, it requires ensuring the security of the file system. Key rotation is manual. 

Place each service account's private key JSON file in a directory accessible by the Apigee hybrid components. Reference the path to these files in your `overrides.yaml` configuration using the `serviceAccountPath` and `envs[].serviceAccountPaths` properties. 

For example:
    
    
    logger:
      serviceAccountPath: "my-project-apigee-logger.json"

You can generate and download the service account key files using the `create-service-account` tool provided with Apigee hybrid. For more information, see [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/create-service-account).

### Store service account keys in Vault

Integrate HashiCorp Vault to manage your service account keys. Vault provides a robust solution for secret management, offering features like dynamic secret generation, auditing, and automated key rotation. It requires setting up and maintaining a Vault instance.

You will need to create separate Vault secrets, policies, and roles for the org-level and env-level components. You reference these secrets in your `overrides.yaml` configuration using the `serviceAccountSecretProviderClass` and `envs[].serviceAccountSecretProviderClass` properties. 

For example:
    
    
    serviceAccountSecretProviderClass: apigee-orgsakeys-spc
    
    envs:
    - name: my-env
      serviceAccountSecretProviderClass: apigee-envsakeys-my-env-spc

See [Store service account keys in Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-vault).

### Workload Identity Federation for GKE

Workload Identity Federation for GKE allows Kubernetes service accounts to act as Google Cloud service accounts. This method eliminates the need for service account key files entirely. Instead, your GKE cluster directly authenticates workloads using Google Cloud IAM. Workload Identity Federation for GKE provides a highly secure and automated authentication mechanism, simplifying key management. This method is specific to GKE clusters.

This method requires binding each Kubernetes service account to a specific Google Cloud service account. The Apigee hybrid installation process creates the Kubernetes service accounts specific to your installation when you install the Apigee hybrid Helm charts. When you run the `helm install` or `helm upgrade` command with the `--dry-run` flag for each chart, the output will include the commands to bind the Kubernetes service accounts to the Google Cloud service accounts for the specific Apigee hybrid component in that chart. 

You enable Workload Identity Federation for GKE in your overrides.yaml file with the `gcp.workloadIdentity.enabled` property. 

For example:
    
    
    gcp:
      projectID: my-project
      region: us-west1
      workloadIdentity:
        enabled: true

See [Enable Workload Identity Federation for GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke).

### Workload Identity Federation on platforms other than GKE

Workload Identity Federation extends the benefits of Workload Identity Federation for GKE to Kubernetes clusters running outside of Google Cloud, such as Azure Kubernetes Service (AKS), Amazon Elastic Kubernetes Service (EKS), or OpenShift. This method allows your non-GKE cluster to authenticate to Google Cloud using your cluster's OIDC provider to configure a trust relationship between your cluster's identity provider and Google Cloud. After initial setup, this method eliminates the need for service account key files.

You can use Workload Identity Federation with: 

  * Credential configuration files (in place of service account key files)
  * Kubernetes secrets
  * Vault



To use Workload Identity Federation you create credential configuration files for each Google Cloud service account. You use these files in place of service account key files or to set up the Kubernetes secrets or Vault if you are using those methods.

You enable Workload Identity Federation in your overrides.yaml file with the `gcp.federatedWorkloadIdentity.enabled`, `gcp.federatedWorkloadIdentity.audience`, and `gcp.federatedWorkloadIdentity.credentialSourceFile` properties. 

For example:
    
    
    gcp:
      projectID: my-project
      region: us-west1
      federatedWorkloadIdentity:
        enabled: true
        audience: "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider"
        credentialSourceFile: "/var/run/service-account/token"

See [Enable Workload Identity Federation](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).

## Choose an Authentication Method

Select an authentication method based on your deployment environment and security requirements.

  * **For GKE deployments** , Workload Identity Federation for GKE offers a secure and streamlined approach. It removes the need to manage service account key files directly.
  * **For non-GKE Kubernetes deployments** (AKS, EKS, OpenShift), Workload Identity Federation provides a similar keyless authentication experience. This method is the recommended choice for these environments.
  * **If Workload Identity Federation for GKE or Workload Identity Federation are not options** , consider using Vault for centralized key management and automation.
  * **For simpler deployments or if you lack a Vault setup** , storing keys in Kubernetes secrets provides a native Kubernetes solution. This method offers better security than direct file storage.
  * **Direct service account key files** are suitable for initial testing or environments where other methods are not feasible. However, this method requires careful manual key management and rotation.



## What's next

  * Continue planning and preparing: [Secure ports usage](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/ports).
  * Learn more about service accounts in Apigee hybrid: [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about).
  * Install Apigee hybrid: [Part 1, Project and org setup: Overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
