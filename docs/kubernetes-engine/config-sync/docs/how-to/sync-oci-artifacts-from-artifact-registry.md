---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/sync-oci-artifacts-from-artifact-registry/
title: Sync OCI artifacts from Artifact Registry \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:06.319998+00:00
---

# Sync OCI artifacts from Artifact Registry  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/sync-oci-artifacts-from-artifact-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Sync OCI artifacts from Artifact Registry Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to create and publish your image to a repository in Artifact Registry with [`crane`](https://github.com/google/go-containerregistry/tree/main/cmd/crane) and [`oras`](https://oras.land/).

You can configure Config Sync to sync from [OCI](https://opencontainers.org/) images by using [Artifact Registry](https://docs.cloud.google.com/artifact-registry). To use this feature, you must enable the [RootSync and RepoSync APIs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

## About Artifact Registry

Artifact Registry is a fully-managed service with support for both container images and non-container artifacts. We recommend Artifact Registry for your container image storage and management on Google Cloud. There are many tools available to push artifacts to Artifact Registry. For example, you can [push a Docker image](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images#push) or use the [go-containerregistry library](https://github.com/google/go-containerregistry) to work with container registries. Choose the tool that works best for you.

**Caution:** Don't add base images to your OCI files stored in Artifact Registry. Because OCI images act as file storage, adding base images can cause permission issues when syncing.

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

  7. Enable the GKE, Config Sync, Artifact Registry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com  anthosconfigmanagement.googleapis.com  artifactregistry.googleapis.com

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

  13. Enable the GKE, Config Sync, Artifact Registry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com  anthosconfigmanagement.googleapis.com  artifactregistry.googleapis.com

  14. Create, or have access to, a cluster that meets the [requirements for Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/cluster-requirements) and is on the latest version of Config Sync.
  15. [Install the `nomos` CLI or upgrade it to the latest version.](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#installing)
  16. (Optional) If you want to use Cosign to verify OCI image signatures, install the following:
     * [Cosign](https://docs.sigstore.dev/cosign/system_config/installation/) to sign OCI images.
     * [OpenSSL](https://github.com/openssl/openssl) to generate credentials for the webhook server.
     * [Docker](https://docs.docker.com/get-started/get-docker/) to build and push the Admission Webhook server image.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [ Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Create an Artifact Registry repository

In this section, you create an Artifact Registry repository. To learn more about creating Artifact Registry repositories, see [Create repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).

Create an Artifact Registry repository:
    
    
    gcloud artifacts repositories create AR_REPO_NAME \
       --repository-format=docker \
       --location=AR_REGION \
       --description="Config Sync repo" \
       --project=PROJECT_ID
    

Replace the following:

  * `PROJECT_ID`: the organization's project ID.
  * `AR_REPO_NAME`: the ID of the repository.
  * `AR_REGION`: the regional or multi-regional location of the repository.



Variables used in the following sections:

  * `FLEET_HOST_PROJECT_NUMBER`: if you're using GKE Workload Identity Federation for GKE, this is the same as the project number for `PROJECT_ID`. If you're using fleet Workload Identity Federation for GKE, this is the project number of the fleet that your cluster is registered to.
  * `FLEET_HOST_PROJECT_ID`: if you're using GKE Workload Identity Federation for GKE, this is the same as `PROJECT_ID`. If you're using fleet Workload Identity Federation for GKE, this is the project ID of the fleet that your cluster is registered to.
  * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount for the reconciler: 
    * For root repositories, if the `RootSync` name is `root-sync`, add `root-reconciler`. Otherwise, add `root-reconciler-ROOT_SYNC_NAME`.
    * For namespace repositories, if the `RepoSync` name is `repo-sync`, add `ns-reconciler-NAMESPACE`. Otherwise, add `ns-reconciler-NAMESPACE-REPO_SYNC_NAME-REPO_SYNC_NAME_LENGTH` where `REPO_SYNC_NAME_LENGTH` is the number of characters in `REPO_SYNC_NAME`.



## Grant reader permission

Grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) on the repository to the Kubernetes ServiceAccount:
    
    
    gcloud artifacts repositories add-iam-policy-binding AR_REPO_NAME \
       --location=AR_REGION \
       --member="principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_HOST_PROJECT_ID.svc.id.goog/subject/ns/config-management-system/sa/KUBERNETES_SERVICEACCOUNT" \
       --role=roles/artifactregistry.reader \
       --project=PROJECT_ID \
       --condition=None
    

## Push an image to the Artifact Registry repository

In this section, you create an OCI image and push it to Artifact Registry.

  1. Create a `Namespace` manifest file:
         
         cat <<EOF> test-namespace.yaml
         apiVersion: v1
         kind: Namespace
         metadata:
           name: test
         EOF
         

  2. Sign in to Artifact Registry:
         
         gcloud auth configure-docker AR_REGION-docker.pkg.dev
         

  3. Package and push the image to Artifact Registry:

### `crane`

The commands in this section use `crane` to interact with remote images and registries.

     1. Package the file:
            
            tar -cf test-namespace.tar test-namespace.yaml
            

     2. Install the [`crane`](https://github.com/google/go-containerregistry/tree/main/cmd/crane) tool.

     3. Push the image to Artifact Registry:
            
            crane append -f test-namespace.tar -t AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME/test-namespace:v1
            

### `oras`

The commands in this section use `oras` to interact with remote images and registries.

     1. Package the file:
            
            tar -czf test-namespace.tar.gz test-namespace.yaml
            

     2. Install the [`oras`](https://oras.land/docs/installation) tool.

     3. Push the image to Artifact Registry:
            
            oras push AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME/test-namespace:v1 test-namespace.tar.gz
            

**Caution:** Config Sync requires that the OCI layer is compressed in the **`tar`** or **`tar+gzip`** format. Other formats (for example, `tar+bz2`) are not recognized by Config Sync. Switching from a valid REPO to an OCI image with an unsupported format will cause managed resources to be pruned without an error.



## Configure Config Sync to sync from your image

In this section, you'll create a `RootSync` object and configure Config Sync to sync from the OCI image.

  1. Create a `RootSync` object with a unique name:
         
         cat <<EOF>> ROOT_SYNC_NAME.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RootSync
         metadata:
           name: ROOT_SYNC_NAME
           namespace: config-management-system
         spec:
           sourceFormat: unstructured
           sourceType: oci
           oci:
             image: AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME/test-namespace:v1
             dir: .
             auth: k8sserviceaccount
         EOF
         

Replace `ROOT_SYNC_NAME` with the name of your `RootSync` object. The name should be unique in the cluster and have no more than 26 characters. For the full list of options when configuring `RootSync` objects, see [`RootSync` and `RepoSync` fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#configuring-oci-image).

  2. Apply the `RootSync` object:
         
         kubectl apply -f ROOT_SYNC_NAME.yaml
         

  3. Verify that Config Sync is syncing from the image:
         
         nomos status --contexts=$(kubectl config current-context)
         

You should see output similar to the following example:
         
         Connecting to clusters...
         
         *publish-config-registry
            --------------------
            <root>:root-sync-test   AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME/test-namespace:v1   
            SYNCED                  05e6a6b77de7a62286387cfea833d45290105fe84383224938d7b3ab151a55a1
            Managed resources:
               NAMESPACE   NAME             STATUS    SOURCEHASH
                           namespace/test   Current   05e6a6b
         

You have now successfully synced an image to your cluster.




## (Optional) Verify OCI source signatures

You can verify the authenticity of OCI source images before configurations are applied to your clusters. This method uses a `ValidatingWebhookConfiguration` object and a validating webhook server to intercept update requests for `RootSync` and `RepoSync` objects. Config Sync updates the `configsync.gke.io/image-to-sync` annotation of `RootSync` and `RepoSync` objects after it fetches a new image digest successfully. The validating webhook server compares values between the old annotation and the new annotation, and runs the validation with a validating tool like Cosign when a change is detected.

### Set up a signature verification server

To ensure the authenticity of your OCI sources, you need an HTTP server to verify the signatures. You can use the samples in the [Config Sync samples repository](https://github.com/GoogleCloudPlatform/anthos-config-management-samples/tree/main/pre-sync/oci-image-verification) or use your own Docker image.

  1. If you want to use the provided sample, complete the following steps:

     1. Clone the sample repository:
            
            git clone https://github.com/GoogleCloudPlatform/anthos-config-management-samples/
            

     2. Change to the directory that contains the signature verification server samples:
            
            cd anthos-config-management-samples/tree/main/pre-sync/oci-image-verification
            

  2. To create a Docker image for the signature verification server and push it to an image registry, run the following command:
         
         docker build -t SIGNATURE_VERIFICATION_SERVER_IMAGE_URL:latest . && docker push SIGNATURE_VERIFICATION_SERVER_IMAGE_URL:latest
         

Replace `SIGNATURE_VERIFICATION_SERVER_IMAGE_URL` with the URL of your signature verification server image.




### Authenticate to services

To set up your signature verification server, you must authenticate to Artifact Registry, the Cosign client, and the webhook server.

  1. Create a namespace:
         
         kubectl create ns signature-verification
         

  2. To authenticate to Artifact Registry with a Kubernetes ServiceAccount, complete the following steps:

     1. Create a Kubernetes ServiceAccount in the namespace that you created:
            
            kubectl create sa signature-verification-sa -n signature-verification
            

     2. Grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) on the repository to the Kubernetes ServiceAccount:
            
            gcloud artifacts repositories add-iam-policy-binding REPOSITORY_NAME \
               --location=REPOSITORY_LOCATION \
               --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/signature-verification/sa/signature-verification-sa" \
               --role=roles/artifactregistry.reader \
               --project=PROJECT_ID \
               --condition=None
            

Replace the following:

        * `REPOSITORY_NAME`: the name of your Artifact Registry repository where you store your OCI images.
        * `REPOSITORY_LOCATION`: the location of your Artifact Registry repository.
        * `PROJECT_NUMBER`: your project number.
        * `PROJECT_ID`: your project ID.
  3. To authenticate to the Cosign client, complete the following steps:

     1. Generate a pair of Cosign keys. This command generates a public and a private key:
            
            cosign generate-key-pair
            

     2. Store the public key in a Kubernetes Secret in the namespace that you created:
            
            kubectl create secret generic cosign-key --from-file=cosign.pub -n signature-verification
            

  4. To authenticate the signature verification server, complete the following steps:

     1. To encrypt communication within the signature verification server, generate a TLS certificate and private key with OpenSSL:
            
            openssl req -nodes -x509 -sha256 -newkey rsa:4096 \
            -keyout tls.key \
            -out tls.crt \
            -days 356 \
            -subj "/CN=signature-verification-service.signature-verification.svc"  \
            -addext "subjectAltName = DNS:signature-verification-service,DNS:signature-verification-service.signature-verification.svc,DNS:signature-verification-service.signature-verification"
            

     2. Store the credentials that you generated in a Kubernetes Secret:
            
            kubectl create secret tls webhook-tls --cert=tls.crt --key=tls.key -n signature-verification
            

     3. Get the base64-encoded content of the `tls.cert`. This is required for The validating webhook configuration that you create in the next section:
            
            cat tls.crt | base64 -w 0.
            




### Deploy the admission webhook

You can use the following samples to create a deployment for the signature verification server and a validating webhook configuration.

  1. Create a deployment for the signature verification server by saving the following file:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: signature-verification-server
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: signature-verification-server
           template:
             metadata:
               labels:
                 app: signature-verification-server
             spec:
               serviceAccountName: signature-verification-sa
               containers:
               - name: signature-verification-server
                 command:
                 - /signature-verification-server
                 image: SIGNATURE_VERIFICATION_SERVER_IMAGE_URL
                 imagePullPolicy: Always
                 ports:
                 - containerPort: 10250
                 volumeMounts:
                 - name: tls-certs
                   mountPath: "/tls"
                 - name: cosign-key
                   mountPath: "/cosign-key"
               volumes:
               - name: cosign-key
                 secret:
                   secretName: cosign-key
               - name: tls-certs
                 secret:
                   secretName: webhook-tls
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: signature-verification-service
         spec:
           ports:
           - port: 10250
             targetPort: 10250
           selector:
             app: signature-verification-server

Replace `SIGNATURE_VERIFICATION_SERVER_IMAGE_URL` with the full URL of the signature verification server image.

  2. Apply the deployment to the cluster:
         
         kubectl apply -f signature-verification-deployment.yaml -n signature-verification
         

  3. Create a validating webhook configuration by saving the following file:
         
         apiVersion: admissionregistration.k8s.io/v1
         kind: ValidatingWebhookConfiguration
         metadata:
           name: image-verification-webhook
         webhooks:
         - name: imageverification.webhook.com
           clientConfig:
             service:
               name: signature-verification-service
               namespace: signature-verification
               path: "/validate"
               port: 10250
             caBundle: CA_BUNDLE
           rules:
           - apiGroups:
             - configsync.gke.io
             apiVersions:
             - v1beta1
             - v1alpha1
             operations:
             - UPDATE
             resources:
             - 'rootsyncs'
             - 'reposyncs'
             scope: '*'
           admissionReviewVersions: ["v1", "v1beta1"]
           sideEffects: None

Replace `CA_BUNDLE` with the base64-encoded content from the `tls.cert`.

  4. Apply the validating webhook configuration to the cluster:
         
         kubectl apply -f signature-verification-validatingwebhookconfiguration.yaml
         




### Check logs for image verification errors

Once you have set up your image verification server, any attempts to sync from unsigned OCI images should fail.

To check for signature verification errors, view the logs from the signature verification server by running the following commands:

  1. Check `kubectl` logs:
         
         kubectl logs deployment  signature-verification-server -n  signature-verification
         

Errors from `kubectl` related to signature verification resemble the following:
         
         main.go:69: error during command execution: no signatures found
         

  2. Check Config Sync logs:
         
         nomos status
         

Errors from Config Sync related to signature verification resemble the following:
         
         Error:   KNV2002: admission webhook "imageverification.webhook.com" denied the request: Image validation failed: cosign verification failed: exit status 10, output: Error: no signatures found
         




If you don't get any errors, you can confirm that the signed image is the object being synced by inspecting your `RootSync` or `RepoSync` configuration:

###  `RootSync`
    
    
     kubectl get rootsync ROOTSYNC_NAME -n config-management-system -oyaml
    

Replace `ROOTSYNC_NAME` with the name of your `RootSync`.

###  `RepoSync`
    
    
     kubectl get reposync REPOSYNC_NAME -n REPOSYNC_NAMESPACE -oyaml
    

Replace the following:

  * `REPOSYNC_NAME`: the name of your `RepoSync`.
  * `REPOSYNC_NAMESPACE`: the name of the namespace associated with your `RepoSync`.



You should see the annotation `configsync.gke.io/image-to-sync` added to your `RootSync` or `RepoSync` object. The annotation contains the URL of the source OCI image and the latest digest fetched by Config Sync.

## What's next

  * Learn more about [installing Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync).
  * [Troubleshoot Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/troubleshooting-config-sync).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
