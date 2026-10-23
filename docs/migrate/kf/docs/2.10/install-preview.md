---
url: https://docs.cloud.google.com/migrate/kf/docs/2.10/install-preview/
title: Install Kf on Google Cloud (Preview) \u00a0|\u00a0 Kf 2.10 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:05.255985+00:00
---

# Install Kf on Google Cloud (Preview)  |  Kf 2.10  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.10/install-preview/

Version 2.10

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
  * [ 2.10 ](https://docs.cloud.google.com/migrate/kf/docs/2.10)



Send feedback 

#  Install Kf on Google Cloud (Preview) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to set up a GKE cluster, and then install Kf and its dependencies using new features in preview.

**Note:** This installation guide includes the following notable differences from the GA installation guide:

  * Kf will use the new v2 wrapped stack to deliver cloud native buildpack benefits for legacy applications.
  * Removes Config Connector as a dependency.
  * Removes the `serviceAccountUpdater`custom IAM role.



## Before you begin

**Note:** Autopilot GKE clusters are not currently able to run Kf. Use a Standard GKE cluster. For more information about these modes, and to learn more about Autopilot, see the [Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).

### GKE cluster requirements

  * Optional, but recommended, the cluster should be dedicated to Kf. We recommend that you only install Kf and its dependencies to ensure that the compatibility matrix is maintained.

  * At least four nodes. If you need to add nodes, see [Resizing a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster).

  * The minimum machine type that has at least four vCPUs, such as `e2-standard-4`. If the machine type for your cluster doesn't have at least four vCPUs, change the machine type as described in [Migrating workloads to different machine types](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrating-node-pool).

  * Optional, but recommended, enroll the cluster in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). Follow the instructions in [Enrolling an existing cluster in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#enrolling_an_existing_cluster_in_a_release_channel) if you have a static GKE version.

  * [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled.




### Kf requirements

Review and understand the access permissions of components in Kf in the [Kf dependencies and architecture page](https://docs.cloud.google.com/migrate/kf/docs/2.10/concepts/kf-dependencies).

The [Dependency matrix](https://docs.cloud.google.com/migrate/kf/docs/2.10/downloads#dependency_matrix) lists the specific versions.

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs)

  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs)

  * [Config Connector](https://docs.cloud.google.com/config-connector/docs)

  * [Tekton](https://github.com/tektoncd/pipeline) for use by Kf; this is not a user facing service

  * A dedicated Google Service Account


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



## Prepare a new GKE cluster and related services

### Set up environment variables

**Note:** Export these environment variables in your terminal or Cloud Shell to make subsequent commands work. If you disconnect from your shell environment and reconnect later, you need to set up the variables again.

### Linux and Mac
    
    
    export PROJECT_ID=YOUR_PROJECT_ID
    export CLUSTER_PROJECT_ID=YOUR_PROJECT_ID
    export CLUSTER_NAME=kf-cluster
    export COMPUTE_ZONE=us-central1-a
    export COMPUTE_REGION=us-central1
    export CLUSTER_LOCATION=${COMPUTE_ZONE} # Replace ZONE with REGION to switch
    export NODE_COUNT=4
    export MACHINE_TYPE=e2-standard-4
    export NETWORK=default
    

### Windows PowerShell
    
    
    Set-Variable -Name PROJECT_ID -Value YOUR_PROJECT_ID
    Set-Variable -Name CLUSTER_PROJECT_ID -Value YOUR_PROJECT_ID
    Set-Variable -Name CLUSTER_NAME -Value kf-cluster
    Set-Variable -Name COMPUTE_ZONE -Value us-central1-a
    Set-Variable -Name COMPUTE_REGION -Value us-central1
    Set-Variable -Name CLUSTER_LOCATION -Value $COMPUTE_ZONE # Replace ZONE with REGION to switch
    Set-Variable -Name NODE_COUNT -Value 4
    Set-Variable -Name MACHINE_TYPE -Value e2-standard-4
    Set-Variable -Name NETWORK -Value default
    

### Set up service account

Create a Google Cloud service account that will be associated with a Kubernetes Service Account via [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). This prevents the need to create and inject a service account key.

**Note:** Read through and understand the security implications of using Workload Identity in the [Security overview](https://docs.cloud.google.com/migrate/kf/docs/2.10/concepts/security-overview#workload_identity) document.

  1. Create the service account that Kf will use.
         
         gcloud iam service-accounts create ${CLUSTER_NAME}-sa \
         --project=${CLUSTER_PROJECT_ID} \
         --description="GSA for Kf ${CLUSTER_NAME}" \
         --display-name="${CLUSTER_NAME}"

  2. Grant the monitoring metrics role to the service account for write access to Cloud Monitoring.
         
         gcloud projects add-iam-policy-binding ${CLUSTER_PROJECT_ID} \
           --member="serviceAccount:${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/monitoring.metricWriter"

  3. Grant the logging role to the service account for write access to Cloud Logging.
         
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
      --disk-size "122" \
      --network=${NETWORK} \
      --addons HorizontalPodAutoscaling,HttpLoadBalancing,GcePersistentDiskCsiDriver \
      --enable-dataplane-v2 \
      --enable-stackdriver-kubernetes \
      --enable-ip-alias \
      --enable-autorepair \
      --enable-autoupgrade \
      --scopes cloud-platform \
      --release-channel=regular \
      --workload-pool="${CLUSTER_PROJECT_ID}.svc.id.goog" \
      --service-account="${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com"

### Set firewall rules

Kf requires some firewall ports to be open. The master node needs to be able to communicate with pods on ports 80, 443, 8080, 8443 and 6443.

### Enable Workload Identity

Now that you have a service account and GKE cluster, associate the cluster's identity namespace with the cluster.
    
    
    gcloud iam service-accounts add-iam-policy-binding \
      --project=${CLUSTER_PROJECT_ID} \
      --role roles/iam.workloadIdentityUser \
      --member "serviceAccount:${CLUSTER_PROJECT_ID}.svc.id.goog[kf/controller]" \
      "${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com"
    
    gcloud iam service-accounts add-iam-policy-binding \
      --project=${CLUSTER_PROJECT_ID} \
      --role roles/iam.workloadIdentityUser \
      --member "serviceAccount:${CLUSTER_PROJECT_ID}.svc.id.goog[cnrm-system/cnrm-controller-manager]" \
      "${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com"

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




## Install software dependencies on a cluster

**Note:** The dependency matrix on the [Kf Downloads](https://docs.cloud.google.com/migrate/kf/docs/2.10/downloads) page has supported dependency version numbers for each Kf version.

  1. Install Cloud Service Mesh.

     1. Follow the [Cloud Service Mesh install guide](https://docs.cloud.google.com/service-mesh/docs/unified-install/install).

     2. After installing Cloud Service Mesh, you must create an ingress gateway using the [gateway install guide](https://docs.cloud.google.com/service-mesh/docs/unified-install/install#install_gateways).

  2. Install Tekton:
         
         kubectl apply -f "https://storage.googleapis.com/tekton-releases/pipeline/previous/v0.32.1/release.yaml"




## Install Kf

**Note:** Ensure your cluster meets the requirements found in Create and prepare a GKE cluster for Kf.

  1. Install the Kf CLI:

### Linux

This command installs the Kf CLI for all users on the system. Follow the instructions in the Cloud Shell tab to install it just for yourself.
         
         gcloud storage cp gs://kf-releases/v2.10.0/kf-linux /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Mac

This command installs `kf` for all users on the system.
         
         gcloud storage cp gs://kf-releases/v2.10.0/kf-darwin /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Cloud Shell

This command installs `kf` on your Cloud Shell instance if you use `bash`, the instructions may need to be modified for other shells.
         
         mkdir -p ~/bin
         gcloud storage cp gs://kf-releases/v2.10.0/kf-linux ~/bin/kf
         chmod a+x ~/bin/kf
         echo "export PATH=$HOME/bin:$PATH" >> ~/.bashrc
         source ~/.bashrc

### Windows

This command downloads `kf` to current directory. Add it to the path if you want to call if from anywhere other than the current directory.
         
         gcloud storage cp gs://kf-releases/v2.10.0/kf-windows.exe kf.exe

  2. Install the operator:
         
         kubectl apply -f "https://storage.googleapis.com/kf-releases/v2.10.0/operator.yaml"

  3. Install Kf `AppDevExperience Build` (ADX Build).
         
         export CONTAINER_REGISTRY=${COMPUTE_REGION}-docker.pkg.dev/${CLUSTER_PROJECT_ID}/${CLUSTER_NAME}
         cat << EOF | kubectl apply --filename -
         apiVersion: builds.appdevexperience.dev/v1alpha1
         kind: BuildSystem
         metadata:
             name: buildsystem
         spec:
           secrets:
             workloadidentity:
               googleprojectid: ${CLUSTER_PROJECT_ID}
               googleserviceaccount: ${CLUSTER_NAME}-sa
           containerRegistry: ${CONTAINER_REGISTRY}
           enabled: true
         EOF

  4. Configure ADX Build for Workload Identity.
         
         gcloud iam service-accounts add-iam-policy-binding \
           --project=${CLUSTER_PROJECT_ID} \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:${CLUSTER_PROJECT_ID}.svc.id.goog[adx-builds-system/controller]" \
           "${GSA_NAME}@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com"

  5. Configure the operator for Kf:
         
         kubectl apply -f "https://storage.googleapis.com/kf-releases/v2.10.0/kfsystem.yaml"

  6. Setup secrets and defaults:
         
         export CONTAINER_REGISTRY=${COMPUTE_REGION}-docker.pkg.dev/${CLUSTER_PROJECT_ID}/${CLUSTER_NAME}
         
         kubectl patch \
         kfsystem kfsystem \
         --type='json' \
         -p="[{'op': 'replace', 'path': '/spec/kf', 'value': {'enabled': true, 'config': {'featureFlags': {'enable_appdevexperience_builds': true}, 'spaceContainerRegistry': '${CONTAINER_REGISTRY}', 'secrets':{'workloadidentity':{'googleserviceaccount':'${CLUSTER_NAME}-sa', 'googleprojectid':'${CLUSTER_PROJECT_ID}'}}}}}]"
         




## Validate installation

**Note:** This command will inspect the cluster to ensure Kf and its dependencies are installed and working. It will run up to 20 times to give the Kubernetes cluster time to reconcile, and should result in a series `PASS` results. If the status for any component results in `FAIL` after the retries, please see the [Kf Troubleshooting](https://docs.cloud.google.com/migrate/kf/docs/2.10/support/troubleshooting) page.
    
    
    kf doctor --retries=20

## Clean up

These steps should remove all the components created in the Create and prepare a new GKE cluster section.

  1. Delete Google Service Account:
         
         gcloud iam service-accounts delete ${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com

  2. Delete IAM policy bindings:
         
         gcloud projects remove-iam-policy-binding ${CLUSTER_PROJECT_ID} \
             --member="serviceAccount:${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
             --role="roles/iam.serviceAccountAdmin"
         gcloud projects remove-iam-policy-binding ${CLUSTER_PROJECT_ID} \
             --member="serviceAccount:${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
             --role="roles/monitoring.metricWriter"

  3. Delete container image repository:
         
         gcloud artifacts repositories delete ${CLUSTER_NAME} \
           --location=${COMPUTE_REGION}

  4. Uninstall Kf:
         
         kubectl patch kfsystem kfsystem \
           --type='json' \
           -p="[{'op': 'replace', 'path': '/spec/kf', 'value': {'enabled': false, }}]"

  5. Delete GKE cluster:
         
         gcloud container clusters delete ${CLUSTER_NAME} --zone ${CLUSTER_LOCATION}




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
