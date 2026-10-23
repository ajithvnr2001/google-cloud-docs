---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke/
title: Prerequisites for GKE clusters on Google Cloud \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:56.379033+00:00
---

# Prerequisites for GKE clusters on Google Cloud  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Prerequisites for GKE clusters on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

If you're registering a GKE cluster on Google Cloud, you might need to do one or more of the following before registering the cluster, depending on the registration option that you choose. This guide assumes that you've already completed the [general prerequisites](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin) for cluster registration.

## Enable Workload Identity Federation for GKE

We recommend registering your GKE clusters with fleet Workload Identity Federation enabled, which provides a consistent way for applications on the clusters to authenticate to Google Cloud APIs and services. You can find out more about the advantages of enabling fleet Workload Identity Federation in [Use fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity).

To use this feature, you must ensure [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) is enabled on the cluster before registration. Registering a GKE cluster with fleet Workload Identity Federation without having Workload Identity Federation for GKE enabled on the cluster can lead to inconsistencies on how identity is asserted by workloads in the cluster, and is not a supported configuration. Autopilot clusters have Workload Identity Federation for GKE enabled by default.

### gcloud

To check if your cluster has Workload Identity Federation for GKE enabled, run the following command to list the cluster's [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools). If you haven't already specified [a default zone or region for `gcloud`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters#before_you_begin), you need to specify a `--region` or `--zone` flag when running this command.
    
    
    gcloud container clusters describe CLUSTER_NAME --format="value(workloadIdentityConfig.workloadPool)"
    

Replace the following:

  * CLUSTER_NAME: the `name` of the GKE cluster.



If you see a result similar to the following then Workload Identity Federation for GKE is already enabled on your cluster:
    
    
    GKE_PROJECT_ID.svc.id.goog

If there are no results, then Workload Identity Federation for GKE is not enabled. Follow the instructions in [Enabling Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_cluster).

### Console

To check if your cluster has Workload Identity Federation for GKE enabled:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of your cluster.

  3. On the cluster details page, in the **Security** section, confirm that **Workload Identity** is listed as **Enabled**.




If Workload Identity is **Disabled** and you want to enable this feature:

  1. In the cluster details page, click edit **Edit Workload Identity**.
  2. In the **Edit Workload Identity** dialog, select the **Enable Workload Identity** checkbox.
  3. Click **Save changes**.



## Grant permissions for registering a cluster into a different project

Registering a GKE cluster to the fleet in its own project does not require any special permissions beyond those described in [Grant access permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#grant_iam_roles). However, if you want to register a GKE cluster from its own project (GKE_PROJECT) to a fleet in a _different_ project (FLEET_HOST_PROJECT), the FLEET_HOST_PROJECT [service agent account `gcp-sa-gkehub`](https://docs.cloud.google.com/iam/docs/service-agents) must have the [`gkehub.serviceAgent` role](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) in the GKE_PROJECT project. This role grants the service account the permissions to manage cluster resources in that project.

You can check if the fleet host project `gcp-sa-gkehub` service account has the required role in your cluster's project using gcloud CLI or the Google Cloud console, as follows.

### gcloud

Run the following command:
    
    
    gcloud projects get-iam-policy GKE_PROJECT_ID | grep gcp-sa-gkehub
    

where GKE_PROJECT_ID is the ID of your cluster's project.

If the fleet host project `gcp-sa-gkehub` has the required roles in your cluster's project, it should appear in the output in the form `service-[FLEET_HOST-PROJECT-NUMBER]@gcp-sa-gkehub.iam.gserviceaccount.com`. For example:
    
    
    - members:
      - serviceAccount:service-1234567890@gcp-sa-gkehub.iam.gserviceaccount.com
      role: roles/gkehub.serviceAgent
    

### Console

  1. With your cluster's project selected, go to the **IAM & Admin** page in the Google Cloud console.

[Go to the IAM & Admin page](https://console.cloud.google.com/iam-admin)

  2. Select the **Include Google-provided role grants** checkbox to view the complete allow policy, including service agents.




If the fleet host project service account `gcp-sa-gkehub` has the required roles in your cluster's project, it should appear in this list in the form `service-[FLEET_HOST-PROJECT-NUMBER]@gcp-sa-gkehub.iam.gserviceaccount.com`.

If you don't see the service agent listed in the project's IAM allow policy, do the following to update the necessary permissions:

### gcloud

  1. To grant `gcp-sa-gkehub` the `gkehub.serviceAgent` role, first ensure that this service account exists in the fleet host project. If you have registered clusters in this fleet project before, then this service account should exist already. You can check by looking at the IAM allow policy for the fleet host project:
         
         gcloud projects get-iam-policy FLEET_HOST_PROJECT_ID | grep gcp-sa-gkehub
         

  2. If you need to create the `gcp-sa-gkehub` service account, run the following command:
         
         gcloud beta services identity create --service=gkehub.googleapis.com --project=FLEET_HOST_PROJECT_ID
         

This command should output the following:
         
         Service identity created: service-[FLEET_HOST_PROJECT_NUMBER]@gcp-sa-gkehub.iam.gserviceaccount.com
         

  3. Run the following command to grant the service account the `roles/gkehub.serviceAgent` role in both projects and the `roles/gkehub.crossProjectServiceAgent` in the cluster's project:
         
         GKE_PROJECT_ID=GKE_PROJECT_ID
         FLEET_HOST_PROJECT_ID=FLEET_HOST_PROJECT_ID
         FLEET_HOST_PROJECT_NUMBER=$(gcloud projects describe "${FLEET_HOST_PROJECT_ID}" --format "value(projectNumber)")
         gcloud projects add-iam-policy-binding "${FLEET_HOST_PROJECT_ID}" \
           --member "serviceAccount:service-${FLEET_HOST_PROJECT_NUMBER}@gcp-sa-gkehub.iam.gserviceaccount.com" \
           --role roles/gkehub.serviceAgent
         gcloud projects add-iam-policy-binding "${GKE_PROJECT_ID}" \
           --member "serviceAccount:service-${FLEET_HOST_PROJECT_NUMBER}@gcp-sa-gkehub.iam.gserviceaccount.com" \
           --role roles/gkehub.serviceAgent
         gcloud projects add-iam-policy-binding "${GKE_PROJECT_ID}" \
           --member "serviceAccount:service-${FLEET_HOST_PROJECT_NUMBER}@gcp-sa-gkehub.iam.gserviceaccount.com" \
           --role roles/gkehub.crossProjectServiceAgent
         

where:

     * GKE_PROJECT_ID is the Google Cloud project ID of the GKE cluster.
     * FLEET_HOST_PROJECT_ID is the Google Cloud project ID in which you want to register clusters. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  4. To confirm that the role binding is granted, run the following command again:
         
         gcloud projects get-iam-policy GKE_PROJECT_ID
         

If you see the service account name along with the `gkehub.serviceAgent` and `gkehub.crossProjectServiceAgent` role, the role bindings have been granted. For example:
         
         - members:
           - serviceAccount:service-[FLEET_HOST_PROJECT_NUMBER]@gcp-sa-gkehub.iam.gserviceaccount.com
           role: roles/gkehub.serviceAgent
         - members:
           - serviceAccount:service-[FLEET_HOST_PROJECT_NUMBER]@gcp-sa-gkehub.iam.gserviceaccount.com
           role: roles/gkehub.crossProjectServiceAgent
         




## Configure a service account for Terraform

If you want to use [Terraform](https://docs.cloud.google.com/docs/terraform) to register a Google Kubernetes Engine cluster, you need to create a service account that Terraform can use to access the [Fleet API](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#enable_apis) to create a membership.

### gcloud

  1. Create a service account as follows:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME --project=FLEET_HOST_PROJECT_ID
         

  2. Bind the `gkehub.admin` IAM role to the service account so that Terraform can use it with the Fleet API:
         
         FLEET_HOST_PROJECT_ID=FLEET_HOST_PROJECT_ID
         gcloud projects add-iam-policy-binding ${FLEET_HOST_PROJECT_ID} \
            --member="serviceAccount:SERVICE_ACCOUNT_NAME@${FLEET_HOST_PROJECT_ID}.iam.gserviceaccount.com" \
            --role="roles/gkehub.admin"
         

If you want to create a new cluster with Terraform and then register it, you also need to bind `roles/container.admin` role to the service account so that Terraform can use this service account to access the GKE API to create a cluster.
         
         FLEET_HOST_PROJECT_ID=FLEET_HOST_PROJECT_ID
         gcloud projects add-iam-policy-binding ${FLEET_HOST_PROJECT_ID} \
            --member="serviceAccount:SERVICE_ACCOUNT_NAME@${FLEET_HOST_PROJECT_ID}.iam.gserviceaccount.com" \
            --role="roles/container.admin"
         

Replace the following:

     * FLEET_HOST_PROJECT_ID is the Google Cloud project ID in which you want to register clusters. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * SERVICE_ACCOUNT_NAME is the display name that you choose for the [Service Account].
  3. Download the service account's private key JSON file, as described in Create a Google Cloud service account using `gcloud`. You will need this file to [create and register clusters using Terraform](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#register_your_cluster).




## Configure a service account for Config Connector

If you want to use [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) to register a GKE cluster, do the following:

### gcloud

  1. Ensure that you have installed the [Config Connector add-on](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall). You should have a version of Config Connector above 1.47.0.

  2. Follow [the Config Connector instructions](https://cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#identity) to create a service account.

  3. Bind the `gkehub.admin` IAM role to this service account so that your Config Connector can use this service account to access the Fleet API:
         
         FLEET_HOST_PROJECT_ID=FLEET_HOST_PROJECT_ID
         gcloud projects add-iam-policy-binding ${FLEET_HOST_PROJECT_ID} \
            --member="serviceAccount:SERVICE_ACCOUNT_NAME@${FLEET_HOST_PROJECT_ID}.iam.gserviceaccount.com" \
            --role="roles/gkehub.admin"
         

If you want to create a new cluster with Config Connector and then register it, you also need to bind `roles/container.admin` role to the service account so that your Config Connector controller can use this service account to access the GKE API to create a cluster.
         
         FLEET_HOST_PROJECT_ID=FLEET_HOST_PROJECT_ID
         gcloud projects add-iam-policy-binding ${FLEET_HOST_PROJECT_ID} \
            --member="serviceAccount:SERVICE_ACCOUNT_NAME@${FLEET_HOST_PROJECT_ID}.iam.gserviceaccount.com" \
            --role="roles/container.admin"
         

Replace the following:

     * FLEET_HOST_PROJECT_ID is the Google Cloud project ID in which you want to register clusters. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * SERVICE_ACCOUNT_NAME is the display name that you choose for the [Service Account].
  4. Follow [the Config Connector instruction](https://cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#addon-configuring) to configure your Config Connector with this service account.




## What's next?

Follow the instructions to [register a cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
