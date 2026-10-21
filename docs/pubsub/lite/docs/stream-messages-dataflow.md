---
url: https://docs.cloud.google.com/pubsub/lite/docs/stream-messages-dataflow/
title: Quickstart: Stream Pub/Sub Lite messages by using Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:10.497377+00:00
---

# Quickstart: Stream Pub/Sub Lite messages by using Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/stream-messages-dataflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Stream Pub/Sub Lite messages by using Dataflow

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

As an alternative to writing and running your own data processing programs, you can use [Dataflow](https://docs.cloud.google.com/dataflow) with the Pub/Sub Lite I/O connector for [Apache Beam](https://beam.apache.org/). Dataflow is a fully-managed service for transforming and enriching data in streaming (real-time) and batch modes with equal reliability and expressiveness. It reliably executes programs developed using the Apache Beam SDK, which has an extensible set of powerful stateful processing abstractions, and I/O connectors to other streaming and batch systems.

This quickstart shows you how to write an Apache Beam pipeline that will:

  * Read messages from Pub/Sub Lite
  * Window (or group) the messages by publish timestamp
  * Write the messages to Cloud Storage



It also shows you how to:

  * Submit your pipeline to run on Dataflow
  * Create a Dataflow Flex Template from your pipeline



This tutorial requires Maven, but it's also possible to convert the example project from Maven to Gradle. To learn more, see [Optional: Convert from Maven to Gradle](https://beam.apache.org/get-started/quickstart-java/#optional-convert-from-maven-to-gradle).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  7. Enable the Pub/Sub Lite, Dataflow, Google Cloud Storage JSON API, and Cloud Logging APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable pubsublite.googleapis.com  dataflow.googleapis.com  storage-api.googleapis.com  logging.googleapis.com

  8. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant roles to the service account. Run the following command once for each of the following IAM roles: `roles/dataflow.worker, roles/storage.objectAdmin, roles/pubsublite.admin`: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     4. Grant the required role to the principal that will attach the service account to other resources. 
            
            gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --member="user:USER_EMAIL" --role=roles/iam.serviceAccountUser

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `USER_EMAIL`: the email address for a Google Account

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Pub/Sub Lite, Dataflow, Google Cloud Storage JSON API, and Cloud Logging APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable pubsublite.googleapis.com  dataflow.googleapis.com  storage-api.googleapis.com  logging.googleapis.com

  15. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant roles to the service account. Run the following command once for each of the following IAM roles: `roles/dataflow.worker, roles/storage.objectAdmin, roles/pubsublite.admin`: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     4. Grant the required role to the principal that will attach the service account to other resources. 
            
            gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --member="user:USER_EMAIL" --role=roles/iam.serviceAccountUser

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `USER_EMAIL`: the email address for a Google Account

  16. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




## Set up your Pub/Sub Lite project

  1. Create variables for your Cloud Storage bucket, project, and Dataflow region. Cloud Storage bucket names must be globally unique. The Dataflow region must be a valid region where you can run your job. For more information about regions and locations, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations).
         
         export PROJECT_ID=$(gcloud config get-value project)
         export SERVICE_ACCOUNT=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         export BUCKET=BUCKET_NAME
         export DATAFLOW_REGION=DATAFLOW_REGION

  2. Create a Cloud Storage bucket owned by this project:
         
         gcloud storage buckets create gs://$BUCKET




## Create a Pub/Sub Lite zonal Lite topic and subscription

Create a zonal Lite Pub/Sub Lite topic and Lite subscription.

For the Lite location, choose a supported Pub/Sub Lite [location](https://docs.cloud.google.com/pubsub/lite/docs/locations). You must also specify a zone for the region. For example, `us-central1-a`.
    
    
    export TOPIC=LITE_TOPIC_ID
    export SUBSCRIPTION=LITE_SUBSCRIPTION_ID
    export LITE_LOCATION=LITE_LOCATION
    gcloud pubsub lite-topics create $TOPIC \
          --location=$LITE_LOCATION \
          --partitions=1 \
          --per-partition-bytes=30GiB
    gcloud pubsub lite-subscriptions create $SUBSCRIPTION \
          --location=$LITE_LOCATION \
          --topic=$TOPIC \
          --starting-offset=beginning

## Stream messages to Dataflow

### Download the quickstart sample code

Clone the quickstart repository and navigate to the sample code directory.
    
    
    git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git
    cd java-docs-samples/pubsublite/streaming-analytics

#### Sample code

This sample code uses Dataflow to:

  * Read messages from a Pub/Sub Lite subscription as an unbounded source.
  * Group messages based on their publish timestamps, using [fixed time windows](https://beam.apache.org/documentation/programming-guide/#fixed-time-windows) and the [default trigger](https://beam.apache.org/documentation/programming-guide/#default-trigger).
  * Write the grouped messages to files on Cloud Storage.




### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import com.google.cloud.pubsublite.proto.[SequencedMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SequencedMessage.html);
    import org.apache.beam.examples.common.WriteOneFilePerWindow;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.gcp.pubsublite.PubsubLiteIO;
    import org.apache.beam.sdk.io.gcp.pubsublite.SubscriberOptions;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.windowing.FixedWindows;
    import org.apache.beam.sdk.transforms.windowing.Window;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.joda.time.Duration;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    public class PubsubliteToGcs {
      /*
       * Define your own configuration options. Add your arguments to be processed
       * by the command-line parser.
       */
      public interface PubsubliteToGcsOptions extends StreamingOptions {
        @Description("Your Pub/Sub Lite subscription.")
        @Required
        String getSubscription();
    
        void setSubscription(String value);
    
        @Description("Window size of output files in minutes.")
        @Default.Integer(1)
        Integer getWindowSize();
    
        void setWindowSize(Integer value);
    
        @Description("Filename prefix of output files.")
        @Required
        String getOutput();
    
        void setOutput(String value);
      }
    
      private static final Logger LOG = LoggerFactory.getLogger(PubsubliteToGcs.class);
    
      public static void main(String[] args) throws InterruptedException {
        // The maximum number of shards when writing output files.
        int numShards = 1;
    
        PubsubliteToGcsOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(PubsubliteToGcsOptions.class);
    
        options.setStreaming(true);
    
        SubscriberOptions subscriberOptions =
            SubscriberOptions.newBuilder()
                .setSubscriptionPath([SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).parse(options.getSubscription()))
                .build();
    
        Pipeline pipeline = Pipeline.create(options);
        pipeline
            .apply("Read From Pub/Sub Lite", PubsubLiteIO.read(subscriberOptions))
            .apply(
                "Convert messages",
                MapElements.into(TypeDescriptors.strings())
                    .via(
                        (SequencedMessage sequencedMessage) -> {
                          String data = sequencedMessage.getMessage().getData().toStringUtf8();
                          LOG.info("Received: " + data);
                          long publishTime = sequencedMessage.getPublishTime().getSeconds();
                          return data + "\t" + publishTime;
                        }))
            .apply(
                "Apply windowing function",
                Window
                    // Group the elements using fixed-sized time intervals based on the element
                    // timestamp (using the default event time trigger). The element timestamp
                    // is the publish timestamp associated with a message.
                    //
                    // NOTE: If data is not being continuously ingested, such as with a batch or
                    // intermittent publisher, the final window will never close as the watermark
                    // will not advance. If this is a possibility with your pipeline, you should
                    // add an additional processing time trigger to force window closure after
                    // enough time has passed. See
                    // https://beam.apache.org/documentation/programming-guide/#triggers
                    // for more information.
                    .<String>into(FixedWindows.of(Duration.standardMinutes(options.getWindowSize()))))
            .apply("Write elements to GCS", new WriteOneFilePerWindow(options.getOutput(), numShards));
    
        // Execute the pipeline. You may add `.waitUntilFinish()` to observe logs in your console, but
        // `waitUntilFinish()` will not work in Dataflow Flex Templates.
        pipeline.run();
      }
    }

### Start the Dataflow pipeline

To start the pipeline in Dataflow, run the following command:
    
    
    mvn compile exec:java \
        -Dexec.mainClass=examples.PubsubliteToGcs \
        -Dexec.args=" \
            --subscription=projects/$PROJECT_ID/locations/$LITE_LOCATION/subscriptions/$SUBSCRIPTION \
            --output=gs://$BUCKET/samples/output \
            --windowSize=1 \
            --project=$PROJECT_ID \
            --region=$DATAFLOW_REGION \
            --tempLocation=gs://$BUCKET/temp \
            --runner=DataflowRunner \
            --serviceAccount=$SERVICE_ACCOUNT"

The preceding command launches a Dataflow job. Follow the link in the console output to access the job in the Dataflow monitoring console.

## Observe job progress

Observe the job's progress in the Dataflow console.

[Go to the Dataflow console](https://console.cloud.google.com/dataflow?project=)

Open the job details view to see:

  * Job graph
  * Execution details
  * Job metrics



[Publish](https://docs.cloud.google.com/pubsub/lite/docs/publishing) some messages to your Lite topic.
    
    
    gcloud pubsub lite-topics publish $TOPIC \
        --location=$LITE_LOCATION \
        --message="Hello World!"

You may have to wait a few minutes to see the messages in your Worker Logs.

Use the command below to check which files have been written out to Cloud Storage.
    
    
    gcloud storage ls "gs://$BUCKET/samples/"

The output should look like the following:
    
    
     gs://$BUCKET/samples/output-19:41-19:42-0-of-1
     gs://$BUCKET/samples/output-19:47-19:48-0-of-1
     gs://$BUCKET/samples/output-19:48-19:49-0-of-1
    

Use the command below to look at the content in a file:
    
    
    gcloud storage cat "gs://$BUCKET/samples/your-filename"

## Optional: Create a Dataflow template

You can optionally create a custom [Dataflow Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates) based on your pipeline. Dataflow templates let you run jobs with different input parameters from Google Cloud console or the command line without the need to set up a full Java development environment.

  1. Create a fat JAR that includes all the dependencies of your pipeline. You should see `target/pubsublite-streaming-bundled-1.0.jar` after the command has run.
         
         mvn clean package -DskipTests=true

  2. Provide names and locations for your template file and template container image.
         
         export TEMPLATE_PATH="gs://$BUCKET/samples/your-template-file.json"
         export TEMPLATE_IMAGE="gcr.io/$PROJECT_ID/your-template-image:latest"

  3. Build a custom flex template. A required [`metadata.json`](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/pubsublite/streaming-analytics/metadata.json) file, which contains the necessary spec to run the job, has been provided with the example.
         
         gcloud dataflow flex-template build $TEMPLATE_PATH \
             --image-gcr-path $TEMPLATE_IMAGE \
             --sdk-language "JAVA" \
             --flex-template-base-image "JAVA11" \
             --metadata-file "metadata.json" \
             --jar "target/pubsublite-streaming-bundled-1.0.jar" \
             --env FLEX_TEMPLATE_JAVA_MAIN_CLASS="examples.PubsubliteToGcs"

  4. Run a job using the custom flex template.

**Note:** Pub/Sub Lite allows only one subscriber to pull messages from one partition. If your topic is configured to have only one partition and you use its subscription in more than one Dataflow jobs, only one job will receive messages.



### Console

  1. [**Create job from template**](https://console.cloud.google.com/dataflow/createjob?project=).

  2. Enter a **Job name**.

  3. Enter your **Dataflow region**.

  4. Choose your **Custom Template**.

  5. Enter your **template path**.

  6. Enter the required parameters.

  7. Click **Run job**.




### gcloud
    
    
    gcloud dataflow flex-template run "pubsublite-to-gcs-`date +%Y%m%d`" \
         --template-file-gcs-location $TEMPLATE_PATH \
         --parameters subscription="projects/$PROJECT_ID/locations/$LITE_LOCATION/subscriptions/$SUBSCRIPTION" \
         --parameters output="gs://$BUCKET/samples/template-output" \
         --parameters windowSize=1 \
         --region $DATAFLOW_REGION \ 
         --serviceAccount=$SERVICE_ACCOUNT

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  1. In the Dataflow console, stop the job. Cancel the pipeline instead of draining it.

  2. Delete the topic and subscription.
         
         gcloud pubsub lite-topics delete $TOPIC
         gcloud pubsub lite-subscriptions delete $SUBSCRIPTION

  3. Delete the files created by the pipeline.
         
         gcloud storage rm "gs://$BUCKET/samples/*" --recursive --continue-on-error
         gcloud storage rm "gs://$BUCKET/temp/*" --recursive --continue-on-error

  4. Delete the template image and the template file if they exist.
         
         gcloud container images delete $TEMPLATE_IMAGE
         gcloud storage rm $TEMPLATE_PATH

  5. Remove the Cloud Storage bucket.
         
         gcloud storage rm gs://$BUCKET --recursive

  6. Delete the service account: 
         
         gcloud iam service-accounts delete SERVICE_ACCOUNT_EMAIL

  7. Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
         
         gcloud auth application-default revoke

  8. Optional: Revoke credentials from the gcloud CLI. 
         
         gcloud auth revoke




## What's next

  * Read more about [Configuring Dataflow Flex Templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates).

  * Understand Dataflow [streaming pipelines](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
