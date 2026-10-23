---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install-with-alloydb-ai/
title: Install AlloyDB AI in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: 17.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:45.094598+00:00
---

# Install AlloyDB AI in AlloyDB Omni  |  AlloyDB Omni using containers: 17.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install-with-alloydb-ai/

This page documents AlloyDB Omni version **17.7.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/overview)



Send feedback 

#  Install AlloyDB AI in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.7.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install-with-alloydb-ai)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/install-with-alloydb-ai)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/install-with-alloydb-ai)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/install-with-alloydb-ai)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/install-with-alloydb-ai)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/install-with-alloydb-ai)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install-with-alloydb-ai)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install-with-alloydb-ai)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/install-with-alloydb-ai)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/install-with-alloydb-ai)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/install-with-alloydb-ai)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/install-with-alloydb-ai)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/install-with-alloydb-ai)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/install-with-alloydb-ai)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install-with-alloydb-ai)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install-with-alloydb-ai)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/install-with-alloydb-ai)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/install-with-alloydb-ai)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/install-with-alloydb-ai)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-with-alloydb-ai)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/install-with-alloydb-ai)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install-with-alloydb-ai)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install-with-alloydb-ai)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-with-alloydb-ai)

This page shows you how to install AlloyDB Omni and integrate AlloyDB AI. 

[AlloyDB AI](https://cloud.google.com/alloydb/ai) is a suite of features included with AlloyDB Omni that let you build enterprise generative AI applications. For more information about the AI/ML functionality of AlloyDB, see [Build generative AI applications](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/overview-ai).

AlloyDB Omni with AlloyDB AI lets you query remote ML models to work with online predictions and text embeddings generated from ML models. AlloyDB Omni with AlloyDB AI can also process vector embeddings from other content such as an image, for example, if you use the `google_ml.predict_row` interface and do the translation yourself in the query.

## Configure your AlloyDB Omni instance to query remote models

AlloyDB Omni can query remote ML models using the `google_ml_integration` extension.

Optionally, if you want to query Vertex AI models, you must configure AlloyDB Omni service account with Vertex AI before installing AlloyDB Omni.

To configure AlloyDB Omni to query remote models, follow these steps:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with Google Cloud.

  2. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating), in JSON format, and download it. Make a note of the service account key because you use it later in this procedure.

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  3. Copy the service account key that you created to `KEY_PATH`. The key path should be a path on your host accessible, and owned, by the user that will run your AlloyDB Omni container.

  4. Enable the Vertex AI API in your Google Cloud project.
         
         gcloud services enable aiplatform.googleapis.com
         

  5. Add Vertex AI Identity and Access Management (IAM) permissions to the appropriate project and service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role="roles/aiplatform.user"
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project.

     * `SERVICE_ACCOUNT_ID`: ID of the service account that you created in the step one. This includes the full `@PROJECT_ID.iam.gserviceaccount.com` suffix. For example, `my-service@my-project.iam.gserviceaccount.com`.




## Configure AlloyDB AI for AlloyDB Omni

To install AlloyDB Omni and integrate AlloyDB AI, complete the following steps as the root user:

  1. Complete all of the steps listed in Configure your AlloyDB Omni to query cloud-based models.

  2. If an existing container of the same name exists, stop and remove it.

**Caution:** Ensure that the data for your container is mounted on a volume that points to a directory on your host. This keeps your data safe between containers.

### Docker
         
         docker stop CONTAINER_NAME
         docker rm CONTAINER_NAME

### Docker
         
         docker stop CONTAINER_NAME
         docker rm CONTAINER_NAME

### Podman
         
         podman stop CONTAINER_NAME
         podman rm CONTAINER_NAME

### Podman
         
         podman stop CONTAINER_NAME
         podman rm CONTAINER_NAME

Replace the following:

     * `CONTAINER_NAME`: Name to assign your AlloyDB Omni container in your host machine's container registry. For example, `my-omni-1`.
  3. Start a new AlloyDB Omni container mounting the key into the container.

### Docker
         
         docker run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -v "KEY_PATH":/etc/postgresql/private-key.json \
         -p HOST_PORT:5432 \
         --restart=always \
         google/alloydbomni:latest
         

### Docker
         
         docker run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -v "KEY_PATH":/etc/postgresql/private-key.json \
         -p HOST_PORT:5432 \
         --restart=always \
         google/alloydbomni:latest
         

### Podman
         
         podman run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -v "KEY_PATH":/etc/postgresql/private-key.json \
         -p HOST_PORT:5432 \
         --restart=always \
         docker.io/google/alloydbomni:latest
         

### Podman
         
         podman run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -v "KEY_PATH":/etc/postgresql/private-key.json \
         -p HOST_PORT:5432 \
         --restart=always \
         docker.io/google/alloydbomni:latest
         

Replace the following variables:

     * `CONTAINER_NAME`: Name to assign your AlloyDB Omni container in your host machine's container registry. For example, `my-omni-1`.
     * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation. Note that `NEW_PASSWORD` will only set a new password when `DATA_DIR` is a new location.
     * `DATA_DIR`: Host directory path that your data is stored in.
     * `KEY_PATH`: Path for your service account key file.
     * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.
  4. Make the key file readable by the `postgres` user inside the AlloyDB Omni container.

### Docker
         
         docker exec CONTAINER_NAME chown postgres /etc/postgresql/private-key.json
         docker exec CONTAINER_NAME chmod 600 /etc/postgresql/private-key.json

### Docker
         
         docker exec CONTAINER_NAME chown postgres /etc/postgresql/private-key.json
         docker exec CONTAINER_NAME chmod 600 /etc/postgresql/private-key.json

### Podman
         
         podman exec CONTAINER_NAME chown postgres /etc/postgresql/private-key.json
         podman exec CONTAINER_NAME chmod 600 /etc/postgresql/private-key.json

### Podman
         
         podman exec CONTAINER_NAME chown postgres /etc/postgresql/private-key.json
         podman exec CONTAINER_NAME chmod 600 /etc/postgresql/private-key.json

Replace the following variables:

     * `CONTAINER_NAME`: Name to assign your AlloyDB Omni container in your host machine's container registry. For example, `my-omni-1`.
     * `KEY_PATH`: Host path for your service account key file.
  5. Update AlloyDB Omni by adding the following configuration options.

### Docker
         
         docker exec CONTAINER_NAME sh -c "cat << EOF >> /var/lib/postgresql/data/postgresql.conf
         omni_enable_ml_agent_process = 'on'
         omni_google_cloud_private_key_file_path = '/etc/postgresql/private-key.json'
         EOF"
         

### Docker
         
         docker exec CONTAINER_NAME sh -c "cat << EOF >> /var/lib/postgresql/data/postgresql.conf
         omni_enable_ml_agent_process = 'on'
         omni_google_cloud_private_key_file_path = '/etc/postgresql/private-key.json'
         EOF"
         

### Podman
         
         podman exec CONTAINER_NAME sh -c "cat << EOF >> /var/lib/postgresql/data/postgresql.conf
         omni_enable_ml_agent_process = 'on'
         omni_google_cloud_private_key_file_path = '/etc/postgresql/private-key.json'
         EOF"
         

### Podman
         
         podman exec CONTAINER_NAME sh -c "cat << EOF >> /var/lib/postgresql/data/postgresql.conf
         omni_enable_ml_agent_process = 'on'
         omni_google_cloud_private_key_file_path = '/etc/postgresql/private-key.json'
         EOF"
         

Replace the following variables:

     * `CONTAINER_NAME`: Name to assign your AlloyDB Omni container in your host machine's container registry. For example, `my-omni-1`.
  6. Restart the AlloyDB Omni container.

### Docker
         
         docker restart CONTAINER_NAME
         

### Docker
         
         docker restart CONTAINER_NAME
         

### Podman
         
         podman restart CONTAINER_NAME
         

### Podman
         
         podman restart CONTAINER_NAME
         

Replace the following variable:

     * `CONTAINER_NAME`: Name to assign your AlloyDB Omni container in your host machine's container registry. For example, `my-omni-1`.



## Connect using the containerized `psql`

To connect to the AlloyDB Omni database server using its own containerized copy of `psql`, run the following command:

### Docker
    
    
    docker exec -it CONTAINER_NAME psql -U postgres
    

### Docker
    
    
    docker exec -it CONTAINER_NAME psql -U postgres
    

### Podman
    
    
    podman exec -it CONTAINER_NAME psql -U postgres
    

### Podman
    
    
    podman exec -it CONTAINER_NAME psql -U postgres
    

Replace the following variable:

  * `CONTAINER_NAME`: Name to assign your AlloyDB Omni container in your host machine's container registry. For example, `my-omni-1`.



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

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/run-connect)
  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/manage)
  * [Build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/overview-ai)
  * [Register and call remote AI models](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/register-model-endpoint)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
