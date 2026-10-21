---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-iam/
title: Google Kubernetes Engine Identity and Access Management roles and identity \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:23.988003+00:00
---

# Google Kubernetes Engine Identity and Access Management roles and identity  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-iam/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Google Kubernetes Engine Identity and Access Management roles and identity Stay organized with collections  Save and categorize content based on your preferences. 

## Data plane Identity

Managed Service for Apache Spark on GKE uses [GKE workload identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to allow pods within the Managed Service for Apache Spark on GKE cluster to act with the authority of the default [Managed Service for Apache Spark VM service account (data plane identity)](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#vm_service_account_data_plane_identity).

**Note:** Although granting IAM roles directly to a Kubernetes ServiceAccount principal (`principal://`) is the recommended best practice for [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), Managed Service for Apache Spark on GKE requires IAM service account impersonation because the `--setup-workload-identity` flag and `dataproc:dataproc.gke.*.google-service-account` cluster properties require an IAM service account email address.

Workload identity requires the following permissions to update IAM policies on the GSA used by your Managed Service for Apache Spark on GKE virtual cluster:

  * `compute.projects.get`
  * `iam.serviceAccounts.getIamPolicy`
  * `iam.serviceAccounts.setIamPolicy`

**Note:** You can use workload identity with a different GSA: see Custom IAM configuration.

GKE workload identity links the following GKE Service Accounts (KSAs) to the Managed Service for Apache Spark VM Service Account: 

  1. `agent` KSA (interacts with Managed Service for Apache Spark control plane):  
`serviceAccount:${PROJECT}.svc.id.goog[${DPGKE_NAMESPACE}/agent]`
  2. `spark-driver` KSA (runs Spark drivers):  
`serviceAccount:${PROJECT}.svc.id.goog[${DPGKE_NAMESPACE}/spark-driver]`
  3. `spark-executor` KSA (runs Spark executors):  
`serviceAccount:${PROJECT}.svc.id.goog[${DPGKE_NAMESPACE}/spark-executor]`

Use the `gcloud dataproc clusters gke create --setup-workload-identity` flag when you [create a Managed Service for Apache Spark on GKE cluster](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/dataproc-gke-quickstart-create-cluster) to create the workload identity bindings required for the cluster.

### Assign roles

Grant permissions to the [Managed Service for Apache Spark VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#vm_service_account_data_plane_identity) to allow the `spark-driver` and `spark-executor` to access project resources, data sources, data sinks, and any other services required by your workload.

Example:

The following command assigns roles to the [default Managed Service for Apache Spark VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#dataproc_service_accounts_2) to allow Spark workloads running on Managed Service for Apache Spark on GKE cluster VMs to access Cloud Storage buckets and BigQuery data sets in the project.
    
    
    gcloud projects add-iam-policy-binding \
        --role=roles/storage.objectAdmin \
        --role=roles/bigquery.dataEditor \
        --member="project-number-compute@developer.gserviceaccount.com" \
        "${PROJECT}"
    

## Custom IAM configuration

Managed Service for Apache Spark on GKE uses [GKE workload identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to link the default [Managed Service for Apache Spark VM service account (data plane identity)](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#vm_service_account_data_plane_identity) to the three GKE service accounts (KSAs).

To create and use a different Google service account (GSA) to link to the KSAs:

  1. Create the GSA (see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)).

gcloud CLI example: 
         
         gcloud iam service-accounts create "dataproc-${USER}" \
             --description "Used by Managed Service for Apache Spark on GKE workloads."
         

Notes: 
     * The example sets the GSA name as "dataproc-${USER}", but you can use a different name.
  2. Set environmental variables: 
         
         PROJECT=project-id \
           DPGKE_GSA="dataproc-${USER}@${PROJECT}.iam.gserviceaccount.com"
           DPGKE_NAMESPACE=GKE namespace
         

Notes: 
     * `DPGKE_GSA`: The examples set and use `DPGKE_GSA` as the name of the variable that contains the email address of your GSA. You can set and use a different variable name.
     * `DPGKE_NAMESPACE`: The default GKE namespace is the name of your Managed Service for Apache Spark on GKE cluster.
  3. When you create the Managed Service for Apache Spark on GKE cluster, add the following properties for Managed Service for Apache Spark to use your GSA instead of the default GSA: 
         
         --properties "dataproc:dataproc.gke.agent.google-service-account=${DPGKE_GSA}" \
         --properties "dataproc:dataproc.gke.nodepool.google-service-account=${DPGKE_GSA}" \
         --properties "dataproc:dataproc.gke.spark.driver.google-service-account=${DPGKE_GSA}" \
         --properties "dataproc:dataproc.gke.spark.executor.google-service-account=${DPGKE_GSA}" \
         

  4. Run the following commands to assign necessary [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) permissions to the service accounts:

     1. Assign your GSA the `dataproc.worker` role to allow it to act as agent: 
            
            gcloud projects add-iam-policy-binding \
                --role=roles/dataproc.worker \
                --member="serviceAccount:${DPGKE_GSA}" \
                "${PROJECT}"
            

     2. Assign the `agent` KSA the `iam.workloadIdentityUser` role to allow it to act as your GSA: 
            
            gcloud iam service-accounts add-iam-policy-binding \
                --role=roles/iam.workloadIdentityUser \
                --member="serviceAccount:${PROJECT}.svc.id.goog[${DPGKE_NAMESPACE}/agent]" \
                "${DPGKE_GSA}"
            

     3. Grant the `spark-driver` KSA the `iam.workloadIdentityUser` role to allow it to act as your GSA: 
            
            gcloud iam service-accounts add-iam-policy-binding \
                --role=roles/iam.workloadIdentityUser \
                --member="serviceAccount:${PROJECT}.svc.id.goog[${DPGKE_NAMESPACE}/spark-driver]" \
                "${DPGKE_GSA}"
            

     4. Grant the `spark-executor` KSA the `iam.workloadIdentityUser` role to allow it to act as your GSA: 
            
            gcloud iam service-accounts add-iam-policy-binding \
                --role=roles/iam.workloadIdentityUser \
                --member="serviceAccount:${PROJECT}.svc.id.goog[${DPGKE_NAMESPACE}/spark-executor]" \
                "${DPGKE_GSA}"
            




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
