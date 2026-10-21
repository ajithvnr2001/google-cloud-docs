---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-gcs-with-sampling/
title: Inspect storage with sampling \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:33.249932+00:00
---

# Inspect storage with sampling  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-gcs-with-sampling/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Inspect storage with sampling Stay organized with collections  Save and categorize content based on your preferences. 

The following examples demonstrate using the Cloud DLP API to scan a 90% subset of a Cloud Storage bucket for person names. The scan starts from a random location in the dataset and only includes text files under 200 bytes.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Inspect Google Cloud storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class InspectStorageWithSampling
    {
        public static async Task<DlpJob> InspectAsync(
            string projectId,
            string gcsUri,
            string topicId,
            string subId,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Possible](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Possible),
            IEnumerable<InfoType> infoTypes = null)
        {
    
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct Storage config by specifying the GCS file to be inspected
            // and sample method.
            var storageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
            {
                CloudStorageOptions = new [CloudStorageOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.html)
                {
                    FileSet = new CloudStorageOptions.Types.FileSet
                    {
                        Url = gcsUri
                    },
                    BytesLimitPerFile = 200,
                    FileTypes = { new [FileType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileType.html)[] { [FileType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileType.html).[Csv](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileType.html#Google_Cloud_Dlp_V2_FileType_Csv) } },
                    FilesLimitPercent = 90,
                    SampleMethod = [CloudStorageOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.Types.html).[SampleMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.Types.SampleMethod.html).[RandomStart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.Types.SampleMethod.html#Google_Cloud_Dlp_V2_CloudStorageOptions_Types_SampleMethod_RandomStart)
                }
            };
    
            // Construct the Inspect Config and specify the type of info the inspection
            // will look for.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes =
                {
                    infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[] { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" } }
                },
                IncludeQuote = true,
                MinLikelihood = minLikelihood
            };
    
            // Construct the pubsub action.
            var actions = new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)[]
            {
                new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)
                {
                    PubSub = new Action.Types.PublishToPubSub
                    {
                        Topic = $"projects/{projectId}/topics/{topicId}"
                    }
                }
            };
    
            // Construct the inspect job config using above created objects.
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = storageConfig,
                InspectConfig = inspectConfig,
                Actions = { actions }
            };
    
            // Issue Create Dlp Job Request
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                InspectJob = inspectJob,
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
            };
    
            // We keep the name of the job that we just created.
            var dlpJob = dlp.CreateDlpJob(request);
            var jobName = dlpJob.Name;
    
            // Listen to pub/sub for the job
            var subscriptionName = new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html)(projectId, subId);
            var subscriber = await [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_CreateAsync_Google_Cloud_PubSub_V1_SubscriptionName_)(
                subscriptionName);
    
            await subscriber.StartAsync(([PubsubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html) message, CancellationToken cancel) =>
            {
                if (message.Attributes["DlpJobName"] == jobName)
                {
                    subscriber.StopAsync(cancel);
                    return Task.FromResult(SubscriberClient.Reply.Ack);
                }
                else
                {
                    return Task.FromResult(SubscriberClient.Reply.Nack);
                }
            });
    
            // Get the latest state of the job from the service
            var resultJob = dlp.GetDlpJob(new [GetDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDlpJobRequest.html)
            {
                DlpJobName = [DlpJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html).[Parse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html#Google_Cloud_Dlp_V2_DlpJobName_Parse_System_String_)(jobName)
            });
    
            // Parse the response and process results.
            System.Console.WriteLine($"Job status: {resultJob.State}");
            System.Console.WriteLine($"Job Name: {resultJob.Name}");
    
            var result = resultJob.InspectDetails.Result;
            foreach (var infoType in result.[InfoTypeStats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeStats.html))
            {
                System.Console.WriteLine($"Info Type: {infoType.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html).Name}");
                System.Console.WriteLine($"Count: {infoType.Count}");
            }
            return resultJob;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    	"cloud.google.com/go/pubsub"
    )
    
    // inspectGcsFileWithSampling inspects a storage with sampling
    func inspectGcsFileWithSampling(w io.Writer, projectID, gcsUri, topicID, subscriptionId string) error {
    	// projectId := "your-project-id"
    	// gcsUri := "gs://" + "your-bucket-name" + "/path/to/your/file.txt"
    	// topicID := "your-pubsub-topic-id"
    	// subscriptionId := "your-pubsub-subscription-id"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    	// Closing the client safely cleans up background resources.
    	defer client.Close()
    
    	// Specify the GCS file to be inspected and sampling configuration
    	var cloudStorageOptions = &dlppb.CloudStorageOptions{
    		FileSet: &dlppb.CloudStorageOptions_FileSet{
    			Url: gcsUri,
    		},
    		BytesLimitPerFile: int64(200),
    		FileTypes: []dlppb.FileType{
    			dlppb.[FileType_TEXT_FILE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_FileType_FILE_TYPE_UNSPECIFIED_FileType_BINARY_FILE_FileType_TEXT_FILE_FileType_IMAGE_FileType_WORD_FileType_PDF_FileType_AVRO_FileType_CSV_FileType_TSV_FileType_POWERPOINT_FileType_EXCEL),
    		},
    		FilesLimitPercent: int32(90),
    		SampleMethod:      dlppb.[CloudStorageOptions_RANDOM_START](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CloudStorageOptions_SAMPLE_METHOD_UNSPECIFIED_CloudStorageOptions_TOP_CloudStorageOptions_RANDOM_START),
    	}
    
    	var storageConfig = &dlppb.StorageConfig{
    		Type: &dlppb.StorageConfig_CloudStorageOptions{
    			CloudStorageOptions: cloudStorageOptions,
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	// Specify how the content should be inspected.
    	var inspectConfig = &dlppb.InspectConfig{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: "PERSON_NAME"},
    		},
    		ExcludeInfoTypes: true,
    		IncludeQuote:     true,
    		MinLikelihood:    dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    	}
    
    	// Create a PubSub Client used to listen for when the inspect job finishes.
    	pubsubClient, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return err
    	}
    	defer pubsubClient.Close()
    
    	// Create a PubSub subscription we can use to listen for messages.
    	// Create the Topic if it doesn't exist.
    	t := pubsubClient.Topic(topicID)
    	if exists, err := t.Exists(ctx); err != nil {
    		return err
    	} else if !exists {
    		if t, err = pubsubClient.CreateTopic(ctx, topicID); err != nil {
    			return err
    		}
    	}
    
    	// Create the Subscription if it doesn't exist.
    	s := pubsubClient.Subscription(subscriptionId)
    	if exists, err := s.Exists(ctx); err != nil {
    		return err
    	} else if !exists {
    		if s, err = pubsubClient.CreateSubscription(ctx, subscriptionId, pubsub.SubscriptionConfig{Topic: t}); err != nil {
    			return err
    		}
    	}
    
    	// topic is the PubSub topic string where messages should be sent.
    	topic := "projects/" + projectID + "/topics/" + topicID
    
    	var action = &dlppb.Action{
    		Action: &dlppb.Action_PubSub{
    			PubSub: &dlppb.Action_PublishToPubSub{
    				Topic: topic,
    			},
    		},
    	}
    
    	// Configure the long running job we want the service to perform.
    	var inspectJobConfig = &dlppb.InspectJobConfig{
    		StorageConfig: storageConfig,
    		InspectConfig: inspectConfig,
    		Actions: []*dlppb.Action{
    			action,
    		},
    	}
    
    	// Create the request for the job configured above.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: inspectJobConfig,
    		},
    	}
    
    	// Use the client to send the request.
    	j, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "Job Created: %v", j.GetName())
    
    	// Wait for the inspect job to finish by waiting for a PubSub message.
    	// This only waits for 10 minutes. For long jobs, consider using a truly
    	// asynchronous execution model such as Cloud Functions.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Minute)
    	defer cancel()
    	err = s.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    		// If this is the wrong job, do not process the result.
    		if msg.Attributes["DlpJobName"] != j.GetName() {
    			msg.Nack()
    			return
    		}
    		msg.Ack()
    
    		// Stop listening for more messages.
    		defer cancel()
    
    		resp, err := client.GetDlpJob(ctx, &dlppb.GetDlpJobRequest{
    			Name: j.GetName(),
    		})
    		if err != nil {
    			fmt.Fprintf(w, "Error getting completed job: %v\n", err)
    			return
    		}
    		r := resp.GetInspectDetails().GetResult().GetInfoTypeStats()
    		if len(r) == 0 {
    			fmt.Fprintf(w, "No results")
    			return
    		}
    		for _, s := range r {
    			fmt.Fprintf(w, "\nFound %v instances of infoType %v\n", s.GetCount(), s.GetInfoType().GetName())
    		}
    	})
    	if err != nil {
    		return err
    	}
    	return nil
    
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html);
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).[FileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.FileSet.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).SampleMethod;
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class InspectGcsFileWithSampling {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String gcsUri = "gs://" + "your-bucket-name" + "/path/to/your/file.txt";
        String topicId = "your-pubsub-topic-id";
        String subscriptionId = "your-pubsub-subscription-id";
        inspectGcsFileWithSampling(projectId, gcsUri, topicId, subscriptionId);
      }
    
      // Inspects a file in a Google Cloud Storage Bucket.
      public static void inspectGcsFileWithSampling(
          String projectId, String gcsUri, String topicId, String subscriptionId)
          throws ExecutionException, InterruptedException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the GCS file to be inspected and sampling configuration
          [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html) cloudStorageOptions =
              [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).newBuilder()
                  .[setFileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_setFileSet_com_google_privacy_dlp_v2_CloudStorageOptions_FileSet_)([FileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.FileSet.html).newBuilder().setUrl(gcsUri))
                  .[setBytesLimitPerFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_setBytesLimitPerFile_long_)(200)
                  .[addFileTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_addFileTypes_com_google_privacy_dlp_v2_FileType_)([FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType.html).TEXT_FILE)
                  .[setFilesLimitPercent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_setFilesLimitPercent_int_)(90)
                  .setSampleMethod(SampleMethod.RANDOM_START)
                  .build();
    
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder().[setCloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setCloudStorageOptions_com_google_privacy_dlp_v2_CloudStorageOptions_)(cloudStorageOptions).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME").build();
    
          // Specify how the content should be inspected.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addInfoTypes(infoType)
                  .setExcludeInfoTypes(true)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .setMinLikelihood([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).POSSIBLE)
                  .build();
    
          // Specify the action that is triggered when the job completes.
          String pubSubTopic = String.format("projects/%s/topics/%s", projectId, topicId);
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishToPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishToPubSub.html) publishToPubSub =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).PublishToPubSub.newBuilder().setTopic(pubSubTopic).build();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPubSub_com_google_privacy_dlp_v2_Action_PublishToPubSub_)(publishToPubSub).build();
    
          // Configure the long running job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .setInspectConfig(inspectConfig)
                  .addActions(action)
                  .build();
    
          // Create the request for the job configured above.
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Use the client to send the request.
          final [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) dlpJob = dlp.createDlpJob(createDlpJobRequest);
          System.out.println("Job created: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
          // Set up a Pub/Sub subscriber to listen on the job completion status
          final SettableApiFuture<Boolean> done = [SettableApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html).create();
    
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) messageHandler =
              (PubsubMessage pubsubMessage, AckReplyConsumer ackReplyConsumer) -> {
                handleMessage(dlpJob, done, pubsubMessage, ackReplyConsumer);
              };
          [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, messageHandler).build();
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)();
    
          // Wait for job completion semi-synchronously
          // For long jobs, consider using a truly asynchronous execution model such as Cloud Functions
          try {
            done.get(15, TimeUnit.MINUTES);
          } catch (TimeoutException e) {
            System.out.println("Job was not completed after 15 minutes.");
            return;
          } finally {
            subscriber.stopAsync();
            subscriber.awaitTerminated();
          }
    
          // Get the latest state of the job from the service
          [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html) request = [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html).newBuilder().setName(dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)()).build();
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) completedJob = dlp.getDlpJob(request);
    
          // Parse the response and process results.
          System.out.println("Job status: " + completedJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) result = completedJob.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : result.getInfoTypeStatsList()) {
            System.out.print("\tInfo type: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount());
          }
        }
      }
    
      // handleMessage injects the job and settableFuture into the message reciever interface
      private static void handleMessage(
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) job,
          SettableApiFuture<Boolean> done,
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage,
          [AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html) ackReplyConsumer) {
        String messageAttribute = pubsubMessage.[getAttributesMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html#com_google_pubsub_v1_PubsubMessage_getAttributesMap__)().get("DlpJobName");
        if (job.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)().equals(messageAttribute)) {
          done.set(true);
          [ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)ReplyConsumer.[ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)();
        } else {
          ackReplyConsumer.[nack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_nack__)();
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client libraries
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Instantiates clients
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The gcs file path
    // const gcsUri = 'gs://" + "your-bucket-name" + "/path/to/your/file.txt';
    
    // Specify the type of info the inspection will look for.
    // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    // const infoTypes = [{ name: 'PERSON_NAME' }];
    
    // The name of the Pub/Sub topic to notify once the job completes
    // TODO(developer): create a Pub/Sub topic to use for this
    // const topicId = 'MY-PUBSUB-TOPIC'
    
    // The name of the Pub/Sub subscription to use when listening for job
    // completion notifications
    // TODO(developer): create a Pub/Sub subscription to use for this
    // const subscriptionId = 'MY-PUBSUB-SUBSCRIPTION'
    
    // DLP Job max time (in milliseconds)
    const DLP_JOB_WAIT_TIME = 15 * 1000 * 60;
    
    async function inspectGcsFileSampling() {
      // Specify the GCS file to be inspected and sampling configuration
      const storageItemConfig = {
        cloudStorageOptions: {
          fileSet: {url: gcsUri},
          bytesLimitPerFile: 200,
          filesLimitPercent: 90,
          fileTypes: [DLP.protos.google.privacy.dlp.v2.[FileType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.filetype.html).[TEXT_FILE](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.filetype.html)],
          sampleMethod:
            DLP.protos.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.cloudstorageoptions-class.html).SampleMethod
              .RANDOM_START,
        },
      };
    
      // Specify how the content should be inspected.
      const inspectConfig = {
        infoTypes: infoTypes,
        minLikelihood: DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[POSSIBLE](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        includeQuote: true,
        excludeInfoTypes: true,
      };
    
      // Specify the action that is triggered when the job completes.
      const actions = [
        {
          pubSub: {
            topic: `projects/${projectId}/topics/${topicId}`,
          },
        },
      ];
    
      // Create the request for the job configured above.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: {
          inspectConfig: inspectConfig,
          storageConfig: storageItemConfig,
          actions: actions,
        },
      };
    
      // Use the client to send the request.
      const [topicResponse] = await pubsub.topic(topicId).get();
    
      // Verify the Pub/Sub topic and listen for job notifications via an
      // existing subscription.
      const subscription = await topicResponse.subscription(subscriptionId);
    
      const [jobsResponse] = await dlp.createDlpJob(request);
      const jobName = jobsResponse.name;
      // Watch the Pub/Sub topic until the DLP job finishes
      await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)((resolve, reject) => {
        // Set up the timeout
        const timer = setTimeout(() => {
          reject(new Error('Timeout'));
        }, DLP_JOB_WAIT_TIME);
    
        const messageHandler = message => {
          if (message.attributes && message.attributes.DlpJobName === jobName) {
            message.ack();
            subscription.removeListener('message', messageHandler);
            subscription.removeListener('error', errorHandler);
            clearTimeout(timer);
            resolve(jobName);
          } else {
            message.nack();
          }
        };
    
        const errorHandler = err => {
          subscription.removeListener('message', messageHandler);
          subscription.removeListener('error', errorHandler);
          clearTimeout(timer);
          reject(err);
        };
    
        subscription.on('message', messageHandler);
        subscription.on('error', errorHandler);
      });
      const [job] = await dlp.getDlpJob({name: jobName});
      console.log(`Job ${job.name} status: ${job.state}`);
    
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.[length](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html) > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `  Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    
    await inspectGcsFileSampling();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishToPubSub;
    use Google\Cloud\Dlp\V2\BigQueryOptions\SampleMethod;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CloudStorageOptions;
    use Google\Cloud\Dlp\V2\CloudStorageOptions\FileSet;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\StorageConfig;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Inspect storage with sampling.
     * The following examples demonstrate using the Cloud DLP API to scan a 90% subset of a
     * Cloud Storage bucket for person names. The scan starts from a random location in the dataset
     * and only includes text files under 200 bytes.
     *
     * @param string $callingProjectId  The project ID to run the API call under.
     * @param string $gcsUri            Google Cloud Storage file url.
     * @param string $topicId           The ID of the Pub/Sub topic to notify once the job completes.
     * @param string $subscriptionId    The ID of the Pub/Sub subscription to use when listening for job.
     */
    function inspect_gcs_with_sampling(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $gcsUri = 'gs://GOOGLE_STORAGE_BUCKET_NAME/dlp_sample.csv',
        string $topicId = 'dlp-pubsub-topic',
        string $subscriptionId = 'dlp_subcription'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
        $pubsub = new PubSubClient();
        $topic = $pubsub->topic($topicId);
    
        // Construct the items to be inspected.
        $cloudStorageOptions = (new CloudStorageOptions())
            ->setFileSet((new FileSet())
                ->setUrl($gcsUri))
            ->setBytesLimitPerFile(200)
            ->setFilesLimitPercent(90)
            ->setSampleMethod(SampleMethod::RANDOM_START);
    
        $storageConfig = (new StorageConfig())
            ->setCloudStorageOptions($cloudStorageOptions);
    
        // Specify the type of info the inspection will look for.
        $phoneNumberInfoType = (new InfoType())
            ->setName('PHONE_NUMBER');
        $emailAddressInfoType = (new InfoType())
            ->setName('EMAIL_ADDRESS');
        $cardNumberInfoType = (new InfoType())
            ->setName('CREDIT_CARD_NUMBER');
        $infoTypes = [$phoneNumberInfoType, $emailAddressInfoType, $cardNumberInfoType];
    
        // Specify how the content should be inspected.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infoTypes)
            ->setIncludeQuote(true);
    
        // Construct the action to run when job completes.
        $action = (new Action())
            ->setPubSub((new PublishToPubSub())
                ->setTopic($topic->name()));
    
        // Construct inspect job config to run.
        $inspectJob = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Listen for job notifications via an existing topic/subscription.
        $subscription = $topic->subscription($subscriptionId);
    
        // Submit request.
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJob);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        // Poll Pub/Sub using exponential backoff until job finishes.
        // Consider using an asynchronous execution model such as Cloud Functions.
        $attempt = 1;
        $startTime = time();
        do {
            foreach ($subscription->pull() as $message) {
                if (
                    isset($message->attributes()['DlpJobName']) &&
                    $message->attributes()['DlpJobName'] === $job->getName()
                ) {
                    $subscription->acknowledge($message);
                    // Get the updated job. Loop to avoid race condition with DLP API.
                    do {
                        $getDlpJobRequest = (new GetDlpJobRequest())
                            ->setName($job->getName());
                        $job = $dlp->getDlpJob($getDlpJobRequest);
                    } while ($job->getState() == JobState::RUNNING);
                    break 2; // break from parent do while.
                }
            }
            printf('Waiting for job to complete' . PHP_EOL);
            // Exponential backoff with max delay of 60 seconds.
            sleep(min(60, pow(2, ++$attempt)));
        } while (time() - $startTime < 600); // 10 minute timeout.
    
        // Print finding counts.
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    printf('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf(
                            '  Found %s instance(s) of infoType %s' . PHP_EOL,
                            $infoTypeStat->getCount(),
                            $infoTypeStat->getInfoType()->getName()
                        );
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                printf('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                printf('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import threading
    from typing import List
    
    import google.cloud.dlp
    import google.cloud.pubsub
    
    
    def inspect_gcs_with_sampling(
        project: str,
        bucket: str,
        topic_id: str,
        subscription_id: str,
        info_types: List[str] = None,
        file_types: List[str] = None,
        min_likelihood: str = None,
        max_findings: int = None,
        timeout: int = 300,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze files in GCS by
        limiting the amount of data to be scanned.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            bucket: The name of the GCS bucket containing the file, as a string.
            topic_id: The id of the Cloud Pub/Sub topic to which the API will
                broadcast job completion. The topic must already exist.
            subscription_id: The id of the Cloud Pub/Sub subscription to listen on
                while waiting for job completion. The subscription must already
                exist and be subscribed to the topic.
            info_types: A list of strings representing infoTypes to look for.
                A full list of info type categories can be fetched from the API.
            file_types: Type of files in gcs bucket where the inspection would happen.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            timeout: The number of seconds to wait for a response from the API.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries.
        if not info_types:
            info_types = ["FIRST_NAME", "LAST_NAME", "EMAIL_ADDRESS"]
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Specify how the content should be inspected. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": info_types,
            "exclude_info_types": True,
            "include_quote": True,
            "min_likelihood": min_likelihood,
            "limits": {"max_findings_per_request": max_findings},
        }
    
        # Setting default file types as CSV files
        if not file_types:
            file_types = ["CSV"]
    
        # Construct a cloud_storage_options dictionary with the bucket's URL.
        url = f"gs://{bucket}/*"
        storage_config = {
            "cloud_storage_options": {
                "file_set": {"url": url},
                "bytes_limit_per_file": 200,
                "file_types": file_types,
                "files_limit_percent": 90,
                "sample_method": "RANDOM_START",
            }
        }
    
        # Tell the API where to send a notification when the job is complete.
        topic = google.cloud.pubsub.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html).topic_path(project, topic_id)
        actions = [{"pub_sub": {"topic": topic}}]
    
        # Construct the inspect_job, which defines the entire inspect content task.
        inspect_job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
        # Convert the project id into full resource ids.
        parent = f"projects/{project}/locations/global"
    
        # Call the API
        operation = dlp.create_dlp_job(
            request={"parent": parent, "inspect_job": inspect_job}
        )
        print(f"Inspection operation started: {operation.name}")
    
        # Create a Pub/Sub client and find the subscription. The subscription is
        # expected to already be listening to the topic.
        subscriber = google.cloud.pubsub.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
        subscription_path = subscriber.subscription_path(project, subscription_id)
    
        # Set up a callback to acknowledge a message. This closes around an event
        # so that it can signal that it is done and the main thread can continue.
        job_done = threading.Event()
    
        def callback(message):
            try:
                if message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes)["DlpJobName"] == operation.name:
                    # This is the message we're looking for, so acknowledge it.
                    message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
                    # Now that the job is done, fetch the results and print them.
                    job = dlp.get_dlp_job(request={"name": operation.name})
                    print(f"Job name: {job.name}")
                    if job.inspect_details.result.info_type_stats:
                        print("Findings:")
                        for finding in job.inspect_details.result.info_type_stats:
                            print(
                                f"Info type: {finding.info_type.name}; Count: {finding.count}"
                            )
                    else:
                        print("No findings.")
    
                    # Signal to the main thread that we can exit.
                    job_done.set()
                else:
                    # This is not the message we're looking for.
                    message.[drop](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_drop)()
            except Exception as e:
                # Because this is executing in a thread, an exception won't be
                # noted unless we print it manually.
                print(e)
                raise
    
        # Register the callback and wait on the event.
        [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
        finished = job_done.wait(timeout=timeout)
        if not finished:
            print(
                "No event received before the timeout. Please verify that the "
                "subscription provided is subscribed to the topic provided."
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
