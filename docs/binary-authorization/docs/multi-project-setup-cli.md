---
url: https://docs.cloud.google.com/binary-authorization/docs/multi-project-setup-cli/
title: Configure a multi-project setup \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:20.958306+00:00
---

# Configure a multi-project setup  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/multi-project-setup-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Configure a multi-project setup Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to use Binary Authorization in a multi-project configuration. For a simpler single-project configuration, see [Get started using the Google Cloud CLI (GKE)](https://docs.cloud.google.com/binary-authorization/docs/getting-started-cli).

To establish [separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties), you can setup Binary Authorization in a multiple-project configuration. The purpose of each project is discussed later in this tutorial.

## Objectives

In this tutorial, you perform the following tasks: 

  1. Set up a different project for deployment (GKE), attestor, and attestation management, to support [separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties).

  2. Configure the default [rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#rules) of your Binary Authorization [policy](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies) to require attestations.

  3. Create Public-Key Infrastructure (X.509) (PKIX) key pair to sign, and later verify, the attestation.

  4. Create an attestor that the Binary Authorization enforcer uses to verify the attestation.

  5. Sign an example image, creating an attestation.

  6. Test the policy by deploying the example image.




You must configure each project's appropriate access control through Identity and Access Management (IAM).

For additional security, you can use VPC Service Controls to help protect the resources you create in this tutorial. For more information, see [Securing with VPC Service Controls](https://docs.cloud.google.com/binary-authorization/docs/securing-with-vpcsc).

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)
  * [Binary Authorization](https://docs.cloud.google.com/binary-authorization/pricing)
  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * Optional: [Cloud Key Management Service](https://docs.cloud.google.com/kms/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

**Note:** For this configuration, you set up three projects.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Install [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl) for interacting with GKE.



## Set up the deployer project

The _deployer project_ manages the Google Kubernetes Engine (GKE) clusters, where you deploy images, and the Binary Authorization [policy](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies) that Binary Authorization enforces at deploy time. You can have more than one deployer project, depending on the size, complexity, and other requirements of your environment.

**Note:** To use the same attestor with multiple deployer projects, repeat the steps below, substituting DEPLOYER_PROJECT_ID with the ID of each deployer project.

To set up the deployer project:

  1. Create the project and enable billing in Google Cloud console if you have not already done so.

  2. Identity and Access Management note: The deployer project contains your GKE cluster. The Identity and Access Management configuration for this project should reflect that.

  3. Set environment variables to store the Google Cloud project and number:
         
         DEPLOYER_PROJECT_ID=DEPLOYER_PROJECT_ID
         

Replace DEPLOYER_PROJECT_ID with the Google Cloud project ID.
         
         DEPLOYER_PROJECT_NUMBER=$(gcloud projects describe "${DEPLOYER_PROJECT_ID}" \
             --format="value(projectNumber)")
         

  4. Enable APIs:

###  Artifact Registry 
         
         gcloud --project=${DEPLOYER_PROJECT_ID} \
           services enable\
           container.googleapis.com\
           artifactregistry.googleapis.com\
           binaryauthorization.googleapis.com
         

  5. Get the deployer project service account name:
         
         DEPLOYER_SERVICE_ACCOUNT="service-${DEPLOYER_PROJECT_NUMBER}@gcp-sa-binaryauthorization.iam.gserviceaccount.com"
         

You use the service account name in a later step when you configure permissions on the Artifact Analysis note associated with your attestor.




## Set up the attestor project

An _attestor project_ stores the [attestors](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors) that can verify that an image is ready for deployment. Often, you have a single attestor project that acts as a centralized store for information about trusted parties in the authorization process. This allows you to centrally manage security keys required to verify the identity of attestors and to restrict access to only those parties who administer them.

To set up the attestor project:

  1. Create the project and enable billing in Google Cloud console if you have not already done so.

  2. Identity and Access Management note: Because the this project contains your attestors, only security personnel should have write access.

  3. Set environment variables to store the project ID and number:
         
         ATTESTOR_PROJECT_ID=ATTESTOR_PROJECT_ID
         

Replace ATTESTOR_PROJECT_ID with the attestor project ID.
         
         ATTESTOR_PROJECT_NUMBER=$(gcloud projects describe "${ATTESTOR_PROJECT_ID}" \
             --format="value(projectNumber)")
         

  4. Enable the Artifact Analysis and Binary Authorization APIs:
         
         gcloud services --project=${ATTESTOR_PROJECT_ID} \
             enable containeranalysis.googleapis.com \
             binaryauthorization.googleapis.com
         

  5. Get the attestor project service account name:
         
         ATTESTOR_SERVICE_ACCOUNT="service-${ATTESTOR_PROJECT_NUMBER}@gcp-sa-binaryauthorization.iam.gserviceaccount.com"
         

You use the service account name in a later step when you configure permissions on the Artifact Analysis note associated with your attestor.




## Set up the attestations project

An _attestation_ project is one that stores [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations) that attestors make when they verify an image. A separate attestation project allows you to organize and inspect statements about software readiness more easily.

  1. Create the project and enable billing in Google Cloud console if you have not already done so.

  2. Identity and Access Management note: All roles involved in binary authorization should have read access to the Artifact Analysis Notes and Occurrences in this project, however only attestation managers need to have write access.

  3. Set an environment variable to store the project name:
         
         ATTESTATION_PROJECT_ID=ATTESTATION_PROJECT_ID
         

Replace ATTESTATION_PROJECT_ID with the attestation project ID.

  4. Enable the Artifact Analysis and Binary Authorization APIs:
         
         gcloud services --project=${ATTESTATION_PROJECT_ID} \
             enable containeranalysis.googleapis.com \
             binaryauthorization.googleapis.com
         




## Create a cluster

Now you can create a GKE cluster in the deployer project. This is the cluster where you want your deployed container images to run. When you create the cluster, you pass the `--binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE` flag to the `gcloud container clusters create` command.

To create the cluster:
    
    
    gcloud --project=${DEPLOYER_PROJECT_ID} \
        container clusters create \
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE \
        --zone us-central1-a \
        test-cluster
    

Here, you create a cluster named `test-cluster` in the GKE zone `us-central1-a`.

You must also update the local `kubeconfig` file for your `kubectl` installation. This provides the credentials and endpoint information required to access the cluster in GKE.

To update the local `kubeconfig` file:
    
    
    gcloud --project=${DEPLOYER_PROJECT_ID} \
        container clusters get-credentials \
        --zone us-central1-a \
        test-cluster
    

## Create an attestor

An [attestor](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors) is a party that is responsible for attesting that a required process has completed before a container image can be deployed. This party can be a human user or, more often, a machine process like a build and test system, or your continuous integration (CI) and deployment (CD) pipelines. You create attestors in your attestor project.

Creating an attestor requires you to:

  * Create a [note](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#analysis_notes) in [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) to store trusted metadata used in the authorization process
  * Create the attestor itself in the attestor project and associate the note you created
  * Add an IAM role binding for the deployer project service account to the attestor
  * Set permissions on the Artifact Analysis note



For this tutorial, you have one attestor named `test-attestor` and a Container Analysis note named `test-attestor-note`. In a real-world scenario, you can have any number of attestors, each one representing a party that participates in the authorization process for the image.

### Create the Artifact Analysis note

  1. Set variables that store the name of your attestor and Artifact Analysis note:
         
         ATTESTOR_NAME=test-attestor
         NOTE_ID=test-attestor-note
         

Replace:

     * test-attestor: attestor name of your choice.
     * test-attestor-note: attestor note name of your choice.
  2. Create a JSON file in `/tmp/note_payload.json` that describes the Container Analysis note:
         
         cat > /tmp/note_payload.json << EOM
         {
           "name": "projects/${ATTESTOR_PROJECT_ID}/notes/${NOTE_ID}",
           "attestation": {
             "hint": {
               "human_readable_name": "Attestor Note"
             }
           }
         }
         EOM
         

  3. Create the note by sending an HTTP request to the Artifact Analysis REST API:
         
         curl -X POST \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
             --data-binary @/tmp/note_payload.json  \
             "https://containeranalysis.googleapis.com/v1/projects/${ATTESTOR_PROJECT_ID}/notes/?noteId=${NOTE_ID}"
         

**Caution:** Binary Authorization doesn't support Artifact Analysis [regional storage](https://docs.cloud.google.com/artifact-analysis/docs/locations) or [regional endpoints](https://docs.cloud.google.com/artifact-analysis/docs/endpoints). We recommend that you use the Artifact Analysis global API endpoint (`https://containeranalysis.googleapis.com/`).
  4. Verify that the note was created:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://containeranalysis.googleapis.com/v1/projects/${ATTESTOR_PROJECT_ID}/notes/${NOTE_ID}"
         




### Create the attestor

Now, you can create the attestor:

  1. Create the attestor in Binary Authorization:
         
         gcloud --project=${ATTESTOR_PROJECT_ID} \
             container binauthz attestors create ${ATTESTOR_NAME} \
             --attestation-authority-note=${NOTE_ID} \
             --attestation-authority-note-project=${ATTESTOR_PROJECT_ID}
         

  2. Verify that the attestor was created:
         
         gcloud --project=${ATTESTOR_PROJECT_ID} \
             container binauthz attestors list
         




The attestor you created is not yet usable without an associated PKIX key pair, which you create below.

### Add an IAM role binding for the deployer project

You must add an IAM role binding for the deployer project to the attestor. This is used by Binary Authorization when it evaluates a policy to determine whether the project has permissions to access any associated attestations.

To add the IAM role binding:
    
    
    gcloud --project ${ATTESTOR_PROJECT_ID} \
        container binauthz attestors add-iam-policy-binding \
        "projects/${ATTESTOR_PROJECT_ID}/attestors/${ATTESTOR_NAME}" \
        --member="serviceAccount:${DEPLOYER_SERVICE_ACCOUNT}" \
        --role=roles/binaryauthorization.attestorsVerifier
    

### Set permissions on the Artifact Analysis note

You must also set permissions on the Artifact Analysis note you created so that it is accessible to both the deployer project and the attestor project. You do this by updating the IAM policy for the note to assign **Viewer** access to the project service accounts.

  1. Generate a JSON file that contains the information needed to set the IAM policy on your note.
         
         cat > /tmp/iam_request.json << EOM
         {
           'resource': 'projects/${ATTESTOR_PROJECT_ID}/notes/${NOTE_ID}',
           'policy': {
             'bindings': [
               {
                 'role': 'roles/containeranalysis.notes.occurrences.viewer',
                 'members': [
                   'serviceAccount:${ATTESTOR_SERVICE_ACCOUNT}',
                   'serviceAccount:${DEPLOYER_SERVICE_ACCOUNT}'
                 ]
               }
             ]
           }
         }
         EOM
         

  2. Add the service account and requested access roles to the IAM policy for the note you created:
         
         curl -X POST  \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             --data-binary @/tmp/iam_request.json \
             "https://containeranalysis.googleapis.com/v1/projects/${ATTESTOR_PROJECT_ID}/notes/${NOTE_ID}:setIamPolicy"
         

**Caution:** Binary Authorization doesn't support Artifact Analysis [regional storage](https://docs.cloud.google.com/artifact-analysis/docs/locations) or [regional endpoints](https://docs.cloud.google.com/artifact-analysis/docs/endpoints). We recommend that you use the Artifact Analysis global API endpoint (`https://containeranalysis.googleapis.com/`).



## Set up PKIX keys

Binary Authorization uses cryptographic keys to securely verify the identity of attestors. This ensures that only verified parties can participate in the authorization of a container image. The key pair consists of a private key, which the attestor uses to digitally sign attestations, and a public key, which you add to the attestor as stored by the Binary Authorization service.

In this tutorial, you use the recommended [Elliptic Curve Digital Signature Algorithm (ECDSA)](https://docs.cloud.google.com/kms/docs/algorithms#asymmetric_signing_algorithms) to create the key pair. You can also use RSA or PGP keys for signing. See [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms) for more information on signing algorithms.

The asymmetric keys generated and stored by [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) (Cloud KMS) are PKIX-compliant. See [Creating attestors using the CLI](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli) for more information on using PKIX keys and Cloud KMS.

### Generate a key pair

A [PKIX key pair](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#cryptographic_keys) consists of a private key, which the [signer](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#signers) uses to digitally sign attestations, and a public key, which you add to the attestor. At deploy time, Binary Authorization uses this public key to verify the attestation signed by the private key.

  1. Generate the private key:

To generate a new local asymmetric PKIX key pair and store it in a file:

###  PKIX (Cloud KMS) 

This step shows how to perform an attestation using keys generated and stored in [Cloud Key Management Service](https://docs.cloud.google.com/kms).

     1. Set up environment variables to store information about the key pair as managed by Cloud KMS:

If you already have a key pair, you can set these environment variables and skip the next step.
            
            KMS_KEY_PROJECT_ID=KMS_KEY_PROJECT_ID
            KMS_KEY_LOCATION=KMS_KEY_LOCATION
            KMS_KEYRING_NAME=KMS_KEYRING_NAME
            KMS_KEY_NAME=KMS_KEY_NAME
            KMS_KEY_VERSION=KMS_KEY_VERSION
            

Replace the following:

        * KMS_KEY_PROJECT_ID: the ID of the project where the keys are stored
        * KMS_KEY_LOCATION: the location of the key
        * KMS_KEYRING_NAME: the name of the key ring
        * KMS_KEY_NAME: the name of the key
        * KMS_KEY_VERSION: the key version
     2. [Optional] Set up a KMS key:

**Note:** You can skip these steps if you already have a KMS key.
        1. Create a KMS key whose public key can be stored in an attestor. This step also sets up environment variables you use below.

To create a key and set up the environment variables:
               
               KMS_KEY_PROJECT_ID=${PROJECT_ID}
               KMS_KEYRING_NAME=my-binauthz-keyring
               KMS_KEY_NAME=my-binauthz-kms-key-name
               KMS_KEY_LOCATION=global
               KMS_KEY_PURPOSE=asymmetric-signing
               KMS_KEY_ALGORITHM=ec-sign-p256-sha256
               KMS_PROTECTION_LEVEL=software
               KMS_KEY_VERSION=1
               

        2. Create a KMS key ring:
               
               gcloud kms keyrings create ${KMS_KEYRING_NAME} \
                 --location ${KMS_KEY_LOCATION} \
                 --project ${KMS_KEY_PROJECT_ID}
               

        3. Create the key:
               
               gcloud kms keys create ${KMS_KEY_NAME} \
                 --location ${KMS_KEY_LOCATION} \
                 --keyring ${KMS_KEYRING_NAME}  \
                 --purpose ${KMS_KEY_PURPOSE} \
                 --default-algorithm ${KMS_KEY_ALGORITHM} \
                 --protection-level ${KMS_PROTECTION_LEVEL} \
                 --project ${KMS_KEY_PROJECT_ID}
               

For more information on creating KMS keys, see [Create an asymmetric key](https://docs.cloud.google.com/kms/docs/creating-asymmetric-keys).

     3. Add the public key to the attestor:
            
            gcloud --project="${ATTESTOR_PROJECT_ID}" \
                container binauthz attestors public-keys add \
                --attestor="${ATTESTOR_NAME}" \
                --keyversion-project="${KMS_KEY_PROJECT_ID}" \
                --keyversion-location="${KMS_KEY_LOCATION}" \
                --keyversion-keyring="${KMS_KEYRING_NAME}" \
                --keyversion-key="${KMS_KEY_NAME}" \
                --keyversion="${KMS_KEY_VERSION}"
            

###  PKIX (local key) 

**Warning:** We strongly recommend against using locally generated key pairs in production environments as they present a security risk. We recommend that you instead use Cloud Key Management Service. This example is provided for illustrative purposes only. 

     1. To generate the private key, run the following commands:
            
            PRIVATE_KEY_FILE="/tmp/ec_private.pem"
            openssl ecparam -genkey -name prime256v1 -noout -out ${PRIVATE_KEY_FILE}
            

PRIVATE_KEY_FILE is the name of the file that contains the private key that is stored in the attestor.

     2. Extract the public key from the private key and store it in a file:
            
            PUBLIC_KEY_FILE="/tmp/ec_public.pem"
            openssl ec -in ${PRIVATE_KEY_FILE} -pubout -out ${PUBLIC_KEY_FILE}
            

PUBLIC_KEY_FILE is the name of the file that contains the public key that is stored in the attestor.

     3. To add the public key you exported to the attestor, run the following code.
            
            gcloud --project="${ATTESTOR_PROJECT_ID}" \
              container binauthz attestors public-keys add \
              --attestor="${ATTESTOR_NAME}" \
              --pkix-public-key-file=${PUBLIC_KEY_FILE} \
              --pkix-public-key-algorithm=ecdsa-p256-sha256
            

Binary Authorization uses the public key in the attestor to verify the attestation.




## Configure the policy

Now, you can configure your policy in the deployer project. In this step, you export the policy YAML file to your local system and modify the default rule so that it requires an attestation by the attestor you defined above.

To configure the policy:

  1. Create a new policy file that allows [Google-maintained system images](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#google-maintained_system_images), sets the [`evaluationMode`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#evaluationmode) to `REQUIRE_ATTESTATION`, and adds a node named [`requireAttestationsBy`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#requireattestationsby) that references the attestor you created:
         
         cat > /tmp/policy.yaml << EOM
             globalPolicyEvaluationMode: ENABLE
             defaultAdmissionRule:
               evaluationMode: REQUIRE_ATTESTATION
               enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
               requireAttestationsBy:
                 - projects/${ATTESTOR_PROJECT_ID}/attestors/${ATTESTOR_NAME}
             name: projects/${DEPLOYER_PROJECT_ID}/policy
         EOM
         

  2. Import the policy YAML file into Binary Authorization:
         
         gcloud --project=${DEPLOYER_PROJECT_ID} \
             container binauthz policy import /tmp/policy.yaml
         




For more information on configuring a policy, see [Configuring a Policy Using the CLI](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli).

## Test the policy

In this tutorial, you create an attestation for example, public "Hello World!" images from Artifact Registry. Initially, the enforcer blocks the images from being deployed because the required attestation does not exist.

To try to deploy the image:

###  Artifact Registry 
    
    
    kubectl run hello-server --image us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 --port 8080
    

Now, verify that the deployment was blocked by Binary Authorization:
    
    
    kubectl get pods
    

The command prints the following message, which indicates that the image was not deployed:
    
    
    No resources found.
    

You can get further details about the deployment:
    
    
    kubectl get event --template \
    '{{range.items}}{{"\033[0;36m"}}{{.reason}}:{{"\033[0m"}}\{{.message}}{{"\n"}}{{end}}'
    

You see a response that resembles the following:
    
    
    FailedCreate: Error creating: pods POD_NAME is forbidden: admission webhook "imagepolicywebhook.image-policy.k8s.io" denied the request: Image IMAGE_NAME denied by Binary Authorization default admission rule. Image IMAGE_NAME denied by attestor ATTESTOR_NAME: No attestations found
    

In this output:

  * POD_NAME: the name of the Pod.
  * IMAGE_NAME: the name of the image.
  * ATTESTOR_NAME: the name of the attestor.



Make sure to delete the deployment so you can continue to the next step:
    
    
    kubectl delete deployment hello-server
    

## Create an attestation

An [attestation](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations) is a statement by an attestor that a required process in your pipeline has been completed and that the container image in question is authorized for deployment. The attestation itself is a digitally signed record that contains the full path to a version of the image as stored your container image registry, as well as the identity of the attestor.

In this tutorial, your attestation simply states that you authorize the image for deployment. You create the attestation in the attestation project.

To create an attestation:

  1. Set variables that store the registry path and digest of the image:

###  Artifact Registry 
         
         IMAGE_PATH="us-docker.pkg.dev/google-samples/containers/gke/hello-app"
         IMAGE_DIGEST="sha256:37e5287945774f27b418ce567cd77f4bbc9ef44a1bcd1a2312369f31f9cce567"
         IMAGE_TO_ATTEST=${IMAGE_PATH}@${IMAGE_DIGEST}
         

  2. Create the attestation

###  PKIX Cloud KMS 

To create the attestation using the Cloud KMS key, run the following command:
         
         gcloud beta container binauthz attestations sign-and-create \
             --project="${PROJECT_ID}" \
             --artifact-url="${IMAGE_TO_ATTEST}" \
             --attestor="${ATTESTOR_NAME}" \
             --attestor-project="${PROJECT_ID}" \
             --keyversion-project="${KMS_KEY_PROJECT_ID}" \
             --keyversion-location="${KMS_KEY_LOCATION}" \
             --keyversion-keyring="${KMS_KEYRING_NAME}" \
             --keyversion-key="${KMS_KEY_NAME}" \
             --keyversion="${KMS_KEY_VERSION}"
         

###  PKIX (local key) 

To create the attestation using a local key, do the following:

     1. Generate the attestation payload:

**Note:** In the following command, while an `${IMAGE_PATH}` is required to create the signature payload for the attestation, only the `${IMAGE_DIGEST}` is used at deploy time. This means you can deploy an identical container image from multiple locations with the same attestation.
            
            gcloud --project=${ATTESTATION_PROJECT_ID} \
              container binauthz create-signature-payload \
              --artifact-url=${IMAGE_TO_ATTEST} > /tmp/generated_payload.json
            

The payload JSON file has the following contents:

###  Artifact Registry 
            
            {
            "critical": {
              "identity": {
                "docker-reference": "us-docker.pkg.dev/google-samples/containers/gke/hello-app"
              },
              "image": {
                "docker-manifest-digest": "sha256:37e5287945774f27b418ce567cd77f4bbc9ef44a1bcd1a2312369f31f9cce567"
              },
              "type": "Google cloud binauthz container signature"
            }
            }
            

     2. Sign the payload.

If using local PKIX files, sign the payload with your local PKIX private key and output a signature file:
            
            openssl dgst -sha256 -sign ${PRIVATE_KEY_FILE} /tmp/generated_payload.json > /tmp/ec_signature
            

The output file is a signed version of the payload JSON file you created above.

     3. Get the public key ID from the attestor.

You can view your public key ID at any time using the command: `gcloud container binauthz attestors describe ATTESTOR_NAME`.

To save your public key ID in an environment variable, enter this command:
            
            PUBLIC_KEY_ID=$(gcloud container binauthz attestors describe ${ATTESTOR_NAME} \
            --format='value(userOwnedGrafeasNote.publicKeys[0].id)' --project ${ATTESTOR_PROJECT_ID})
            

     4. Create and validate the attestation:
            
            gcloud container binauthz attestations create \
              --project="${ATTESTATION_PROJECT_ID}" \
              --artifact-url="${IMAGE_TO_ATTEST}" \
              --attestor="projects/${ATTESTOR_PROJECT_ID}/attestors/${ATTESTOR_NAME}" \
              --signature-file=/tmp/ec_signature \
              --public-key-id="${PUBLIC_KEY_ID}" \
              --validate
            

The `validate` flag checks that the attestation can be verified by the attestor you configured in your policy.

  3. Verify that the attestation was created:
         
         gcloud --project=${ATTESTATION_PROJECT_ID} \
             container binauthz attestations list \
             --attestor=$ATTESTOR_NAME --attestor-project=$ATTESTOR_PROJECT_ID
         




For more information on creating attestations, see [Creating Attestations](https://docs.cloud.google.com/binary-authorization/docs/making-attestations).

## Retest the policy

Test the policy by deploying a sample container image to the cluster. This time, you must deploy the image using the digest rather than a tag like `1.0` or `latest`, as Binary Authorization uses the digest to look up attestations. Here, Binary Authorization allows the image to be deployed because the image has an associated attestation.

To deploy the image:
    
    
    kubectl run hello-server --image ${IMAGE_TO_ATTEST} --port 8080
    

To verify that the image was deployed:
    
    
    kubectl get pods
    

The command prints a message similar to the following, which indicates that deployment was successful:
    
    
    NAME                            READY     STATUS    RESTARTS   AGE
    hello-server-579859fb5b-h2k8s   1/1       Running   0          1m
    

Now that you have successfully deployed the container image and verified that your setup is working, you can delete the cluster you created in GKE:
    
    
    gcloud --project=${DEPLOYER_PROJECT_ID} \
        container clusters delete \
        --zone=us-central1-a \
        test-cluster
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

  1. Delete the cluster that you created in GKE:
         
         gcloud container clusters delete \
             --zone=us-central1-a \
             test-cluster
         

  2. You can also delete Google Cloud projects that you created for this tutorial.




## What's next

  * [Learn more about Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview)
  * [Learn key concepts used in Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/key-concepts)
  * [Enable dry run mode to disable enforcement](https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run)
  * [Use breakglass to bypass enforcement](https://docs.cloud.google.com/binary-authorization/docs/using-breakglass)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
