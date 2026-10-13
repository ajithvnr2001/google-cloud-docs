---
url: https://docs.cloud.google.com/compute/docs/samples/compute-images-list/
title: List all non-deprecated images in a project \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:41.631179+00:00
---

# List all non-deprecated images in a project  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-images-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  List all non-deprecated images in a project Stay organized with collections  Save and categorize content based on your preferences. 

Get a list of all non-deprecated images available in a specified project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create an instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-public-image)
  * [Using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System;
    using System.Threading.Tasks;
    
    public class ListImagesAsyncSample
    {
        public async Task ListImagesAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id")
        {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [ImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html) client = await [ImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html#Google_Cloud_Compute_V1_ImagesClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Make the request to list all non-deprecated images in a project.
            [ListImagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListImagesRequest.html) request = new [ListImagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListImagesRequest.html)
            {
                Project = projectId,
                // Listing only non-deprecated images to reduce the size of the reply.
                Filter = "deprecated.state != DEPRECATED",
                // MaxResults indicates the maximum number of items that will be returned per page.
                MaxResults = 100
            };
    
            // Although the MaxResults parameter is specified in the request, the sequence returned
            // by the ListAsync() method hides the pagination mechanic. The library makes multiple
            // requests to the API for you, so you can simply iterate over all the images.
            await foreach (var image in client.[ListAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html#Google_Cloud_Compute_V1_ImagesClient_ListAsync_Google_Cloud_Compute_V1_ListImagesRequest_Google_Api_Gax_Grpc_CallSettings_)(request))
            {
                // The result is an Image collection.
                Console.WriteLine($"Image: {image.Name}");
            }
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/api/iterator"
    	"google.golang.org/protobuf/proto"
    )
    
    // printImagesList prints a list of all non-deprecated image names available in given project.
    func printImagesList(w io.Writer, projectID string) error {
    	// projectID := "your_project_id"
    	ctx := context.Background()
    	imagesClient, err := compute.[NewImagesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ImagesClient_NewImagesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImagesRESTClient: %w", err)
    	}
    	defer imagesClient.Close()
    
    	// Listing only non-deprecated images to reduce the size of the reply.
    	req := &computepb.ListImagesRequest{
    		Project:    projectID,
    		MaxResults: proto.Uint32(3),
    		Filter:     proto.String("deprecated.state != DEPRECATED"),
    	}
    
    	// Although the `MaxResults` parameter is specified in the request, the iterator returned
    	// by the `list()` method hides the pagination mechanic. The library makes multiple
    	// requests to the API for you, so you can simply iterate over all the images.
    	it := imagesClient.List(ctx, req)
    	for {
    		image, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s\n", image.GetName())
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).ListPage;
    import com.google.cloud.compute.v1.[ListImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListImagesRequest.html);
    import java.io.IOException;
      // Prints a list of all non-deprecated image names available in given project.
      public static void listImages(String project) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to
        // safely clean up any remaining background resources.
        try ([ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html) imagesClient = [ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).create()) {
    
          // Listing only non-deprecated images to reduce the size of the reply.
          [ListImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListImagesRequest.html) imagesRequest = [ListImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListImagesRequest.html).newBuilder()
              .setProject(project)
              .setMaxResults(100)
              .setFilter("deprecated.state != DEPRECATED")
              .build();
    
          // Although the `setMaxResults` parameter is specified in the request, the iterable returned
          // by the `list()` method hides the pagination mechanic. The library makes multiple
          // requests to the API for you, so you can simply iterate over all the images.
          int imageCount = 0;
          for ([Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html) image : imagesClient.list(imagesRequest).iterateAll()) {
            imageCount++;
            System.out.println(image.getName());
          }
          System.out.printf("Image count in %s is: %s", project, imageCount);
        }
      }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function listImages() {
      const imagesClient = new compute.[ImagesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Listing only non-deprecated images to reduce the size of the reply.
      const images = imagesClient.listAsync({
        project: projectId,
        maxResults: 3,
        filter: 'deprecated.state != DEPRECATED',
      });
    
      // Although the `maxResults` parameter is specified in the request, the iterable returned
      // by the `listAsync()` method hides the pagination mechanic. The library makes multiple
      // requests to the API for you, so you can simply iterate over all the images.
      for await (const image of images) {
        console.log(` - ${image.name}`);
      }
    }
    
    listImages();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Compute\V1\Client\ImagesClient;
    use Google\Cloud\Compute\V1\ListImagesRequest;
    
    /**
     * Prints a list of all non-deprecated image names available in given project.
     *
     * @param string $projectId Project ID or project number of the Cloud project you want to list images from.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     */
    function list_all_images(string $projectId)
    {
        $imagesClient = new ImagesClient();
        // Listing only non-deprecated images to reduce the size of the reply.
        $optionalArgs = ['maxResults' => 100, 'filter' => 'deprecated.state != DEPRECATED'];
    
        /**
         * Although the maxResults parameter is specified in the request, the iterateAllElements() method
         * hides the pagination mechanic. The library makes multiple requests to the API for you,
         * so you can simply iterate over all the images.
         */
        $request = (new ListImagesRequest())
            ->setProject($projectId)
            ->setMaxResults($optionalArgs['maxResults'])
            ->setFilter($optionalArgs['filter']);
        $pagedResponse = $imagesClient->list($request);
        print('=================== Flat list of images ===================' . PHP_EOL);
        foreach ($pagedResponse->iterateAllElements() as $element) {
            printf(' - %s' . PHP_EOL, $element->getName());
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.compute_v1 as compute_v1
    
    def print_images_list(project: str) -> str:
        """
        Prints a list of all non-deprecated image names available in given project.
    
        Args:
            project: project ID or project number of the Cloud project you want to list images from.
    
        Returns:
            The output as a string.
        """
        images_client = compute_v1.ImagesClient()
        # Listing only non-deprecated images to reduce the size of the reply.
        images_list_request = compute_v1.ListImagesRequest(
            project=project, max_results=100, filter="deprecated.state != DEPRECATED"
        )
        output = []
    
        # Although the `max_results` parameter is specified in the request, the iterable returned
        # by the `list()` method hides the pagination mechanic. The library makes multiple
        # requests to the API for you, so you can simply iterate over all the images.
        for img in images_client.list(request=images_list_request):
            print(f" -  {img.name}")
            output.append(f" -  {img.name}")
        return "\n".join(output)
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/compute/v1"
    
    # Prints a list of all non-deprecated image names available in given project.
    #
    # @param [String] project project ID or project number of the Cloud project you want to list images from.
    def print_images_list project:
      client = ::Google::Cloud::Compute::V1::Images::Rest::Client.new
    
      # Make the request to list all non-deprecated images in a project.
      request = {
        project: project,
        # max_results indicates the maximum number of items that will be returned per page.
        max_results: 100,
        # Listing only non-deprecated images to reduce the size of the reply.
        filter: "deprecated.state != DEPRECATED"
      }
    
      # Although the `max_results` parameter is specified in the request, the iterable returned
      # by the `list` method hides the pagination mechanic. The library makes multiple
      # requests to the API for you, so you can simply iterate over all the images.
      client.list(request).each do |image|
        puts " - #{image.name}"
      end
    end

### Rust
    
    
    pub use google_cloud_compute_v1::client::Images;
    pub use google_cloud_gax::paginator::ItemPaginator;
    
    pub async fn sample(client: &Images, project_id: &str) -> anyhow::Result<()> {
        let mut items = client
            .list()
            .set_project(project_id)
            // Maximum number of results per page. Higher values reduce the number
            // of RPCs, but increase memory usage.
            .set_max_results(100_u32)
            // Skip deprecated images.
            .set_filter("deprecated.state != DEPRECATED")
            .by_item();
        println!("iterating by item:");
        while let Some(image) = items.next().await.transpose()? {
            println!("item = {:?}", image);
        }
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
