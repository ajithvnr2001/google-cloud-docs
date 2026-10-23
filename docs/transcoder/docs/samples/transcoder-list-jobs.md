---
url: https://docs.cloud.google.com/transcoder/docs/samples/transcoder-list-jobs/
title: List jobs \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:04.527790+00:00
---

# List jobs  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/samples/transcoder-list-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Samples ](https://docs.cloud.google.com/transcoder/docs/samples)



#  List jobs Stay organized with collections  Save and categorize content based on your preferences. 

List all of the transcoding jobs for a given location.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and managing jobs](https://docs.cloud.google.com/transcoder/docs/how-to/jobs)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Transcoder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using System.Linq;
    using System.Collections.Generic;
    
    public class ListJobsSample
    {
        public IList<Job> ListJobs(string projectId, string location)
        {
            // Create the client.
            [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html) client = [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_Create)();
    
            // Build the parent location name.
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) parentLocation = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, location);
    
            // Call the API.
            PagedEnumerable<ListJobsResponse, Job> response = client.[ListJobs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_ListJobs_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(parentLocation);
    
            // The returned sequence will lazily perform RPCs as it's being iterated over.
            return response.ToList();
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/transcoder). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"google.golang.org/api/iterator"
    
    	transcoder "cloud.google.com/go/video/transcoder/apiv1"
    	"cloud.google.com/go/video/transcoder/apiv1/transcoderpb"
    )
    
    // listJobs lists all jobs for a given location. See
    // https://cloud.google.com/transcoder/docs/how-to/jobs#list_jobs for more
    // information.
    func listJobs(w io.Writer, projectID string, location string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	ctx := context.Background()
    	client, err := transcoder.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_Close)()
    
    	req := &transcoderpb.ListJobsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    	}
    
    	it := client.ListJobs(ctx, req)
    	fmt.Fprintln(w, "Jobs:")
    
    	for {
    		response, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListJobs: %w", err)
    		}
    		fmt.Fprintln(w, response.GetName())
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html);
    import com.google.cloud.video.transcoder.v1.[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ListJobsRequest.html);
    import com.google.cloud.video.transcoder.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import java.io.IOException;
    
    public class ListJobs {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
    
        listJobs(projectId, location);
      }
    
      // Lists the jobs for a given location.
      public static void listJobs(String projectId, String location) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html) transcoderServiceClient = [TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html).create()) {
    
          [ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ListJobsRequest.html) listJobsRequest =
              [ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ListJobsRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html).of(projectId, location).toString())
                  .build();
    
          // Send the list jobs request and process the response.
          [TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html).[ListJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.ListJobsPagedResponse.html) response =
              transcoderServiceClient.listJobs(listJobsRequest);
          System.out.println("Jobs:");
    
          for ([Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html) job : response.iterateAll()) {
            System.out.println(job.getName());
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function listJobs() {
      const iterable = await transcoderServiceClient.[listJobsAsync](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)({
        parent: transcoderServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location),
      });
      console.info('Jobs:');
      for await (const response of iterable) {
        console.log(response.name);
      }
    }
    
    listJobs();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\ListJobsRequest;
    
    /**
     * Lists all Transcoder jobs in a location.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the jobs.
     */
    function list_jobs($projectId, $location)
    {
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedParent = $transcoderServiceClient->locationName($projectId, $location);
        $request = (new ListJobsRequest())
            ->setParent($formattedParent);
        $response = $transcoderServiceClient->listJobs($request);
    
        // Print job list.
        $jobs = $response->iterateAllElements();
        print('Jobs:' . PHP_EOL);
        foreach ($jobs as $job) {
            printf('%s' . PHP_EOL, $job->getName());
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video.transcoder_v1.services.transcoder_service import (
        pagers,
        TranscoderServiceClient,
    )
    
    
    def list_jobs(
        project_id: str,
        location: str,
    ) -> pagers.ListJobsPager:
        """Lists all jobs in a location.
    
        Args:
            project_id: The GCP project ID.
            location: The location of the jobs.
    
        Returns:
            An iterable object containing job resources.
        """
    
        client = TranscoderServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        response = client.list_jobs(parent=parent)
        print("Jobs:")
        for job in response.jobs:
            print({job.name})
    
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location   = "YOUR-JOB-LOCATION"  # (e.g. "us-central1")
    
    # Require the Transcoder client library.
    require "google/cloud/video/transcoder"
    
    # Create a Transcoder client.
    client = Google::Cloud::Video::Transcoder.transcoder_service
    
    # Build the resource name of the parent.
    parent = client.location_path project: project_id, location: location
    
    # Get the list of jobs.
    response = client.list_jobs parent: parent
    
    puts "Jobs:"
    # Print out all jobs.
    response.each do |job|
      puts job.name
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=transcoderapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
