---
url: https://docs.cloud.google.com/video-intelligence/docs/annotate-video-client-libraries/
title: Quickstart: Annotate a video by using client libraries \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:06.625034+00:00
---

# Quickstart: Annotate a video by using client libraries  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/annotate-video-client-libraries/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Annotate a video by using client libraries

This quickstart introduces you to Video Intelligence API. In this quickstart, you set up your Google Cloud project and authorization and then make a request for Video Intelligence to annotate a video.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Video Intelligence API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=videointelligence.googleapis.com)

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

  10. Enable the Cloud Video Intelligence API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=videointelligence.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Install the client library

### Go
    
    
    go get cloud.google.com/go/videointelligence/apiv1

### Java

If you are using [Maven](https://maven.apache.org/), add the following to your `pom.xml` file. For more information about BOMs, see [The Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.90.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-video-intelligence</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-video-intelligence'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-video-intelligence" % "2.98.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

### Node.js

Before installing the library, make sure you've [prepared your environment for Node.js development](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    npm install @google-cloud/video-intelligence

### Python

Before installing the library, make sure you've [prepared your environment for Python development](https://docs.cloud.google.com/python/docs/setup).
    
    
    pip install --upgrade google-cloud-videointelligence

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

## Set up authentication

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




## Label detection

**Caution:** VPC Service Controls egress restrictions are not enforced on the `outputUri` of `videos:annotate` requests. The service can write annotation results to a Cloud Storage bucket outside of your service perimeter. For details, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#videointelligence).

Now you can use the Video Intelligence API to request information from a video or video segment, such as label detection. Run the following code to perform your first video label detection request:

### Go
    
    
    // Sample video_quickstart uses the Google Cloud Video Intelligence API to label a video.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/golang/protobuf/ptypes"
    
    	video "cloud.google.com/go/videointelligence/apiv1"
    	videopb "cloud.google.com/go/videointelligence/apiv1/videointelligencepb"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := video.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_Close)()
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		InputUri: "gs://cloud-samples-data/video/cat.mp4",
    		Features: []videopb.Feature{
    			videopb.Feature_LABEL_DETECTION,
    		},
    	})
    	if err != nil {
    		log.Fatalf("Failed to start annotation job: %v", err)
    	}
    
    	resp, err := op.[Wait](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_AnnotateVideoOperation_Wait)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to annotate: %v", err)
    	}
    
    	// Only one video was processed, so get the first result.
    	result := resp.GetAnnotationResults()[0]
    
    	for _, annotation := range result.SegmentLabelAnnotations {
    		fmt.Printf("Description: %s\n", annotation.Entity.Description)
    
    		for _, category := range annotation.CategoryEntities {
    			fmt.Printf("\tCategory: %s\n", category.Description)
    		}
    
    		for _, segment := range annotation.Segments {
    			start, _ := ptypes.Duration(segment.Segment.StartTimeOffset)
    			end, _ := ptypes.Duration(segment.Segment.EndTimeOffset)
    			fmt.Printf("\tSegment: %s to %s\n", start, end)
    			fmt.Printf("\tConfidence: %v\n", segment.Confidence)
    		}
    	}
    }
    

### Java
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoProgress.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html);
    import com.google.cloud.videointelligence.v1.[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html);
    import com.google.cloud.videointelligence.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html);
    import com.google.cloud.videointelligence.v1.[LabelAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LabelAnnotation.html);
    import com.google.cloud.videointelligence.v1.[LabelSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LabelSegment.html);
    import com.google.cloud.videointelligence.v1.[VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html);
    import com.google.cloud.videointelligence.v1.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html);
    import java.util.List;
    
    public class QuickstartSample {
    
      /** Demonstrates using the video intelligence client to detect labels in a video file. */
      public static void main(String[] args) throws Exception {
        // Instantiate a video intelligence client
        try ([VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html) client = [VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html).create()) {
          // The Google Cloud Storage path to the video to annotate.
          String gcsUri = "gs://cloud-samples-data/video/cat.mp4";
    
          // Create an operation that will contain the response when the operation completes.
          [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html) request =
              [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html).newBuilder()
                  .setInputUri(gcsUri)
                  .[addFeatures](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_addFeatures_com_google_cloud_videointelligence_v1_Feature_)([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html).LABEL_DETECTION)
                  .build();
    
          OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> response =
              client.[annotateVideoAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html#com_google_cloud_videointelligence_v1_VideoIntelligenceServiceClient_annotateVideoAsync_com_google_cloud_videointelligence_v1_AnnotateVideoRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
    
          List<VideoAnnotationResults> results = response.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getAnnotationResultsList();
          if (results.isEmpty()) {
            System.out.println("No labels detected in " + gcsUri);
            return;
          }
          for ([VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html) result : results) {
            System.out.println("Labels:");
            // get video segment label annotations
            for ([LabelAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LabelAnnotation.html) annotation : result.getSegmentLabelAnnotationsList()) {
              System.out.println(
                  "Video label description : " + annotation.getEntity().getDescription());
              // categories
              for ([Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html) categoryEntity : annotation.getCategoryEntitiesList()) {
                System.out.println("Label Category description : " + categoryEntity.getDescription());
              }
              // segments
              for ([LabelSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LabelSegment.html) segment : annotation.getSegmentsList()) {
                double startTime =
                    segment.getSegment().getStartTimeOffset().getSeconds()
                        + segment.getSegment().getStartTimeOffset().getNanos() / 1e9;
                double endTime =
                    segment.getSegment().getEndTimeOffset().getSeconds()
                        + segment.getSegment().getEndTimeOffset().getNanos() / 1e9;
                System.out.printf("Segment location : %.3f:%.3f\n", startTime, endTime);
                System.out.println("Confidence : " + segment.getConfidence());
              }
            }
          }
        }
      }
    }

### Node.js

Before running the example, make sure you've [prepared your environment for Node.js development](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    // Imports the Google Cloud Video Intelligence library
    const videoIntelligence = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)');
    
    // Creates a client
    const client = new videoIntelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    // The GCS uri of the video to analyze
    const gcsUri = 'gs://cloud-samples-data/video/cat.mp4';
    
    // Construct request
    const request = {
      inputUri: gcsUri,
      features: ['LABEL_DETECTION'],
    };
    
    // Execute request
    const [operation] = await client.annotateVideo(request);
    
    console.log(
      'Waiting for operation to complete... (this may take a few minutes)'
    );
    
    const [operationResult] = await operation.promise();
    
    // Gets annotations for video
    const annotations = operationResult.annotationResults[0];
    
    // Gets labels for video from its annotations
    const labels = annotations.segmentLabelAnnotations;
    labels.forEach(label => {
      console.log(`Label ${label.entity.description} occurs at:`);
      label.segments.forEach(segment => {
        segment = segment.segment;
        console.log(
          `\tStart: ${segment.startTimeOffset.seconds}` +
            `.${(segment.startTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
        console.log(
          `\tEnd: ${segment.endTimeOffset.seconds}.` +
            `${(segment.endTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
      });
    });

### Python

Before running the example, make sure you've [prepared your environment for Python development](https://docs.cloud.google.com/python/docs/setup).
    
    
    from google.cloud import videointelligence
    
    video_client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
    features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).LABEL_DETECTION]
    operation = video_client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
        request={
            "features": features,
            "input_uri": "gs://cloud-samples-data/video/cat.mp4",
        }
    )
    print("\nProcessing video for label annotations:")
    
    result = operation.result(timeout=180)
    print("\nFinished processing.")
    
    # first result is retrieved because a single video was processed
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        print("Video label description: {}".format(segment_label.entity.description))
        for category_entity in segment_label.category_entities:
            print(
                "\tLabel category description: {}".format(category_entity.description)
            )
    
        for i, segment in enumerate(segment_label.segments):
            start_time = (
                segment.segment.start_time_offset.seconds
                + segment.segment.start_time_offset.microseconds / 1e6
            )
            end_time = (
                segment.segment.end_time_offset.seconds
                + segment.segment.end_time_offset.microseconds / 1e6
            )
            positions = "{}s to {}s".format(start_time, end_time)
            confidence = segment.confidence
            print("\tSegment {}: {}".format(i, positions))
            print("\tConfidence: {}".format(confidence))
        print("\n")

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

Congratulations! You've sent your first request to Video Intelligence API.

## How did it go?

It worked!  **Great!** What did you like about the quickstart? What could we have done better?  Let us know!.  I got stuck.  **We're sorry to hear that.** Let us know what went wrong. We'll want to fix it. 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  * Use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you don't need it.



## What's next

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
