---
url: https://docs.cloud.google.com/binary-authorization/docs/cv-slsa-check/
title: Use the SLSA check \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:34.183370+00:00
---

# Use the SLSA check  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/cv-slsa-check/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Use the SLSA check Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to use the Binary Authorization continuous validation (CV) [SLSA check](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#slsa-check), which checks the SLSA-compliant provenance of container images associated with Pods running on GKE clusters where CV is enabled.

To use this check, you must build images with Cloud Build, which produces [SLSA-compliant provenance](https://slsa.dev/provenance).

The example in this guide uses Cloud Source Repositories for the source code repository, Artifact Registry for the image registry, and Cloud Build to build the image and produce the provenance.

The only trusted builder that the SLSA check supports is Cloud Build.

## Costs

This guide uses the following Google Cloud services:

  * Artifact Registry
  * Binary Authorization, but CV is available free of charge during the [Preview](https://cloud.google.com/products/#product-launch-stages) stage
  * Cloud Build
  * Cloud Source Repositories
  * GKE



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

  7. Enable the Artifact Registry, Binary Authorization, Cloud Build, GKE, Cloud Source Repositories APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com binaryauthorization.googleapis.com cloudbuild.googleapis.com container.googleapis.com sourcerepo.googleapis.com

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

  13. Enable the Artifact Registry, Binary Authorization, Cloud Build, GKE, Cloud Source Repositories APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com binaryauthorization.googleapis.com cloudbuild.googleapis.com container.googleapis.com sourcerepo.googleapis.com

  14. Ensure that the gcloud CLI is updated to the latest version.
  15. [Install the `kubectl` command-line tool.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
  16. If your Binary Authorization policies and GKE clusters are in different projects, make sure that Binary Authorization is enabled in both projects.



## Required roles

This section shows you how to set roles for this check.

### Overview

If you run all of the products that are mentioned in this guide in the same project, you don't need to set any permissions. Binary Authorization configures the roles correctly when you enable it. If you run the products in different projects, you must set roles as described in this section.

To ensure that the Binary Authorization Service Agent in each project has the necessary permissions to evaluate the CV SLSA check, ask your administrator to grant the following IAM roles to the Binary Authorization Service Agent in each project: 

**Important:** You must grant these roles to the Binary Authorization Service Agent in each project, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) on the cluster project Compute Engine service account
  * If your cluster project is different from the policy project: [Binary Authorization Policy Evaluator ](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEvaluator) (`roles/binaryauthorization.policyEvaluator`) on the cluster project Binary Authorization Service Agent, for it to access the policy project 
  * If your attestation project is different from your policy project: [Container Analysis Occurrences Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`) on the policy project Binary Authorization Service Agent, for it to access the attestation project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Binary Authorization Service Agent in each project the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant roles using the gcloud CLI

To ensure that the service accounts in each project have the necessary permissions to evaluate this check, grant the service accounts in each project the following IAM roles:

  1. If the project where you run your cluster is different from the project where the policy resides, you must grant permission for the cluster project's Binary Authorization service agent to access the policy in the policy project.

     1. Get the cluster project's Binary Authorization service agent:
            
            PROJECT_NUMBER=$(gcloud projects list \
              --filter="projectId:CLUSTER_PROJECT_ID" \
              --format="value(PROJECT_NUMBER)")
            CLUSTER_SERVICE_ACCOUNT="service-$PROJECT_NUMBER@gcp-sa-binaryauthorization.iam.gserviceaccount.com"
            

Replace `CLUSTER_PROJECT_ID` with the project ID of the cluster.

     2. Allow CV to evaluate the policy on the cluster:
            
            gcloud projects add-iam-policy-binding POLICY_PROJECT_ID \
                --member="serviceAccount:$CLUSTER_SERVICE_ACCOUNT" \
                --role='roles/binaryauthorization.policyEvaluator'
            

Replace `POLICY_PROJECT_ID` with the ID of the project that contains your policy.

  2. Allow the policy project service agent to access attestations:

     1. Obtain the Binary Authorization service agent associated with the policy project:
            
            PROJECT_NUMBER=$(gcloud projects list \
              --filter="projectId:POLICY_PROJECT_ID" \
              --format="value(PROJECT_NUMBER)")
            POLICY_PROJECT_SERVICE_ACCOUNT="service-$PROJECT_NUMBER@gcp-sa-binaryauthorization.iam.gserviceaccount.com"
            

Replace `POLICY_PROJECT_ID` with the ID of the project that contains your policy.

     2. Grant the role:
            
            gcloud projects add-iam-policy-binding ATTESTATION_PROJECT_ID \
                --member="serviceAccount:$POLICY_PROJECT_SERVICE_ACCOUNT" \
                --role='roles/containeranalysis.occurrences.viewer'
            

Replace `ATTESTATION_PROJECT_ID` with the ID of the project that contains your attestations.

  3. Allow the default Compute Engine service account permission to pull the image from the repository:

     1. Obtain the Compute Engine service account associated with the cluster project:
            
            PROJECT_NUMBER=$(gcloud projects list \
              --filter="projectId:CLUSTER_PROJECT_ID" \
              --format="value(PROJECT_NUMBER)")
            COMPUTE_ENGINE_SERVICE_ACCOUNT="$PROJECT_NUMBER-compute@developer.gserviceaccount.com"
            

Replace `CLUSTER_PROJECT_ID` with the ID of the cluster project that contains your policy.

     2. Grant the role:
            
            gcloud projects add-iam-policy-binding ARTIFACT_PROJECT_ID \
                --member="serviceAccount:$COMPUTE_ENGINE_SERVICE_ACCOUNT" \
                --role='roles/artifactregistry.reader'
            

Replace `ARTIFACT_PROJECT_ID` with the ID of the Artifact Registry project that stores the images that are to be deployed.




## Optional: Build and upload a sample image

This section is included for illustrative purposes, to show you how to build an example image with SLSA-compliant provenance. The provenance is used later in the guide to demonstrate the check. Learn more about [Cloud Build provenance](https://docs.cloud.google.com/build/docs/securing-builds/view-build-provenance).

### Create the sample repository

To create a repository in Cloud Source Repositories, do the following:

  1. Create the repository and clone it locally:
         
         gcloud source repos create SOURCE_REPO_NAME \
             --project=SOURCE_REPO_PROJECT_ID && \
         gcloud source repos clone SOURCE_REPO_NAME \
             --project=SOURCE_REPO_PROJECT_ID && \
         cd SOURCE_REPO_NAME
         

Replace the following:

     * `SOURCE_REPO_NAME`: the name of your source code repository—for example: `slsa-check-test-repo`
     * `SOURCE_REPO_PROJECT_ID`: the repository project ID
  2. To create the source, config, and build files, do the following:

     1. Create the image source:
            
            cat > quickstart.sh <<EOF
            #!/bin/sh
            echo "Hello, world! The time is $(date)."
            sleep infinity
            EOF
            

     2. Make the file executable:
            
            chmod +x quickstart.sh
            

     3. Create the Dockerfile config file:
            
            cat > Dockerfile <<EOF
            FROM alpine
            COPY quickstart.sh /
            CMD ["/quickstart.sh"]
            EOF
            

     4. Create the Cloud Build `cloudbuild.yaml` file, which pushes the image to Artifact Registry:
            
            cat > cloudbuild.yaml <<EOF
            steps:
            - name: 'gcr.io/cloud-builders/docker'
              args: [ 'build', '-t', 'LOCATION-docker.pkg.dev/ARTIFACT_PROJECT_ID/ARTIFACT_REPO_NAME/DIRECTORY/IMAGE', '.' ]
            options:
              requestedVerifyOption: VERIFIED
            images:
            - 'LOCATION-docker.pkg.dev/ARTIFACT_PROJECT_ID/ARTIFACT_REPO_NAME/DIRECTORY/IMAGE'
            EOF
            

Replace the following:

        * `LOCATION`: the Artifact Registry location—for example: `us-west2`, `europe-central2`, or `asia-east1`
        * `ARTIFACT_PROJECT_ID`: the ID of the project that stores Artifact Registry artifacts
        * `ARTIFACT_REPO_NAME`: the Artifact Registry repository name—for example: `slsa-check-test-repo`
        * `DIRECTORY`: the directory—for example: `slsa-check`
        * `IMAGE`: the path to the image—for example: `slsa-check-image`
     5. Commit the files to Cloud Source Repositories:
            
            git add .
            git commit -a
            




### Build and upload the sample image

To simplify using this guide, we recommend that you use the same project for SOURCE_REPO_PROJECT_ID, and ARTIFACT_PROJECT_ID. If you use different projects, you might need to set up additional IAM permissions. Learn more about [Artifact Registry access control](https://docs.cloud.google.com/artifact-registry/docs/access-control). To learn more about Cloud Build, see [Overview of Cloud Build](https://docs.cloud.google.com/build/docs/overview).

To create the repository, do the following:

  1. Create the Artifact Registry repository:
         
         gcloud artifacts repositories create ARTIFACT_REPO_NAME \
             --project=ARTIFACT_PROJECT_ID \
             --repository-format=docker \
             --location=LOCATION \
             --description="Docker repository"
         

Replace the following:

     * `ARTIFACT_REPO_NAME`: the name of your repository
     * `ARTIFACT_PROJECT_ID`: the artifact project ID
     * `LOCATION`: the Artifact Registry location—for example: `us-west2`, `europe-central2`, or `asia-east1`
  2. Create the Cloud Build build trigger:
         
         gcloud beta builds triggers create cloud-source-repositories \
             --project=SOURCE_REPO_PROJECT_ID \
             --repo=SOURCE_REPO_NAME \
             --region=LOCATION \
             --branch-pattern=.* \
             --build-config=cloudbuild.yaml
         

Replace the following:

     * `SOURCE_REPO_NAME`: the source code repository name
     * `SOURCE_REPO_PROJECT_ID`: the Cloud Build project ID
     * `LOCATION`: the location
  3. Trigger a build by pushing the files that you created earlier in this guide.
         
         git push
         

When the image builds successfully, Cloud Build generates provenance and uploads the image to your Artifact Registry repository.

  4. To check for the latest image and get its digest, do the following:

     1. Ensure that Cloud Build built your image:
            
            gcloud artifacts docker images list LOCATION-docker.pkg.dev/ARTIFACT_PROJECT_ID/REPO_NAME/DIRECTORY \
                --project=ARTIFACT_PROJECT_ID \
                --sort-by=create_time
            

Replace the following:

        * `LOCATION`: the Artifact Registry location
        * `ARTIFACT_PROJECT_ID`: the project ID for artifacts
        * `ARTIFACT_REPO_NAME`: the repository name
        * `DIRECTORY`: the directory
     2. Copy the digest of the most recent image. The digest looks similar to the following: `sha256:9432f747bd058b33de33bb5314d6eec1ac357d664e04c76824bb7072a9218d59`

  5. Optional: View the provenance of your image:
         
         gcloud artifacts docker images describe \
           LOCATION-docker.pkg.dev/ARTIFACT_PROJECT_ID/ARTIFACT_REPO_NAME/DIRECTORY/IMAGE@DIGEST \
             --project=ARTIFACT_PROJECT_ID \
             --show-provenance
         

Replace the following:

     * `ARTIFACT_PROJECT_ID`: the project ID for artifacts
     * `LOCATION`: the Artifact Registry location
     * `ARTIFACT_REPO_NAME`: the artifact repository name
     * `DIRECTORY`: the directory
     * `IMAGE`: the path to the image
     * `DIGEST`: the digest associated with the image

The command output looks similar to the following:
    
    image_summary:
      digest: sha256:9432f747bd058b33de33bb5314d6eec1ac357d664e04c76824bb7072a9218d59
      fully_qualified_digest: us-west2-docker.pkg.dev/my-project/slsa-check-repo/slsa-check-image@sha256:9432f747bd058b33de33bb5314d6eec1ac357d664e04c76824bb7072a9218d59
      registry: us-west2-docker.pkg.dev
      repository: slsa-check-repo
      slsa_build_level: 3
    provenance_summary:
      provenance:
      - build:
          intotoStatement:
            _type: https://in-toto.io/Statement/v0.1
            predicateType: https://slsa.dev/provenance/v0.1
            slsaProvenance:
              builder:
                id: https://cloudbuild.googleapis.com/GoogleHostedWorker
              materials:
              - digest:
                  sha1: de4e4227fff1d00d6f7785a827608627e4a369ea
                uri: git+https://source.cloud.google.com/my-project/slsa-check-source-repo
              metadata:
                ...
    envelope:
      payload: eyJfdHlwZSI6I ... taW1hZ2U6dGFnMSJ9XX0=
      payloadType: application/vnd.in-toto+json
      signatures:
      - keyid: projects/verified-builder/locations/global/keyRings/attestor/cryptoKeys/provenanceSigner/cryptoKeyVersions/1
        sig: MEQCIBCCkho_re4EfAT-NBSSmAXOZlv4lU_vWzEru97tU8KmAiAKcAa99umWngzNQADmPixqYjbKjLOKQEUvrI5chSrf7g==
      - keyid: projects/verified-builder/locations/global/keyRings/attestor/cryptoKeys/builtByGCB/cryptoKeyVersions/1
        sig: MEUCIFOEq_7RpiZAB4vUlit3hkZ2yI0n37-5Y87l0JbU-EZSAiEA9TNZZcv_MnzKffTnswHWZR2DSLmYiklr5twWfIec-zo=
    

The output must contain the `provenance_summary` block for the SLSA check to function. If the output doesn't contain the block, check that Cloud Build was invoked by a build trigger. Cloud Build doesn't produce provenance information when it is triggered manually.




## Create a platform policy

To generate provenance, you must use a Cloud Build trigger to build your image, as described in Build and upload the sample image.

To create a platform policy with a SLSA check, do the following:

  1. Create the platform policy YAML file:
         
         cat > POLICY_PATH <<EOF
         gkePolicy:
           checkSets:
           - checks:
             - displayName: My SLSA check
               imageAllowlist:
                 # This policy exempts images that are in the following artifact registry
                 allowPattern:
                 - ARTIFACT_LOCATION-docker.pkg.dev/ARTIFACT_PROJECT_ID/ARTIFACT_REPO_NAME/EXEMPT_IMAGE_PATH/**
               slsaCheck:
                 rules:
                 - attestationSource:
                     containerAnalysisAttestationProjects:
                     - projects/ATTESTATION_PROJECT_ID
                   configBasedBuildRequired: true
                   trustedBuilder: GOOGLE_CLOUD_BUILD
                   trustedSourceRepoPatterns:
                   - source.cloud.google.com/SOURCE_REPO_PROJECT_ID/SOURCE_REPO_NAME
                   customConstraints: CEL_EXPRESSION
             displayName: My check set
         EOF
         

Replace the following:

     * `POLICY_PATH`: A path for the policy file.
     * `ARTIFACT_LOCATION`: The location of your repository in Artifact Registry.
     * `ARTIFACT_PROJECT_ID`: The ID of the project that contains your artifacts.
     * `ARTIFACT_REPO_NAME`: The repository that contains the image.
     * `EXEMPT_IMAGE_PATH`: An optional path to one or more exempt images—for example: `not-built-by-cloud-build`. The `imageAllowlist` block is included in this platform policy so that you can exempt images that lack provenance so that they don't violate the platform policy. To instead log violations from these images, omit this block.
     * `ATTESTATION_PROJECT_ID`: The project ID that stores the attestations that were created by Cloud Build.
     * `SOURCE_REPO_PROJECT_ID`: The ID of the project that contains your source code.
     * `SOURCE_REPO_NAME`: The repository that contains the image. For illustrative purposes, to force a violation of this check, set `SOURCE_REPO_NAME` to a source code repository other than where your image resides.
     * `POLICY_PROJECT_ID`: The ID of the project that contains the CV policy.
     * `POLICY_ID`: The ID of this policy.
     * `CEL_EXPRESSION`: A [CEL](https://cel.dev) expression that provides additional constraints on the SLSA policy. For example, to add a custom constraint that further requires that images come from a specific directory path, replace `CEL_EXPRESSION` with the following expression:
           
           payload.predicate.externalParameters.buildConfigSource.path != "" && payload.predicate.externalParameters.buildConfigSource.repository.contains("github.com/my-repo/my-production-repo")
           

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

## Deploy the image

  1. Configure `kubectl`:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=LOCATION \
             --project=CLUSTER_PROJECT_ID
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster
     * `LOCATION`: the cluster location
     * `CLUSTER_PROJECT_ID`: the cluster project ID
  2. Deploy the Pod:
         
         kubectl run hello-app \
             --image='LOCATION-docker.pkg.dev/ARTIFACT_PROJECT_ID/ARTIFACT_REPO_NAME/DIRECTORY/IMAGE@DIGEST'
         

The Pod is deployed. Because the image was built with provenance and from a trusted source code repository, it won't violate the CV SLSA check and no log entries are generated.

To force a violation of the SLSA check, you can set `SOURCE_REPO_NAME` to a source code repository other than where your image resides. You can also manually trigger the build, which skips provenance generation. Then check for log entries.




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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
