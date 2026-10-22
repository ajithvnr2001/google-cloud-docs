---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install-with-alloydb-ai/
title: Install AlloyDB Omni with AlloyDB AI \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:35.738068+00:00
---

# Install AlloyDB Omni with AlloyDB AI  |  AlloyDB Omni for containers: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install-with-alloydb-ai/

This page documents AlloyDB Omni version **15.5.4** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/overview)



Send feedback 

#  Install AlloyDB Omni with AlloyDB AI Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

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



**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This page shows you how to install AlloyDB Omni and integrate AlloyDB AI in it.

[AlloyDB AI](https://cloud.google.com/alloydb/ai) is a suite of features included with AlloyDB Omni that let you build enterprise generative AI applications. For more information about the ML functionality of AlloyDB, see [Build generative AI applications](https://docs.cloud.google.com/alloydb/docs/vertex-ai).

AlloyDB Omni with AlloyDB AI lets you query remote ML models to work with online predictions and text embeddings generated from ML models. AlloyDB Omni with AlloyDB AI can also process vector embeddings from other content such as an image, for example, if you use the `google_ml.predict_row` interface and do the translation yourself in the query.

Based on where you want to install AlloyDB Omni with AlloyDB AI, select one of the following options:

Single-server Kubernetes GDC air-gapped

## Configure your AlloyDB Omni instance to query remote models

To configure AlloyDB Omni to query remote models, follow these steps:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with Google Cloud.

  2. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating), in JSON format, and download it.

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  3. Store the key in a permanent location on your file system. It resides at this location for the lifetime of your AlloyDB Omni server.

Note its location on your file system; you need it for the next step.

  4. Add Vertex AI Identity and Access Management (IAM) permissions to the appropriate project and service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
                --member="serviceAccount:SERVICE_ACCOUNT_ID" \
                --role="roles/aiplatform.user"

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `SERVICE_ACCOUNT_ID`: the ID of the service account that you created in the previous step. This includes the full `@PROJECT_ID.iam.gserviceaccount.com` suffix—for example, `my-service@my-project.iam.gserviceaccount.com`.




## Install AlloyDB Omni with AlloyDB AI

To install AlloyDB Omni and integrate AlloyDB AI, follow these steps:

  1. Ensure you completed all of the steps listed in Configure your AlloyDB Omni to query cloud-based models.

  2. Make a local copy of the default AlloyDB Omni configuration file:
         
         docker run -i --rm google/alloydbomni:15.5.4 cat /usr/share/postgresql/postgresql.conf.sample > my-postgres.conf

  3. Edit the configuration file copy to add directives for AlloyDB AI integration:
         
         echo "omni_enable_ml_agent_process = 'on'" >> my-postgres.conf
            echo "omni_google_cloud_private_key_file_path = '/etc/postgresql/private-key.json'" >> my-postgres.conf

  4. Adjust the file system permissions of the key and configuration files:
         
         sudo chmod +r my-postgres.conf
            sudo chmod +r KEY_PATH

Replace `KEY_PATH` with the path to the service account private key file on your host file system. This is the key that you created and downloaded earlier in this procedure.

  5. Install the key and configuration files mounted onto the container:
         
         docker run --name CONTAINER_NAME -e POSTGRES_PASSWORD=NEW_PASSWORD -p HOST_PORT:5432 -v "$PWD/my-postgres.conf":/etc/postgresql/postgresql.conf -v "FULL_KEY_PATH":/etc/postgresql/private-key.json -d google/alloydbomni:15.5.4 -c 'config_file=/etc/postgresql/postgresql.conf'

Replace the following:

     * `CONTAINER_NAME`: the name to assign this new simplified AlloyDB Omni installation method container in your host machine's container registry—for example, `my-omni-1`.

     * `NEW_PASSWORD`: the password assigned to new container's `postgres` user after its creation.

     * `HOST_PORT`: the TCP port on the host machine that the container should publish its own port 5432 to. To use the PostgreSQL default port on the host machine as well, specify `5432`.

     * `FULL_KEY_PATH`: the full file system path to the service account private key file on your host system.




## Verify AlloyDB Omni with AlloyDB AI installation

To verify your installation is successful and uses model prediction, enter the following:
    
    
       CREATE EXTENSION google_ml_integration CASCADE;
    
       SELECT array_dims(embedding( 'textembedding-gecko@001', 'AlloyDB AI')::real[]);
       array_dims
    
    

The output looks similar to the following:
    
    
        [1:768]
        (1 row)
    

In the previous query, the `embedding()` call generates embeddings for the input text `AlloyDB AI`. `array_dims` returns the dimensions of the array returned by `embedding()`. Since the pre-registered `textembedding-gecko` model returns an output with 768 dimensions, the output is `[768]`.

## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/run-connect)
  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/manage)
  * [Build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/model-endpoint-overview)
  * [Register and call remote AI models](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/model-endpoint-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
