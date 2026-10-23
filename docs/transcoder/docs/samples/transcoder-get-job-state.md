---
url: https://docs.cloud.google.com/transcoder/docs/samples/transcoder-get-job-state/
title: Get the job state \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:57.138492+00:00
---

# Get the job state  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/samples/transcoder-get-job-state/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Samples ](https://docs.cloud.google.com/transcoder/docs/samples)



#  Get the job state Stay organized with collections  Save and categorize content based on your preferences. 

Get the job state for a specific transcoding job.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Transcode a video with the Transcoder API](https://docs.cloud.google.com/transcoder/docs/transcode-video)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Transcoder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.html);
    
    public class GetJobStateSample
    {
        public Job.Types.ProcessingState GetJobState(string projectId, string location, string jobId)
        {
            // Create the client.
            [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html) client = [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_Create)();
    
            // Build the job name.
            [JobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobName.html) jobName = [JobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobName.html).[FromProjectLocationJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobName.html#Google_Cloud_Video_Transcoder_V1_JobName_FromProjectLocationJob_System_String_System_String_System_String_)(projectId, location, jobId);
    
            // Call the API.
            [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html) job = client.[GetJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_GetJob_Google_Cloud_Video_Transcoder_V1_GetJobRequest_Google_Api_Gax_Grpc_CallSettings_)(jobName);
    
            // Return the result.
            return job.[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html#Google_Cloud_Video_Transcoder_V1_Job_State);
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/transcoder). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	transcoder "cloud.google.com/go/video/transcoder/apiv1"
    	"cloud.google.com/go/video/transcoder/apiv1/transcoderpb"
    )
    
    // getJobState gets the state for a previously-created job. See
    // https://cloud.google.com/transcoder/docs/how-to/jobs#check_job_status for
    // more information.
    func getJobState(w io.Writer, projectID string, location string, jobID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// jobID := "my-job-id"
    	ctx := context.Background()
    	client, err := transcoder.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_Close)()
    
    	req := &transcoderpb.GetJobRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/jobs/%s", projectID, location, jobID),
    	}
    
    	response, err := client.GetJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetJob: %w", err)
    	}
    	fmt.Fprintf(w, "Job state: %v\n----\nJob failure reason:%v\n", response.State, response.Error)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.GetJobRequest.html);
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html);
    import com.google.cloud.video.transcoder.v1.[JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import java.io.IOException;
    
    public class GetJobState {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String jobId = "my-job-id";
    
        getJobState(projectId, location, jobId);
      }
    
      // Gets the state of a job.
      public static void getJobState(String projectId, String location, String jobId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html) transcoderServiceClient = [TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html).create()) {
          [JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html) jobName =
              [JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html).newBuilder().setProject(projectId).setLocation(location).setJob(jobId).build();
          [GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.GetJobRequest.html) getJobRequest = [GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.GetJobRequest.html).newBuilder().setName(jobName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html#com_google_cloud_video_transcoder_v1_JobName_toString__)()).build();
    
          // Send the get job request and process the response.
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html) job = transcoderServiceClient.getJob(getJobRequest);
          System.out.println("Job state: " + job.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html#com_google_cloud_video_transcoder_v1_Job_getState__)());
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
    // jobId = 'my-job-id';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function getJob() {
      // Construct request
      const request = {
        name: transcoderServiceClient.[jobPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location, jobId),
      };
      const [response] = await transcoderServiceClient.getJob(request);
      console.log(`Job state: ${response.state}`);
    }
    
    getJob();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\GetJobRequest;
    use Google\Cloud\Video\Transcoder\V1\Job;
    
    /**
     * Gets a Transcoder job's state.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the job.
     * @param string $jobId The job ID.
     */
    function get_job_state($projectId, $location, $jobId)
    {
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedName = $transcoderServiceClient->jobName($projectId, $location, $jobId);
        $request = (new GetJobRequest())
            ->setName($formattedName);
        $job = $transcoderServiceClient->getJob($request);
    
        // Print job state.
        printf('Job state: %s' . PHP_EOL, Job\ProcessingState::name($job->getState()));
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import transcoder_v1
    from google.cloud.video.transcoder_v1.services.transcoder_service import (
        TranscoderServiceClient,
    )
    
    
    def get_job_state(
        project_id: str,
        location: str,
        job_id: str,
    ) -> transcoder_v1.types.resources.Job:
        """Gets a job's state.
    
        Args:
            project_id: The GCP project ID.
            location: The location this job is in.
            job_id: The job ID.
    
        Returns:
            The job resource.
        """
    
        client = TranscoderServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/jobs/{job_id}"
        response = client.get_job(name=name)
    
        print(f"Job state: {str(response.state.name)}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location   = "YOUR-JOB-LOCATION"  # (e.g. "us-central1")
    # job_id     = "YOUR-JOB-ID"  # (e.g. "c82c295b-3f5a-47df-8562-938a89d40fd0")
    
    # Require the Transcoder client library.
    require "google/cloud/video/transcoder"
    
    # Create a Transcoder client.
    client = Google::Cloud::Video::Transcoder.transcoder_service
    
    # Build the resource name of the job.
    name = client.job_path project: project_id, location: location, job: job_id
    
    # Get the job.
    job = client.get_job name: name
    
    # Print the job state.
    puts "Job state: #{job.state}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=transcoderapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
