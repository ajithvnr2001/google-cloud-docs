---
url: https://docs.cloud.google.com/binary-authorization/docs/getting-started-console/
title: Get started using the Google Cloud console (GKE) \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:09.515929+00:00
---

# Get started using the Google Cloud console (GKE)  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/getting-started-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Get started using the Google Cloud console (GKE) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This tutorial assumes that you have read the [Binary Authorization overview](https://docs.cloud.google.com/binary-authorization/docs/overview).

This tutorial shows how to configure and test a Binary Authorization policy that requires [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations). This type of policy secures your container-based software supply chain by defining who can deploy container images on [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs) (GKE) and which container images GKE is allowed to deploy.

At deploy time, Binary Authorization uses [attestors](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors) to verify digital signatures in [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations). The attestations were created by [signers](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#signers) as part of the build process.

In this tutorial, the GKE cluster, attestations, and attestors are all located in a single project. A single-project configuration is mostly useful for testing or experimenting with the service. For a more real-world example, see [multi-project configuration](https://docs.cloud.google.com/binary-authorization/docs/multi-project-setup-cli).

The steps below describe tasks that you perform from Google Cloud console, as well as some tasks you perform using `gcloud` commands. To perform these steps using `gcloud`, see [Get started using the Google Cloud CLI](https://docs.cloud.google.com/binary-authorization/docs/getting-started-cli).

## Objectives

In this tutorial, you learn how to:

  * Create a (GKE) cluster with Binary Authorization enabled
  * Create an attestor that the Binary Authorization enforcer uses to verify the signature on an attestation
  * Configure a policy that requires an attestation
  * Create a cryptographic key pair to sign attestations and later verify them
  * Sign a container image digest, creating a signature
  * Create an attestation using the signature
  * Test the policy by deploying a container image to GKE



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)
  * [Binary Authorization](https://docs.cloud.google.com/binary-authorization/pricing)
  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * Optional: [Cloud Key Management Service](https://docs.cloud.google.com/kms/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Container Registry, Artifact Analysis and Binary Authorization APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,containeranalysis.googleapis.com,artifactregistry.googleapis.com,binaryauthorization.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Container Registry, Artifact Analysis and Binary Authorization APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,containeranalysis.googleapis.com,artifactregistry.googleapis.com,binaryauthorization.googleapis.com&redirect=https%3A//console.cloud.google.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Install [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl).



## Set the default project

To facilitate commands that follow, store your Google Cloud project ID in an environment variable as follows:
    
    
    PROJECT_ID=PROJECT_ID
    

where PROJECT_ID is the name of your project.

If the default project is not selected, set it now:
    
    
    gcloud config set project ${PROJECT_ID}
    

## Create a cluster with Binary Authorization enabled

### Create the cluster

Now you can create a GKE cluster with Binary Authorization enabled. Here, you create a cluster named `test-cluster` in the GKE zone `us-central1-a`.

To create the cluster, follow these steps:

  1. Visit the GKE menu in Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create Cluster**.

  3. Enter `test-cluster` in the **Name** field.

  4. Select **Zonal** in the **Location type** options.

  5. Select `us-central1-a` from the **Zone** drop-down list.

  6. In the navigation pane, in the **Cluster** section, click **Advanced settings**.

  7. In the **Binary authorization** row, click _edit_ **Edit configuration**.

  8. Select **Enable Binary Authorization**.

  9. Select **Enforce-only** , and then click **Save**.

  10. Click **Create**.




### Configure `kubectl`

You must also update the local `kubeconfig` file for your `kubectl` installation. This provides the credentials and endpoint information required to access the cluster in GKE.

To update the local `kubeconfig` file, follow these steps:
    
    
    gcloud container clusters get-credentials \
        --zone us-central1-a \
        test-cluster
    

## View the default policy

A [policy](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies) in Binary Authorization is a set of rules that govern the deployment of container images. You can have one policy per project. By default, the policy is configured to allow all container images to be deployed.

To view the default policy, follow these steps:

  1. Go to the Binary Authorization page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

  2. Click **Edit Policy**.

  3. In **Project Default Rule** , the option **Allow All Images** is displayed.

  4. Click **Save Policy**.




## Create an attestor

An [attestor](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors) is the verification authority that the Binary Authorization enforcer uses at deploy time to decide whether to allow GKE to deploy the corresponding signed container image. The attestor contains the public key and is typically managed by people responsible for software supply chain security.

Creating an attestor requires you to:

  * Create the attestor itself in Binary Authorization
  * Auto-generate an associated attestor [note](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#analysis_notes) in [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) to store trusted attestation metadata used in the authorization process



For this tutorial, you have one attestor named `test-attestor`. In a real-world scenario, you can have any number of attestors, each one representing a party that participates in the authorization process for the image.

### Generate a key pair

Binary Authorization uses [cryptographic keys](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#cryptographic_keys) to securely verify the identity of [signers](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#signers). This ensures that only authorized container images can deploy. The key pair consists of a private key and a public key. The [signer](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#signers) uses the private key to sign the container image digest, producing a signature that is then stored in an [attestation](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations). The public key is stored in the [attestor](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors). At deploy time, the Binary Authorization enforcer uses the attestor's public key to verify the signature in the attestation before allowing the container to deploy.

In this tutorial, you use Public-Key Infrastructure (X.509) (PKIX) format for cryptographic keys. This tutorial uses the recommended [Elliptic Curve Digital Signature Algorithm (ECDSA)](https://docs.cloud.google.com/kms/docs/algorithms#asymmetric_signing_algorithms) to generate a PKIX key pair. You can also use RSA or PGP keys for signing. See [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms) for more information on signing algorithms.

The keys generated and stored by [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) (Cloud KMS) are PKIX-compliant. See [Creating attestors using the CLI](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli) for more information on using PKIX keys and Cloud KMS.

**Warning:** We strongly recommend against using locally generated key pairs in production environments as they present a security risk. We recommend that you instead use Cloud Key Management Service. This example is provided for illustrative purposes only. 

To generate a PKIX key pair, do the following:

  1. Create the private key:
         
         PRIVATE_KEY_FILE="/tmp/ec_private.pem"
         openssl ecparam -genkey -name prime256v1 -noout -out ${PRIVATE_KEY_FILE}
         

  2. Extract the public key from the private key:
         
         PUBLIC_KEY_FILE="/tmp/ec_public.pem"
         openssl ec -in ${PRIVATE_KEY_FILE} -pubout -out ${PUBLIC_KEY_FILE}
         




### Create the attestor

Now you can create the attestor itself in Binary Authorization and associate the public key that you created.

To create the attestor, do the following:

  1. Return to the Binary Authorization page in the Google Cloud console.

[Return to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

  2. In the **Attestors** tab, click **Create**.

![Screenshot of policy tab showing default rule](https://docs.cloud.google.com/static/binary-authorization/docs/images/default-rule-attestors-tab.png)

  3. Fill out the fields as follows:

     1. Enter `test-attestor` in the **Attestor name** field.

     2. Verify **Automatically create a Artifact Analysis note** is checked.

     3. Click **Add a PKIX Public Key**.

     4. Open `/tmp/ec_public.pem` in a text editor. This is the public key file that you created in the previous step. Copy the contents of the file to the **Public key material** text box.

     5. Click `Elliptic Curve P-256 - SHA256 Digest` in the **Signature algorithm** pull down.

     6. Click **Done**.

  4. Click **Create** to create the attestor.

  5. Store the public key ID.

To view your attestor's public key ID after adding it to the attestor, use `gcloud container binauthz attestors describe ${ATTESTOR_NAME}`. To create an environment variable to store the public key ID, execute the following command:
         
         ATTESTOR_NAME=test-attestor
         PUBLIC_KEY_ID=$(gcloud container binauthz attestors describe ${ATTESTOR_NAME}\
           --format='value(userOwnedGrafeasNote.publicKeys[0].id)')
         




## Configure the policy

Now, you can configure your policy:

  1. Return to the Binary Authorization page in Google Cloud console.

  2. In the **Policy** tab, click **Edit Policy**.

  3. Select **Allow Only Images That Have Been Approved By the Following Attestors**.

  4. Click **Add Attestors**.

  5. Click **Add by project and attestor name**.

  6. Enter PROJECT_ID in the **Project name** field.

  7. Enter `test-attestor` in the **Attestor name** field.

  8. Click **Add 1 Attestor**.

  9. Click **Save Policy**.


**Note:** It can take a few minutes for the policy to take effect.

For more information, see [Configuring a Policy Using the Console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console).

## Test the policy

You can test the policy you configured above by trying to deploy a sample container image to the cluster. The policy will block deployment because the required attestation has not been made.

For this tutorial, you can use sample images from Artifact Registry. The image from Artifact Registry is located at the path `us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0`. The path contains a public image created by Google that contains a "Hello, World!" sample application.

To try to deploy the image, execute the following command:
    
    
    kubectl run hello-server --image us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 --port 8080
    

Now, verify that the deployment was blocked by Binary Authorization:
    
    
    kubectl get pods
    

The command prints the following message, which indicates that the image was not deployed:
    
    
    No resources found.
    

You can get further details about the deployment:
    
    
    kubectl get event --template \
    '{{range.items}}{{"\033[0;36m"}}{{.reason}}:{{"\033[0m"}}\{{.message}}{{"\n"}}{{end}}'
    

You see a response that resembles the following:
    
    
    FailedCreate: Error creating: pods POD_NAME is forbidden: admission webhook "imagepolicywebhook.image-policy.k8s.io" denied the request: Image IMAGE_NAME denied by Binary Authorization default admission rule. Image IMAGE_NAME denied by ATTESTOR_NAME: No attestations found
    

In this output:

  * POD_NAME: the name of the Pod.
  * IMAGE_NAME: the name of the image.
  * ATTESTOR_NAME: the name of the attestor.



Make sure to delete the deployment so you can continue to the next step:
    
    
    kubectl delete deployment hello-server
    

## Create an attestation

An _attestation_ is a digital document created by a signer that certifies that GKE is allowed to deploy the associated container image. The process of creating an attestation is sometimes called "signing an image."

In this tutorial, you create an attestation for example images from Artifact Registry.

To create an attestation, do the following:

  1. Set variables that store the registry path and digest of the image, and the attestor name:

###  Artifact Registry 
         
         IMAGE_PATH="us-docker.pkg.dev/google-samples/containers/gke/hello-app"
         IMAGE_DIGEST="sha256:37e5287945774f27b418ce567cd77f4bbc9ef44a1bcd1a2312369f31f9cce567"
         ATTESTOR="test-attestor"
         IMAGE_TO_ATTEST=${IMAGE_PATH}@${IMAGE_DIGEST}
         

  2. Generate the attestation payload:

**Note:** In the following command, while an `${IMAGE_PATH}` is required to create the signature payload for the attestation, only the `${IMAGE_DIGEST}` is used at deploy time. This means you can deploy an identical container image from multiple locations with the same attestation.

###  Artifact Registry 
         
         gcloud container binauthz create-signature-payload \
         --artifact-url=${IMAGE_PATH}@${IMAGE_DIGEST} > /tmp/generated_payload.json
         

The payload JSON file has the following contents:
         
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
         

  3. Sign the payload with your PKIX private key and output a signature file:
         
         openssl dgst -sha256 -sign ${PRIVATE_KEY_FILE} /tmp/generated_payload.json > /tmp/ec_signature
         

The signature file is a digitally-signed version of the payload JSON file you created above.

  4. Create and validate the attestation:
         
         gcloud container binauthz attestations create \
             --project="${PROJECT_ID}" \
             --artifact-url="${IMAGE_TO_ATTEST}" \
             --attestor="projects/${PROJECT_ID}/attestors/${ATTESTOR_NAME}" \
             --signature-file=/tmp/ec_signature \
             --public-key-id="${PUBLIC_KEY_ID}" \
             --validate
         

where `PUBLIC_KEY_ID` is the public key id that you found in Generate a PKIX key pair above.

The `validate` flag checks that the attestation can be verified by the attestor you configured in your policy.

  5. Verify that the attestation was created:
         
         gcloud container binauthz attestations list \
             --attestor=$ATTESTOR_NAME --attestor-project=$PROJECT_ID
         




For more information on creating attestations, see [Creating Attestations](https://docs.cloud.google.com/binary-authorization/docs/making-attestations).

## Retest the policy

Again, test the policy by deploying a sample container image to the cluster. This time, you must deploy the image using the digest rather than a tag like `1.0` or `latest`, as Binary Authorization will use the digest to look up attestations. Here, Binary Authorization allows the image to be deployed because the required attestation has been made.

To deploy the image, execute the following command:
    
    
    kubectl run hello-server --image ${IMAGE_PATH}@${IMAGE_DIGEST} --port 8080
    

To verify that the image was deployed, execute the following command:
    
    
    kubectl get pods
    

The command prints a message similar to the following, which indicates that deployment was successful:
    
    
    NAME                            READY     STATUS    RESTARTS   AGE
    hello-server-579859fb5b-h2k8s   1/1       Running   0          1m
    

To delete the pod, execute the following command:
    
    
    kubectl delete pod hello-server
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

Delete the cluster that you created in GKE:
    
    
    gcloud container clusters delete \
        --zone=us-central1-a \
        test-cluster
    

## What's next

  * [Learn more about Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview)
  * [Learn key concepts used in Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/key-concepts)
  * Use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).
  * [Learn how to use image digests in Kubernetes manifests](https://docs.cloud.google.com/architecture/using-container-image-digests-in-kubernetes-manifests)
  * [Enable dry run mode to disable enforcement](https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
