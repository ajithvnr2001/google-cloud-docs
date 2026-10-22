---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/deploy-cluster-overview/
title: Deploy a cluster with blueprints \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:59.985620+00:00
---

# Deploy a cluster with blueprints  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/deploy-cluster-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Deploy a cluster with blueprints Stay organized with collections  Save and categorize content based on your preferences. 

Cluster Toolkit is an open-source solution that simplifies deploying high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads on Google Cloud. With customizable blueprints, you can provision infrastructure that aligns with Google Cloud best practices, which helps to ensure an efficient and consistent setup for your compute environments.

The [`gcluster` CLI](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) helps you deploy, review, and monitor these configured infrastructure blueprints. Although you can update some active cluster configurations, making fundamental architectural changes might require redeploying the cluster.

## Before you begin

  1. If you are using a Linux or macOS workstation to deploy your cluster, then follow [install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).
  2. From either your workstation or Cloud Shell, [configure your environment](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  3. Verify that you have created a cluster blueprint or selected one from the [Cluster Toolkit blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog).



## Deploy the cluster

To deploy your cluster using a blueprint, complete the following steps:

  1. Switch to the main Cluster Toolkit working directory:
         
         cd cluster-toolkit
         

  2. Deploy the cluster using the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy):

     * To deploy using command-line variables:
           
           ./gcluster deploy --vars project_id=PROJECT_ID PATH_TO_BLUEPRINT_FILE
           

     * To deploy with a [deployment file](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/cluster-deployment-files):
           
           ./gcluster deploy -d PATH_TO_DEPLOYMENT_FILE PATH_TO_BLUEPRINT_FILE
           

Replace the following:

     * `PROJECT_ID`: The unique identifier for your target Google Cloud project.
     * `PATH_TO_BLUEPRINT_FILE`: The relative or absolute path to your cluster blueprint file.
     * `PATH_TO_DEPLOYMENT_FILE`: The path to your cluster deployment configuration file.
  3. The `gcluster` command reports proposed changes for your cluster. To continue the deployment, accept the proposed changes by pressing `a`, and then pressing `Enter`. Optionally, you can review the proposed changes by pressing `d`, and then pressing `Enter`.
         
         Summary of proposed changes: Plan: 37 to add, 0 to change, 0 to destroy.
         (D)isplay full proposed changes,
         (A)pply proposed changes,
         (S)top and exit,
         (C)ontinue without applying
         Please select an option [d,a,s,c]: a
         

  4. After accepting the changes, `gcluster` runs `terraform apply` automatically. This operation takes approximately five minutes while it displays progress. If the run is successful, the output is similar to the following:
         
         Apply complete! Resources: 37 added, 0 changed, 0 destroyed.
         




## Get command-line help

To view all available flags and commands, run the `--help` flag:
    
    
    ./gcluster --help
    ./gcluster deploy --help
    

## What's next

  * Review [Best practices for HPC workloads](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices).
  * Learn about [GKE deployments in Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview).
  * Learn how to manage active deployments in [Reconfigure a running cluster](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/reconfigure-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
