---
url: https://docs.cloud.google.com/migrate/kf/docs/2.7/outside-gcp-install/
title: Install Kf outside Google Cloud \u00a0|\u00a0 Kf 2.7 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:54.823118+00:00
---

# Install Kf outside Google Cloud  |  Kf 2.7  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.7/outside-gcp-install/

Version 2.7

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
  * [ 2.7 ](https://docs.cloud.google.com/migrate/kf/docs/2.7)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.7/getting-started)



Send feedback 

#  Install Kf outside Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to install Kf and its dependencies on either a [Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview) or [Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/concepts/about-bare-metal) on-premises cluster.

If you are already familiar with the process of installing Kf on a GKE cluster in Google Cloud, the main differences for the on-premises procedure are:

  * You do not have to install the Config Connector for an on-premises install.
  * The on-premises procedure uses Docker credentials instead of Workload Identity.



## Before you begin

### GKE Enterprise requirements

  * A user cluster that meets [Cloud Service Mesh requirements](https://docs.cloud.google.com/service-mesh/docs/unified-install/prerequisites).

  * Configured for logging and monitoring.

    * [Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/logging-and-monitoring).
    * [Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/log-monitoring).
  * Registered in your GKE Enterprise fleet:

[Go to GKE Enterprise clusters](https://console.cloud.google.com/anthos/clusters)

Learn how to [register a cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster).




### Kf requirements

Review and understand the access permissions of components in Kf in the [Kf dependencies and architecture page](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/kf-dependencies).

  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/install).

  * [Tekton](https://github.com/tektoncd/pipeline) for use by Kf. This is not a user facing service.

  * A dedicated Google Service Account.




## Prepare a new GKE Enterprise cluster and related services

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
    export CLUSTER_PROJECT_ID=YOUR_PROJECT_ID
    export CLUSTER_NAME=kf-cluster
    export DOCKER_SERVER=YOUR_DOCKER_SERVER_URL
    export SA_NAME=${CLUSTER_NAME}-sa
    export SA_EMAIL=${SA_NAME}@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com

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
    Set-Variable -Name CLUSTER_PROJECT_ID -Value YOUR_PROJECT_ID
    Set-Variable -Name CLUSTER_NAME -Value kf-cluster
    Set-Variable -Name DOCKER_SERVER -Value YOUR_DOCKER_SERVER_URL
    Set-Variable -Name SA_NAME -Value ${CLUSTER_NAME}-sa
    Set-Variable -Name SA_EMAIL -Value ${SA_NAME}@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com

### Set up service account

Create the Google Cloud service account (GSA) and service account key used for the builds to read/write from Container Registry. This step is different if you are using a different container registry because it could have a different way of obtaining the credentials to access the registry.

  1. Create the service account used by Kf:
         
         gcloud beta iam service-accounts create ${SA_NAME} \
             --project=${CLUSTER_PROJECT_ID} \
             --description="gcr.io admin for ${CLUSTER_NAME}" \
             --display-name="${CLUSTER_NAME}"

  2. Assign the service account the `storage.admin` role required to read/write from the Container Registry:
         
         gcloud projects add-iam-policy-binding ${CLUSTER_PROJECT_ID} \
             --member="serviceAccount:${SA_NAME}@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
             --role="roles/storage.admin"

  3. Create the service account key:
         
         temp_dir=$(mktemp -d)
         key_path=${temp_dir}/key.json
         gcloud iam service-accounts keys create --iam-account ${SA_EMAIL} ${key_path}
         key_json=$(cat ${key_path})
         rm -rf ${temp_dir}




## Install software dependencies on cluster

  1. Install Cloud Service Mesh v1.12.

     1. Follow the [Cloud Service Mesh install guide](https://docs.cloud.google.com/service-mesh/v1.11/docs/unified-install/install).

     2. After installing Cloud Service Mesh, you must create an ingress gateway using the [gateway install guide](https://docs.cloud.google.com/service-mesh/v1.11/docs/unified-install/install#install_gateways).

     3. If on Google Distributed Cloud, set the `loadBalancerIP` to an IP allocated to the cluster as described in [Configure external IP addresses for Google Distributed Cloud](https://docs.cloud.google.com/service-mesh/v1.11/docs/unified-install/external-ip-load-balance).

  2. Install Tekton:
         
         kubectl apply -f "https://storage.googleapis.com/tekton-releases/pipeline/previous/v0.29.0/release.yaml"




## Install Kf

  1. Install the Kf CLI:

### Linux

This command installs the Kf CLI for all users on the system. Follow the instructions in the Cloud Shell tab to install it just for yourself.
         
         gcloud storage cp gs://kf-releases/v2.7.3/kf-linux /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Mac

This command installs `kf` for all users on the system.
         
         gcloud storage cp gs://kf-releases/v2.7.3/kf-darwin /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Cloud Shell

This command installs `kf` on your Cloud Shell instance if you use `bash`, the instructions may need to be modified for other shells.
         
         mkdir -p ~/bin
         gcloud storage cp gs://kf-releases/v2.7.3/kf-linux ~/bin/kf
         chmod a+x ~/bin/kf
         echo "export PATH=$HOME/bin:$PATH" >> ~/.bashrc
         source ~/.bashrc

### Windows

This command downloads `kf` to current directory. Add it to the path if you want to call if from anywhere other than the current directory.
         
         gcloud storage cp gs://kf-releases/v2.7.3/kf-windows.exe kf.exe

  2. Install the operator:
         
         kubectl apply -f "https://storage.googleapis.com/kf-releases/v2.7.3/operator.yaml"

  3. Configure the operator for Kf:
         
         kubectl apply -f "https://storage.googleapis.com/kf-releases/v2.7.3/kfsystem.yaml"




## Create a Kubernetes secret for Docker credentials

Create a Kubernetes secret in the Kf namespace for Docker credentials you created above in Service account setup. Then patch the Kubernetes secret to the `subresource-apiserver` deployment for source uploads.

  1. Enable and update the Kf operator to use Container Registry as the container registry.

**Note:** The command below uses the following Container Registry as the container registry: `gcr.io/${CLUSTER_PROJECT_ID}`. Alternatively, you can use your own custom container registry. Modify this command as necessary if you use a custom container registry.
         
         export CONTAINER_REGISTRY=gcr.io/${CLUSTER_PROJECT_ID}
         kubectl patch kfsystem kfsystem \
           --type='json' \
           -p="[{'op': 'replace', 'path': '/spec/kf', 'value': {'enabled': true, 'config': {'spaceContainerRegistry':'${CONTAINER_REGISTRY}'}}}]"
         

  2. Verify the `kf` namespace has been created by the Kf operator. This might take a few minutes to complete.
         
         kubectl get namespace kf

  3. Create a Kubernetes secret for use with Docker registries.
         
         export secret_name=kf-gcr-key-${RANDOM}
         kubectl -n kf create secret docker-registry ${secret_name} \
            --docker-username=_json_key --docker-server ${DOCKER_SERVER} \
            --docker-password="${key_json}"
         

  4. Update the Kf operator to specify the secret containing Docker credentials.
         
         kubectl patch kfsystem kfsystem \
           --type='json' \
           -p="[{'op': 'replace', 'path': '/spec/kf', 'value': {'config': {'secrets':{'build':{'imagePushSecrets':'${secret_name}'}}}}}]"
         




## Validate installation
    
    
    kf doctor --retries=20

**Note:** This command will inspect the cluster to ensure Kf and its dependencies are installed and working. It will run up to 20 times to give the Kubernetes cluster time to reconcile, and should result in a series `PASS` results. If the status for any component results in `FAIL` after the retries, please see the [Kf Troubleshooting](https://docs.cloud.google.com/migrate/kf/docs/2.7/support/troubleshooting) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
