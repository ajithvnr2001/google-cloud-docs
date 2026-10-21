---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/build-rag-chatbot/
title: Build a RAG chatbot with GKE and Cloud Storage \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:40.544942+00:00
---

# Build a RAG chatbot with GKE and Cloud Storage  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/build-rag-chatbot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Build a RAG chatbot with GKE and Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to integrate a large language model (LLM) application based on retrieval-augmented generation (RAG) with PDF files that you upload to a Cloud Storage bucket.

This guide uses a database as a storage and semantic search engine that holds the representations (embeddings) of the uploaded documents. You use the [Langchain framework](https://www.langchain.com/) to interact with the embeddings and you use Gemini models available through Vertex AI.

Langchain is a popular open-source Python framework that simplifies many machine learning tasks and has interfaces to integrate with different vector databases and AI services.

This tutorial is intended for cloud platform [administrators and architects](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#admins), [ML engineers](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#data-ai-ml-engineer), and MLOps (DevOps) professionals interested in deploying RAG LLM applications to GKE and Cloud Storage.

## Objectives

In this tutorial, you learn how to:

  * Build and deploy an application to create and store document embeddings in a vector database.
  * Automate the application to trigger new document uploads to a Cloud Storage bucket.
  * Deploy a chatbot application that uses semantic search to answer questions based on the document content.



## Deployment architecture

In this tutorial, you create a Cloud Storage bucket, an Eventarc trigger, and the following Services:

  * `embed-docs`: Eventarc triggers this Service every time a user uploads a new document to the Cloud Storage bucket. The Service starts a [Kubernetes Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) which creates embeddings for the uploaded document and inserts the embeddings into a vector database.
  * `chatbot`: This Service answers natural language questions about the uploaded documents using semantic search and the [Gemini API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini).



The following diagram shows the process of uploading and vectorizing documents:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/rag-architecture-embedding.svg)

In the diagram, the user uploads files into the Cloud Storage bucket. Eventarc subscribes to object `metadataUpdated` events for the bucket and uses Eventarc's event forwarder, which is a Kubernetes workload, to call the `embed-docs` Service when you upload a new document. The Service then creates embeddings for the uploaded document. The `embed-docs` Service stores the embeddings in a vector database using the Vertex AI embedding model.

The following diagram shows the process of asking questions about the uploaded document content using the `chatbot` Service:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/rag-architecture-asking-llm-model.svg)

Users can ask questions using natural language, and the chatbot generates answers based solely on the content of the uploaded files. The chatbot retrieves context from the vector database using semantic search, then sends the question and context to Gemini.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [Cloud Build](https://cloud.google.com/build/pricing)
  * [Eventarc](https://cloud.google.com/eventarc/pricing)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/pricing)
  * [Vertex AI](https://cloud.google.com/vertex-ai/pricing)
  * [Pub/Sub](https://cloud.google.com/pubsub/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs) to run commands. Cloud Shell is a shell environment for managing resources hosted on Google Cloud. Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), [kubectl](https://kubernetes.io/docs/reference/kubectl/), and [Terraform](https://docs.cloud.google.com/docs/terraform) command-line tools. If you don't use Cloud Shell, install the Google Cloud CLI.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Vertex AI, Cloud Build, Eventarc, Artifact Registry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable aiplatform.googleapis.com cloudbuild.googleapis.com eventarc.googleapis.com artifactregistry.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Vertex AI, Cloud Build, Eventarc, Artifact Registry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable aiplatform.googleapis.com cloudbuild.googleapis.com eventarc.googleapis.com artifactregistry.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `eventarc.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Create a cluster

Create a Qdrant, Elasticsearch, or Postgres cluster:

###  Qdrant 

Follow the instructions in [Deploy a Qdrant vector database on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-qdrant) to create a Qdrant cluster running on an Autopilot mode or Standard mode GKE cluster.

###  Elasticsearch 

Follow the instructions in [Deploy an Elasticsearch vector database on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-elasticsearch) to create an Elasticsearch cluster running on an Autopilot mode or Standard mode GKE cluster.

###  PGVector 

Follow the instructions in [Deploy a PostgreSQL vector database on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-pgvector) to create a Postgres cluster with PGVector running on an Autopilot mode or Standard mode GKE cluster.

###  Weaviate 

Follow the instructions to [Deploy a Weaviate vector database on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-weaviate) to create a Weaviate cluster running on an Autopilot or Standard mode GKE cluster.

## Set up your environment

Set up your environment with Cloud Shell:

  1. Set environment variables for your project:

###  Qdrant 
         
         export PROJECT_ID=PROJECT_ID
         export KUBERNETES_CLUSTER_PREFIX=qdrant
         export CONTROL_PLANE_LOCATION=us-central1
         export REGION=us-central1
         export DB_NAMESPACE=qdrant
         

Replace `PROJECT_ID` with your Google Cloud project ID.

###  Elasticsearch 
         
         export PROJECT_ID=PROJECT_ID
         export KUBERNETES_CLUSTER_PREFIX=elasticsearch
         export CONTROL_PLANE_LOCATION=us-central1
         export REGION=us-central1
         export DB_NAMESPACE=elastic
         

Replace `PROJECT_ID` with your Google Cloud project ID.

###  PGVector 
         
         export PROJECT_ID=PROJECT_ID
         export KUBERNETES_CLUSTER_PREFIX=postgres
         export CONTROL_PLANE_LOCATION=us-central1
         export REGION=us-central1
         export DB_NAMESPACE=pg-ns
         

Replace `PROJECT_ID` with your Google Cloud project ID.

###  Weaviate 
         
         export PROJECT_ID=PROJECT_ID
         export KUBERNETES_CLUSTER_PREFIX=weaviate
         export CONTROL_PLANE_LOCATION=us-central1
         export REGION=us-central1
         export DB_NAMESPACE=weaviate
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Verify that your GKE cluster is running:
         
         gcloud container clusters list --project=${PROJECT_ID} --location=${CONTROL_PLANE_LOCATION}
         

The output is similar to the following:
         
         NAME                                    LOCATION        MASTER_VERSION      MASTER_IP     MACHINE_TYPE  NODE_VERSION        NUM_NODES STATUS
         [KUBERNETES_CLUSTER_PREFIX]-cluster   us-central1   1.30.1-gke.1329003  <EXTERNAL IP> e2-standard-2 1.30.1-gke.1329003   6        RUNNING
         

  3. Clone the sample code repository from GitHub:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  4. Navigate to the `databases` directory:
         
         cd kubernetes-engine-samples/databases
         




## Prepare your infrastructure

Create an Artifact Registry repository, build Docker images, and push Docker images to Artifact Registry:

  1. Create an Artifact Registry repository:
         
         gcloud artifacts repositories create ${KUBERNETES_CLUSTER_PREFIX}-images \
             --repository-format=docker \
             --location=${REGION} \
             --description="Vector database images repository" \
             --async
         

  2. Set the `storage.objectAdmin` and `artifactregistry.admin` permissions on the Compute Engine service account to use [Cloud Build](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit) to build and push Docker images for the `embed-docs` and `chatbot` Services.
         
         export PROJECT_NUMBER=PROJECT_NUMBER
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID}  \
         --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
         --role="roles/storage.objectAdmin"
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID}  \
         --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
         --role="roles/artifactregistry.admin"
         

Replace `PROJECT_NUMBER` with your Google Cloud project number.

  3. Build Docker images for the `embed-docs` and `chatbot` Services. The `embed-docs` image contains Python code for both the application that receives Eventarc forwarder requests and the embedding job.

###  Qdrant 
         
         export DOCKER_REPO="${REGION}-docker.pkg.dev/${PROJECT_ID}/${KUBERNETES_CLUSTER_PREFIX}-images"
         gcloud builds submit qdrant/docker/chatbot --region=${REGION} \
           --tag ${DOCKER_REPO}/chatbot:1.0 --async
         gcloud builds submit qdrant/docker/embed-docs --region=${REGION} \
           --tag ${DOCKER_REPO}/embed-docs:1.0 --async
         

###  Elasticsearch 
         
         export DOCKER_REPO="${REGION}-docker.pkg.dev/${PROJECT_ID}/${KUBERNETES_CLUSTER_PREFIX}-images"
         gcloud builds submit elasticsearch/docker/chatbot --region=${REGION} \
           --tag ${DOCKER_REPO}/chatbot:1.0 --async
         gcloud builds submit elasticsearch/docker/embed-docs --region=${REGION} \
           --tag ${DOCKER_REPO}/embed-docs:1.0 --async
         

###  PGVector 
         
         export DOCKER_REPO="${REGION}-docker.pkg.dev/${PROJECT_ID}/${KUBERNETES_CLUSTER_PREFIX}-images"
         gcloud builds submit postgres-pgvector/docker/chatbot --region=${REGION} \
           --tag ${DOCKER_REPO}/chatbot:1.0 --async
         gcloud builds submit postgres-pgvector/docker/embed-docs --region=${REGION} \
           --tag ${DOCKER_REPO}/embed-docs:1.0 --async
         

###  Weaviate 
         
         export DOCKER_REPO="${REGION}-docker.pkg.dev/${PROJECT_ID}/${KUBERNETES_CLUSTER_PREFIX}-images"
         gcloud builds submit weaviate/docker/chatbot --region=${REGION} \
           --tag ${DOCKER_REPO}/chatbot:1.0 --async
         gcloud builds submit weaviate/docker/embed-docs --region=${REGION} \
           --tag ${DOCKER_REPO}/embed-docs:1.0 --async
         

  4. Verify the images:
         
         gcloud artifacts docker images list $DOCKER_REPO \
             --project=$PROJECT_ID \
             --format="value(IMAGE)"
         

The output is similar to the following:
         
         $REGION-docker.pkg.dev/$PROJECT_ID/${KUBERNETES_CLUSTER_PREFIX}-images/chatbot
         $REGION-docker.pkg.dev/$PROJECT_ID/${KUBERNETES_CLUSTER_PREFIX}-images/embed-docs
         

  5. Deploy a [Kubernetes Service Account](https://kubernetes.io/docs/concepts/security/service-accounts/) with permissions to run Kubernetes Jobs:

###  Qdrant 
         
         sed "s/<PROJECT_ID>/$PROJECT_ID/;s/<CLUSTER_PREFIX>/$KUBERNETES_CLUSTER_PREFIX/" qdrant/manifests/05-rag/service-account.yaml | kubectl -n qdrant apply -f -
         

###  Elasticsearch 
         
         sed "s/<PROJECT_ID>/$PROJECT_ID/;s/<CLUSTER_PREFIX>/$KUBERNETES_CLUSTER_PREFIX/" elasticsearch/manifests/05-rag/service-account.yaml | kubectl -n elastic apply -f -
         

###  PGVector 
         
         sed "s/<PROJECT_ID>/$PROJECT_ID/;s/<CLUSTER_PREFIX>/$KUBERNETES_CLUSTER_PREFIX/" postgres-pgvector/manifests/03-rag/service-account.yaml | kubectl -n pg-ns apply -f -
         

###  Weaviate 
         
         sed "s/<PROJECT_ID>/$PROJECT_ID/;s/<CLUSTER_PREFIX>/$KUBERNETES_CLUSTER_PREFIX/" weaviate/manifests/04-rag/service-account.yaml | kubectl -n weaviate apply -f -
         

  6. When using Terraform to create the GKE cluster and have `create_service_account` set as true, a separate service account will be created and used by the cluster and nodes. Grant `artifactregistry.serviceAgent` role to this Compute Engine service account to allow the nodes to pull image from the Artifact Registry created for `embed-docs` and `chatbot`.
         
         export CLUSTER_SERVICE_ACCOUNT=$(gcloud container clusters describe ${KUBERNETES_CLUSTER_PREFIX}-cluster \
         --location=${CONTROL_PLANE_LOCATION} \
         --format="value(nodeConfig.serviceAccount)")
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID}  \
         --member="serviceAccount:${CLUSTER_SERVICE_ACCOUNT}" \
         --role="roles/artifactregistry.serviceAgent"
         

Without granting access to the service account, your nodes might experience permission issue when trying to pull image from the Artifact Registry when deploying the `embed-docs` and `chatbot` Services.

  7. Deploy a Kubernetes Deployment for the `embed-docs` and `chatbot` Services. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster.:

###  Qdrant 
         
         sed "s|<DOCKER_REPO>|$DOCKER_REPO|" qdrant/manifests/05-rag/chatbot.yaml | kubectl -n qdrant apply -f -
         sed "s|<DOCKER_REPO>|$DOCKER_REPO|" qdrant/manifests/05-rag/docs-embedder.yaml | kubectl -n qdrant apply -f -
         

###  Elasticsearch 
         
         sed "s|<DOCKER_REPO>|$DOCKER_REPO|" elasticsearch/manifests/05-rag/chatbot.yaml | kubectl -n elastic apply -f -
         sed "s|<DOCKER_REPO>|$DOCKER_REPO|" elasticsearch/manifests/05-rag/docs-embedder.yaml | kubectl -n elastic apply -f -
         

###  PGVector 
         
         sed "s|<DOCKER_REPO>|$DOCKER_REPO|" postgres-pgvector/manifests/03-rag/chatbot.yaml | kubectl -n pg-ns apply -f -
         sed "s|<DOCKER_REPO>|$DOCKER_REPO|" postgres-pgvector/manifests/03-rag/docs-embedder.yaml | kubectl -n pg-ns apply -f -
         

###  Weaviate 
         
         sed "s|<DOCKER_REPO>|$DOCKER_REPO|" weaviate/manifests/04-rag/chatbot.yaml | kubectl -n weaviate apply -f -
         sed "s|<DOCKER_REPO>|$DOCKER_REPO|" weaviate/manifests/04-rag/docs-embedder.yaml | kubectl -n weaviate apply -f -
         

  8. Enable Eventarc triggers for GKE:
         
         gcloud eventarc gke-destinations init
         

When prompted, enter `y`.

  9. Deploy the Cloud Storage bucket and create an Eventarc trigger using Terraform:
         
         export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
         terraform -chdir=vector-database/terraform/cloud-storage init
         terraform -chdir=vector-database/terraform/cloud-storage apply \
           -var project_id=${PROJECT_ID} \
           -var region=${REGION} \
           -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX} \
           -var db_namespace=${DB_NAMESPACE}
         

When prompted, type `yes`. It might take several minutes for the command to complete.

Terraform creates the following resources:

     * A Cloud Storage bucket to upload the documents
     * An Eventarc trigger
     * A Google Cloud Service Account named `service_account_eventarc_name` with permission to use Eventarc.
     * A Google Cloud Service Account named `service_account_bucket_name` with permission to read the bucket and access Vertex AI models.

The output is similar to the following:
    
    ... # Several lines of output omitted
    
    Apply complete! Resources: 15 added, 0 changed, 0 destroyed.
    
    ... # Several lines of output omitted
    




## Load documents and run chatbot queries

Upload the demo documents and run queries to search over the demo documents using the chatbot:

  1. Upload the example `carbon-free-energy.pdf` document to your bucket:
         
         gcloud storage cp vector-database/documents/carbon-free-energy.pdf gs://${PROJECT_ID}-${KUBERNETES_CLUSTER_PREFIX}-training-docs
         

  2. Verify the document embedder job completed successfully:
         
         kubectl get job -n ${DB_NAMESPACE}
         

The output is similar to the following:
         
         NAME                            COMPLETIONS   DURATION   AGE
         docs-embedder1716570453361446   1/1           32s        71s
         

  3. Get the external IP address of the load balancer:
         
         export EXTERNAL_IP=$(kubectl -n ${DB_NAMESPACE} get svc chatbot --output jsonpath='{.status.loadBalancer.ingress[0].ip}')
         echo http://${EXTERNAL_IP}:80
         

  4. Open the external IP address in your web browser:
         
         http://EXTERNAL_IP
         

The chatbot responds with a message similar to the following:
         
         How can I help you?
         

  5. Ask questions about the content of the uploaded documents. If the chatbot cannot find anything, it answers `I don't know`. For example, you could ask the following:
         
         You: Hi, what are Google plans for the future?
         

An example output from the chatbot is similar to the following:
         
         Bot: Google intends to run on carbon-free energy everywhere, at all times by 2030. To achieve this, it will rely on a combination of renewable energy sources, such as wind and solar, and carbon-free technologies, such as battery storage.
         

  6. Ask the chatbot a question that is out of context of the uploaded document. For example, you could ask the following:
         
         You: What are Google plans to colonize Mars?
         

An example output from the chatbot is similar to the following:
         
         Bot: I don't know. The provided context does not mention anything about Google's plans to colonize Mars.
         




## About the application code

This section explains how the application code works. There are three scripts inside the Docker images:

  * `endpoint.py`: receives Eventarc events on each document upload and starts the Kubernetes Jobs to process them.
  * `embedding-job.py`: downloads documents from the bucket, creates embeddings, and insert embeddings into the vector database.
  * `chat.py`: runs queries over the content of stored documents.



The diagram shows the process of generating answers using the documents data:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/rag-application-code.svg)

In the diagram, the application loads a PDF file, splits the file into chunks, then vectors, then sends the vectors to a vector database. Later, a user asks a question to the chatbot. The RAG chain uses semantic search to search the vector database, then returns the context along with the question to the LLM. The LLM answers the question, and stores the question into chat history.

### About `endpoint.py`

This file processes messages from Eventarc, creates a Kubernetes Job for embedding the document, and accepts request from anywhere on port 5001

###  Qdrant 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from flask import Flask, jsonify
    from flask import request
    import logging
    import sys,os, time
    from kubernetes import client, config, utils
    import kubernetes.client
    from kubernetes.client.rest import ApiException
    
    
    app = Flask(__name__)
    @app.route('/check')
    def message():
        return jsonify({"Message": "Hi there"})
    
    
    @app.route('/', methods=['POST'])
    def bucket():
        request_data = request.get_json()
        print(request_data)
        bckt = request_data['bucket']
        f_name = request_data['name']
        id = request_data['generation'] 
        kube_create_job(bckt, f_name, id)
        return "ok"
    
    # Set logging
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    
    # Setup K8 configs
    config.load_incluster_config()
    def kube_create_job_object(name, container_image, bucket_name, f_name, namespace="qdrant", container_name="jobcontainer", env_vars={}):
    
        body = client.V1Job(api_version="batch/v1", kind="Job")
        body.metadata = client.V1ObjectMeta(namespace=namespace, name=name)
        body.status = client.V1JobStatus()
    
        template = client.V1PodTemplate()
        template.template = client.V1PodTemplateSpec()
        env_list = [
            client.V1EnvVar(name="QDRANT_URL", value=os.getenv("QDRANT_URL")),
            client.V1EnvVar(name="COLLECTION_NAME", value="training-docs"), 
            client.V1EnvVar(name="FILE_NAME", value=f_name), 
            client.V1EnvVar(name="BUCKET_NAME", value=bucket_name),
            client.V1EnvVar(name="APIKEY", value_from=client.V1EnvVarSource(secret_key_ref=client.V1SecretKeySelector(key="api-key", name="qdrant-database-apikey"))), 
        ]
    
        container = client.V1Container(name=container_name, image=container_image, env=env_list)
        template.template.spec = client.V1PodSpec(containers=[container], restart_policy='Never', service_account='embed-docs-sa')
    
        body.spec = client.V1JobSpec(backoff_limit=3, ttl_seconds_after_finished=60, template=template.template)
        return body
    def kube_test_credentials():
        try: 
            api_response = api_instance.get_api_resources()
            logging.info(api_response)
        except ApiException as e:
            print("Exception when calling API: %s\n" % e)
    
    def kube_create_job(bckt, f_name, id):
        container_image = os.getenv("JOB_IMAGE")
        namespace = os.getenv("JOB_NAMESPACE")
        name = "docs-embedder" + id
        body = kube_create_job_object(name, container_image, bckt, f_name)
        v1=client.BatchV1Api()
        try: 
            v1.create_namespaced_job(namespace, body, pretty=True)
        except ApiException as e:
            print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)
        return
    
    if __name__ == '__main__':
        app.run('0.0.0.0', port=5001, debug=True)
    

###  Elasticsearch 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from flask import Flask, jsonify
    from flask import request
    import logging
    import sys,os, time
    from kubernetes import client, config, utils
    import kubernetes.client
    from kubernetes.client.rest import ApiException
    
    
    app = Flask(__name__)
    @app.route('/check')
    def message():
        return jsonify({"Message": "Hi there"})
    
    
    @app.route('/', methods=['POST'])
    def bucket():
        request_data = request.get_json()
        print(request_data)
        bckt = request_data['bucket']
        f_name = request_data['name']
        id = request_data['generation'] 
        kube_create_job(bckt, f_name, id)
        return "ok"
    
    # Set logging
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    
    # Setup K8 configs
    config.load_incluster_config()
    
    def kube_create_job_object(name, container_image, bucket_name, f_name, namespace="elastic", container_name="jobcontainer", env_vars={}):
    
        body = client.V1Job(api_version="batch/v1", kind="Job")
        body.metadata = client.V1ObjectMeta(namespace=namespace, name=name)
        body.status = client.V1JobStatus()
    
        template = client.V1PodTemplate()
        template.template = client.V1PodTemplateSpec()
        env_list = [
            client.V1EnvVar(name="ES_URL", value=os.getenv("ES_URL")),
            client.V1EnvVar(name="INDEX_NAME", value="training-docs"), 
            client.V1EnvVar(name="FILE_NAME", value=f_name), 
            client.V1EnvVar(name="BUCKET_NAME", value=bucket_name),
            client.V1EnvVar(name="PASSWORD", value_from=client.V1EnvVarSource(secret_key_ref=client.V1SecretKeySelector(key="elastic", name="elasticsearch-ha-es-elastic-user"))), 
        ]
    
        container = client.V1Container(name=container_name, image=container_image, image_pull_policy='Always', env=env_list)
        template.template.spec = client.V1PodSpec(containers=[container], restart_policy='Never', service_account='embed-docs-sa')
    
        body.spec = client.V1JobSpec(backoff_limit=3, ttl_seconds_after_finished=60, template=template.template)
        return body
    
    def kube_test_credentials():
        try: 
            api_response = api_instance.get_api_resources()
            logging.info(api_response)
        except ApiException as e:
            print("Exception when calling API: %s\n" % e)
    
    def kube_create_job(bckt, f_name, id):
        container_image = os.getenv("JOB_IMAGE")
        namespace = os.getenv("JOB_NAMESPACE")
        name = "docs-embedder" + id
        body = kube_create_job_object(name, container_image, bckt, f_name)
        v1=client.BatchV1Api()
        try: 
            v1.create_namespaced_job(namespace, body, pretty=True)
        except ApiException as e:
            print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)
        return
    
    if __name__ == '__main__':
        app.run('0.0.0.0', port=5001, debug=True)
    

###  PGVector 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from flask import Flask, jsonify
    from flask import request
    import logging
    import sys,os, time
    from kubernetes import client, config, utils
    import kubernetes.client
    from kubernetes.client.rest import ApiException
    
    
    app = Flask(__name__)
    @app.route('/check')
    def message():
        return jsonify({"Message": "Hi there"})
    
    
    @app.route('/', methods=['POST'])
    def bucket():
        request_data = request.get_json()
        print(request_data)
        bckt = request_data['bucket']
        f_name = request_data['name']
        id = request_data['generation'] 
        kube_create_job(bckt, f_name, id)
        return "ok"
    
    # Set logging
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    
    # Setup K8 configs
    config.load_incluster_config()
    def kube_create_job_object(name, container_image, bucket_name, f_name, namespace="pg-ns", container_name="jobcontainer", env_vars={}):
    
        body = client.V1Job(api_version="batch/v1", kind="Job")
        body.metadata = client.V1ObjectMeta(namespace=namespace, name=name)
        body.status = client.V1JobStatus()
    
        template = client.V1PodTemplate()
        template.template = client.V1PodTemplateSpec()
        env_list = [
            client.V1EnvVar(name="POSTGRES_HOST", value=os.getenv("POSTGRES_HOST")),
            client.V1EnvVar(name="DATABASE_NAME", value="app"), 
            client.V1EnvVar(name="COLLECTION_NAME", value="training-docs"), 
            client.V1EnvVar(name="FILE_NAME", value=f_name), 
            client.V1EnvVar(name="BUCKET_NAME", value=bucket_name),
            client.V1EnvVar(name="PASSWORD", value_from=client.V1EnvVarSource(secret_key_ref=client.V1SecretKeySelector(key="password", name="gke-pg-cluster-app"))), 
            client.V1EnvVar(name="USERNAME", value_from=client.V1EnvVarSource(secret_key_ref=client.V1SecretKeySelector(key="username", name="gke-pg-cluster-app"))), 
        ]
    
        container = client.V1Container(name=container_name, image=container_image, image_pull_policy='Always', env=env_list)
        template.template.spec = client.V1PodSpec(containers=[container], restart_policy='Never', service_account='embed-docs-sa')
    
        body.spec = client.V1JobSpec(backoff_limit=3, ttl_seconds_after_finished=60, template=template.template)
        return body
    def kube_test_credentials():
        try: 
            api_response = api_instance.get_api_resources()
            logging.info(api_response)
        except ApiException as e:
            print("Exception when calling API: %s\n" % e)
    
    def kube_create_job(bckt, f_name, id):
        container_image = os.getenv("JOB_IMAGE")
        namespace = os.getenv("JOB_NAMESPACE")
        name = "docs-embedder" + id
        body = kube_create_job_object(name, container_image, bckt, f_name)
        v1=client.BatchV1Api()
        try: 
            v1.create_namespaced_job(namespace, body, pretty=True)
        except ApiException as e:
            print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)
        return
    
    if __name__ == '__main__':
        app.run('0.0.0.0', port=5001, debug=True)
    

###  Weaviate 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from flask import Flask, jsonify
    from flask import request
    import logging
    import sys,os, time
    from kubernetes import client, config, utils
    import kubernetes.client
    from kubernetes.client.rest import ApiException
    
    
    app = Flask(__name__)
    @app.route('/check')
    def message():
        return jsonify({"Message": "Hi there"})
    
    
    @app.route('/', methods=['POST'])
    def bucket():
        request_data = request.get_json()
        print(request_data)
        bckt = request_data['bucket']
        f_name = request_data['name']
        id = request_data['generation'] 
        kube_create_job(bckt, f_name, id)
        return "ok"
    
    # Set logging
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    
    # Setup K8 configs
    config.load_incluster_config()
    def kube_create_job_object(name, container_image, bucket_name, f_name, namespace, container_name="jobcontainer", env_vars={}):
    
        body = client.V1Job(api_version="batch/v1", kind="Job")
        body.metadata = client.V1ObjectMeta(namespace=namespace, name=name)
        body.status = client.V1JobStatus()
    
        template = client.V1PodTemplate()
        template.template = client.V1PodTemplateSpec()
        env_list = [
            client.V1EnvVar(name="WEAVIATE_ENDPOINT", value=os.getenv("WEAVIATE_ENDPOINT")),
            client.V1EnvVar(name="WEAVIATE_GRPC_ENDPOINT", value=os.getenv("WEAVIATE_GRPC_ENDPOINT")),
            client.V1EnvVar(name="FILE_NAME", value=f_name), 
            client.V1EnvVar(name="BUCKET_NAME", value=bucket_name),
            client.V1EnvVar(name="APIKEY", value_from=client.V1EnvVarSource(secret_key_ref=client.V1SecretKeySelector(key="AUTHENTICATION_APIKEY_ALLOWED_KEYS", name="apikeys"))), 
        ]
    
        container = client.V1Container(name=container_name, image=container_image, image_pull_policy='Always', env=env_list)
        template.template.spec = client.V1PodSpec(containers=[container], restart_policy='Never', service_account='embed-docs-sa')
    
        body.spec = client.V1JobSpec(backoff_limit=3, ttl_seconds_after_finished=60, template=template.template)
        return body
    def kube_test_credentials():
        try: 
            api_response = api_instance.get_api_resources()
            logging.info(api_response)
        except ApiException as e:
            print("Exception when calling API: %s\n" % e)
    
    def kube_create_job(bckt, f_name, id):
        container_image = os.getenv("JOB_IMAGE")
        namespace = os.getenv("JOB_NAMESPACE")
        name = "docs-embedder" + id
        body = kube_create_job_object(name, container_image, bckt, f_name, namespace)
        v1=client.BatchV1Api()
        try: 
            v1.create_namespaced_job(namespace, body, pretty=True)
        except ApiException as e:
            print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)
        return
    
    if __name__ == '__main__':
        app.run('0.0.0.0', port=5001, debug=True)
    

### About `embedding-job.py`

This file processes documents and sends them to the vector database.

###  Qdrant 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from langchain_google_vertexai import ChatVertexAI
    from langchain.prompts import ChatPromptTemplate
    from langchain_google_vertexai import VertexAIEmbeddings
    from langchain.memory import ConversationBufferWindowMemory
    from langchain_community.vectorstores import Qdrant
    from qdrant_client import QdrantClient
    import streamlit as st
    import os
    
    vertexAI = ChatVertexAI(model_name=os.getenv("VERTEX_AI_MODEL_NAME", "gemini-2.5-flash-preview-04-17"), streaming=True, convert_system_message_to_human=True)
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant who helps in finding answers to questions using the provided context."),
            ("human", """
            The answer should be based on the text context given in "text_context" and the conversation history given in "conversation_history" along with its Caption: \n
            Base your response on the provided text context and the current conversation history to answer the query.
            Select the most relevant information from the context.
            Generate a draft response using the selected information. Remove duplicate content from the draft response.
            Generate your final response after adjusting it to increase accuracy and relevance.
            Now only show your final response!
            If you do not know the answer or context is not relevant, response with "I don't know".
    
            text_context:
            {context}
    
            conversation_history:
            {history}
    
            query:
            {query}
            """),
        ]
    )
    
    embedding_model = VertexAIEmbeddings("text-embedding-005")
    
    client = QdrantClient(
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("APIKEY"),
    )
    collection_name = os.getenv("COLLECTION_NAME")
    vector_search = Qdrant(client, collection_name, embeddings=embedding_model)
    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])
    
    st.title("🤖 Chatbot")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "ai", "content": "How can I help you?"}]
    if "memory" not in st.session_state:
        st.session_state["memory"] = ConversationBufferWindowMemory(
            memory_key="history",
            ai_prefix="Bob",
            human_prefix="User",
            k=3,
        )
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    if chat_input := st.chat_input():
        with st.chat_message("human"):
            st.write(chat_input)
            st.session_state.messages.append({"role": "human", "content": chat_input})
    
        found_docs = vector_search.similarity_search(chat_input)
        context = format_docs(found_docs)
    
        prompt_value = prompt_template.format_messages(name="Bob", query=chat_input, context=context, history=st.session_state.memory.load_memory_variables({}))
        with st.chat_message("ai"):
            with st.spinner("Typing..."):
                content = ""
                with st.empty():
                    for chunk in vertexAI.stream(prompt_value):
                        content += chunk.content
                        st.write(content)
                st.session_state.messages.append({"role": "ai", "content": content})
    
        st.session_state.memory.save_context({"input": chat_input}, {"output": content})
    
    

###  Elasticsearch 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from langchain_google_vertexai import VertexAIEmbeddings
    from langchain_community.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from elasticsearch import Elasticsearch
    from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import os
    
    bucketname = os.getenv("BUCKET_NAME")
    filename = os.getenv("FILE_NAME")
    
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucketname)
    blob = bucket.blob(filename)
    blob.[download_to_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_to_filename)("/documents/" + filename)
    
    loader = PyPDFLoader("/documents/" + filename)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = loader.load_and_split(text_splitter)
    
    embeddings = VertexAIEmbeddings("text-embedding-005")
    
    client = Elasticsearch(
        [os.getenv("ES_URL")], 
        verify_certs=False, 
        ssl_show_warn=False,
        basic_auth=("elastic", os.getenv("PASSWORD"))
    )
    
    db = ElasticsearchStore.from_documents(
        documents,
        embeddings,
        es_connection=client,
        index_name=os.getenv("INDEX_NAME")
    )
    db.client.indices.refresh(index=os.getenv("INDEX_NAME"))
    
    print(filename + " was successfully embedded") 
    print(f"# of vectors = {len(documents)}")
    
    

###  PGVector 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from langchain_google_vertexai import VertexAIEmbeddings
    from langchain_community.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores.pgvector import PGVector
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import os
    bucketname = os.getenv("BUCKET_NAME")
    filename = os.getenv("FILE_NAME")
    
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucketname)
    blob = bucket.blob(filename)
    blob.[download_to_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_to_filename)("/documents/" + filename)
    
    loader = PyPDFLoader("/documents/" + filename)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = loader.load_and_split(text_splitter)
    for document in documents:
        document.page_content = document.page_content.replace('\x00', '')
    
    embeddings = VertexAIEmbeddings("text-embedding-005")
    
    CONNECTION_STRING = PGVector.connection_string_from_db_params(
        driver="psycopg2",
        host=os.environ.get("POSTGRES_HOST"),
        port=5432,
        database=os.environ.get("DATABASE_NAME"),
        user=os.environ.get("USERNAME"),
        password=os.environ.get("PASSWORD"),
    )
    COLLECTION_NAME = os.environ.get("COLLECTION_NAME")
    
    db = PGVector.from_documents(
        embedding=embeddings,
        documents=documents,
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING,
        use_jsonb=True
    )
    
    print(filename + " was successfully embedded") 
    print(f"# of vectors = {len(documents)}")
    
    

###  Weaviate 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from langchain_google_vertexai import VertexAIEmbeddings
    from langchain_community.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    import weaviate
    from weaviate.connect import ConnectionParams
    from langchain_weaviate.vectorstores import WeaviateVectorStore
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import os
    bucketname = os.getenv("BUCKET_NAME")
    filename = os.getenv("FILE_NAME")
    
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucketname)
    blob = bucket.blob(filename)
    blob.[download_to_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_to_filename)("/documents/" + filename)
    
    loader = PyPDFLoader("/documents/" + filename)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = loader.load_and_split(text_splitter)
    
    embeddings = VertexAIEmbeddings("text-embedding-005")
    
    auth_config = weaviate.auth.AuthApiKey(api_key=os.getenv("APIKEY"))
    client = weaviate.WeaviateClient(
        connection_params=ConnectionParams.from_params(
            http_host=os.getenv("WEAVIATE_ENDPOINT"),
            http_port="80",
            http_secure=False,
            grpc_host=os.getenv("WEAVIATE_GRPC_ENDPOINT"),
            grpc_port="50051",
            grpc_secure=False,
        ),
        auth_client_secret=auth_config
    )
    client.connect()
    if not client.collections.exists("trainingdocs"):
        collection = client.collections.create(name="trainingdocs")
    db = WeaviateVectorStore.from_documents(documents, embeddings, client=client, index_name="trainingdocs")
    
    print(filename + " was successfully embedded") 
    print(f"# of vectors = {len(documents)}")
    
    

### About `chat.py`

This file configures the model to answer questions using only the provided context and previous answers. If the context or conversation history does not match any data, the model returns `I don't know`.

###  Qdrant 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from flask import Flask, jsonify
    from flask import request
    import logging
    import sys,os, time
    from kubernetes import client, config, utils
    import kubernetes.client
    from kubernetes.client.rest import ApiException
    
    
    app = Flask(__name__)
    @app.route('/check')
    def message():
        return jsonify({"Message": "Hi there"})
    
    
    @app.route('/', methods=['POST'])
    def bucket():
        request_data = request.get_json()
        print(request_data)
        bckt = request_data['bucket']
        f_name = request_data['name']
        id = request_data['generation'] 
        kube_create_job(bckt, f_name, id)
        return "ok"
    
    # Set logging
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    
    # Setup K8 configs
    config.load_incluster_config()
    def kube_create_job_object(name, container_image, bucket_name, f_name, namespace="qdrant", container_name="jobcontainer", env_vars={}):
    
        body = client.V1Job(api_version="batch/v1", kind="Job")
        body.metadata = client.V1ObjectMeta(namespace=namespace, name=name)
        body.status = client.V1JobStatus()
    
        template = client.V1PodTemplate()
        template.template = client.V1PodTemplateSpec()
        env_list = [
            client.V1EnvVar(name="QDRANT_URL", value=os.getenv("QDRANT_URL")),
            client.V1EnvVar(name="COLLECTION_NAME", value="training-docs"), 
            client.V1EnvVar(name="FILE_NAME", value=f_name), 
            client.V1EnvVar(name="BUCKET_NAME", value=bucket_name),
            client.V1EnvVar(name="APIKEY", value_from=client.V1EnvVarSource(secret_key_ref=client.V1SecretKeySelector(key="api-key", name="qdrant-database-apikey"))), 
        ]
    
        container = client.V1Container(name=container_name, image=container_image, env=env_list)
        template.template.spec = client.V1PodSpec(containers=[container], restart_policy='Never', service_account='embed-docs-sa')
    
        body.spec = client.V1JobSpec(backoff_limit=3, ttl_seconds_after_finished=60, template=template.template)
        return body
    def kube_test_credentials():
        try: 
            api_response = api_instance.get_api_resources()
            logging.info(api_response)
        except ApiException as e:
            print("Exception when calling API: %s\n" % e)
    
    def kube_create_job(bckt, f_name, id):
        container_image = os.getenv("JOB_IMAGE")
        namespace = os.getenv("JOB_NAMESPACE")
        name = "docs-embedder" + id
        body = kube_create_job_object(name, container_image, bckt, f_name)
        v1=client.BatchV1Api()
        try: 
            v1.create_namespaced_job(namespace, body, pretty=True)
        except ApiException as e:
            print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)
        return
    
    if __name__ == '__main__':
        app.run('0.0.0.0', port=5001, debug=True)
    

###  Elasticsearch 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from langchain_google_vertexai import ChatVertexAI
    from langchain.prompts import ChatPromptTemplate
    from langchain_google_vertexai import VertexAIEmbeddings
    from langchain.memory import ConversationBufferWindowMemory
    from elasticsearch import Elasticsearch
    from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
    import streamlit as st
    import os
    
    vertexAI = ChatVertexAI(model_name=os.getenv("VERTEX_AI_MODEL_NAME", "gemini-2.5-flash-preview-04-17"), streaming=True, convert_system_message_to_human=True)
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant who helps in finding answers to questions using the provided context."),
            ("human", """
            The answer should be based on the text context given in "text_context" and the conversation history given in "conversation_history" along with its Caption: \n
            Base your response on the provided text context and the current conversation history to answer the query.
            Select the most relevant information from the context.
            Generate a draft response using the selected information. Remove duplicate content from the draft response.
            Generate your final response after adjusting it to increase accuracy and relevance.
            Now only show your final response!
            If you do not know the answer or context is not relevant, response with "I don't know".
    
            text_context:
            {context}
    
            conversation_history:
            {history}
    
            query:
            {query}
            """),
        ]
    )
    
    embedding_model = VertexAIEmbeddings("text-embedding-005")
    
    client = Elasticsearch(
        [os.getenv("ES_URL")], 
        verify_certs=False, 
        ssl_show_warn=False,
        basic_auth=("elastic", os.getenv("PASSWORD"))
    )
    vector_search = ElasticsearchStore(
        index_name=os.getenv("INDEX_NAME"),
        es_connection=client,
        embedding=embedding_model
    )
    
    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])
    
    st.title("🤖 Chatbot")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "ai", "content": "How can I help you?"}]
    
    if "memory" not in st.session_state:
        st.session_state["memory"] = ConversationBufferWindowMemory(
            memory_key="history",
            ai_prefix="Bot",
            human_prefix="User",
            k=3,
        )
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    if chat_input := st.chat_input():
        with st.chat_message("human"):
            st.write(chat_input)
            st.session_state.messages.append({"role": "human", "content": chat_input})
    
        found_docs = vector_search.similarity_search(chat_input)
        context = format_docs(found_docs)
    
        prompt_value = prompt_template.format_messages(name="Bot", query=chat_input, context=context, history=st.session_state.memory.load_memory_variables({}))
        with st.chat_message("ai"):
            with st.spinner("Typing..."):
                content = ""
                with st.empty():
                    for chunk in vertexAI.stream(prompt_value):
                        content += chunk.content
                        st.write(content)
                st.session_state.messages.append({"role": "ai", "content": content})
    
        st.session_state.memory.save_context({"input": chat_input}, {"output": content})
    
    

###  PGVector 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from langchain_google_vertexai import ChatVertexAI
    from langchain.prompts import ChatPromptTemplate
    from langchain_google_vertexai import VertexAIEmbeddings
    from langchain.memory import ConversationBufferWindowMemory
    from langchain_community.vectorstores.pgvector import PGVector
    import streamlit as st
    import os
    
    vertexAI = ChatVertexAI(model_name=os.getenv("VERTEX_AI_MODEL_NAME", "gemini-2.5-flash-preview-04-17"), streaming=True, convert_system_message_to_human=True)
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant who helps in finding answers to questions using the provided context."),
            ("human", """
            The answer should be based on the text context given in "text_context" and the conversation history given in "conversation_history" along with its Caption: \n
            Base your response on the provided text context and the current conversation history to answer the query.
            Select the most relevant information from the context.
            Generate a draft response using the selected information. Remove duplicate content from the draft response.
            Generate your final response after adjusting it to increase accuracy and relevance.
            Now only show your final response!
            If you do not know the answer or context is not relevant, response with "I don't know".
    
            text_context:
            {context}
    
            conversation_history:
            {history}
    
            query:
            {query}
            """),
        ]
    )
    
    embedding_model = VertexAIEmbeddings("text-embedding-005")
    
    CONNECTION_STRING = PGVector.connection_string_from_db_params(
        driver="psycopg2",
        host=os.environ.get("POSTGRES_HOST"),
        port=5432,
        database=os.environ.get("DATABASE_NAME"),
        user=os.environ.get("USERNAME"),
        password=os.environ.get("PASSWORD"),
    )
    COLLECTION_NAME = os.environ.get("COLLECTION_NAME"),
    
    vector_search = PGVector(
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING,
        embedding_function=embedding_model,
    )
    
    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])
    
    st.title("🤖 Chatbot")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "ai", "content": "How can I help you?"}]
    
    if "memory" not in st.session_state:
        st.session_state["memory"] = ConversationBufferWindowMemory(
            memory_key="history",
            ai_prefix="Bot",
            human_prefix="User",
            k=3,
        )
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    if chat_input := st.chat_input():
        with st.chat_message("human"):
            st.write(chat_input)
            st.session_state.messages.append({"role": "human", "content": chat_input})
    
        found_docs = vector_search.similarity_search(chat_input)
        context = format_docs(found_docs)
    
        prompt_value = prompt_template.format_messages(name="Bot", query=chat_input, context=context, history=st.session_state.memory.load_memory_variables({}))
        with st.chat_message("ai"):
            with st.spinner("Typing..."):
                content = ""
                with st.empty():
                    for chunk in vertexAI.stream(prompt_value):
                        content += chunk.content
                        st.write(content)
                st.session_state.messages.append({"role": "ai", "content": content})
    
        st.session_state.memory.save_context({"input": chat_input}, {"output": content})
    
    

###  Weaviate 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    from langchain_google_vertexai import ChatVertexAI
    from langchain.prompts import ChatPromptTemplate
    from langchain_google_vertexai import VertexAIEmbeddings
    from langchain.memory import ConversationBufferWindowMemory
    import weaviate
    from weaviate.connect import ConnectionParams
    from langchain_weaviate.vectorstores import WeaviateVectorStore
    import streamlit as st
    import os
    
    vertexAI = ChatVertexAI(model_name=os.getenv("VERTEX_AI_MODEL_NAME", "gemini-2.5-flash-preview-04-17"), streaming=True, convert_system_message_to_human=True)
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant who helps in finding answers to questions using the provided context."),
            ("human", """
            The answer should be based on the text context given in "text_context" and the conversation history given in "conversation_history" along with its Caption: \n
            Base your response on the provided text context and the current conversation history to answer the query.
            Select the most relevant information from the context.
            Generate a draft response using the selected information. Remove duplicate content from the draft response.
            Generate your final response after adjusting it to increase accuracy and relevance.
            Now only show your final response!
            If you do not know the answer or context is not relevant, response with "I don't know".
    
            text_context:
            {context}
    
            conversation_history:
            {history}
    
            query:
            {query}
            """),
        ]
    )
    
    embedding_model = VertexAIEmbeddings("text-embedding-005")
    
    auth_config = weaviate.auth.AuthApiKey(api_key=os.getenv("APIKEY"))
    client = weaviate.WeaviateClient(
        connection_params=ConnectionParams.from_params(
            http_host=os.getenv("WEAVIATE_ENDPOINT"),
            http_port="80",
            http_secure=False,
            grpc_host=os.getenv("WEAVIATE_GRPC_ENDPOINT"),
            grpc_port="50051",
            grpc_secure=False,
        ),
        auth_client_secret=auth_config
    )
    client.connect()
    
    vector_search = WeaviateVectorStore.from_documents([],embedding_model,client=client, index_name="trainingdocs")
    
    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])
    
    st.title("🤖 Chatbot")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "ai", "content": "How can I help you?"}]
    
    if "memory" not in st.session_state:
        st.session_state["memory"] = ConversationBufferWindowMemory(
            memory_key="history",
            ai_prefix="Bot",
            human_prefix="User",
            k=3,
        )
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    if chat_input := st.chat_input():
        with st.chat_message("human"):
            st.write(chat_input)
            st.session_state.messages.append({"role": "human", "content": chat_input})
    
        found_docs = vector_search.similarity_search(chat_input)
        context = format_docs(found_docs)
    
        prompt_value = prompt_template.format_messages(name="Bot", query=chat_input, context=context, history=st.session_state.memory.load_memory_variables({}))
        with st.chat_message("ai"):
            with st.spinner("Typing..."):
                content = ""
                with st.empty():
                    for chunk in vertexAI.stream(prompt_value):
                        content += chunk.content
                        st.write(content)
                st.session_state.messages.append({"role": "ai", "content": content})
    
        st.session_state.memory.save_context({"input": chat_input}, {"output": content})
    
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to avoid billing is to delete the project you created for this tutorial.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

If you deleted the project, your clean up is complete. If you didn't delete the project, proceed to delete the individual resources.

### Delete individual resources

  1. Delete the Artifact Registry repository:
         
         gcloud artifacts repositories delete ${KUBERNETES_CLUSTER_PREFIX}-images \
             --location=${REGION} \
             --async
         

When prompted, type `y`.

  2. Delete the Cloud Storage bucket and the Eventarc trigger:
         
         export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
         terraform -chdir=vector-database/terraform/cloud-storage destroy \
           -var project_id=${PROJECT_ID} \
           -var region=${REGION} \
           -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX} \
           -var db_namespace=${DB_NAMESPACE}
         

When prompted, type `yes`.

Eventarc requires that you have a valid endpoint target both during creation and during deletion.




## What's next

  * Learn about the [best practices for deploying databases on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options).
  * Discover solutions for running [data-intensive workloads with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
