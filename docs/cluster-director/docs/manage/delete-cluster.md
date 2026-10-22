---
url: https://docs.cloud.google.com/cluster-director/docs/manage/delete-cluster/
title: Delete a cluster \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:06.045294+00:00
---

# Delete a cluster  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/manage/delete-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Delete a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to delete a cluster in Cluster Director.

When you no longer need a cluster and its associated resources, you can permanently delete it to save costs and free up resources. Deleting a cluster is an irreversible action that also deletes all of its Compute Engine instances and Slurm configuration.

**Warning:** When you delete a cluster, you also delete any network or storage resources that Cluster Director created for it. To avoid data loss and retain these resources, back them up before you delete the cluster. If you specified existing network or storage resources when creating the cluster, then deleting the cluster doesn't impact those resources.

## Before you begin

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

### Required roles

To get the permission that you need to delete clusters, ask your administrator to grant you the [Cluster Director Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `hypercomputecluster.clusters.delete` permission, which is required to delete clusters. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Delete a cluster

To delete a cluster in your project, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/cluster-director/clusters/list)

  2. In the **Clusters** table, in the **Name** column, click the name of the cluster that you want to delete. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  3. Click delete **Delete**.

  4. In the dialog that appears, enter the name of your cluster, and then click **Delete** to confirm.

The **Clusters** page appears. Deleting your cluster can take some time to complete.




###  gcloud 

To delete a cluster, use the [`gcloud alpha cluster-director clusters delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cluster-director/clusters/delete).

To run the command, select one of the following options:

###  Bash 
    
    
    gcloud alpha cluster-director clusters delete CLUSTER_NAME \
        --location=REGION
    

###  Powershell 
    
    
    gcloud alpha cluster-director clusters delete CLUSTER_NAME `
        --location=REGION
    

###  cmd.exe 
    
    
    gcloud alpha cluster-director clusters delete CLUSTER_NAME ^
        --location=REGION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster that you want to delete.

  * `REGION`: the region where your cluster exists.




The output is similar to the following:
    
    
    Delete request issued for: [cluster000]
    Waiting for operation [projects/example-project/locations/us-central1/operations/operation-1759334170069-6401ae83f88df-342228e4-42174ca2] to complete...working...
    

Deleting your cluster can take some time to complete. When it does complete, the output is similar to the following:
    
    
    Deleted cluster [cluster000].
    

###  REST 

To delete a cluster, make a `DELETE` request to the [`clusters.delete` method](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/delete).

Your request must include the following HTTP method and request URL:
    
    
    DELETE https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.

  * `REGION`: the region where your cluster exists.

  * `CLUSTER_NAME`: the name of the cluster that you want to delete.




To send your request, select one of the following options:

###  curl (Bash) 
    
    
    curl -X DELETE \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME"
    

###  Powershell 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
        -Method DELETE `
        -Headers $headers `
        -Uri "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME" | Select-Object -Expand Content
    

###  curl (cmd.exe) 
    
    
    curl -X DELETE ^
         -H "Authorization: Bearer $(gcloud auth print-access-token)" ^
         "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME"
    

The response is similar to the following:
    
    
    {
      "name": "projects/example-project/locations/us-central1/operations/operation-1758790097068-63f9c3af860a4-1f0c5497-8b116854",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.hypercomputecluster.v1.OperationMetadata",
        "createTime": "2025-09-25T08:48:17.077238445Z",
        "target": "projects/example-project/locations/us-central1/clusters/clusterfpv",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Deleting your cluster can take some time to complete.

## What's next

  * Create a new cluster:

    * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

    * [Create a custom cluster from scratch](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)

  * [View audit logs](https://docs.cloud.google.com/cluster-director/docs/monitor/view-audit-logs)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
