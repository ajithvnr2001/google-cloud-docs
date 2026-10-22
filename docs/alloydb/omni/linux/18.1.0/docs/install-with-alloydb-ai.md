---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-with-alloydb-ai/
title: Install AlloyDB Omni with AlloyDB AI \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:04.260195+00:00
---

# Install AlloyDB Omni with AlloyDB AI  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-with-alloydb-ai/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Install AlloyDB Omni with AlloyDB AI Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/install-with-alloydb-ai)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/install-with-alloydb-ai)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/install-with-alloydb-ai)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/install-with-alloydb-ai)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-with-alloydb-ai)

This page shows you how to install AlloyDB Omni and integrate AlloyDB AI. 

[AlloyDB AI](https://cloud.google.com/alloydb/ai) is a suite of features included with AlloyDB Omni that let you build enterprise generative AI applications. For more information about the AI/ML functionality of AlloyDB, see [Build generative AI applications](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/overview-ai).

AlloyDB Omni with AlloyDB AI lets you query remote ML models using the `google_ml_integration` extension to work with online predictions and text embeddings generated from ML models. AlloyDB Omni with AlloyDB AI can also process vector embeddings from other content such as an image, for example, if you use the `google_ml.predict_row` interface and do the translation yourself in the query.

## Set up Google Cloud to query remote models

If you want to query Vertex AI models, then you must configure an AlloyDB Omni service account with Vertex AI before installing AlloyDB Omni.

To set up a service account to query remote models, follow these steps:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with Google Cloud. You grant this service account permissions to access Vertex AI in a later step.

  2. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) and save it in JSON format to the `private-key.json` file, and download it.

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  3. Copy the service account key that you created to KEY_PATH. The key path should be a path on your host accessible, and owned, by the user that will run AlloyDB Omni. 

  4. Enable the Vertex AI API in your Google Cloud project.
         
         gcloud services enable aiplatform.googleapis.com
         

  5. Add Vertex AI Identity and Access Management (IAM) permissions to the appropriate project and service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role="roles/aiplatform.user"
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project.

     * `SERVICE_ACCOUNT_ID`: ID of the service account that you created in the step one. This includes the full `@PROJECT_ID.iam.gserviceaccount.com` suffix. For example, `my-service@my-project.iam.gserviceaccount.com`.



  1. Install the AlloyDB Omni RPM package.



## Configure AlloyDB AI for AlloyDB Omni

After you install the AlloyDB Omni RPM package, complete the following steps to integrate AlloyDB AI:

  1. Complete all of the steps listed in Set up Google Cloud to query remote models.

  2. Move the service account key to AlloyDB Omni's data directory.
         
         sudo mv KEY_PATH DATA_DIR/private-key.json

Replace the following variables:

     * `KEY_PATH`: Path for your service account key file.
     * `DATA_DIR`: Host directory path that your data is stored in.
  3. Set the service account key's owner to `postgres` and its permissions to `600`.
         
         sudo chown postgres:postgres DATA_DIR/private-key.json
         sudo chmod 600 DATA_DIR/private-key.json

  4. Update the AlloyDB Omni configuration by adding the following options to the `postgresql.conf` file:
         
         sudo tee -a DATA_DIR/postgresql.conf << EOF
         omni_enable_ml_agent_process = 'on'
         omni_google_cloud_private_key_file_path = 'DATA_DIR/private-key.json'
         EOF

  5. Restart the AlloyDB Omni service.
         
         sudo systemctl restart alloydbomni18




## Connect using `psql`

To connect to the AlloyDB Omni database, run the following command:
    
    
    sudo -u postgres /usr/lib/postgresql/18/bin/psql -U postgres

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

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/run-connect)
  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage)
  * [Register and call remote AI models](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/register-model-endpoint)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
