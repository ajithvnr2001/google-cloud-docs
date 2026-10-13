---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools/
title: Install dependent tools and verify cluster \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:35.989728+00:00
---

# Install dependent tools and verify cluster  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools/

You are viewing archived v1.22 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Install dependent tools and verify cluster

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This page shows you how to prepare your environment and cluster to install in-cluster Cloud Service Mesh for Kubernetes workloads off Google Cloud.

## Install required tools

You can run `asmcli` on [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell) or on your local machine running Linux. Cloud Shell pre-installs all the required tools.

**Note:** macOS isn't supported.

If you are running `asmcli` locally, make sure you have the following tools installed:

  * The [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install)
  * The standard command-line tools: `awk`, `curl`, `grep`, `sed`, and `tr`
  * [`git`](https://git-scm.com/downloads)
  * [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
  * [`jq`](https://stedolan.github.io/jq/)
  * (Optional, in order to test connectivity) netcat (`nc`)



### Configure gcloud

Do the following steps even if you are using Cloud Shell.

  1. Authenticate with the Google Cloud CLI:
         
         gcloud auth login --project PROJECT_ID
         

  2. Update the components:
         
         gcloud components update
         




### Set the current context to your user cluster:

Set your `kubectl` context to point to your off-Google Cloud cluster, according to platform-specific instructions.

**Note:** You can also use service account impersonation by configuring your `gcloud config` before running the tool. Run the command `gcloud config set auth/impersonate_service_account` SA-NAME`@`GCP-PROJECT`.iam.gserviceaccount.com`. To unset the impersonation after you've installed Cloud Service Mesh, run `gcloud config unset auth/impersonate_service_account`. For more information, see [gcloud config](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).

## Download asmcli

This section describes how to download the `asmcli`.

  1. Download the version that installs Cloud Service Mesh 1.22.8 to the current working directory:
         
         curl https://storage.googleapis.com/csm-artifacts/asm/asmcli_1.22 > asmcli
         

**Note:** We recommend that you always download the latest version of `asmcli` when installing Cloud Service Mesh. The command in the previous step downloads the latest version.

Expected output:
         
         % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                      Dload  Upload   Total   Spent    Left  Speed
         100  167k  100  167k    0     0   701k      0 --:--:-- --:--:-- --:--:--  701k
         

  2. Make the script executable:
         
         chmod +x asmcli
         




## Grant cluster admin permissions

  1. Ensure you have set the context to your user cluster:

**Note:** To check existing contexts, run `kubectl config get-contexts`.
         
         kubectl config use-context CONTEXT

  2. Grant cluster admin permissions to your user account (your Google Cloud login email address). You need these permissions to create the necessary [role based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) rules for Cloud Service Mesh:
         
         kubectl create clusterrolebinding cluster-admin-binding \
           --clusterrole=cluster-admin \
           --user=USER_ACCOUNT




## Validate project and cluster

You can run `asmcli validate` to make sure that your project and cluster are setup as required to install Cloud Service Mesh. With this option, `asmcli` doesn't make any changes to your project or cluster, and it doesn't install Cloud Service Mesh.

`asmcli` validates that:

  * Your environment has the required tools.

  * The cluster meets the [minimum requirements](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/cloud-service-mesh-prerequisites#cluster_requirements).

  * You have the [required permissions](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh#roles-required) on the specified project.

  * The project has all the [required Google APIs](https://docs.cloud.google.com/service-mesh/v1.22/docs/project-cluster-setup#set_up_your_project) enabled.




By default, `asmcli` downloads and extracts the installation file and downloads the [`asm`](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/release-1.22/asm/) configuration package from GitHub to a temp directory. Before exiting, `asmcli` outputs a message that provides the name of the temp directory. We recommend that you specify a directory for the downloads with the `--output_dir DIR_PATH` option. The `--output_dir` option makes it convenient for you to use the `istioctl` command-line tool. You might need `istioctl` for [troubleshooting configuration issues](https://docs.cloud.google.com/service-mesh/v1.22/docs/troubleshooting/troubleshoot-intro#use_automated_validation_tools). Additionally, the configuration files to enable optional features using `asmcli` are included in the `asm/istio/options` directory.

Run the following command to validate your configuration and download the installation file and `asm` package to the `OUTPUT_DIR` directory.

Use the following command to run `asmcli validate` on the following platforms: Google Distributed Cloud (software only) for VMware, Google Distributed Cloud (software only) for bare metal, GKE on AWS, GKE on Azure, Amazon EKS, and Microsoft AKS.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run the following command to validate your configuration and download the installation file and `asm` package to the `OUTPUT_DIR` directory:
         
         ./asmcli validate \
            --kubeconfig KUBECONFIG_FILE \
            --fleet_id FLEET_PROJECT_ID \
            --output_dir DIR_PATH \
            --platform multicloud
         

     * `--kubeconfig` The path to the [`kubeconfig`](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.

     * `--fleet_id` The project ID of the [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project). `asmcli validate` checks that the cluster is registered to the specified fleet.

     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `asm` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.

     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud.




On success, `asmcli` outputs the following:
    
    
    asmcli: Setting up necessary files...
    asmcli: Using asm_kubeconfig as the kubeconfig...
    asmcli: Checking installation tool dependencies...
    asmcli: Fetching/writing GCP credentials to kubeconfig file...
    asmcli: Verifying connectivity (10s)...
    asmcli: kubeconfig set to asm_kubeconfig
    asmcli: using context gke_example-project-12345_us-central1_cluster-2
    asmcli: Getting account information...
    asmcli: Downloading ASM..
    asmcli: Downloading ASM kpt package...
    fetching package "/asm" from "https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages" to "asm"
    asmcli: Checking required APIs...
    asmcli: Checking for project example-project-12345...
    asmcli: Reading labels for us-central1/cluster-2...
    asmcli: Checking for istio-system namespace...
    asmcli: Confirming node pool requirements for example-project-12345/us-central1/cluster-2...
    asmcli: Checking Istio installations...
    asmcli: [WARNING]: There is no way to validate that the meshconfig API has been initialized.
    asmcli: [WARNING]: This needs to happen once per GCP project. If the API has not been initialized
    asmcli: [WARNING]: for example-project-12345, please re-run this tool with the --enable_gcp_components
    asmcli: [WARNING]: flag. Otherwise, installation will succeed but Anthos Service Mesh
    asmcli: [WARNING]: will not function correctly.
    asmcli: Successfully validated all requirements to install ASM.

If one of the tests fails the validation, `asmcli` outputs an error message. For example, if your project doesn't have all of the required Google APIs enabled, you see the following error:
    
    
    ERROR: One or more APIs are not enabled. Please enable them and retry, or run
    `asmcli` with the '--enable_gcp_apis' flag to allow `asmcli` to enable them
    on your behalf.

If you got an error message about needing to run `asmcli` with an [enablement flag](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement-flags), you have the following options:

  * Include the specific flag from the error message or the `--enable_all` flag when running `asmcli` to do the actual installation.

  * If you prefer, you can update your project and cluster yourself before running `asmcli` as described in [Set up your project and GKE cluster yourself](https://docs.cloud.google.com/service-mesh/v1.22/docs/project-cluster-setup#set_up_your_project).




Note that `asmcli validate` doesn't allow any enablement flags because it only validates that your project and cluster are ready for installation.

### Inspect cluster install and upgrade requirements

Before upgrading you should check that your configuration is compatible with the new version of Cloud Service Mesh.

  1. Change to the directory that you specified in `--output_dir`.

  2. Run the following command to inspect the Kubernetes cluster for install and upgrade requirements. Make sure you use the version of `istioctl` distributed with the new Cloud Service Mesh version.
         
         istioctl experimental precheck
         




## What's next?

  * [Install Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh)
  * [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/upgrade)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
