---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-recreate-cluster/
title: Recreate and update a Google Kubernetes Engine virtual cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:10.829810+00:00
---

# Recreate and update a Google Kubernetes Engine virtual cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-recreate-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Recreate and update a Google Kubernetes Engine virtual cluster Stay organized with collections  Save and categorize content based on your preferences. 

You can copy an existing Managed Service for Apache Spark on GKE virtual cluster's configuration, update the copied configuration, and then create a new Managed Service for Apache Spark on GKE cluster using the updated configuration.

## Recreate and update a Managed Service for Apache Spark on GKE cluster

### gcloud

  1. Set environment variables: 
         
         CLUSTER=existing Managed Service for Apache Spark on GKE  cluster name \
           REGION=[region](https://docs.cloud.google.com/compute/docs/regions-zones#available)
         

  2. Export the existing Managed Service for Apache Spark on GKE cluster configuration to a YAML file. 
         
         gcloud dataproc clusters export $CLUSTER \
             --region=$REGION > "${CLUSTER}-config.yaml"
         

  3. Update the configuration.

     1. Remove the [`kubernetesNamespace`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#KubernetesClusterConfig.FIELDS.kubernetes_namespace) field. Removing this field is necessary to avoid a namespace conflict when you create the updated cluster.

Sample `sed` command to remove the `kubernetesNamespace` field: 
            
            sed -E "s/kubernetesNamespace: .+$//g" ${CLUSTER}-config.yaml
            

     2. Make additional changes to update Managed Service for Apache Spark on GKE virtual cluster configuration settings, such as changing the Spark [componentVersion](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#KubernetesSoftwareConfig.FIELDS.component_version).

  4. [Delete the existing Managed Service for Apache Spark on GKE virtual cluster](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-delete-cluster) if you will create a cluster that has the same name as the cluster it is updating (if you are replacing the original cluster).

  5. Wait for the previous delete operation to finish, and then import the updated cluster configuration to create a new Managed Service for Apache Spark on GKE virtual cluster with the updated config settings. 
         
         gcloud dataproc clusters import $CLUSTER \
             --region=$REGION \
             --source="${CLUSTER}-config.yaml"




### API

  1. Set environment variables: 
         
         CLUSTER=existing Managed Service for Apache Spark on GKE  cluster name \
           REGION=[region](https://docs.cloud.google.com/compute/docs/regions-zones#available)
         

  2. Export the existing Managed Service for Apache Spark on GKE cluster configuration to a YAML file. 
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)"  "https://dataproc.googleapis.com/v1/projects/${PROJECT}/regions/${REGION}/clusters/${CLUSTER}?alt=json" > "${CLUSTER}-config.json"

  3. Update the configuration.

     1. Remove the [`kubernetesNamespace`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#KubernetesClusterConfig.FIELDS.kubernetes_namespace) field. Removal of this field is necessary to avoid a namespace conflict when you create the updated cluster.

Sample `jq` command to remove `kubernetesNamespace` field: 
            
            jq 'del(.virtualClusterConfig.kubernetesClusterConfig.kubernetesNamespace)'
            

     2. Make additional changes to update Managed Service for Apache Spark on GKE virtual cluster configuration settings, such as changing the Spark [componentVersion](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#KubernetesSoftwareConfig.FIELDS.component_version).

  4. Delete the existing Managed Service for Apache Spark on GKE virtual cluster if you will create a cluster that has the same name as the cluster it is updating (if you are replacing the original cluster). 
         
         curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://dataproc.googleapis.com/v1/projects/${PROJECT}/regions/${REGION}/clusters/${CLUSTER}"
         

  5. Wait for the previous delete operation to finish, and then import the updated cluster configuration to create a new Managed Service for Apache Spark on GKE virtual cluster with the updated settings. 
         
         curl -i -X POST  -H "Authorization: Bearer $(gcloud auth print-access-token)"  -H "Content-Type: application/json; charset=utf-8" -d "@${CLUSTER}-config.json" "https://dataproc.googleapis.com/v1/projects/${PROJECT}/regions/${REGION}/clusters?alt=json"
         




### Console

The Google Cloud console does not support recreating a Managed Service for Apache Spark on GKE virtual cluster by importing an existing cluster's configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
