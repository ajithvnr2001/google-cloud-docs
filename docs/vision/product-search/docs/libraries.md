---
url: https://docs.cloud.google.com/vision/product-search/docs/libraries/
title: Vision API Product Search client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:08.138140+00:00
---

# Vision API Product Search client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/libraries/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/product-search/docs/apis)



Send feedback 

#  Vision API Product Search client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Vision API Product Search. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

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
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    )
    
    // getSimilarProductsURI searches for products from a product set similar to products in an image file on GCS.
    func getSimilarProductsURI(w io.Writer, projectID string, location string, productSetID string, productCategory string, imageURI string, filter string) error {
    	ctx := context.Background()
    	c, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImageAnnotatorClient: %w", err)
    	}
    	defer c.Close()
    
    	image := vision.[NewImageFromURI](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_NewImageFromURI)(imageURI)
    
    	ictx := &visionpb.[ImageContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ImageContext){
    		ProductSearchParams: &visionpb.[ProductSearchParams](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ProductSearchParams){
    			ProductSet:        fmt.Sprintf("projects/%s/locations/%s/productSets/%s", projectID, location, productSetID),
    			ProductCategories: []string{productCategory},
    			Filter:            filter,
    		},
    	}
    
    	response, err := c.[ProductSearch](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_ImageAnnotatorClient_ProductSearch)(ctx, image, ictx)
    	if err != nil {
    		return fmt.Errorf("ProductSearch: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product set index time:\n")
    	fmt.Fprintf(w, "seconds: %d\n", response.IndexTime.Seconds)
    	fmt.Fprintf(w, "nanos: %d\n", response.IndexTime.Nanos)
    
    	fmt.Fprintf(w, "Search results:\n")
    	for _, result := range response.Results {
    		fmt.Fprintf(w, "Score(Confidence): %f\n", result.Score)
    		fmt.Fprintf(w, "Image name: %s\n", result.[Image](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Image))
    
    		fmt.Fprintf(w, "Prodcut name: %s\n", result.[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Product).Name)
    		fmt.Fprintf(w, "Product display name: %s\n", result.[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Product).DisplayName)
    		fmt.Fprintf(w, "Product labels: %s\n", result.[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Product).ProductLabels)
    	}
    
    	return nil
    }
    

### Java
    
    
    /**
     * Search similar products to image in local file.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productSetId - Id of the product set.
     * @param productCategory - Category of the product.
     * @param filePath - Local file path of the image to be searched
     * @param filter - Condition to be applied on the labels. Example for filter: (color = red OR
     *     color = blue) AND style = kids It will search on all products with the following labels:
     *     color:red AND style:kids color:blue AND style:kids
     * @throws IOException - on I/O errors.
     */
    public static void getSimilarProductsFile(
        String projectId,
        String computeRegion,
        String productSetId,
        String productCategory,
        String filePath,
        String filter)
        throws IOException {
      try (ImageAnnotatorClient queryImageClient = ImageAnnotatorClient.create()) {
    
        // Get the full path of the product set.
        String productSetPath = ProductSetName.format(projectId, computeRegion, productSetId);
    
        // Read the image as a stream of bytes.
        File imgPath = new File(filePath);
        byte[] content = Files.readAllBytes(imgPath.toPath());
    
        // Create annotate image request along with product search feature.
        Feature featuresElement = Feature.newBuilder().setType(Type.PRODUCT_SEARCH).build();
        // The input image can be a HTTPS link or Raw image bytes.
        // Example:
        // To use HTTP link replace with below code
        //  ImageSource source = ImageSource.newBuilder().setImageUri(imageUri).build();
        //  Image image = Image.newBuilder().setSource(source).build();
        Image image = Image.newBuilder().setContent(ByteString.copyFrom(content)).build();
        ImageContext imageContext =
            ImageContext.newBuilder()
                .setProductSearchParams(
                    ProductSearchParams.newBuilder()
                        .setProductSet(productSetPath)
                        .addProductCategories(productCategory)
                        .setFilter(filter))
                .build();
    
        AnnotateImageRequest annotateImageRequest =
            AnnotateImageRequest.newBuilder()
                .addFeatures(featuresElement)
                .setImage(image)
                .setImageContext(imageContext)
                .build();
        List<AnnotateImageRequest> requests = Arrays.asList(annotateImageRequest);
    
        // Search products similar to the image.
        BatchAnnotateImagesResponse response = queryImageClient.batchAnnotateImages(requests);
    
        List<Result> similarProducts =
            response.getResponses(0).getProductSearchResults().getResultsList();
        System.out.println("Similar Products: ");
        for (Result product : similarProducts) {
          System.out.println(String.format("\nProduct name: %s", product.getProduct().getName()));
          System.out.println(
              String.format("Product display name: %s", product.getProduct().getDisplayName()));
          System.out.println(
              String.format("Product description: %s", product.getProduct().getDescription()));
          System.out.println(String.format("Score(Confidence): %s", product.getScore()));
          System.out.println(String.format("Image name: %s", product.getImage()));
        }
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    // Creates a client
    const productSearchClient = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    const imageAnnotatorClient = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function getSimilarProductsGcs(
      projectId,
      location,
      productSetId,
      productCategory,
      filePath,
      filter
    ) {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productSetId = 'Id of the product set';
      // const productCategory = 'Category of the product';
      // const filePath = 'Local file path of the image to be searched';
      // const filter = 'Condition to be applied on the labels';
      const productSetPath = productSearchClient.productSetPath(
        projectId,
        location,
        productSetId
      );
    
      const request = {
        // The input image can be a GCS link or HTTPS link or Raw image bytes.
        // Example:
        // To use GCS link replace with below code
        // image: {source: {gcsImageUri: filePath}}
        // To use HTTP link replace with below code
        // image: {source: {imageUri: filePath}}
        image: {source: {gcsImageUri: filePath}},
        features: [{type: 'PRODUCT_SEARCH'}],
        imageContext: {
          productSearchParams: {
            productSet: productSetPath,
            productCategories: [productCategory],
            filter: filter,
          },
        },
      };
      console.log(request.image);
    
      const [response] = await imageAnnotatorClient.batchAnnotateImages({
        requests: [request],
      });
      console.log('Search Image:', filePath);
      console.log('\nSimilar product information:');
    
      const results = response['responses'][0]['productSearchResults']['results'];
      results.forEach(result => {
        console.log('Product id:', result['product'].name.split('/').pop(-1));
        console.log('Product display name:', result['product'].displayName);
        console.log('Product description:', result['product'].description);
        console.log('Product category:', result['product'].productCategory);
      });
    }
    getSimilarProductsGcs();

### Python
    
    
    from google.cloud import vision
    
    def get_similar_products_uri(
        project_id, location, product_set_id, product_category, image_uri, filter
    ):
        """Search similar products to image.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
            product_category: Category of the product.
            image_uri: Cloud Storage location of image to be searched.
            filter: Condition to be applied on the labels.
            Example for filter: (color = red OR color = blue) AND style = kids
            It will search on all products with the following labels:
            color:red AND style:kids
            color:blue AND style:kids
        """
        # product_search_client is needed only for its helper methods.
        product_search_client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
        image_annotator_client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        # Create annotate image request along with product search feature.
        image_source = vision.[ImageSource](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ImageSource.html)(image_uri=image_uri)
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(source=image_source)
    
        # product search specific parameters
        product_set_path = product_search_client.[product_set_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_set_path)(
            project=project_id, location=location, product_set=product_set_id
        )
        product_search_params = vision.[ProductSearchParams](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ProductSearchParams.html)(
            product_set=product_set_path,
            product_categories=[product_category],
            filter=filter,
        )
        image_context = vision.[ImageContext](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ImageContext.html)(product_search_params=product_search_params)
    
        # Search products similar to the image.
        response = image_annotator_client.[product_search](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.html)(image, image_context=image_context)
    
        index_time = response.product_search_results.index_time
        print("Product set index time: ")
        print(index_time)
    
        results = response.product_search_results.results
    
        print("Search results:")
        for result in results:
            product = result.product
    
            print(f"Score(Confidence): {result.score}")
            print(f"Image name: {result.image}")
    
            print(f"Product name: {product.name}")
            print("Product display name: {}".format(product.display_name))
            print(f"Product description: {product.description}\n")
            print(f"Product labels: {product.product_labels}\n")
    
    

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



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Vision API performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Vision API free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
