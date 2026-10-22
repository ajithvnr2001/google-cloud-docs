---
url: https://docs.cloud.google.com/apigee/docs/hybrid/preview/new-install-user-guide/
title: New Apigee hybrid installation and administration Preview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:54.870342+00:00
---

# New Apigee hybrid installation and administration Preview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/preview/new-install-user-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  New Apigee hybrid installation and administration Preview Stay organized with collections  Save and categorize content based on your preferences. 

**This preview is discontinued.**

**Preview — Apigee hybrid new install process (discontinued)**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

* * *

**Preview User Guide:**  
Preview of new installation and administration procedures for Apigee hybrid v1.8.

* * *

## In this document:

  * Preview
    * Feedback
  * Overview
    * Changes in the new installation process
  * Prerequisites
    * Preview version
    * Apigee hybrid setup
    * Tools
  * Basic Apigee Hybrid Installation
    * Download setup files
    * Run setup
  * Customized Apigee Hybrid installation
    * Download setup files
    * Create namespace
    * Using docker images from private repositories (optional)
    * Configuring imagePullSecrets (optional)
    * Configuring forward proxy (optional)
    * Specifying ingress TLS certificates
    * Update ingress deployment
    * Configuring custom Google Cloud service accounts
    * Using workload identities
    * Edit resource yamls
    * Create initialization resources and controller
    * Give permissions to Synchronizer service account to interact with Control Plane
    * Create Apigee data plane components
    * Wait for resources to start
    * Customize installation for cert-manager in a custom namespace
  * Kustomize and Components
    * Overview
    * How to use Components
    * OpenShift
    * imagepullsecret
    * nodeselector
    * workload-identity
    * http-proxy
    * logger and metrics
    * gcs-backup and gcs-restore
    * non-gcs-backup and non-gcs-restore
    * http-client
    * non-sni-client
    * http-and-non-sni-client
    * multi-region
  * Concepts
    * Adding a new environment
    * Using force delete in Apigee Datastore
  * Understanding the script
  * Apigee Hybrid Setup Folder Structure
  * Storing service account keys in external vaults
  * Apigee Hybrid Upgrade
    * Create Backup
    * Upgrade your Kubernetes platform if needed
    * Download setup files
    * Update service account permissions if needed
    * Upgrade controller
    * Update Apigee Kubernetes components
  * Apigee Hybrid Rollback
    * Restore apigee-hybrid-setup
    * Rollback Kubernetes components
    * Rollback controller
  * Cleanup
  * Deleting an environment
    * Deleting a hybrid setup
  * Multi Instance Installation
    * Multi Instance setup on GKE
    * Troubleshooting
    * Supportability, Diagnosis & Troubleshooting Guide
    * Manual Cleanup after using forceDelete in multi Region Apigee Hybrid setup



## Preview

* * *

**Note:** This document and the software it is documenting are part of a preview release. Apigee does not warranty the software or the procedures in this preview. The documentation and software are subject to change without notice.

This document is intended for the Apigee operator persona (users who install/manage/administer Apigee hybrid installations). Experience in installing Apigee hybrid on one of the supported Kubernetes platforms is a prerequisite for following the instructions in this document. It is recommended you create an evaluation Apigee org to try the steps below.

### Feedback

Please send feedback on this process to [Apigee-hybrid-install-preview@google.com](mailto:Apigee-hybrid-install-preview@google.com).

* * *

## Overview

The new Apigee hybrid installation experience installs Apigee components using [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) and integrates installation and management of Apigee Hybrid with Kubernetes configuration orchestration tools like [Kustomize](https://kustomize.io/). The enhanced validations and visibility of the components being installed provides better debuggability and improves the overall install process.

An install script, `apigee-hybrid-setup.sh`, provides an easy tool for basic installation. You can use that to create your hybrid installation and then modify it to fit your needs with `kubectl`, or you can create your hybrid installation from scratch using `kubectl`. All Apigee hybrid configuration properties are stored in yaml files, one for each major component. This allows much more granular control of your hybrid installation on your Kubernetes environment. You can find the configuration files and installation scripts in the [repository in GitHub](https://github.com/apigee/apigee-hybrid-install/releases/tag/preview-1).

### Changes in the new installation process

Apigee is changing the process of installing Apigee hybrid for the following reasons:

  * The new method of installing Apigee hybrid can be integrated with existing Kubernetes CI/CD tools like Argo, Flux or Anthos Config Management which do not use an [`overrides.yaml`](https://cloud.google.com/apigee/docs/hybrid/v1.8/config-prop-ref) configuration file.
  * Apigee hybrid has provided [`apigeectl`](https://cloud.google.com/apigee/docs/hybrid/v1.8/cli-reference), a custom templating tool that generates Kubernetes manifests (amongst other things) to install and manage Apigee hybrid in Kubernetes clusters. The new installation and management process provides an experience similar to that from other software vendors.
  * The new process enables basic installation quickly by automatically creating service accounts with the requisite permissions, TLS certificates, pre-populating defaults and other necessary foundational elements.



## Prerequisites

Before using this preview installation, you must meet the following prerequisites:

### Preview version

This preview is intended to work with [Apigee hybrid version 1.8.x](https://cloud.google.com/apigee/docs/hybrid/v1.8/what-is-hybrid). Later versions of Apigee hybrid are not supported.

### Apigee hybrid setup

Before proceeding with the actual installation of Apigee Hybrid, you are expected to have completed the following instructions listed in the following sections of the documentation:

  1. Project and Org setup 
     * [Overview](https://cloud.google.com/apigee/docs/hybrid/v1.8/precog-overview) for the prerequisites for installing Apigee hybrid.
     * [Step 1: Enable APIs](https://cloud.google.com/apigee/docs/hybrid/v1.8/precog-enableapi)
     * [Step 2: Create an organization](https://cloud.google.com/apigee/docs/hybrid/v1.8/precog-provision)
     * [Step 3: Create an environment and environment group](https://cloud.google.com/apigee/docs/hybrid/v1.8/precog-add-environment)
  2. Hybrid runtime Setup 
     * [Step 1: Create a cluster](https://cloud.google.com/apigee/docs/hybrid/v1.8/install-create-cluster)
     * [Step 2: Install cert-manager](https://cloud.google.com/apigee/docs/hybrid/v1.8/install-cert-manager)



### Tools

In addition, you need to have the following tools downloaded and configured on your workstation:

  * `curl`
  * `docker` is required to run the `apigee-hybrid-setup.sh` script. Follow the instructions at [Get Docker](https://docs.docker.com/get-docker/) to install Docker.
  * `envsubst` should be available in most Linux/UNIX based systems. For MacOS and other systems, [follow the instructions in this repo](https://github.com/a8m/envsubst).
  * `jq` should be installed. [Download jq](https://stedolan.github.io/jq/download/).
  * `kpt` [Download kpt](https://kpt.dev/installation/).

**Note:** KPT versions v0.39 and below are not supported. Download kpt from the link mentioned above (v1.0+) to ensure that it's working.
  * `kubectl` version 1.23 or newer. See [Install Tools: kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) in the kubernetes documentation.




## Common variables used in this guide

This guide uses the following environment variables in several steps. You can define them at the command line or with a script, or you can replace the text in the commands when you enter them.

  * `APIGEE_NAMESPACE`: Your Apigee namespace. By default this is `apigee`. However, you can use a different namespace.
  * `CLUSTER_NAME`: The name of the cluster where you are installing Apigee hybrid. This is the cluster you create in [Step 1: Create a Cluster](https://cloud.google.com/apigee/docs/hybrid/v1.8/install-create-cluster)
  * `CLUSTER_LOCATION`: The region of your cluster. The procedures in this guide assume you are using a regional cluster. If you are using a zonal cluster, see the instructions in [Step 1: Create a Cluster](https://cloud.google.com/apigee/docs/hybrid/v1.8/install-create-cluster)
  * `ENV_GROUP`: The name of the environment group for your Apigee hybrid installation. This is the environment group you create in [Step 3: Create an environment group](https://cloud.google.com/apigee/docs/hybrid/v1.8/precog-add-environment). You can create multiple environment groups.
  * `ENV_NAME`: The name of the environment group for your Apigee hybrid installation. This is the environment group you create in [Step 3: Create an environment group](https://cloud.google.com/apigee/docs/hybrid/v1.8/precog-add-environment). You can create multiple environment groups.
  * `INSTALL_DIR`: The directory where you install Apigee hybrid. By default, this is the `apigee-hybrid-install/` subdirectory of the directory where you download the installer, for example: `/myhybrid/apigee-hybrid-install/`. This is the root directory for the file structure documented in Apigee Hybrid Setup Folder Structure.
  * `INSTANCE_DIR`: The directory for a specific Apigee hybrid instance. By default, the first instance is named `instance-1`. The instance dir is a subdirectory of `${INSTALL_DIR}/overlays/instances/`. You can specify any name for your hybrid instances. See Multi Instance Installation.
  * `ORG_NAME`: The name of your Apigee hybrid organization. This must be the same as your Google Cloud project ID. See: [Step 2: Create an organization](https://cloud.google.com/apigee/docs/hybrid/v1.8/precog-provision).



## Basic Apigee hybrid installation

To quickly install Apigee Hybrid without heavy customization, you can use the following two-step procedure.

* * *

**Note:** A basic installation has the following configuration:

  * A single environment
  * A single environment group
  * A single Google Cloud service account is created and used for all the individual components
  * Default values for all encryption keys and passwords.



* * *

  1. Download setup files
  2. Run setup



### Download setup files

Download and prepare the setup files by cloning the GitHub repository at `https://github.com/apigee/apigee-hybrid-install/releases/tag/preview-1`:

  1. Clone the repository:
         
         git clone https://github.com/apigee/apigee-hybrid-install.git
         

  2. Navigate to the directory for the cloned repository:
         
         cd apigee-hybrid-install
         

  3. Create a branch from the preview-1 tag:
         
         git branch preview-1 preview-1
         git checkout preview-1
         

  4. Make the setup script executable:
         
         chmod +x ./tools/apigee-hybrid-setup.sh
         

The cloned repository will have a structure resembling the one described in Apigee Hybrid Setup Folder Structure:




### Run setup

Run the `apigee-hybrid-setup.sh` shell script located inside the `tools/` folder.
    
    
    ./tools/apigee-hybrid-setup.sh --cluster-name $CLUSTER_NAME --cluster-region $CLUSTER_LOCATION --org $ORG_NAME --setup-all
    

* * *

**Note:** Running the script with these arguments uses the Apigee Organization, Environment, and Environment group you created in Prerequisites.

If you encounter errors try running the script a second time.

* * *

Additional options you may want to use are:

  * `--env $ENV_NAME` specifies the name of the Apigee environment.
  * `--envgroup $ENV_GROUP` specifies the environment group.
  * `--ingress-domain $HOSTNAME` specifies the hostname you supplied for your environment group.
  * `--gcp-project-id $PROJECT_ID` specifies the id of your Google Cloud project.



For more options, refer to Understanding the script.

Any errors during the execution will be printed to standard output.

Once the script completes successfully, you will have completed the basic hybrid installation. You can test your installation by creating a sample proxy as detailed in [Create and deploy a new API proxy](https://cloud.google.com/apigee/docs/hybrid/v1.8/install-deploy-proxy).

## Customized Apigee Hybrid installation

For more advanced users who would like fine grained control over the installation, you can follow the these sequence of steps (for many of the steps given below, you can choose to either perform the step manually, or use the shell script to automate that individual step):

* * *

**Note:** These steps require a basic understanding of kubernetes concepts. Refer to the Concepts section or [Kubernetes Documentation](https://kubernetes.io/docs/home/) for more details.

* * *

### Download setup files

Download and prepare the setup files:

  1. Clone the GitHub repository at `https://github.com/apigee/apigee-hybrid-install/`

The cloned repository will have a structure resembling the one described in Apigee Hybrid Setup Folder Structure:

  2. `cd` into the `apigee-hybrid-install/` directory

  3. Make the setup script executable:
         
         chmod +x ./tools/apigee-hybrid-setup.sh
         




### Create namespace

Create a kubernetes namespace in your cluster which will contain all the Apigee cluster components.
    
    
    kubectl create namespace apigee
    

* * *

**Note:** Apigee is the default name for the namespace. You can use a different name.

* * *

If you choose another name for the namespace, then you can choose to follow one of the three options below:

  * (Recommended) Use `--namespace={YOUR_NAMESPACE_NAME}` while prefilling values in Edit resource yamls.
  * Run the two following commands:

    1. Use `kpt` to specify the Apigee namespace:
           
           kpt fn eval "${INSTALL_DIR}/overlays/" \
             --image gcr.io/kpt-fn/apply-setters:v0.2.0 -- \
             APIGEE_NAMESPACE="${APIGEE_NAMESPACE}"
           # This is for replacing the namespace in istio discoveryAddress which cannot be
           # achieved with kpt
           

    2. Use `sed` to replace the namespace in istio discoveryAddress:
           
           sed -i -E -e "s/(discoveryAddress: apigee-ingressgateway-manager\.).*(\.svc:15012)/\1${APIGEE_NAMESPACE}\2/" "${INSTALL_DIR}/overlays/controllers/istiod/apigee-istio-mesh-config.yaml"
           

  * As an alternative, you can manually change the resources individually to be created in the namespace of your choice.




### Using docker images from private repositories (optional)

You can choose to not use the publicly hosted images, and can use images from your own private repositories:

  1. The first step is to push all the images to your private repo, which can be done by following the steps in [apigee-pull-push | Apigee X](https://cloud.google.com/apigee/docs/hybrid/v1.8/apigee-pull-push). By default, images are tagged with the Apigee Hybrid version which they correspond to, and it is recommended that you do not edit these tags. We also recommend that you not edit the image names either so that the final image path can be constructed as explained in Image Hub.
  2. Set the value of `imageHub` field present inside file apigee-hybrid-config.yaml to the private repo host path. (Refer to Image Hub for details).
         
         imageHub: "your.private.repo/apigee/hybrid"
         




This will ensure that all the Apigee hybrid components use the images from your private repo.

In addition to this, you may also want to use a private image for the controller and Apigee ingress gateway, for which, you will have to edit the apigee-controller-deployment.yaml and apigee-ingressgateway-manager-deployment.yaml files and replace all the `image` fields with the image from their private repo.

* * *

**Note:** If you are pulling images from a private repository, then most likely you'll need to authenticate in order to pull those images. The credentials required for this authentication are specified as `imagePullSecrets`, which has been discussed in detail in Configuring imagePullSecrets (optional).

* * *

### Configuring imagePullSecrets (optional)

  1. Create a [kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) containing the credentials to authenticate with the private repositories. Refer [Pull an Image from a Private Registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/) to understand how the secret has to be created.
  2. Once the secret is created, all that's left is to refer to that secret, which can be done by editing the file apigee-hybrid-config.yaml and setting the value of the `imagePullSecret` field to the name of the secret created previously, and enable the `imagePullSecret` component in the corresponding `kustomization.yaml` file.



* * *

**Note:** If you are using private images for the controller as well, then you may also need to add `imagePullSecret`s fields in the deployment spec present in the `apigee-controller-deployment.yaml` and `apigee-ingressgateway-manager-deployment.yaml` files.

If in case you do specify the `imagePullSecrets` in both the places, the one present inside apigee-controller-manager.yaml file will take precedence.

* * *

### Configuring forward proxy (optional)

Forward proxies can be configured by adding the `forwardProxy` field to the `apigee-hybrid-config.yaml` file. For example:
    
    
      forwardProxy: |
        scheme: HTTP
        host: 10.12.0.47
        port: 3128
    

### Specifying ingress TLS certificates

#### Using the script
    
    
    ./tools/apigee-hybrid-setup.sh --create-ingress-tls-certs
    

Refer - Understanding the script for more details about this flag.

#### Manual

You are expected to provide TLS certificates which will be used for istio ingress gateway. You can:

  * either use certificates signed by a known authority using the steps mentioned in [Obtain TLS certificates: An example | Apigee X](https://cloud.google.com/apigee/docs/hybrid/v1.8/lets-encrypt)
  * or generate self signed certificates.



Here we'll use self signed certificates as an example. Self signed certificates can be generated using (assuming `DOMAIN`has been properly set and should match the hostname set in your envgroup):
    
    
    openssl req -nodes -new -x509 -keyout ./tls.key -out ./tls.crt -subj '/CN='$DOMAIN'' -days 3650
    

This will create two files named `tls.key` and `tls.crt`.

You then need to create a secret having the following format You can use `kubectl create` or `kubectl apply` as explained in Using custom certificate/key pair for certificate signing authority (optional):
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: "{ORG_NAME}-{ENV_GROUP_NAME}"
      namespace: {$APIGEE_NAMESPACE}
    type: Opaque
    data:
      cert: |
        {BASE64_ENCODED_TLS_CRT}
      key: |
        {BASE64_ENCODED_TLS_KEY}
    
    ---
    

Example of creating the secret using `kubectl create`:
    
    
    kubectl create secret tls {ORG_NAME}-{ENV_GROUP_NAME} \
      --cert="tls.crt" \
      --key="tls.key" \
      -n {$APIGEE_NAMESPACE}
    

* * *

**Note:** If you change the name of the secret above, you'll need to make a corresponding change in `apigee-route-config.yaml` by changing the value of `secretNameRef` to **_YOUR_SECRET_NAME_**

* * *

### Update ingress deployment

To create/modify ingress deployments - you need to modify the `spec.components.ingressGateways` field in the ApigeeOrganization Custom Resource in `bases/initialization/crds/customresourcedefinition-apigeeorganizations.apigee.cloud.google.com.yaml`.

By default, we create one ingress deployment with default parameters(default values will be shown in the CR reference docs ):
    
    
    ingressGateways:
    - name: "prod-1"
    

Examples:

A. Overriding ingress service fields
    
    
    ingressGateways:
    - name: "prod-1"
      serviceSpec:
        annotations:
          {KEY}: ${VALUE}
        loadBalancerIP: ${IP}
    

B. Change replica Min/Max
    
    
    ingressGateways:
    - name: "prod-1"
      ​​autoScaler:
        minReplicas: 4
        maxReplicas: 10
    

C. Adding new Ingress Deployment
    
    
    ingressGateways:
    - name: "prod-1"
    - name: "prod-2"
    

### Configuring custom Google Cloud service accounts

* * *

**Note:** One of Configuring custom Google Cloud service accounts or Using workload identities is mandatory)

* * *

#### Using the script
    
    
    ./tools/apigee-hybrid-setup.sh --create-gcp-sa-and-secrets  --namespace APIGEE_NAMESPACE
    

Where APIGEE_NAMESPACE is your custom namespace. The default namespace is `apigee`.

Refer to Understanding the script for more details about the flags.

#### Manual

Google Cloud service account keys need to be stored as secrets in the cluster. The secret yaml should have the following structure:
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: "{NAME}"
      namespace: {APIGEE_NAMESPACE}
    type: Opaque
    data:
      client_secret.json: |
        {BASE64_ENCODED_SA_KEY}
    

For more details about what all service accounts are required and the names of the secrets, refer to the Google Cloud service accounts section.

You are free to choose a different name for the secrets but then you'll have to make a corresponding change in the component where that secret name was used. For example, if you decide to change the name of the runtime service account secret from `apigee-runtime-svc-account-${ORG_NAME}-${ENV_NAME}` to `my-runtime-svc`, you will have to make a corresponding change in the `apigee-environment.yaml` for that environment

* * *

**Note:** The secrets which contain the service account keys can be sourced from external secret management tools like Vault. Refer Storing service account keys in external vaults section for details on how to do that.

* * *

### Using workload identities

* * *

**Note:** Workload identities can only be used with GKE clusters in Google Cloud.

One of Configuring custom Google Cloud service accounts or Using workload identities is mandatory.

* * *

#### Prerequisites

Before using workload identities, make sure that your GKE cluster has the support enabled. Refer [Updating Node Pools | Apigee X](https://cloud.google.com/apigee/docs/hybrid/v1.8/enable-workload-identity#update-node-pools) for details.

#### Enabling workload-identity

Refer Workload identities section under Kustomize and Components for details on how you can enable workload identities before installation.

### Edit resource yamls

Some places in the component yamls require the correct organization, environment and environment group names to be present. You can set these values either manually, or use the shell script to automatically fill these values.

#### Using the script
    
    
    ./tools/apigee-hybrid-setup.sh --fill-values
    

### Create initialization resources and controller
    
    
    #Additional steps for openshift
    kubectl apply -k ${INSTALL_DIR}/overlays/initialization/openshift
    //apigee datastore
    kubectl apply -f ${INSTANCE_DIR}/overlays/instances/${INSTANCE_DIR}/datastore/components/openshift-scc/scc.yaml
    //telemetry
    kubectl apply -f ${INSTANCE_DIR}/overlays/instances/${INSTANCE_DIR}/telemetry/components/openshift-scc/scc.yaml
    
    #Create Apigee initialization kubernetes resources
    kubectl apply -f ${INSTALL_DIR}/overlays/initialization/namespace.yaml
    kubectl apply -k ${INSTALL_DIR}/overlays/initialization/certificates
    kubectl apply --server-side --force-conflicts -k ${INSTALL_DIR}/overlays/initialization/crds
    kubectl apply -k ${INSTALL_DIR}/overlays/initialization/webhooks
    kubectl apply -k ${INSTALL_DIR}/overlays/initialization/rbac
    kubectl apply -k ${INSTALL_DIR}/overlays/initialization/ingress
    
    # Create controller config and controller
    kubectl apply -k ${INSTALL_DIR}/overlays/controllers
    
    # Wait for the controllers to be available
    kubectl wait deployment/apigee-controller-manager deployment/apigee-ingressgateway-manager -n "${APIGEE_NAMESPACE}" --for=condition=available --timeout=2m
    
    # Create the datastore and redis secrets first and then the rest of the secrets.
    kubectl apply -f ${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}/datastore/secrets.yaml
    kubectl apply -f ${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}/redis/secrets.yaml
    kubectl apply -f ${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}/environments/${ENV_NAME}/secrets.yaml
    kubectl apply -f ${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}/organization/secrets.yaml
    

### Give permissions to Synchronizer service account to interact with Control Plane

Follow the steps in [Step 8: Enable Synchronizer access](https://cloud.google.com/apigee/docs/hybrid/v1.8/install-enable-synchronizer-access), replacing name of the service account, either `apigee-non-prod` or `apigee-synchronizer`, with `apigee-all-sa`, the name of the service account created by the new install process.

* * *

**★ Important:** Make sure to change the service account name in the instructions under [Enable synchronizer access](https://cloud.google.com/apigee/docs/hybrid/v1.8/install-enable-synchronizer-access#enable-synchronizer-access). Otherwise enabling access for synchronizer will fail.

* * *

### Create Apigee data plane components

If you had changed the names of any of the resources in the previous steps, you'll need to make a corresponding change in other YAML files where that resource was referenced. Once that's done, use the commands in the following example:
    
    
    # Create the rest of the resources.
    kubectl apply -k ${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}
    

to install all the components.

### Wait for resources to start
    
    
    kubectl wait "apigeedatastore/default" \
    "apigeeredis/default" \
    "apigeeenvironment/${ORG_NAME}-${ENV_NAME}" \
    "apigeeorganization/${ORG_NAME}" \
    "apigeetelemetry/apigee-telemetry" \
    -n "${APIGEE_NAMESPACE}" --for="jsonpath=.status.state=running" --timeout=15m
    

### Customize installation for cert-manager in a custom namespace

Customize the namespace where cert-manager is running with the following procedure.

If cert-manager is installed in your cluster in a namespace other than cert-manager you will need to update the namespace used to create the Apigee root certificate.

  1. Edit the customization.yaml file for the certificate creation: `$INSTALL_DIR/overlays/initialization/certificates/kustomize.yaml`
  2. Add the following to the end of the file.
         
         - patch: |-
         - op: replace
           path: /metadata/namespace
           value: "gk-cert-manager"
         target:
         group: cert-manager.io
         version: v1
         kind: Certificate
         name: apigee-root-certificate
         

  3. Save the file




## Kustomize and Components

### Overview

The new Hybrid Installation inherits the [Kustomize](https://kustomize.io/) ideology of structuring yamls in the form of [Bases](https://kubectl.docs.kubernetes.io/references/kustomize/glossary/#base) and [Overlays](https://kubectl.docs.kubernetes.io/references/kustomize/glossary/#overlay)

  * Bases are files supplied by Apigee, which might change between each new Hybrid release. You are not expected to modify these files. These files hold some default values that are supplied by Apigee. All files under the top level `bases/` folder contain these Bases
  * Overlays hold user configuration and serve as the means through which you can modify default values specified in the Bases. All files under the top level `overlays/` folder contain these Overlays

* * *

**Note:** For a better understanding of Kustomize and how overlays have been used to modify bases, it is strongly recommended that you go through [Kustomize Patches](https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/patches/).

* * *




### How to use Components

The subfolders within the top level `overlays/` directory have been structured in such a way that you can enable (or disable) a certain additional feature by commenting (or uncommenting) certain lines in the `kustomization.yaml` files.

For example, this is what the `overlays/instances/{INSTANCE_NAME}/telemetry` folder structure looks like:
    
    
    telemetry
    ├── components
    │   ├── http-proxy
    │   ├── imagepullsecret
    │   ├── logger
    │   ├── metrics
    │   ├── nodeselector
    │   ├── openshift-scc
    │   ├── workload-identity-logger
    │   └── workload-identity-metrics
    ├── apigee-telemetry.yaml
    └── kustomization.yaml
    

Here's how the `telemetry/kustomization.yaml` files would probably look like by default:
    
    
    resources:
    - apigee-telemetry.yaml
    
    components:
    - ./components/metrics
    # - ./components/workload-identity-metrics
    # - ./components/logger
    # - ./components/workload-identity-logger
    # - ./components/http-proxy
    # - ./components/nodeselector/
    # - ./components/imagepullsecret
    # - ./components/openshift-scc
    

We can see that the `./components/logger` has been commented out, which simply means that we've not enabled uGoogle Clod logger by default. In order to enable that, you can simply uncomment that line like so:
    
    
    components:
    
    - ./components/logger
    

Similarly, to disable metrics, you can comment out the `./components/metrics` line:
    
    
    ...
    components:
    ...
    # - ./components/metrics
    …
    

The following sections will talk about all such various components, when they can be used, and how they can be configured.

### OpenShift

For users who wish to install Apigee Hybrid in an `OpenShift` cluster, you might need to enable a few components/resources **before performing the install**. (This is required if you don't use the script to perform the installation). The files which need to be modified are:

  * `overlays/initialization/openshift/kustomization.yaml` . Under `resources:` section, uncomment:
        
        # - ../../../bases/initialization/openshift/
        

  * `overlays/instances/{INSTANCE_NAME}/datastore/kustomization.yaml` Uncomment:
        
        # - ./components/openshift-scc
        

and uncomment the "`components:`" field if it is still commented out.

  * `overlays/instances/{INSTANCE_NAME}/telemetry/kustomization.yaml` Uncomment:
        
        # - ./components/openshift-scc
        

and uncomment the "`components:`" field if it is still commented out.




You can then proceed with the installation steps.

### `imagepullsecret`

This component can be enabled when you have images stored in your private repository. To pull images from a private repository, you can create a kubernetes secret which will have your authentication details and can then reference this secret inside. See [Configuring imagePullSecrets (optional)](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/preview/new-install-user-guide#configuring-imagepullsecrets-\(optional\)) for instructions. Refer to [Pull an Image from a Private Registry | Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/) in the Kubernetes documentation for more information.

#### Available in:

  * `overlays/controllers/apigee-controller`
  * `overlays/controllers/istiod`
  * `overlays/instances/{INSTANCE_NAME}/datastore`
  * `overlays/instances/{INSTANCE_NAME}/environments/{ENV_NAME}`
  * `overlays/instances/{INSTANCE_NAME}/organization`
  * `overlays/instances/{INSTANCE_NAME}/redis`
  * `overlays/instances/{INSTANCE_NAME}/telemetry`



#### Enabling:

Uncomment the "`./components/imagepullsecret/`" line in the respective `kustomization.yaml` files wherever required.

#### Modifications to be made:

  * components/imagepullsecret/patch.yaml 
    * _REQUIRED_ Add relevant secret names to the list in `spec.template.spec.imagePullSecrets`



#### Usage:

  1. If you have not yet installed Apigee Hybrid, you can continue with the installation steps and these changes will get applied in the process
  2. If you already have Apigee Hybrid installed, you will need to apply these new changes using:
         
         kubectl apply -k overlays/instances/{INSTANCE_NAME}
         




### `nodeselector`

This component allows you to schedule pods for an Apigee resource on specific nodes. Refer to [Assigning Pods to Nodes | Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) for additional information.

#### Available in:

  * `overlays/controllers/apigee-controller`
  * `overlays/controllers/istiod`
  * `overlays/instances/{INSTANCE_NAME}/datastore`
  * `overlays/instances/{INSTANCE_NAME}/environments/{ENV_NAME}`
  * `overlays/instances/{INSTANCE_NAME}/organization`
  * `overlays/instances/{INSTANCE_NAME}/redis`
  * `overlays/instances/{INSTANCE_NAME}/telemetry`



#### Enabling:

Uncomment the "`./components/nodeselector`" line in the respective `kustomization.yaml` files wherever required.

#### Modifications to be made:

  * components/nodeselector/patch.yaml 
    * _OPTIONAL_ Change the value of the node selector label from `apigee-runtime` or `apigee-data` to the desired one.



#### Usage:

  1. If you have not yet installed Apigee Hybrid, you can continue with the installation steps and these changes will get applied in the process
  2. If you already have Apigee Hybrid installed, you will need to apply these new changes using:
         
         kubectl apply -k overlays/instances/{INSTANCE_NAME}
         




### workload-identity

Various containers in the Apigee Hybrid ecosystem require permissions to make certain API calls to the Apigee Control Plane / Management Plane. Workload identity is one of granting the pods (and the containers within) these permissions. Useful resources to read more about this include: \- [Introducing Workload Identity: Better authentication for your GKE applications | Google Cloud Blog](https://cloud.google.com/blog/products/containers-kubernetes/introducing-workload-identity-better-authentication-for-your-gke-applications) \- [Use Workload Identity | Kubernetes Engine Documentation | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

#### Available in:

  * `overlays/instances/{INSTANCE_NAME}/datastore`
  * `overlays/instances/{INSTANCE_NAME}/environments/{ENV_NAME}`
  * `overlays/instances/{INSTANCE_NAME}/organization`
  * `overlays/instances/{INSTANCE_NAME}/redis`
  * `overlays/instances/{INSTANCE_NAME}/telemetry`



#### Prerequisite:

Before you are able to make use of workload identity, you'll need to grant the relevant permissions within you Google Cloud project using:
    
    
        gcloud iam service-accounts add-iam-policy-binding \
            --role roles/iam.workloadIdentityUser \
            --member "serviceAccount:${ORG_NAME}.svc.id.goog[${APIGEE_NAMESPACE}/${KSA_NAME}]" \
            ${GSA_NAME}@${ORG_NAME}.iam.gserviceaccount.com
    

where: \- ${ORG_NAME} - The name of your Apigee Organization. \- ${APIGEE_NAMESPACE} - The kubernetes namespace where Apigee components have been installed. This would usually be `apigee` unless explicitly changed by the user during the installation \- ${KSA_NAME} - The name of the kubernetes namespace. **You will need to run this command for each kubernetes service account mentioned inKubernetes service accounts** \- ${GSA_NAME} - The name of the Google Cloud service account. If you have not made any changes during installation, this will have the value `apigee-all-sa`. If you set up multiple Google Cloud service accounts for individual components, you'll need to match the KSA_NAME with the corresponding GSA_NAME. You can compare the tables in Google Cloud service accounts with Kubernetes service accounts to find the equivalents.

#### Enabling:

Uncomment the `./components/workload-identity` line in the respective `kustomization.yaml` files wherever required. Note that within telemetry, we have separate workload identity addons for `metrics` and `logger` components which can be enabled individually.

#### Usage:

  1. If you have not yet installed hybrid, you can simply enable the workload-identity as mentioned in the previous section and continue with the installation which will then automatically use workload-identity.
  2. If you already have Apigee Hybrid installed, you will need to apply these new changes using:
         
         kubectl apply -k overlays/instances/{INSTANCE_NAME}
         




### `http-proxy`

You can configure a proxy server in each of the following components so that traffic for that component goes through the http proxy configured for that component. You can configure the proxy for each Apigee component individually.

#### Available in:

  * `overlays/instances/{INSTANCE_NAME}/datastore`
  * `overlays/instances/{INSTANCE_NAME}/environments/{ENV_NAME}`
  * `overlays/instances/{INSTANCE_NAME}/organization`
  * `overlays/instances/{INSTANCE_NAME}/telemetry`



#### Enabling:

Uncomment the "`./components/http-proxy/`" line in the respective `kustomization.yaml` files wherever required.

#### Modifications to be made:

  * components/http-proxy/patch.yaml Following parameters can be configured under the `spec.httpForwardProxy`
    * `scheme`: _REQUIRED_ One of `HTTP` or `HTTPS`
    * `host`: _REQUIRED_ The Host address of your proxy
    * `port`: _REQUIRED_ The port number
    * `username`: _OPTIONAL_ The username associated with your proxy
    * `password`: _OPTIONAL_ The password for accessing the proxy



#### Usage:

  1. If you have not yet installed Apigee Hybrid, you can continue with the installation steps and these changes will get applied in the process
  2. If you already have Apigee Hybrid installed, you will need to apply these new changes using:
         
         kubectl apply -k overlays/instances/{INSTANCE_NAME}
         




### logger and metrics

You can individually enable or disable logger or metrics within overlays/instances/{INSTANCE_NAME}/telemetry. By default, logger is disabled and metrics are enabled. Enabling or disabling them is simply uncommenting or commenting their lines in the telemetry/kustomization.yaml

### gcs-backup and gcs-restore

This kustomize component can be used to perform a backup and restore for the cassandra database to Google Cloud Storage.

#### Available in:

  * `overlays/instances/{INSTANCE_NAME}/datastore`



#### Prerequisite:

  1. Download the Google Cloud service accounts keys for an account which has the Storage Object Admin role.

     * If you used the script to perform the installation and did not use workload-identities you can reuse the downloaded keys available under the service-accounts folder which gets created by the script.
     * You could also use the create-service-account.sh script to create a new service account and download its keys:
           
           ./tools/create-service-accounts=.sh --env prod --profile apigee‑cassandra
           

  2. Once the keys have been downloaded, you need to create a kubernetes secret with the name apigee-cassandra-backup-and-restore-gcp-sa-key which can be done using the command:
         
         kubectl create secret generic "apigee-cassandra-backup-and-restore-gcp-sa-key" \
                   --from-file="dbbackup_key.json=${PATH_TO_SA_KEY}" \
                   -n "${APIGEE_NAMESPACE}"
         

Where:

     * ${PATH_TO_SA_KEY} \- Path to the file containing the service account keys.
     * ${APIGEE_NAMESPACE} \- The kubernetes namespace where Apigee components have been installed. This would usually be apigee unless, explicitly changed during the installation



Alternatively, you can use the template file templates/secret-apigee-cassandra-backup-and-restore-gcp-sa-key.yaml to create this secret.

#### Enabling:

  * If you want to enable backup, uncomment the "./components/gcs-backup" line in the datastore kustomization.yaml file.
  * If you want to restore a backup, uncomment the "./components/gcs-restore" line in the datastore kustomization.yaml file.



#### Modifications for backup only

  * components/gcs-backup/apigee-datastore-patch.yaml 
    * _REQUIRED_ Change value of DATABASE_STORAGE_BUCKET environment variable which will be of the form gs://BUCKET_NAME and points to the Google Cloud Storage bucket where data needs to be backed up. Description matches dbStorageBucket [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/backup-recovery#scheduling-cassandra-backups).
  * components/gcs-backup/cron-patch.yaml 
    * _REQUIRED_ Change spec.schedule to specify the frequency of the backup. Field accepts the standard Crontab schedule format. Description matches schedule [described here](https://cloud.google.com/apigee/docs/hybrid/1.8/backup-recovery#scheduling-cassandra-backups).
    * _REQUIRED_ Change value of DATABASE_STORAGE_BUCKET environment variable which will be of the form gs://BUCKET_NAME and points to the Google Cloud Storage bucket where data needs to be backed up. Description matches dbStorageBucket [described here](https://cloud.google.com/apigee/docs/hybrid/latest/backup-recovery#scheduling-cassandra-backups).
    * _OPTIONAL_ Change value of HTTP_PROXY_URL to point to any proxy configured. The format could be as follows: 
      * `http://${USERNAME}:${PASSOWORD}@${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `https://${USERNAME}:${PASSOWORD}@${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `http://${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `http://${HOST_IP_ADDRESS>:${HOST_PORT}`



#### Performing Backup

You can perform the backup with the following command:
    
    
    kubectl apply -k overlays/instances/{INSTANCE_NAME}
    

To apply you changes and enable the backup:

#### Modifications for restore only

  * components/gcs-restore/apigee-datastore-patch.yaml 
    * _REQUIRED_ Change value of DATABASE_STORAGE_BUCKET environment variable which will be of the form gs://BUCKET_NAME and points to the Google Cloud Storage bucket where data needs to be backed up. Description matches dbStorageBucket [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/backup-recovery#scheduling-cassandra-backups).
  * components/gcs-restore/job-patch.yaml 
    * _REQUIRED_ Change value of DATABASE_STORAGE_BUCKET environment variable which will be of the form gs://BUCKET_NAME and points to the Google Cloud Storage bucket where data needs to be backed up.
    * _REQUIRED_ Change value of BACKUP_SNAPSHOT_TIMESTAMP environment variable. Description matches restore:snapshotTimestamp [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/backup-recovery#scheduling-cassandra-backups).
    * _OPTIONAL_ Change value of HTTP_PROXY_URL to point to any proxy configured. The format could be as follows: 
      * `http://${USERNAME}:${PASSOWORD}@${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `https://${USERNAME}:${PASSOWORD}@${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `http://${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `http://${HOST_IP_ADDRESS}:${HOST_PORT}`



#### Performing the restore:

For background information about restoring backups, see [Restoring backups | Apigee X | Google Cloud](https://cloud.google.com/apigee/docs/hybrid/v1.8/backup-recovery#restoring-backups)

  1. Create a new Kubernetes cluster with a new namespace in which to restore the hybrid runtime deployment. You cannot use the same cluster and namespace that you used for the original hybrid installation.
  2. Install Hybrid into the new cluster with the above configured settings in addition to any other settings that you desire:

     * You can either use the Basic install and **install hybrid in the new namespace:**
    
    ./tools/apigee-hybrid-setup.sh \
    --cluster-name $CLUSTER_NAME \
    --cluster-region $CLUSTER_LOCATION \
    --namespace ${NEW_APIGEE_NAMESPACE}
    

     * Or follow the Customized Apigee Hybrid installation to configure things as per your choice.
  3. Once the restoration is complete, all resources in the old namespace could be deleted and switched over to the new namespace.




For more information, see [Restoring backups](https://cloud.google.com/apigee/docs/hybrid/v1.8/backup-recovery#restoring-backups).

### non-gcs-backup and non-gcs-restore

This kustomize component can be used to perform a backup and restore for the cassandra database to Google Cloud Storage.

#### Available in:

  * `overlays/instances/{INSTANCE_NAME}/datastore`



#### Prerequisite:

  1. Steps from the already existing documentation for [Set up the server and SSH](https://cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-non-gcs#server-ssh) can be utilized.
  2. From the above steps, you'll need to use the SSH private key which is available in the file "ssh_key" generated by following the previous steps. We'll then create a kubernetes secret by the name apigee-cassandra-backup-and-restore-gcp-sa-key which contains this SSH Private key.

* * *

**Note:** Ensure that your SSH private key file has a new line at the end.

* * *

The kubernetes secret can be created using the following command:
         
         kubectl create secret generic "apigee-cassandra-backup-and-restore-key-file" \
                 --from-file="key=${PATH_TO_SSH_PRIVATE_KEY}" \
                 -n "${APIGEE_NAMESPACE}"
         

Where:

     * ${PATH_TO_SSH_PRIVATE_KEY} \- Path to the file containing the SSH private key
     * ${APIGEE_NAMESPACE} \- The kubernetes namespace where Apigee components have been installed. This would usually be apigee unless, explicitly changed during the installation

Alternatively, you can use the template file templates/secret-apigee-cassandra-backup-and-restore-key-file.yaml to create this secret.




#### Enabling:

  * If you want to enable backup, uncomment the "`./components/non-gcs-backup`" line in the datastore kustomization.yaml file.
  * If you want to restore a backup, uncomment the "`./components/non-gcs-restore`" line in the datastore kustomization.yaml file.



#### Modifications for backup only

  * components/non-gcs-backup/apigee-datastore-patch.yaml 
    * _REQUIRED_ Change value of BACKUP_SERVER_IP. Description matches BACKUP_SERVER_IP [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-non-gcs).
    * _REQUIRED_ Change value of BACKUP_STORAGE_DIR. Description matches BACKUP_STORAGE_DIR [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-non-gcs).
  * components/non-gcs-backup/cron-patch.yaml 
    * _REQUIRED_ Change spec.schedule to specify the frequency of the backup. Field accepts the standard Crontab schedule format. Description matches schedule [described here](https://docs.google.com/document/d/1NeK0h24ZxZFclZGy2zJ28ydrsAUuqZ3B12w7n69xZqc/edit#bookmark=kix.1zhdsab5ui21).
    * _REQUIRED_ Change value of BACKUP_SERVER_IP. Description matches BACKUP_SERVER_IP [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-non-gcs).
    * _REQUIRED_ Change value of BACKUP_STORAGE_DIR. Description matches BACKUP_STORAGE_DIR [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-non-gcs).
    * _OPTIONAL_ Change value of HTTP_PROXY_URL to point to any proxy configured. The format could be as follows: 
      * `http://${USERNAME}:${PASSOWORD}@${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `https://${USERNAME}:${PASSOWORD}@${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `http://${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `http://${HOST_IP_ADDRESS}:${HOST_PORT}`



#### Performing Backup

You can perform the backup with the following command:
    
    
    kubectl apply -k overlays/instances/{INSTANCE_NAME}
    

To apply you changes and enable the backup:

#### Modifications for backup only

  * components/non-gcs-restore/apigee-datastore-patch.yaml 
    * _REQUIRED_ Change value of `BACKUP_SERVER_I`P. Description matches `BACKUP_SERVER_IP` [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-non-gcs).
    * _REQUIRED_ Change value of BACKUP_STORAGE_DIR. Description matches `BACKUP_STORAGE_DIR` [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-non-gcs).
  * components/non-gcs-restore/job-patch.yaml 
    * _REQUIRED_ Change value of `BACKUP_SNAPSHOT_TIMESTAMP` environment variable. Description matches `restore:snapshotTimestamp` [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-non-gcs).
    * _REQUIRED_ Change value of `BACKUP_SERVER_IP`. Description matches `BACKUP_SERVER_IP` [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-non-gcs).
    * _REQUIRED_ Change value of `BACKUP_STORAGE_DIR`. Description matches `BACKUP_STORAGE_DIR` [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-non-gcs).
    * _OPTIONAL_ Change value of `HTTP_PROXY_URL` to point to any proxy configured. The format could be as follows: 
      * `http://${USERNAME}:${PASSOWORD}@${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `https://${USERNAME}:${PASSOWORD}@${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `http://${HOST_IP_ADDRESS}:${HOST_PORT}`
      * `http://${HOST_IP_ADDRESS}:${HOST_PORT}`



#### Performing the restore:

For an overview on restoring backups, see [Cassandra restore overview](https://cloud.google.com/apigee/docs/hybrid/v1.8/restore-cassandra-backup).

  1. Create a new Kubernetes cluster with a new namespace in which to restore the hybrid runtime deployment. You cannot use the same cluster and namespace that you used for the original hybrid installation.
  2. Install Hybrid into the new cluster with the above configured settings in addition to any other settings that you desire: You can either use the Basic install and **install hybrid in the new namespace:**
         
         ./tools/apigee-hybrid-setup.sh \
           --cluster-name $CLUSTER_NAME \
           --cluster-region $CLUSTER_LOCATION \
           --namespace ${NEW_APIGEE_NAMESPACE}
         

Or follow the Customized Apigee Hybrid installation to configure things as per your choice.

  3. Once the restoration is complete, all resources in the old namespace could be deleted and switched over to the new namespace.

For more information, see [Scheduling backups on a remote server](https://cloud.google.com/apigee/docs/hybrid/v1.8/schedule-cassandra-backup-non-gcs.html).




### http-client

For instructions, see [Enable HTTP clients | Apigee](https://cloud.google.com/apigee/docs/hybrid/v1.8/enable-non-sni#enable-http-clients).

#### Available in:

  * overlays/instances/${INSTANCE_NAME}/route-config/${ENV_GROUP}



#### Enabling:

Uncomment the "`./components/http-client`" line in the respective `route-config/${ENV_GROUP}/kustomization.yaml` file

#### Modifications to be made:

  * No mandatory modifications required.



#### Usage:

  1. If you have not yet installed Apigee Hybrid, you can continue with the installation steps and these changes will get applied in the process
  2. If you already have Apigee Hybrid installed, you will need to apply these new changes using:
         
         kubectl apply -k overlays/instances/{INSTANCE_NAME}
         




### non-sni-client

Equivalent of the already existing [How to configure a non-SNI client | Apigee](https://cloud.google.com/apigee/docs/hybrid/v1.8/enable-non-sni#how-to-configure-a-non-sni-client).

#### Available in:

  * overlays/instances/${INSTANCE_NAME}/route-config/${ENV_GROUP}



#### Enabling:

Uncomment the "`./components/non-sni-client`" line in the respective `route-config/${ENV_GROUP}/kustomization.yaml` file

#### Modifications to be made:

  * components/non-sni-client/apigee-route.yaml 
    * _REQUIRED_ `credentialName` Description matches `credential_name` [described here](https://docs.google.com/document/d/1NeK0h24ZxZFclZGy2zJ28ydrsAUuqZ3B12w7n69xZqc/edit#bookmark=kix.1zhdsab5ui21).



#### Usage:

  1. If you have not yet installed Apigee Hybrid, you can continue with the installation steps and these changes will get applied in the process
  2. If you already have Apigee Hybrid installed, you will need to apply these new changes using:
         
         kubectl apply -k overlays/instances/{INSTANCE_NAME}
         




### http-and-non-sni-client

For instructions, see [Enable support for both non-SNI and HTTP clients | Apigee](https://cloud.google.com/apigee/docs/hybrid/katest/enable-non-sni#enable-support-for-both-non-sni-and-http-clients).

#### Enabling:

Uncomment the "`./components/http-and-non-sni-client`" line in the respective `route-config/${ENV_GROUP}/kustomization.yaml` file

#### Modifications to be made:

  * components/http-and-non-sni-client/apigee-route.yaml 
    * _REQUIRED_ `credentialName` Description matches `credential_name` [described here](https://cloud.google.com/apigee/docs/hybrid/v1.8/enable-non-sni#how-to-configure-a-non-sni-client).



#### Usage:

  1. If you have not yet installed Apigee Hybrid, you can continue with the installation steps and these changes will get applied in the process
  2. If you already have Apigee Hybrid installed, you will need to apply these new changes using:
         
         kubectl apply -k overlays/instances/{INSTANCE_NAME}
         




### multi-region

This component can be used while configuring a multi-region cassandra deployment. For more information, see [Multi-region deployment on GKE and GKE on-prem](https://cloud.google.com/apigee/docs/hybrid/v1.8/multi-region)

#### Enabling:

Uncomment the "`./components/multi-region`" line in the `datastore/kustomization.yaml` file

#### Modifications to be made:

  * components/multi-region/cassandra-data-replication.yaml

    * _REQUIRED_ `source.region` The source Cassandra datacenter name that will be used to replicate data from. Can be identified by using the following command in the source cluster:
    
    kubectl get apigeedatastore -n ${APIGEE_NAMESPACE} -o=jsonpath='{.items[*].spec.components.cassandra.properties.datacenter}'
    

  * components/multi-region/patch.yaml

    * _REQUIRED_ `spec.components.properties.multiRegionSeedHost` The Pod IP of any of the source cassandra pods. We can use:
    
    kubectl get pods -n ${APIGEE_NAMESPACE} -o wide
    

    * To list all the pods and get the IP of any cassandra pod, use the following command:
    
    kubectl get pods -o wide -n apigee
    

Your output should look something like the following:
    
    NAME                      READY   STATUS      RESTARTS   AGE   IP          NODE                                          NOMINATED NODE
    apigee-cassandra-default-0        1/1     Running     0          5d    10.0.0.11   gke-k8s-dc-2-default-pool-a2206492-p55d
    apigee-cassandra-default-1        1/1     Running     0          5d    10.0.2.4    gke-k8s-dc-2-default-pool-e9daaab3-tjmz
    apigee-cassandra-default-2        1/1     Running     0          5d    10.0.3.5    gke-k8s-dc-2-default-pool-e589awq3-kjch
    




For more information, see [Prerequisites for GKE in "Multi-region deployment on GKE, GKE on-prem, and AKS"](https://cloud.google.com/apigee/docs/hybrid/v1.8/multi-region#gke):

#### Usage:

The use of this component mostly makes sense when you are setting up Apigee Hybrid in a new cluster and you already have another working setup of Apigee Hybrid.

  1. Both the new and the existing cluster need to be using the same TLS certificates to ensure proper communication between the Cassandra pods. So we'll need to copy the `apigee-root-certificate` secret from the existing cluster and use it in the newer one as well:
  2. Run:
         
         kubectl config get-contexts
         

     * To get a list of all the kubernetes contexts and then run
    
    kubectl config use-context SOURCE_CLUSTER_CONTEXT
    

where SOURCE_CLUSTER_CONTEXT is the name of the source kubernetes cluster context.

  3. Store the root certificate secret in a file:
         
         kubectl get secret/apigee-root-certificate -n cert-manager -o yaml > apigee-root-certificate.yaml
         

  4. Switch the cluster context to the new cluster where you are installing Apigee Hybrid.
         
         kubectl config use-context ${NEW_CLUSTER_CONTEXT}
         

  5. Create the root secret in the new cluster:
         
         kubectl -n cert-manager apply -f apigee-root-certificate.yaml
         

  6. Disable the creation of a new root certificate. This will ensure that we don't create a new `apigee-root-certificate` and end up overwriting the one that we created in the previous step.

  7. Uncomment the following lines in the `overlays/initialization/certificates/kustomization.yaml` file:
         
         # components:
         # - ./components/disable-apigee-root-certificate-generation
         

  8. Continue with the rest of the Apigee Hybrid installation either using the Basic Apigee Hybrid Installation or the Customized Apigee Hybrid installation. For example, following the Basic Apigee Hybrid Installation, you can execute:
         
         ./tools/apigee-hybrid-setup.sh --cluster-name $CLUSTER_NAME --cluster-region $CLUSTER_LOCATION
         

  9. Verify the rebuild status using the following command.

* * *

**Note:** The rebuild operation can take up to several hours depending on the data size.

* * *
         
         kubectl -n ${APIGEE_NAMESPACE} get apigeeds -o json | jq ".items[].status.cassandraDataReplication"
         

  10. Verify the rebuild processes from the logs. Also, verify the data size using the nodetool status command:
         
         kubectl logs apigee-cassandra-default-0 -f -n ${APIGEE_NAMESPACE}
         kubectl exec apigee-cassandra-default-0 -n ${APIGEE_NAMESPACE}  -- nodetool -u ${JMX_USER} -pw ${JMX_PASSWORD} status
         

  11. Verify the rebuild status using the following command.

* * *

**Note:** The rebuild operation can take up to several hours depending on the data size.

* * *
         
         kubectl -n apigee get apigeeds -o json | jq ".items[].status.cassandraDataReplication"
         

The results should look something like:
         
         {
         "rebuildDetails": {
         "apigee-cassandra-default-0": {
           "state": "complete",
           "updated": 1623105760
         },
         "apigee-cassandra-default-1": {
           "state": "complete",
           "updated": 1623105765
         },
         "apigee-cassandra-default-2": {
           "state": "complete",
           "updated": 1623105770
         }
         },
         "state": "complete",
         "updated": 1623105770
         }
         

See also: [Multi-region deployment](https://cloud.google.com/apigee/docs/hybrid/v1.8/multi-region#gke).

  12. Removing the following lines from `components/multi-region/patch.yaml`:
         
         properties:
             multiRegionSeedHost: {IP_ADDRESS} # To be modified. REQUIRED
         

  13. Apply the changes:
         
         kubectl apply -k overlays/instances/{INSTANCE_NAME}
         




## Concepts

### Image Hub

Docker container images are generally specified in the format:
    
    
    ${REGISTRY_HOST_PATH}/${IMAGE_NAME}:${IMAGE_TAG}
    

or ones that use a digest look like:
    
    
    ${REGISTRY_HOST_PATH}/${IMAGE_NAME}@${DIGEST}
    

Apigee uses the concept of "Image Hub", which in the above formats refers to the `${REGISTRY_HOST_PATH}`. The default value of the Image Hub is `gcr.io/apigee-release/hybrid/`.

(Images which utilize DIGEST will need to be individually set in each subcomponent)

Apigee constructs the final image path by combining the value of following:

  * "Image Hub" which can be overridden in apigee-hybrid-config.yaml (refer to Using docker images from private repositories section for detailed steps on how to override Image Hub).
  * The value of the `IMAGE_TAG` is obtained from the `version` field, which is present inside the yaml file for each of the individual components (for example, apigee-organization.yaml). Apigee tags the images with the Apigee Hybrid version - meaning `IMAGE_TAG` is 1.8 for Apigee Hybrid version 1.8
  * `IMAGE_NAME` is implicitly determined from the name of the container where the image will be used. For example, for the `apigee-runtime` container, the `IMAGE_NAME` will be apigee-runtime.



Thus, a complete example of an image path would be `gcr.io/apigee-release/hybrid/apigee-runtime:1.8.0`

In this way, the final image path is constructed, which would then be used inside each of the containers in their respective pods.

### Google Cloud service accounts

Google Cloud service accounts are accounts used by applications to make authorized calls to Google APIs. Google Cloud service account keys can be downloaded which can then be used for authentication purposes. Apigee expects the user to provide service account keys by creating secrets. The following are the names of the components and the default name of the secret where it looks for service account keys:

Component | Subcomponent | Default kubernetes secret name containing service account key  
---|---|---  
**organization** |  |   
| connectAgent | `apigee-connect-agent-gcp-sa-key-${ORG_NAME}`  
| watcher | `apigee-watcher-gcp-sa-key-${ORG_NAME}`  
| mart | `apigee-mart-gcp-sa-key-${ORG_NAME}`  
| udca | `apigee-udca-gcp-sa-key-${ORG_NAME}`  
| ingressGateways | N/A  
**environment** |  |   
| runtime | `apigee-runtime-gcp-sa-key-${ORG_NAME}-${ENV_NAME}`  
| udca | `apigee-udca-gcp-sa-key-${ORG_NAME}-${ENV_NAME}`  
| synchronizer | `apigee-synchronizer-gcp-sa-key-${ORG_NAME}-${ENV_NAME}`  
**telemetry** |  |   
| metrics | `apigee-metrics-gcp-sa-key`  
| containerLogs | `apigee-logger-gcp-sa-key`  
  
### Kubernetes service accounts

Kubernetes service accounts provide identities to pods in your cluster. By default, Apigee controller creates these for you. But, if you'd like to override the creation (for example, when you are using Workload identities), then you can do so by specifying the `podServiceAccountName` field in the various sub components.

List of components and their respective sub components where the kubernetes service account can be specified along with the default name of the k8s service account when you enable the workload identity patch for them.

Component | Subcomponent | Default name (available when you've enabled workload identity patch)  
---|---|---  
**organization** |  |   
| connectAgent | `apigee-connect-agent-svc-account-${ORG_NAME}`  
| watcher | `apigee-watcher-svc-account-${ORG_NAME}`  
| mart | `apigee-mart-svc-account-${ORG_NAME}`  
| udca | `apigee-udca-svc-account-${ORG_NAME}`  
**environment** |  |   
| synchronizer | `apigee-synchronizer-svc-account-${ORG_NAME}-${ENV_NAME}`  
| udca | `apigee-udca-svc-account-${ORG_NAME}-${ENV_NAME}`  
| runtime | `apigee-runtime-svc-account-${ORG_NAME}-${ENV_NAME}`  
**datastore** |  |   
| cassandra | `apigee-datastore-svc-account`  
**telemetry** |  |   
| metricsApp | `apigee-metricsApp-svc-account`  
| metricsProxy | `apigee-metricsProxy-svc-account`  
| metricsAdapter | `apigee-metricsAdapter-svc-account`  
| containerLogs | `apigee-container-logs-svc-account`  
  
### Workload identities

Workload identities allow pods (which use kubernetes service accounts) running in GKE to directly authenticate with Google Cloud APIs without requiring Google Cloud service account keys.

### Adding a new environment
    
    
    .
    ├── ...
    ├── instances/instance1/components
    │   ├── ...
    │   ├── environments
    │   │   ├── dev
    │   │   │   └── apigee-environment.yaml
    │   │   │   └── secrets.yaml
    │   │   └── new-env-name (new)
    │   │       └── apigee-environment.yaml (new)
    │   │       └── secrets.yaml (new)
    └── ...
    

Adding a new environment is as simple as:

  1. Creating a new folder inside the environments directory (or however you have structured your folders)
  2. Copying the `apigee-environment.yaml` file from any existing environment to the new folder.
  3. If you wish to create new service account and encryption keys for the new environment, copy the `secrets.yaml` into the new folder and rename the secrets appropriately to distinguish them from the other existing environments (this is usually done by adding the name of the environment as a suffix)
  4. Making appropriate changes to the `apigee-environment.yaml`, like: 
     * Changing the name of the environment
     * If new service accounts and encryption keys are going to be created, they need to be correctly referenced in the yaml.
  5. Applying the `yaml`s:


    
    
    kubectl apply -f components/environments/new-env-name/secrets.yaml
    kubectl apply -f components/environments/new-env-name/apigee-environment.yaml
    

### Using force delete in Apigee Datastore

If datastore delete is not progressing because of any reason, now apigee datastore can be force deleted using the following commands irrespective of the current state of the cluster.

* * *

**Note:** Using force delete will also delete the PVCs. So, if the current Apigee Hybrid deployment is single reason, take a backup before proceeding.

* * *

* * *

**Note:** Using force delete in multi region clusters requires manual cleanup in other regions after datastore delete is complete to keep the cassandra in healthy state. Refer to the troubleshooting guide on how to do manual cleanup.

* * *

  1. Delete `apigeeds` in the `apigee` namespace:
         
         Kubectl delete -n apigee apigeeds default
         

If this step becomes stuck, you can get out of that using CTRL + C.

  2. Edit a new `apigeeds`:
         
         Kubectl edit -n apigee apigeeds default
         

  3. Add/update forceDelete field in apigee datastore spec
         
         spec:
         forceDelete: true
         

  4. Save the file and exit.




Now wait for the datastore to be deleted. It can take a few minutes to delete all the cassandra resources.

## Understanding the script

`apigee-hybrid-setup.sh` script performs some basic validations and helps automate the steps which you would otherwise have to do if you want more detailed customization as documented in Customized Apigee Hybrid installation. Even with the customized installation, you can still partially use the script to help with certain tasks.

You can run `./tools/apigee-hybrid-setup.sh --help` to see a list of flags supported and get some extra help with the script. The following flags are supported at the moment:

  * `--namespace` By default, the script installs all the components in the `apigee` namespace. You can change this behavior by specifying the name of the namespace using this flag.
  * `--org` Used to provide the name of the Apigee organization. If not specified, defaults to the Google Cloud project currently selected in `gcloud`
  * `--envgroup` Used to provide the name of the environment group inside your organization. If not specified, an attempt is made to query the control plane APIs to determine the name of the environment group. If multiple environment groups are found, error is returned and the script exits.
  * `--env` Used to provide the name of the environment inside your organization. If not specified, an attempt is made to query the control plane APIs to determine the name of the environment. If multiple environments are found or the environment is not part of the environment group, error is returned and the script exits.
  * `--cluster-name` The Kubernetes cluster name.
  * `--cluster-region` The region in which the kubernetes cluster is located
  * `--gcp-project-id` The Google Cloud project ID where the kubernetes cluster exists
  * `--ingress-domain` Specifies the hostname/domain-name that will be used to generate the self signed TLS certificates for istio ingress-gateway. If none is specified, an attempt is made to determine the value by querying the control plane APIs to get the value from the envgroup. If there were some problems with determining the envgroup or there were multiple hostnames configured for the envgroup, then error is returned and the script exits.
  * `--generate-internal-tls-certs` This will generate a kubernetes secret named apigee-ca that contains a certificate and key pair generated by us.
  * `--create-ingress-tls-certs` This will generate a secret named `{ORG_NAME}-{ENV_GROUP_NAME}` (derived from the org and envgroup name) inside the istio-system namespace that will contain a certificate and key pair that will be used for TLS communication. The domain name used to generate these certificates are derived from the value found in the envgroup configuration. In case of conflicts (like when we find multiple domains), appropriate error messages will be shown.
  * `--create-gcp-sa-and-secrets` Creates a single Google Cloud service account in the Google Cloud project, downloads the keys, and then creates the kubernetes secrets containing the key. The names of the secrets can be found in Google Cloud service accounts.
  * `--fill-values` Replaces the values of the org, env, envgroup and other names wherever they are required in the various yamls.
  * `--apply-configuration` This will create the certificate issuers, custom resource definitions, webhooks, roles and the controller resource. Resources will be created in the correct order and command will block until all are healthy.
  * `-- rename-directories` Rename the environment and environment group to the names of the correct environment and environment group.
  * `--verbose` Shows detailed output for debugging.
  * `--help` Display usage information.
  * `--setup-all` This will execute all the tasks that can be performed by this script



## Apigee Hybrid Setup Folder Structure

The `apigee-hybrid-setup` folder has the following hierarchical structure by default:
    
    
    .
    ├── bases
    │   ├── controllers
    │   │   ├── apigee-controller
    │   │   │   ├── apigee-controller-deployment.yaml
    │   │   │   └── kustomization.yaml
    │   │   └── apigee-ingressgateway-manager
    │   │       ├── apigee-ingressgateway-manager-deployment.yaml
    │   │       └── kustomization.yaml
    │   ├── datastore
    │   │   └── backup-and-restore
    │   │       ├── backup
    │   │       │   ├── cronjob.yaml
    │   │       │   └── kustomization.yaml
    │   │       ├── common
    │   │       │   ├── kustomization.yaml
    │   │       │   ├── rbac.yaml
    │   │       │   └── tls-certificate.yaml
    │   │       └── restore
    │   │           ├── job.yaml
    │   │           └── kustomization.yaml
    │   └── initialization
    │       ├── certificates
    │       │   ├── certificates-and-issuers.yaml
    │       │   └── kustomization.yaml
    │       ├── crds
    │       │   ├── customresourcedefinition-apigeedatastores.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeedeployments.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeeenvironments.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeeorganizations.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeeredis.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeerouteconfigs.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeeroutes.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeetelemetries.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-cassandradatareplications.apigee.cloud.google.com.yaml
    │       │   └── kustomization.yaml
    │       ├── openshift
    │       │   ├── kustomization.yaml
    │       │   └── scc.yaml
    │       ├── rbac
    │       │   ├── apigee-controller
    │       │   │   ├── kustomization.yaml
    │       │   │   └── rbac.yaml
    │       │   └── apigee-embedded-ingress-controller
    │       │       ├── cluster-role-bindings.yaml
    │       │       ├── cluster-roles.yaml
    │       │       ├── kustomization.yaml
    │       │       └── service-account.yaml
    │       └── webhooks
    │           ├── kustomization.yaml
    │           ├── mutatingwebhookconfiguration.yaml
    │           └── validatingwebhookconfiguration.yaml
    ├── CONTRIBUTING.md
    ├── docs
    │   └── api_references
    │       ├── v1alpha1.md
    │       └── v1alpha2.md
    ├── kokoro
    │   ├── build.sh
    │   ├── common.cfg
    │   ├── continuous.cfg
    │   ├── presubmit.cfg
    │   └── release.cfg
    ├── LICENSE
    ├── overlays
    │   ├── controllers
    │   │   ├── apigee-controller
    │   │   │   ├── apigee-hybrid-config.yaml
    │   │   │   ├── components
    │   │   │   │   ├── imagepullsecret
    │   │   │   │   │   ├── kustomization.yaml
    │   │   │   │   │   └── patch.yaml
    │   │   │   │   └── nodeselector
    │   │   │   │       ├── kustomization.yaml
    │   │   │   │       └── patch.yaml
    │   │   │   └── kustomization.yaml
    │   │   ├── apigee-ingressgateway-manager
    │   │   │   ├── apigee-ingressgateway-manager-deployment-patch.yaml
    │   │   │   ├── apigee-istio-mesh-config.yaml
    │   │   │   ├── components
    │   │   │   │   ├── imagepullsecret
    │   │   │   │   │   ├── kustomization.yaml
    │   │   │   │   │   └── patch.yaml
    │   │   │   │   └── nodeselector
    │   │   │   │       ├── kustomization.yaml
    │   │   │   │       └── patch.yaml
    │   │   │   └── kustomization.yaml
    │   │   └── kustomization.yaml
    │   ├── initialization
    │   │   ├── certificates
    │   │   │   ├── apigee-ingressgateway-manager-certificate-patch.yaml
    │   │   │   ├── apigee-serving-cert-patch.yaml
    │   │   │   ├── components
    │   │   │   │   └── disable-apigee-root-certificate-generation
    │   │   │   │       └── kustomization.yaml
    │   │   │   └── kustomization.yaml
    │   │   ├── crds
    │   │   │   └── kustomization.yaml
    │   │   ├── ingress
    │   │   │   ├── envoyfilter-1.11.yaml
    │   │   │   └── kustomization.yaml
    │   │   ├── namespace.yaml
    │   │   ├── openshift
    │   │   │   ├── kustomization.yaml
    │   │   │   └── scc.yaml
    │   │   ├── rbac
    │   │   │   ├── apigee-controller
    │   │   │   │   └── kustomization.yaml
    │   │   │   ├── apigee-ingressgateway-manager
    │   │   │   │   └── kustomization.yaml
    │   │   │   └── kustomization.yaml
    │   │   └── webhooks
    │   │       ├── kustomization.yaml
    │   │       ├── mutatingwebhookconfiguration.yaml
    │   │       └── validatingwebhookconfiguration.yaml
    │   └── instances
    │       └── instance1
    │           ├── datastore
    │           │   ├── apigee-datastore.yaml
    │           │   ├── components
    │           │   │   ├── gcs-backup
    │           │   │   │   ├── apigee-datastore-patch.yaml
    │           │   │   │   ├── cron-patch.yaml
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── tls-certificate-patch.yaml
    │           │   │   ├── gcs-restore
    │           │   │   │   ├── apigee-datastore-patch.yaml
    │           │   │   │   ├── job-patch.yaml
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── tls-certificate-patch.yaml
    │           │   │   ├── http-proxy
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── imagepullsecret
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── multi-region
    │           │   │   │   ├── cassandra-data-replication.yaml
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── nodeselector
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── non-gcs-backup
    │           │   │   │   ├── apigee-datastore-patch.yaml
    │           │   │   │   ├── cron-patch.yaml
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── tls-certificate-patch.yaml
    │           │   │   ├── non-gcs-restore
    │           │   │   │   ├── apigee-datastore-patch.yaml
    │           │   │   │   ├── job-patch.yaml
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── tls-certificate-patch.yaml
    │           │   │   ├── openshift-scc
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── scc.yaml
    │           │   │   └── workload-identity
    │           │   │       ├── kustomization.yaml
    │           │   │       ├── patch.yaml
    │           │   │       └── service-accounts.yaml
    │           │   ├── kustomization.yaml
    │           │   └── secrets.yaml
    │           ├── environments
    │           │   ├── kustomization.yaml
    │           │   └── test
    │           │       ├── apigee-environment.yaml
    │           │       ├── components
    │           │       │   ├── http-proxy
    │           │       │   │   ├── kustomization.yaml
    │           │       │   │   └── patch.yaml
    │           │       │   ├── imagepullsecret
    │           │       │   │   ├── kustomization.yaml
    │           │       │   │   └── patch.yaml
    │           │       │   ├── nodeselector
    │           │       │   │   ├── kustomization.yaml
    │           │       │   │   └── patch.yaml
    │           │       │   └── workload-identity
    │           │       │       ├── kustomization.yaml
    │           │       │       ├── patch.yaml
    │           │       │       └── service-accounts.yaml
    │           │       ├── kustomization.yaml
    │           │       └── secrets.yaml
    │           ├── kustomization.yaml
    │           ├── organization
    │           │   ├── apigee-organization.yaml
    │           │   ├── components
    │           │   │   ├── http-proxy
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── imagepullsecret
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── nodeselector
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   └── workload-identity
    │           │   │       ├── kustomization.yaml
    │           │   │       ├── patch.yaml
    │           │   │       └── service-accounts.yaml
    │           │   ├── kustomization.yaml
    │           │   └── secrets.yaml
    │           ├── redis
    │           │   ├── apigee-redis.yaml
    │           │   ├── components
    │           │   │   ├── imagepullsecret
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── nodeselector
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   └── workload-identity
    │           │   │       ├── kustomization.yaml
    │           │   │       ├── patch.yaml
    │           │   │       └── service-accounts.yaml
    │           │   ├── kustomization.yaml
    │           │   └── secrets.yaml
    │           ├── route-config
    │           │   ├── kustomization.yaml
    │           │   └── test-envgroup
    │           │       ├── apigee-route-config.yaml
    │           │       ├── components
    │           │       │   ├── http-and-non-sni-client
    │           │       │   │   ├── apigee-route.yaml
    │           │       │   │   └── kustomization.yaml
    │           │       │   ├── http-client
    │           │       │   │   ├── apigee-route.yaml
    │           │       │   │   └── kustomization.yaml
    │           │       │   └── non-sni-client
    │           │       │       ├── apigee-route.yaml
    │           │       │       └── kustomization.yaml
    │           │       └── kustomization.yaml
    │           └── telemetry
    │               ├── apigee-telemetry.yaml
    │               ├── components
    │               │   ├── http-proxy
    │               │   │   ├── kustomization.yaml
    │               │   │   └── patch.yaml
    │               │   ├── imagepullsecret
    │               │   │   ├── kustomization.yaml
    │               │   │   └── patch.yaml
    │               │   ├── logger
    │               │   │   ├── kustomization.yaml
    │               │   │   └── patch.yaml
    │               │   ├── metrics
    │               │   │   ├── kustomization.yaml
    │               │   │   └── patch.yaml
    │               │   ├── nodeselector
    │               │   │   ├── kustomization.yaml
    │               │   │   └── patch.yaml
    │               │   ├── openshift-scc
    │               │   │   ├── kustomization.yaml
    │               │   │   └── scc.yaml
    │               │   ├── workload-identity-logger
    │               │   │   ├── kustomization.yaml
    │               │   │   ├── patch.yaml
    │               │   │   └── service-accounts.yaml
    │               │   └── workload-identity-metrics
    │               │       ├── kustomization.yaml
    │               │       ├── patch.yaml
    │               │       └── service-accounts.yaml
    │               └── kustomization.yaml
    ├── README.md
    ├── templates
    │   ├── certificate-org-envgroup.yaml
    │   ├── secret-apigee-cassandra-backup-and-restore-gcp-sa-key.yaml
    │   ├── secret-apigee-cassandra-backup-and-restore-key-file.yaml
    │   ├── secret-gcp-sa-key.yaml
    │   └── secret-ingress-tls-cert-key.yaml
    └── tools
        ├── apigee-hybrid-setup.sh
        ├── apigee-pull-push.sh
        ├── common.sh
        ├── create-service-account.sh
        └── dump_kubernetes.sh
    
    

A version of the above files can be found in the preview-1 tag of the github repository at: <https://github.com/apigee/apigee-hybrid-install/releases/tag/preview-1>.

The above folder contains Kubernetes manifests for [Apigee hybrid](https://cloud.google.com/apigee/docs/hybrid/v1.8/what-is-hybrid) runtime and uses [Kustomize](https://kustomize.io/) for configuration management. The manifests are organized based on the concept of [Kustomize bases & overlays](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#bases-and-overlays). The bases folder contains the minimal required configuration for every apigee component. The overlays folder contains multiple additional features(configurations) that are defined as [components](https://kubectl.docs.kubernetes.io/guides/config_management/components/). A component can be by uncommenting the component reference in the kustomization.yaml

**Example :** To enable the `gcs-backup` for apigee datastore, the `gcs-backup` component has been uncommented in the below customization.yaml.

**Path :** `${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}/datastore/kustomization.yaml`
    
    
    namespace: "apigee" # kpt-set: ${APIGEE_NAMESPACE}
    
    resources:
    - apigee-datastore.yaml
    
    components:
    # - ./components/http-proxy
    # - ./components/nodeselector/
    # - ./components/imagepullsecret
    # - ./components/workload-identity
    # - ./components/openshift-scc
    - ./components/gcs-backup (uncommented)
    # - ./components/gcs-restore
    # - ./components/non-gcs-backup
    # - ./components/non-gcs-restore
    

Any value that requires customisations will have to be set in the corresponding patch.yaml for gcs-backup. In the below file, the value of `CLOUD_STORAGE_BUCKET_PATH` has to be set by the user

**Path:** `$INSTALL_DIR/overlays/instances/$INSTANCE_DIR/datastore/components/gcs-backup/cron-patch.yaml`
    
    
    apiVersion: batch/v1beta1
    kind: CronJob
    metadata:
      name: apigee-cassandra-backup
      namespace: apigee
    spec:
      schedule: "${YOUR_BACKUP_SCHEDULE_CODE}" # To be modified
      jobTemplate:
        spec:
          template:
            spec:
              containers:
              - name: apigee-cassandra-backup
                env:
                - name: APIGEE_CLOUDPROVIDER
                  value: "GCP"
                - name: DATABASE_STORAGE_BUCKET
                  value: "${CLOUD_STORAGE_BUCKET_PATH}" # To be modified. REQUIRED
                volumeMounts:
                - name: apigee-cassandra-backup
                  mountPath: /var/secrets/google
              volumes:
              - name: apigee-cassandra-backup
                secret:
                  secretName: "apigee-cassandra-backup-and-restore-svc-account"
    

Likewise, any feature/configuration that requires customizations can be enabled by uncommenting the component in the apigee component's kustomization.yaml. Also, as required the corresponding values for the fields in the component's patch.yaml need to be set accordingly.

Brief explanation of the folders and files:

#### bases

This folder has the templates with bare minimum configuration required by each of the apigee components. There wouldn't be a need for modifications to the manifests in this folder.

#### overlays

This folder contains the kustomize components templates for the additional configurations

#### initialization

##### namespaces.yaml

The namespace where Apigee data plane components will be installed. The default namespace name is `apigee`

##### certificates

Contains the `Issuer` and `Certificate` resources that are used to issue certificates to the webhooks. Also contains the `Issuer` that is used to issue certificates to various pods for TLS communication.

##### rbac

Contains the `Role`, `ClusterRole`, `RoleBinding` and `ClusterRoleBinding` that will be used by various components.

##### crds
    
    
        Contains the definition of all the CRDs which are used by Apigee.
    

##### webhooks

Contains `ValidatingWebhookConfiguration` and`MutatingWebhookConfiguration` that will be used to perform validations on the custom resources.

##### ingress

Contains configuration that is applicable for all Ingress PODs. Eg. Common header modification, health check etc.

##### openshift

Contains the definition of openshift [SecurityContextConstraints](https://docs.openshift.com/container-platform/4.6/authentication/managing-security-context-constraints.html).

#### Controllers

##### apigee-controller

###### apigee-hybrid-config.yaml

Contains a `ConfigMap` which is supplied as input in apigee-controller-manager.yaml. This ConfigMap contains configuration like `imageHub`, `imagePullSecrets`, `forwardProxy` among other things.

###### apigee-controller-deployment.yaml

Contains two Services for controller and webhook, and the Deployment for the controller. If in case you'd like to use a private image for the controller, this is where you'll need to make the change in.

##### istiod

Apigee-istio-mesh-config.yaml Contains mesh config for Istio used by Apigee. This is not applicable for other installations of ASM/Istio in the cluster.

###### apigee-ingressgateway-manager-deployment-patch.yaml

Contains a service and deployment of Istiod. This is a private istiod used only for Apigee's use cases.

#### instances/{instanceName}

##### datastore

###### apigee-datastore.yaml

Contains the `ApigeeDatastore` custom resource which manages cassandra.

###### secrets.yaml

Contains default credentials for datastore.

##### redis

###### apigee-redis.yaml

Contains the `ApigeeRedis` custom resource which manages redis.

###### secrets.yaml

Contains default credentials for datastore.

##### organization

###### apigee-organization.yaml

Contains the `ApigeeOrganization` custom resource which manages other subcomponents like connectAgent, watcherAndSynchronizer, MART,UDCA and Ingress.

###### secrets.yaml

Contains the `Secret`s which are referenced in apigee-organization.yaml. Some secrets are commented out as they are generated by the script. If you disable their generation, you'll need to manually create those

##### environments

Contains all the environment in your organization. You should create a separate folder for each environment by copying the one that is already provided to you and configuring it as per requirement.

###### dev

###### apigee-environment.yaml

Contains the `ApigeeEnvironment` custom resource which manages other subcomponents like runtime.

###### secrets.yaml

Contains the `Secret`s which are referenced in apigee-environment.yaml. Some secrets are commented out as they are generated by the script. If you disable their generation, you'll need to manually create those

##### telemetry

###### apigee-telemetry.yaml

Contains the `ApigeeTelemetry` custom resource.

###### secrets.yaml

Contains the `Secret`s which are referenced in apigee-telemetry.yaml. Some secrets are commented out as they are generated by the script. If you disable their generation, you'll need to manually create those

##### route-config

###### dev-envgroup

###### apigee-route-config.yaml

Contains the `ApigeeRouteConfig` custom resource.

###### secrets.yaml

Contains a `Secret` which is referenced in apigee-route-config.yaml. It's commented out since it's automatically generated by the apigee-hybrid-setup.sh script and is kept there to provide a sample of what the secret should look like if you were to create it manually.

#### diagnostic

##### diagnostic-collector.yaml

Resources that will be used for bringing up the diagnostic deployment

#### tools

##### apigee-hybrid-setup.sh

##### apigee-create-service-account.sh

##### dump-kubernetes.sh

##### apigee-pull-push.sh

## Storing service account keys in external vaults

[Vault](https://www.vaultproject.io/) (by Hashicorp) is a popular secret management system that has several integrations with secret stores provided by Google, Azure, AWS and others. Hashicorp Vault allows you to fetch secrets from an external source and then use them within kubernetes resources. There are several ways in which one can use Vault to source secrets. The following steps will serve as a basic example about how to use the [Vault CSI Provider](https://www.vaultproject.io/docs/platform/k8s/csi) to mount Google Cloud service account keys stored in some secret engine provided by Vault.

* * *

**Note:** In this example, we are installing Vault in dev mode for testing purposes. For an actual production system, you'd want to install helm one of the [other modes listed here](https://www.vaultproject.io/docs/platform/k8s). For detailed steps about installing Vault for production use cases, kindly refer [Vault on Kubernetes Deployment Guide | Vault](https://learn.hashicorp.com/tutorials/vault/kubernetes-raft-deployment-guide?in=vault/kubernetes).

* * *

  1. We'll be using Helm to install Vault related resources in your cluster. Follow the steps in [Installing Helm](https://helm.sh/docs/intro/install/) on how to set up helm in your system.
  2. Follow the steps in [Install the Vault Helm chart](https://learn.hashicorp.com/tutorials/vault/kubernetes-secret-store-driver?in=vault/kubernetes#install-the-vault-helm-chart), namely:

     1. Adding the Hashicorp repo to helm
            
            helm repo add hashicorp https://helm.releases.hashicorp.com
            

     2. Update helm repos
            
            helm repo update
            

     3. Installing Vault
            
            helm install vault hashicorp/vault \
            --set "server.dev.enabled=true" \
            --set "injector.enabled=false" \
            --set "csi.enabled=true"
            

  3. Now we'll store the secret inside Vault.

     1. Get a shell inside the vault dev pod
            
            kubectl exec -it vault-0 -- /bin/sh
             ```
            

     2. We'll use the key/value secret engine for storing data in this example.
            
            vault kv put secret/runtime-gcp-sa-key key="${BASE_64_ENCODED_KEY}"
            

     3. To verify that the key was stored successfully, use:
            
            vault kv get secret/runtime-gcp-sa-key
            

  4. Setup authentication to allow the runtime pod to pull the key. As discussed in Kubernetes service accounts, kubernetes service accounts provide identity to pods and allow them to authenticate with other systems.

     1. Get a shell inside the vault dev pod
            
            kubectl exec -it vault-0 -- /bin/sh
            

     2. Enable kubernetes authentication method
            
            vault auth enable kubernetes
            

     3. Write the auth config
            
            vault write auth/kubernetes/config \
            issuer="https://kubernetes.default.svc.cluster.local" \
            token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
            kubernetes_host="https://$KUBERNETES_PORT_443_TCP_ADDR:443" \
            kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt \
            disable_iss_validation=true
            

     4. Create the auth policy
            
            vault policy write apigee-runtime-app - <<EOF
            path "secret/data/runtime-gcp-sa-key" {
            capabilities = ["read"]
            }
            EOF
            

     5. Bind the policy with the service account
            
            vault write auth/kubernetes/role/apigee-runtime-role \
            bound_service_account_names=apigee-runtime-sa \
            bound_service_account_namespaces=${APIGEE_NAMESPACE} \
            policies=apigee-runtime-app \
            ttl=20m
            

Here, we assume that the service account is inside the apigee namespace. If you've some other namespace for installing apigee, you'll be using that name.

     1. Exit the shell inside vault-0
            
            exit
            

  5. Install secrets store CSI driver
         
         # Add repo to helm
         helm repo add secrets-store-csi-driver https://raw.githubusercontent.com/kubernetes-sigs/secrets-store-csi-driver/master/charts
         # Install driver in cluster
         helm install csi secrets-store-csi-driver/secrets-store-csi-driver
         

  6. Create `SecretProviderClass` kubernetes resource that references the secret that you created inside vault
         
         cat > spc-vault.yaml <<EOF
         apiVersion: secrets-store.csi.x-k8s.io/v1alpha1
         kind: SecretProviderClass
         metadata:
         name: vault-apigee-runtime-gcp-sa-key
         spec:
         provider: vault
         parameters:
           vaultAddress: "http://vault.default:8200"
           roleName: "apigee-runtime-role"
           objects: |
             - objectName: "client_secret.json"
               secretPath: "secret/data/runtime-gcp-sa-key"
               secretKey: "key"
         EOF
         

  7. Apply the `yaml`
         
         kubectl apply -f spc-vault.yaml
         

  8. Create the kubernetes service account to which we assigned the permissions in step (4.e)
         
         kubectl create serviceaccount -n ${APIGEE_NAMESPACE} apigee-runtime-sa
         

  9. Modify the apigee-environment.yaml file for the environment and add the following lines:
         
         apiVersion: apigee.cloud.google.com/v1alpha2
         kind: ApigeeEnvironment
         # existing content
         spec:
         name: {ENV_NAME}
         organizationRef: {ORG_NAME}
         components:
          runtime:
         # existing content
            pod
            containers:
            - name: apigee-runtime
              podServiceAccountName: apigee-runtime-sa
         # existing content
              volumeMounts:
              - name: secrets-store-inline
                mountPath: "/opt/apigee/sa"
                readOnly: true
            volumes:
            - name: secrets-store-inline
              csi:
                driver: secrets-store.csi.k8s.io
                readOnly: true
                volumeAttributes:
                  secretProviderClass: "vault-apigee-runtime-gcp-sa-key"
         

  10. Apply the changes:
         
         kubectl apply -k ${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}/environments/$ENV_NAME
         




## Apigee Hybrid Upgrade

* * *

**Note:** \- This procedure covers upgrades between hybrid versions that are supporting the new installation model. It does not cover migration from apigeectl experience to the new installation model.

* * *

You should have completed all the requirements mentioned in Prerequisites. Also, it is recommended you do a rolling restart of all the components to check if the cluster is healthy. The order of restarts will be Cassandra, Redis, ApigeeOrganization and ApigeeEnvironment.

### Create Backup

  1. Create a backup copy of the current hybrid setup. Backup will be needed in case you need to rollback the upgrade back to the current version.
         
         tar -czvf apigee-hybrid-install.v-X.Y.Z.tar.gz $HYBRID_INSTALL_BASE_DIR
         

  2. Create backup of cassandra database. Cassandra backups are an important measure of protection against disaster scenarios.




### Upgrade your Kubernetes platform if needed

This step is not required every time but you will need to upgrade your Kubernetes platform like kubernetes, openshift and components like cert-manager, cassandra etc version if it is no longer supported by newer version of apigee hybrid. Documentation will contain [supported versions](https://cloud.google.com/apigee/docs/hybrid/v1.8/upgrade#supported-platforms) of platforms and components.

### Download setup files

Download the repository and replace the `bases` and `tools` folder in the existing apigee hybrid setup with a newer one:

  1. Clone the GitHub repository preview-1 tag at `https://github.com/apigee/apigee-hybrid-install/releases/tag/preview-1`

The cloned repository will have a structure resembling the one described in Apigee Hybrid Setup Folder Structure:

  2. replace initialization, tools and controller folder in the existing apigee hybrid setup.
         
         export HYBRID_INSTALL_HOME=PATH_TO_PREVIOUS_HYBRID_INSTALL_DIRECTORY
         mv -f bases $HYBRID_INSTALL_HOME/bases
         mv -f tools $HYBRID_INSTALL_HOME/tools
         




### Update service account permissions if needed

This step is also not required every time but you will need to create a new service account or update permissions of existing service accounts if needed. Upgrade guide will provide the details about which service accounts need to be modified or created and what are the roles needed to be added.

  * If you need to modify permissions of existing service accounts, use the appropriate `gcloud` command. The upgrade guide will have detailed commands and roles that need to be added.
        
        gcloud projects add-iam-policy-binding $PROJECT_ID \
          --member="serviceAccount:apigee-component@$PROJECT_ID.iam.gserviceaccount.com" \
          --role="roles/$NEW_ROLE"
        

  * If the newer apigee hybrid version might require an additional service account for new / existing components then you need to create those. You can use the `apigee-create-service-account.sh` script shipped within the tool folder to create new service accounts. Since the script will be already updated as part of step 4 it will have details and a new profile needed for a new service account that needs to be created.

The newly created service account name has to be referenced in the corresponding component CR.
        
        ./tools/create-service-account --env prod --profile apigee-component
        




### Upgrade controller

Change the version fields for the components listed in `${INSTALL_DIR}/overlays/instances/$INSTANCE_DIR/kustomization.yaml` to the relevant hybrid version.

Here is a sample $INSTALL_DIR/overlays/instances/$INSTANCE_DIR/kustomization.yaml file. The value of the version field has to be updated to the relevant version
    
    
    resources:
    - datastore/
    - environments/
    - organization/
    - redis/
    - route-config/
    - telemetry/
    
    patches:
    - target:
        group: apigee.cloud.google.com
        version: v1alpha1
        kind: ApigeeDatastore
      patch: |-
        - op: add
          path: /spec/version
          value: 1-6-1 (Modify the version)
    - target:
        group: apigee.cloud.google.com
        version: v1alpha2
        kind: ApigeeEnvironment
      patch: |-
        - op: add
          path: /spec/version
          value: 1-6-1 (Modify the version)
    

Follow the same set of steps provided in Create initialization resources and controller in apigee hybrid installation workflow. you can use script or can follow provided manual steps to upgrade initialization resources and controller.

### Update Apigee Kubernetes components

You will need to make the following changes: \- In case of any architectural changes or introduction of new fields or deprecation of old fields, you will have to modify the CRs with appropriate changes as per the instructions provided in upgrade guide. \- At minimum you need to update the version fields within CRs (which will denote the version of apigee hybrid installed) to the newer apigee hybrid version.

Apply the changes for apigee CRs. For non-prod environment, you can apply all changes to apigee components simultaneously
    
    
    kubectl apply -f ${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}
    

## Apigee Hybrid Rollback

  1. Restore apigee-hybrid-setup

Move to the directory that contains the previous version of apigee hybrid setup. If not available, restore it from the zip file created in step 1[link] during apigee hybrid upgrade.

  2. Rollback Kubernetes components

Apply the changes for apigee CRs
         
         kubectl apply -k ${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}
         

  3. Rollback controller

Follow the same set of steps provided create initialization resources and controller in apigee hybrid installation workflow. you can use a script or can follow provided manual steps to rollback initialization resources and controller.

  4. Cleanup

You will need to clean up any new additional resources created during upgrade like new components or service accounts introduced in the newer version of hybrid. What all resources need to be cleaned up and steps to clean them up will be provided in the upgrade guide.




## Deleting an environment

* * *

**Caution:** If you have multiple environments, make sure whatever secrets you are deleting are not referenced in the other environments. To check that, do `kubectl get env -n ${APIGEE_NAMESPACE} ${ENV_RESOURCE_NAME} -o yaml` and then grep for whatever resource you plan on deleting.

* * *

Following are the steps to delete all resources related to an environment from your kubernetes cluster:

  1. Get the name of the environment CR. This can be done by getting all the environments:
         
         kubectl get env -n ${APIGEE_NAMESPACE}
         

Store the resource name in `APIGEE_ENV` environment variable.

  2. Delete the environment encryption keys. For example, if you had not change the name of the encryption keys, then you can delete them by using:
         
         kubectl delete secret -n ${APIGEE_NAMESPACE} $APIGEE_ENV-encryption-keys
         

  3. Delete Google Cloud service account secrets:
         
         kubectl delete secret -n ${APIGEE_NAMESPACE} $(kubectl get env $APIGEE_ENV -n ${APIGEE_NAMESPACE} -o=jsonpath='{.spec.components.*.appServiceAccountSecretName}')
         

  4. Delete kubernetes service accounts:
         
         kubectl delete secret -n ${APIGEE_NAMESPACE} $(kubectl get env $APIGEE_ENV -n ${APIGEE_NAMESPACE} -o=jsonpath='{.spec.components.*.podServiceAccountName}')
         

  5. Delete the Apigee environment custom resource:
         
         kubectl -n ${APIGEE_NAMESPACE} delete env $APIGEE_ENV
         




### Deleting a hybrid setup

* * *

**Caution:** This is how the steps will appear for normal apigee hybrid installation, steps will slightly differ for advanced cases like having second organization within same cluster etc.

* * *

Following are the steps to delete all resources related to apigee hybrid from your kubernetes cluster:

  1. You will need to delete apigee user setup and schema setup jobs.
         
         # To list all jobs in ${APIGEE_NAMESPACE}
         kubectl -n ${APIGEE_NAMESPACE} get jobs
         # To delete all jobs in ${APIGEE_NAMESPACE}
         kubectl -n ${APIGEE_NAMESPACE} delete jobs $(kubectl -n ${APIGEE_NAMESPACE} get jobs -o custom-columns=':.metadata.name')
         

  2. You will need to delete the deployed apigee hybrid dataplane components. Use the following command to delete all components:
         
         kubectl delete -k ${INSTALL_DIR}/overlays/instances/$INSTANCE_NAME
         

  3. This step is only required if you have not relied on the default name for kubernetes service account secrets, Google Cloud service account secrets etc. If you have relied on default names then it would be deleted in next step otherwise you will need to delete them manually using following commands:
         
         kubectl delete secret -n ${APIGEE_NAMESPACE} $(kubectl get ${APIGEE_COMPONENT} ${APIGEE_COMPONENT_NAME} -n ${APIGEE_NAMESPACE} -o=jsonpath='{.spec.components.*.appServiceAccountSecretName}')
         kubectl delete secret -n ${APIGEE_NAMESPACE} $(kubectl get ${APIGEE_COMPONENT} ${APIGEE_COMPONENT_NAME} -n ${APIGEE_NAMESPACE} -o=jsonpath='{.spec.components.*.podServiceAccountName}')
         

  4. In case of OpenShift, you will need to delete scc (Security Context Constraints) created during installation of apigee hybrid.
         
         kubectl delete scc ${SECURITY_CONTEXT_CONSTRAINTS_NAME}
         

  5. Run the below command to delete roles, rolebindings, CRDs, controller deployments etc.
         
         kubectl delete -k ${INSTALL_DIR}/overlays/initialization/ingress
         kubectl delete -k ${INSTALL_DIR}/overlays/initialization/rbac
         kubectl delete -k ${INSTALL_DIR}/overlays/initialization/webhooks
         kubectl delete -k ${INSTALL_DIR}/overlays/initialization/crds
         kubectl delete -k ${INSTALL_DIR}/overlays/initialization/certificates
         

  6. Run the below command to delete apigee namespace
         
         kubectl delete -f ${INSTALL_DIR}/overlays/initialization/namespace.yaml
         

Alternatively, use the command:
         
         kubectl delete $APIGEE_NAMESPACE
         




## Multi Instance Installation

Multi instance setup refers to the hybrid setup that can span across multiple regions or within the same regions too. Apigee recommends organizing the configurations of the 2nd instance in a separate directory structure as the environment configurations (replicas,etc) are invariably different between instances. Configurations of every instance are decoupled and are organized independently in their respective folder structures.

For example - For an [Active-Passive](https://cloud.google.com/apigee/docs/hybrid/v1.8/multi-region) setup in a multi region scenario, you may want to configure a 2nd region in a warm standby with different sizings, configs.

In the folder structure below, you can make a copy of **instance1** directory called **instance2** and modify the datastore and ingress configurations as needed.

`apigee-hybrid-setup` folder structure for multi instance setup.]
    
    
    .
    ├── bases
    │   ├── controllers
    │   │   ├── apigee-controller
    │   │   │   ├── apigee-controller-deployment.yaml
    │   │   │   └── kustomization.yaml
    │   │   └── istiod
    │   │       ├── apigee-ingressgateway-manager-deployment.yaml
    │   │       └── kustomization.yaml
    │   └── initialization
    │       ├── certificates
    │       │   ├── certificates-and-issuers.yaml
    │       │   └── kustomization.yaml
    │       ├── crds
    │       │   ├── customresourcedefinition-apigeedatastores.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeedeployments.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeeenvironments.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeeorganizations.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeeredis.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeerouteconfigs.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeeroutes.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-apigeetelemetries.apigee.cloud.google.com.yaml
    │       │   ├── customresourcedefinition-cassandradatareplications.apigee.cloud.google.com.yaml
    │       │   └── kustomization.yaml
    │       ├── ingress
    │       │   ├── envoyfilter-1.11.yaml
    │       │   └── kustomization.yaml
    │       ├── openshift
    │       │   ├── kustomization.yaml
    │       │   └── scc.yaml
    │       ├── rbac
    │       │   ├── apigee-controller
    │       │   │   ├── kustomization.yaml
    │       │   │   └── rbac.yaml
    │       │   └── apigee-embedded-ingress-controller
    │       │       ├── cluster-role-bindings.yaml
    │       │       ├── cluster-roles.yaml
    │       │       ├── kustomization.yaml
    │       │       └── service-account.yaml
    │       └── webhooks
    │           ├── kustomization.yaml
    │           ├── mutatingwebhookconfiguration.yaml
    │           └── validatingwebhookconfiguration.yaml
    ├── instances
    │   └── instance1 (Add the 2nd instance under instances directory similar to instance1)
    │       ├── datastore
    │       │   ├── apigee-datastore.yaml
    │       │   ├── components
    │       │   │   ├── http-proxy
    │       │   │   │   ├── kustomization.yaml
    │       │   │   │   └── patch.yaml
    │       │   │   ├── imagepullsecret
    │       │   │   │   ├── kustomization.yaml
    │       │   │   │   └── patch.yaml
    │       │   │   ├── nodeselector
    │       │   │   │   ├── kustomization.yaml
    │       │   │   │   └── patch.yaml
    │       │   │   └── workload-identity
    │       │   │       ├── apigee-workload-identities.yaml
    │       │   │       ├── kustomization.yaml
    │       │   │       └── patch.yaml
    │       │   ├── kustomization.yaml
    │       │   └── secrets.yaml
    │       ├── environments
    │       │   ├── kustomization.yaml
    │       │   └── test
    │       │       ├── apigee-environment.yaml
    │       │       ├── components
    │       │       │   ├── http-proxy
    │       │       │   │   ├── kustomization.yaml
    │       │       │   │   └── patch.yaml
    │       │       │   ├── imagepullsecret
    │       │       │   │   ├── kustomization.yaml
    │       │       │   │   └── patch.yaml
    │       │       │   ├── nodeselector
    │       │       │   │   ├── kustomization.yaml
    │       │       │   │   └── patch.yaml
    │       │       │   └── workload-identity
    │       │       │       ├── apigee-workload-identities.yaml
    │       │       │       ├── kustomization.yaml
    │       │       │       └── patch.yaml
    │       │       ├── kustomization.yaml
    │       │       └── secrets.yaml
    │       ├── kustomization.yaml
    │       ├── organization
    │       │   ├── apigee-organization.yaml
    │       │   ├── components
    │       │   │   ├── http-proxy
    │       │   │   │   ├── kustomization.yaml
    │       │   │   │   └── patch.yaml
    │       │   │   ├── imagepullsecret
    │       │   │   │   ├── kustomization.yaml
    │       │   │   │   └── patch.yaml
    │       │   │   ├── nodeselector
    │       │   │   │   ├── kustomization.yaml
    │       │   │   │   └── patch.yaml
    │       │   │   └── workload-identity
    │       │   │       ├── apigee-workload-identities.yaml
    │       │   │       ├── kustomization.yaml
    │       │   │       └── patch.yaml
    │       │   ├── kustomization.yaml
    │       │   └── secrets.yaml
    │       ├── redis
    │       │   ├── apigee-redis.yaml
    │       │   ├── components
    │       │   │   ├── imagepullsecret
    │       │   │   │   ├── kustomization.yaml
    │       │   │   │   └── patch.yaml
    │       │   │   ├── nodeselector
    │       │   │   │   ├── kustomization.yaml
    │       │   │   │   └── patch.yaml
    │       │   │   └── workload-identity
    │       │   │       ├── apigee-workload-identities.yaml
    │       │   │       ├── kustomization.yaml
    │       │   │       └── patch.yaml
    │       │   ├── kustomization.yaml
    │       │   └── secrets.yaml
    │       ├── route-config
    │       │   ├── kustomization.yaml
    │       │   └── test-env-group
    │       │       ├── apigee-route-config.yaml
    │       │       ├── components
    │       │       │   ├── http-and-non-sni-client
    │       │       │   │   ├── apigee-route.yaml
    │       │       │   │   └── kustomization.yaml
    │       │       │   ├── http-client
    │       │       │   │   ├── apigee-route.yaml
    │       │       │   │   └── kustomization.yaml
    │       │       │   └── non-sni-client
    │       │       │       ├── apigee-route.yaml
    │       │       │       └── kustomization.yaml
    │       │       └── kustomization.yaml
    │       └── telemetry
    │           ├── apigee-telemetry.yaml
    │           ├── components
    │           │   ├── http-proxy
    │           │   │   ├── kustomization.yaml
    │           │   │   └── patch.yaml
    │           │   ├── imagepullsecret
    │           │   │   ├── kustomization.yaml
    │           │   │   └── patch.yaml
    │           │   ├── logger
    │           │   │   ├── kustomization.yaml
    │           │   │   └── patch.yaml
    │           │   ├── metrics
    │           │   │   ├── kustomization.yaml
    │           │   │   └── patch.yaml
    │           │   ├── nodeselector
    │           │   │   ├── kustomization.yaml
    │           │   │   └── patch.yaml
    │           │   ├── workload-identity-logger
    │           │   │   ├── apigee-workload-identities.yaml
    │           │   │   ├── kustomization.yaml
    │           │   │   └── patch.yaml
    │           │   └── workload-identity-metrics
    │           │       ├── apigee-workload-identities.yaml
    │           │       ├── kustomization.yaml
    │           │       └── patch.yaml
    │           └── kustomization.yaml
    ├── overlays
    │   ├── controllers
    │   │   ├── apigee-controller
    │   │   │   ├── apigee-hybrid-config.yaml
    │   │   │   ├── components
    │   │   │   │   ├── imagepullsecret
    │   │   │   │   │   ├── kustomization.yaml
    │   │   │   │   │   └── patch.yaml
    │   │   │   │   └── nodeselector
    │   │   │   │       ├── kustomization.yaml
    │   │   │   │       └── patch.yaml
    │   │   │   └── kustomization.yaml
    │   │   ├── istiod
    │   │   │   ├── apigee-ingressgateway-manager-deployment-patch.yaml
    │   │   │   ├── apigee-istio-mesh-config.yaml
    │   │   │   ├── components
    │   │   │   │   ├── imagepullsecret
    │   │   │   │   │   ├── kustomization.yaml
    │   │   │   │   │   └── patch.yaml
    │   │   │   │   └── nodeselector
    │   │   │   │       ├── kustomization.yaml
    │   │   │   │       └── patch.yaml
    │   │   │   └── kustomization.yaml
    │   │   └── kustomization.yaml
    │   ├── initialization
    │   │   ├── certificates
    │   │   │   ├── apigee-ingressgateway-manager-certificate.yaml
    │   │   │   └── kustomization.yaml
    │   │   ├── crds
    │   │   │   └── kustomization.yaml
    │   │   ├── ingress
    │   │   │   └── kustomization.yaml
    │   │   ├── namespace.yaml
    │   │   ├── openshift
    │   │   │   ├── kustomization.yaml
    │   │   │   └── scc.yaml
    │   │   ├── rbac
    │   │   │   ├── apigee-controller
    │   │   │   │   └── kustomization.yaml
    │   │   │   ├── apigee-embedded-ingress-controller
    │   │   │   │   └── kustomization.yaml
    │   │   │   └── kustomization.yaml
    │   │   └── webhooks
    │   │       ├── kustomization.yaml
    │   │       ├── mutatingwebhookconfiguration.yaml
    │   │       └── validatingwebhookconfiguration.yaml
    │   └── instances
    │       └── instance1
    │           ├── datastore
    │           │   ├── apigee-datastore.yaml
    │           │   ├── components
    │           │   │   ├── http-proxy
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── imagepullsecret
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── nodeselector
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── openshift-scc
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── scc.yaml
    │           │   │   └── workload-identity
    │           │   │       ├── apigee-workload-identities.yaml
    │           │   │       ├── kustomization.yaml
    │           │   │       └── patch.yaml
    │           │   ├── kustomization.yaml
    │           │   └── secrets.yaml
    │           ├── environments
    │           │   ├── kustomization.yaml
    │           │   └── test
    │           │       ├── apigee-environment.yaml
    │           │       ├── components
    │           │       │   ├── http-proxy
    │           │       │   │   ├── kustomization.yaml
    │           │       │   │   └── patch.yaml
    │           │       │   ├── imagepullsecret
    │           │       │   │   ├── kustomization.yaml
    │           │       │   │   └── patch.yaml
    │           │       │   ├── nodeselector
    │           │       │   │   ├── kustomization.yaml
    │           │       │   │   └── patch.yaml
    │           │       │   └── workload-identity
    │           │       │       ├── apigee-workload-identities.yaml
    │           │       │       ├── kustomization.yaml
    │           │       │       └── patch.yaml
    │           │       ├── kustomization.yaml
    │           │       └── secrets.yaml
    │           ├── kustomization.yaml
    │           ├── organization
    │           │   ├── apigee-organization.yaml
    │           │   ├── components
    │           │   │   ├── http-proxy
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── imagepullsecret
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── nodeselector
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   └── workload-identity
    │           │   │       ├── apigee-workload-identities.yaml
    │           │   │       ├── kustomization.yaml
    │           │   │       └── patch.yaml
    │           │   ├── kustomization.yaml
    │           │   └── secrets.yaml
    │           ├── redis
    │           │   ├── apigee-redis.yaml
    │           │   ├── components
    │           │   │   ├── imagepullsecret
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   ├── nodeselector
    │           │   │   │   ├── kustomization.yaml
    │           │   │   │   └── patch.yaml
    │           │   │   └── workload-identity
    │           │   │       ├── apigee-workload-identities.yaml
    │           │   │       ├── kustomization.yaml
    │           │   │       └── patch.yaml
    │           │   ├── kustomization.yaml
    │           │   └── secrets.yaml
    │           ├── route-config
    │           │   ├── kustomization.yaml
    │           │   └── test-envgroup
    │           │       ├── apigee-route-config.yaml
    │           │       ├── components
    │           │       │   ├── http-and-non-sni-client
    │           │       │   │   ├── apigee-route.yaml
    │           │       │   │   └── kustomization.yaml
    │           │       │   ├── http-client
    │           │       │   │   ├── apigee-route.yaml
    │           │       │   │   └── kustomization.yaml
    │           │       │   └── non-sni-client
    │           │       │       ├── apigee-route.yaml
    │           │       │       └── kustomization.yaml
    │           │       └── kustomization.yaml
    │           └── telemetry
    │               ├── apigee-telemetry.yaml
    │               ├── components
    │               │   ├── http-proxy
    │               │   │   ├── kustomization.yaml
    │               │   │   └── patch.yaml
    │               │   ├── imagepullsecret
    │               │   │   ├── kustomization.yaml
    │               │   │   └── patch.yaml
    │               │   ├── logger
    │               │   │   ├── kustomization.yaml
    │               │   │   └── patch.yaml
    │               │   ├── metrics
    │               │   │   ├── kustomization.yaml
    │               │   │   └── patch.yaml
    │               │   ├── nodeselector
    │               │   │   ├── kustomization.yaml
    │               │   │   └── patch.yaml
    │               │   ├── openshift-scc
    │               │   │   ├── kustomization.yaml
    │               │   │   └── scc.yaml
    │               │   ├── workload-identity-logger
    │               │   │   ├── apigee-workload-identities.yaml
    │               │   │   └── kustomization.yaml
    │               │   └── workload-identity-metrics
    │               │       ├── apigee-workload-identities.yaml
    │               │       ├── kustomization.yaml
    │               │       └── patch.yaml
    │               └── kustomization.yaml
    ├── README.md
    ├── templates
    │   ├── ingress-certificate.yaml
    │   ├── ingress-cert-secret.yaml
    │   └── service-account-key-secret.yaml
    └── tools
        ├── apigee-hybrid-setup.sh
        ├── common.sh
        ├── create-service-account.sh
        └── dump_kubernetes.sh
    

### Multi Instance setup on GKE

#### Prerequisites

Before configuring multiple instances of hybrid, you are expected have completed the following prerequisites:

  * Set up Kubernetes clusters in multiple regions(same or different) with different CIDR blocks
  * Set up cross-region communication
  * Open Cassandra ports 7000 and 7001 between Kubernetes clusters across all regions (7000 may be used as a backup option during troubleshooting). See also [Configure ports](https://cloud.google.com/apigee/docs/hybrid/v1.8/ports).



* * *

**Note:** Apigee recommends that you ensure that your servers' times are synchronized. Several features such as expiration and token revocation rely on accurate system times. If you host the runtime components in different datacenters, then be sure that the system times are synchronized.

You can use a tool such as **ntpdate** to verify that server times are synchronized.

* * *

#### Configure the multi-region seed host

  1. Make a copy of the $INSTANCE_NAME folder from your existing instance and add it under instances folder.
  2. Modify the value of the namespace field if it differs from instance1 namespace.
  3. Follow the steps specified in Specifying ingress TLS certificates to modify the ingress configuration for the other instance.
  4. Refer to the [Managing Apigee ingress gateway](https://cloud.google.com/apigee/docs/hybrid/v1.8/managing-ingress) for information on configuring the load balancer ip for the other instance

* * *

**Note:** It is recommended not to modify the configurations of the rest of the components except the ones listed out in the upcoming steps.

* * *

  5. Set the kubectl context to the original cluster before retrieving the seed name
         
         kubectl config use-context original-cluster-name
         

  6. Run the following [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) command to identify a seed host address for Cassandra in the current region.
         
         kubectl get pods -o wide -n apigee -l app=apigee-cassandra
         

  7. Any of the Pod IPs returned from the previous command can be considered as the multi-region seed host.

  8. In the 2nd instance, configure the value of multiRegionSeedHost in the apigee datastore CR under ${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}/datastore/apigee-datastore.yaml




#### Set up the new instance

  1. Set the context to the existing cluster
         
         kubectl config use-context existing-cluster-name
         

  2. Export the apigee-ca secret to a file
         
         kubectl -n cert-manager get secret apigee-root-certificate -o yaml > apigee-root-certificate.yaml
         

  3. Set the context to the new region's cluster name:
         
         kubectl config use-context NEW_CLUSTER_NAME
         

  4. Import the secret to the new cluster
         
         kubectl -n cert-manager apply -f apigee-root-certificate.yaml
         

  5. Install hybrid in the new instance (region) by following the steps outlined in Create initialization resources and controller.

  6. Set up Cassandra on all the pods in the new data centers. Get apigeeorg from the cluster with the following command:
         
         kubectl get apigeeorg -n apigee -o json | jq ".items[].metadata.name"
         

  7. Create a cassandra data replication custom resource (YAML) file. The file can have any name. In the following examples the file will have the name datareplication.yaml. The file must contain the following
         
         apiVersion: apigee.cloud.google.com/v1alpha1
         kind: CassandraDataReplication
         metadata:
         name: REGION_EXPANSION
         namespace: NAMESPACE
         spec:
         organizationRef: APIGEEORG_VALUE
         force: false
         source:
           region: SOURCE_REGION
         

Where:

     * REGION_EXPANSION is the name you are giving this metadata. You can choose a name like "cassandra-data-replication"
     * NAMESPACE is the same namespace that was chosen for the 2nd instance. This is usually "apigee".
     * APIGEEORG_VALUE is the value output from the kubectl get apigeeorg -n apigee -o json | jq ".items[].metadata.name" command in the previous step.
     * SOURCE_REGION is the value of the value of cassandra datacenter from the nodetool status from the source cluster.
  8. Apply the CassandraDataReplication with the following command:
         
         kubectl apply -f datareplication.yaml
         

  9. Verify the rebuild status using the following command.

* * *

**Note:** The rebuild operation can take up to several hours depending on the data size.

* * *
         
         kubectl -n apigee get apigeeds -o json | jq ".items[].status.cassandraDataReplication"
         

The result should look something like
         
         {
         "rebuildDetails": {
           "apigee-cassandra-default-0": {
             "state": "complete",
             "updated": 1623105760
           },
           "apigee-cassandra-default-1": {
             "state": "complete",
             "updated": 1623105765
           },
           "apigee-cassandra-default-2": {
             "state": "complete",
             "updated": 1623105770
           }
         },
         "state": "complete",
         "updated": 1623105770
         }
         

  10. Verify the rebuild processes from the logs. Also, verify the data size using the nodetool status command:
         
         kubectl logs apigee-cassandra-default-0 -f -n apigee
         

Refer the datastore/secrets.yaml for the JMX_user and JMX_password
         
         kubectl exec apigee-cassandra-default-0 -n apigee  -- nodetool -u JMX_user -pw JMX_password status
         

  11. Remove `multiRegionSeedHost` from the apigee datastore CR and run the below command to apply the change
         
         kubectl apply k apply -k ${INSTALL_DIR}/overlays/instances/${INSTANCE_DIR}/datastore
         

  12. Check the Cassandra cluster status

The following command is useful to see if the cluster setup is successful in two data centers. The command checks the nodetool status for the two regions.
         
         kubectl exec apigee-cassandra-default-0 -n apigee  -- nodetool -u JMX_user -pw JMX_password status
         
         
         
         Datacenter: us-central1
         =======================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address     Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.12.1.45  112.09 KiB  256          100.0%            3c98c816-3f4d-48f0-9717-03d0c998637f  ra-1
         UN  10.12.4.36  95.27 KiB  256          100.0%            0a36383d-1d9e-41e2-924c-7b62be12d6cc  ra-1
         UN  10.12.5.22  88.7 KiB   256          100.0%            3561f4fa-af3d-4ea4-93b2-79ac7e938201  ra-1
         Datacenter: us-west1
         ====================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address     Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.0.4.33   78.69 KiB  256          100.0%               a200217d-260b-45cd-b83c-182b27ff4c99  ra-1
         UN  10.0.0.21   78.68 KiB  256          100.0%               9f3364b9-a7a1-409c-9356-b7d1d312e52b  ra-1
         UN  10.0.1.26   15.46 KiB  256          100.0%               1666df0f-702e-4c5b-8b6e-086d0f2e47fa  ra-1
         




## Troubleshooting

### Supportability, Diagnosis & Troubleshooting Guide

<https://cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/troubleshooting-apigee-hybrid>.

### Manual Cleanup after using forceDelete in multi Region Apigee Hybrid setup

  * In the following example, there are 2 regions - `us-east1` and `us-west1`.
  * In the `us-west1` region, apigee datastore was deleted using force delete.
  * In the `us-east1` region, cassandra is still up and running.
  * Verify `apigeeds` is deleted using command
        
        kubectl get apigeeds -n apigee
        No resources found in apigee namespace.
        

  * Change the kubectl context to the other region where the cassandra cluster is still up and running (here `us-east1`) region.

  * Verify datastore is in running state
        
        kubectl get apigeeds -n apigee
        NAME      STATE     AGE
        default      running    23h
        

  * Exec into one of cassandra pods in up region (here `us-east1`) region
        
        kubectl exec -it -n apigee apigee-cassandra-default-0 -- bash
        apigee@apigee-cassandra-default-0:~$
        

  * Check nodetool status, it will show all nodes down in the deleted region (here `us-west1`) region
        
        apigee@apigee-cassandra-default-0:~$ nodetool -u ${APIGEE_JMX_USER} -pw ${APIGEE_JMX_PASSWORD} status
        
        
        Datacenter: us-east1
        ====================
        Status=Up/Down
        |/ State=Normal/Leaving/Joining/Moving
        --     Address         Load           Tokens   Owns    Host ID                                                           Rack
        UN  10.52.0.212   685.01 KiB  256          ?         e1aa61e3-4eae-4549-9b58-506d495d87ab   ra-1
        UN  10.52.0.72     606.75 KiB  256          ?         477dfc03-f93e-40ea-810a-d15769822ad5     ra-1
        UN  10.52.0.104   648.3 KiB    256          ?         a8854cff-c2e3-4f0c-a342-e692787efcab        ra-1
        Datacenter: us-west1
        ====================
        Status=Up/Down
        |/ State=Normal/Leaving/Joining/Moving
        --     Address         Load             Tokens   Owns     Host ID                                                           Rack
        DN  10.60.0.143   567.06 KiB    256          ?           355d6ace-ab77-42cb-8138-9993bfd62d0e    ra-1
        DN  10.60.0.40     535.99 KiB    256          ?           4ed2c903-ff56-40fa-a15e-80a3de3cb22d      ra-1
        DN  10.60.0.17     573.08 KiB    256          ?           f9a50d19-c04a-4d0d-a088-612384bed9f5     ra-1
        

  * Remove all the nodes in the deleted region (here `us-west1`) region
        
        apigee@apigee-cassandra-default-0:~$ nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD removenode 355d6ace-ab77-42cb-8138-9993bfd62d0e
        apigee@apigee-cassandra-default-0:~$ nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD removenode 4ed2c903-ff56-40fa-a15e-80a3de3cb22d
        apigee@apigee-cassandra-default-0:~$ nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD removenode f9a50d19-c04a-4d0d-a088-612384bed9f5
        

  * Verify no nodes of the deleted region (here `us-west1`) are left
        
        apigee@apigee-cassandra-default-0:~$ nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD status
        
        
        
        Datacenter: us-east1
        ====================
        Status=Up/Down
        |/ State=Normal/Leaving/Joining/Moving
        --     Address         Load             Tokens  Owns   Host ID                                                           Rack
        UN  10.52.0.212   699.71 KiB    256          ?        e1aa61e3-4eae-4549-9b58-506d495d87ab  ra-1
        UN  10.52.0.72     586.77 KiB    256          ?        477dfc03-f93e-40ea-810a-d15769822ad5    ra-1
        UN  10.52.0.104   623.6 KiB      256          ?        a8854cff-c2e3-4f0c-a342-e692787efcab       ra-1
        

  * Once this is complete, delete the user setup job in up region (here `us-east1`). Job will be recreated again automatically within a few seconds.
        
        kubectl get jobs -n apigee
        
        
        
        ​​NAME                                                                                    COMPLETIONS   DURATION   AGE
        apigee-cassandra-schema-setup-apigee--0d2504c                    0/1           5m54s      5m54s
        apigee-cassandra-user-setup--apigee--0d2504c                          0/1            7s         7s
        
        
        
        kubectl delete job apigee-cassandra-user-setup--apigee--0d2504c
        

  * Wait for user setup job to complete
        
        kubectl get jobs -n apigee
        
        
        ​​NAME                                                                                    COMPLETIONS   DURATION   AGE
        apigee-cassandra-schema-setup-apigee--0d2504c                    1/1           5m54s      5m54s
        apigee-cassandra-user-setup--apigee--0d2504c                      1/1           7m                7m
        

  * Verify keyspaces are not having the deleted region.

  * Create a cassandra debugging pod.

    * Follow hybrid version 1.5+, follow documentation of cassandra troubleshooting guide (e.g. for hybrid 1.5 - [link](https://cloud.google.com/apigee/docs/hybrid/v1.8/ts-cassandra#create-a-client-container-for-debugging), hybrid 1.6 - [link](https://cloud.google.com/apigee/docs/hybrid/v1.8/ts-cassandra#create-a-client-container-for-debugging)) and then exec into the pod created
  * Login to cqlsh in debugging pod using the command
        
        apigee@cassandra-debug-client:~$ cqlsh apigee-cassandra-default-0.apigee-cassandra-default.apigee.svc.cluster.local -u ddl_user --ssl
        Password:
        

  * Verify the `us-west1` region is removed from all the keyspaces
        
        ddl_user@cqlsh> SELECT * FROM system_schema.keyspaces;
        
        
        keyspace_name              | durable_writes | replication
        ---------------------------+----------------+-----------------------------------------------------------------------------------
        cache_prince_hybrid_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'us-east1': '3'}
          rtc_prince_hybrid_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'us-east1': '3'}
                        system_auth |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'us-east1': '3'}
                      system_schema |           True |                            {'class': 'org.apache.cassandra.locator.LocalStrategy'}
        quota_prince_hybrid_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'us-east1': '3'}
          kms_prince_hybrid_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'us-east1': '3'}
                 system_distributed |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'us-east1': '3'}
                             system |           True |                            {'class': 'org.apache.cassandra.locator.LocalStrategy'}
                             perses |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'us-east1': '3'}
          kvm_prince_hybrid_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'us-east1': '3'}
                      system_traces |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'us-east1': '3'}
        (11 rows)
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
