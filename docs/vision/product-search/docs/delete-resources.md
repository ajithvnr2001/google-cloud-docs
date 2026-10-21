---
url: https://docs.cloud.google.com/vision/product-search/docs/delete-resources/
title: Deleting resources \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:10:12.748358+00:00
---

# Deleting resources  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/delete-resources/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/product-search/docs/create-product-set-search-products)



Send feedback 

#  Deleting resources Stay organized with collections  Save and categorize content based on your preferences. 

You can delete reference image, product, or product set resources created by the API.

## Individual resource deletion

### Deleting a reference image

You can delete a reference image associated with a product.

After the operation request the images are marked for deletion, but will remain in the product until the next time it is indexed.

The actual image files in Cloud Storage are NOT deleted by this operation. Only the reference to the image is removed from the product.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_ID: The ID for the product that is associated with a reference image. This ID is either randomly set or specified by the user at product creation time.
  * IMAGE_ID: The ID of the target image resource.



HTTP method and URL: 
    
    
    DELETE https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages/image-id

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages/image-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages/image-id" | Select-Object -Expand Content

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
    
    // deleteReferenceImage deletes a reference image from a product.
    func deleteReferenceImage(w io.Writer, projectID string, location string, productID string, referenceImageID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[DeleteReferenceImageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_DeleteReferenceImageRequest){
    		Name: fmt.Sprintf("projects/%s/locations/%s/products/%s/referenceImages/%s", projectID, location, productID, referenceImageID),
    	}
    
    	if err = c.DeleteReferenceImage(ctx, req); err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    
    	fmt.Fprintf(w, "Reference image deleted from product.\n")
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Delete a reference image.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @param referenceImageId - Id of the image.
     * @throws IOException - on I/O errors.
     */
    public static void deleteReferenceImage(
        String projectId, String computeRegion, String productId, String referenceImageId)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the reference image.
        String formattedName =
            ImageName.format(projectId, computeRegion, productId, referenceImageId);
        // Delete the reference image.
        client.deleteReferenceImage(formattedName);
        System.out.println("Reference image deleted from product.");
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function deleteReferenceImage() {
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
    
      await client.deleteReferenceImage(request);
      console.log('Reference image deleted from product.');
    }
    deleteReferenceImage();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def delete_reference_image(project_id, location, product_id, reference_image_id):
        """Delete a reference image.
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
    
        # Delete the reference image.
        client.[delete_reference_image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_delete_reference_image)(name=reference_image_path)
        print("Reference image deleted from product.")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

### Deleting a product

You can delete a product associated with a specific project.

Deleting a Product causes its child images to be deleted.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_ID: The ID for the product that is associated with a reference image. This ID is either randomly set or specified by the user at product creation time.



HTTP method and URL: 
    
    
    DELETE https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id" | Select-Object -Expand Content

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
    
    // deleteProduct deletes a product.
    func deleteProduct(w io.Writer, projectID string, location string, productID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[DeleteProductRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_DeleteProductRequest){
    		Name: fmt.Sprintf("projects/%s/locations/%s/products/%s", projectID, location, productID),
    	}
    
    	if err = c.DeleteProduct(ctx, req); err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product deleted.\n")
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Delete the product and all its reference images.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @throws IOException - on I/O errors.
     */
    public static void deleteProduct(String projectId, String computeRegion, String productId)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product.
        String formattedName = ProductName.format(projectId, computeRegion, productId);
    
        // Delete a product.
        client.deleteProduct(formattedName);
        System.out.println("Product deleted.");
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function deleteProduct() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
    
      // Resource path that represents full path to the product.
      const productPath = client.productPath(projectId, location, productId);
    
      await client.deleteProduct({name: productPath});
      console.log('Product deleted.');
    }
    deleteProduct();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    from google.protobuf import field_mask_pb2 as field_mask
    
    def delete_product(project_id, location, product_id):
        """Delete the product and all its reference images.
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
    
        # Delete a product.
        client.[delete_product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_delete_product)(name=product_path)
        print("Product deleted.")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

### Deleting a product set

You can also delete a product set.

Deleting a product set immediately removes the product set from results. However, deleting a product set **will not** remove individual products in the set, as a product may belong to several different sets. You do not need to wait for the next index for the change to take effect.

The actual image files in Cloud Storage are NOT deleted by this operation. `ReferenceImage` resources created by the API are not removed.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_SET_ID: The ID for the product set you want to run the operation on.



HTTP method and URL: 
    
    
    DELETE https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets/product-set-id" | Select-Object -Expand Content

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
    
    // deleteProductSet deletes a product set.
    func deleteProductSet(w io.Writer, projectID string, location string, productSetID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[DeleteProductSetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_DeleteProductSetRequest){
    		Name: fmt.Sprintf("projects/%s/locations/%s/productSets/%s", projectID, location, productSetID),
    	}
    
    	if err = c.DeleteProductSet(ctx, req); err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    
    	fmt.Fprintln(w, "Product set deleted.")
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Delete a product set.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productSetId - Id of the product set.
     * @throws IOException - on I/O errors.
     */
    public static void deleteProductSet(String projectId, String computeRegion, String productSetId)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product set.
        String formattedName = ProductSetName.format(projectId, computeRegion, productSetId);
        // Delete the product set.
        client.deleteProductSet(formattedName);
        System.out.println(String.format("Product set deleted"));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function deleteProductSet() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productSetId = 'Id of the product set';
    
      // Resource path that represents full path to the product set.
      const productSetPath = client.productSetPath(
        projectId,
        location,
        productSetId
      );
    
      await client.deleteProductSet({name: productSetPath});
      console.log('Product set deleted.');
    }
    deleteProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def delete_product_set(project_id, location, product_set_id):
        """Delete a product set.
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
    
        # Delete the product set.
        client.[delete_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_delete_product_set)(name=product_set_path)
        print("Product set deleted.")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Batch resource deletion

You can now batch delete products. Product batch deletion is available for the following product types:

  * All products in a specific product set
  * All products that belong to _no_ product set



To avoid concurrent operation errors, wait to delete the product set after this batch product delete operation has completed. If reusing the emptied product set, also wait until batch deletion is finished before importing new products.

These considerations are similar for individual products; you should avoid acting on any individual products involved in batch deletion. For example, you shouldn't add any of these products to another product set, as they will eventually be deleted.

**Batch deletion (`purge`) cannot be undone**. You should keep a CSV for batch import with the products to be deleted if you need to re-import the data. 

### Delete products in a product set

You can delete all products in a given product set by specifying the product set ID in the request.

All products in the product set will be deleted **regardless of if they belong to _other_ product sets**.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_SET_ID: The ID for the product set you want to run the operation on.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products:purge

Request JSON body: 
    
    
    {
      "force": "true",
      "productSetPurgeConfig": {
        "productSetId": "product-set-id"
      }
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
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products:purge"

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
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products:purge" | Select-Object -Expand Content

This request starts a long-running operation. The JSON response contains information about this long-running operation: 
    
    
    {
    "name": "projects/project-id/locations/location-id/operations/**bc4e1d412863e626** "
    }

In this case, the operation-id is `bc4e1d412863e626`.

You can track the progress of this operation using the operation-id. For an example of getting an operation's status, see Getting the status of an operation. 

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
    
    // purgeProductsInProductSet deletes all products in a product set.
    func purgeProductsInProductSet(w io.Writer, projectID string, location string, productSetID string) error {
    	// projectID := "your-gcp-project-id"
    	// location := "us-west1"
    	// productSetID := "sampleProductSetID"
    
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[PurgeProductsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_PurgeProductsRequest){
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		Target: &visionpb.[PurgeProductsRequest_ProductSetPurgeConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_PurgeProductsRequest_ProductSetPurgeConfig){
    			ProductSetPurgeConfig: &visionpb.[ProductSetPurgeConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ProductSetPurgeConfig){
    				ProductSetId: productSetID,
    			},
    		},
    		Force: true,
    	}
    
    	// The purge operation is async.
    	op, err := c.PurgeProducts(ctx, req)
    	if err != nil {
    		return fmt.Errorf("PurgeProducts: %w", err)
    	}
    	fmt.Fprintf(w, "Processing operation name: %q\n", op.Name())
    
    	if err := op.Wait(ctx); err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted products in product set.\n")
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.vision.v1.[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchOperationMetadata.html);
    import com.google.cloud.vision.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.LocationName.html);
    import com.google.cloud.vision.v1.[ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html);
    import com.google.cloud.vision.v1.[ProductSetPurgeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSetPurgeConfig.html);
    import com.google.cloud.vision.v1.[PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    import java.util.concurrent.TimeUnit;
    
    public class PurgeProductsInProductSet {
    
      // Delete all products in a product set.
      public static void purgeProductsInProductSet(
          String projectId, String location, String productSetId) throws Exception {
    
        // String projectId = "YOUR_PROJECT_ID";
        // String location = "us-central1";
        // String productSetId = "YOUR_PRODUCT_SET_ID";
        // boolean force = true;
    
        try ([ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html) client = [ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html).create()) {
    
          String parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.LocationName.html).format(projectId, location);
          [ProductSetPurgeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSetPurgeConfig.html) productSetPurgeConfig =
              [ProductSetPurgeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSetPurgeConfig.html).newBuilder().setProductSetId(productSetId).build();
    
          [PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.html) request =
              [PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.html).newBuilder()
                  .setParent(parent)
                  .[setProductSetPurgeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.Builder.html#com_google_cloud_vision_v1_PurgeProductsRequest_Builder_setProductSetPurgeConfig_com_google_cloud_vision_v1_ProductSetPurgeConfig_)(productSetPurgeConfig)
                  // The operation is irreversible and removes multiple products.
                  // The user is required to pass in force=True to actually perform the
                  // purge.
                  // If force is not set to True, the service raises an exception.
                  .[setForce](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.Builder.html#com_google_cloud_vision_v1_PurgeProductsRequest_Builder_setForce_boolean_)(true)
                  .build();
    
          OperationFuture<Empty, BatchOperationMetadata> response = client.[purgeProductsAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html#com_google_cloud_vision_v1_ProductSearchClient_purgeProductsAsync__org_jspecify_annotations_Nullable_com_google_cloud_vision_v1_LocationName_)(request);
          response.getPollingFuture().get(180, TimeUnit.SECONDS);
    
          System.out.println("Products removed from product set.");
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
    
    async function purgeProductsInProductSet() {
      // Deletes all products in a product set.
    
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productSetId = 'Id of the product set';
    
      const formattedParent = client.locationPath(projectId, location);
      const purgeConfig = {productSetId: productSetId};
    
      // The operation is irreversible and removes multiple products.
      // The user is required to pass in force=true to actually perform the purge.
      // If force is not set to True, the service raises an error.
      const force = true;
    
      try {
        const [operation] = await client.purgeProducts({
          parent: formattedParent,
          productSetPurgeConfig: purgeConfig,
          force: force,
        });
        await operation.promise();
        console.log('Products removed from product set.');
      } catch (err) {
        console.log(err);
      }
    }
    purgeProductsInProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def purge_products_in_product_set(project_id, location, product_set_id, force):
        """Delete all products in a product set.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
            force: Perform the purge only when force is set to True.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        product_set_purge_config = vision.[ProductSetPurgeConfig](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ProductSetPurgeConfig.html)(
            product_set_id=product_set_id
        )
    
        # The purge operation is async.
        operation = client.[purge_products](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_purge_products)(
            request={
                "parent": parent,
                "product_set_purge_config": product_set_purge_config,
                # The operation is irreversible and removes multiple products.
                # The user is required to pass in force=True to actually perform the
                # purge.
                # If force is not set to True, the service raises an exception.
                "force": force,
            }
        )
    
        operation.result(timeout=500)
    
        print("Deleted products in product set.")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

### Delete orphan products

You can delete all products _not_ in a product set by specifying this option in the request.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products:purge

Request JSON body: 
    
    
    {
      "force": "true",
      "deleteOrphanProducts": "true"
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
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products:purge"

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
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products:purge" | Select-Object -Expand Content

This request starts a long-running operation. The JSON response contains information about this long-running operation: 
    
    
    {
    "name": "projects/project-id/locations/location-id/operations/**bc4e1d412863e626** "
    }

In this case, the operation-id is `bc4e1d412863e626`.

You can track the progress of this operation using the operation-id. For an example of getting an operation's status, see Getting the status of an operation. 

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
    
    // purgeOrphanProducts deletes all products not in any product sets.
    func purgeOrphanProducts(w io.Writer, projectID string, location string) error {
    	// projectID := "your-gcp-project-id"
    	// location := "us-west1"
    
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[PurgeProductsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_PurgeProductsRequest){
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		Target: &visionpb.[PurgeProductsRequest_DeleteOrphanProducts](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_PurgeProductsRequest_DeleteOrphanProducts){
    			DeleteOrphanProducts: true,
    		},
    		Force: true,
    	}
    
    	// The purge operation is async.
    	op, err := c.PurgeProducts(ctx, req)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	fmt.Fprintf(w, "Processing operation name: %q\n", op.Name())
    
    	if err := op.Wait(ctx); err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Orphan products deleted.\n")
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.vision.v1.[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchOperationMetadata.html);
    import com.google.cloud.vision.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.LocationName.html);
    import com.google.cloud.vision.v1.[ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html);
    import com.google.cloud.vision.v1.[PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    import java.util.concurrent.TimeUnit;
    
    public class PurgeProducts {
    
      // Delete the product and all its reference images.
      public static void purgeOrphanProducts(String projectId, String computeRegion) throws Exception {
    
        // String projectId = "YOUR_PROJECT_ID";
        // String computeRegion = "us-central1";
        // boolean force = true;
    
        try ([ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html) client = [ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html).create()) {
          String parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.LocationName.html).format(projectId, computeRegion);
    
          // The purge operation is async.
          [PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.html) request =
              [PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.html).newBuilder()
                  .[setDeleteOrphanProducts](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.Builder.html#com_google_cloud_vision_v1_PurgeProductsRequest_Builder_setDeleteOrphanProducts_boolean_)(true)
                  // The operation is irreversible and removes multiple products.
                  // The user is required to pass in force=True to actually perform the
                  // purge.
                  // If force is not set to True, the service raises an exception.
                  .[setForce](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.Builder.html#com_google_cloud_vision_v1_PurgeProductsRequest_Builder_setForce_boolean_)(true)
                  .setParent(parent)
                  .build();
    
          OperationFuture<Empty, BatchOperationMetadata> response = client.[purgeProductsAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html#com_google_cloud_vision_v1_ProductSearchClient_purgeProductsAsync__org_jspecify_annotations_Nullable_com_google_cloud_vision_v1_LocationName_)(request);
          response.getPollingFuture().get(180, TimeUnit.SECONDS);
    
          System.out.println("Orphan products deleted.");
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
    
    async function purgeOrphanProducts() {
      // Deletes all products not in any product sets.
    
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
    
      const formattedParent = client.locationPath(projectId, location);
    
      // The operation is irreversible and removes multiple products.
      // The user is required to pass in force=true to actually perform the purge.
      // If force is not set to True, the service raises an error.
      const force = true;
    
      try {
        const [operation] = await client.purgeProducts({
          parent: formattedParent,
          deleteOrphanProducts: true,
          force: force,
        });
        await operation.promise();
        console.log('Orphan products deleted.');
      } catch (err) {
        console.log(err);
      }
    }
    purgeOrphanProducts();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    from google.protobuf import field_mask_pb2 as field_mask
    
    def purge_orphan_products(project_id, location, force):
        """Delete all products not in any product sets.
        Args:
            project_id: Id of the project.
            location: A compute region name.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        # The purge operation is async.
        operation = client.[purge_products](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_purge_products)(
            request={
                "parent": parent,
                "delete_orphan_products": True,
                # The operation is irreversible and removes multiple products.
                # The user is required to pass in force=True to actually perform the
                # purge.
                # If force is not set to True, the service raises an exception.
                "force": force,
            }
        )
    
        operation.result(timeout=500)
    
        print("Orphan products deleted.")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Getting the status of an operation

You can use the operation-id of a long-running operation (such as purge product set, or purge orphan products) to get its status.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * OPERATION_ID: The ID of your operation. The ID is the last element of the name of your operation. For example: 
    * operation name: `projects/PROJECT_ID/locations/LOCATION_ID/operations/**bc4e1d412863e626**`
    * operation id: `**bc4e1d412863e626**`



HTTP method and URL: 
    
    
    GET https://vision.googleapis.com/v1/locations/location-id/operations/operation-id

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/locations/location-id/operations/operation-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/locations/location-id/operations/operation-id" | Select-Object -Expand Content

You should see output similar to the following for a completed **product set purge operation** : 
    
    
    {
      "name": "locations/location-id/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.BatchOperationMetadata",
        "state": "SUCCESSFUL",
        "submitTime": "2019-09-04T15:58:39.131591882Z",
        "endTime": "2019-09-04T15:58:43.099020580Z"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.PurgeProductsRequest",
        "parent": "projects/project-id/locations/location-id",**"productSetPurgeConfig": {
          "productSetId": " project-set-id"
        },
        "force": true**
      }
    }

You should see output similar to the following for a completed **purge orphaned products operation** :
    
    
    {
      "name": "locations/location-id/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.BatchOperationMetadata",
        "state": "SUCCESSFUL",
        "submitTime": "2019-09-04T16:08:38.278197397Z",
        "endTime": "2019-09-04T16:08:45.075778639Z"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.PurgeProductsRequest",
        "parent": "projects/project-id/locations/location-id",**"deleteOrphanProducts": true,
        "force": true**
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
