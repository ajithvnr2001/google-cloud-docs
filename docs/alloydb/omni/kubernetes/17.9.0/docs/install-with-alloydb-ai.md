---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/install-with-alloydb-ai/
title: Install AlloyDB AI in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:43.470090+00:00
---

# Install AlloyDB AI in AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/install-with-alloydb-ai/

This page documents AlloyDB Omni version **17.9.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/overview)



Send feedback 

#  Install AlloyDB AI in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/install-with-alloydb-ai)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/install-with-alloydb-ai)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/install-with-alloydb-ai)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/install-with-alloydb-ai)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/install-with-alloydb-ai)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/install-with-alloydb-ai)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/install-with-alloydb-ai)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/install-with-alloydb-ai)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/install-with-alloydb-ai)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/install-with-alloydb-ai)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/install-with-alloydb-ai)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/install-with-alloydb-ai)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/install-with-alloydb-ai)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/install-with-alloydb-ai)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/install-with-alloydb-ai)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/install-with-alloydb-ai)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/install-with-alloydb-ai)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/install-with-alloydb-ai)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/install-with-alloydb-ai)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/install-with-alloydb-ai)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/install-with-alloydb-ai)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install-with-alloydb-ai)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install-with-alloydb-ai)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/install-with-alloydb-ai)

This page shows you how to install AlloyDB Omni and integrate AlloyDB AI. 

[AlloyDB AI](https://cloud.google.com/alloydb/ai) is a suite of features included with AlloyDB Omni that let you build enterprise generative AI applications. For more information about the AI/ML functionality of AlloyDB, see [Build generative AI applications](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/overview-ai).

AlloyDB Omni with AlloyDB AI lets you query remote ML models to work with online predictions and text embeddings generated from ML models. AlloyDB Omni with AlloyDB AI can also process vector embeddings from other content such as an image, for example, if you use the `google_ml.predict_row` interface and do the translation yourself in the query.

## Configure your AlloyDB Omni instance to query remote models

You can query remote models using model endpoint management by enabling `googleMLExtension` in your database cluster manifest.

Optionally, if you want to query Vertex AI models, you must configure AlloyDB service account with Vertex AI, create a Kubernetes secret using the key, and set the Kubernetes secret in the database cluster manifest.

### Add the Vertex AI permissions to AlloyDB service account

To configure AlloyDB Omni to query remote Vertex AI models, follow these steps:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with Google Cloud.

  2. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) and save it in JSON format to the `private-key.json` file, and download it.

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  3. Store the key in a permanent location on your file system. It resides at this location for the lifetime of your AlloyDB Omni server.

Note its location on your file system; you need it for subsequent steps.

  4. Add Vertex AI Identity and Access Management (IAM) permissions to the appropriate project and service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member="serviceAccount:SERVICE_ACCOUNT_ID" \
         --role="roles/aiplatform.user"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `SERVICE_ACCOUNT_ID`: the ID of the service account that you created in the previous step. This includes the full `@PROJECT_ID.iam.gserviceaccount.com` suffix—for example, `my-service@my-project.iam.gserviceaccount.com`.




### Create a Kubernetes secret using the service account key

To create a Kubernetes secret based on the service account key downloaded in the preceding steps, run the following command:

**Note:** Ensure that you create the Kubernetes secret in the same namespace as your `DBCluster` resource.
    
    
    kubectl create secret generic SECRET_NAME \
    --from-file=PATH_TO_SERVICE_ACCOUNT_KEY/private-key.json \
    -n NAMESPACE
    

Replace the following:

  * `SECRET_NAME`: the name of the secret used when you create a `DBCluster` manifest to enable AlloyDB Omni to access AlloyDB AI features. For example, `vertex-ai-key-alloydb`.

  * `PATH_TO_SERVICE_ACCOUNT_KEY`: the path to the location where you downloaded the `private-key.json` service account key.

  * `NAMESPACE`: the namespace of the database cluster.




## Install the AlloyDB Omni operator

Install the AlloyDB Omni operator using steps listed in [Install the AlloyDB Omni operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/deploy-kubernetes#install).

## Create a database cluster with AlloyDB AI

  1. Create a database cluster with AlloyDB AI.

When you set `enabled` to `true` under the `googleMLExtension` field, it lets you query remote models. Set the `vertexAIKeyRef` to the Kubernetes secret if you want to query Vertex AI models.
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: db-pw-DB_CLUSTER_NAME
         type: Opaque
         data:
           DB_CLUSTER_NAME: "ENCODED_PASSWORD"
         ---
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: DB_CLUSTER_NAME
         spec:
         databaseVersion: "17.9.0"
         primarySpec:
             adminUser:
               passwordRef:
                 name: db-pw-DB_CLUSTER_NAME
             features:
               googleMLExtension:
                 enabled: true
                 config:
                   vertexAIKeyRef: VERTEX_AI_SECRET_NAME
                   vertexAIRegion: VERTEX_AI_REGION
             resources:
               cpu: CPU_COUNT
               memory: MEMORY_SIZE
               disks:
               - name: DataDisk
                 size: DISK_SIZE
                 storageClass: standard
         

Replace the following:

     * `DB_CLUSTER_NAME`: the name of this database cluster—for example, `my-db-cluster`.

     * `VERTEX_AI_SECRET_NAME` (Optional): the Vertex AI secret that you created in preceding steps. You must set this option if you want to call Vertex AI models.

     * `VERTEX_AI_REGION` (Optional): the Vertex AI regional endpoint that you want to send your request to—for example, `us-west4`. The default value is `us-central1`.

     * `ENCODED_PASSWORD`: the database login password for the default `postgres` user role, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM=` for `ChangeMe123`.

     * `CPU_COUNT`: the number of CPUs available to each database instance in this database cluster.

     * `MEMORY_SIZE`: the amount of memory per database instance of this database cluster. We recommend setting this to 8 gigabytes per CPU. For example, if you set `cpu` to `2` earlier in this manifest, then we recommend setting `memory` to `16Gi`.

     * `DISK_SIZE`: the disk size per database instance—for example, `10Gi`.

  2. Apply the manifest.
         
         kubectl apply -f DB_CLUSTER_YAML

Replace the following:

     * `DB_CLUSTER_YAML`: the name of this database cluster manifest file—for example, `alloydb-omni-db-cluster.yaml`.
**Caution:** The database will be restarted after you apply the manifest with the `googleMLExtension` extension enabled.



## Connect using the preinstalled psql

You can make a test connection using a `psql` client already installed on the pod running the database.

To do this, run the following commands:
    
    
    export DBPOD=`kubectl get pod --selector=alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -o jsonpath='{.items[0].metadata.name}'`
    kubectl exec -ti $DBPOD -c database -- psql -h localhost -U postgres

Replace the `DB_CLUSTER_NAME` with the name of your database cluster. It's the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/install-with-alloydb-ai?resource=kubernetes#enable-alloydb-ai).

After you enter the command, the database server prompts you for a password. Enter the password whose base64-encoded version you supplied as a Kubernetes secret when creating the database cluster. For example, if you created the database cluster with a secret of `Q2hhbmdlTWUxMjM=`, then the login password to use here is `ChangeMe123`.

## Verify AlloyDB Omni with AlloyDB AI installation

To verify your installation is successful and uses model prediction, enter the following:
    
    
    CREATE EXTENSION IF NOT EXISTS google_ml_integration CASCADE;
    
    SELECT array_dims(embedding('text-embedding-005', 'AlloyDB AI')::real[]);
    

The output looks similar to the following:
    
    
    array_dims
    ------------
    [1:768]
    (1 row) 
    

**Note:** Vertex AI model support is governed by Vertex AI model versioning and lifecycle guidelines. For more information about stable versions, see [Model versions and lifecycle](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions).

In the previous query, the `embedding()` call generates embeddings for the input text `AlloyDB AI`. `array_dims` returns the dimensions of the array returned by `embedding()`. Since the `text-embedding-005` model returns an output with 768 dimensions, the output is `[768]`.

## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/run-connect)
  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manage)
  * [Build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/overview-ai)
  * [Register and call remote AI models](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/register-model-endpoint)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
