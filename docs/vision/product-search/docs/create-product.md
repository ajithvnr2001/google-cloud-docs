---
url: https://docs.cloud.google.com/vision/product-search/docs/create-product/
title: Creating and managing your product resources \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:05.986603+00:00
---

# Creating and managing your product resources  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/create-product/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/product-search/docs/create-product-set-search-products)



Send feedback 

#  Creating and managing your product resources Stay organized with collections  Save and categorize content based on your preferences. 

After you have created a product set, you can create products and add them to the product set. When you create a product, you must provide a display name for the product and a product category. Currently supported categories are: `homegoods-v2`, `apparel-v2`, `toys-v2`, `packagedgoods-v1`, and `general-v1` *.

You can also supply an optional description of your product, and optional labels for your product. Labels are key/value pairs that describe your product such as `color=black` or `style=mens`. You can include labels to filter the results of a product search to only search certain product images.

*** Legacy`productCategory` codes: **Legacy categories (`homegoods`, `apparel`, and `toys`) are still supported, but the updated `-v2` categories should be used for new products.

## Creating a product

You can use online import to create an individual product. After a product is created you can then add a reference image to it or add it to one or more product sets.

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

## Adding a product to a product set

When you have a product and product set available you can then add the product to the product set.

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

## Removing a product from a product set

You can also remove an existing product from a product set.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_SET_ID: The ID for the product set you want to run the operation on.
  * PRODUCT_NAME: The full resource name of the product. Format: 
    * `projects/PROJECT_ID/locations/LOCATION_ID/products/PRODUCT_ID`



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id:removeProduct

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
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id:removeProduct"

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
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id:removeProduct" | Select-Object -Expand Content

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
    
    // removeProductFromProductSet removes a product from a product set.
    func removeProductFromProductSet(w io.Writer, projectID string, location string, productID string, productSetID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[RemoveProductFromProductSetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_RemoveProductFromProductSetRequest){
    		Name:    fmt.Sprintf("projects/%s/locations/%s/productSets/%s", projectID, location, productSetID),
    		Product: fmt.Sprintf("projects/%s/locations/%s/products/%s", projectID, location, productID),
    	}
    
    	if err = c.RemoveProductFromProductSet(ctx, req); err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product removed from product set.\n")
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Remove a product from a product set.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @param productSetId - Id of the product set.
     * @throws IOException - on I/O errors.
     */
    public static void removeProductFromProductSet(
        String projectId, String computeRegion, String productId, String productSetId)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product set.
        String formattedParent = ProductSetName.format(projectId, computeRegion, productSetId);
    
        // Get the full path of the product.
        String formattedName = ProductName.format(projectId, computeRegion, productId);
    
        // Remove the product from the product set.
        client.removeProductFromProductSet(formattedParent, formattedName);
    
        System.out.println(String.format("Product removed from product set."));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function removeProductFromProductSet() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      const productSetPath = client.productSetPath(
        projectId,
        location,
        productSetId
      );
    
      const productPath = client.productPath(projectId, location, productId);
    
      const request = {
        name: productSetPath,
        product: productPath,
      };
    
      await client.removeProductFromProductSet(request);
      console.log('Product removed from product set.');
    }
    removeProductFromProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def remove_product_from_product_set(project_id, location, product_id, product_set_id):
        """Remove a product from a product set.
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
    
        # Remove the product from the product set.
        client.[remove_product_from_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_remove_product_from_product_set)(name=product_set_path, product=product_path)
        print("Product removed from product set.")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
