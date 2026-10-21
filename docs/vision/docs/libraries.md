---
url: https://docs.cloud.google.com/vision/docs/libraries/
title: Vision client libraries \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:06.458063+00:00
---

# Vision client libraries  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/docs/apis)



Send feedback 

#  Vision client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Vision API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

**Note:** Additional client libraries are available for Java applications.

## Install the client library

### C++

See [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup) for details about this client library's requirements and install dependencies.

### C#

If you are using Visual Studio 2017 or higher, open nuget package manager window and type the following: 
    
    
    Install-Package Google.Apis

If you are using .NET Core command-line interface tools to install your dependencies, run the following command:
    
    
    dotnet add package Google.Apis

For more information, see [Setting Up a C# Development Environment](https://docs.cloud.google.com/dotnet/docs/setup).

### Go
    
    
    go get cloud.google.com/go/vision/apiv1

For more information, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

### Java

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

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    npm install @google-cloud/vision

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### PHP
    
    
    composer require google/apiclient

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

### Python

**Note:** See the [migration guide](https://docs.cloud.google.com/vision/docs/python-client-migration) for information about migrating to Python client library v0.25.1. 
    
    
    pip install --upgrade google-cloud-vision

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

### Ruby
    
    
    gem install google-api-client

For more information, see [Setting Up a Ruby Development Environment](https://docs.cloud.google.com/ruby/docs/setup).

## Set up authentication

To authenticate calls to Google Cloud APIs, client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

For production environments, the way you set up ADC depends on the service and context. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

For a local development environment, you can set up ADC with the credentials that are associated with your Google Account:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




## Use the client library

The following example shows how to use the client library. 

### C++
    
    
    #include "google/cloud/vision/v1/image_annotator_client.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      auto constexpr kDefaultUri =
          "gs://cloud-samples-data/vision/label/wakeupcat.jpg";
      if (argc > 2) {
        std::cerr << "Usage: " << argv[0] << " [gcs-uri]\n"
                  << "  The gcs-uri must be in gs://... format. It defaults to "
                  << kDefaultUri << "\n";
        return 1;
      }
      auto uri = std::string{argc == 2 ? argv[1] : kDefaultUri};
    
      namespace vision = ::google::cloud::vision_v1;
      auto client =
          vision::ImageAnnotatorClient(vision::MakeImageAnnotatorConnection());
    
      // Define the image we want to annotate
      google::cloud::vision::v1::Image image;
      image.mutable_source()->set_image_uri(uri);
      // Create a request to annotate this image with Request text annotations for a
      // file stored in GCS.
      google::cloud::vision::v1::AnnotateImageRequest request;
      *request.mutable_image() = std::move(image);
      request.add_features()->set_type(
          google::cloud::vision::v1::Feature::TEXT_DETECTION);
    
      google::cloud::vision::v1::BatchAnnotateImagesRequest batch_request;
      *batch_request.add_requests() = std::move(request);
      auto batch = client.BatchAnnotateImages(batch_request);
      if (!batch) throw std::move(batch).status();
    
      // Find the longest annotation and print it
      auto result = std::string{};
      for (auto const& response : batch->responses()) {
        for (auto const& annotation : response.text_annotations()) {
          if (result.size() < annotation.description().size()) {
            result = annotation.description();
          }
        }
      }
      std::cout << "The image contains this text: " << result << "\n";
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### Go
    
    
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
    
    

## Additional resources

### C++

The following list contains links to more resources related to the client library for C++:

  * [API reference](https://docs.cloud.google.com/cpp/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [`google-cloud-vision` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-vision%5D%5Bc%2B%2B%5D)
  * [Source code](https://github.com/googleapis/google-cloud-cpp)



### C#

The following list contains links to more resources related to the client library for C#:

  * [API reference](https://developers.google.com/api-client-library/dotnet)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-dotnet-client/issues)
  * [`google-cloud-vision` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-vision%5D+%5Bc%23%5D)
  * [Source code](https://github.com/google/google-api-dotnet-client)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://docs.cloud.google.com/go/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * [`google-cloud-vision` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-vision%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://docs.cloud.google.com/java/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-java/issues)
  * [`google-cloud-vision` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-vision%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/google-cloud-java)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://docs.cloud.google.com/nodejs/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/nodejs-vision/issues)
  * [`google-cloud-vision` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-vision%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/googleapis/nodejs-vision)



### PHP

The following list contains links to more resources related to the client library for PHP:

  * [API reference](https://developers.google.com/api-client-library/php/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-php-client/issues)
  * [`google-cloud-vision` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-vision%5D+%5Bphp%5D)
  * [Source code](https://github.com/google/google-api-php-client)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://docs.cloud.google.com/python/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-python/issues)
  * [`google-cloud-vision` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-vision%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/google-cloud-python)



### Ruby

The following list contains links to more resources related to the client library for Ruby:

  * [API reference](https://developers.google.com/api-client-library/ruby/apis/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-ruby-client/issues)
  * [`google-cloud-vision` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-vision%5D+%5Bruby%5D)
  * [Source code](https://github.com/google/google-api-ruby-client)



## Additional client libraries

In addition to the libraries shown above, [Spring Cloud Google Cloud](https://spring.io/projects/spring-cloud-gcp) is available for Java applications. Spring Vision API helps you use Cloud Vision in any application that's built with the [Spring Framework](https://spring.io/projects/spring-framework).

To get started, learn how to [add Spring Cloud Vision to your application](https://docs.cloud.google.com/vision/docs/adding-spring).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Vision API performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Vision API free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
