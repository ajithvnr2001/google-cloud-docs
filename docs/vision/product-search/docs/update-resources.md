---
url: https://docs.cloud.google.com/vision/product-search/docs/update-resources/
title: Updating resources \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:31.051565+00:00
---

# Updating resources  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/update-resources/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/product-search/docs/create-product-set-search-products)



Send feedback 

#  Updating resources Stay organized with collections  Save and categorize content based on your preferences. 

### Updating a product

You can update a product's labels via key-value pairs, such as `"style=womens"` or `"onSale=true"`, using the following code.

**Caution:** `update_product_labels` overwrites any existing labels. So if a product already has the label `"style=womens"` and the following function is used to add `"onSale=true"` the `"style"` label will be removed.

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
