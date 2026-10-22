---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster/
title: Configure a cluster to be managed by the GKE On-Prem API \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:12:38.356752+00:00
---

# Configure a cluster to be managed by the GKE On-Prem API  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure a cluster to be managed by the GKE On-Prem API Stay organized with collections  Save and categorize content based on your preferences. 

The GKE On-Prem API lets you manage on-premises cluster lifecycles by using the Google Cloud console, the Google Cloud CLI, or Terraform. When you create a cluster with these tools, the API stores cluster metadata in your chosen Google Cloud region. If you create clusters with `gkectl`, you must enroll them in the GKE On-Prem API to view details and manage their lifecycles through these interfaces.

Enrolling a cluster is separate from registering it to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs). All Google Distributed Cloud clusters automatically register to a [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project) at creation. In the Google Cloud console, registered clusters managed by the GKE On-Prem API show as **VMware** in the **Type** column, whereas unenrolled clusters appear as **External**.

### View registered clusters

All your fleet clusters are displayed on the [GKE Clusters](https://console.cloud.google.com/kubernetes/list/overview) pages in the console. This both gives you an overview of your entire fleet and, for Google Distributed Cloud, lets you see which clusters are managed by the GKE On-Prem API.

To view your fleet clusters:

  1. In the console, go to the GKE clusters page.  
[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)
  2. Select the Google Cloud project. 
     * If **VMware** is displayed in the **Type** column, the cluster is managed by the GKE On-Prem API. 
     * If **External** is displayed in the **Type** column, the cluster isn't managed by the GKE On-Prem API. 



## Requirements

  * User clusters must be version 1.11 or higher.
  * Admin clusters must be version 1.13 or higher.

  * If you aren't a project owner, minimally, you must be granted the Identity and Access Management role `roles/gkeonprem.admin` on the project. For details on the permissions included in this role, see [GKE on-prem roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem) in the IAM documentation.




## Before you begin

  1. Set up the gcloud CLI, if needed.

     1. If you need to install the gcloud CLI, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/docs/install).

     2. Update the gcloud CLI components, if needed:
            
            gcloud components update
            

  2. Do the following steps to activate and use the GKE On-Prem API:

     1. Enable the API in your project:
            
            gcloud services enable \
                --project PROJECT_ID \
                gkeonprem.googleapis.com
            

Replace `PROJECT_ID` with the project ID of your fleet host project. This is the project ID that was configured in the `gkeconnect` section of your [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeconnect-section) or [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeconnect-section).

If you get a `PERMISSION_DENIED` error, double check the project ID that you entered. If the project ID is correct, run `gcloud auth login` to sign in to the Google Cloud CLI with the account that has access to the project.

     2. If this is the first time that you have enabled the GKE On-Prem API in your project, you need to [initialize the API](https://docs.cloud.google.com/iam/docs/service-agents). You can do this by calling a gcloud CLI command that displays available versions that you can use to create a cluster:
            
            gcloud container vmware clusters query-version-config \
                --project=PROJECT_ID \
                --location=REGION
            

Replace `REGION` with `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api).

  3. If your organization has set up [an allowlist](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules) that lets traffic from Google APIs and other addresses pass through your proxy server, add the following to the allowlist:

     * gkeonprem.googleapis.com
     * gkeonprem.mtls.googleapis.com

These are the service names for the GKE On-Prem API.




## Enroll a user cluster

###  gcloud CLI 

  1. List the fleet memberships of registered clusters:
         
         gcloud container fleet memberships list \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with the project ID of your fleet host project.

Note the region in which the admin cluster that manages the user cluster is a member because you will need this in the next step.

  2. Enroll the cluster in the GKE On-Prem API:
         
         gcloud container vmware clusters enroll USER_CLUSTER_NAME \
             --project=<var>PROJECT_ID</var> \
             --admin-cluster-membership=projects/PROJECT_ID/locations/MEMBERSHIP_REGION/memberships/ADMIN_CLUSTER_NAME \
             --location=REGION
         

Replace the following:

     * `USER_CLUSTER_NAME`: the name of the user cluster that you want to enroll.

     * `PROJECT_ID`: the project ID of your fleet host project.

     * `MEMBERSHIP_REGION`: the region in which the admin cluster that manages the user cluster is a member. This could be `global` or a Google Cloud region.

     * `ADMIN_CLUSTER_NAME`: the name of the admin cluster that manages the user cluster.

The `ADMIN_CLUSTER_NAME`, `MEMBERSHIP_REGION`, and `PROJECT_ID` form the fully-specified cluster name for the `--admin-cluster-membership` flag.

     * `REGION`: the Google Cloud region in which the GKE On-Prem API runs and stores cluster metadata. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). The region can't be changed after the cluster is enrolled.




### `gkectl`

Do the following steps on your admin workstation.

  1. Add the following section to the user cluster configuration file:
         
         gkeOnPremAPI:
           enabled:true
           location:REGION
         

Replace `REGION` with the Google Cloud region in which the GKE On-Prem API runs and stores cluster metadata. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). The region can't be changed after the cluster is enrolled.

  2. Update the cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG_FILE
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

     * `USER_CLUSTER_CONFIG_FILE`: the path of your user cluster configuration file.




## Enroll an admin cluster

###  gcloud CLI 

  1. List the fleet memberships of registered clusters:
         
         gcloud container fleet memberships list \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with the project ID of your fleet host project.

Note the region in which the admin cluster is a member because you will need this in the next step.

  2. Enroll the admin cluster in the GKE On-Prem API:
         
         gcloud container vmware admin-clusters enroll ADMIN_CLUSTER_NAME \
             --project=PROJECT_ID \
             --admin-cluster-membership=projects/PROJECT_ID/locations/MEMBERSHIP_REGION/memberships/ADMIN_CLUSTER_NAME \
             --location=REGION
         




Replace the following:

  * `ADMIN_CLUSTER_NAME`: the name of the admin cluster that you want to enroll.

  * `PROJECT_ID` the project ID of your fleet host project.

  * `MEMBERSHIP_REGION`: the region in which the admin cluster is a member. This could be `global` or a Google Cloud region.

The `ADMIN_CLUSTER_NAME`, `MEMBERSHIP_REGION`, and `PROJECT_ID` form the fully-specified cluster name for the `--admin-cluster-membership` flag.

  * `REGION`: the Google Cloud region in which the GKE On-Prem API runs and stores cluster metadata.. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). We recommend that you use the same region that is configured in `stackdriver.clusterLocation` in the admin cluster configuration file. The region can't be changed after the cluster is enrolled.




### `gkectl`

Do the following steps on your admin workstation.

  1. Add the following section to the admin cluster configuration file:
         
         gkeOnPremAPI:
           enabled:true
           location:REGION
         

Replace `REGION` with the Google Cloud region in which the GKE On-Prem API runs and stores cluster metadata. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). We recommend that you use the same region that is configured in `stackdriver.clusterLocation`. The region can't be changed after the cluster is enrolled.

  2. Update the cluster:
         
         gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG_FILE
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

     * `ADMIN_CLUSTER_CONFIG_FILE`: the path of your admin cluster configuration file.




## Get information about your cluster

After the cluster is enrolled, you can use the following commands to get information about your clusters:

### User cluster

  * To describe a user cluster:


    
    
    gcloud container vmware clusters describe USER_CLUSTER_NAME \
      --project=PROJECT_ID \
      --location=REGION
    

  * To list your user clusters:


    
    
    gcloud container vmware clusters list \
      --project=PROJECT_ID \
      --location=-
    

When you set `--location=-`, that means to list all clusters in all regions. If you need to scope down the list, set `--location` to the region you specified when you enrolled the cluster.

### Admin cluster

  * To describe an admin cluster:


    
    
    gcloud container vmware admin-clusters describe ADMIN_CLUSTER_NAME \
      --project=PROJECT_ID \
      --location=REGION
    

  * To list your admin clusters:


    
    
    gcloud container vmware admin-clusters list \
      --project=PROJECT_ID \
      --location=-
    

When you set `--location=-`, that means to list all clusters in all regions. If you need to scope down the list, set `--location` to the region you specified when you enrolled the cluster.

## Connect to the cluster

After the cluster is enrolled with the GKE On-Prem API, you need to choose and configure an authentication method so that you can manage the cluster from the Google Cloud console. The authentication method that you select also controls access to the cluster from the command line. For more information, see the following:

  * [Manage clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console)
  * [GKE Identity Service ](https://docs.cloud.google.com/anthos/identity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
