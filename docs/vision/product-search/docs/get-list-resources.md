---
url: https://docs.cloud.google.com/vision/product-search/docs/get-list-resources/
title: Getting and listing resources \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:10:13.192746+00:00
---

# Getting and listing resources  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/get-list-resources/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/product-search/docs/create-product-set-search-products)



Send feedback 

#  Getting and listing resources Stay organized with collections  Save and categorize content based on your preferences. 

At any time, you can list and get any product set, product, or reference image resources you have.

## Listing product sets

This section describes how to retrieve a list of all your product sets.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 



HTTP method and URL: 
    
    
    GET https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "productSets": [
        {
          "name": "projects/project-id/locations/location-id/productSets/product-set-id1",
          "displayName": "display-name1",
          "indexTime": "2019-09-04T15:33:43.581861690Z",
          "indexError": {}
        },
        {
          "name": "projects/project-id/locations/location-id/productSets/product-set-id2",
          "displayName": "display-name2",
          "indexTime": "1970-01-01T00:00:00Z",
          "indexError": {}
        },
        {
          "name": "projects/project-id/locations/location-id/productSets/product-set-id3",
          "displayName": "display-name3",
          "indexTime": "2019-12-26T17:03:38.935312842Z",
          "indexError": {}
        },
        {
          "name": "projects/project-id/locations/location-id/productSets/product-set-id4",
          "displayName": "display-name4",
          "indexTime": "2019-09-04T15:33:43.581861690Z",
          "indexError": {}
        },
        {
          "name": "projects/project-id/locations/location-id/productSets/product-set-id5",
          "displayName": "display-name5",
          "indexTime": "1970-01-01T00:00:00Z",
          "indexError": {}
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
    	"google.golang.org/api/iterator"
    )
    
    // listProductSets lists product sets.
    func listProductSets(w io.Writer, projectID string, location string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[ListProductSetsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ListProductSetsRequest){
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    	}
    
    	it := c.ListProductSets(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Next: %w", err)
    		}
    
    		fmt.Fprintf(w, "Product set name: %s\n", resp.Name)
    		fmt.Fprintf(w, "Product set display name: %s\n", resp.DisplayName)
    		fmt.Fprintf(w, "Product set index time:\n")
    		fmt.Fprintf(w, "seconds: %d\n", resp.IndexTime.Seconds)
    		fmt.Fprintf(w, "nanos: %d\n", resp.IndexTime.Nanos)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * List all product sets
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @throws IOException - on I/O errors.
     */
    public static void listProductSets(String projectId, String computeRegion) throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
        // A resource that represents Google Cloud Platform location.
        String formattedParent = LocationName.format(projectId, computeRegion);
        // List all the product sets available in the region.
        for (ProductSet productSet : client.listProductSets(formattedParent).iterateAll()) {
          // Display the product set information
          System.out.println(String.format("Product set name: %s", productSet.getName()));
          System.out.println(
              String.format(
                  "Product set id: %s",
                  productSet.getName().substring(productSet.getName().lastIndexOf('/') + 1)));
          System.out.println(
              String.format("Product set display name: %s", productSet.getDisplayName()));
          System.out.println("Product set index time:");
          System.out.println(String.format("\tseconds: %s", productSet.getIndexTime().getSeconds()));
          System.out.println(String.format("\tnanos: %s", productSet.getIndexTime().getNanos()));
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
    
    async function listProductSets() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
    
      // Resource path that represents Google Cloud Platform location.
      const locationPath = client.locationPath(projectId, location);
    
      const [productSets] = await client.listProductSets({parent: locationPath});
      productSets.forEach(productSet => {
        console.log(`Product Set name: ${productSet.name}`);
        console.log(`Product Set display name: ${productSet.displayName}`);
      });
    }
    listProductSets();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def list_product_sets(project_id, location):
        """List all product sets.
        Args:
            project_id: Id of the project.
            location: A compute region name.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # A resource that represents Google Cloud Platform location.
        location_path = f"projects/{project_id}/locations/{location}"
    
        # List all the product sets available in the region.
        product_sets = client.[list_product_sets](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_list_product_sets)(parent=location_path)
    
        # Display the product set information.
        for product_set in product_sets:
            print(f"Product set name: {product_set.name}")
            print("Product set id: {}".format(product_set.name.split("/")[-1]))
            print(f"Product set display name: {product_set.display_name}")
            print("Product set index time: ")
            print(product_set.index_time)
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Getting a single product set

You can get a single product set to use or modify.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_SET_ID: The ID for the product set you want to run the operation on.



HTTP method and URL: 
    
    
    GET https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/location-id/productSets/product-set-id",
      "displayName": "display-name",
      "indexTime": "2019-09-04T15:33:43.581861690Z",
      "indexError": {}
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
    
    // getProductSet gets a product set.
    func getProductSet(w io.Writer, projectID string, location string, productSetID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[GetProductSetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_GetProductSetRequest){
    		Name: fmt.Sprintf("projects/%s/locations/%s/productSets/%s", projectID, location, productSetID),
    	}
    
    	resp, err := c.GetProductSet(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetProductSet: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product set name: %s\n", resp.Name)
    	fmt.Fprintf(w, "Product set display name: %s\n", resp.DisplayName)
    	fmt.Fprintf(w, "Product set index time:\n")
    	fmt.Fprintf(w, "seconds: %d\n", resp.IndexTime.Seconds)
    	fmt.Fprintf(w, "nanos: %d\n", resp.IndexTime.Nanos)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Get info about the product set.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productSetId - Id of the product set.
     * @throws IOException - on I/O errors.
     */
    public static void getProductSet(String projectId, String computeRegion, String productSetId)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product set.
        String formattedName = ProductSetName.format(projectId, computeRegion, productSetId);
        // Get complete detail of the product set.
        ProductSet productSet = client.getProductSet(formattedName);
        // Display the product set information
        System.out.println(String.format("Product set name: %s", productSet.getName()));
        System.out.println(
            String.format(
                "Product set id: %s",
                productSet.getName().substring(productSet.getName().lastIndexOf('/') + 1)));
        System.out.println(
            String.format("Product set display name: %s", productSet.getDisplayName()));
        System.out.println("Product set index time:");
        System.out.println(String.format("\tseconds: %s", productSet.getIndexTime().getSeconds()));
        System.out.println(String.format("\tnanos: %s", productSet.getIndexTime().getNanos()));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function getProductSet() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productSetId = 'Id of the product set';
    
      // Resource path that represents Google Cloud Platform location.
      const productSetPath = client.productSetPath(
        projectId,
        location,
        productSetId
      );
    
      const [productSet] = await client.getProductSet({name: productSetPath});
      console.log(`Product Set name: ${productSet.name}`);
      console.log(`Product Set display name: ${productSet.displayName}`);
    }
    getProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def get_product_set(project_id, location, product_set_id):
        """Get info about the product set.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the full path of the product set.
        product_set_path = client.[product_set_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_set_path)(
            project=project_id, location=location, product_set=product_set_id
        )
    
        # Get complete detail of the product set.
        product_set = client.[get_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_get_product_set)(name=product_set_path)
    
        # Display the product set information.
        print(f"Product set name: {product_set.name}")
        print("Product set id: {}".format(product_set.name.split("/")[-1]))
        print(f"Product set display name: {product_set.display_name}")
        print("Product set index time: ")
        print(product_set.index_time)
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Listing products

You can view all products in a Google Cloud Platform project, or in a specific product set.

### Listing all products in a project

The following example shows how to list products in a project.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 



HTTP method and URL: 
    
    
    GET https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

You should see output similar to the following. Note that the number of products returned is limited to 10 at a time, and a `nextPageToken` is provided if there are more pages.

#### Response
    
    
    {
      "products": [
        {
          "name": "projects/project-id/locations/location-id/products/product-id01",
          "displayName": " ",
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
        },
        {
          "name": "projects/project-id/locations/location-id/products/product-id02",
          "displayName": " ",
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
        },
        {
          "name": "projects/project-id/locations/location-id/products/product-id03",
          "displayName": " ",
          "productCategory": "apparel-v2",
          "productLabels": [
            {
              "key": "style",
              "value": "women"
            },
            {
              "key": "category",
              "value": "shoe"
            }
          ]
        },
        {
          "name": "projects/project-id/locations/location-id/products/product-id04",
          "displayName": " ",
          "productCategory": "apparel-v2",
          "productLabels": [
            {
              "key": "style",
              "value": "men"
            },
            {
              "key": "category",
              "value": "shoe"
            }
          ]
        },
        {
          "name": "projects/project-id/locations/location-id/products/product-id05",
          "displayName": " ",
          "productCategory": "apparel-v2",
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
        {
          "name": "projects/project-id/locations/location-id/products/product-id06",
          "displayName": " ",
          "productCategory": "apparel-v2",
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
        {
          "name": "projects/project-id/locations/location-id/products/product-id07",
          "displayName": " ",
          "productCategory": "apparel-v2",
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
        {
          "name": "projects/project-id/locations/location-id/products/product-id08",
          "displayName": " ",
          "productCategory": "apparel-v2",
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
        {
          "name": "projects/project-id/locations/location-id/products/product-id09",
          "displayName": " ",
          "productCategory": "apparel-v2",
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
        {
          "name": "projects/project-id/locations/location-id/products/product-id10",
          "displayName": " ",
          "productCategory": "apparel-v2",
          "productLabels": [
            {
              "key": "style",
              "value": "women"
            },
            {
              "key": "category",
              "value": "shoe"
            }
          ]
        }
      ],**"nextPageToken": "jMGjEqhXMtN95vZz2g"**
    }
    

If a `nextPageToken` is returned, you can use the token to get the next page of product results. Use the `nextPageToken` from the response JSON (`jMGjEqhXMtN95vZz2g` in this example) as a `pageToken` query appended to the request URL:
    
    
    https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products**?pageToken=** jMGjEqhXMtN95vZz2g

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    	"google.golang.org/api/iterator"
    )
    
    // listProducts lists products.
    func listProducts(w io.Writer, projectID string, location string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[ListProductsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ListProductsRequest){
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    	}
    
    	it := c.ListProducts(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Next: %w", err)
    		}
    
    		fmt.Fprintf(w, "Product name: %s\n", resp.Name)
    		fmt.Fprintf(w, "Product display name: %s\n", resp.DisplayName)
    		fmt.Fprintf(w, "Product category: %s\n", resp.ProductCategory)
    		fmt.Fprintf(w, "Product labels: %s\n", resp.ProductLabels)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * List all products.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @throws IOException - on I/O errors.
     */
    public static void listProducts(String projectId, String computeRegion) throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // A resource that represents Google Cloud Platform location.
        String formattedParent = LocationName.format(projectId, computeRegion);
    
        // List all the products available in the region.
        for (Product product : client.listProducts(formattedParent).iterateAll()) {
          // Display the product information
          System.out.println(String.format("\nProduct name: %s", product.getName()));
          System.out.println(
              String.format(
                  "Product id: %s",
                  product.getName().substring(product.getName().lastIndexOf('/') + 1)));
          System.out.println(String.format("Product display name: %s", product.getDisplayName()));
          System.out.println(String.format("Product category: %s", product.getProductCategory()));
          System.out.println("Product labels:");
          System.out.println(
              String.format("Product labels: %s", product.getProductLabelsList().toString()));
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
    
    async function listProducts() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
    
      // Resource path that represents Google Cloud Platform location.
      const locationPath = client.locationPath(projectId, location);
    
      const [products] = await client.listProducts({parent: locationPath});
      products.forEach(product => {
        console.log(`Product name: ${product.name}`);
        console.log(`Product id: ${product.name.split('/').pop()}`);
        console.log(`Product display name: ${product.displayName}`);
        console.log(`Product description: ${product.description}`);
        console.log(`Product category: ${product.productCategory}`);
        if (product.productLabels.length) {
          console.log('Product labels:');
          product.productLabels.forEach(productLabel => {
            console.log(`${productLabel.key}: ${productLabel.value}`);
          });
        }
      });
    }
    listProducts();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    from google.protobuf import field_mask_pb2 as field_mask
    
    def list_products(project_id, location):
        """List all products.
        Args:
            project_id: Id of the project.
            location: A compute region name.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # A resource that represents Google Cloud Platform location.
        location_path = f"projects/{project_id}/locations/{location}"
    
        # List all the products available in the region.
        products = client.[list_products](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_list_products)(parent=location_path)
    
        # Display the product information.
        for product in products:
            print(f"Product name: {product.name}")
            print("Product id: {}".format(product.name.split("/")[-1]))
            print(f"Product display name: {product.display_name}")
            print(f"Product description: {product.description}")
            print(f"Product category: {product.product_category}")
            print(f"Product labels: {product.product_labels}\n")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

### Listing all products in a product set

The following example shows how to list products in a specific product set.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_SET_ID: The ID for the product set you want to run the operation on.



HTTP method and URL: 
    
    
    GET https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id/products

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id/products"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id/products" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

You should see output similar to the following. Note that the number of products returned is limited to 10 at a time, and a `nextPageToken` is provided if there are more pages.

#### Response
    
    
    {
      "products": [
        {
          "name": "projects/project-id/locations/location-id/products/product-id01",
          "displayName": " ",
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
        },
        {
          "name": "projects/project-id/locations/location-id/products/product-id02",
          "displayName": " ",
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
        },
        {
          "name": "projects/project-id/locations/location-id/products/product-id03",
          "displayName": " ",
          "productCategory": "apparel-v2",
          "productLabels": [
            {
              "key": "style",
              "value": "women"
            },
            {
              "key": "category",
              "value": "shoe"
            }
          ]
        },
        {
          "name": "projects/project-id/locations/location-id/products/product-id04",
          "displayName": " ",
          "productCategory": "apparel-v2",
          "productLabels": [
            {
              "key": "style",
              "value": "men"
            },
            {
              "key": "category",
              "value": "shoe"
            }
          ]
        },
        {
          "name": "projects/project-id/locations/location-id/products/product-id05",
          "displayName": " ",
          "productCategory": "apparel-v2",
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
        {
          "name": "projects/project-id/locations/location-id/products/product-id06",
          "displayName": " ",
          "productCategory": "apparel-v2",
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
        {
          "name": "projects/project-id/locations/location-id/products/product-id07",
          "displayName": " ",
          "productCategory": "apparel-v2",
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
        {
          "name": "projects/project-id/locations/location-id/products/product-id08",
          "displayName": " ",
          "productCategory": "apparel-v2",
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
        {
          "name": "projects/project-id/locations/location-id/products/product-id09",
          "displayName": " ",
          "productCategory": "apparel-v2",
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
        {
          "name": "projects/project-id/locations/location-id/products/product-id10",
          "displayName": " ",
          "productCategory": "apparel-v2",
          "productLabels": [
            {
              "key": "style",
              "value": "women"
            },
            {
              "key": "category",
              "value": "shoe"
            }
          ]
        }
      ],**"nextPageToken": "e5nEGpoVEZqlBbZRhQ"**
    }
    

If a `nextPageToken` is returned, you can use the token to get the next page of product results. Use the `nextPageToken` from the response JSON (`e5nEGpoVEZqlBbZRhQ` in this example) as a `pageToken` query appended to the request URL:
    
    
    https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products**?pageToken=** e5nEGpoVEZqlBbZRhQ

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    	"google.golang.org/api/iterator"
    )
    
    // listProductsInProductSet lists products in a product set.
    func listProductsInProductSet(w io.Writer, projectID string, location string, productSetID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[ListProductsInProductSetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ListProductsInProductSetRequest){
    		Name: fmt.Sprintf("projects/%s/locations/%s/productSets/%s", projectID, location, productSetID),
    	}
    
    	it := c.ListProductsInProductSet(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Next: %w", err)
    		}
    
    		fmt.Fprintf(w, "Product name: %s\n", resp.Name)
    		fmt.Fprintf(w, "Product display name: %s\n", resp.DisplayName)
    		fmt.Fprintf(w, "Product category: %s\n", resp.ProductCategory)
    		fmt.Fprintf(w, "Product labels: %s\n", resp.ProductLabels)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * List all products in a product set.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productSetId - Id of the product set.
     * @throws IOException - on I/O errors.
     */
    public static void listProductsInProductSet(
        String projectId, String computeRegion, String productSetId) throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product set.
        String formattedName = ProductSetName.format(projectId, computeRegion, productSetId);
        // List all the products available in the product set.
        for (Product product : client.listProductsInProductSet(formattedName).iterateAll()) {
          // Display the product information
          System.out.println(String.format("Product name: %s", product.getName()));
          System.out.println(
              String.format(
                  "Product id: %s",
                  product.getName().substring(product.getName().lastIndexOf('/') + 1)));
          System.out.println(String.format("Product display name: %s", product.getDisplayName()));
          System.out.println(String.format("Product description: %s", product.getDescription()));
          System.out.println(String.format("Product category: %s", product.getProductCategory()));
          System.out.println("Product labels: ");
          for (Product.KeyValue element : product.getProductLabelsList()) {
            System.out.println(String.format("%s: %s", element.getKey(), element.getValue()));
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function listProductsInProductSet() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productSetId = 'Id of the product set';
      const productSetPath = client.productSetPath(
        projectId,
        location,
        productSetId
      );
      const request = {
        name: productSetPath,
      };
    
      const [products] = await client.listProductsInProductSet(request);
      products.forEach(product => {
        console.log(`Product name: ${product.name}`);
        console.log(`Product display name: ${product.displayName}`);
      });
    }
    listProductsInProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_products_in_product_set(project_id, location, product_set_id):
        """List all products in a product set.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
        """
        client = vision.ProductSearchClient()
    
        # Get the full path of the product set.
        product_set_path = client.product_set_path(
            project=project_id, location=location, product_set=product_set_id
        )
    
        # List all the products available in the product set.
        products = client.list_products_in_product_set(name=product_set_path)
    
        # Display the product information.
        for product in products:
            print(f"Product name: {product.name}")
            print("Product id: {}".format(product.name.split("/")[-1]))
            print(f"Product display name: {product.display_name}")
            print(f"Product description: {product.description}")
            print(f"Product category: {product.product_category}")
            print(f"Product labels: {product.product_labels}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Getting a single product

You can also get a single product to use or modify.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_ID: The ID for the product that is associated with a reference image. This ID is either randomly set or specified by the user at product creation time.



HTTP method and URL: 
    
    
    GET https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/location-id/products/product-id",
      "displayName": " ",
      "productCategory": "apparel-v2",
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
    
    // getProduct gets a product.
    func getProduct(w io.Writer, projectID string, location string, productID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[GetProductRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_GetProductRequest){
    		Name: fmt.Sprintf("projects/%s/locations/%s/products/%s", projectID, location, productID),
    	}
    
    	resp, err := c.GetProduct(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetProduct: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product name: %s\n", resp.Name)
    	fmt.Fprintf(w, "Product display name: %s\n", resp.DisplayName)
    	fmt.Fprintf(w, "Product category: %s\n", resp.ProductCategory)
    	fmt.Fprintf(w, "Product labels: %s\n", resp.ProductLabels)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Get information about a product.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @throws IOException - on I/O errors.
     */
    public static void getProduct(String projectId, String computeRegion, String productId)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product.
        String formattedName = ProductName.format(projectId, computeRegion, productId);
        // Get complete detail of the product.
        Product product = client.getProduct(formattedName);
        // Display the product information
        System.out.println(String.format("Product name: %s", product.getName()));
        System.out.println(
            String.format(
                "Product id: %s",
                product.getName().substring(product.getName().lastIndexOf('/') + 1)));
        System.out.println(String.format("Product display name: %s", product.getDisplayName()));
        System.out.println(String.format("Product description: %s", product.getDescription()));
        System.out.println(String.format("Product category: %s", product.getProductCategory()));
        System.out.println(String.format("Product labels: "));
        for (Product.KeyValue element : product.getProductLabelsList()) {
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
    
    async function getProduct() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
    
      // Resource path that represents Google Cloud Platform location.
      const productPath = client.productPath(projectId, location, productId);
    
      const [product] = await client.getProduct({name: productPath});
      console.log(`Product name: ${product.name}`);
      console.log(`Product id: ${product.name.split('/').pop()}`);
      console.log(`Product display name: ${product.displayName}`);
      console.log(`Product description: ${product.description}`);
      console.log(`Product category: ${product.productCategory}`);
      console.log(`Product labels: ${product.productLabels}`);
    }
    getProduct();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    from google.protobuf import field_mask_pb2 as field_mask
    
    def get_product(project_id, location, product_id):
        """Get information about a product.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the full path of the product.
        product_path = client.[product_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_path)(
            project=project_id, location=location, product=product_id
        )
    
        # Get complete detail of the product.
        product = client.[get_product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_get_product)(name=product_path)
    
        # Display the product information.
        print(f"Product name: {product.name}")
        print("Product id: {}".format(product.name.split("/")[-1]))
        print(f"Product display name: {product.display_name}")
        print(f"Product description: {product.description}")
        print(f"Product category: {product.product_category}")
        print(f"Product labels: {product.product_labels}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Listing reference images

A product can have multiple associated reference images. The following example describes how to obtain all reference images linked to a single product.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_ID: The ID for the product that is associated with a reference image. This ID is either randomly set or specified by the user at product creation time.



HTTP method and URL: 
    
    
    GET https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

You should see output similar to the following. The default number of images returned is 10 at a time, and a `nextPageToken` is provided if there are more pages.

The below response is for a product with two reference images. One of these images has associated bounding box, while the other image does not have a bounding polygon.

#### Response
    
    
    {
      "referenceImages": [
        {
          "name": "projects/project-id/locations/location-id/products/product-id/referenceImages/image-id1",
          "uri": "gs://storage-bucket/filename1.jpg",
          "boundingPolys": [
            {
              "normalizedVertices": [
                {
                  "x": 0.10443038,
                  "y": 0.06962025
                },
                {
                  "x": 0.8924051,
                  "y": 0.06962025
                },
                {
                  "x": 0.8924051,
                  "y": 0.87974685
                },
                {
                  "x": 0.10443038,
                  "y": 0.87974685
                }
              ]
            }
          ]
        },
        {
          "name": "projects/project-id/locations/location-id/products/product-id/referenceImages/image-id2",
          "uri": "gs://storage-bucket/filename2.jpg"
        }
      ]
    }
    

If the response contains a `nextPageToken`, there are more results. You can repeat the request, adding a `pageToken` parameter with the value of `nextPageToken` (for example, `1LqhSgZfM_uWKOxvog`):
    
    
    https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages**?pageToken=** 1LqhSgZfM_uWKOxvog

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    	"google.golang.org/api/iterator"
    )
    
    // listReferenceImages lists reference images of a product.
    func listReferenceImages(w io.Writer, projectID string, location string, productID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[ListReferenceImagesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ListReferenceImagesRequest){
    		Parent: fmt.Sprintf("projects/%s/locations/%s/products/%s", projectID, location, productID),
    	}
    
    	it := c.ListReferenceImages(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Next: %w", err)
    		}
    
    		fmt.Fprintf(w, "Reference image name: %s\n", resp.Name)
    		fmt.Fprintf(w, "Reference image uri: %s\n", resp.Uri)
    		fmt.Fprintf(w, "Reference image bounding polygons: %s\n", resp.BoundingPolys)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * List all images in a product.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @throws IOException - on I/O errors.
     */
    public static void listReferenceImagesOfProduct(
        String projectId, String computeRegion, String productId) throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product.
        String formattedParent = ProductName.format(projectId, computeRegion, productId);
        for (ReferenceImage image : client.listReferenceImages(formattedParent).iterateAll()) {
          // Display the reference image information.
          System.out.println(String.format("Reference image name: %s", image.getName()));
          System.out.println(
              String.format(
                  "Reference image id: %s",
                  image.getName().substring(image.getName().lastIndexOf('/') + 1)));
          System.out.println(String.format("Reference image uri: %s", image.getUri()));
          System.out.println(
              String.format(
                  "Reference image bounding polygons: %s \n",
                  image.getBoundingPolysList().toString()));
        }
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function listReferenceImage() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
    
      // const formattedParent = client.productPath(projectId, location, productId);
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
      const formattedParent = client.productPath(projectId, location, productId);
      const request = {
        parent: formattedParent,
      };
    
      const [response] = await client.listReferenceImages(request);
      response.forEach(image => {
        console.log(`image.name: ${image.name}`);
        console.log(`image.uri: ${image.uri}`);
      });
    }
    listReferenceImage();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def list_reference_images(project_id, location, product_id):
        """List all images in a product.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the full path of the product.
        product_path = client.[product_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_path)(
            project=project_id, location=location, product=product_id
        )
    
        # List all the reference images available in the product.
        reference_images = client.[list_reference_images](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_list_reference_images)(parent=product_path)
    
        # Display the reference image information.
        for image in reference_images:
            print(f"Reference image name: {image.name}")
            print("Reference image id: {}".format(image.name.split("/")[-1]))
            print(f"Reference image uri: {image.uri}")
            print("Reference image bounding polygons: {}".format(image.bounding_polys))
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Getting a single reference image

You can also get a single reference image linked to a product.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_ID: The ID for the product that is associated with a reference image. This ID is either randomly set or specified by the user at product creation time.
  * IMAGE_ID: The ID of the target image resource.



HTTP method and URL: 
    
    
    GET https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages/image-id

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages/image-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages/image-id" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

You should see output similar to the following. The example reference image has associated bounding boxes specified.

#### Response
    
    
    {
      "name": "projects/project-id/locations/location-id/products/product-id/referenceImages/image-id",
      "uri": "gs://storage-bucket/filename.jpg",
      "boundingPolys": [
        {
          "normalizedVertices": [
            {
              "x": 0.10443038,
              "y": 0.06962025
            },
            {
              "x": 0.8924051,
              "y": 0.06962025
            },
            {
              "x": 0.8924051,
              "y": 0.87974685
            },
            {
              "x": 0.10443038,
              "y": 0.87974685
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
    
    // getReferenceImage gets a reference image.
    func getReferenceImage(w io.Writer, projectID string, location string, productID string, referenceImageID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[GetReferenceImageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_GetReferenceImageRequest){
    		Name: fmt.Sprintf("projects/%s/locations/%s/products/%s/referenceImages/%s", projectID, location, productID, referenceImageID),
    	}
    
    	resp, err := c.GetReferenceImage(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetReferenceImage: %w", err)
    	}
    
    	fmt.Fprintf(w, "Reference image name: %s\n", resp.Name)
    	fmt.Fprintf(w, "Reference image uri: %s\n", resp.Uri)
    	fmt.Fprintf(w, "Reference image bounding polygons: %s\n", resp.BoundingPolys)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Get info about a reference image.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @param referenceImageId - Id of the image.
     * @throws IOException - on I/O errors.
     */
    public static void getReferenceImage(
        String projectId, String computeRegion, String productId, String referenceImageId)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the reference image.
        String formattedName =
            ImageName.format(projectId, computeRegion, productId, referenceImageId);
        // Get complete detail of the reference image.
        ReferenceImage image = client.getReferenceImage(formattedName);
        // Display the reference image information.
        System.out.println(String.format("Reference image name: %s", image.getName()));
        System.out.println(
            String.format(
                "Reference image id: %s",
                image.getName().substring(image.getName().lastIndexOf('/') + 1)));
        System.out.println(String.format("Reference image uri: %s", image.getUri()));
        System.out.println(
            String.format(
                "Reference image bounding polygons: %s \n", image.getBoundingPolysList().toString()));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function getReferenceImage() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
      // const referenceImageId = 'Id of the reference image';
    
      const formattedName = client.referenceImagePath(
        projectId,
        location,
        productId,
        referenceImageId
      );
    
      const request = {
        name: formattedName,
      };
    
      const response = await client.getReferenceImage(request);
      console.log(`response.name: ${response.name}`);
      console.log(`response.uri: ${response.uri}`);
    }
    getReferenceImage();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def get_reference_image(project_id, location, product_id, reference_image_id):
        """Get info about a reference image.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
            reference_image_id: Id of the reference image.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the full path of the reference image.
        reference_image_path = client.[reference_image_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_reference_image_path)(
            project=project_id,
            location=location,
            product=product_id,
            reference_image=reference_image_id,
        )
    
        # Get complete detail of the reference image.
        image = client.[get_reference_image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_get_reference_image)(name=reference_image_path)
    
        # Display the reference image information.
        print(f"Reference image name: {image.name}")
        print("Reference image id: {}".format(image.name.split("/")[-1]))
        print(f"Reference image uri: {image.uri}")
        print(f"Reference image bounding polygons: {image.bounding_polys}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
