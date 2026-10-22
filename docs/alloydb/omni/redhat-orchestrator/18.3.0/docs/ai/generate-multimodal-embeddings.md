---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/generate-multimodal-embeddings/
title: Generate multimodal embeddings \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:28.552119+00:00
---

# Generate multimodal embeddings  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/generate-multimodal-embeddings/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Generate multimodal embeddings Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/ai/generate-multimodal-embeddings)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/ai/generate-multimodal-embeddings)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/generate-multimodal-embeddings)

**Note:** This experimental launch is a Pre-GA offering.

You can generate multimodal embeddings in AlloyDB Omni using the supported Vertex AI multimodal model, `multimodalembedding@001`.

You can use the Vertex AI multimodal embedding models referred to in [Supported models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings#supported-models).

This page assumes that you're familiar with AlloyDB Omni and [generative AI concepts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings#supported-models). For more information, see [What are embeddings](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/work-with-embeddings#what-are-embeddings).

## Before you begin

Before you use multimodal embeddings, do the following:

  1. [Configure user access to Vertex AI models](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-with-alloydb-ai#with-cloud).
  2. Verify that the latest version of `google_ml_integration` is installed. 
     1. To check the installed version, run the following command:
            
            SELECT extversion FROM pg_extension WHERE extname = 'google_ml_integration';
            extversion
            ------------
            1.5.2
            (1 row)

     2. If the extension isn't installed or if the installed version is earlier than 1.5.2, update the extension.
            
            CREATE EXTENSION IF NOT EXISTS google_ml_integration;
            ALTER EXTENSION google_ml_integration UPDATE;

If you experience issues when you run the preceding commands, or if the extension isn't updated to version 1.5.2 after you run the preceding commands, contact [Google Cloud support](https://cloud.google.com/support).

  3. To use the AlloyDB AI query engine functionality, set the `google_ml_integration.enable_ai_query_engine` flag to `on`.

  4. Access data in Cloud Storage to generate multimodal embeddings.




### Access data in Cloud Storage to generate multimodal embeddings

  * To generate multimodal embeddings, refer to content in Cloud Storage using a `gs://` URI.
  * Access Cloud Storage content through your current project's Vertex AI service agent. By default, the Vertex AI service agent already has permission to access the bucket in the same project. For more information, see [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent).
  * To access data in a Cloud Storage bucket in another Google Cloud project, run the following gcloud CLI command to grant the [Storage Object Viewer role (`roles/storage.objectViewer`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the Vertex AI service agent of your Google Cloud project.
        
        gcloud projects add-iam-policy-binding <ANOTHER_PROJECT_ID> \
        --member="serviceAccount:service-<PROJECT_ID>@gcp-sa-aiplatform.iam.gserviceaccount.com" \
        --role="roles/storage.objectViewer"

For more information, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).




To generate multimodal embeddings, select one of the following schemas.

ai schema google_ml schema

## Generate multimodal embeddings

To generate text embeddings for a `multimodalembedding@001` model endpoint, run the following statement:
    
    
    SELECT
      ai.text_embedding(
        model_id => 'multimodalembedding@001',
        content => 'TEXT');
    

Replace `TEXT` with the text to generate the embedding for.

To generate image embeddings for a registered `multimodalembedding@001` model endpoint where the image mimetype is default `image/jpeg`, run the following statement:
    
    
    SELECT
      ai.image_embedding(
        model_id => 'multimodalembedding@001',
        image => 'IMAGE_PATH_OR_TEXT',
        mimetype => 'MIMETYPE');
    

Replace the following:

  * `IMAGE_PATH_OR_TEXT` with the Cloud Storage URI of the image, for example, `gs://my-bucket/embeddings/flowers.jpeg`, or the base64 string of the image.

  * `MIMETYPE` with the mimetype of the image, for example, `image/jpeg`. For the full list of supported mimetypes, see the [Multimodal embeddings API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/multimodal-embeddings-api#image).




To generate video embeddings for a registered `multimodalembedding@001` model endpoint, run the following statement:
    
    
    SELECT
      ai.video_embedding(
        model_id => 'multimodalembedding@001',
        video => 'VIDEO_URI');
    

Replace `VIDEO_URI` with the Cloud Storage URI of the target video, for example, `gs://my-bucket/embeddings/supermarket-video.mp4`, or the base64 string of the video. These are two-dimensional arrays that can be accessed as `my_array[0][5]` like syntax. For more information, see [Arrays](https://www.postgresql.org/docs/17/arrays.html).

## What's next

  * [Register a model endpoint with model endpoint management](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/register-model-endpoint).

  * [Query using AI powered SQL operators](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/evaluate-semantic-queries-ai-operators).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
