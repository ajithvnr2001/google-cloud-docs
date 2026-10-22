---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter-binary-auth/
title: Transmitting HL7v2 messages over TCP/IP connections using a signed MLLP image \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:36.924495+00:00
---

# Transmitting HL7v2 messages over TCP/IP connections using a signed MLLP image  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter-binary-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Transmitting HL7v2 messages over TCP/IP connections using a signed MLLP image Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial provides instructions for using Binary Authorization as part of a minimal lower layer protocol (MLLP) deployment in a multi-project setup. Using Binary Authorization on Google Kubernetes Engine ensures that the MLLP adapter can only be deployed from a verified and signed container image.

The open source MLLP adapter Binary Authorization codelab in [GitHub](https://github.com/GoogleCloudPlatform/mllp/blob/master/mllp_adapter/docs/binary_authz.md) demonstrates a similar scenario in detail.

## Objectives

After completing this tutorial, you'll know how to:

  * Configure an attestor to attest when an MLLP image is ready for deployment.
  * Deploy an attested image of the MLLP adapter binary.
  * Use a multi-project setup to separate responsibility for signing images from the deployment environment.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud Healthcare API
  * Google Kubernetes Engine
  * Artifact Analysis
  * Cloud Key Management Service
  * Binary Authorization



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Prerequisites

Before beginning this tutorial, familiarize yourself with the conceptual documentation on MLLP by reviewing [MLLP and the Google Cloud MLLP adapter](https://docs.cloud.google.com/healthcare-api/docs/concepts/hl7v2#mllp_and_the_google_cloud_platform_mllp_adapter). The conceptual documentation provides an overview of MLLP, how care systems can send and receive messages to and from the Cloud Healthcare API over an MLLP connection, and the basics of MLLP security.

## Choosing a shell

To complete this tutorial, you can use [Cloud Shell](https://docs.cloud.google.com/shell) or your local shell.

Cloud Shell is a shell environment for managing resources hosted on Google Cloud. Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and the [`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/) command-line tool. The gcloud CLI provides the primary command-line interface for Google Cloud. The `kubectl` tool provides the command-line interface for running commands against Kubernetes clusters.

If you prefer using your local shell, you must install the Google Cloud CLI.

To open Cloud Shell or configure your local shell, complete the following steps:

###  Cloud Shell 

To launch Cloud Shell, complete the following steps:

  1. Go to Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. From the top-right corner of the console, click the **Activate Google Cloud Shell** button: ![](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png)




A Cloud Shell session opens inside a frame at the bottom of the console. You use this shell to run `gcloud` and `kubectl` commands.

###  Local Shell 

To install the gcloud CLI and the `kubectl` tool, complete the following steps:

  1. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs).

  2. Install the `kubectl` command-line tool by running the following command:
         
         gcloud components install kubectl
         




## Container project

The container project, `cloud-healthcare-containers`, already exists. It holds the MLLP adapter images.

## Creating a key ring and key pair

The Cloud KMS project provides a Public Key Infrastructure (X.509) (PKIX) signature using Cloud KMS. Binary Authorization uses cryptographic keys to securely verify the identity of attestors. This makes sure that only verified parties can participate in the authorization of a container image. The key pair consists of a private key, which the attestor uses to digitally sign attestations, and a public key, which you add to the attestor as stored by the Binary Authorization service.

If you want to manage private and public key pairs locally, the Cloud KMS project isn't required. For more information, see [Using customer-managed encryption keys](https://docs.cloud.google.com/container-registry/docs/using-encryption-keys).

To create a key ring and key pair, complete the following steps:

  1. Create the Cloud KMS project by completing the following steps:

     1. In the Google Cloud console, go to the New Project page. 

[Go to New Project](https://console.cloud.google.com/projectcreate)

     2. Complete the form and then click **Create**. The project name you select is referenced as KMS_PROJ_ID throughout this tutorial.

For more information about creating projects, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  2. To enable Cloud KMS API on the Cloud KMS project, run the following command:
         
         gcloud services enable cloudkms.googleapis.com \
             --project=KMS_PROJ_ID

  3. To create a key ring, run the following command, where KEY_RING is a unique name for the key ring and KEY_RING_LOCATION is a region such as `us-central-1`:
         
         gcloud kms keyrings create KEY_RING \
             --project=KMS_PROJ_ID \
             --location=KEY_RING_LOCATION

  4. To create a key pair, run the following command:
         
         gcloud kms keys create KEY \
             --project=KMS_PROJ_ID \
             --keyring=KEY_RING \
             --location=KEY_RING_LOCATION \
             --purpose=asymmetric-signing \
             --default-algorithm="ec-sign-p256-sha256"

  5. To verify the key version on the Cloud KMS project, run the following command. The key version should be `1`.
         
         gcloud kms keys versions list \
             --project=KMS_PROJ_ID \
             --location=KEY_RING_LOCATION \
             --key=KEY \
             --keyring=KEY_RING




## Creating and configuring the HL7v2 project, dataset, and HL7v2 store

To create and configure the HL7v2 project, dataset, and HL7v2 store, complete the following steps:

  1. To create the HL7v2 project, complete the following steps:

     1. In the Google Cloud console, go to the New Project page. 

[Go to New Project](https://console.cloud.google.com/projectcreate)

     2. Complete the form and then click **Create**. The project name you select is referenced as HL7V2_PROJ_ID throughout this tutorial.

  2. To enable the Cloud Healthcare API on the project, run the following command:
         
         gcloud services enable healthcare.googleapis.com \
             --project=HL7V2_PROJ_ID

  3. To create a dataset to store the HL7v2 store, run the following command:
         
         gcloud healthcare datasets create DATASET_ID \
             --location=HL7V2_STORE_LOCATION \
             --project=HL7V2_PROJ_ID

  4. To create the HL7v2 store, run the following command:
         
         gcloud healthcare hl7v2-stores create HL7V2_STORE_ID \
             --dataset=DATASET_ID \
             --location=HL7V2_STORE_LOCATION \
             --project=HL7V2_PROJ_ID




## Creating a Artifact Analysis note

The note project owns the Artifact Analysis note.

To create a Artifact Analysis note, complete the following steps:

  1. Create the note project by completing the following steps:

     1. In the Google Cloud console, go to the New Project page. 

[Go to New Project](https://console.cloud.google.com/projectcreate)

     2. Complete the form and then click **Create**. The project name you select is referenced as NOTE_PROJ_ID throughout this tutorial.
  2. To enable the Artifact Analysis API on the note project, run the following command:
         
         gcloud services enable containeranalysis.googleapis.com \
              --project=NOTE_PROJ_ID

  3. To save the sample note payload to a file named `./tmp/note_payload.json`, run the following command:
         
         cat > ./tmp/note_payload.json << EOM
         {
           "name": "projects/NOTE_PROJ_ID/notes/NOTE_ID",
           "attestation": {
             "hint": {
               "human_readable_name": "Attestor note"
             }
           }
         }
         EOM

  4. To create a Artifact Analysis note in the note project, run the following command:
         
         curl -X POST \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"  \
             --data-binary @./tmp/note_payload.json  \
             "https://containeranalysis.googleapis.com/v1/projects/NOTE_PROJ_ID/notes/?noteId=NOTE_ID"

  5. To verify that the note has been created, run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://containeranalysis.googleapis.com/v1/projects/NOTE_PROJ_ID/notes/NOTE_ID"




## Creating and configuring an attestor

The attestor project stores attestors, which verify or attest that a container image is ready for deployment.

To create and configure an attestor, complete the following steps:

  1. To create the attestor project, complete the following steps:

     1. In the Google Cloud console, go to the New Project page. 

[Go to New Project](https://console.cloud.google.com/projectcreate)

     2. Complete the form and then click **Create**. The project name you select is referenced as ATTESTOR_PROJ_ID throughout this tutorial.
  2. To enable the Binary Authorization and Cloud KMS APIs on the attestor project, run the following commands:
         
         gcloud services enable binaryauthorization.googleapis.com \
             --project=ATTESTOR_PROJ_ID
         gcloud services enable cloudkms.googleapis.com \
             --project=ATTESTOR_PROJ_ID

  3. To create an attestor on the attestor project, run the following command. The attestor uses the note created in the note project for attestation.
         
         gcloud beta container binauthz attestors create ATTESTOR_ID \
             --project=ATTESTOR_PROJ_ID \
             --attestation-authority-note=NOTE_ID \
             --attestation-authority-note-project=NOTE_PROJ_ID

  4. To verify that the attestor has been created, run the following command:
         
         gcloud beta container binauthz attestors list \
             --project=ATTESTOR_PROJ_ID

  5. Make the following substitutions and then save the sample JSON to a file named `./tmp/iam_request.json` by running the following command:

     * Use the values of NOTE_PROJ_ID and NOTE_ID from Creating a Artifact Analysis note.
     * To find the ATTESTOR_PROJECT_NUM, complete the following steps:

       1. Go to the [**Dashboard** page](https://console.cloud.google.com/home) in the Google Cloud console. 

[ Go to the Dashboard page](https://console.cloud.google.com/home)

       2. Click the **Select from** drop-down list at the top of the page. In the **Select from** window that appears, select the attestor project.

The project number is displayed on the project Dashboard **Project info** card.
    
    cat > ./tmp/iam_request.json << EOM
    {
      "resource": "projects/NOTE_PROJ_ID/notes/NOTE_ID",
      "policy": {
        "bindings": [
          {
            "role": "roles/containeranalysis.notes.occurrences.viewer",
            "members": [
              "serviceAccount:service-ATTESTOR_PROJ_NUM@gcp-sa-binaryauthorization.iam.gserviceaccount.com"
            ]
          }
        ]
      }
    }
    EOM

  6. To grant the attestor project's Binary Authorization service account permission to read the Artifact Analysis note occurrences in the note project, run the following command:
         
         curl -X POST  \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             --data-binary @./tmp/iam_request.json \
         "https://containeranalysis.googleapis.com/v1/projects/NOTE_PROJ_ID/notes/NOTE_ID:setIamPolicy"

  7. To add the key generated in the Cloud KMS project to the attestor, run the following command:
         
         gcloud beta container binauthz attestors public-keys add  \
             --project=ATTESTOR_PROJ_ID \
             --attestor=ATTESTOR_ID  \
             --keyversion-project=KMS_PROJ_ID  \
             --keyversion-location=KEY_RING_LOCATION \
             --keyversion-keyring=KEY_RING \
             --keyversion-key=KEY \
             --keyversion=KEY_VERSION




## Creating an attestation

The attestation project stores attestations. An attestation is a statement by an attestor that a required process in your pipeline is complete and a container image is authorized for deployment.

To create an attestation, complete the following steps:

  1. To create the attestation project, complete the following steps:

     1. In the Google Cloud console, go to the New Project page. 

[Go to New Project](https://console.cloud.google.com/projectcreate)

     2. Complete the form and then click **Create**. The project name you select is referenced as ATTESTATION_PROJ_ID throughout this tutorial.
  2. To enable the Binary Authorization API on the attestation project, run the following command:
         
         gcloud services enable binaryauthorization.googleapis.com \
             --project=ATTESTATION_PROJ_ID

  3. To sign and create the attestation, run the following command, where IMAGE_SIGNED is the location of the [signed MLLP Adapter Image](https://gcr.io/cloud-healthcare-containers/mllp-adapter), `gcr.io/cloud-healthcare-containers/mllp-adapter@sha256:231b073df13db0c65e57b0e1d526ab6816a73c37262e25c18bcca99bf4b4b185`:
         
         gcloud beta container binauthz attestations sign-and-create \
             --project=ATTESTATION_PROJ_ID \
             --artifact-url=IMAGE_SIGNED \
             --attestor=ATTESTOR_ID \
             --attestor-project=ATTESTOR_PROJ_ID \
             --keyversion-project=KMS_PROJ_ID \
             --keyversion-location=KEY_RING_LOCATION \
             --keyversion-keyring=KEY_RING \
             --keyversion-key=KEY \
             --keyversion=KEY_VERSION




## Deploying the MLLP adapter

The deployer project owns the GKE cluster where Binary Authorization is imported and stored.

To deploy the MLLP adapter, complete the following steps:

  1. To create the deployer project, complete the following steps:

     1. In the Google Cloud console, go to the New Project page. 

[Go to New Project](https://console.cloud.google.com/projectcreate)

     2. Complete the form and then click **Create**. The project name you select is referenced as DEPLOYER_PROJ_ID throughout this tutorial.
  2. To enable the Binary Authorization API on the deployer project, run the following command:
         
         gcloud services enable binaryauthorization.googleapis.com \
             --project=DEPLOYER_PROJ_ID

  3. To grant the Binary Authorization service account on the deployer project permission to access the attestor for attestation verification, run the following command:
         
         gcloud beta container binauthz attestors add-iam-policy-binding \
             "projects/ATTESTOR_PROJ_ID/attestors/ATTESTOR_ID" \
             --project=ATTESTOR_PROJ_ID \
             --member="serviceAccount:service-DEPLOYER_PROJ_NUM@gcp-sa-binaryauthorization.iam.gserviceaccount.com" \
             --role=roles/binaryauthorization.attestorsVerifier

  4. To create a cluster with `--binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE` in the deployer project, run the following command:
         
         gcloud beta container clusters create CLUSTER_NAME \
             --project=DEPLOYER_PROJ_ID \
             --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE \
             --zone CLUSTER_ZONE

  5. The sample deployment policy adds image sources to the allowlist and sets a project scope default rule to block images from sources that haven't been attested by the attestor. To save the sample deployment policy to a file named `./tmp/policy.yaml`, run the following command:
         
         cat > ./tmp/policy.yaml << EOM
             admissionWhitelistPatterns:
             - namePattern: gcr.io/google_containers/*
             - namePattern: gcr.io/google-containers/*
             - namePattern: k8s.gcr.io/*
             - namePattern: gcr.io/stackdriver-agents/*
             defaultAdmissionRule:
               evaluationMode: REQUIRE_ATTESTATION
               enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
               requireAttestationsBy:
                 - projects/ATTESTOR_PROJ_ID/attestors/ATTESTOR_ID
             name: projects/DEPLOYER_PROJ_ID/policy
         EOM

  6. To import the deployment policy to the deployer project, run the following command:
         
         gcloud beta container binauthz policy import ./tmp/policy.yaml \
             --project=DEPLOYER_PROJ_ID

  7. To view details about the policy, go to the Binary Authorization page in the Google Cloud console.

[Go to the Binary Authorization page](https://console.cloud.google.com/security/binary-authorization/)

  8. To check out the GKE cluster credentials, run the following command:
         
         gcloud container clusters get-credentials \
             --project=DEPLOYER_PROJ_ID \
             --zone CLUSTER_ZONE CLUSTER_NAME

  9. Make the following substitutions and then save the sample YAML to a file named `./tmp/deployment.yaml` by running the following command:

     * IMAGE_SIGNED is the location of the [signed MLLP Adapter Image](https://gcr.io/cloud-healthcare-containers/mllp-adapter), `gcr.io/cloud-healthcare-containers/mllp-adapter@sha256:231b073df13db0c65e57b0e1d526ab6816a73c37262e25c18bcca99bf4b4b185`.
     * Use the values of HL7V2_PROJ_ID, HL7V2_STORE_LOCATION, DATASET_ID, and HL7V2_STORE_ID that you used in Creating and configuring the HL7v2 project, dataset, and store.
    
    cat > ./tmp/deployment.yaml << EOM
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: mllp-adapter-deployment
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: mllp-adapter
       template:
         metadata:
           labels:
             app: mllp-adapter
         spec:
           containers:
             - name: mllp-adapter
               imagePullPolicy: Always
               image: IMAGE_SIGNED
               ports:
                 - containerPort: 2575
                   protocol: TCP
                   name: "port"
               command:
                 - "/usr/mllp_adapter/mllp_adapter"
                 - "--hl7_v2_project_id=HL7V2_PROJ_ID"
                 - "--hl7_v2_location_id=HL7V2_STORE_LOCATION"
                 - "--hl7_v2_dataset_id=DATASET_ID"
                 - "--hl7_v2_store_id=HL7V2_STORE_ID"
                 - "--api_addr_prefix=https://healthcare.googleapis.com:443/v1beta1"
                 - "--logtostderr"
                 - "--receiver_ip=0.0.0.0"
    EOM

  10. To create a deployment with the attested image, run the following command:
         
         kubectl create -f ./tmp/deployment.yaml

  11. To confirm that the deployment was successful, run the following commands:
         
         kubectl get pods
         kubectl get event

The `get pods` command shows one running pod and the `get event` shows `Scaled up replica set mllp-adapter-deployment-xxxx to 1`.




After completing this section, you have successfully securely deployed an attested MLLP adapter image to Google Kubernetes Engine.

## Deleting the projects

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, you can clean up the resources you created on Google Cloud.

Follow the steps below to delete the following projects that you created in this tutorial:

  * Attestor project
  * Attestation project
  * Deployer project
  * Note project
  * Cloud KMS project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
