---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-get-batch-prediction-job-sample/
title: Get a batch prediction job \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:24.154096+00:00
---

# Get a batch prediction job  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-get-batch-prediction-job-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Get a batch prediction job Stay organized with collections  Save and categorize content based on your preferences. 

Gets a batch prediction job using the get_batch_prediction_job method.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html);
    import com.google.cloud.aiplatform.v1.[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.html);
    import com.google.cloud.aiplatform.v1.[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.OutputConfig.html);
    import com.google.cloud.aiplatform.v1.[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).[OutputInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.OutputInfo.html);
    import com.google.cloud.aiplatform.v1.[BatchPredictionJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJobName.html);
    import com.google.cloud.aiplatform.v1.[BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html);
    import com.google.cloud.aiplatform.v1.[BigQuerySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.html);
    import com.google.cloud.aiplatform.v1.[CompletionStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CompletionStats.html);
    import com.google.cloud.aiplatform.v1.[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html);
    import com.google.cloud.aiplatform.v1.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html);
    import com.google.cloud.aiplatform.v1.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html);
    import com.google.cloud.aiplatform.v1.[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[ResourcesConsumed](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ResourcesConsumed.html);
    import com.google.protobuf.[Any](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Any.html);
    import com.google.rpc.[Status](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html);
    import java.io.IOException;
    import java.util.List;
    
    public class GetBatchPredictionJobSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String batchPredictionJobId = "YOUR_BATCH_PREDICTION_JOB_ID";
        getBatchPredictionJobSample(project, batchPredictionJobId);
      }
    
      static void getBatchPredictionJobSample(String project, String batchPredictionJobId)
          throws IOException {
        [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html) jobServiceSettings =
            [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html) jobServiceClient = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html).create(jobServiceSettings)) {
          String location = "us-central1";
          [BatchPredictionJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJobName.html) batchPredictionJobName =
              [BatchPredictionJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJobName.html).of(project, location, batchPredictionJobId);
    
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) batchPredictionJob =
              jobServiceClient.getBatchPredictionJob(batchPredictionJobName);
    
          System.out.println("Get Batch Prediction Job Response");
          System.out.format("\tName: %s\n", batchPredictionJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getName__)());
          System.out.format("\tDisplay Name: %s\n", batchPredictionJob.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getDisplayName__)());
          System.out.format("\tModel: %s\n", batchPredictionJob.[getModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getModel__)());
    
          System.out.format("\tModel Parameters: %s\n", batchPredictionJob.[getModelParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getModelParameters__)());
          System.out.format("\tState: %s\n", batchPredictionJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getState__)());
    
          System.out.format("\tCreate Time: %s\n", batchPredictionJob.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getCreateTime__)());
          System.out.format("\tStart Time: %s\n", batchPredictionJob.[getStartTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getStartTime__)());
          System.out.format("\tEnd Time: %s\n", batchPredictionJob.[getEndTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getEndTime__)());
          System.out.format("\tUpdate Time: %s\n", batchPredictionJob.[getUpdateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getUpdateTime__)());
          System.out.format("\tLabels: %s\n", batchPredictionJob.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getLabelsMap__)());
    
          [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.html) inputConfig = batchPredictionJob.[getInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getInputConfig__)();
          System.out.println("\tInput Config");
          System.out.format("\t\tInstances Format: %s\n", inputConfig.getInstancesFormat());
    
          [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html) gcsSource = inputConfig.getGcsSource();
          System.out.println("\t\tGcs Source");
          System.out.format("\t\t\tUris: %s\n", gcsSource.[getUrisList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html#com_google_cloud_aiplatform_v1_GcsSource_getUrisList__)());
    
          [BigQuerySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.html) bigquerySource = inputConfig.getBigquerySource();
          System.out.println("\t\tBigquery Source");
          System.out.format("\t\t\tInput Uri: %s\n", bigquerySource.[getInputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.html#com_google_cloud_aiplatform_v1_BigQuerySource_getInputUri__)());
    
          [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.OutputConfig.html) outputConfig = batchPredictionJob.[getOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getOutputConfig__)();
          System.out.println("\tOutput Config");
          System.out.format("\t\tPredictions Format: %s\n", outputConfig.getPredictionsFormat());
    
          [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html) gcsDestination = outputConfig.[getGcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.OutputConfig.html#com_google_cloud_aiplatform_v1_OutputConfig_getGcsDestination__)();
          System.out.println("\t\tGcs Destination");
          System.out.format("\t\t\tOutput Uri Prefix: %s\n", gcsDestination.[getOutputUriPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html#com_google_cloud_aiplatform_v1_GcsDestination_getOutputUriPrefix__)());
    
          [BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html) bigqueryDestination = outputConfig.getBigqueryDestination();
          System.out.println("\t\tBigquery Destination");
          System.out.format("\t\t\tOutput Uri: %s\n", bigqueryDestination.[getOutputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html#com_google_cloud_aiplatform_v1_BigQueryDestination_getOutputUri__)());
    
          [OutputInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.OutputInfo.html) outputInfo = batchPredictionJob.[getOutputInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getOutputInfo__)();
          System.out.println("\tOutput Info");
          System.out.format("\t\tGcs Output Directory: %s\n", outputInfo.[getGcsOutputDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.OutputInfo.html#com_google_cloud_aiplatform_v1_OutputInfo_getGcsOutputDirectory__)());
          System.out.format("\t\tBigquery Output Dataset: %s\n", outputInfo.getBigqueryOutputDataset());
    
          [Status](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html) status = batchPredictionJob.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getError__)();
          System.out.println("\tError");
          System.out.format("\t\tCode: %s\n", status.[getCode](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getCode__)());
          System.out.format("\t\tMessage: %s\n", status.[getMessage](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getMessage__)());
    
          List<Any> detailsList = status.[getDetailsList](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getDetailsList__)();
    
          for ([Status](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html) partialFailure : batchPredictionJob.[getPartialFailuresList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getPartialFailuresList__)()) {
            System.out.println("\tPartial Failure");
            System.out.format("\t\tCode: %s\n", partialFailure.getCode());
            System.out.format("\t\tMessage: %s\n", partialFailure.getMessage());
            List<Any> details = partialFailure.getDetailsList();
          }
    
          [ResourcesConsumed](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ResourcesConsumed.html) resourcesConsumed = batchPredictionJob.[getResourcesConsumed](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getResourcesConsumed__)();
          System.out.println("\tResources Consumed");
          System.out.format("\t\tReplica Hours: %s\n", resourcesConsumed.[getReplicaHours](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ResourcesConsumed.html#com_google_cloud_aiplatform_v1_ResourcesConsumed_getReplicaHours__)());
    
          [CompletionStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CompletionStats.html) completionStats = batchPredictionJob.[getCompletionStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getCompletionStats__)();
          System.out.println("\tCompletion Stats");
          System.out.format("\t\tSuccessful Count: %s\n", completionStats.[getSuccessfulCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CompletionStats.html#com_google_cloud_aiplatform_v1_CompletionStats_getSuccessfulCount__)());
          System.out.format("\t\tFailed Count: %s\n", completionStats.[getFailedCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CompletionStats.html#com_google_cloud_aiplatform_v1_CompletionStats_getFailedCount__)());
          System.out.format("\t\tIncomplete Count: %s\n", completionStats.[getIncompleteCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CompletionStats.html#com_google_cloud_aiplatform_v1_CompletionStats_getIncompleteCount__)());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    
    
    def get_batch_prediction_job_sample(
        project: str,
        batch_prediction_job_id: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html)(client_options=client_options)
        name = client.[batch_prediction_job_path](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html#google_cloud_aiplatform_v1_services_job_service_JobServiceClient_batch_prediction_job_path)(
            project=project, location=location, batch_prediction_job=batch_prediction_job_id
        )
        response = client.[get_batch_prediction_job](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html#google_cloud_aiplatform_v1_services_job_service_JobServiceClient_get_batch_prediction_job)(name=name)
        print("response:", response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
