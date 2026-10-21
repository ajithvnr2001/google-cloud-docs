---
url: https://docs.cloud.google.com/binary-authorization/docs/creating-cluster/
title: Create a cluster \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:10.470028+00:00
---

# Create a cluster  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/creating-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Create a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create a cluster in Google Kubernetes Engine (GKE) with Binary Authorization enabled. You perform this step at the command line using `gcloud` commands or in the Google Cloud console. This step is part of [setting up Binary Authorization for GKE](https://docs.cloud.google.com/binary-authorization/docs/setting-up).

## Before you begin

  * [Enable Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enabling).

  * Enable the GKE API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com&redirect=https%3A//cloud.google.com/binary-authorization/docs/creating-cluster)

  * Configure a platform policy using the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console), [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli), or [REST API](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-rest).




## Create a cluster with Binary Authorization enabled (CV monitoring-only)

Binary Authorization works with Autopilot or Standard clusters. To configure monitoring-only evaluation mode, you must specify at least one [check-based platform policy](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#platform-policies).

To create a cluster with Binary Authorization enabled with only CV monitoring, do the following:

###  Console 

The following steps configure a Standard cluster.

  1. In the Google Cloud console, go to the GKE page.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create Cluster**. Enter values for the default fields as described in [Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster).

  3. In the navigation pane, in the **Cluster** section, click **Advanced settings**.

  4. In the **Binary authorization** row, click _edit_ **Edit configuration**.

  5. Select **Enable Binary Authorization**.

  6. Select **Audit-only** , configure [CV check-based platform policies](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#platform-policies) that you want Binary Authorization to evaluate your cluster's images against, and then click **Save**.

  7. Click **Create**.




###  gcloud 

  1. Set your default Google Cloud project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project where you want to create the cluster.

  2. Create a cluster that uses only CV platform policy-based monitoring:

Before using any of the command data below, make the following replacements: 

     * `CLUSTER_NAME`: a cluster name.
     * `LOCATION`: the location—for example, `us-central1` or `asia-south1`.
     * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored.
     * `POLICY_ID`: the policy ID.
     * `CLUSTER_PROJECT_ID`: the cluster project ID.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --binauthz-evaluation-mode=POLICY_BINDINGS \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID \
        --project=CLUSTER_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME `
        --location=LOCATION `
        --binauthz-evaluation-mode=POLICY_BINDINGS `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID `
        --project=CLUSTER_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME ^
        --location=LOCATION ^
        --binauthz-evaluation-mode=POLICY_BINDINGS ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID ^
        --project=CLUSTER_PROJECT_ID




**Important:** The cluster creation process does not check the validity or existence of the provided platform policies. Platform policy validity is checked only during the periodic monitoring cycles. Take extra caution in ensuring platform policies exist, are formatted appropriately, and have no typographical errors prior to cluster creation. 

It can take a few minutes for your cluster to be created.

## Create a cluster with Binary Authorization enabled (enforce-only)

Binary Authorization works with Autopilot or Standard clusters. The enforcement policy is set to the [project policy](https://docs.cloud.google.com/binary-authorization/docs/configure-policy-gke#default_policy) which by default allows all images. To change the project policy follow [these instructions](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli).

To create a cluster with Binary Authorization enabled with only enforcement enabled, do the following:

###  Console 

The following steps configure a Standard cluster.

  1. In the Google Cloud console, go to the GKE page.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create Cluster**. Enter values for the default fields as described in [Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster).

  3. In the navigation pane, in the **Cluster** section, click **Advanced settings**.

  4. In the **Binary authorization** row, click _edit_ **Edit configuration**.

  5. Select **Enable Binary Authorization**.

  6. Select **Enforce-only** , and then click **Save**.

  7. Click **Create**.




###  gcloud 

  1. Set your default Google Cloud project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project where you want to create the cluster.

  2. Create a cluster that uses policy enforcement only:

Before using any of the command data below, make the following replacements: 

     * `CLUSTER_NAME`: a cluster name.
     * `LOCATION`: the location—for example, `us-central1` or `asia-south1`.
     * `CLUSTER_PROJECT_ID`: the cluster project ID.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE \
        --project=CLUSTER_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME `
        --location=LOCATION `
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE `
        --project=CLUSTER_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME ^
        --location=LOCATION ^
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE ^
        --project=CLUSTER_PROJECT_ID




###  Terraform 

The following Terraform example creates and configures a Standard cluster:
    
    
    resource "google_container_cluster" "default" {
      name               = "gke-standard-regional-binauthz-enforce"
      location           = "us-west1"
      initial_node_count = 1
    
      binary_authorization {
        evaluation_mode = "PROJECT_SINGLETON_POLICY_ENFORCE"
      }
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

It can take a few minutes for your cluster to be created.

## Create a cluster with Binary Authorization enabled (CV monitor and enforce)

Binary Authorization works with Autopilot or Standard clusters.

For enforcement, the policy is set to the [project policy](https://docs.cloud.google.com/binary-authorization/docs/configure-policy-gke#default_policy) which by default allows all images. To change the project policy follow [these instructions](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli).

For CV monitoring, you must specify at least one [CV check-based platform policy](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#platform-policies).

To create a cluster with Binary Authorization enabled with both CV monitoring and enforcement, do the following:

###  Console 

The following steps configure a Standard cluster.

  1. In the Google Cloud console, go to the GKE page.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create Cluster**. Enter values for the default fields as described in [Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster).

  3. In the navigation pane, in the **Cluster** section, click **Advanced settings**.

  4. In the **Binary authorization** row, click _edit_ **Edit configuration**.

  5. Select **Enable Binary Authorization**.

  6. Select **Audit and Enforce** , configure [CV check-based platform policies](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#checks), and then click **Save**.

  7. Click **Create**.




###  gcloud 

  1. Set your default Google Cloud project:
         
         gcloud config set project PROJECT_ID
         

Replace PROJECT_ID with the ID of the project where you want to create the cluster.

  2. Create a cluster that uses both project-singleton policy enforcement and CV platform policy-based monitoring:

Before using any of the command data below, make the following replacements: 

     * `CLUSTER_NAME`: a cluster name.
     * `LOCATION`: the location—for example, `us-central1` or `asia-south1`.
     * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored.
     * `POLICY_ID`: the policy ID.
     * `CLUSTER_PROJECT_ID`: the cluster project ID.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID \
        --project=CLUSTER_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME `
        --location=LOCATION `
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID `
        --project=CLUSTER_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME ^
        --location=LOCATION ^
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID ^
        --project=CLUSTER_PROJECT_ID




**Important:** The cluster creation process does not check the validity or existence of the provided platform policies. Platform policy validity is checked only during periodic CV monitoring cycles. Take extra caution in ensuring that platform policies exist, are formatted appropriately, and have no typographical errors prior to cluster creation. 

It can take a few minutes for your cluster to be created.

## Create a CV cluster that uses multiple platform policies (CV monitoring only)

Binary Authorization works with Autopilot or Standard clusters.

You can create clusters with multiple platform policies bound to them (see [GKE API Reference](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#binaryauthorization) for more information).

###  Console 

The following steps configure a Standard cluster.

  1. In the Google Cloud console, go to the GKE page.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create Cluster**. Enter values for the default fields as described in [Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster).

  3. In the navigation pane, in the **Cluster** section, click **Advanced settings**.

  4. In the **Binary authorization** row, click _edit_ **Edit configuration**.

  5. Select **Enable Binary Authorization**.

  6. Select [**Audit-only**](https://docs.cloud.google.com/binary-authorization/docs/configure-policy-bindings#configuring_an_audit-only_evaluation_mode), configure one or more platform policies that you want Binary Authorization to evaluate your cluster against, and then click **Save**.

  7. Click **Create**.




###  gcloud 

  1. Set your default Google Cloud project:
         
         gcloud config set project PROJECT_ID
         

  2. Create the cluster.

Before using any of the command data below, make the following replacements: 

     * `CLUSTER_NAME`: a cluster name.
     * `LOCATION`: the location — for example, `us-central1` or `asia-south1`.
     * `POLICY_PROJECT_ID_1`: the ID of the project where the first platform policy is stored.
     * `POLICY_ID_1`: the policy ID of the first platform policy.
     * `POLICY_PROJECT_ID_2`: the ID of the project where the second platform policy is stored. Multiple policies can be stored in the same project or in different projects.
     * `POLICY_ID_2`: the policy ID of the second platform policy.
     * `CLUSTER_PROJECT_ID`: the cluster project ID.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --binauthz-evaluation-mode=POLICY_BINDINGS \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_1/platforms/gke/policies/POLICY_ID_1 \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_2/platforms/gke/policies/POLICY_ID_2 \
        --project=CLUSTER_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME `
        --location=LOCATION `
        --binauthz-evaluation-mode=POLICY_BINDINGS `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_1/platforms/gke/policies/POLICY_ID_1 `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_2/platforms/gke/policies/POLICY_ID_2 `
        --project=CLUSTER_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME ^
        --location=LOCATION ^
        --binauthz-evaluation-mode=POLICY_BINDINGS ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_1/platforms/gke/policies/POLICY_ID_1 ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_2/platforms/gke/policies/POLICY_ID_2 ^
        --project=CLUSTER_PROJECT_ID




**Important:** The cluster creation process does not check the validity or existence of the provided platform policies. Platform policy validity is checked only during periodic CV monitoring cycles. Take extra caution in ensuring that platform policies exist, are formatted appropriately, and have no typographical errors prior to cluster creation. 

It can take a few minutes for your cluster to be created.

## Create a CV cluster that uses multiple platform policies (CV monitor and enforce)

Binary Authorization works with Autopilot or Standard clusters.

You can create clusters with multiple platform policies bound to them (see [GKE API Reference](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#binaryauthorization) for more information).

###  Console 

The following steps configure a Standard cluster.

  1. In the Google Cloud console, go to the GKE page.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create Cluster**. Enter values for the default fields as described in [Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster).

  3. In the navigation pane, in the **Cluster** section, click **Advanced settings**.

  4. In the **Binary authorization** row, click _edit_ **Edit configuration**.

  5. Select **Enable Binary Authorization**.

  6. Select **Audit and Enforce** , configure CV monitoring policies, and then click **Save**.

  7. Click **Create**.




###  gcloud 

  1. Set your default Google Cloud project:
         
         gcloud config set project PROJECT_ID
         

  2. Create a cluster that uses both project-singleton policy enforcement and CV platform policy-based monitoring:

Before using any of the command data below, make the following replacements: 

     * `CLUSTER_NAME`: a cluster name.
     * `LOCATION`: the location — for example, `us-central1` or `asia-south1`.
     * `POLICY_PROJECT_ID_1`: the ID of the project where the first platform policy is stored.
     * `POLICY_ID_1`: the policy ID of the first platform policy.
     * `POLICY_PROJECT_ID_2`: the ID of the project where the second platform policy is stored. Multiple policies can be stored in the same project or in different projects.
     * `POLICY_ID_2`: the policy ID of the second platform policy.
     * `CLUSTER_PROJECT_ID`: the cluster project ID.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_1/platforms/gke/policies/POLICY_ID_1 \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_2/platforms/gke/policies/POLICY_ID_2 \
        --project=CLUSTER_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME `
        --location=LOCATION `
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_1/platforms/gke/policies/POLICY_ID_1 `
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_2/platforms/gke/policies/POLICY_ID_2 `
        --project=CLUSTER_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container clusters create CLUSTER_NAME ^
        --location=LOCATION ^
        --binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_1/platforms/gke/policies/POLICY_ID_1 ^
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID_2/platforms/gke/policies/POLICY_ID_2 ^
        --project=CLUSTER_PROJECT_ID




**Important:** The cluster creation process does not check the validity or existence of the provided platform policies. Platform policy validity is checked only during periodic CV monitoring cycles. Take extra caution in ensuring that platform policies exist, are formatted appropriately, and have no typographical errors prior to cluster creation. 

It can take a few minutes for your cluster to be created.

## Verify that Binary Authorization is enabled

To verify that Binary Authorization is enabled for the cluster, do the following:

###  Console 

  1. Open the GKE page in the Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Under **Kubernetes clusters** , find your cluster.

  3. Under **Security** , verify that **Binary Authorization** is set to **Enabled**.




###  gcloud 

To list the policy bindings for your cluster, do the following: 
    
    
    gcloud beta container clusters describe CLUSTER_NAME --location LOCATION --project CLUSTER_PROJECT_ID | grep -A 10 policyBindings:
    

Note that there may be additional information after the policy binding listing.

## What's next

  * [Learn more about Binary Authorization Continuous Validation](https://docs.cloud.google.com/binary-authorization/docs/overview-cv) ([Preview](https://cloud.google.com/products#product-launch-stages)).
  * [Learn more about Binary Authorization enforcement](https://docs.cloud.google.com/binary-authorization/docs/overview#what-does-binauthz-do).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
