---
url: https://docs.cloud.google.com/migrate/kf/docs/2.3/install/
title: Install Kf \u00a0|\u00a0 Kf 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:49.931028+00:00
---

# Install Kf  |  Kf 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.3/install/

Version 2.3

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.3 ](https://docs.cloud.google.com/migrate/kf/docs/2.3)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.3/getting-started)



Send feedback 

#  Install Kf Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up a GKE cluster, then install Kf and its dependencies. 

## Before you begin

### Overview

**Note:** Autopilot GKE clusters are not currently able to run Kf. Please use a Standard GKE cluster. For more information about these modes, and to learn more about Autopilot, see the [Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).

  * Your GKE cluster must meet the following requirements:

    * Optional, but recommended, the cluster should be dedicated to Kf. We recommend that you only install Kf and its dependencies to ensure that the compatibility matrix is maintained.

    * At least four nodes. If you need to add nodes, see [Resizing a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster).

    * The minimum machine type that has at least four vCPUs, such as `e2-standard-4`. If the machine type for your cluster doesn't have at least four vCPUs, change the machine type as described in [Migrating workloads to different machine types](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrating-node-pool).

    * Optional, but recommended, enroll the cluster in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). Follow the instructions in [Enrolling an existing cluster in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#enrolling_an_existing_cluster_in_a_release_channel) if you have a static GKE version.

    * [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled.

    * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) enabled.

    * [Cloud Service Mesh (ASM)](https://docs.cloud.google.com/service-mesh/docs).

    * [Tekton](https://github.com/tektoncd/pipeline) installed. See the [Dependency matrix](https://docs.cloud.google.com/migrate/kf/docs/2.3/downloads#dependency_matrix) for the version.

    * A Google Service Account with the following IAM policy (creation instructions linked below):

      * `roles/iam.serviceAccountAdmin`
      * `serviceAccount:${CLUSTER_PROJECT}.svc.id.goog[kf/controller]` (for member `serviceAccount:${CLUSTER_PROJECT}.svc.id.goog[kf/controller]`)

**Note:** The Clean up section has instructions on deleting the cluster.

### Enable support for Compute Engine

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Compute Engine API.

[ Enable the API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)




### Enable support for Artifact Registry

  1. Enable the Artifact Registry API.

[ Enable the Artifact Registry API](https://console.cloud.google.com/apis/api/artifactregistry.googleapis.com/overview)




### Enable and configure GKE

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Create and prepare a new GKE cluster

### Setup environment variables

**Note:** Export these environment variables in your terminal or Cloud Shell to make subsequent commands work. If you disconnect from your shell environment and reconnect later, you need to set up the variables again.**Note:** Before setting up environment variables, be sure to check the dependency matrix on the [Kf Downloads](https://docs.cloud.google.com/migrate/kf/docs/2.3/downloads) page for the given Kf version.

### Linux
    
    
    export PROJECT_ID=YOUR_PROJECT_ID
    export CLUSTER_PROJECT_ID=YOUR_PROJECT_ID
    export CLUSTER_NAME=kf-cluster
    export COMPUTE_ZONE=us-central1-a
    export COMPUTE_REGION=us-central1
    export CLUSTER_LOCATION=${COMPUTE_ZONE}
    export NODE_COUNT=4
    export MACHINE_TYPE=e2-standard-4
    export NETWORK=default
    export KF_VERSION=v2.3.2
    export TEKTON_VERSION=v0.19.0
    

### Windows Powershell
    
    
    Set-Variable -Name PROJECT_ID -Value YOUR_PROJECT_ID
    Set-Variable -Name CLUSTER_PROJECT_ID -Value YOUR_PROJECT_ID
    Set-Variable -Name CLUSTER_NAME -Value kf-cluster
    Set-Variable -Name COMPUTE_ZONE -Value us-central1-a
    Set-Variable -Name COMPUTE_REGION -Value us-central1
    Set-Variable -Name CLUSTER_LOCATION -Value $COMPUTE_ZONE
    Set-Variable -Name NODE_COUNT -Value 4
    Set-Variable -Name MACHINE_TYPE -Value e2-standard-4
    Set-Variable -Name NETWORK -Value default
    Set-Variable -Name KF_VERSION -Value v2.3.0
    Set-Variable -Name TEKTON_VERSION -Value v0.19.0
    

### Service account setup

Create a GCP service account (GSA) that will be associated with a Kubernetes Service Account via [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). This prevents the need to create and inject a service account key.

**Note:** Please read through and understand the security implications of using Workload Identity in the [Security Overview](https://docs.cloud.google.com/migrate/kf/docs/2.3/concepts/security-overview#workload_identity) document.

  1. Create the service account that Kf will use.
         
         gcloud iam service-accounts create ${CLUSTER_NAME}-sa \
           --project=${CLUSTER_PROJECT_ID} \
           --description="GSA for Kf ${CLUSTER_NAME}" \
           --display-name="${CLUSTER_NAME}"

  2. Allow the service account to modify its own policy. The Kf controller will use this to add new (name)spaces to the policy, allowing reuse for Workload Identity.
         
         gcloud iam service-accounts add-iam-policy-binding ${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com \
           --project=${CLUSTER_PROJECT_ID} \
           --role="roles/iam.serviceAccountAdmin" \
           --member="serviceAccount:${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com"

  3. Give monitoring metrics role for write access to Cloud Monitoring.
         
         gcloud projects add-iam-policy-binding ${CLUSTER_PROJECT_ID} \
           --member="serviceAccount:${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/monitoring.metricWriter"

  4. Give logging role for write access to Cloud Logging.
         
         gcloud projects add-iam-policy-binding ${CLUSTER_PROJECT_ID} \
           --member="serviceAccount:${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/logging.logWriter"




### Create GKE cluster

**Note:** For demonstration purposes, these instructions use a zonal cluster. For production deployments, a regional cluster is recommended.
    
    
    gcloud container clusters create ${CLUSTER_NAME} \
      --project=${CLUSTER_PROJECT_ID} \
      --zone=${CLUSTER_LOCATION} \
      --num-nodes=${NODE_COUNT} \
      --machine-type=${MACHINE_TYPE} \
      --network=${NETWORK} \
      --addons=HttpLoadBalancing,HorizontalPodAutoscaling,NetworkPolicy \
      --enable-stackdriver-kubernetes \
      --enable-ip-alias \
      --enable-network-policy \
      --enable-autorepair \
      --enable-autoupgrade \
      --scopes=https://www.googleapis.com/auth/cloud-platform \
      --release-channel=regular \
      --workload-pool="${CLUSTER_PROJECT_ID}.svc.id.goog" \
      --service-account="${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com"

### Set firewall rules

Kf requires some firewall ports to be open. The master node needs to be able to communicate with pods on ports 80, 443, 8080, 8443 and 6443.

### Enable Workload Identity

Now that you have a service account and GKE cluster, associate the cluster's identity namespace with the cluster.
    
    
    gcloud iam service-accounts add-iam-policy-binding \
      "${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
      --project=${CLUSTER_PROJECT_ID} \
      --role="roles/iam.workloadIdentityUser" \
      --member="serviceAccount:${CLUSTER_PROJECT_ID}.svc.id.goog[kf/controller]"

### Target GKE cluster

Configure kubectl command line access by running the following command.
    
    
    gcloud container clusters get-credentials ${CLUSTER_NAME} \
        --project=${CLUSTER_PROJECT_ID} \
        --zone=${CLUSTER_LOCATION}

### Create an Artifact Registry repository

  1. Create an Artifact Registry for container images to be stored.
         
         gcloud artifacts repositories create ${CLUSTER_NAME} \
           --project=${CLUSTER_PROJECT_ID} \
           --repository-format=docker \
           --location=${COMPUTE_REGION}

  2. Grant the service account permission on the Artifact Registry repository.
         
         gcloud artifacts repositories add-iam-policy-binding ${CLUSTER_NAME} \
           --project=${CLUSTER_PROJECT_ID} \
           --location=${COMPUTE_REGION} \
           --member="serviceAccount:${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role='roles/artifactregistry.writer'




### Install software dependencies on cluster

**Note:** Before installing anything, be sure to check the dependency matrix on the [Kf Downloads](https://docs.cloud.google.com/migrate/kf/docs/2.3/downloads) page for the given Kf version.

  1. Install Service Mesh.

**Note:** See the [Dependency matrix](https://docs.cloud.google.com/migrate/kf/docs/2.3/downloads#dependency_matrix) for the correct version.
  2. Install Tekton:

**Note:** See the [Dependency matrix](https://docs.cloud.google.com/migrate/kf/docs/2.3/downloads#dependency_matrix) for the correct version.
         
         kubectl apply -f "https://github.com/tektoncd/pipeline/releases/download/${TEKTON_VERSION}/release.yaml"




## Install Kf

  1. See Create and prepare a GKE cluster for Kf to create a cluster prepared to run Kf.

  2. Select and note the desired Kf release. Reference the [Kf Downloads](https://docs.cloud.google.com/migrate/kf/docs/2.3/downloads) page for available versions

**Note:** Many of the commands in this guide depend on these environment variables. If you disconnect from your shell environment and reconnect later, you will need to set up the variables again.
  3. Install CLI:

### Linux

This will install `kf` for all users on the system. Follow the instructions in the Cloud Shell tab to install it just for yourself.
         
         gcloud storage cp gs://kf-releases/${KF_VERSION}/kf-linux /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Mac

This will install `kf` for all users on the system.
         
         gcloud storage cp gs://kf-releases/${KF_VERSION}/kf-darwin /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Cloud Shell

This will install `kf` on your Cloud Shell instance if you use `bash`, the instructions may need to be modified for other shells.
         
         mkdir -p ~/bin
         gcloud storage cp gs://kf-releases/${KF_VERSION}/kf-linux ~/bin/kf
         chmod a+x ~/bin/kf
         echo "export PATH=$HOME/bin:$PATH" >> ~/.bashrc
         source ~/.bashrc

### Windows

This will download `kf` to current directory. Add it to the path if you want to call if from anywhere other than the current directory.
         
         gcloud storage cp gs://kf-releases/${KF_VERSION}/kf-windows.exe kf.exe

  4. Install server components:

### Linux and Mac

This will download kf.yaml to current directory.
         
         gcloud storage cp gs://kf-releases/${KF_VERSION}/kf.yaml /tmp/kf.yaml
         kubectl apply -f /tmp/kf.yaml

### Windows

This will download kf.yaml to current directory.
         
         gcloud storage cp gs://kf-releases/${KF_VERSION}/kf.yaml kf.yaml
         kubectl apply -f kf.yaml

  5. Setup secrets:
         
         export WI_ANNOTATION=iam.gke.io/gcp-service-account=${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com
         
         kubectl annotate serviceaccount controller ${WI_ANNOTATION} \
         --namespace kf \
         --overwrite
         
         echo "{\"apiVersion\":\"v1\",\"kind\":\"ConfigMap\",\"metadata\":{\"name\":\"config-secrets\", \"namespace\":\"kf\"},\"data\":{\"wi.googleServiceAccount\":\"${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com\"}}" | kubectl apply -f -

  6. Setup Kf defaults, these values can be changed later. The example below uses [domain templates](https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/setting-up-a-custom-domain#domain_templates) with a wildcard DNS provider to provide each Space its own domain name:
         
         export CONTAINER_REGISTRY=${COMPUTE_REGION}-docker.pkg.dev/${CLUSTER_PROJECT_ID}/${CLUSTER_NAME}
         export DOMAIN='$(SPACE_NAME).$(CLUSTER_INGRESS_IP).nip.io'
         
         kubectl patch configmaps config-defaults \
         -n=kf \
         -p="{\"data\":{\"spaceContainerRegistry\":\"${CONTAINER_REGISTRY}\",\"spaceClusterDomains\":\"- domain: ${DOMAIN}\"}}"

  7. Validate installation:
         
         kf doctor --retries 10

**Note:** This command will inspect the cluster to ensure Kf and its dependencies are installed and working. It will run up to 10 times to give the Kubernetes cluster time to reconcile, and should result in a series `PASS` results. If the status for any component results in `FAIL` after the retries, please see the [Kf Troubleshooting](https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/troubleshooting) page.



## Clean up

These steps should remove all the components created in the Create and prepare a new GKE cluster section.

  1. Delete Google Service Account:
         
         gcloud iam service-accounts delete ${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com

  2. Delete IAM policy bindings:
         
         gcloud projects remove-iam-policy-binding ${CLUSTER_PROJECT_ID} \
           --member="serviceAccount:${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/storage.admin"
         
         gcloud projects remove-iam-policy-binding ${CLUSTER_PROJECT_ID} \
           --member="serviceAccount:${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/iam.serviceAccountAdmin"
         
         gcloud projects remove-iam-policy-binding ${CLUSTER_PROJECT_ID} \
           --member="serviceAccount:${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/monitoring.metricWriter"

  3. Delete container image repository:
         
         gcloud artifacts repositories delete ${CLUSTER_NAME} \
           --location=${COMPUTE_REGION}

  4. Delete GKE cluster:
         
         gcloud container clusters delete ${CLUSTER_NAME} --zone ${CLUSTER_LOCATION}




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
