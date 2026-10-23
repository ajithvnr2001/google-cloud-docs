---
url: https://docs.cloud.google.com/vision/product-search/docs/tutorial/
title: Product Search Tutorial \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:51.577048+00:00
---

# Product Search Tutorial  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/tutorial/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/product-search/docs/create-product-set-search-products)



Send feedback 

#  Product Search Tutorial Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates how to create a product set which contains a group of products with reference images for those products. The tutorial shows users how to create a product set via online (individual) import. After the product set has been indexed, you can query the product set using Vision API Product Search.

**Note:**

The Product Search index of products is updated approximately every day. When images are added or deleted, the change won't be reflected in your Product Search responses until the index is next updated.

To make sure that indexing has completed successfully, check the [`indexTime`](https://cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.productSets#ProductSet) field of a product set.

In this tutorial, you will learn how to:

  1. Create a product set through online (individual) import
  2. Create an individual product
  3. Add a product to a product set
  4. Update a product
  5. Create a reference image
  6. Search for similar products



## Before you begin

Before you begin this tutorial make sure you have installed the appropriate [client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries), [enabled billing and the API](https://docs.cloud.google.com/vision/product-search/docs/before-you-begin) for your project, and have properly [set up authentication](https://docs.cloud.google.com/vision/product-search/docs/auth).

## Import Libraries

To use the Vision API Product Search, import the following modules after downloading and installing the [client library](https://docs.cloud.google.com/vision/product-search/docs/libraries):

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    )
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.vision.v1.[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchOperationMetadata.html);
    import com.google.cloud.vision.v1.[ImportProductSetsGcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImportProductSetsGcsSource.html);
    import com.google.cloud.vision.v1.[ImportProductSetsGcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImportProductSetsGcsSource.html).Builder;
    import com.google.cloud.vision.v1.[ImportProductSetsInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImportProductSetsInputConfig.html);
    import com.google.cloud.vision.v1.[ImportProductSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImportProductSetsResponse.html);
    import com.google.cloud.vision.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.LocationName.html);
    import com.google.cloud.vision.v1.[ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html);
    import com.google.cloud.vision.v1.[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ReferenceImage.html);
    import java.io.PrintStream;
    import javax.swing.JPanel;
    import net.sourceforge.argparse4j.ArgumentParsers;
    import net.sourceforge.argparse4j.inf.ArgumentParser;
    import net.sourceforge.argparse4j.inf.ArgumentParserException;
    import net.sourceforge.argparse4j.inf.Namespace;
    import net.sourceforge.argparse4j.inf.Subparser;
    import net.sourceforge.argparse4j.inf.Subparsers;
    

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Running the Application

**Viewing Code Samples:** Most of the code samples in this tutorial are taken from larger code files located in [GitHub](https://github.com/). You can view and download the complete file from which a code sample is taken by clicking the "View on GitHub" button provided above a sample.

## Step 1: Create a Product Catalog

Users have two options for creating a product catalog, either via batch import using a CSV file, which allows an entire product catalog to be imported in a single API call, or via online import, which offers you control over your product sets and allows for management of one resource or relationship at a time. This primarily means individual creation of product sets, products, and reference images. Online import also allows you to incrementally update a product catalog you have already created via batch import.

In this tutorial you will use online import. See the [Quickstart](https://docs.cloud.google.com/vision/product-search/docs/quickstart) for an example of batch import with a CSV.

### Online (Individual) Import

### 1\. Create a Product Set

Create an empty Product Set which is a simple container for a group of products.

#### Request

Create an empty Product Set and name it "PS_CLOTH-SHOE_070318" by executing the following request using the method `create_product_set()`. Pass the product set id and display name as arguments.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * DISPLAY_NAME: A string display name of your choosing.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets

Request JSON body: 
    
    
    {
      "displayName": "display-name"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

You should see output similar to the following. You can use the product set ID (`b6d809615b6dd675`, in this case) to perform other operations on the product set.
    
    
    {
      "name": "projects/project-id/locations/location-id/productSets/**b6d809615b6dd675** ",
      "displayName": "new-product-set"
    }
    

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    )
    
    // createProductSet creates a product set.
    func createProductSet(w io.Writer, projectID string, location string, productSetID string, productSetDisplayName string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[CreateProductSetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_CreateProductSetRequest){
    		Parent:       fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		ProductSetId: productSetID,
    		ProductSet: &visionpb.[ProductSet](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ProductSet){
    			DisplayName: productSetDisplayName,
    		},
    	}
    
    	resp, err := c.CreateProductSet(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateProductSet: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product set name: %s\n", resp.Name)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Create a product set
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productSetId - Id of the product set.
     * @param productSetDisplayName - Display name of the product set.
     * @throws IOException - on I/O errors.
     */
    public static void createProductSet(
        String projectId, String computeRegion, String productSetId, String productSetDisplayName)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // A resource that represents Google Cloud Platform location.
        String formattedParent = LocationName.format(projectId, computeRegion);
    
        // Create a product set with the product set specification in the region.
        ProductSet myProductSet =
            ProductSet.newBuilder().setDisplayName(productSetDisplayName).build();
        CreateProductSetRequest request =
            CreateProductSetRequest.newBuilder()
                .setParent(formattedParent)
                .setProductSet(myProductSet)
                .setProductSetId(productSetId)
                .build();
        ProductSet productSet = client.createProductSet(request);
        // Display the product set information
        System.out.println(String.format("Product set name: %s", productSet.getName()));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function createProductSet() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productSetId = 'Id of the product set';
      // const productSetDisplayName = 'Display name of the product set';
    
      // Resource path that represents Google Cloud Platform location.
      const locationPath = client.locationPath(projectId, location);
    
      const productSet = {
        displayName: productSetDisplayName,
      };
    
      const request = {
        parent: locationPath,
        productSet: productSet,
        productSetId: productSetId,
      };
    
      const [createdProductSet] = await client.createProductSet(request);
      console.log(`Product Set name: ${createdProductSet.name}`);
    }
    createProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def create_product_set(project_id, location, product_set_id, product_set_display_name):
        """Create a product set.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
            product_set_display_name: Display name of the product set.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # A resource that represents Google Cloud Platform location.
        location_path = f"projects/{project_id}/locations/{location}"
    
        # Create a product set with the product set specification in the region.
        product_set = vision.[ProductSet](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ProductSet.html)(display_name=product_set_display_name)
    
        # The response is the product set with `name` populated.
        response = client.[create_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_create_product_set)(
            parent=location_path, product_set=product_set, product_set_id=product_set_id
        )
    
        # Display the product set information.
        print(f"Product set name: {response.name}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

#### Response
    
    
    Product set name: projects/prj-prod-search-tutorials/locations/us-east1/productSets/PS_CLOTH-SHOE_070318
    Product set id: PS_CLOTH-SHOE_070318
    Product set display name: CLOTH-SHOE
    

### 2\. Create a Product

After a product set has been created, the next step is to create a product. Create a product by executing the following request.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * DISPLAY_NAME: A string display name of your choosing.
  * PRODUCT_DESCRIPTION: A string description of your choosing.
  * product-category: A valid product category. The following product categories are currently available: `homegoods-v2`, `apparel-v2`, `toys-v2`, `packagedgoods-v1`, and `general-v1` .
  * `productLabels`: One or more key-value pairs associated with a product. Each KEY_STRING must have an associated VALUE_STRING.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products

Request JSON body: 
    
    
    {
      "displayName": "display-name",
      "description": "product-description",
      "productCategory": "product-category",
      "productLabels": [
          {
            "key": "key-string",
            "value": "value-string"
          }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products" | Select-Object -Expand Content

**Example request body:**
    
    
    {
      "displayName": "sample-product-1234",
      "description": "Athletic shorts",
      "productCategory": "apparel-v2",
      "productLabels": [
          {
            "key": "style",
            "value": "womens"
          },
          {
            "key": "color",
            "value": "blue"
          }
      ]
    }
    

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

You should see output similar to the following. You can use the product ID (`37b9811d308c4e42`, in this case) to perform other operations on the product.
    
    
    {
      "name": "projects/project-id/locations/location-id/products/**37b9811d308c4e42** ",
      "displayName": "sample-product-456",
      "description": "Athletic shorts",
      "productCategory": "apparel-v2",
      "productLabels": [
        {
          "key": "style",
          "value": "womens"
        },
        {
          "key": "color",
          "value": "blue"
        }
      ]
    }
    

###  Creating a product using a specified `productId`

When creating a product resource you have the option of providing a specific product ID with your request.

This information is passed as a query to the request URL (`?productId=product-id`). 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_ID: The ID for the product that is associated with a reference image. This ID is either randomly set or specified by the user at product creation time.
  * DISPLAY_NAME: A string display name of your choosing.
  * PRODUCT_DESCRIPTION: A string description of your choosing.
  * product-category: A valid product category. The following product categories are currently available: `homegoods-v2`, `apparel-v2`, `toys-v2`, `packagedgoods-v1`, and `general-v1` .
  * `productLabels`: One or more key-value pairs associated with a product. Each KEY_STRING must have an associated VALUE_STRING.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products**?productId= product-id**

Request JSON body: 
    
    
    {
      "displayName": "display-name",
      "description": "product-description",
      "productCategory": "product-category",
      "productLabels": [
          {
            "key": "key-string",
            "value": "value-string"
          }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products**?productId= product-id**"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products**?productId= product-id**" | Select-Object -Expand Content

**Example request URL and body:**
    
    
    https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products**?productId=product-id-456**
    
    
    {
      "displayName": "sample-product-456",
      "description": "Athletic shorts",
      "productCategory": "apparel-v2",
      "productLabels": [
          {
            "key": "style",
            "value": "womens"
          },
          {
            "key": "color",
            "value": "blue"
          }
      ]
    }
    

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

You should see output similar to the following. You can use the product ID you set (`**product-id-456**`, in this case) to perform other operations on the product.
    
    
    {
      "name": "projects/project-id/locations/location-id/products/**product-id-456** ",
      "displayName": "sample-product-456",
      "description": "Athletic shorts",
      "productCategory": "apparel-v2",
      "productLabels": [
        {
          "key": "style",
          "value": "womens"
        },
        {
          "key": "color",
          "value": "blue"
        }
      ]
    }

Sending a request with a product ID that already exists produces the following error:
    
    
    {
      "error": {
        "code": 409,
        "message": "Product with ID 'product-id' already exists.",
        "status": "ALREADY_EXISTS",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.DebugInfo",
            "detail": "[ORIGINAL ERROR] generic::already_exists: Product with ID 'product-id' already exists. [google.rpc.error_details_ext] { message: \"Product with ID \\'product-id\\' already exists.\" }"
          }
        ]
      }
    }
    

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    )
    
    // createProduct creates a product.
    func createProduct(w io.Writer, projectID string, location string, productID string, productDisplayName string, productCategory string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[CreateProductRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_CreateProductRequest){
    		Parent:    fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		ProductId: productID,
    		Product: &visionpb.[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Product){
    			DisplayName:     productDisplayName,
    			ProductCategory: productCategory,
    		},
    	}
    
    	resp, err := c.CreateProduct(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateProduct: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product name: %s\n", resp.Name)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Create one product.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @param productDisplayName - Display name of the product.
     * @param productCategory - Category of the product.
     * @throws IOException - on I/O errors.
     */
    public static void createProduct(
        String projectId,
        String computeRegion,
        String productId,
        String productDisplayName,
        String productCategory)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // A resource that represents Google Cloud Platform location.
        String formattedParent = LocationName.format(projectId, computeRegion);
        // Create a product with the product specification in the region.
        // Multiple labels are also supported.
        Product myProduct =
            Product.newBuilder()
                .setName(productId)
                .setDisplayName(productDisplayName)
                .setProductCategory(productCategory)
                .build();
        Product product = client.createProduct(formattedParent, myProduct, productId);
        // Display the product information
        System.out.println(String.format("Product name: %s", product.getName()));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    async function createProduct() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
      // const productDisplayName = 'Display name of the product';
      // const productCategory = 'Catoegory of the product';
    
      // Resource path that represents Google Cloud Platform location.
      const locationPath = client.locationPath(projectId, location);
    
      const product = {
        displayName: productDisplayName,
        productCategory: productCategory,
      };
    
      const request = {
        parent: locationPath,
        product: product,
        productId: productId,
      };
    
      const [createdProduct] = await client.createProduct(request);
      console.log(`Product name: ${createdProduct.name}`);
    }
    createProduct();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    from google.protobuf import field_mask_pb2 as field_mask
    
    def create_product(
        project_id, location, product_id, product_display_name, product_category
    ):
        """Create one product.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
            product_display_name: Display name of the product.
            product_category: Category of the product.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # A resource that represents Google Cloud Platform location.
        location_path = f"projects/{project_id}/locations/{location}"
    
        # Create a product with the product specification in the region.
        # Set product display name and product category.
        product = vision.[Product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Product.html)(
            display_name=product_display_name, product_category=product_category
        )
    
        # The response is the product with the `name` field populated.
        response = client.[create_product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_create_product)(
            parent=location_path, product=product, product_id=product_id
        )
    
        # Display the product information.
        print(f"Product name: {response.name}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

#### Response
    
    
    Product name: projects/prj-prod-search-tutorials/locations/us-east1/products/P_CLOTH-SHOE_46903668_070318
    Product id: P_CLOTH-SHOE_46903668_070318
    Product display name: Blue Dress
    Product category: apparel
    Product description: Short sleeved and 1950s style satin dress
    Product labels:
      Product label 1:
            key: style
            value: women
      Product label 2:
            key: category
            value: dress
      Product label 3:
            key: color
            value: dark-blue
    

### 3\. Add a Product to a Product Set

After a product set and a product have been created, you can add the product to the product set.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_SET_ID: The ID for the product set you want to run the operation on.
  * PRODUCT_NAME: The full resource name of the product. Format: 
    * `projects/PROJECT_ID/locations/LOCATION_ID/products/PRODUCT_ID`



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id:addProduct

Request JSON body: 
    
    
    {
      "product": "product-name"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id:addProduct"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id:addProduct" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    )
    
    // addProductToProductSet adds a product to a product set.
    func addProductToProductSet(w io.Writer, projectID string, location string, productID string, productSetID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[AddProductToProductSetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_AddProductToProductSetRequest){
    		Name:    fmt.Sprintf("projects/%s/locations/%s/productSets/%s", projectID, location, productSetID),
    		Product: fmt.Sprintf("projects/%s/locations/%s/products/%s", projectID, location, productID),
    	}
    
    	if err = c.AddProductToProductSet(ctx, req); err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product added to product set.\n")
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Add a product to a product set.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @param productSetId - Id of the product set.
     * @throws IOException - on I/O errors.
     */
    public static void addProductToProductSet(
        String projectId, String computeRegion, String productId, String productSetId)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product set.
        String formattedName = ProductSetName.format(projectId, computeRegion, productSetId);
    
        // Get the full path of the product.
        String productPath = ProductName.of(projectId, computeRegion, productId).toString();
    
        // Add the product to the product set.
        client.addProductToProductSet(formattedName, productPath);
    
        System.out.println(String.format("Product added to product set."));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function addProductToProductSet() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
      // const productSetId = 'Id of the product set';
    
      const productPath = client.productPath(projectId, location, productId);
      const productSetPath = client.productSetPath(
        projectId,
        location,
        productSetId
      );
    
      const request = {
        name: productSetPath,
        product: productPath,
      };
    
      await client.addProductToProductSet(request);
      console.log('Product added to product set.');
    }
    addProductToProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def add_product_to_product_set(project_id, location, product_id, product_set_id):
        """Add a product to a product set.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
            product_set_id: Id of the product set.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the full path of the product set.
        product_set_path = client.[product_set_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_set_path)(
            project=project_id, location=location, product_set=product_set_id
        )
    
        # Get the full path of the product.
        product_path = client.[product_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_path)(
            project=project_id, location=location, product=product_id
        )
    
        # Add the product to the product set.
        client.[add_product_to_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_add_product_to_product_set)(name=product_set_path, product=product_path)
        print("Product added to product set.")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

#### Response
    
    
    Product added to product set.
    

### 4\. Update a product

If you need to update a product or product set after it has been created, you can use our update methods. This example shows a product update where the labels are changed:

### Command-line

When you send a `PATCH` request all previous fields and their values will be erased except for the `productCategory` field, which is immutable. Send all fields you need with values when making the `PATCH` update request. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_ID: The ID for the product that is associated with a reference image. This ID is either randomly set or specified by the user at product creation time.
  * display-name: A string display name of your choosing. This can be the same as the previous display name or an updated value. 
  * description: A string description of your choosing. This can be the same as the previous display name or an updated value. Omit the `description` field and value if you don't need it. 
  * `productLabels`: One or more key-value pairs associated with a product. Each KEY_STRING must have an associated VALUE_STRING.



HTTP method and URL: 
    
    
    PATCH https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id

Request JSON body: 
    
    
    {
      "displayName": "display-name",
      "description": "description",
      "productLabels": [
        {
          "key": "key-string",
          "value": "value-string"
        },
        {
          "key": "key-string",
          "value": "value-string"
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/location-id/products/product-id",
      "displayName": "display-name",
      "description": "description",
      "productCategory": "apparel-v2",
      "productLabels": [
        {
          "key": "style",
          "value": "womens"
        },
        {
          "key": "onSale",
          "value": "true"
        }
      ]
    }
    

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    	field_mask "google.golang.org/genproto/protobuf/field_mask"
    )
    
    // updateProductLabels updates product labels of a product.
    func updateProductLabels(w io.Writer, projectID string, location string, productID string, key string, value string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[UpdateProductRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_UpdateProductRequest){
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{
    				"product_labels",
    			},
    		},
    		Product: &visionpb.[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Product){
    			Name: fmt.Sprintf("projects/%s/locations/%s/products/%s", projectID, location, productID),
    			ProductLabels: []*visionpb.[Product_KeyValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Product_KeyValue){
    				{
    					Key:   key,
    					Value: value,
    				},
    			},
    		},
    	}
    
    	resp, err := c.UpdateProduct(ctx, req)
    	if err != nil {
    		return fmt.Errorf("UpdateProduct: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product name: %s\n", resp.Name)
    	fmt.Fprintf(w, "Updated product labels: %s\n", resp.ProductLabels)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Update the product labels.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId -Id of the product.
     * @param productLabels - Labels of the product.
     * @throws IOException - on I/O errors.
     */
    public static void updateProductLabels(
        String projectId, String computeRegion, String productId, String productLabels)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product.
        String formattedName = ProductName.format(projectId, computeRegion, productId);
    
        // Set product name, product labels and product display name.
        // Multiple labels are also supported.
        Product product =
            Product.newBuilder()
                .setName(formattedName)
                .addProductLabels(
                    KeyValue.newBuilder()
                        .setKey(productLabels.split(",")[0].split("=")[0])
                        .setValue(productLabels.split(",")[0].split("=")[1])
                        .build())
                .build();
    
        // Set product update field name.
        FieldMask updateMask = FieldMask.newBuilder().addPaths("product_labels").build();
    
        // Update the product.
        Product updatedProduct = client.updateProduct(product, updateMask);
        // Display the product information
        System.out.println(String.format("Product name: %s", updatedProduct.getName()));
        System.out.println(String.format("Updated product labels: "));
        for (Product.KeyValue element : updatedProduct.getProductLabelsList()) {
          System.out.println(String.format("%s: %s", element.getKey(), element.getValue()));
        }
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function updateProductLabels() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
      // const key = 'The key of the label';
      // const value = 'The value of the label';
    
      // Resource path that represents full path to the product.
      const productPath = client.productPath(projectId, location, productId);
    
      const product = {
        name: productPath,
        productLabels: [
          {
            key: key,
            value: value,
          },
        ],
      };
    
      const updateMask = {
        paths: ['product_labels'],
      };
    
      const request = {
        product: product,
        updateMask: updateMask,
      };
    
      const [updatedProduct] = await client.updateProduct(request);
      console.log(`Product name: ${updatedProduct.name}`);
      console.log(`Product display name: ${updatedProduct.displayName}`);
      console.log(`Product description: ${updatedProduct.description}`);
      console.log(`Product category: ${updatedProduct.productCategory}`);
      console.log(
        `Product Labels: ${updatedProduct.productLabels[0].key}: ${updatedProduct.productLabels[0].value}`
      );
    }
    updateProductLabels();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    from google.protobuf import field_mask_pb2 as field_mask
    
    def update_product_labels(project_id, location, product_id, key, value):
        """Update the product labels.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
            key: The key of the label.
            value: The value of the label.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the name of the product.
        product_path = client.[product_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_path)(
            project=project_id, location=location, product=product_id
        )
    
        # Set product name, product label and product display name.
        # Multiple labels are also supported.
        key_value = vision.[Product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Product.html).[KeyValue](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Product.KeyValue.html)(key=key, value=value)
        product = vision.[Product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Product.html)(name=product_path, product_labels=[key_value])
    
        # Updating only the product_labels field here.
        update_mask = field_mask.FieldMask(paths=["product_labels"])
    
        # This overwrites the product_labels.
        updated_product = client.[update_product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_update_product)(product=product, update_mask=update_mask)
    
        # Display the updated product information.
        print(f"Product name: {updated_product.name}")
        print(f"Updated product labels: {product.product_labels}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

#### Response
    
    
    Product name: projects/prj-prod-search-tutorials/locations/us-east1/products/P_CLOTH-SHOE_46903668_070318
    Product id: P_CLOTH-SHOE_46903668_070318
    Product display name: Blue Dress
    Updated product labels:
      Product label 1:
            key: style
            value: women
      Product label 2:
            key: category
            value: dress
      Product label 3:
            key: color
            value: blue
    Product description: Short sleeved and 1950s style satin dress

### 5\. Create a Product's Reference Image

Creating a reference image for an individual product allows Vision API Product Search to search for the product by this image after it is indexed. You can have multiple reference images in a product, particularly if you desire a better match quality.

You can add a new reference image to a product at any time.

When creating a reference image you have the option to include bounding poly coordinates. A bounding poly identifies an area of interest in the reference image. For example, if you create a reference image for a product that is a jacket, you can provide the coordinates for the jacket in the bounding poly argument, and the system will only consider the jacket when looking for product matches. Note: You can provide multiple bounding polys at index time, though at query time the API supports only a single bounding poly.

A convenient way to get the bounding poly coordinates for an image is to use Vision API object localization. For more information on object localization, see [Detecting Multiple Objects](https://docs.cloud.google.com/vision/docs/object-localizer).

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_ID: The ID for the product that is associated with a reference image. This ID is either randomly set or specified by the user at product creation time.
  * CLOUD_STORAGE_IMAGE_URI: the path to a valid image file in a Cloud Storage bucket. You must at least have read privileges to the file. Example: 
    * gs://storage-bucket/filename.jpg

**Note** : The boundingPolys field is optional. If you don't specify a bounding box, Cloud Vision API will try to infer regions of interest in the image that are compatible with the `productCategory` on the parent product. 


HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages

Request JSON body: 
    
    
    {
      "uri": "cloud-storage-image-uri",
      "boundingPolys": [
        {
          "vertices": [
            {
              "x": X_MIN,
              "y": Y_MIN
            },
            {
              "x": X_MAX,
              "y": Y_MIN
            },
            {
              "x": X_MAX,
              "y": Y_MAX
            },
            {
              "x": X_MIN,
              "y": Y_MAX
            }
          ]
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

You should see output similar to the following. The example request specified a single `boundingPoly` in the image. The vertices for the bounding box are _not_ normalized; the vertex values are the actual pixel values, and _not_ relative to the original image and scaled from 0 to 1. These vertices have the following values: [(33,22),(282,22),(282,278),(33,278)]. 
    
    
    
    {
      "name": "projects/project-id/locations/location-id/products/product-id/referenceImages/image-id",
      "uri": "gs://storage-bucket/filename.jpg",
      "boundingPolys": [
        {
          "vertices": [
            {
              "x": 33,
              "y": 22
            },
            {
              "x": 282,
              "y": 22
            },
            {
              "x": 282,
              "y": 278
            },
            {
              "x": 33,
              "y": 278
            }
          ]
        }
      ]
    }
    

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    )
    
    // createReferenceImage creates a reference image for a product.
    func createReferenceImage(w io.Writer, projectID string, location string, productID string, referenceImageID string, gcsURI string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[CreateReferenceImageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_CreateReferenceImageRequest){
    		Parent: fmt.Sprintf("projects/%s/locations/%s/products/%s", projectID, location, productID),
    		ReferenceImage: &visionpb.[ReferenceImage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ReferenceImage){
    			Uri: gcsURI,
    		},
    		ReferenceImageId: referenceImageID,
    	}
    
    	resp, err := c.CreateReferenceImage(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateReferenceImage: %w", err)
    	}
    
    	fmt.Fprintf(w, "Reference image name: %s\n", resp.Name)
    	fmt.Fprintf(w, "Reference image uri: %s\n", resp.Uri)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Create a reference image.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @param referenceImageId - Id of the image.
     * @param gcsUri - Google Cloud Storage path of the input image.
     * @throws IOException - on I/O errors.
     */
    public static void createReferenceImage(
        String projectId,
        String computeRegion,
        String productId,
        String referenceImageId,
        String gcsUri)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product.
        String formattedParent = ProductName.format(projectId, computeRegion, productId);
        // Create a reference image.
        ReferenceImage referenceImage = ReferenceImage.newBuilder().setUri(gcsUri).build();
    
        ReferenceImage image =
            client.createReferenceImage(formattedParent, referenceImage, referenceImageId);
        // Display the reference image information.
        System.out.println(String.format("Reference image name: %s", image.getName()));
        System.out.println(String.format("Reference image uri: %s", image.getUri()));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function createReferenceImage() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
      // const referenceImageId = 'Id of the reference image';
      // const gcsUri = 'Google Cloud Storage path of the input image';
    
      const formattedParent = client.productPath(projectId, location, productId);
    
      const referenceImage = {
        uri: gcsUri,
      };
    
      const request = {
        parent: formattedParent,
        referenceImage: referenceImage,
        referenceImageId: referenceImageId,
      };
    
      const [response] = await client.createReferenceImage(request);
      console.log(`response.name: ${response.name}`);
      console.log(`response.uri: ${response.uri}`);
    }
    createReferenceImage();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def create_reference_image(
        project_id, location, product_id, reference_image_id, gcs_uri
    ):
        """Create a reference image.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
            reference_image_id: Id of the reference image.
            gcs_uri: Google Cloud Storage path of the input image.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the full path of the product.
        product_path = client.[product_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_path)(
            project=project_id, location=location, product=product_id
        )
    
        # Create a reference image.
        reference_image = vision.[ReferenceImage](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ReferenceImage.html)(uri=gcs_uri)
    
        # The response is the reference image with `name` populated.
        image = client.[create_reference_image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_create_reference_image)(
            parent=product_path,
            reference_image=reference_image,
            reference_image_id=reference_image_id,
        )
    
        # Display the reference image information.
        print(f"Reference image name: {image.name}")
        print(f"Reference image uri: {image.uri}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

#### Response
    
    
    Reference image name: projects/prj-prod-search-tutorials/locations/us-east1/products/P_CLOTH-SHOE_46903668_070318/referenceImages/I_469a896b70ba11e8be97d20059124800_070418
    Reference image id: I_469a896b70ba11e8be97d20059124800_070418
    Reference image uri: gs://product-search-tutorial/dress-shoe-dataset/469a896b70ba11e8be97d20059124800.jpg
    Reference image bounding polygons:
    vertices {
      x: 80
      y: 50
    }
    vertices {
      x: 80
      y: 660
    }
    vertices {
      x: 300
      y: 50
    }
    vertices {
      x: 430
      y: 660
    }

## Step 2: Search For Matching Products

This interface allows you to query the product catalog you created by taking a new image as input and searching for the best matching product.

Similar to creating a reference image, when searching for matching images you have the option to include bounding poly coordinates. A bounding poly identifies the area of interest in the source image that you want to find matches for. For example, if your source image contains both a dress and a purse, and you only want to find matches for the dress, you can identify the bounding poly coordinates for the region of the picture that contains only the dress. By default, if no bounding poly is specified the API determines the largest bounding poly and queries it automatically.

A convenient way to get the bounding poly coordinates for an image is to use Vision API object localization. For more information on object localization, see [Detecting Multiple Objects](https://docs.cloud.google.com/vision/docs/object-localizer). For example, you can explicitly query a full image by specifying a bounding poly of the entire image box: [(0, 0), (0, 1), (1, 1), (1, 0)].

The request returns an API response that includes the best matching product for an image with the score and the matching image. This image is returned using the highest confidence value.

**Note:** You can also search for best matching products using an image URI as an argument instead of a local filepath. See [Searching for Products](https://docs.cloud.google.com/vision/product-search/docs/searching) for more information.

### REST

Before using any of the request data, make the following replacements: 

  * BASE64_ENCODED_IMAGE: The base64 representation (ASCII string) of your binary image data. This string should look similar to the following string: 
    * `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`
Visit the [base64 encode](https://docs.cloud.google.com/vision/product-search/docs/base64) topic for more information.
  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_SET_ID: The ID for the product set you want to run the operation on.



**Field-specific considerations:**

  * `features.maxResults` \- The maximum number of results to be returned. 
  * `imageContext.productCategories` \- The product category to search in. Currently you can only specify one product category (homegoods, apparel, toys, packaged goods, and general ). 
  * `imageContext.filter` \- (Optional) A key-value filtering expression (or multiple expressions) for product label. Format: "`key`=`value`". Filtering key-value pairs can be linked with AND or OR expressions: "`color`=`blue` AND `style`=`mens`", or "`color`=`blue` OR `color`=`black`". If using the OR expression **all keys in the expression must be the same**. 



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "content": base64-encoded-image
          },
          "features": [
            {
              "type": "PRODUCT_SEARCH",
              "maxResults": 5
            }
          ],
          "imageContext": {
            "productSearchParams": {
              "productSet": "projects/project-id/locations/location-id/productSets/product-set-id",
              "productCategories": [
                   "apparel"
              ],
              "filter": "style = womens"
            }
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/images:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/images:annotate" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

The response JSON includes the two following result types:

  * `productSearchResults` \- Contains a list of matching products for the entire image. In the sample response the matching products are: product_id65, product_id35, product_id34, product_id62, product_id32. 
  * `productGroupedResults` \- Contains bounding box coordinates and matching items for _each_ product identified in the image. In the following response there is only one product identified, followed by matching products in the sample product set: product_id65, product_id35, product_id34, product_id93, product_id62. 



Note that while there is overlap in the two result types, there may also be differences (for example, product_id32 and product_id93 in the response).

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 1},{"x": 1,"y": 1},{"y": 1}]**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.products.referenceImages#boundingpoly). 

#### Response
    
    
    
    
    
    {
      "responses": [
        {**"productSearchResults"** : {
            "indexTime": "2019-09-04T21:03:35.662099907Z",
            "results": [
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id65** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.38946953,
                "image": "projects/project-id/locations/location-id/products/product_id65/referenceImages/**image65** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id35** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.3847863,
                "image": "projects/project-id/locations/location-id/products/product_id35/referenceImages/**image35** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id34** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.33896044,
                "image": "projects/project-id/locations/location-id/products/product_id34/referenceImages/**image34** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id62** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.32509044,
                "image": "projects/project-id/locations/location-id/products/product_id62/referenceImages/**image62** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id32** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.3237155,
                "image": "projects/project-id/locations/location-id/products/product_id32/referenceImages/image32"
              }
            ],**"productGroupedResults"** : [
              {
                "boundingPoly": {
                  "normalizedVertices": [
                    {
                      "x": 0.00458825,
                      "y": 0.11000001
                    },
                    {
                      "x": 0.988353,
                      "y": 0.11000001
                    },
                    {
                      "x": 0.988353,
                      "y": 0.9290588
                    },
                    {
                      "x": 0.00458825,
                      "y": 0.9290588
                    }
                  ]
                },
                "results": [
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id65** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.41785678,
                    "image": "projects/project-id/locations/location-id/products/product_id65/referenceImages/**image65** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id35** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.3803885,
                    "image": "projects/project-id/locations/location-id/products/product_id35/referenceImages/**image35** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id34** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.36055994,
                    "image": "projects/project-id/locations/location-id/products/product_id34/referenceImages/**image34** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id93** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "shoe"
                        },
                        {
                          "key": "kids",
                          "value": "true"
                        }
                      ]
                    },
                    "score": 0.33286288,
                    "image": "projects/project-id/locations/location-id/products/product_id93/referenceImages/**image93** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id62** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.32263064,
                    "image": "projects/project-id/locations/location-id/products/product_id62/referenceImages/**image62** "
                  }
                ],
                "objectAnnotations": [
                  {
                    "mid": "/m/01d40f",
                    "name": "Dress",
                    "score": 0.95488
                  }
                ]
              }
            ]
          }
        }
      ]
    }

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    )
    
    // getSimilarProducts searches for products from a product set similar to products in an image file.
    func getSimilarProducts(w io.Writer, projectID string, location string, productSetID string, productCategory string, file string, filter string) error {
    	ctx := context.Background()
    	c, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImageAnnotatorClient: %w", err)
    	}
    	defer c.Close()
    
    	f, err := os.Open(file)
    	if err != nil {
    		return fmt.Errorf("Open: %w", err)
    	}
    	defer f.Close()
    
    	image, err := vision.[NewImageFromReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_NewImageFromReader)(f)
    	if err != nil {
    		return fmt.Errorf("NewImageFromReader: %w", err)
    	}
    
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

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    const fs = require('fs');
    // Creates a client
    const productSearchClient = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    const imageAnnotatorClient = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function getSimilarProductsFile() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'nodejs-docs-samples';
      // const location = 'us-west1';
      // const productSetId = 'indexed_product_set_id_for_testing';
      // const productCategory = 'apparel';
      // const filePath = './resources/shoes_1.jpg';
      // const filter = '';
      const productSetPath = productSearchClient.productSetPath(
        projectId,
        location,
        productSetId
      );
      const content = fs.readFileSync(filePath, 'base64');
      const request = {
        // The input image can be a GCS link or HTTPS link or Raw image bytes.
        // Example:
        // To use GCS link replace with below code
        // image: {source: {gcsImageUri: filePath}}
        // To use HTTP link replace with below code
        // image: {source: {imageUri: filePath}}
        image: {content: content},
        features: [{type: 'PRODUCT_SEARCH'}],
        imageContext: {
          productSearchParams: {
            productSet: productSetPath,
            productCategories: [productCategory],
            filter: filter,
          },
        },
      };
      const [response] = await imageAnnotatorClient.batchAnnotateImages({
        requests: [request],
      });
      console.log('Search Image:', filePath);
      const results = response['responses'][0]['productSearchResults']['results'];
      console.log('\nSimilar product information:');
      results.forEach(result => {
        console.log('Product id:', result['product'].name.split('/').pop(-1));
        console.log('Product display name:', result['product'].displayName);
        console.log('Product description:', result['product'].description);
        console.log('Product category:', result['product'].productCategory);
      });
    }
    getSimilarProductsFile();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def get_similar_products_file(
        project_id,
        location,
        product_set_id,
        product_category,
        file_path,
        filter,
        max_results,
    ):
        """Search similar products to image.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
            product_category: Category of the product.
            file_path: Local file path of the image to be searched.
            filter: Condition to be applied on the labels.
                    Example for filter: (color = red OR color = blue) AND style = kids
                    It will search on all products with the following labels:
                    color:red AND style:kids
                    color:blue AND style:kids
            max_results: The maximum number of results (matches) to return. If omitted, all results are returned.
        """
        # product_search_client is needed only for its helper methods.
        product_search_client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
        image_annotator_client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        # Read the image as a stream of bytes.
        with open(file_path, "rb") as image_file:
            content = image_file.read()
    
        # Create annotate image request along with product search feature.
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(content=content)
    
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
        response = image_annotator_client.[product_search](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.html)(
            image, image_context=image_context, max_results=max_results
        )
    
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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

#### Apparel Response Example
    
    
    Search Image:
      D:/product/final/images-20180618T073733Z-01/images/469355b570ba11e88ff2d20059124800.jpg

![Image search result](https://docs.cloud.google.com/static/vision/product-search/docs/images/draw_image.png)
    
    
    Similar product information:
     Product id: 46930b6b
     Product display name: Evening gown
     Product description: Blue evening gown in 1940s style
     Product category: apparel
     style: women
     category: dress
     color: blue

#### Searching with a Label

The following search example includes a filter based on color.

**Note:** The filtering system only works on user-defined labels, so the label of interest (color, in this case) has to be provided when creating the products.

#### Request

Make a search request by executing the following request with method `get_similar_products_file()` or `get_similar_products_uri()`. Product set id, local image file path and filter are passed as arguments. This input image is also present in "resources/input/".

### Python
    
    
    python product_search.py get_similar_products_file "12000002" "D:/product/final/images-20180618T073733Z-001/images/469355b570ba11e88ff2d20059124800.jpg" "color=white"
    

#### Response
    
    
    Search Image:
      D:/product/final/images-20180618T073733Z-001/images/469355b570ba11e88ff2d20059124800.jpg

![Image search result 2](https://docs.cloud.google.com/static/vision/product-search/docs/images/draw_image2.jpg)
    
    
    Similar product information:
     Product id: p569d4e7a1
     Product display name: Wedding Dress
     Product description: Elegant Wedding Dress for women
     Product category: apparel
     style: women
     category: dress
     color: white

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
