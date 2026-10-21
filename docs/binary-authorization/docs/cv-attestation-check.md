---
url: https://docs.cloud.google.com/binary-authorization/docs/cv-attestation-check/
title: Use the simple signing attestation check \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:11:10.463158+00:00
---

# Use the simple signing attestation check  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/cv-attestation-check/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Use the simple signing attestation check Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to use the Binary Authorization continuous validation (CV) [simple signing attestation check](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#simple-signing-check). The check verifies the attestations of container images associated with Pods running in a Google Kubernetes Engine (GKE) cluster where CV is enabled.

## Costs

This guide uses the following Google Cloud services:

  * Binary Authorization, but CV is available free of charge during the [Preview](https://cloud.google.com/products/#product-launch-stages) stage
  * GKE
  * Cloud Key Management Service



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
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

  7. Enable the Binary Authorization, Cloud Key Management Service, Google Kubernetes Engine APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable binaryauthorization.googleapis.com cloudkms.googleapis.com container.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
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

  13. Enable the Binary Authorization, Cloud Key Management Service, Google Kubernetes Engine APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable binaryauthorization.googleapis.com cloudkms.googleapis.com container.googleapis.com

  14. Ensure that the gcloud CLI is updated to the latest version.
  15. [Install the `kubectl` command-line tool.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
  16. If your Binary Authorization policies and GKE clusters are in different projects, make sure that Binary Authorization is enabled in both projects.



## Required roles

This section shows you how to set roles for this check.

### Overview

If you run all of the products that are mentioned in this guide in the same project, you don't need to set any permissions. Binary Authorization configures the roles correctly when you enable it. If you run the products in different projects, you must set roles as described in this section.

To ensure that the Binary Authorization Service Agent in each project has the necessary permissions to evaluate the CV simple signing attestation check, ask your administrator to grant the following IAM roles to the Binary Authorization Service Agent in each project: 

**Important:** You must grant these roles to the Binary Authorization Service Agent in each project, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * If your cluster project is different from the policy project: [Binary Authorization Policy Evaluator ](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEvaluator) (`roles/binaryauthorization.policyEvaluator`) on the cluster project Binary Authorization Service Agent, for it to access the policy project 
  * If your attestation project is different from your policy project: [Container Analysis Occurrences Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`) on the policy project Binary Authorization Service Agent, for it to access the attestation project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Binary Authorization Service Agent in each project the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant roles using the gcloud CLI

To ensure that the Binary Authorization Service Agent in each project has the necessary permissions to evaluate the CV simple signing attestation check, grant the Binary Authorization Service Agent in each project the following IAM roles:

  1. Grant permission for the cluster project's Binary Authorization Service Agent to access the policy in the policy project.

     1. Get the cluster project's Binary Authorization service agent:
            
            PROJECT_NUMBER=$(gcloud projects list --filter="projectId:CLUSTER_PROJECT_ID" \
              --format="value(PROJECT_NUMBER)")
            CLUSTER_SERVICE_ACCOUNT="service-$PROJECT_NUMBER@gcp-sa-binaryauthorization.iam.gserviceaccount.com"
            

Replace `CLUSTER_PROJECT_ID` with the project ID of the cluster.

     2. Allow CV to evaluate the policy on the cluster:
            
            gcloud projects add-iam-policy-binding POLICY_PROJECT_ID \
                --member="serviceAccount:$CLUSTER_SERVICE_ACCOUNT" \
                --role='roles/binaryauthorization.policyEvaluator'
            

Replace `POLICY_PROJECT_ID` with the ID of the project that contains your policy.

  2. Allow the policy project Binary Authorization Service Agent to access the attestations in your attestation project:

     1. Obtain the policy project's Binary Authorization service agent:
            
            PROJECT_NUMBER=$(gcloud projects list \
              --filter="projectId:POLICY_PROJECT_ID" \
              --format="value(PROJECT_NUMBER)")
            SERVICE_ACCOUNT="service-$PROJECT_NUMBER@gcp-sa-binaryauthorization.iam.gserviceaccount.com"
            

Replace `POLICY_PROJECT_ID` with the ID of the project that contains your policy.

     2. Grant the role:
            
            gcloud projects add-iam-policy-binding ATTESTATION_PROJECT_ID \
                --member="serviceAccount:$SERVICE_ACCOUNT" \
                --role='roles/containeranalysis.occurrences.viewer'
            

Replace `ATTESTATION_PROJECT_ID` with the ID of the project that contains your attestations.




## Create a key pair

In this section, you create an [Elliptic Curve Digital Signature Algorithm (ECDSA)](https://docs.cloud.google.com/kms/docs/algorithms#asymmetric_signing_algorithms) asymmetric key pair.

You use the private key to sign the image, which creates the attestation. You include the public key in a platform policy. When CV checks the attestation, it uses the public key to verify the attestation.

You can use either [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/resource-hierarchy) or local keys, but we recommend that you use Cloud KMS keys for production.

###  PKIX Cloud KMS 

To create the key pair in Cloud KMS, do the following:

  1. Set up environment variables needed to create the key pair. To do so, we recommend that you fill in the placeholders in the following command, and then run the command.
         
         KMS_KEY_PROJECT_ID=KMS_KEY_PROJECT_ID
         KMS_KEYRING_NAME=KMS_KEYRING_NAME
         KMS_KEY_NAME=KMS_KEY_NAME
         KMS_KEY_LOCATION=global
         KMS_KEY_PURPOSE=asymmetric-signing
         KMS_KEY_ALGORITHM=ec-sign-p256-sha256
         KMS_PROTECTION_LEVEL=software
         KMS_KEY_VERSION=1
         KEY_FILE=KEY_FILE
         

Replace the following:

     * `KMS_KEY_PROJECT_ID`: your project ID
     * `KMS_KEYRING_NAME`: a name for your Cloud KMS key ring
     * `KMS_KEY_NAME`: a name for your Cloud KMS key
     * `KEY_FILE`: a local path to save your Cloud KMS key
  2. Create the key ring:
         
         gcloud kms keyrings create ${KMS_KEYRING_NAME} \
             --location=${KMS_KEY_LOCATION} \
             --project=${KMS_KEY_PROJECT_ID}
         

  3. Create the key:
         
         gcloud kms keys create ${KMS_KEY_NAME} \
             --location=${KMS_KEY_LOCATION} \
             --keyring=${KMS_KEYRING_NAME}  \
             --purpose=${KMS_KEY_PURPOSE} \
             --default-algorithm=${KMS_KEY_ALGORITHM} \
             --protection-level=${KMS_PROTECTION_LEVEL} \
             --project=${KMS_KEY_PROJECT_ID}
         

  4. Export the public key material to a file:
         
         gcloud kms keys versions get-public-key ${KMS_KEY_VERSION} \
             --key=${KMS_KEY_NAME} \
             --keyring=${KMS_KEYRING_NAME} \
             --location=${KMS_KEY_LOCATION} \
             --output-file=${KEY_FILE} \
             --project=${KMS_KEY_PROJECT_ID}
         




###  Local key 

**Warning:** We strongly recommend against using locally generated key pairs in production environments as they present a security risk. We recommend that you instead use Cloud Key Management Service. This example is provided for illustrative purposes only. 

To create the key pair locally, do the following:

  1. Create the private key:
         
         PRIVATE_KEY_FILE="/tmp/ec_private.pem"
         openssl ecparam -genkey -name prime256v1 -noout -out ${PRIVATE_KEY_FILE}
         

  2. Get the public key from the private key:
         
         PUBLIC_KEY_FILE="/tmp/ec_public.pem"
         openssl ec -in ${PRIVATE_KEY_FILE} -pubout -out ${PUBLIC_KEY_FILE}
         




## Create a platform policy

To create a CV platform policy with a simple signing attestation check, do the following:

  1. Create the simple signing attestation check platform policy YAML file:

###  PKIX Cloud KMS 
         
         cat > /tmp/my-policy.yaml << EOF
         gkePolicy:
           checkSets:
           - checks:
             - simpleSigningAttestationCheck:
                 containerAnalysisAttestationProjects:
                 - projects/ATTESTATION_PROJECT_ID
                 attestationAuthenticators:
                   pkixPublicKeySet:
                     pkixPublicKeys:
                       publicKeyPem: |
         $(awk '{printf "                %s\n", $0}' ${KEY_FILE})
                       signatureAlgorithm: ECDSA_P256_SHA256
                       keyId: |-
                         //cloudkms.googleapis.com/v1/projects/${KMS_KEY_PROJECT_ID}/locations/${KMS_KEY_LOCATION}/keyRings/${KMS_KEYRING_NAME}/cryptoKeys/${KMS_KEY_NAME}/cryptoKeyVersions/${KMS_KEY_VERSION}
         EOF
         

Replace `ATTESTATION_PROJECT_ID` with the ID of the project that stores attestations that are created using this Cloud KMS key.

###  Local key 
         
         cat > /tmp/my-policy.yaml <<EOF
         gkePolicy:
           checkSets:
           - checks:
             - simpleSigningAttestationCheck:
                 containerAnalysisAttestationProjects:
                 - projects/ATTESTATION_PROJECT_ID
                 attestationAuthenticators:
                   pkixPublicKeySet:
                     pkixPublicKeys:
                       publicKeyPem: |
         $(awk '{printf "                %s\n", $0}' /tmp/ec_public.pem)
                       signatureAlgorithm: ECDSA_P256_SHA256
                       keyId: |
                         PUBLIC_KEY_ID
         EOF
         

Replace the following:

     * `ATTESTATION_PROJECT_ID`: the ID of the project that stores attestations that are created using your local key
     * `PUBLIC_KEY_ID`: an ID that uniquely identifies your local key

  2. Create the platform policy:

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

  3. Store the ID value for later use:
         
         PUBLIC_KEY_ID="PUBLIC_KEY_ID"
         

Replace `PUBLIC_KEY_ID` with the ID that you specified in the `keyId` field in the platform policy file earlier in this guide.

The private key is used when attestations are created, as described later in this guide.




## Enable CV

You can create a new cluster or update an existing cluster to use CV monitoring with check-based platform policies. 

### Create a cluster that uses CV monitoring

In this section, you create a cluster that uses only CV monitoring with check-based platform policies. 

Before using any of the command data below, make the following replacements: 

  * `CLUSTER_NAME`: a cluster name.
  * `LOCATION`: the location—for example, `us-central1` or `asia-south1`.
  * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored.
  * `POLICY_ID`: the policy ID.
  * `CLUSTER_PROJECT_ID`: the cluster project ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --binauthz-evaluation-mode=POLICY_BINDINGS \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID \
        --project=CLUSTER_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters create CLUSTER_NAME `
        --location=LOCATION `
        --binauthz-evaluation-mode=POLICY_BINDINGS `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID `
        --project=CLUSTER_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters create CLUSTER_NAME ^
        --location=LOCATION ^
        --binauthz-evaluation-mode=POLICY_BINDINGS ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID ^
        --project=CLUSTER_PROJECT_ID

### Create cluster that uses enforcement and CV monitoring

In this section, you create a cluster that uses both [project-singleton](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#project-singleton-policy) policy enforcement and CV monitoring with check-based platform policies: 

Before using any of the command data below, make the following replacements: 

  * `CLUSTER_NAME`: a cluster name.
  * `LOCATION`: the location—for example, `us-central1` or `asia-south1`.
  * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored.
  * `POLICY_ID`: the policy ID.
  * `CLUSTER_PROJECT_ID`: the cluster project ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID \
        --project=CLUSTER_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters create CLUSTER_NAME `
        --location=LOCATION `
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID `
        --project=CLUSTER_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container clusters create CLUSTER_NAME ^
        --location=LOCATION ^
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID ^
        --project=CLUSTER_PROJECT_ID

### Update a cluster to use CV monitoring

In this section, you update a cluster to use CV monitoring with check-based platform policies only. If the cluster already has project-singleton policy enforcement enabled, running this command disables it. Instead, consider updating the cluster with enforcement and CV monitoring enabled. 

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

### Update a cluster to use enforcement and CV monitoring

In this section, you update a cluster to use both project-singleton policy enforcement and CV monitoring with check-based platform policies. 

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

## Create the Artifact Analysis note

In this section, you create an example [Artifact Analysis note](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#analysis_notes) to link attestations. To create the note, do the following:

  1. Create the note variables:
         
         NOTE_PROJECT_ID=NOTE_PROJECT_ID
         NOTE_ID="test-note"
         NOTE_URI="projects/${NOTE_PROJECT_ID}/notes/${NOTE_ID}"
         DESCRIPTION="CV test note"
         

Replace `NOTE_PROJECT_ID`: the ID of the project that contains the note.

  2. Create the note content file:
         
         cat > /tmp/note_payload.json << EOM
         {
           "name": "${NOTE_URI}",
           "attestation": {
             "hint": {
               "human_readable_name": "${DESCRIPTION}"
             }
           }
         }
         EOM
         

  3. Create the note:
         
         curl -X POST \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
             -H "x-goog-user-project: ${NOTE_PROJECT_ID}" \
             --data-binary @/tmp/note_payload.json "https://containeranalysis.googleapis.com/v1/projects/${NOTE_PROJECT_ID}/notes/?noteId=${NOTE_ID}"
         

Replace `NOTE_PROJECT_ID`: the ID of the project that contains the note

**Caution:** Binary Authorization doesn't support Artifact Analysis [regional storage](https://docs.cloud.google.com/artifact-analysis/docs/locations) or [regional endpoints](https://docs.cloud.google.com/artifact-analysis/docs/endpoints). We recommend that you use the Artifact Analysis global API endpoint (`https://containeranalysis.googleapis.com/`).
  4. Optional: To verify that you created the note:
         
         curl \
             -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
             -H "x-goog-user-project: NOTE_PROJECT_ID" \
         "https://containeranalysis.googleapis.com/v1/projects/NOTE_PROJECT_ID/notes/"
         

Replace `NOTE_PROJECT_ID` with the ID of the project that contains the note.




## Test CV

In this section, you test CV by deploying the image for which you created an attestation. In this case, the CV simple signing attestation check verifies the attestation and produces no log entry.

You then attempt to deploy a different image that has no attestation. In this case, the CV check can't find the attestation and logs the violation to Cloud Logging.

To create the variables you use to test CV, run the following commands:
    
    
    IMAGE_PATH="us-docker.pkg.dev/google-samples/containers/gke/hello-app"
    IMAGE_DIGEST="sha256:37e5287945774f27b418ce567cd77f4bbc9ef44a1bcd1a2312369f31f9cce567"
    IMAGE_TO_ATTEST="${IMAGE_PATH}@${IMAGE_DIGEST}"
    

### Create an attestation

To satisfy the simple signing attestation check, the image needs a valid attestation.

You can create an attestation using the gcloud CLI or the REST API.

###  PKIX Cloud KMS 

### gcloud

To create an attestation using the gcloud CLI, do the following:

  1. Sign the image and create the attestation using [Pre-Authentication Encoding (PAE)](https://github.com/secure-systems-lab/dsse/blob/master/protocol.md#dsse-protocol) (recommended):
         
         gcloud beta container binauthz attestations sign-and-create \
             --artifact-url=${IMAGE_TO_ATTEST} \
             --keyversion=${KMS_KEY_VERSION} \
             --keyversion-key=${KMS_KEY_NAME} \
             --keyversion-keyring=${KMS_KEYRING_NAME} \
             --keyversion-location=${KMS_KEY_LOCATION} \
             --note=${NOTE_URI} \
             --pae-encode-payload \
             --dsse-type=DSSE_TYPE
         

Replace `DSSE_TYPE` with the DSSE type for PAE encoding. The flag defaults to `application/vnd.dev.cosign.simplesigning.v1+json`.




### REST API

To create an attestation using the REST API, do the following:

  1. Create a signature payload file:
         
         cat > /tmp/generated_payload.json << EOM
         {
           "critical": {
             "identity": {
               "docker-reference": "${IMAGE_PATH}"
             },
             "image": {
               "docker-manifest-digest": "${IMAGE_DIGEST}"
             },
             "type": "Google Cloud BinAuthz container signature"
           }
         }
         EOM
         

  2. Sign the payload:
         
         gcloud kms asymmetric-sign \
             --version=${KMS_KEY_VERSION} \
             --key=${KMS_KEY_NAME} \
             --keyring=${KMS_KEYRING_NAME} \
             --location=${KMS_KEY_LOCATION} \
             --digest-algorithm=sha256 \
             --input-file=/tmp/generated_payload.json \
             --signature-file=/tmp/ec_signature \
             --project=${KMS_KEY_PROJECT_ID}
         

  3. Create the attestation content:
         
         cat > /tmp/attestation.json << EOM
         {
         "resourceUri": "${IMAGE_TO_ATTEST}",
         "note_name": "${NOTE_URI}",
         "attestation": {
           "serialized_payload": "$(base64 --wrap=0 /tmp/generated_payload.json)",
           "signatures": [{
             "public_key_id": "${PUBLIC_KEY_ID}",
             "signature": "$(base64 --wrap=0 /tmp/ec_signature)"
           }]
         }
         }
         EOM
         

  4. Create the attestation:
         
         curl -X POST "https://containeranalysis.googleapis.com/v1/projects/${NOTE_PROJECT_ID}/occurrences/" \
           -H "Content-Type: application/json" \
           -H "X-Goog-User-Project: ${NOTE_PROJECT_ID}" \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           --data-binary @/tmp/attestation.json
         

Replace `NOTE_PROJECT_ID` with the ID of the project that contains the note.




###  Local key 

###  gcloud 

  1. Create a signature payload file:
         
         cat > /tmp/generated_payload.json << EOM
         {
           "critical": {
             "identity": {
               "docker-reference": "${IMAGE_PATH}"
             },
             "image": {
               "docker-manifest-digest": "${IMAGE_DIGEST}"
             },
             "type": "Google Cloud BinAuthz container signature"
           }
         }
         EOM
         

  2. Create the signature payload file:
         
         openssl dgst -sha256 -sign ${PRIVATE_KEY_FILE} /tmp/generated_payload.json > /tmp/ec_signature
         

  3. Create the attestation:
         
         gcloud container binauthz attestations create \
             --project=ATTESTATION_PROJECT_ID \
             --artifact-url=${IMAGE_TO_ATTEST} \
             --note=${NOTE_URI} \
             --signature-file=/tmp/ec_signature \
             --public-key-id=PUBLIC_KEY_ID
         




###  REST API 

  1. Create a signature payload file:
         
         cat > /tmp/generated_payload.json << EOM
         {
           "critical": {
             "identity": {
               "docker-reference": "${IMAGE_PATH}"
             },
             "image": {
               "docker-manifest-digest": "${IMAGE_DIGEST}"
             },
             "type": "Google Cloud BinAuthz container signature"
           }
         }
         EOM
         

  2. Create the signature payload file:
         
         openssl dgst -sha256 -sign ${PRIVATE_KEY_FILE} /tmp/generated_payload.json > /tmp/ec_signature
         

  3. Create the attestation content:
         
         cat > /tmp/attestation.json << EOM
         {
         "resourceUri": "${IMAGE_TO_ATTEST}",
         "note_name": "${NOTE_URI}",
         "attestation": {
           "serialized_payload": "$(base64 --wrap=0 /tmp/generated_payload.json)",
           "signatures": [{
             "public_key_id": "${PUBLIC_KEY_ID}",
             "signature": "$(base64 --wrap=0 /tmp/ec_signature)"
           }]
         }
         }
         EOM
         

  4. Create the attestation:
         
         curl -X POST "https://containeranalysis.googleapis.com/v1/projects/${NOTE_PROJECT_ID}/occurrences/" \
           -H "Content-Type: application/json" \
           -H "X-Goog-User-Project: ${NOTE_PROJECT_ID}" \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           --data-binary @/tmp/attestation.json
         




### Deploy the image that has an attestation

To deploy an image for which an attestation was created, do the following:

  1. Configure `kubectl`:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=LOCATION \
             --project=CLUSTER_PROJECT_ID
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster
     * `LOCATION`: the cluster location
     * `CLUSTER_PROJECT_ID`: the cluster project ID
  2. Deploy a service and check the deployment against the Binary Authorization policy:
         
         kubectl run hello-app-with-attestation --image=$IMAGE_PATH@$IMAGE_DIGEST
         

The Pod was deployed. Because the image has an attestation, CV doesn't produce log entries related to this Pod.




### Deploy an image without an attestation

In this section, you deploy an image that doesn't have an associated attestation.

Because the policy requires attestations and this image doesn't have one, CV regularly logs the violation while the container is running.

To deploy the image, run the following command:
    
    
    kubectl run hello-app-without-attestation \
       --image=$IMAGE_PATH@$IMAGE_DIGEST
    

The Pod was deployed. Because the image doesn't have an attestation, CV produces log entries while the Pod is running.

## View logs for CV entries

You can search Cloud Logging entries to find CV configuration errors and CV platform policy validation violations.

CV logs errors and violations to Cloud Logging within 24 hours. You can usually see entries within a few hours.

### View CV configuration error logs

To view CV configuration error logs, run the following command:
    
    
    gcloud logging read \
         --order="desc" \
         --freshness=7d \
         --project=CLUSTER_PROJECT_ID \
        'logName:"binaryauthorization.googleapis.com%2Fcontinuous_validation" "configErrorEvent"'
    

The following output shows a configuration error in which a CV platform policy isn't found:
    
    
    {
      "insertId": "141d4f10-72ea-4a43-b3ec-a03da623de42",
      "jsonPayload": {
        "@type": "type.googleapis.com/google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent",
        "configErrorEvent": {
          "description": "Cannot monitor cluster 'us-central1-c.my-cluster': Resource projects/123456789/platforms/gke/policies/my-policy does not exist."
        }
      },
      "resource": {
        "type": "k8s_cluster",
        "labels": {
          "cluster_name": "my-cluster",
          "location": "us-central1-c",
          "project_id": "my-project"
        }
      },
      "timestamp": "2024-05-28T15:31:03.999566Z",
      "severity": "WARNING",
      "logName": "projects/my-project/logs/binaryauthorization.googleapis.com%2Fcontinuous_validation",
      "receiveTimestamp": "2024-05-28T16:30:56.304108670Z"
    }
    

### View CV platform policy validation violations

If no images violate the platform policies that you have enabled, no entries appear in the logs.

To view CV log entries for the last seven days, run the following command:
    
    
    gcloud logging read \
         --order="desc" \
         --freshness=7d \
         --project=CLUSTER_PROJECT_ID \
        'logName:"binaryauthorization.googleapis.com%2Fcontinuous_validation" "policyName"'
    

Replace `CLUSTER_PROJECT_ID` with the cluster project ID.

#### Check types

CV logs check violation information to `checkResults`. In the entry, the value `checkType` indicates the check. The values for each check are as follows:

  * `ImageFreshnessCheck`
  * `SigstoreSignatureCheck`
  * `SimpleSigningAttestationCheck`
  * `SlsaCheck`
  * `TrustedDirectoryCheck`
  * `VulnerabilityCheck`



#### Example log

The following example CV Logging entry describes a non-conformant image that violates a [trusted directory check](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#trusted-directory-check):
    
    
    {
      "insertId": "637c2de7-0000-2b64-b671-24058876bb74",
      "jsonPayload": {
        "podEvent": {
          "endTime": "2022-11-22T01:14:30.430151Z",
          "policyName": "projects/123456789/platforms/gke/policies/my-policy",
          "images": [
            {
              "result": "DENY",
              "checkResults": [
                {
                  "explanation": "TrustedDirectoryCheck at index 0 with display name \"My trusted directory check\" has verdict NOT_CONFORMANT. Image is not in a trusted directory",
                  "checkSetName": "My check set",
                  "checkSetIndex": "0",
                  "checkName": "My trusted directory check",
                  "verdict": "NON_CONFORMANT",
                  "checkType": "TrustedDirectoryCheck",
                  "checkIndex": "0"
                }
              ],
              "image": "gcr.io/my-project/hello-app:latest"
            }
          ],
          "verdict": "VIOLATES_POLICY",
          "podNamespace": "default",
          "deployTime": "2022-11-22T01:06:53Z",
          "pod": "hello-app"
        },
        "@type": "type.googleapis.com/google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent"
      },
      "resource": {
        "type": "k8s_cluster",
        "labels": {
          "project_id": "my-project",
          "location": "us-central1-a",
          "cluster_name": "my-test-cluster"
        }
      },
      "timestamp": "2022-11-22T01:44:28.729881832Z",
      "severity": "WARNING",
      "logName": "projects/my-project/logs/binaryauthorization.googleapis.com%2Fcontinuous_validation",
      "receiveTimestamp": "2022-11-22T03:35:47.171905337Z"
    }
    

## Clean up

This section describes how to clean up the CV monitoring you configured earlier in this guide.

You can disable CV monitoring or both Binary Authorization and CV in your cluster.

### Disable Binary Authorization in a cluster

To disable both CV and Binary Authorization enforcement in your cluster, run the following command:
    
    
    gcloud beta container clusters update CLUSTER_NAME \
        --binauthz-evaluation-mode=DISABLED \
        --location=LOCATION \
        --project=CLUSTER_PROJECT_ID
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster
  * `LOCATION`: the cluster location
  * `CLUSTER_PROJECT_ID`: the cluster project ID



### Disable check-based policy monitoring in a cluster

To disable CV with check-based policies in the cluster, and re-enable enforcement using the Binary Authorization enforcement policy, run the following command:
    
    
    gcloud beta container clusters update CLUSTER_NAME  \
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE \
        --location=LOCATION \
        --project="CLUSTER_PROJECT_ID"
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster
  * `LOCATION`: the cluster location
  * `CLUSTER_PROJECT_ID`: the cluster project ID



Note that `--binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE` is equivalent to the older flag `--enable-binauthz`.

### Delete the policy

To delete the policy, run the following command. It is not necessary to delete the check-based platform policy to disable check-based policy auditing.
    
    
    gcloud beta container binauthz policy delete POLICY_ID \
        --platform=gke \
        --project="POLICY_PROJECT_ID"
    

Replace the following:

  * `POLICY_ID`: the ID of the policy
  * `POLICY_PROJECT_ID`: the policy project ID



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
