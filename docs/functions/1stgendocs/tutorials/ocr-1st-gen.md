---
url: https://docs.cloud.google.com/functions/1stgendocs/tutorials/ocr-1st-gen/
title: Optical Character Recognition (OCR) Tutorial (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:37.229102+00:00
---

# Optical Character Recognition (OCR) Tutorial (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/tutorials/ocr-1st-gen/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback 

#  Optical Character Recognition (OCR) Tutorial (1st gen) Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to perform optical character recognition (OCR) on Google Cloud. This tutorial demonstrates how to upload image files to [Cloud Storage](https://docs.cloud.google.com/storage), extract text from the images using the [Cloud Vision API](https://docs.cloud.google.com/vision), translate the text using the [Google Cloud Translation API](https://docs.cloud.google.com/translate), and save your translations back to Cloud Storage. [Pub/Sub](https://docs.cloud.google.com/pubsub) is used to queue various tasks and trigger the right Cloud Run functions to carry them out.

For more information about sending a text detection (OCR) request, see [Detect text in images](https://docs.cloud.google.com/vision/docs/ocr), [Detect handwriting in images](https://docs.cloud.google.com/vision/docs/handwriting), or [Detect text in files (PDF/TIFF)](https://docs.cloud.google.com/vision/docs/pdf).

## Objectives

  * Write and deploy several [Background Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#background-functions).
  * Upload images to Cloud Storage.
  * Extract, translate and save text contained in uploaded images.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud Run functions
  * Pub/Sub
  * Cloud Storage
  * Cloud Translation API
  * Cloud Vision



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Functions, Cloud Build, Cloud Pub/Sub, Cloud Storage, Cloud Translation, and Cloud Vision APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions,cloudbuild.googleapis.com,pubsub,storage_api,translate,vision.googleapis.com&redirect=https%3A//cloud.google.com/functions/1stgendocs/tutorials/ocr-1st-gen)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Functions, Cloud Build, Cloud Pub/Sub, Cloud Storage, Cloud Translation, and Cloud Vision APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions,cloudbuild.googleapis.com,pubsub,storage_api,translate,vision.googleapis.com&redirect=https%3A//cloud.google.com/functions/1stgendocs/tutorials/ocr-1st-gen)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

If you already have the gcloud CLI installed, update it by running the following command:
    
    gcloud components update

  14. Prepare your development environment. 

###  Node.js 

[ Go to the Node.js setup guide ](https://docs.cloud.google.com/nodejs/docs/setup)

###  Python 

[ Go to the Python setup guide ](https://docs.cloud.google.com/python/docs/setup)

###  Go 

[ Go to the Go setup guide ](https://docs.cloud.google.com/go/docs/setup)

###  Java 

[ Go to the Java setup guide ](https://docs.cloud.google.com/java/docs/setup)




## Visualizing the flow of data

The flow of data in the OCR tutorial application involves several steps:

  1. An image that contains text in any language is uploaded to Cloud Storage.
  2. A Cloud Run function is triggered, which uses the Vision API to extract the text and detect the source language.
  3. The text is queued for translation by [publishing a message to a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/publisher). A translation is queued for each target language different from the source language.
  4. If a target language matches the source language, the translation queue is skipped, and text is sent to the result queue, which is a different Pub/Sub topic.
  5. A Cloud Run function uses the Translation API to translate the text in the translation queue. The translated result is sent to the result queue.
  6. Another Cloud Run function saves the translated text from the result queue to Cloud Storage.
  7. The results are found in Cloud Storage as text files for each translation.



It may help to visualize the steps:

![](https://docs.cloud.google.com/static/functions/img/gcf-ocr.svg)

## Preparing the application

  1. Create a Cloud Storage bucket to upload images to, where `YOUR_IMAGE_BUCKET_NAME` is a globally unique bucket name:
         
         gcloud storage buckets create gs://YOUR_IMAGE_BUCKET_NAME

  2. Create a Cloud Storage bucket to save text translations to, where `YOUR_RESULT_BUCKET_NAME` is a globally unique bucket name:
         
         gcloud storage buckets create gs://YOUR_RESULT_BUCKET_NAME

  3. Create a Pub/Sub topic to publish translation requests to, where `YOUR_TRANSLATE_TOPIC_NAME` is the name of your translation request topic:
         
         gcloud pubsub topics create YOUR_TRANSLATE_TOPIC_NAME

  4. Create a Pub/Sub topic to publish finished translation results to, where `YOUR_RESULT_TOPIC_NAME` is the name of your translation result topic:
         
         gcloud pubsub topics create YOUR_RESULT_TOPIC_NAME

  5. Clone the sample app repository to your local machine:

###  Node.js 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/main.zip) as a zip file and extract it. 

###  Python 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/main.zip) as a zip file and extract it. 

###  Go 
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/golang-samples/archive/main.zip) as a zip file and extract it. 

###  Java 
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/java-docs-samples/archive/main.zip) as a zip file and extract it. 

  6. Change to the directory that contains the Cloud Run functions sample code:

###  Node.js 
         
         cd nodejs-docs-samples/functions/ocr/app/

###  Python 
         
         cd python-docs-samples/functions/ocr/app/

###  Go 
         
         cd golang-samples/functions/ocr/app/

###  Java 
         
         cd java-docs-samples/functions/ocr/ocr-process-image/




## Understanding the code

### Importing dependencies

The application must import several dependencies in order to communicate with Google Cloud Platform services:

###  Node.js 
    
    
    // Get a reference to the Pub/Sub component
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    // Get a reference to the Cloud Storage component
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Get a reference to the Cloud Vision API component
    const Vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    const vision = new Vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    // Get a reference to the Translate API component
    const {Translate} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)').v2;
    const translate = new [Translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.translate.html)();
    

###  Python 
    
    
    import base64
    import json
    import os
    from typing import Dict, TypeVar
    
    from google.cloud import pubsub_v1
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud import translate_v2 as translate
    from google.cloud import vision
    
    vision_client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    translate_client = translate.Client()
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    project_id = os.environ["GCP_PROJECT"]

###  Go 
    
    
    // Package ocr contains Go samples for creating OCR
    // (Optical Character Recognition) Cloud functions.
    package ocr
    
    import (
    	"context"
    	"fmt"
    	"os"
    	"strings"
    	"time"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/storage"
    	"cloud.google.com/go/translate"
    	vision "cloud.google.com/go/vision/apiv1"
    	"golang.org/x/text/language"
    )
    
    type ocrMessage struct {
    	Text     string       `json:"text"`
    	FileName string       `json:"fileName"`
    	Lang     language.Tag `json:"lang"`
    	SrcLang  language.Tag `json:"srcLang"`
    }
    
    // GCSEvent is the payload of a GCS event.
    type GCSEvent struct {
    	Bucket         string    `json:"bucket"`
    	Name           string    `json:"name"`
    	Metageneration string    `json:"metageneration"`
    	ResourceState  string    `json:"resourceState"`
    	TimeCreated    time.Time `json:"timeCreated"`
    	Updated        time.Time `json:"updated"`
    }
    
    // PubSubMessage is the payload of a Pub/Sub event.
    // See the documentation for more details:
    // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
    type [PubSubMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/apiv1/pubsublitepb.html#cloud_google_com_go_pubsublite_apiv1_pubsublitepb_PubSubMessage) struct {
    	Data []byte `json:"data"`
    }
    
    var (
    	visionClient    *vision.[ImageAnnotatorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_ImageAnnotatorClient)
    	translateClient *translate.Client
    	pubsubClient    *pubsub.Client
    	storageClient   *storage.Client
    
    	projectID      string
    	resultBucket   string
    	resultTopic    string
    	toLang         []string
    	translateTopic string
    )
    
    func setup(ctx context.Context) error {
    	projectID = os.Getenv("GCP_PROJECT")
    	resultBucket = os.Getenv("RESULT_BUCKET")
    	resultTopic = os.Getenv("RESULT_TOPIC")
    	toLang = strings.Split(os.Getenv("TO_LANG"), ",")
    	translateTopic = os.Getenv("TRANSLATE_TOPIC")
    
    	var err error // Prevent shadowing clients with :=.
    
    	if visionClient == nil {
    		visionClient, err = vision.[NewImageAnnotatorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_ImageAnnotatorClient_NewImageAnnotatorClient)(ctx)
    		if err != nil {
    			return fmt.Errorf("vision.NewImageAnnotatorClient: %w", err)
    		}
    	}
    
    	if translateClient == nil {
    		translateClient, err = translate.NewClient(ctx)
    		if err != nil {
    			return fmt.Errorf("translate.NewClient: %w", err)
    		}
    	}
    
    	if pubsubClient == nil {
    		pubsubClient, err = pubsub.NewClient(ctx, projectID)
    		if err != nil {
    			return fmt.Errorf("translate.NewClient: %w", err)
    		}
    	}
    
    	if storageClient == nil {
    		storageClient, err = storage.NewClient(ctx)
    		if err != nil {
    			return fmt.Errorf("storage.NewClient: %w", err)
    		}
    	}
    	return nil
    }
    

###  Java 
    
    
    public class OcrProcessImage implements BackgroundFunction<GcsEvent> {
      // TODO<developer> set these environment variables
      private static final String PROJECT_ID = System.getenv("GCP_PROJECT");
      private static final String TRANSLATE_TOPIC_NAME = System.getenv("TRANSLATE_TOPIC");
      private static final String[] TO_LANGS = System.getenv("TO_LANG").split(",");
    
      private static final Logger logger = Logger.getLogger(OcrProcessImage.class.getName());
      private static final String LOCATION_NAME = LocationName.of(PROJECT_ID, "global").toString();
      private Publisher publisher;
    
      public OcrProcessImage() throws IOException {
        publisher = Publisher.newBuilder(
            ProjectTopicName.of(PROJECT_ID, TRANSLATE_TOPIC_NAME)).build();
      }
    }

### Processing images

The following function reads an uploaded image file from Cloud Storage and calls a function to detect whether the image contains text:

###  Node.js 
    
    
    /**
     * This function is exported by index.js, and is executed when
     * a file is uploaded to the Cloud Storage bucket you created
     * for uploading images.
     *
     * @param {object} event A Google Cloud Storage File object.
     */
    exports.processImage = async event => {
      const {bucket, name} = event;
    
      if (!bucket) {
        throw new Error(
          'Bucket not provided. Make sure you have a "bucket" property in your request'
        );
      }
      if (!name) {
        throw new Error(
          'Filename not provided. Make sure you have a "name" property in your request'
        );
      }
    
      await detectText(bucket, name);
      console.log(`File ${name} processed.`);
    };

###  Python 
    
    
    def process_image(file_info: dict, context: dict) -> None:
        """Cloud Function triggered by Cloud Storage when a file is changed.
    
        Args:
            file_info: Metadata of the changed file, provided by the
                triggering Cloud Storage event.
            context: a dictionary containing metadata about the event.
    
        Returns:
            None; the output is written to stdout and Cloud Logging.
        """
        bucket = validate_message(file_info, "bucket")
        name = validate_message(file_info, "name")
    
        detect_text(bucket, name)
    
        print(f"File '{file_info['name']}' processed.")

###  Go 
    
    
    package ocr
    
    import (
    	"context"
    	"fmt"
    	"log"
    )
    
    // ProcessImage is executed when a file is uploaded to the Cloud Storage bucket you
    // created for uploading images. It runs detectText, which processes the image for text.
    func ProcessImage(ctx context.Context, event GCSEvent) error {
    	if err := setup(ctx); err != nil {
    		return fmt.Errorf("ProcessImage: %w", err)
    	}
    	if event.Bucket == "" {
    		return fmt.Errorf("empty file.Bucket")
    	}
    	if event.Name == "" {
    		return fmt.Errorf("empty file.Name")
    	}
    	if err := detectText(ctx, event.Bucket, event.Name); err != nil {
    		return fmt.Errorf("detectText: %w", err)
    	}
    	log.Printf("File %s processed.", event.Name)
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.cloud.translate.v3.[DetectLanguageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectLanguageRequest.html);
    import com.google.cloud.translate.v3.[DetectLanguageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectLanguageResponse.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.LocationName.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import functions.eventpojos.GcsEvent;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.logging.Level;
    import java.util.logging.Logger;
    
      @Override
      public void accept(GcsEvent gcsEvent, Context context) {
    
        // Validate parameters
        String bucket = gcsEvent.getBucket();
        if (bucket == null) {
          throw new IllegalArgumentException("Missing bucket parameter");
        }
        String filename = gcsEvent.getName();
        if (filename == null) {
          throw new IllegalArgumentException("Missing name parameter");
        }
    
        detectText(bucket, filename);
      }
    }

The following function extracts text from the image using the Vision API and queues the text for translation:

###  Node.js 
    
    
    /**
     * Detects the text in an image using the Google Vision API.
     *
     * @param {string} bucketName Cloud Storage bucket name.
     * @param {string} filename Cloud Storage file name.
     * @returns {Promise}
     */
    const detectText = async (bucketName, filename) => {
      console.log(`Looking for text in image ${filename}`);
      const [textDetections] = await vision.textDetection(
        `gs://${bucketName}/${filename}`
      );
      const [annotation] = textDetections.textAnnotations;
      const text = annotation ? annotation.description.trim() : '';
      console.log('Extracted text from image:', text);
    
      let [translateDetection] = await translate.detect(text);
      if (Array.isArray(translateDetection)) {
        [translateDetection] = translateDetection;
      }
      console.log(
        `Detected language "${translateDetection.language}" for ${filename}`
      );
    
      // Submit a message to the bus for each language we're going to translate to
      const TO_LANGS = process.env.TO_LANG.split(',');
      const topicName = process.env.TRANSLATE_TOPIC;
    
      const tasks = TO_LANGS.map(lang => {
        const messageData = {
          text: text,
          filename: filename,
          lang: lang,
        };
    
        // Helper function that publishes translation result to a Pub/Sub topic
        // For more information on publishing Pub/Sub messages, see this page:
        //   https://cloud.google.com/pubsub/docs/publisher
        return publishResult(topicName, messageData);
      });
    
      return Promise.all(tasks);
    };

###  Python 
    
    
    def detect_text(bucket: str, filename: str) -> None:
        """
        Extract the text from an image uploaded to Cloud Storage.
    
        Extract the text from an image uploaded to Cloud Storage, then
        publish messages requesting subscribing services translate the text
        to each target language and save the result.
    
        Args:
            bucket: name of GCS bucket in which the file is stored.
            filename: name of the file to be read.
    
        Returns:
            None; the output is written to stdout and Cloud Logging.
        """
        print("Looking for text in image {}".format(filename))
    
        futures = []
    
        image = vision.Image(
            source=vision.ImageSource(gcs_image_uri=f"gs://{bucket}/{filename}")
        )
        text_detection_response = vision_client.text_detection(image=image)
        annotations = text_detection_response.text_annotations
    
        if len(annotations) > 0:
            text = annotations[0].description
        else:
            text = ""
    
        print(f"Extracted text {text} from image ({len(text)} chars).")
    
        detect_language_response = translate_client.detect_language(text)
        src_lang = detect_language_response["language"]
        print(f"Detected language {src_lang} for text {text}.")
    
        # Submit a message to the bus for each target language
        to_langs = os.environ["TO_LANG"].split(",")
        for target_lang in to_langs:
            topic_name = os.environ["TRANSLATE_TOPIC"]
            if src_lang == target_lang or src_lang == "und":
                topic_name = os.environ["RESULT_TOPIC"]
            message = {
                "text": text,
                "filename": filename,
                "lang": target_lang,
                "src_lang": src_lang,
            }
            message_data = json.dumps(message).encode("utf-8")
            topic_path = publisher.topic_path(project_id, topic_name)
            future = publisher.publish(topic_path, data=message_data)
            futures.append(future)
        for future in futures:
            future.result()

###  Go 
    
    
    package ocr
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    	"golang.org/x/text/language"
    )
    
    // detectText detects the text in an image using the Google Vision API.
    func detectText(ctx context.Context, bucketName, fileName string) error {
    	log.Printf("Looking for text in image %v", fileName)
    	maxResults := 1
    	image := &visionpb.[Image](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Image){
    		Source: &visionpb.[ImageSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ImageSource){
    			GcsImageUri: fmt.Sprintf("gs://%s/%s", bucketName, fileName),
    		},
    	}
    	annotations, err := visionClient.DetectTexts(ctx, image, &visionpb.[ImageContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ImageContext){}, maxResults)
    	if err != nil {
    		return fmt.Errorf("DetectTexts: %w", err)
    	}
    	text := ""
    	if len(annotations) > 0 {
    		text = annotations[0].Description
    	}
    	if len(annotations) == 0 || len(text) == 0 {
    		log.Printf("No text detected in image %q. Returning early.", fileName)
    		return nil
    	}
    	log.Printf("Extracted text %q from image (%d chars).", text, len(text))
    
    	detectResponse, err := translateClient.DetectLanguage(ctx, []string{text})
    	if err != nil {
    		return fmt.Errorf("DetectLanguage: %w", err)
    	}
    	if len(detectResponse) == 0 || len(detectResponse[0]) == 0 {
    		return fmt.Errorf("DetectLanguage gave empty response")
    	}
    	srcLang := detectResponse[0][0].Language.String()
    	log.Printf("Detected language %q for text %q.", srcLang, text)
    
    	// Submit a message to the bus for each target language
    	for _, targetLang := range toLang {
    		topicName := translateTopic
    		if srcLang == targetLang || srcLang == "und" { // detection returns "und" for undefined language
    			topicName = resultTopic
    		}
    		targetTag, err := language.Parse(targetLang)
    		if err != nil {
    			return fmt.Errorf("language.Parse: %w", err)
    		}
    		srcTag, err := language.Parse(srcLang)
    		if err != nil {
    			return fmt.Errorf("language.Parse: %w", err)
    		}
    		message, err := json.Marshal(ocrMessage{
    			Text:     text,
    			FileName: fileName,
    			Lang:     targetTag,
    			SrcLang:  srcTag,
    		})
    		if err != nil {
    			return fmt.Errorf("json.Marshal: %w", err)
    		}
    		topic := pubsubClient.Topic(topicName)
    		ok, err := topic.Exists(ctx)
    		if err != nil {
    			return fmt.Errorf("Exists: %w", err)
    		}
    		if !ok {
    			topic, err = pubsubClient.CreateTopic(ctx, topicName)
    			if err != nil {
    				return fmt.Errorf("CreateTopic: %w", err)
    			}
    		}
    		msg := &pubsub.Message{
    			Data: []byte(message),
    		}
    		if _, err = topic.Publish(ctx, msg).Get(ctx); err != nil {
    			return fmt.Errorf("Get: %w", err)
    		}
    	}
    	return nil
    }
    

###  Java 
    
    
    private void detectText(String bucket, String filename) {
      logger.info("Looking for text in image " + filename);
    
      List<AnnotateImageRequest> visionRequests = new ArrayList<>();
      String gcsPath = String.format("gs://%s/%s", bucket, filename);
    
      ImageSource imgSource = ImageSource.newBuilder().setGcsImageUri(gcsPath).build();
      Image img = Image.newBuilder().setSource(imgSource).build();
    
      Feature textFeature = Feature.newBuilder().setType(Feature.Type.TEXT_DETECTION).build();
      AnnotateImageRequest visionRequest =
          AnnotateImageRequest.newBuilder().addFeatures(textFeature).setImage(img).build();
      visionRequests.add(visionRequest);
    
      // Detect text in an image using the Cloud Vision API
      AnnotateImageResponse visionResponse;
      try (ImageAnnotatorClient client = ImageAnnotatorClient.create()) {
        visionResponse = client.batchAnnotateImages(visionRequests).getResponses(0);
        if (visionResponse == null || !visionResponse.hasFullTextAnnotation()) {
          logger.info(String.format("Image %s contains no text", filename));
          return;
        }
    
        if (visionResponse.hasError()) {
          // Log error
          logger.log(
              Level.SEVERE, "Error in vision API call: " + visionResponse.getError().getMessage());
          return;
        }
      } catch (IOException e) {
        // Log error (since IOException cannot be thrown by a Cloud Function)
        logger.log(Level.SEVERE, "Error detecting text: " + e.getMessage(), e);
        return;
      }
    
      String text = visionResponse.getFullTextAnnotation().getText();
      logger.info("Extracted text from image: " + text);
    
      // Detect language using the Cloud Translation API
      DetectLanguageRequest languageRequest =
          DetectLanguageRequest.newBuilder()
              .setParent(LOCATION_NAME)
              .setMimeType("text/plain")
              .setContent(text)
              .build();
      DetectLanguageResponse languageResponse;
      try (TranslationServiceClient client = TranslationServiceClient.create()) {
        languageResponse = client.detectLanguage(languageRequest);
      } catch (IOException e) {
        // Log error (since IOException cannot be thrown by a function)
        logger.log(Level.SEVERE, "Error detecting language: " + e.getMessage(), e);
        return;
      }
    
      if (languageResponse.getLanguagesCount() == 0) {
        logger.info("No languages were detected for text: " + text);
        return;
      }
    
      String languageCode = languageResponse.getLanguages(0).getLanguageCode();
      logger.info(String.format("Detected language %s for file %s", languageCode, filename));
    
      // Send a Pub/Sub translation request for every language we're going to translate to
      for (String targetLanguage : TO_LANGS) {
        logger.info("Sending translation request for language " + targetLanguage);
        OcrTranslateApiMessage message = new OcrTranslateApiMessage(text, filename, targetLanguage);
        ByteString byteStr = ByteString.copyFrom(message.toPubsubData());
        PubsubMessage pubsubApiMessage = PubsubMessage.newBuilder().setData(byteStr).build();
        try {
          publisher.publish(pubsubApiMessage).get();
        } catch (InterruptedException | ExecutionException e) {
          // Log error
          logger.log(Level.SEVERE, "Error publishing translation request: " + e.getMessage(), e);
          return;
        }
      }
    }

### Translating text

The following function translates the extracted text and queues the translated text to be saved back to Cloud Storage:

###  Node.js 
    
    
    /**
     * This function is exported by index.js, and is executed when
     * a message is published to the Cloud Pub/Sub topic specified
     * by the TRANSLATE_TOPIC environment variable. The function
     * translates text using the Google Translate API.
     *
     * @param {object} event The Cloud Pub/Sub Message object.
     * @param {string} {messageObject}.data The "data" property of the Cloud Pub/Sub
     * Message. This property will be a base64-encoded string that you must decode.
     */
    exports.translateText = async event => {
      const pubsubData = event.data;
      const jsonStr = Buffer.from(pubsubData, 'base64').toString();
      const {text, filename, lang} = JSON.parse(jsonStr);
    
      if (!text) {
        throw new Error(
          'Text not provided. Make sure you have a "text" property in your request'
        );
      }
      if (!filename) {
        throw new Error(
          'Filename not provided. Make sure you have a "filename" property in your request'
        );
      }
      if (!lang) {
        throw new Error(
          'Language not provided. Make sure you have a "lang" property in your request'
        );
      }
    
      console.log(`Translating text into ${lang}`);
      const [translation] = await translate.translate(text, lang);
    
      console.log('Translated text:', translation);
    
      const messageData = {
        text: translation,
        filename: filename,
        lang: lang,
      };
    
      await publishResult(process.env.RESULT_TOPIC, messageData);
      console.log(`Text translated to ${lang}`);
    };

###  Python 
    
    
    def translate_text(event: dict, context: dict) -> None:
        """Cloud Function triggered by PubSub when a message is received from
        a subscription.
    
        Translates the text in the message from the specified source language
        to the requested target language, then sends a message requesting another
        service save the result.
    
        Args:
            event: dictionary containing the PubSub event.
            context: a dictionary containing metadata about the event.
    
        Returns:
            None; the output is written to stdout and Cloud Logging.
        """
        if event.get("data"):
            message_data = base64.b64decode(event["data"]).decode("utf-8")
            message = json.loads(message_data)
        else:
            raise ValueError("Data sector is missing in the Pub/Sub message.")
    
        text = validate_message(message, "text")
        filename = validate_message(message, "filename")
        target_lang = validate_message(message, "lang")
        src_lang = validate_message(message, "src_lang")
    
        print(f"Translating text into {target_lang}.")
        translated_text = translate_client.translate(
            text, target_language=target_lang, source_language=src_lang
        )
        topic_name = os.environ["RESULT_TOPIC"]
        message = {
            "text": translated_text["translatedText"],
            "filename": filename,
            "lang": target_lang,
        }
        encoded_message = json.dumps(message).encode("utf-8")
        topic_path = publisher.topic_path(project_id, topic_name)
        future = publisher.publish(topic_path, data=encoded_message)
        future.result()

###  Go 
    
    
    package ocr
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/translate"
    )
    
    // TranslateText is executed when a message is published to the Cloud Pub/Sub
    // topic specified by the TRANSLATE_TOPIC environment variable, and translates
    // the text using the Google Translate API.
    func TranslateText(ctx context.Context, event [PubSubMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/apiv1/pubsublitepb.html#cloud_google_com_go_pubsublite_apiv1_pubsublitepb_PubSubMessage)) error {
    	if err := setup(ctx); err != nil {
    		return fmt.Errorf("setup: %w", err)
    	}
    	if event.Data == nil {
    		return fmt.Errorf("empty data")
    	}
    	var message ocrMessage
    	if err := json.Unmarshal(event.Data, &message); err != nil {
    		return fmt.Errorf("json.Unmarshal: %w", err)
    	}
    
    	log.Printf("Translating text into %s.", message.Lang.String())
    	opts := translate.[Options](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Options){
    		Source: message.SrcLang,
    	}
    	translateResponse, err := translateClient.[Translate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Client_Translate)(ctx, []string{message.[Text](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_HTML_Text)}, message.Lang, &opts)
    	if err != nil {
    		return fmt.Errorf("Translate: %w", err)
    	}
    	if len(translateResponse) == 0 {
    		return fmt.Errorf("Empty Translate response")
    	}
    	translatedText := translateResponse[0]
    
    	messageData, err := json.Marshal(ocrMessage{
    		Text:     translated[Text](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_HTML_Text).[Text](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_HTML_Text),
    		FileName: message.FileName,
    		Lang:     message.Lang,
    		SrcLang:  message.SrcLang,
    	})
    	if err != nil {
    		return fmt.Errorf("json.Marshal: %w", err)
    	}
    
    	topic := pubsubClient.Topic(resultTopic)
    	ok, err := topic.Exists(ctx)
    	if err != nil {
    		return fmt.Errorf("Exists: %w", err)
    	}
    	if !ok {
    		topic, err = pubsubClient.CreateTopic(ctx, resultTopic)
    		if err != nil {
    			return fmt.Errorf("CreateTopic: %w", err)
    		}
    	}
    	msg := &pubsub.Message{
    		Data: messageData,
    	}
    	if _, err = topic.Publish(ctx, msg).Get(ctx); err != nil {
    		return fmt.Errorf("Get: %w", err)
    	}
    	log.Printf("Sent translation: %q", translated[Text](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_HTML_Text).[Text](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_HTML_Text))
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.LocationName.html);
    import com.google.cloud.translate.v3.[TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html);
    import com.google.cloud.translate.v3.[TranslateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import functions.eventpojos.[Message](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html);
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import java.util.concurrent.ExecutionException;
    import java.util.logging.Level;
    import java.util.logging.Logger;
    
    public class OcrTranslateText implements BackgroundFunction<Message> {
      private static final Logger logger = Logger.[getLogger](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.LoggingUtil.SubSystem.html#com_google_cloud_pubsub_v1_LoggingUtil_SubSystem_getLogger__)(OcrTranslateText.class.getName());
    
      // TODO<developer> set these environment variables
      private static final String PROJECT_ID = getenv("GCP_PROJECT");
      private static final String RESULTS_TOPIC_NAME = getenv("RESULT_TOPIC");
      private static final String LOCATION_NAME = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.LocationName.html).of(PROJECT_ID, "global").toString();
    
      private [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher;
    
      public OcrTranslateText() throws IOException {
        publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(
            [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html).of(PROJECT_ID, RESULTS_TOPIC_NAME)).build();
      }
    
      @Override
      public void accept([Message](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html) pubSubMessage, Context context) {
        OcrTranslateApiMessage ocrMessage = OcrTranslateApiMessage.fromPubsubData(
            pubSubMessage.getData().getBytes(StandardCharsets.UTF_8));
    
        String targetLang = ocrMessage.getLang();
        logger.info("Translating text into " + targetLang);
    
        // Translate text to target language
        String text = ocrMessage.getText();
        [TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html) request =
            [TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html).newBuilder()
                .setParent(LOCATION_NAME)
                .setMimeType("text/plain")
                .setTargetLanguageCode(targetLang)
                .addContents(text)
                .build();
    
        [TranslateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html) response;
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          response = client.translateText(request);
        } catch (IOException e) {
          // Log error (since IOException cannot be thrown by a function)
          logger.log(Level.SEVERE, "Error translating text: " + e.getMessage(), e);
          return;
        }
        if (response.[getTranslationsCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html#com_google_cloud_translate_v3_TranslateTextResponse_getTranslationsCount__)() == 0) {
          return;
        }
    
        String translatedText = response.[getTranslations](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html#com_google_cloud_translate_v3_TranslateTextResponse_getTranslations_int_)(0).getTranslatedText();
        logger.info("Translated text: " + translatedText);
    
        // Send translated text to (subsequent) Pub/Sub topic
        String filename = ocrMessage.getFilename();
        OcrTranslateApiMessage translateMessage = new OcrTranslateApiMessage(
            translatedText, filename, targetLang);
        try {
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) byteStr = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(translateMessage.toPubsubData());
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubApiMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().setData(byteStr).build();
    
          [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)(pubsubApiMessage).get();
          logger.info("Text translated to " + targetLang);
        } catch (InterruptedException | ExecutionException e) {
          // Log error (since these exception types cannot be thrown by a function)
          logger.log(Level.SEVERE, "Error publishing translation save request: " + e.getMessage(), e);
        }
      }
    
      // Avoid ungraceful deployment failures due to unset environment variables.
      // If you get this warning you should redeploy with the variable set.
      private static String getenv(String name) {
        String value = System.getenv(name);
        if (value == null) {
          logger.warning("Environment variable " + name + " was not set");
          value = "MISSING";
        }
        return value;
      }
    }

### Saving the translations

Finally, the following function receives the translated text and saves it back to Cloud Storage:

###  Node.js 
    
    
    /**
     * This function is exported by index.js, and is executed when
     * a message is published to the Cloud Pub/Sub topic specified
     * by the RESULT_TOPIC environment variable. The function saves
     * the data packet to a file in GCS.
     *
     * @param {object} event The Cloud Pub/Sub Message object.
     * @param {string} {messageObject}.data The "data" property of the Cloud Pub/Sub
     * Message. This property will be a base64-encoded string that you must decode.
     */
    exports.saveResult = async event => {
      const pubsubData = event.data;
      const jsonStr = Buffer.from(pubsubData, 'base64').toString();
      const {text, filename, lang} = JSON.parse(jsonStr);
    
      if (!text) {
        throw new Error(
          'Text not provided. Make sure you have a "text" property in your request'
        );
      }
      if (!filename) {
        throw new Error(
          'Filename not provided. Make sure you have a "filename" property in your request'
        );
      }
      if (!lang) {
        throw new Error(
          'Language not provided. Make sure you have a "lang" property in your request'
        );
      }
    
      console.log(`Received request to save file ${filename}`);
    
      const bucketName = process.env.RESULT_BUCKET;
      const newFilename = renameImageForSave(filename, lang);
      const file = storage.bucket(bucketName).file(newFilename);
    
      console.log(`Saving result to ${newFilename} in bucket ${bucketName}`);
    
      await file.save(text);
      console.log('File saved.');
    };

###  Python 
    
    
    def save_result(event: dict, context: dict) -> None:
        """
        Cloud Function triggered by PubSub when a message is received from
        a subscription.
    
        Args:
            event: dictionary containing the PubSub event.
            context: a dictionary containing metadata about the event.
    
        Returns:
            None; the output is written to stdout and Cloud Logging.
        """
        if event.get("data"):
            message_data = base64.b64decode(event["data"]).decode("utf-8")
            message = json.loads(message_data)
        else:
            raise ValueError("Data sector is missing in the Pub/Sub message.")
    
        text = validate_message(message, "text")
        filename = validate_message(message, "filename")
        lang = validate_message(message, "lang")
    
        print(f"Received request to save file {filename}.")
    
        bucket_name = os.environ["RESULT_BUCKET"]
        result_filename = f"{filename}_{lang}.txt"
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(result_filename)
    
        print(f"Saving result to {result_filename} in bucket {bucket_name}.")
    
        blob.upload_from_string(text)
    
        print("File saved.")

###  Go 
    
    
    package ocr
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    )
    
    // SaveResult is executed when a message is published to the Cloud Pub/Sub topic
    // specified by the RESULT_TOPIC environment vairable, and saves the data packet
    // to a file in GCS.
    func SaveResult(ctx context.Context, event PubSubMessage) error {
    	if err := setup(ctx); err != nil {
    		return fmt.Errorf("ProcessImage: %w", err)
    	}
    	var message ocrMessage
    	if event.Data == nil {
    		return fmt.Errorf("Empty data")
    	}
    	if err := json.Unmarshal(event.Data, &message); err != nil {
    		return fmt.Errorf("json.Unmarshal: %w", err)
    	}
    	log.Printf("Received request to save file %q.", message.FileName)
    
    	resultFilename := fmt.Sprintf("%s_%s.txt", message.FileName, message.Lang)
    	bucket := storageClient.Bucket(resultBucket)
    
    	log.Printf("Saving result to %q in bucket %q.", resultFilename, resultBucket)
    
    	w := bucket.Object(resultFilename).NewWriter(ctx)
    	defer w.Close()
    	fmt.Fprint(w, message.Text)
    
    	log.Printf("File saved.")
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import functions.eventpojos.PubsubMessage;
    import java.nio.charset.StandardCharsets;
    import java.util.logging.Logger;
    
    public class OcrSaveResult implements BackgroundFunction<PubsubMessage> {
      // TODO<developer> set this environment variable
      private static final String RESULT_BUCKET = System.getenv("RESULT_BUCKET");
    
      private static final [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) STORAGE = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).getDefaultInstance().getService();
      private static final Logger logger = Logger.getLogger(OcrSaveResult.class.getName());
    
      @Override
      public void accept(PubsubMessage pubSubMessage, Context context) {
        OcrTranslateApiMessage ocrMessage = OcrTranslateApiMessage.fromPubsubData(
            pubSubMessage.getData().getBytes(StandardCharsets.UTF_8));
    
        logger.info("Received request to save file " +  ocrMessage.getFilename());
    
        String newFileName = String.format(
            "%s_to_%s.txt", ocrMessage.getFilename(), ocrMessage.getLang());
    
        // Save file to RESULT_BUCKET with name newFileNaem
        logger.info(String.format("Saving result to %s in bucket %s", newFileName, RESULT_BUCKET));
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder([BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(RESULT_BUCKET, newFileName)).build();
        STORAGE.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(blobInfo, ocrMessage.getText().getBytes(StandardCharsets.UTF_8));
        logger.info("File saved");
      }
    }

## Deploying the functions

  1. To deploy the image processing function with a Cloud Storage trigger, run the following command in the directory that contains the sample code (or in the case of Java, the `pom.xml` file):

###  Node.js 
         
         gcloud functions deploy ocr-extract \
         --runtime nodejs22 \  
         --trigger-bucket YOUR_IMAGE_BUCKET_NAME \  
         --entry-point processImage \  
         --set-env-vars "^:^GCP_PROJECT=YOUR_GCP_PROJECT_ID:TRANSLATE_TOPIC=YOUR_TRANSLATE_TOPIC_NAME:RESULT_TOPIC=YOUR_RESULT_TOPIC_NAME:TO_LANG=es,en,fr,ja"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
         
         gcloud functions deploy ocr-extract \
         --runtime python312 \  
         --trigger-bucket YOUR_IMAGE_BUCKET_NAME \  
         --entry-point process_image \  
         --set-env-vars "^:^GCP_PROJECT=YOUR_GCP_PROJECT_ID:TRANSLATE_TOPIC=YOUR_TRANSLATE_TOPIC_NAME:RESULT_TOPIC=YOUR_RESULT_TOPIC_NAME:TO_LANG=es,en,fr,ja"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. **Caution:** If you're using Python 3.7, you may need to omit one or more of [these reserved environment variables](https://docs.cloud.google.com/functions/docs/configuring/env-var#nodejs_8_python_37_and_go_111) from the above command. 

###  Go 
         
         gcloud functions deploy ocr-extract \
         --runtime go121 \  
         --trigger-bucket YOUR_IMAGE_BUCKET_NAME \  
         --entry-point ProcessImage \  
         --set-env-vars "^:^GCP_PROJECT=YOUR_GCP_PROJECT_ID:TRANSLATE_TOPIC=YOUR_TRANSLATE_TOPIC_NAME:RESULT_TOPIC=YOUR_RESULT_TOPIC_NAME:TO_LANG=es,en,fr,ja"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
         
         gcloud functions deploy ocr-extract \
         --entry-point functions.OcrProcessImage \
         --runtime java17 \
         --memory 512MB \  
         --trigger-bucket YOUR_IMAGE_BUCKET_NAME \  
         --set-env-vars "^:^GCP_PROJECT=YOUR_GCP_PROJECT_ID:TRANSLATE_TOPIC=YOUR_TRANSLATE_TOPIC_NAME:RESULT_TOPIC=YOUR_RESULT_TOPIC_NAME:TO_LANG=es,en,fr,ja"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function.  This example has multiple functions, each with its own subdirectory that contains a `pom.xml` file. When deploying this function, make sure you `cd` into the appropriate subdirectory that contains this file. 

where `YOUR_IMAGE_BUCKET_NAME` is the name of your Cloud Storage bucket where you will be uploading images.

  2. To deploy the text translation function with a Pub/Sub trigger, run the following command in the directory that contains the sample code (or in the case of Java, the `pom.xml` file):

###  Node.js 
         
         gcloud functions deploy ocr-translate \
         --runtime nodejs22 \  
         --trigger-topic YOUR_TRANSLATE_TOPIC_NAME \  
         --entry-point translateText \  
         --set-env-vars "GCP_PROJECT=YOUR_GCP_PROJECT_ID,RESULT_TOPIC=YOUR_RESULT_TOPIC_NAME"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
         
         gcloud functions deploy ocr-translate \
         --runtime python312 \  
         --trigger-topic YOUR_TRANSLATE_TOPIC_NAME \  
         --entry-point translate_text \  
         --set-env-vars "GCP_PROJECT=YOUR_GCP_PROJECT_ID,RESULT_TOPIC=YOUR_RESULT_TOPIC_NAME"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. **Caution:** If you're using Python 3.7, you may need to omit one or more of [these reserved environment variables](https://docs.cloud.google.com/functions/docs/configuring/env-var#nodejs_8_python_37_and_go_111) from the above command. 

###  Go 
         
         gcloud functions deploy ocr-translate \
         --runtime go121 \  
         --trigger-topic YOUR_TRANSLATE_TOPIC_NAME \  
         --entry-point TranslateText \  
         --set-env-vars "GCP_PROJECT=YOUR_GCP_PROJECT_ID,RESULT_TOPIC=YOUR_RESULT_TOPIC_NAME"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
         
         gcloud functions deploy ocr-translate \
         --entry-point functions.OcrTranslateText \
         --runtime java17 \
         --memory 512MB \  
         --trigger-topic YOUR_TRANSLATE_TOPIC_NAME \  
         --set-env-vars "GCP_PROJECT=YOUR_GCP_PROJECT_ID,RESULT_TOPIC=YOUR_RESULT_TOPIC_NAME"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function.  This example has multiple functions, each with its own subdirectory that contains a `pom.xml` file. When deploying this function, make sure you `cd` into the appropriate subdirectory that contains this file. 

  3. To deploy the function that saves results to Cloud Storage with a Cloud Pub/Sub trigger, run the following command in the directory that contains the sample code (or in the case of Java, the `pom.xml` file):

###  Node.js 
         
         gcloud functions deploy ocr-save \
         --runtime nodejs22 \  
         --trigger-topic YOUR_RESULT_TOPIC_NAME \  
         --entry-point saveResult \  
         --set-env-vars "GCP_PROJECT=YOUR_GCP_PROJECT_ID,RESULT_BUCKET=YOUR_RESULT_BUCKET_NAME"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
         
         gcloud functions deploy ocr-save \
         --runtime python312 \  
         --trigger-topic YOUR_RESULT_TOPIC_NAME \  
         --entry-point save_result \  
         --set-env-vars "GCP_PROJECT=YOUR_GCP_PROJECT_ID,RESULT_BUCKET=YOUR_RESULT_BUCKET_NAME"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. **Caution:** If you're using Python 3.7, you may need to omit one or more of [these reserved environment variables](https://docs.cloud.google.com/functions/docs/configuring/env-var#nodejs_8_python_37_and_go_111) from the above command. 

###  Go 
         
         gcloud functions deploy ocr-save \
         --runtime go121 \  
         --trigger-topic YOUR_RESULT_TOPIC_NAME \  
         --entry-point SaveResult \  
         --set-env-vars "GCP_PROJECT=YOUR_GCP_PROJECT_ID,RESULT_BUCKET=YOUR_RESULT_BUCKET_NAME"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
         
         gcloud functions deploy ocr-save \
         --entry-point functions.OcrSaveResult \
         --runtime java17 \
         --memory 512MB \  
         --trigger-topic YOUR_RESULT_TOPIC_NAME \  
         --set-env-vars "GCP_PROJECT=YOUR_GCP_PROJECT_ID,RESULT_BUCKET=YOUR_RESULT_BUCKET_NAME"

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function.  This example has multiple functions, each with its own subdirectory that contains a `pom.xml` file. When deploying this function, make sure you `cd` into the appropriate subdirectory that contains this file. 




## Uploading an image

  1. Upload an image to your image Cloud Storage bucket:
         
         gcloud storage cp PATH_TO_IMAGE gs://YOUR_IMAGE_BUCKET_NAME

where

     * `PATH_TO_IMAGE` is a path to an image file (that contains text) on your local system.
     * `YOUR_IMAGE_BUCKET_NAME` is the name of the bucket where you are uploading images.

You can download one of the images from the [sample project](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/tree/master/functions/ocr/images).

  2. Watch the logs to be sure the executions have completed:
         
         gcloud functions logs read --limit 100

  3. You can view the saved translations in the Cloud Storage bucket you used for `YOUR_RESULT_BUCKET_NAME`.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Deleting the function

Deleting Cloud Run functions does not remove any resources stored in Cloud Storage.

To delete the Cloud Run functions you created in this tutorial, run the following commands:
    
    
    gcloud functions delete ocr-extract
    gcloud functions delete ocr-translate
    gcloud functions delete ocr-save

You can also delete Cloud Run functions from the [Google Cloud console](https://console.cloud.google.com/functions/list).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
