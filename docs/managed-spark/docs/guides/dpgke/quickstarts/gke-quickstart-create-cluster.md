---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/gke-quickstart-create-cluster/
title: Run a Spark job on Google Kubernetes Engine \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:10.324055+00:00
---

# Run a Spark job on Google Kubernetes Engine  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/gke-quickstart-create-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Run a Spark job on Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create a Managed Service for Apache Spark on GKE virtual cluster, and then run a Spark job on the cluster.

## Overview of options

While Managed Service for Apache Spark on GKE offers powerful control for containerized environments, Google Cloud also provides fully managed and serverless options that can simplify operations and accelerate development. For a comparison of Spark Managed Service for Apache Spark deployment options, see [Decide on the best Spark service](https://docs.cloud.google.com/managed-spark/docs/concepts/compare#spark-decision-guide).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Verify that you have the permissions required to complete this guide. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. Verify that you have the permissions required to complete this guide. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  16. You must have created a standard (not autopilot) Google Kubernetes Engine (GKE) [**zonal**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster) or [**regional**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster) cluster that has [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled on the cluster.

**Performance tip:** Enable [image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) for faster workload initialization.



### Required roles

Certain IAM roles are required to run the examples on this page. Depending on organization policies, these roles may have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#do_you_need_to_grant_roles).

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### User roles

To get the permissions that you need to create a Managed Service for Apache Spark cluster, ask your administrator to grant you the following IAM roles: 

  * [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account



#### Service account role

To ensure that the Compute Engine default service account has the necessary permissions to create a Managed Service for Apache Spark cluster, ask your administrator to grant the [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) IAM role to the Compute Engine default service account on the project. **Important:** You must grant this role to the Compute Engine default service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

## Create a virtual cluster

A Managed Service for Apache Spark on GKE virtual cluster is created as the deployment platform for Managed Service for Apache Spark components. It's a **virtual** resource, and unlike a Managed Service for Apache Spark on Compute Engine cluster, does not include separate Managed Service for Apache Spark master and worker VMs.

  * Managed Service for Apache Spark on GKE creates node pools within a GKE cluster when you create a Managed Service for Apache Spark on GKE virtual cluster.

  * Managed Service for Apache Spark on GKE jobs are run as pods on these node pools. The node pools and scheduling of pods on the node pools are managed by GKE.

  * **Create multiple virtual clusters.** You can create and run multiple virtual clusters on a GKE cluster to obtain improved resource utilization by sharing node pools across the virtual clusters.

    * Each virtual cluster: 
      * is created with separate properties, including Spark engine version and workload identity
      * is isolated within a separate GKE namespace on the GKE cluster

**Note:** Deletion of one or more Managed Service for Apache Spark on GKE clusters does not delete associated node pools. Node pools are deleted when the GKE cluster is deleted (see [Node pool deletion](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-nodepools#node_pool_deletion)).

### Console

Creating a Managed Service for Apache Spark on GKE cluster is not supported in the Google Cloud console. 

### gcloud

Set environment variables, then run the [`gcloud dataproc clusters gke create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create) command locally or in Cloud Shell to create a Managed Service for Apache Spark on GKE cluster.

  1. Set environment variables: 
         
         DP_CLUSTER=Managed Service for Apache Spark on GKE  cluster-name \
           REGION=[region](https://docs.cloud.google.com/compute/docs/regions-zones#available) \
           GKE_CLUSTER=GKE cluster-name \
           BUCKET=Cloud Storage bucket-name \
           DP_POOLNAME=node pool-name
           PHS_CLUSTER=Managed Service for Apache Spark PHS server name
         

Notes: 
     * `DP_CLUSTER`: Set the Managed Service for Apache Spark virtual cluster name, which must start with a lowercase letter, followed by up to 54 lowercase letters, numbers, or hyphens. It and cannot end with a hyphen.
     * `REGION`: The [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) must be the same as the region where the GKE cluster is located.
     * `GKE_CLUSTER`: The name of your existing GKE cluster.
     * `BUCKET`: (Optional) You can specify the name of a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets), which Managed Service for Apache Spark will use to stage artifacts. If you do not specify a bucket, Managed Service for Apache Spark on GKE will create a staging bucket.
     * `DP_POOLNAME`: The name of a [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) to create on the GKE cluster.
     * `PHS_CLUSTER`: (Optional) [Managed Service for Apache Spark PHS Server](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/history-server#set_up_a_persistent_history_server) to use to view Spark job history on active and deleted Managed Service for Apache Spark on GKE clusters. The PHS cluster must be located in the same region as the Managed Service for Apache Spark on GKE virtual cluster.
  2. Run the command: 
         
         gcloud dataproc clusters gke create ${DP_CLUSTER} \
             --region=${REGION} \
             --gke-cluster=${GKE_CLUSTER} \
             --spark-engine-version=latest \
             --staging-bucket=${BUCKET} \
             --pools="name=${DP_POOLNAME},roles=default" \
             --setup-workload-identity \
             --history-server-cluster=${PHS_CLUSTER}
         

Notes: 
     * `--spark-engine-version`: The [Spark image version](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-versions) used on the Managed Service for Apache Spark cluster. You can use an identifier, such as `3`, `3.1`, or `latest`, or you can specify the full subminor version, such as `3.1-dataproc-5`.
     * `--staging-bucket`: Delete this flag to have Managed Service for Apache Spark on GKE create a staging bucket.
     * `--pools`: This flag is used to specify a new or existing node pool that Managed Service for Apache Spark will create or use to perform the workload. List [Managed Service for Apache Spark on GKE node pool settings](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-nodepools#node_pool_settings), separated by commas, for example: 
           
           --pools=name=dp-default,roles=default,machineType=e2-standard-4,min=0,max=10
           

You must specify the node pool `name` and `role`. Other node pool settings are optional. You can use multiple `--pools` flags to specify multiple node pools. At least one node pool must have the `default` role. All node pools must have the same location.
     * `--setup-workload-identity`: This flag enables [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) bindings. These bindings allow the Kubernetes service accounts (KSAs) to act as the default [Managed Service for Apache Spark VM Service Account (Data Plane identity)](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#vm_service_account_data_plane_identity) of the virtual cluster. You need elevated permissions to set workload identity on a Google service account (GSA) (see [Managed Service for Apache Spark on Google Kubernetes Engine IAM Permissions](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-iam#data_plane_identity)). To use your own GSA with your Managed Service for Apache Spark on GKE virtual cluster, see [Custom IAM configuration](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-iam#custom_iam_configuration).



### REST

Complete a [virtualClusterConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#VirtualClusterConfig) as part of an [`cluster.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API request.

Before using any of the request data, make the following replacements: 

  * PROJECT: Google Cloud project ID
  * REGION: Dataproc virtual cluster [region](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) (same region as the existing GKE cluster region)
  * DP_CLUSTER: Dataproc cluster name
  * GKE_CLUSTER: GKE cluster name
  * NODE_POOL: Node pool name
  * PHS_CLUSTER: [Persistent History Server (PHS) cluster name](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/history-server)
  * BUCKET: (Optional) Staging bucket name. Leave this empty to have Managed Service for Apache Spark on GKE create a staging bucket.



HTTP method and URL: 
    
    
    POST https://dataproc.googleapis.com/v1/projects/project-id/regions/region/clusters

Request JSON body: 
    
    
    {
      "clusterName":"DP_CLUSTER",
      "projectId":"PROJECT",
      "virtualClusterConfig":{
        "auxiliaryServicesConfig":{
          "sparkHistoryServerConfig":{
            "dataprocCluster":"projects/PROJECT/regions/REGION/clusters/PHS_CLUSTER"
          }
        },
        "kubernetesClusterConfig":{
          "gkeClusterConfig":{
            "gkeClusterTarget":"projects/PROJECT/locations/REGION/clusters/GKE_CLUSTER",
            "nodePoolTarget":[
              {
    "nodePool":"projects/PROJECT/locations/REGION/clusters/GKE_CLUSTER/nodePools/NODE_POOL",
                "roles":[
                  "DEFAULT"
                ]
              }
            ]
          },
          "kubernetesSoftwareConfig":{
            "componentVersion":{
              "SPARK":"latest"
            }
          }
        },
        "stagingBucket":"BUCKET"
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataproc.googleapis.com/v1/projects/project-id/regions/region/clusters"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataproc.googleapis.com/v1/projects/project-id/regions/region/clusters" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "projectId":"PROJECT",
      "clusterName":"DP_CLUSTER",
      "status":{
        "state":"RUNNING",
        "stateStartTime":"2022-04-01T19:16:39.865716Z"
      },
      "clusterUuid":"98060b77-...",
      "statusHistory":[
        {
          "state":"CREATING",
          "stateStartTime":"2022-04-01T19:14:27.340544Z"
        }
      ],
      "labels":{
        "goog-dataproc-cluster-name":"DP_CLUSTER",
        "goog-dataproc-cluster-uuid":"98060b77-...",
        "goog-dataproc-location":"REGION",
        "goog-dataproc-environment":"prod"
      },
      "virtualClusterConfig":{
        "stagingBucket":"BUCKET",
        "kubernetesClusterConfig":{
          "kubernetesNamespace":"dp-cluster",
          "gkeClusterConfig":{
    "gkeClusterTarget":"projects/PROJECT/locations/REGION/clusters/GKE_CLUSTER",
            "nodePoolTarget":[
              {
    "nodePool":"projects/PROJECT/locations/REGION/clusters/GKE_CLUSTER/nodePools/NODE_POOL",
                "roles":[
                  "DEFAULT"
                ]
              }
            ]
          },
          "kubernetesSoftwareConfig":{
            "componentVersion":{
              "SPARK":"3.1-..."
            },
            "properties":{
              "dpgke:dpgke.unstable.outputOnly.endpoints.sparkHistoryServer":"https://...",
              "spark:spark.eventLog.dir":"gs://BUCKET/.../spark-job-history",
              "spark:spark.eventLog.enabled":"true"
            }
          }
        },
        "auxiliaryServicesConfig":{
          "sparkHistoryServerConfig":{
            "dataprocCluster":"projects/PROJECT/regions/REGION/clusters/PHS_CLUSTER"
          }
        }
      }
    

## Submit a Spark job

After your Managed Service for Apache Spark on GKE virtual cluster is running, [submit a Spark job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#submit_a_spark_job) using the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit), or the Managed Service for Apache Spark [`jobs.submit`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs/submit) API (by using direct HTTP requests or the [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries)).

**Note:** In the following examples, the job jars are pre-installed and run "locally" on the Managed Service for Apache Spark virtual cluster.

**gcloud CLI Spark job example:**
    
    
    gcloud dataproc jobs submit spark \
        --region=${REGION} \
        --cluster=${DP_CLUSTER} \
        --class=org.apache.spark.examples.SparkPi \
        --jars=local:///usr/lib/spark/examples/jars/spark-examples.jar \
        -- 1000
    

**gcloud CLI PySpark job example:**
    
    
    gcloud dataproc jobs submit pyspark \
        --region=${REGION} \
        --cluster=${DP_CLUSTER} \
        local:///usr/lib/spark/examples/src/main/python/pi.py \
        -- 10
    

**gcloud CLI SparkR job example:**
    
    
    gcloud dataproc jobs submit spark-r \
        --region=${REGION} \
        --cluster=${DP_CLUSTER} \
        local:///usr/lib/spark/examples/src/main/r/dataframe.R
    

## Clean up

  * Delete any of the following resources used in this quickstart that you do not want to continue to use.

  * [Delete the Managed Service for Apache Spark on GKE cluster](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-delete-cluster).

  * [Delete node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deleting_a_node_pool) used by the Managed Service for Apache Spark on GKE cluster.

  * [Delete the GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
