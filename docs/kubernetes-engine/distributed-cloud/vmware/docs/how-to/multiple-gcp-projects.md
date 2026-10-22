---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects/
title: Google Cloud projects for Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:51.641728+00:00
---

# Google Cloud projects for Google Distributed Cloud  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Google Cloud projects for Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to associate one or more Google Cloud projects with a cluster in Google Distributed Cloud.

The instructions here are complete. For a shorter introduction to using a Google Cloud project, see [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure).

## Before you begin

[Install Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cloud-sdk).

## Fleet host project

Every admin cluster must be registered to a [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs). And every user cluster managed by an admin cluster must be registered to the same fleet as the admin cluster.

When an admin or user cluster is registered to a fleet, it is associated with a _fleet host project_. An admin cluster and all the user clusters it manages have the same fleet host project. In the Google Cloud console, in the fleet host project, you can see and manage your admin and user clusters.

Choose a Google Cloud project to serve as your fleet host project. You can choose an existing project, or you can create a new one. Make a note of the project ID. You need the ID of your fleet host project in the steps that follow.

### Enable APIs in your fleet host project

In your fleet host project, enable the required APIs:

### Linux and macOS

Enable the following APIs in your fleet host project:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID \
        anthos.googleapis.com \
        container.googleapis.com \
        gkehub.googleapis.com \
        gkeconnect.googleapis.com \
        connectgateway.googleapis.com \
        monitoring.googleapis.com \
        kubernetesmetadata.googleapis.com \
        logging.googleapis.com \
        opsconfigmonitoring.googleapis.com \
        serviceusage.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com
    

If you want to manage the lifecycle of clusters in the Google Cloud console, the Google Cloud CLI, or [Terraform](https://www.terraform.io/), enable these additional APIs in your fleet host project:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID \
        gkeonprem.googleapis.com \
        anthosaudit.googleapis.com \
        storage.googleapis.com
    

### Windows

Enable the following APIs in your fleet host project:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID ^
        anthos.googleapis.com ^
        container.googleapis.com ^
        gkehub.googleapis.com ^
        gkeconnect.googleapis.com ^
        connectgateway.googleapis.com ^
        monitoring.googleapis.com ^
        kubernetesmetadata.googleapis.com ^
        logging.googleapis.com ^
        opsconfigmonitoring.googleapis.com ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com
    

If you want to manage the lifecycle of user clusters in the Google Cloud console, the Google Cloud CLI, or [Terraform](https://www.terraform.io/), enable these additional APIs in your fleet host project:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID ^
        gkeonprem.googleapis.com ^
        anthosaudit.googleapis.com ^
        storage.googleapis.com
    

### Grant roles to service accounts on your fleet host project

Your connect-register service account must be granted certain roles on your fleet host project. For details see [Connect-register service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account).

Your logging-monitoring service account must be granted certain roles on your fleet host project. For details, see [Logging-monitoring service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account).

Your audit logging service account must be granted certain roles on your fleet host project. For details, see [Audit logging service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#audit_logging_service_account).

### Register a cluster to a fleet

You register a cluster to a fleet when you create the cluster. The details of registration depend on what tool you use to create the cluster:

Tool| How to register  
---|---  
`gkectl`| Fill in the [gkeConnect.projectID](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeconnect-projectid-field) field in the cluster configuration file.  
Google Cloud console| The cluster is automatically registered. The Google Cloud project that you use to create the cluster becomes the fleet host project.  
Terraform| Fill in the `project_id` field in the [.tfvars file](https://registry.terraform.io/providers/terraform-redhat/rhcs/latest/docs/guides/terraform-vars).  
gcloud CLI| When you call `gcloud container vmware clusters create`, provide a value for `--project`.  
  
## Parent project of your component access service account

Before you create a cluster, you must have a service account that Google Distributed Cloud can use to download components from Artifact Registry. This service account is called your _component access service account_.

The Google Cloud project where you created your component access service account is called the _parent_ of your component access service account. This project can be the same as your fleet host project, or it can be different. For more information about service accounts and parent projects see [Understanding service accounts and Google Cloud projects](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#service_accounts_and_projects).

To enable the required APIs for the parent project of your component access service account:

### Linux and macOS
    
    
    gcloud services enable --project [PARENT_PROJECT_ID] \
        serviceusage.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com
    

### Windows
    
    
    gcloud services enable --project [PARENT_PROJECT_ID] ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com
    

## What's next

[Create service accounts and keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
