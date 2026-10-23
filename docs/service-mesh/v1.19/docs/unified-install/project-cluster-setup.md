---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/project-cluster-setup/
title: Set up your project and GKE cluster yourself \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:30.109586+00:00
---

# Set up your project and GKE cluster yourself  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/project-cluster-setup/

You are viewing archived v1.19 Service Mesh documentation.

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
  * [ v1.19 ](https://docs.cloud.google.com/service-mesh/v1.19/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.19/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up your project and GKE cluster yourself

When you install Cloud Service Mesh using [`asmcli`](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/asmcli-overview), it can configure your project and your GKE on Google Cloud cluster for you if you include the `--enable_all` flag or the more granular [enablement flags](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/reference#enablement_flags). If you prefer to do the setup yourself rather than having `asmcli` make the changes, follow the steps on this page.

If you already have a previous version of Cloud Service Mesh installed, you don't need to make any changes to your project or cluster before using [`asmcli` to upgrade](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/upgrade) to the latest Cloud Service Mesh version.

By default, `asmcli` doesn't install the `istio-ingressgateway`. We recommend that you deploy and manage the control plane and gateways separately. Cloud Service Mesh supports auto-injection for gateway deployments, which makes Cloud Service Mesh upgrades easier. After upgrading Cloud Service Mesh, you restart the gateways just like your services to pick up the new control plane configuration. For more information, see [Installing and upgrading gateways](https://docs.cloud.google.com/service-mesh/v1.19/docs/gateways).

**Warning:** On upgrades, `asmcli` removes the default `istio-ingressgateway` from the `istio-system` namespace. If you need the default `istio-ingressgateway` installed with the in-cluster control plane, include the `--option legacy-default-ingressgateway` argument.

## Before you begin

  * [Review the prerequisites and requirements](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/anthos-service-mesh-prerequisites)
  * [Plan the installation](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/plan-install) or [the upgrade](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/plan-upgrade)
  * [Install the required tools](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools)



## Set up your project

  1. Get the project ID for the project that the cluster was created in.

### gcloud

Run the following command:
         
         gcloud projects list
         

### Console

     1. Go to the [**Dashboard** page](https://console.cloud.google.com/home) in the Google Cloud console.

[ Go to the Dashboard page](https://console.cloud.google.com/home)

     2. Click the drop-down list at the top of the page. In the **Select from** window that appears, select your project.

The project ID is displayed on the project Dashboard **Project info** card.

  2. Create the following environment variables:

     * Set the workload pool using the project ID:
           
           export WORKLOAD_POOL=PROJECT_ID.svc.id.goog
           

     * Set the mesh ID using the project number:
           
           export MESH_ID="proj-PROJECT_NUMBER"
           

  3. Set the required Identity and Access Management (IAM) roles. If you are a _Project Owner_ , you have all the necessary permissions to complete the installation. If you aren't a _Project Owner_ , you need someone who is to grant you the following specific IAM roles. In the following command, replace `PROJECT_ID` with the project ID from the previous step and `GCP_EMAIL_ADDRESS` with the account that you use to sign in to Google Cloud.
         
         ROLES=(
         'roles/servicemanagement.admin' \
         'roles/serviceusage.serviceUsageAdmin' \
         'roles/meshconfig.admin' \
         'roles/compute.admin' \
         'roles/container.admin' \
         'roles/resourcemanager.projectIamAdmin' \
         'roles/iam.serviceAccountAdmin' \
         'roles/iam.serviceAccountKeyAdmin' \
         'roles/gkehub.admin')
         for role in "${ROLES[@]}"
         do
           gcloud projects add-iam-policy-binding PROJECT_ID \
             --member "user:GCP_EMAIL_ADDRESS" \
             --role="$role"
         done
         

If you include the `--enable_all` or `--enable_gcp_iam_roles` flag when you run `asmcli`, it sets the required IAM roles for you.

  4. Enable the required Google APIs:
         
         gcloud services enable \
             --project=PROJECT_ID \
             mesh.googleapis.com
         

In addition to `mesh.googleapis.com`, this command also enables the following APIs:

**Note:** Some required APIs have transitive dependencies on other APIs.

API | Purpose | Can Be Disabled  
---|---|---  
`meshconfig.googleapis.com` | Cloud Service Mesh uses the Mesh Configuration API to relay configuration data from your mesh to Google Cloud. Additionally, enabling the Mesh Configuration API lets access the Cloud Service Mesh pages in the Google Cloud console and to use the Cloud Service Mesh certificate authority. | No  
`meshca.googleapis.com` | Related to Cloud Service Mesh certificate authority used by managed Cloud Service Mesh. | No  
`container.googleapis.com` | Required to create Google Kubernetes Engine (GKE) clusters. | No  
`gkehub.googleapis.com` | Required to manage the mesh as a [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs). | No  
`monitoring.googleapis.com` | Required to capture telemetry for mesh workloads. | No  
`stackdriver.googleapis.com` | Required to use the Services UI. | No  
`opsconfigmonitoring.googleapis.com` | Required to use the Services UI for off-Google Cloud clusters. | No  
`connectgateway.googleapis.com` | Required so that the managed Cloud Service Mesh control plane can access mesh workloads. | Yes*  
`trafficdirector.googleapis.com` | Enables a highly available and scalable managed control plane. | Yes*  
`networkservices.googleapis.com` | Enables a highly available and scalable managed control plane. | Yes*  
`networksecurity.googleapis.com` | Enables a highly available and scalable managed control plane. | Yes*  
**Warning:** Disabling `connectgateway.googleapis.com`, `trafficdirector.googleapis.com`, `networkservices.googleapis.com`, and/or `networksecurity.googleapis.com` causes managed Cloud Service Mesh control plane to stop working. If the fleet does not use managed Cloud Service Mesh on any cluster, then these APIs can be disabled.

Enabling the APIs can take a minute or more to complete. When the APIs are enabled, you see output similar to the following:
         
         Operation "operations/acf.601db672-88e6-4f98-8ceb-aa3b5725533c" finished
         successfully.
         

If you include the `--enable_all` or `--enable_apis` flag when you run `asmcli`, it enables the required APIs for you.




## Set up your cluster

If you include the `--enable_all` flag, or one of the more granular [enablement flags](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/reference#enablement_flags), `asmcli` sets up your cluster for you.

  1. Set the default zone or region for the Google Cloud CLI. If you don't set the default here, be sure to specify either the `--zone` or `--region` option in the `gcloud container clusters` commands on this page.

     * If you have a single-zone cluster, set the default zone:
           
           gcloud config set compute/zone CLUSTER_LOCATION
           

     * If you have a regional cluster, set the default region:
           
           gcloud config set compute/region CLUSTER_LOCATION
           

  2. Enable [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity):
         
         gcloud container clusters update CLUSTER_NAME \
             --project=PROJECT_ID \
             --workload-pool=${WORKLOAD_POOL}
         

Enabling Workload Identity can take up to 10 to 15 minutes.

  3. [Register the cluster to the fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-creation).

  4. Initialize your project to ready it for installation. Among other things, this command creates a service account to let data plane components, such as the sidecar proxy, securely access your project's data and resources. In the following command replace `FLEET_PROJECT_ID` with the [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project):

**Warning:** If your `FLEET_PROJECT_ID` is the same as your `PROJECT_ID`, then remove the `"FLEET_PROJECT_ID.hub.id.goog",` from the following command. Otherwise, you will receive an error code due to `INVALID_ARGUMENT`.
         
         curl --request POST  \
          --header "Authorization: Bearer $(gcloud auth print-access-token)" \
          --header "Content-Type: application/json" \
          --data '{"workloadIdentityPools":["FLEET_PROJECT_ID.hub.id.goog","FLEET_PROJECT_ID.svc.id.goog","PROJECT_ID.svc.id.goog"]}' \
          "https://meshconfig.googleapis.com/v1alpha1/projects/PROJECT_ID:initialize"
         

The command responds with empty curly braces: `{}`

  5. Enable [Cloud Monitoring and Cloud Logging on GKE](https://docs.cloud.google.com/monitoring/kubernetes-engine):
         
         gcloud container clusters update CLUSTER_NAME \
             --project=PROJECT_ID \
             --enable-stackdriver-kubernetes
         




Your project and cluster are now ready for a new installation using `asmcli`.

## What's next

  * [Install dependent tools and validate cluster](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
