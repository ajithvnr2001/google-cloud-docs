---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/command-line-tools/
title: Setting up the command-line environment \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:01.710124+00:00
---

# Setting up the command-line environment  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/command-line-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Setting up the command-line environment Stay organized with collections  Save and categorize content based on your preferences. 

Configure the command-line tools to connect to and interact with Knative serving. These steps assume you are using a Mac or Linux operating system. If you are using Microsoft Windows, you need to adjust the commands. 

Although you can choose to use the [Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/console) to manage Knative serving, there are some tasks that require the command-line tools.

To install and configure the command-line tools for Knative serving:

  1. [Install and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  2. Configure the Google Cloud CLI [defaults](https://docs.cloud.google.com/sdk/gcloud/reference/config#run):

     1. Set your default Google Cloud project:
            
            gcloud config set project PROJECT_ID
            

Replace PROJECT_ID with the ID of your Google Cloud project.

     2. Set the [target platform](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--platform):
            
            gcloud config set run/platform gke
            

     3. Set the location of your cluster:
            
            gcloud config set run/cluster_location ZONE_REGION
            

Replace ZONE_REGION with the [zone or region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of your cluster.

     4. If you created and use a new namespace other than the `default` namespace, you can set that namespace as the default in Google Cloud CLI so that it's used each time you run a command:
            
            gcloud config set run/namespace NAMESPACE
            

Replace NAMESPACE with the name of the namespace that you want the gcloud CLI tool to use by default.

  3. Install the `kubectl` command-line tool:
         
         gcloud components install kubectl
         

  4. Optional: Ensure that all previously installed components are up-to-date:
         
         gcloud components update
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
