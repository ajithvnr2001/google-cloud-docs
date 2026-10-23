---
url: https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries/
title: Quickstart: Detect labels in an image by using client libraries \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:21.368468+00:00
---

# Quickstart: Detect labels in an image by using client libraries  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Detect labels in an image by using client libraries

This page shows you how to get started with the Vision API in your favorite programming language. 

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=vision--detect-labels-image-client-libraries-python)

* * *

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

  7. Enable the Vision API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable vision.googleapis.com

  8. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/storage.objectViewer`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

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

  14. Enable the Vision API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable vision.googleapis.com

  15. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/storage.objectViewer`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.




## Install the client library

### Go

Create a project directory, initialize a Go module, and then download the client library:
    
    
    mkdir my-vision-app && cd my-vision-app
    go mod init example.com/vision-app
    go get cloud.google.com/go/vision/apiv1

### Java

For more on setting up your Java development environment, refer to the [Java Development Environment Setup Guide](https://docs.cloud.google.com/java/docs/setup). 

**Note:** If your application uses the Spring Framework, a [Spring module](https://docs.cloud.google.com/vision/docs/adding-spring) is also available. 

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
        <artifactId>google-cloud-vision</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-vision'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-vision" % "3.97.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

### Node.js

For more on setting up your Node.js development environment, refer to the [Node.js Development Environment Setup Guide](https://docs.cloud.google.com/nodejs/docs/setup). 
    
    
    npm install @google-cloud/vision

### Python

For more on setting up your Python development environment, refer to the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup). 
    
    
    pip install --upgrade google-cloud-vision

## Label detection samples

Now you can use the Vision API to request information from an image, such as label detection. Run the following code to perform your first image label detection request.

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample vision-quickstart uses the Google Cloud Vision API to label an image.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"os"
    
    	vision "cloud.google.com/go/vision/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := vision.[NewImageAnnotatorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_ImageAnnotatorClient_NewImageAnnotatorClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.Close()
    
    	// Sets the name of the image file to annotate.
    	filename := "../testdata/cat.jpg"
    
    	file, err := os.Open(filename)
    	if err != nil {
    		log.Fatalf("Failed to read file: %v", err)
    	}
    	defer file.Close()
    	image, err := vision.[NewImageFromReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_NewImageFromReader)(file)
    	if err != nil {
    		log.Fatalf("Failed to create image: %v", err)
    	}
    
    	labels, err := client.[DetectLabels](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_ImageAnnotatorClient_DetectLabels)(ctx, image, nil, 10)
    	if err != nil {
    		log.Fatalf("Failed to detect labels: %v", err)
    	}
    
    	fmt.Println("Labels:")
    	for _, label := range labels {
    		fmt.Println(label.Description)
    	}
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[EntityAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.EntityAnnotation.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).[Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    import java.util.ArrayList;
    import java.util.List;
    
    public class QuickstartSample {
      public static void main(String... args) throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) vision = [ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html).create()) {
    
          // The path to the image file to annotate
          String fileName = "./resources/wakeupcat.jpg";
    
          // Reads the image file into memory
          Path path = Paths.get(fileName);
          byte[] data = Files.readAllBytes(path);
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) imgBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(data);
    
          // Builds the image annotation request
          List<AnnotateImageRequest> requests = new ArrayList<>();
          [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) img = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html).newBuilder().setContent(imgBytes).build();
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feat = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html).LABEL_DETECTION).build();
          [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html) request =
              [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html).newBuilder().addFeatures(feat).setImage(img).build();
          requests.add(request);
    
          // Performs label detection on the image file
          [BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html) response = vision.batchAnnotateImages(requests);
          List<AnnotateImageResponse> responses = response.[getResponsesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html#com_google_cloud_vision_v1_BatchAnnotateImagesResponse_getResponsesList__)();
    
          for ([AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html) res : responses) {
            if (res.hasError()) {
              System.out.format("Error: %s%n", res.getError().getMessage());
              return;
            }
    
            for ([EntityAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.EntityAnnotation.html) annotation : res.getLabelAnnotationsList()) {
              annotation
                  .getAllFields()
                  .forEach((k, v) -> System.out.format("%s : %s%n", k, v.toString()));
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function quickstart() {
      // Imports the Google Cloud client library
      const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
      // Creates a client
      const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
      // Performs label detection on the image file
      const [result] = await client.labelDetection('./resources/wakeupcat.jpg');
      const labels = result.labelAnnotations;
      console.log('Labels:');
      labels.forEach(label => console.log(label.description));
    }
    quickstart();

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    from google.cloud import vision
    
    
    
    def run_quickstart() -> vision.EntityAnnotation:
        """Provides a quick start example for Cloud Vision."""
    
        # Instantiates a client
        client = vision.ImageAnnotatorClient()
    
        # The URI of the image file to annotate
        file_uri = "gs://cloud-samples-data/vision/label/wakeupcat.jpg"
    
        image = vision.Image()
        image.source.image_uri = file_uri
    
        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations
    
        print("Labels:")
        for label in labels:
            print(label.description)
    
        return labels
    
    

## Run the sample

To run the prior samples, use the following commands. If you cloned the GitHub repository for the specific sample language, uncomment the first line:

###  Go 
    
    
    # cd golang-samples/vision/vision_quickstart/
    go run .
    

###  Java 
    
    
    # cd java-docs-samples/vision/snippets/src/main/java/com/example/vision/quickstart/
    javac QuickstartSample.java
    java QuickstartSample.java
    

###  Node.js 
    
    
    # cd nodejs-docs-samples/vision/
    node quickstart.js
    

###  Python 
    
    
    # cd python-docs-samples/vision/snippets/quickstart
    python -c 'import quickstart; quickstart.run_quickstart()'
    

Congratulations! You've sent your first request to Vision. 

## How did it go?

It worked!  **Great!** What did you like about the quickstart? What could we have done better?  Let us know!.  I got stuck.  **We're sorry to hear that.** Let us know what went wrong. We'll want to fix it. 

## Clean up

To avoid incurring charges to your Google Account for the resources used in this quickstart: 

  * Use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you do not need it.



## What's next

Find out more about our [Vision API Client Libraries](https://docs.cloud.google.com/vision/docs/reference/libraries). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
