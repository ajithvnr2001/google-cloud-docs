---
url: https://docs.cloud.google.com/managed-spark/docs/guides/recreate-cluster/
title: Recreate and update a cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:46.256718+00:00
---

# Recreate and update a cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/recreate-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Recreate and update a cluster Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark prevents the creation of clusters with image versions prior to 1.3.95, 1.4.77, 1.5.53, and 2.0.27, which were affected by [Apache Log4j security vulnerabilities](https://logging.apache.org/log4j/2.x/security.html). Managed Service for Apache Spark also prevents cluster creation for Managed Service for Apache Spark image versions 0.x, 1.0.x, 1.1.x, and 1.2.x. Managed Service for Apache Spark advises that, when possible, you create Managed Service for Apache Spark clusters with the latest sub-minor image versions.

Image version | log4j version | Customer guidance  
---|---|---  
2.0.29, 1.5.55, and 1.4.79, or later of each | log4j.2.17.1 | Advised  
2.0.28, 1.5.54, and 1.4.78 | log4j.2.17.0 | Advised  
2.0.27, 1.5.53, and 1.4.77 | log4j.2.16.0 | Strongly recommended  
2.0.26, 1.5.52, and 1.4.76, or earlier of each | Older version | Discontinue use  
  
See the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) for specific image and `log4j` update information.

## Recreate and update a cluster

You can use the `gcloud` command-line tool or the Managed Service for Apache Spark API to copy configuration from an existing cluster, update the copied configuration, and then create a new cluster with the updated configuration.

### gcloud CLI

The example instructions show updating the image version setting in a cluster configuration. You can change the example to update different cluster configuration settings.

The recommended practice is to specify the `major.minor` image version for production environments or when compatibility with specific component versions is important. The sub-minor and OS distributions are automatically set to the latest weekly release.

  1. Set variables. 
         
         export PROJECT=project-id
         export REGION=region
         export OLD_CLUSTER=old-cluster-name
         export NEW_CLUSTER=new-cluster-name
         export NEW_IMAGE_VERSION=image-version (for example, '2.2-debian12')
         

  2. Export the existing (old) cluster configuration to a YAML file. 
         
         gcloud dataproc clusters export $OLD_CLUSTER \
             --project=$PROJECT \
             --region=$REGION > "${OLD_CLUSTER}-config.yaml"

  3. Update the configuration. The following example uses `sed` to update the image version. 
         
         sed -E "s|(^[[:blank:]]+)imageVersion: .+|\1imageVersion: ${NEW_IMAGE_VERSION}|g" "${OLD_CLUSTER}-config.yaml" | sed -E '/^[[:blank:]]+imageUri: /d' > "${NEW_CLUSTER}-config-updated.yaml"

  4. Create a new cluster with a new name and the updated configuration. 
         
         gcloud dataproc clusters import $NEW_CLUSTER \
             --project=$PROJECT \
             --region=$REGION \
             --source="${NEW_CLUSTER}-config-updated.yaml"

  5. After confirming your workloads run in the new cluster without issues, delete the existing (old) cluster. **IMPORTANT:** This step deletes all data stored in HDFS and on local disk in your cluster. 
         
         gcloud dataproc clusters delete $OLD_CLUSTER \
             --project=$PROJECT \
             --region=$REGION




### REST API

The example instructions show updating the cluster name and the image version settings in a cluster configuration. You can change the example variables to update different cluster configuration settings.

The recommended practice is to specify the `major.minor` image version for production environments or when compatibility with specific component versions is important. The sub-minor and OS distributions are automatically set to the latest weekly release.

  1. Set variables. 
         
         export PROJECT=project-id
         export REGION=region
         export OLD_CLUSTER=old-cluster-name
         export NEW_CLUSTER=new-cluster-name
         export NEW_IMAGE_VERSION=image-version (for example, '2.2-debian12')
         
         

  2. Export the existing (old) cluster configuration to a JSON file. 
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)"  "https://dataproc.googleapis.com/v1/projects/${PROJECT}/regions/${REGION}/clusters/${OLD_CLUSTER}?alt=json" > "${OLD_CLUSTER}-config.json"

  3. Update the configuration. The following example uses `jq` to update the cluster name and the image version. 
         
         jq ".clusterName = \"${NEW_CLUSTER}\" | .config.softwareConfig.imageVersion=\"${NEW_IMAGE_VERSION}\" | del(.config.workerConfig.imageUri) | del(.config.masterConfig.imageUri)" "${OLD_CLUSTER}-config.json" > "${NEW_CLUSTER}-config-updated.json"

  4. Import the updated cluster configuration to create a new cluster with the updated configuration. 
         
         curl -i -X POST  -H "Authorization: Bearer $(gcloud auth print-access-token)"  -H "Content-Type: application/json; charset=utf-8" -d "@${NEW_CLUSTER}-config-updated.json" "https://dataproc.googleapis.com/v1/projects/${PROJECT}/regions/${REGION}/clusters?alt=json"

  5. After confirming your workloads run in the new cluster without issues, delete the existing (old) cluster. **IMPORTANT:** This step deletes all data stored in HDFS and on local disk in your cluster. 
         
         curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://dataproc.googleapis.com/v1/projects/${PROJECT}/regions/${REGION}/clusters/${OLD_CLUSTER}"
         




### Console

The console does not support recreating a cluster by importing a cluster configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
