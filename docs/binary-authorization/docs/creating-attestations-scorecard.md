---
url: https://docs.cloud.google.com/binary-authorization/docs/creating-attestations-scorecard/
title: Create attestations with OpenSSF Scorecard \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:17.954042+00:00
---

# Create attestations with OpenSSF Scorecard  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/creating-attestations-scorecard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Create attestations with OpenSSF Scorecard Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates how to use [OpenSSF Scorecard](https://github.com/ossf/scorecard) to check container images for supply chain security best practices. The Scorecard Attestor runs as part of Cloud Build pipeline to generate an attestation that can be verified by Binary Authorization before deployment. This verification step prevents compromised container artifacts from being deployed to production, which can prevent several classes of supply chain vulnerabilities.

## Overview

The Open Source Security Foundation (OpenSSF) is an organization that provides tools, services, and infrastructure for open source security initiatives. Scorecard is a tool, maintained by the OpenSSF, that scans source code management (SCM) repositories for supply chain security best-practices.

Scorecard Attestor is a tool built into Scorecard that allows you to create [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) attestations based on a policy that you configure. Scorecard Attestor runs Scorecard against the SCM repository of a container image, generates results, evaluates the results against the policy, and generates an attestation if the policy is satisfied.

In this tutorial, you build a sample repository and then use Scorecard Attestor. Each sample pipeline contains the following build steps:

  1. `build`: Build a sample container image.
  2. `push`: Push the image to Container Registry.
  3. `attest`: Check and sign the image, using Scorecard Attestor to create an attestation based on the policy.



In the `attest` step of each pipeline, Scorecard Attestor does the following:

  1. Fetches data about the SCM repository for the newly built container image.
  2. Runs Scorecard on the raw data and evaluates the SCM repository against the user-specified policy. 
     1. If all policies are satisfied, Scorecard Attestor creates the attestation.
     2. If any of the policies aren't satisfied, Scorecard Attestor doesn't create the attestation.



At deployment time, Binary Authorization checks for a verifiable attestation. Without one, the enforcer disallows the image from deploying.

## Costs

This tutorial uses the following Google Cloud products.

  * Container Registry
  * Artifact Analysis
  * Cloud Build
  * Cloud Key Management Service



Use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

## Objectives

In this tutorial you do the following:

  1. Set up Scorecard Attestor as a Cloud Build custom builder.
  2. View and configure Scorecard Attestor policy.
  3. Run Scorecard Attestor on a sample repository to create an attestation based on a policy.
  4. Run Scorecard Attestor on a sample repository in verify-only mode without creating an attestation. ## Before you begin



In this section, you perform a one-time setup of the system.

### Set up your environment

  1. Store your Google Cloud project in an environment variable.

**Note:** This Google Cloud project is used throughout this tutorial.
         
         export PROJECT_ID=PROJECT_ID
         

Replace PROJECT_ID with your Google Cloud project.

  2. Set the default project ID to your Google Cloud project:
         
         gcloud config set project $PROJECT_ID
         

  3. Store the project number in an environment variable for future steps:
         
         export PROJECT_NUMBER=$(gcloud projects list --filter="${PROJECT_ID}" \
          --format="value(PROJECT_NUMBER)")
         

  4. Enable APIs:

To ensure the services required for this guide are enabled, execute the following command:
         
         gcloud services enable \
           cloudbuild.googleapis.com \
           containerregistry.googleapis.com \
           containerscanning.googleapis.com \
           cloudkms.googleapis.com
         




### Set up IAM roles

Run the following commands to configure the Cloud Build service account with the following roles:

  * `containeranalysis.notes.editor`: adds the **Artifact Analysis Notes Editor** role to manage the attestor.
  * `containeranalysis.notes.occurrences.viewer`: adds the **Artifact Analysis Occurrences for Notes** role to manage both the vulnerability and attestation occurrences.
  * `roles/containeranalysis.occurrences.editor`: adds the **Artifact Analysis Occurrences Editor** role to create attestation occurrences in Artifact Analysis.
  * `cloudkms.signer`: adds the **Cloud KMS CryptoKey Signer** role that allows the service account to access the Cloud KMS signing service.
        
        gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role roles/containeranalysis.notes.editor
        gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role roles/containeranalysis.notes.occurrences.viewer
        gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role roles/containeranalysis.occurrences.editor
        gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role roles/cloudkms.signer
        




### Create a Cloud KMS signing key

[Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) keys are used to create the attestation.

  1. Create a new Cloud KMS key ring with the name scorecard-attestor-key-ring:
         
         gcloud kms keyrings create scorecard-attestor-key-ring \
             --location global
         

  2. Create a new Cloud KMS key called scorecard-attestor-key within the key ring:
         
         gcloud kms keys create scorecard-attestor-key \
             --keyring scorecard-attestor-key-ring \
             --location global \
             --purpose "asymmetric-signing" \
             --default-algorithm "rsa-sign-pkcs1-2048-sha256"
         

  3. Store the digest algorithm and Cloud KMS in an environment variable for future steps:
         
         export KMS_DIGEST_ALG=SHA256
         export KMS_KEY_NAME=projects/$PROJECT_ID/locations/global/keyRings/scorecard-attestor-key-ring/cryptoKeys/scorecard-attestor-key/cryptoKeyVersions/1
         

  4. Create the Binary Authorization attestor. Later, Scorecard Attestor creates a note associated with this attestor.
         
         gcloud container binauthz attestors create scorecard-attestor \
             --attestation-authority-note=scorecard-attestation \
             --attestation-authority-note-project=$PROJECT_ID \
             --description="Attest that ossf/scorecard policy checks pass"
         

  5. Associate the Binary Authorization attestor with the KMS key:
         
         gcloud container binauthz attestors public-keys add \
             --attestor=scorecard-attestor \
             --keyversion=1 \
             --keyversion-key=scorecard-attestor-key \
             --keyversion-keyring=scorecard-attestor-key-ring \
             --keyversion-location=global \
             --keyversion-project=$PROJECT_ID
         




To explore other signing algorithms, refer to [Creating asymmetric keys](https://docs.cloud.google.com/kms/docs/creating-asymmetric-keys).

## Create attestations with Scorecard Attestor in a Cloud Build pipeline

### Submit the failure-case sample build

In this section, you build a container image and check its supply chain security practices with OpenSSF Scorecard. The image builds successfully, but does not create an attestation. The base repository contains some discouraged supply chain security practices, such as an unpinned dependency to Debian 10 in the Dockerfile, and a compiled binary artifact checked into the source repository. These are violations of the attestation policy in the repository.

  1. Clone the test repository: [scorecard-binauthz-test-bad](https://github.com/ossf-tests/scorecard-binauthz-test-bad).

  2. View the attestation policy file for the failure case.
         
         cat policy-binauthz.yaml
         

  3. (Optional) View the build configuration file for the failure case.
         
         cat samples/signer/cloudbuild.yaml
         

**Note:** This build configuration file also contains [user-defined substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_user-defined_substitutions). Substitutions are variables, used within the build pipeline, that are passed in through the `gcloud builds submit` command with the `--substitutions` parameter.
  4. Submit the build:
         
         gcloud builds submit \
             --substitutions=_KMS_KEY_NAME=$KMS_KEY_NAME,_KMS_DIGEST_ALG=$KMS_DIGEST_ALG \
             --config=cloudbuild.yaml
         




You should see output like the following:
    
    
    time="2022-12-20T22:30:14Z" level=info msg="image failed scorecard attestation policy check"
    

  1. Save the build ID from the last build:
         
         export BUILD_ID=$(gcloud builds list --limit=1 --format="value('ID')")
         

  2. Verify the result:
         
         gcloud storage cat gs://${PROJECT_NUMBER}.cloudbuild-logs.googleusercontent.com/log-${BUILD_ID}.txt | grep "failed scorecard attestation policy check"
         




### Submit the success-case sample build

In this section you build a container image that satisfies its Scorecard attestation policy. In this case, the Scorecard Attestor creates an attestation.

To submit the success-case sample build to Cloud Build, do the following:

  1. Clone the test repository: [scorecard-binauthz-test-good](https://github.com/ossf-tests/scorecard-binauthz-test-good).

  2. View the attestation policy file for the failure case. `sh cat policy-binauthz.yaml`

  3. (Optional) View the build configuration file for the failure case.
         
         cat samples/signer/cloudbuild.yaml
         

**Note:** this build configuration file also contains [user-defined substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_user-defined_substitutions). Substitutions are variables, used within the build pipeline, that are passed in through the `gcloud builds submit` command with the `--substitutions` parameter.
  4. Submit the build:
         
         gcloud builds submit \
             --substitutions=_KMS_KEY_NAME=$KMS_KEY_NAME,_KMS_DIGEST_ALG=$KMS_DIGEST_ALG \
             --config=cloudbuild.yaml
         

  5. Verify the result:
         
         gcloud storage cat gs://${PROJECT_NUMBER}.cloudbuild-logs.googleusercontent.com/log-${BUILD_ID}.txt | grep "passed scorecard attestation policy check"
         

  6. Get the URL of the container image that was built and checked by scorecard
         
         export IMAGE_URI=$(gcloud storage cat gs://${PROJECT_NUMBER}.cloudbuild-logs.googleusercontent.com/log-${BUILD_ID}.txt | grep -o "Attestation for image .* is successfully uploaded" txt | cut -d' ' -f4 | tr -d '"')
         

  7. Confirm that an attestation was created for the container image. Scorecard Attestor uses the Note ID `ossf-scorecard-attestation`, and the note name `projects/${PROJECT_ID}/notes/ossf-scorecard-attestation`.
         
         gcloud container binauthz attestations list \
             --attestor="projects/${PROJECT_ID}/attestors/ossf-scorecard-attestor" \
             --filter="resourceUri='https://${IMAGE_URI}'"
         




## Clean up

To clean up resources used in this document, you can delete the project:
    
    
    gcloud projects delete $PROJECT_ID
    

## What's next

  * View the [Scorecard Attestor documentation](https://github.com/ossf/scorecard/blob/main/attestor/README.md)
  * [Learn more about Scorecard](https://github.com/ossf/scorecard/blob/main/README.md)
  * [Learn more about Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview)
  * Create attestors through the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console) or the [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
