---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-with-alloydb-ai/
title: Install AlloyDB Omni with AlloyDB AI \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:39.318758+00:00
---

# Install AlloyDB Omni with AlloyDB AI  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-with-alloydb-ai/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Install AlloyDB Omni with AlloyDB AI Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-with-alloydb-ai)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-with-alloydb-ai)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-with-alloydb-ai)

This page shows you how to install AlloyDB Omni and integrate AlloyDB AI. 

[AlloyDB AI](https://cloud.google.com/alloydb/ai) is a suite of features included with AlloyDB Omni that let you build enterprise generative AI applications. For more information about the AI/ML functionality of AlloyDB, see [Build generative AI applications](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/overview-ai).

AlloyDB Omni with AlloyDB AI lets you query remote ML models using the `google_ml_integration` extension to work with online predictions and text embeddings generated from ML models. AlloyDB Omni with AlloyDB AI can also process vector embeddings from other content such as an image, for example, if you use the `google_ml.predict_row` interface and do the translation yourself in the query.

## Set up Google Cloud to query remote models

If you want to query Vertex AI models, then you must configure an AlloyDB Omni service account with Vertex AI before installing AlloyDB Omni.

To set up a service account to query remote models, follow these steps:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with Google Cloud. You grant this service account permissions to access Vertex AI in a later step.

  2. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) and save it in JSON format to the `private-key.json` file, and download it.

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  3. Store the key in a permanent location on your file system. It resides at this location for the lifetime of your AlloyDB Omni server.

Note its location on your file system; you need it for subsequent steps.

  4. Enable the Vertex AI API in your Google Cloud project.
         
         gcloud services enable aiplatform.googleapis.com
         

  5. Add Vertex AI Identity and Access Management (IAM) permissions to the appropriate project and service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role="roles/aiplatform.user"
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project.

     * `SERVICE_ACCOUNT_ID`: ID of the service account that you created in the step one. This includes the full `@PROJECT_ID.iam.gserviceaccount.com` suffix. For example, `my-service@my-project.iam.gserviceaccount.com`.




## Create a secret using the service account key path

To create a `Secret` resource based on the service account key downloaded in the preceding steps, complete the following steps:

  1. Convert the contents of the `private-key.json` file to a base64 format.
         
         cat private-key.json | base64 -w 0

The following is a sample response:
         
         ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAibXktcHJvamVjdC1pZ...[TRUNCATED]...CiAifQo=

  2. Create a `Secret` resource and save it to a file, for example, `secret.yaml`:
         
         ---
         Secret:
           metadata:
             name: SECRET_NAME
           spec:
             type: Opaque
             data:
               private-key.json: BASE64_ENCODED_PRIVATE_KEY
         

Replace the following variables:

     * `SECRET_NAME`: the name of the secret—for example, `ai-secret-dbclustera`.
     * `BASE64_ENCODED_PRIVATE_KEY`: the base64-encoded contents of your service account key file generated in the earlier step.
  3. Apply the `Secret` resource using either of the following methods:

### `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "SECRET_SPECIFICATION"

Replace the following variables:

     * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
     * `SECRET_SPECIFICATION`: the path to the `Secret` resource YAML file that you created.

### Ansible

     1. Create a playbook for your database cluster specifications and save it as an `update.yaml` file.
            
            name: Update resource
            spec:
              - hosts: localhost
                vars:
                  update_action: "update_resource_spec"
                  ansible_user: ANSIBLE_USER
                  ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
                roles:
                  - role: google.alloydbomni_orchestrator.update
            

Replace the following variables:

        * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

        * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

     2. Run your playbook.
            
            ansible-playbook UPDATE_PLAYBOOK -i "DEPLOYMENT_SPEC_PATH" \
              -e resource_spec="SECRET_SPECIFICATION"

Replace the following variables:

        * `UPDATE_PLAYBOOK`: path to the `update.yaml` playbook that you created for your database cluster.

        * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

        * `SECRET_SPECIFICATION`: the path to the `Secret` resource YAML file that you created.




## Configure AlloyDB AI for AlloyDB Omni

After you provision your cluster, complete the following steps to integrate AlloyDB AI:

  1. Complete all of the steps listed in Set up Google Cloud to query remote models.

  2. Create a `Secret` resource using steps in Create a secret using the service account key path.

  3. Update your `DBCluster` resource specification to enable AlloyDB AI.

Under the `googleMLExtension` field, set `enabled` to `true` to let you query remote models. If you want to query Agent Platform models, you must also set `vertexAIKeyRef` to the name of the `Secret` you created.
         
         ---
         DBCluster:
           metadata:
             name: DB_CLUSTER_NAME
           spec:
             primarySpec:
               features:
                 googleMLExtension:
                   enabled: true
                   config:
                     vertexAIKeyRef: secret.metadata.SECRET_NAME
                     vertexAIRegion: VERTEX_AI_REGION
         

Replace the following:

     * `DB_CLUSTER_NAME`: the name of this database cluster.
     * `VERTEX_AI_REGION` (Optional): the Agent Platform regional endpoint that you want to send your request to—for example, `us-west4`. The default value is `us-central1`.
  4. Apply the updated `DBCluster` resource specification using either of the following methods. The orchestrator automatically restarts the database to apply the extension settings.

### `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "DBCLUSTER_SPECIFICATION"

Replace the following variables:

     * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
     * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` resource specification file that you modified.

### Ansible

     1. Create a playbook for your database cluster specifications and save it as an `update.yaml` file.
            
            name: Update resource
            spec:
              - hosts: localhost
                vars:
                  update_action: "update_resource_spec"
                  ansible_user: ANSIBLE_USER
                  ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
                roles:
                  - role: google.alloydbomni_orchestrator.update
            

Replace the following variables:

        * `ANSIBLE_USER`: the OS user that Ansible uses to log into your AlloyDB Omni nodes.

        * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: the private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

     2. Run your playbook.
            
            ansible-playbook UPDATE_PLAYBOOK -i "DEPLOYMENT_SPEC_PATH" \
              -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following variables:

        * `UPDATE_PLAYBOOK`: the path to the `update.yaml` playbook that you created for your database cluster.

        * `DEPLOYMENT_SPEC_PATH`: the path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

        * `DBCLUSTER_SPECIFICATION`: the path to your cluster specifications.




## Connect to your database

Connect to your database cluster. For instructions on how to connect to the orchestrator using `psql`, see [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/run-connect).

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

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/run-connect)
  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/manage)
  * [Register and call remote AI models](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/register-model-endpoint)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
