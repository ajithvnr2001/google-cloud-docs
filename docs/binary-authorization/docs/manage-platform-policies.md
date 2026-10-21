---
url: https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies/
title: Manage CV platform policies \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:14.016966+00:00
---

# Manage CV platform policies  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Manage CV platform policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Manage platform policies

This section describes how to manage [CV platform policies](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#platform-policies).

### Create a platform policy

This section shows you how to create a platform policy.

Before using any of the command data below, make the following replacements: 

  * POLICY_ID: A platform policy ID of your choice. If the policy is in another project, you can use the full resource name: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`.
  * POLICY_PATH: A path to the policy file.
  * POLICY_PROJECT_ID: The policy project ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy create POLICY_ID \
        --platform=gke \
        --policy-file=POLICY_PATH \
        --project=POLICY_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy create POLICY_ID `
        --platform=gke `
        --policy-file=POLICY_PATH `
        --project=POLICY_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy create POLICY_ID ^
        --platform=gke ^
        --policy-file=POLICY_PATH ^
        --project=POLICY_PROJECT_ID

### List a CV platform policy

This section shows you how to list platform policies.

Before using any of the command data below, make the following replacements: 

  * `POLICY_PROJECT_ID`: the ID of the project that contains the policies to list



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy list gke \
        --project=POLICY_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy list gke `
        --project=POLICY_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy list gke ^
        --project=POLICY_PROJECT_ID

### Describe a CV platform policy

This section shows you how to describe a platform policy project.

Before using any of the command data below, make the following replacements: 

  * `POLICY_PROJECT_ID`: the ID of the project that contains the policy
  * `POLICY_ID`: the platform policy ID. If the policy is in another project, you can use the full resource name: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy describe POLICY_ID \
        --project=POLICY_PROJECT_ID \
        --platform=gke 

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy describe POLICY_ID `
        --project=POLICY_PROJECT_ID `
        --platform=gke 

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy describe POLICY_ID ^
        --project=POLICY_PROJECT_ID ^
        --platform=gke 

### Update a CV platform policy

This section shows you how to update a platform policy.

Before using any of the command data below, make the following replacements: 

  * POLICY_ID: a platform policy ID. If the policy is in another project, you can use the full resource name: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`.
  * POLICY_PROJECT_ID: the policy project ID
  * POLICY_PATH: a path to the updated policy file



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy update POLICY_ID \
      --policy-file=POLICY_PATH \
      --platform=gke \
      --project=POLICY_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy update POLICY_ID `
      --policy-file=POLICY_PATH `
      --platform=gke `
      --project=POLICY_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy update POLICY_ID ^
      --policy-file=POLICY_PATH ^
      --platform=gke ^
      --project=POLICY_PROJECT_ID

### Delete a CV platform policy

This section shows you how to delete a platform policy.

Before using any of the command data below, make the following replacements: 

  * `POLICY_ID`: The ID of the local platform policy. If the policy is in another project, you can use the full resource name: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`.
  * POLICY_PROJECT_ID: the policy project ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy delete POLICY_ID  \
        --platform=gke \
        --project=POLICY_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy delete POLICY_ID  `
        --platform=gke `
        --project=POLICY_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy delete POLICY_ID  ^
        --platform=gke ^
        --project=POLICY_PROJECT_ID

## Manage GKE clusters with CV policies

This section shows you how to enable CV with platform policies for GKE.

### Update cluster to use only CV monitoring

This section shows you how to update a cluster to use only CV platform policy-based monitoring. If this cluster already has a project-singleton policy enforcement enabled, running this command disables it. Instead, consider updating the cluster with enforcement and CV monitoring enabled.

Before using any of the command data below, make the following replacements: 

  * `CLUSTER_NAME`: the cluster name
  * `LOCATION`: the location—for example: `us-central1` or `asia-south1`
  * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored
  * `POLICY_ID`: the policy ID
  * `CLUSTER_PROJECT_ID`: the cluster project ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --binauthz-evaluation-mode=POLICY_BINDINGS \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID \
        --project=CLUSTER_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters update CLUSTER_NAME `
        --location=LOCATION `
        --binauthz-evaluation-mode=POLICY_BINDINGS `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID `
        --project=CLUSTER_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters update CLUSTER_NAME ^
        --location=LOCATION ^
        --binauthz-evaluation-mode=POLICY_BINDINGS ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID ^
        --project=CLUSTER_PROJECT_ID

### Update a cluster to use Binary Authorization enforcement with CV monitoring

This section shows you how to update a cluster to use both project-singleton policy enforcement and CV platform policy-based monitoring.

Before using any of the command data below, make the following replacements: 

  * `CLUSTER_NAME`: a cluster name
  * `LOCATION`: the location—for example: `us-central1` or `asia-south1`
  * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored
  * `POLICY_ID`: the policy ID
  * `CLUSTER_PROJECT_ID`: the cluster project ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID \
        --project=CLUSTER_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters update CLUSTER_NAME `
        --location=LOCATION `
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID `
        --project=CLUSTER_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters update CLUSTER_NAME ^
        --location=LOCATION ^
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID ^
        --project=CLUSTER_PROJECT_ID

### Disable CV

You can enable CV on a GKE cluster that also uses Binary Authorization and the project-singleton policy for enforcement.

If this is the case and you want to disable only CV, run the following command:

Before using any of the command data below, make the following replacements: 

  * `CLUSTER_NAME`: a cluster name
  * `LOCATION`: the location—for example: `us-central1` or `asia-south1`
  * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored
  * `POLICY_ID`: the policy ID
  * `CLUSTER_PROJECT_ID`: the cluster project ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID \
        --project=CLUSTER_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters update CLUSTER_NAME `
        --location=LOCATION `
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID `
        --project=CLUSTER_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters update CLUSTER_NAME ^
        --location=LOCATION ^
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID ^
        --project=CLUSTER_PROJECT_ID

## What's next

  * [Use the image freshness check](https://docs.cloud.google.com/binary-authorization/docs/cv-freshness-check)
  * [Use the simple signing attestation check](https://docs.cloud.google.com/binary-authorization/docs/cv-attestation-check)
  * [Use the Sigstore signature check](https://docs.cloud.google.com/binary-authorization/docs/cv-sigstore-check)
  * [Use the SLSA check](https://docs.cloud.google.com/binary-authorization/docs/cv-slsa-check)
  * [Use the trusted directory check](https://docs.cloud.google.com/binary-authorization/docs/cv-trusted-directory-check)
  * [Use the vulnerability check](https://docs.cloud.google.com/binary-authorization/docs/cv-vulnerability-check)
  * [View CV logs](https://docs.cloud.google.com/binary-authorization/docs/cv-view-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
