---
url: https://docs.cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen/
title: Cloud Storage Tutorial (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:50.620108+00:00
---

# Cloud Storage Tutorial (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback 

#  Cloud Storage Tutorial (1st gen) Stay organized with collections  Save and categorize content based on your preferences. 

This simple tutorial demonstrates writing, deploying, and triggering an [Event-Driven Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/writing#event-driven_functions) with a [Cloud Storage trigger](https://docs.cloud.google.com/functions/1stgendocs/calling/storage) to respond to Cloud Storage events.

**Note:** Events are delivered using [Pub/Sub notifications](https://docs.cloud.google.com/storage/docs/pubsub-notifications) from Cloud Storage. A bucket can have up to 10 notification configurations set to trigger for a specific event. Setting up too many notifications for the same bucket might exceed the notifications limit for the bucket and make it impossible to create a function, as indicated by the error `Cloud Storage bucket ...: Pub/Sub notification limit reached`. If you reach the limit, you can't create a function until you take remedial action, such as removing notifications.

If you're looking for code samples for using [Cloud Storage](https://docs.cloud.google.com/storage/docs) itself, visit the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?p=storage).

## Objectives

  * Write and deploy an [Event-Driven Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/writing#event-driven_functions).
  * Trigger the function by uploading a file to [Cloud Storage](https://docs.cloud.google.com/storage).



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud Run functions
  * Cloud Storage



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

  4. Enable the Cloud Functions, Cloud Build, Cloud Storage, and Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions,cloudbuild.googleapis.com,storage_api,eventarc.googleapis.com&redirect=https%3A//cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen)

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

  10. Enable the Cloud Functions, Cloud Build, Cloud Storage, and Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions,cloudbuild.googleapis.com,storage_api,eventarc.googleapis.com&redirect=https%3A//cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

If you already have the gcloud CLI installed, update it by running the following command:
    
    gcloud components update

**Note:** Make sure the runtime service account key you are using for your [Application Default Credentials](https://cloud.google.com/docs/authentication/production#automatically) has either the `cloudfunctions.serviceAgent` role or the `storage.buckets.{get, update}` and the `resourcemanager.projects.get` permissions. For more information on setting these permissions, see [Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console). 
  14. Prepare your development environment: 

###  Node.js 

[ Go to the Node.js setup guide ](https://docs.cloud.google.com/nodejs/docs/setup)

###  Python 

[ Go to the Python setup guide ](https://docs.cloud.google.com/python/docs/setup)

###  Go 

[ Go to the Go setup guide ](https://docs.cloud.google.com/go/docs/setup)

###  Java 

[ Go to the Java setup guide ](https://docs.cloud.google.com/java/docs/setup)

###  Ruby 

[ Go to the Ruby setup guide ](https://docs.cloud.google.com/ruby/docs/setup)




## Preparing the application

  1. Create a Cloud Storage bucket to upload a test file, where `YOUR_TRIGGER_BUCKET_NAME` is a globally unique bucket name:
         
         gcloud storage buckets create gs://YOUR_TRIGGER_BUCKET_NAME

  2. Clone the sample app repository to your local machine:

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

###  Ruby 
         
         git clone https://github.com/GoogleCloudPlatform/ruby-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/ruby-docs-samples/archive/main.zip) as a zip file and extract it. 

  3. Change to the directory that contains the Cloud Run functions sample code:

###  Node.js 
         
         cd nodejs-docs-samples/functions/helloworld/

###  Python 
         
         cd python-docs-samples/functions/helloworld/

###  Go 
         
         cd golang-samples/functions/helloworld/

###  Java 
         
         cd java-docs-samples/functions/helloworld/hello-gcs/

###  Ruby 
         
         cd ruby-docs-samples/functions/helloworld/storage/




## Deploying and triggering the function

Cloud Storage functions are based on [Pub/Sub notifications from Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications) and support similar event types:

  * [finalize](https://docs.cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen#object_finalize)

  * [delete](https://docs.cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen#object_delete)

  * [archive](https://docs.cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen#object_archive)

  * [metadata update](https://docs.cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen#object_metadata_update)




The following sections describe how to deploy and trigger a function for each of these event types.

### Object Finalize

Object finalize events trigger when a "write" of a [Cloud Storage Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource) is successfully finalized. In particular, this means that creating a new object or overwriting an existing object triggers this event. Archive and metadata update operations are ignored by this trigger.

#### Object Finalize: deploying the function

Take a look at the sample function, which handles Cloud Storage events:

###  Node.js 
    
    
    /**
     * Generic background Cloud Function to be triggered by Cloud Storage.
     * This sample works for all Cloud Storage CRUD operations.
     *
     * @param {object} file The Cloud Storage file metadata.
     * @param {object} context The event metadata.
     */
    exports.helloGCS = (file, context) => {
      console.log(`  Event: ${context.eventId}`);
      console.log(`  Event Type: ${context.eventType}`);
      console.log(`  Bucket: ${file.bucket}`);
      console.log(`  File: ${file.name}`);
      console.log(`  Metageneration: ${file.metageneration}`);
      console.log(`  Created: ${file.timeCreated}`);
      console.log(`  Updated: ${file.updated}`);
    };

###  Python 
    
    
    def hello_gcs(event, context):
        """Background Cloud Function to be triggered by Cloud Storage.
           This generic function logs relevant data when a file is changed,
           and works for all Cloud Storage CRUD operations.
        Args:
            event (dict):  The dictionary with data specific to this type of event.
                           The `data` field contains a description of the event in
                           the Cloud Storage `object` format described here:
                           https://cloud.google.com/storage/docs/json_api/v1/objects#resource
            context (google.cloud.functions.Context): Metadata of triggering event.
        Returns:
            None; the output is written to Cloud Logging
        """
    
        print(f"Event ID: {context.event_id}")
        print(f"Event type: {context.event_type}")
        print("Bucket: {}".format(event["bucket"]))
        print("File: {}".format(event["name"]))
        print("Metageneration: {}".format(event["metageneration"]))
        print("Created: {}".format(event["timeCreated"]))
        print("Updated: {}".format(event["updated"]))
    
    

###  Go 
    
    
    // Package helloworld provides a set of Cloud Functions samples.
    package helloworld
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"time"
    
    	"cloud.google.com/go/functions/metadata"
    )
    
    // GCSEvent is the payload of a GCS event.
    type GCSEvent struct {
    	Kind                    string                 `json:"kind"`
    	ID                      string                 `json:"id"`
    	SelfLink                string                 `json:"selfLink"`
    	Name                    string                 `json:"name"`
    	Bucket                  string                 `json:"bucket"`
    	Generation              string                 `json:"generation"`
    	Metageneration          string                 `json:"metageneration"`
    	ContentType             string                 `json:"contentType"`
    	TimeCreated             time.Time              `json:"timeCreated"`
    	Updated                 time.Time              `json:"updated"`
    	TemporaryHold           bool                   `json:"temporaryHold"`
    	EventBasedHold          bool                   `json:"eventBasedHold"`
    	RetentionExpirationTime time.Time              `json:"retentionExpirationTime"`
    	StorageClass            string                 `json:"storageClass"`
    	TimeStorageClassUpdated time.Time              `json:"timeStorageClassUpdated"`
    	Size                    string                 `json:"size"`
    	MD5Hash                 string                 `json:"md5Hash"`
    	MediaLink               string                 `json:"mediaLink"`
    	ContentEncoding         string                 `json:"contentEncoding"`
    	ContentDisposition      string                 `json:"contentDisposition"`
    	CacheControl            string                 `json:"cacheControl"`
    	Metadata                map[string]interface{} `json:"metadata"`
    	CRC32C                  string                 `json:"crc32c"`
    	ComponentCount          int                    `json:"componentCount"`
    	Etag                    string                 `json:"etag"`
    	CustomerEncryption      struct {
    		EncryptionAlgorithm string `json:"encryptionAlgorithm"`
    		KeySha256           string `json:"keySha256"`
    	}
    	KMSKeyName    string `json:"kmsKeyName"`
    	ResourceState string `json:"resourceState"`
    }
    
    // HelloGCS consumes a(ny) GCS event.
    func HelloGCS(ctx context.Context, e GCSEvent) error {
    	meta, err := metadata.[FromContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Metadata_FromContext)(ctx)
    	if err != nil {
    		return fmt.Errorf("metadata.FromContext: %w", err)
    	}
    	log.Printf("Event ID: %v\n", meta.EventID)
    	log.Printf("Event type: %v\n", meta.EventType)
    	log.Printf("Bucket: %v\n", e.Bucket)
    	log.Printf("File: %v\n", e.Name)
    	log.Printf("Metageneration: %v\n", e.Metageneration)
    	log.Printf("Created: %v\n", e.TimeCreated)
    	log.Printf("Updated: %v\n", e.Updated)
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import functions.eventpojos.GcsEvent;
    import java.util.logging.Logger;
    
    /**
     * Example Cloud Storage-triggered function.
     * This function can process any event from Cloud Storage.
     */
    public class HelloGcs implements BackgroundFunction<GcsEvent> {
      private static final Logger logger = Logger.getLogger(HelloGcs.class.getName());
    
      @Override
      public void accept(GcsEvent event, Context context) {
        logger.info("Event: " + context.eventId());
        logger.info("Event Type: " + context.eventType());
        logger.info("Bucket: " + event.getBucket());
        logger.info("File: " + event.getName());
        logger.info("Metageneration: " + event.getMetageneration());
        logger.info("Created: " + event.getTimeCreated());
        logger.info("Updated: " + event.getUpdated());
      }
    }
    

###  Ruby 
    
    
    require "functions_framework"
    
    FunctionsFramework.cloud_event "hello_gcs" do |event|
      # This function supports all Cloud Storage events.
      # The `event` parameter is a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      payload = event.data
    
      logger.info "Event: #{event.id}"
      logger.info "Event Type: #{event.type}"
      logger.info "Bucket: #{payload['bucket']}"
      logger.info "File: #{payload['name']}"
      logger.info "Metageneration: #{payload['metageneration']}"
      logger.info "Created: #{payload['timeCreated']}"
      logger.info "Updated: #{payload['updated']}"
    end

To deploy the function, run the following command in the directory where the sample code is located:

###  Node.js 
    
    
    gcloud functions deploy helloGCS \
    --runtime nodejs22 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.finalize

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
    
    
    gcloud functions deploy hello_gcs \
    --runtime python312 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.finalize

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. 

###  Go 
    
    
    gcloud functions deploy HelloGCS \
    --runtime go121 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.finalize

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
    
    
    gcloud functions deploy java-gcs-function \
    --entry-point functions.HelloGcs \
    --runtime java17 \
    --memory 512MB \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.finalize

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function. 

###  Ruby 
    
    
    gcloud functions deploy hello_gcs --runtime ruby33 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.finalize

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Ruby version](https://docs.cloud.google.com/functions/docs/runtime-support#ruby) to run your function. 

where `YOUR_TRIGGER_BUCKET_NAME` is the name of the Cloud Storage bucket that triggers the function.

#### Object Finalize: triggering the function

To trigger the function:

  1. Create an empty `gcf-test.txt` file in the directory where the sample code is located.

  2. Upload the file to Cloud Storage in order to trigger the function:
         
         gcloud storage cp gcf-test.txt gs://YOUR_TRIGGER_BUCKET_NAME

where `YOUR_TRIGGER_BUCKET_NAME` is the name of your Cloud Storage bucket where you will upload a test file.

  3. Check the logs to make sure the executions have completed:
         
         gcloud functions logs read --limit 50
         




### Object Delete

Object delete events are triggered when an object is [soft deleted](https://docs.cloud.google.com/storage/docs/soft-delete). This happens when an object is overwritten or deleted in a bucket without [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) enabled. Deleting an object by specifying its generation number also results in the object being soft deleted.

#### Object Delete: deploying the function

Using the same sample code as in the finalize example, deploy the function with object delete as the trigger event. Run the following command in the directory where the sample code is located:

###  Node.js 
    
    
    gcloud functions deploy helloGCS \
    --runtime nodejs22 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.delete

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
    
    
    gcloud functions deploy hello_gcs \
    --runtime python312 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.delete

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. 

###  Go 
    
    
    gcloud functions deploy HelloGCS \
    --runtime go121 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.delete

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
    
    
    gcloud functions deploy java-gcs-function \
    --entry-point functions.HelloGcs \
    --runtime java17 \
    --memory 512MB \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.delete

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function. 

###  Ruby 
    
    
    gcloud functions deploy hello_gcs --runtime ruby33 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.delete

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Ruby version](https://docs.cloud.google.com/functions/docs/runtime-support#ruby) to run your function. 

where `YOUR_TRIGGER_BUCKET_NAME` is the name of the Cloud Storage bucket that triggers the function.

#### Object Delete: triggering the function

To trigger the function:

  1. Create an empty `gcf-test.txt` file in the directory where the sample code is located.

  2. Make sure that your bucket is non-versioning:
         
         gcloud storage buckets update gs://YOUR_TRIGGER_BUCKET_NAME --no-versioning

  3. Upload the file to Cloud Storage:
         
         gcloud storage cp gcf-test.txt gs://YOUR_TRIGGER_BUCKET_NAME

where `YOUR_TRIGGER_BUCKET_NAME` is the name of your Cloud Storage bucket where you will upload a test file. At this point the function should not execute yet.

  4. Delete the file to trigger the function:
         
         gcloud storage rm gs://YOUR_TRIGGER_BUCKET_NAME/gcf-test.txt

  5. Check the logs to make sure the executions have completed:
         
         gcloud functions logs read --limit 50
         




Note that the function may take some time to finish executing.

### Object Archive

Object archive events are triggered when a live version of an object becomes a noncurrent version. This happens when an object is overwritten or deleted in a bucket with [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) enabled.

#### Object Archive: deploying the function

Using the same sample code as in the finalize example, deploy the function with object archive as the trigger event. Run the following command in the directory where the sample code is located:

###  Node.js 
    
    
    gcloud functions deploy helloGCS \
    --runtime nodejs22 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.archive

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
    
    
    gcloud functions deploy hello_gcs \
    --runtime python312 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.archive

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. 

###  Go 
    
    
    gcloud functions deploy HelloGCS \
    --runtime go121 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.archive

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
    
    
    gcloud functions deploy java-gcs-function \
    --entry-point functions.HelloGcs \
    --runtime java17 \
    --memory 512MB \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.archive

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function. 

###  Ruby 
    
    
    gcloud functions deploy hello_gcs --runtime ruby33 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.archive

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Ruby version](https://docs.cloud.google.com/functions/docs/runtime-support#ruby) to run your function. 

where `YOUR_TRIGGER_BUCKET_NAME` is the name of the Cloud Storage bucket that triggers the function.

#### Object Archive: triggering the function

To trigger the function:

  1. Create an empty `gcf-test.txt` file in the directory where the sample code is located.

  2. Make sure that your bucket has versioning enabled:
         
         gcloud storage buckets update gs://YOUR_TRIGGER_BUCKET_NAME --versioning

  3. Upload the file to Cloud Storage:
         
         gcloud storage cp gcf-test.txt gs://YOUR_TRIGGER_BUCKET_NAME

where `YOUR_TRIGGER_BUCKET_NAME` is the name of your Cloud Storage bucket where you will upload a test file. At this point the function should not execute yet.

  4. Archive the file to trigger the function:
         
         gcloud storage rm gs://YOUR_TRIGGER_BUCKET_NAME/gcf-test.txt

  5. Watch the logs to make sure the executions have completed:
         
         gcloud functions logs read --limit 50
         




### Object Metadata Update

Metadata update events are triggered when the metadata of existing object is updated.

#### Object Metadata Update: deploying the function

Using the same sample code as in the finalize example, deploy the function with metadata update as the trigger event. Run the following command in the directory where the sample code is located:

###  Node.js 
    
    
    gcloud functions deploy helloGCS \
    --runtime nodejs22 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.metadataUpdate

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
    
    
    gcloud functions deploy hello_gcs \
    --runtime python312 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.metadataUpdate

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. 

###  Go 
    
    
    gcloud functions deploy HelloGCS \
    --runtime go121 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.metadataUpdate

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
    
    
    gcloud functions deploy java-gcs-function \
    --entry-point functions.HelloGcs \
    --runtime java17 \
    --memory 512MB \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.metadataUpdate

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function. 

###  Ruby 
    
    
    gcloud functions deploy hello_gcs --runtime ruby33 \  
    --trigger-resource YOUR_TRIGGER_BUCKET_NAME \  
    --trigger-event google.storage.object.metadataUpdate

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Ruby version](https://docs.cloud.google.com/functions/docs/runtime-support#ruby) to run your function. 

where `YOUR_TRIGGER_BUCKET_NAME` is the name of the Cloud Storage bucket that triggers the function.

#### Object Metadata Update: triggering the function

To trigger the function:

  1. Create an empty `gcf-test.txt` file in the directory where the sample code is located.

  2. Make sure that your bucket is non-versioning:
         
         gcloud storage buckets update gs://YOUR_TRIGGER_BUCKET_NAME --no-versioning

  3. Upload the file to Cloud Storage:
         
         gcloud storage cp gcf-test.txt gs://YOUR_TRIGGER_BUCKET_NAME

where `YOUR_TRIGGER_BUCKET_NAME` is the name of your Cloud Storage bucket where you will upload a test file. At this point the function should not execute yet.

  4. Update the metadata of the file:
         
         gcloud storage objects update gs://YOUR_TRIGGER_BUCKET_NAME/gcf-test.txt --content-type=text/plain

  5. Watch the logs to make sure the executions have completed:
         
         gcloud functions logs read --limit 50
         




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

To delete the function you created in this tutorial, run the following command:

###  Node.js 
    
    
    gcloud functions delete helloGCS 

###  Python 
    
    
    gcloud functions delete hello_gcs 

###  Go 
    
    
    gcloud functions delete HelloGCS 

###  Java 
    
    
    gcloud functions delete java-gcs-function 

###  Ruby 
    
    
    gcloud functions delete hello_gcs 

You can also delete Cloud Run functions from the [Google Cloud console](https://console.cloud.google.com/functions/list).

## What's next

  * [Learn how to perform OCR on images uploaded to a bucket](https://docs.cloud.google.com/functions/1stgendocs/tutorials/ocr-1st-gen).
  * [Learn how to translate text files using Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/tutorials/ocr-1st-gen).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
