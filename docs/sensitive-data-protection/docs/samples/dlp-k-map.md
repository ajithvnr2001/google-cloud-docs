---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-k-map/
title: Computing k-map estimates \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:12.462132+00:00
---

# Computing k-map estimates  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-k-map/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Computing k-map estimates Stay organized with collections  Save and categorize content based on your preferences. 

You can estimate k-map values using Cloud DLP, which uses a statistical model to estimate a re-identification dataset.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Computing k-map for a dataset](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-map)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using Newtonsoft.Json;
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading;
    using System.Threading.Tasks;
    using static Google.Cloud.Dlp.V2.Action.Types;
    using static Google.Cloud.Dlp.V2.PrivacyMetric.Types;
    using static Google.Cloud.Dlp.V2.PrivacyMetric.Types.KMapEstimationConfig.Types;
    
    public class RiskAnalysisCreateKMap
    {
        public static object KMap(
            string callingProjectId,
            string tableProjectId,
            string datasetId,
            string tableId,
            string topicId,
            string subscriptionId,
            IEnumerable<FieldId> quasiIds,
            IEnumerable<InfoType> infoTypes,
            string regionCode)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct + submit the job
            var kmapEstimationConfig = new KMapEstimationConfig
            {
                QuasiIds =
                    {
                        quasiIds.Zip(
                            infoTypes,
                            (Field, InfoType) => new [TaggedField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.KMapEstimationConfig.Types.TaggedField.html)
                            {
                                Field = Field,
                                InfoType = InfoType
                            }
                        )
                    },
                RegionCode = regionCode
            };
    
            var config = new [RiskAnalysisJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RiskAnalysisJobConfig.html)()
            {
                PrivacyMetric = new [PrivacyMetric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.html)
                {
                    KMapEstimationConfig = kmapEstimationConfig
                },
                SourceTable = new [BigQueryTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTable.html)
                {
                    ProjectId = tableProjectId,
                    DatasetId = datasetId,
                    TableId = tableId
                },
                Actions =
                {
                    new Google.Cloud.Dlp.V2.Action
                    {
                        PubSub = new [PublishToPubSub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types.PublishToPubSub.html)
                        {
                            Topic = $"projects/{callingProjectId}/topics/{topicId}"
                        }
                    }
                }
            };
    
            var submittedJob = dlp.CreateDlpJob(
                new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
                {
                    ParentAsProjectName = new [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)(callingProjectId),
                    RiskJob = config
                });
    
            // Listen to pub/sub for the job
            var subscriptionName = new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html)(
                callingProjectId,
                subscriptionId);
            var subscriber = [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_CreateAsync_Google_Cloud_PubSub_V1_SubscriptionName_)(
                subscriptionName).Result;
    
            // SimpleSubscriber runs your message handle function on multiple
            // threads to maximize throughput.
            var done = new ManualResetEventSlim(false);
            subscriber.StartAsync(([PubsubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html) message, CancellationToken cancel) =>
            {
                if (message.Attributes["DlpJobName"] == submittedJob.Name)
                {
                    Thread.Sleep(500); // Wait for DLP API results to become consistent
                    done.Set();
                    return Task.FromResult([SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Ack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Ack));
                }
                else
                {
                    return Task.FromResult([SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Nack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Nack));
                }
            });
    
            done.Wait(TimeSpan.FromMinutes(10)); // 10 minute timeout; may not work for large jobs
            subscriber.StopAsync(CancellationToken.None).Wait();
    
            // Process results
            var resultJob = dlp.GetDlpJob(new [GetDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDlpJobRequest.html)
            {
                DlpJobName = [DlpJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html).[Parse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html#Google_Cloud_Dlp_V2_DlpJobName_Parse_System_String_)(submittedJob.Name)
            });
    
            var result = resultJob.RiskDetails.KMapEstimationResult;
    
            for (var histogramIdx = 0; histogramIdx < result.KMapEstimationHistogram.Count; histogramIdx++)
            {
                var histogramValue = result.[KMapEstimationHistogram](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.html#Google_Cloud_Dlp_V2_AnalyzeDataSourceRiskDetails_Types_KMapEstimationResult_KMapEstimationHistogram)[histogramIdx];
                Console.WriteLine($"Bucket {histogramIdx}");
                Console.WriteLine($"  Anonymity range: [{histogramValue.[MinAnonymity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket.html#Google_Cloud_Dlp_V2_AnalyzeDataSourceRiskDetails_Types_KMapEstimationResult_Types_KMapEstimationHistogramBucket_MinAnonymity)}, {histogramValue.[MaxAnonymity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket.html#Google_Cloud_Dlp_V2_AnalyzeDataSourceRiskDetails_Types_KMapEstimationResult_Types_KMapEstimationHistogramBucket_MaxAnonymity)}].");
                Console.WriteLine($"  Size: {histogramValue.BucketSize}");
    
                foreach (var datapoint in histogramValue.BucketValues)
                {
                    // 'UnpackValue(x)' is a prettier version of 'x.toString()'
                    Console.WriteLine($"    Values: [{String.Join(',', datapoint.QuasiIdsValues.Select(x => UnpackValue(x)))}]");
                    Console.WriteLine($"    Estimated k-map anonymity: {datapoint.[EstimatedAnonymity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationQuasiIdValues.html#Google_Cloud_Dlp_V2_AnalyzeDataSourceRiskDetails_Types_KMapEstimationResult_Types_KMapEstimationQuasiIdValues_EstimatedAnonymity)}");
                }
            }
    
            return 0;
        }
    
        public static string UnpackValue([Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) protoValue)
        {
            var jsonValue = JsonConvert.DeserializeObject<Dictionary<string, object>>(protoValue.ToString());
            return jsonValue.Values.ElementAt(0).ToString();
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strings"
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    	"cloud.google.com/go/pubsub"
    	"github.com/golang/protobuf/ptypes/empty"
    )
    
    // riskKMap runs K Map on the given data.
    func riskKMap(w io.Writer, projectID, dataProject, pubSubTopic, pubSubSub, datasetID, tableID, region string, columnNames ...string) error {
    	// projectID := "my-project-id"
    	// dataProject := "bigquery-public-data"
    	// pubSubTopic := "dlp-risk-sample-topic"
    	// pubSubSub := "dlp-risk-sample-sub"
    	// datasetID := "san_francisco"
    	// tableID := "bikeshare_trips"
    	// region := "US"
    	// columnNames := "zip_code"
    	ctx := context.Background()
    	client, err := dlp.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    
    	// Create a PubSub Client used to listen for when the inspect job finishes.
    	pubsubClient, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return err
    	}
    	defer pubsubClient.Close()
    
    	// Create a PubSub subscription we can use to listen for messages.
    	// Create the Topic if it doesn't exist.
    	t := pubsubClient.Topic(pubSubTopic)
    	topicExists, err := t.Exists(ctx)
    	if err != nil {
    		return err
    	}
    	if !topicExists {
    		if t, err = pubsubClient.CreateTopic(ctx, pubSubTopic); err != nil {
    			return err
    		}
    	}
    
    	// Create the Subscription if it doesn't exist.
    	s := pubsubClient.Subscription(pubSubSub)
    	subExists, err := s.Exists(ctx)
    	if err != nil {
    		return err
    	}
    	if !subExists {
    		if s, err = pubsubClient.CreateSubscription(ctx, pubSubSub, pubsub.SubscriptionConfig{Topic: t}); err != nil {
    			return err
    		}
    	}
    
    	// topic is the PubSub topic string where messages should be sent.
    	topic := "projects/" + projectID + "/topics/" + pubSubTopic
    
    	// Build the QuasiID slice.
    	var q []*dlppb.PrivacyMetric_KMapEstimationConfig_TaggedField
    	for _, c := range columnNames {
    		q = append(q, &dlppb.PrivacyMetric_KMapEstimationConfig_TaggedField{
    			Field: &dlppb.FieldId{
    				Name: c,
    			},
    			Tag: &dlppb.PrivacyMetric_KMapEstimationConfig_TaggedField_Inferred{
    				Inferred: &empty.Empty{},
    			},
    		})
    	}
    
    	// Create a configured request.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_RiskJob{
    			RiskJob: &dlppb.RiskAnalysisJobConfig{
    				// PrivacyMetric configures what to compute.
    				PrivacyMetric: &dlppb.PrivacyMetric{
    					Type: &dlppb.PrivacyMetric_KMapEstimationConfig_{
    						KMapEstimationConfig: &dlppb.PrivacyMetric_KMapEstimationConfig{
    							QuasiIds:   q,
    							RegionCode: region,
    						},
    					},
    				},
    				// SourceTable describes where to find the data.
    				SourceTable: &dlppb.BigQueryTable{
    					ProjectId: dataProject,
    					DatasetId: datasetID,
    					TableId:   tableID,
    				},
    				// Send a message to PubSub using Actions.
    				Actions: []*dlppb.Action{
    					{
    						Action: &dlppb.Action_PubSub{
    							PubSub: &dlppb.Action_PublishToPubSub{
    								Topic: topic,
    							},
    						},
    					},
    				},
    			},
    		},
    	}
    	// Create the risk job.
    	j, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateDlpJob: %w", err)
    	}
    	fmt.Fprintf(w, "Created job: %v\n", j.GetName())
    	// Wait for the risk job to finish by waiting for a PubSub message.
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
    		time.Sleep(500 * time.Millisecond)
    		j, err := client.GetDlpJob(ctx, &dlppb.GetDlpJobRequest{
    			Name: j.GetName(),
    		})
    
    		if err != nil {
    			fmt.Fprintf(w, "GetDlpJob: %v", err)
    			return
    		}
    		h := j.GetRiskDetails().GetKMapEstimationResult().GetKMapEstimationHistogram()
    		for i, b := range h {
    			fmt.Fprintf(w, "Histogram bucket %v\n", i)
    			fmt.Fprintf(w, "  Anonymity range: [%v,%v]\n", b.GetMaxAnonymity(), b.GetMaxAnonymity())
    			fmt.Fprintf(w, "  %v unique values total\n", b.GetBucketSize())
    			for _, v := range b.GetBucketValues() {
    				var qvs []string
    				for _, qv := range v.GetQuasiIdsValues() {
    					qvs = append(qvs, qv.String())
    				}
    				fmt.Fprintf(w, "    QuasiID values: %s\n", strings.Join(qvs, ", "))
    				fmt.Fprintf(w, "    Estimated anonymity: %v\n", v.GetEstimatedAnonymity())
    			}
    		}
    		// Stop listening for more messages.
    		cancel()
    	})
    	if err != nil {
    		return fmt.Errorf("Recieve: %w", err)
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
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishToPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishToPubSub.html);
    import com.google.privacy.dlp.v2.[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.html).[KMapEstimationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.html);
    import com.google.privacy.dlp.v2.[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.html).[KMapEstimationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.html).[KMapEstimationHistogramBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationHistogramBucket.html);
    import com.google.privacy.dlp.v2.[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.html).[KMapEstimationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.html).[KMapEstimationQuasiIdValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationQuasiIdValues.html);
    import com.google.privacy.dlp.v2.[BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html);
    import com.google.privacy.dlp.v2.[PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html).[KMapEstimationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.html);
    import com.google.privacy.dlp.v2.[PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html).[KMapEstimationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.html).[TaggedField](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.TaggedField.html);
    import com.google.privacy.dlp.v2.[RiskAnalysisJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RiskAnalysisJobConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import java.util.stream.Collectors;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    class RiskAnalysisKMap {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String datasetId = "your-bigquery-dataset-id";
        String tableId = "your-bigquery-table-id";
        String topicId = "pub-sub-topic";
        String subscriptionId = "pub-sub-subscription";
        calculateKMap(projectId, datasetId, tableId, topicId, subscriptionId);
      }
    
      public static void calculateKMap(
          String projectId, String datasetId, String tableId, String topicId, String subscriptionId)
          throws ExecutionException, InterruptedException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the BigQuery table to analyze
          [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html) bigQueryTable =
              [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html).newBuilder()
                  .setProjectId(projectId)
                  .setDatasetId(datasetId)
                  .setTableId(tableId)
                  .build();
    
          // These values represent the column names of quasi-identifiers to analyze
          List<String> quasiIds = Arrays.asList("Age", "Gender");
    
          // These values represent the info types corresponding to the quasi-identifiers above
          List<String> infoTypeNames = Arrays.asList("AGE", "GENDER");
    
          // Tag each of the quasiId column names with its corresponding infoType
          List<InfoType> infoTypes =
              infoTypeNames.stream()
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          if (quasiIds.size() != infoTypes.size()) {
            throw new IllegalArgumentException("The numbers of quasi-IDs and infoTypes must be equal!");
          }
    
          List<TaggedField> taggedFields = new ArrayList<TaggedField>();
          for (int i = 0; i < quasiIds.size(); i++) {
            [TaggedField](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.TaggedField.html) taggedField =
                [TaggedField](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.TaggedField.html).newBuilder()
                    .setField([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName(quasiIds.get(i)).build())
                    .setInfoType(infoTypes.get(i))
                    .build();
            taggedFields.add(taggedField);
          }
    
          // The k-map distribution region can be specified by any ISO-3166-1 region code.
          String regionCode = "US";
    
          // Configure the privacy metric for the job
          [KMapEstimationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.html) kmapConfig =
              [KMapEstimationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.html).newBuilder()
                  .addAllQuasiIds(taggedFields)
                  .setRegionCode(regionCode)
                  .build();
          [PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html) privacyMetric =
              [PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html).newBuilder().[setKMapEstimationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.Builder.html#com_google_privacy_dlp_v2_PrivacyMetric_Builder_setKMapEstimationConfig_com_google_privacy_dlp_v2_PrivacyMetric_KMapEstimationConfig_)(kmapConfig).build();
    
          // Create action to publish job status notifications over Google Cloud Pub/Sub
          [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html) topicName = [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html).of(projectId, topicId);
          [PublishToPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishToPubSub.html) publishToPubSub =
              [PublishToPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishToPubSub.html).newBuilder().setTopic(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html#com_google_pubsub_v1_ProjectTopicName_toString__)()).build();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPubSub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPubSub_com_google_privacy_dlp_v2_Action_PublishToPubSub_)(publishToPubSub).build();
    
          // Configure the risk analysis job to perform
          [RiskAnalysisJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RiskAnalysisJobConfig.html) riskAnalysisJobConfig =
              [RiskAnalysisJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RiskAnalysisJobConfig.html).newBuilder()
                  .[setSourceTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RiskAnalysisJobConfig.Builder.html#com_google_privacy_dlp_v2_RiskAnalysisJobConfig_Builder_setSourceTable_com_google_privacy_dlp_v2_BigQueryTable_)(bigQueryTable)
                  .[setPrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RiskAnalysisJobConfig.Builder.html#com_google_privacy_dlp_v2_RiskAnalysisJobConfig_Builder_setPrivacyMetric_com_google_privacy_dlp_v2_PrivacyMetric_)(privacyMetric)
                  .addActions(action)
                  .build();
    
          // Build the request to be sent by the client
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .[setRiskJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.Builder.html#com_google_privacy_dlp_v2_CreateDlpJobRequest_Builder_setRiskJob_com_google_privacy_dlp_v2_RiskAnalysisJobConfig_)(riskAnalysisJobConfig)
                  .build();
    
          // Send the request to the API using the client
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) dlpJob = dlpServiceClient.createDlpJob(createDlpJobRequest);
    
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
    
          // Build a request to get the completed job
          [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html) getDlpJobRequest =
              [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html).newBuilder().setName(dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)()).build();
    
          // Retrieve completed job status
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) completedJob = dlpServiceClient.getDlpJob(getDlpJobRequest);
          System.out.println("Job status: " + completedJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
          // Get the result and parse through and process the information
          [KMapEstimationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.html) kmapResult = completedJob.[getRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getRiskDetails__)().getKMapEstimationResult();
    
          for ([KMapEstimationHistogramBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationHistogramBucket.html) result : kmapResult.getKMapEstimationHistogramList()) {
            System.out.printf(
                "\tAnonymity range: [%d, %d]\n", result.getMinAnonymity(), result.getMaxAnonymity());
            System.out.printf("\tSize: %d\n", result.getBucketSize());
    
            for ([KMapEstimationQuasiIdValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationQuasiIdValues.html) valueBucket : result.getBucketValuesList()) {
              List<String> quasiIdValues =
                  valueBucket.getQuasiIdsValuesList().stream()
                      .map(
                          value -> {
                            String s = value.toString();
                            return s.substring(s.indexOf(':') + 1).trim();
                          })
                      .collect(Collectors.toList());
    
              System.out.printf("\tValues: {%s}\n", String.join(", ", quasiIdValues));
              System.out.printf(
                  "\tEstimated k-map anonymity: %d\n", valueBucket.getEstimatedAnonymity());
            }
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
    
    // The project ID the table is stored under
    // This may or (for public datasets) may not equal the calling project ID
    // const tableProjectId = 'my-project';
    
    // The ID of the dataset to inspect, e.g. 'my_dataset'
    // const datasetId = 'my_dataset';
    
    // The ID of the table to inspect, e.g. 'my_table'
    // const tableId = 'my_table';
    
    // The name of the Pub/Sub topic to notify once the job completes
    // TODO(developer): create a Pub/Sub topic to use for this
    // const topicId = 'MY-PUBSUB-TOPIC'
    
    // The name of the Pub/Sub subscription to use when listening for job
    // completion notifications
    // TODO(developer): create a Pub/Sub subscription to use for this
    // const subscriptionId = 'MY-PUBSUB-SUBSCRIPTION'
    
    // The ISO 3166-1 region code that the data is representative of
    // Can be omitted if using a region-specific infoType (such as US_ZIP_5)
    // const regionCode = 'USA';
    
    // A set of columns that form a composite key ('quasi-identifiers'), and
    // optionally their reidentification distributions
    // const quasiIds = [{ field: { name: 'age' }, infoType: { name: 'AGE' }}];
    async function kMapEstimationAnalysis() {
      const sourceTable = {
        projectId: tableProjectId,
        datasetId: datasetId,
        tableId: tableId,
      };
    
      // Construct request for creating a risk analysis job
      const request = {
        parent: `projects/${projectId}/locations/global`,
        riskJob: {
          privacyMetric: {
            kMapEstimationConfig: {
              quasiIds: quasiIds,
              regionCode: regionCode,
            },
          },
          sourceTable: sourceTable,
          actions: [
            {
              pubSub: {
                topic: `projects/${projectId}/topics/${topicId}`,
              },
            },
          ],
        },
      };
      // Create helper function for unpacking values
      const getValue = obj => obj[Object.keys(obj)[0]];
    
      // Run risk analysis job
      const [topicResponse] = await pubsub.topic(topicId).get();
      const subscription = await topicResponse.subscription(subscriptionId);
      const [jobsResponse] = await dlp.createDlpJob(request);
      const jobName = jobsResponse.name;
      console.log(`Job created. Job name: ${jobName}`);
    
      // Watch the Pub/Sub topic until the DLP job finishes
      await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)((resolve, reject) => {
        const messageHandler = message => {
          if (message.attributes && message.attributes.DlpJobName === jobName) {
            message.ack();
            subscription.removeListener('message', messageHandler);
            subscription.removeListener('error', errorHandler);
            resolve(jobName);
          } else {
            message.nack();
          }
        };
    
        const errorHandler = err => {
          subscription.removeListener('message', messageHandler);
          subscription.removeListener('error', errorHandler);
          reject(err);
        };
    
        subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', messageHandler);
        subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('error', errorHandler);
      });
      setTimeout(() => {
        console.log(' Waiting for DLP job to fully complete');
      }, 500);
      const [job] = await dlp.getDlpJob({name: jobName});
    
      const histogramBuckets =
        job.riskDetails.kMapEstimationResult.kMapEstimationHistogram;
    
      histogramBuckets.forEach((histogramBucket, histogramBucketIdx) => {
        console.log(`Bucket ${histogramBucketIdx}:`);
        console.log(
          `  Anonymity range: [${histogramBucket.minAnonymity}, ${histogramBucket.maxAnonymity}]`
        );
        console.log(`  Size: ${histogramBucket.bucketSize}`);
        histogramBucket.bucketValues.forEach(valueBucket => {
          const values = valueBucket.quasiIdsValues.map(value => getValue(value));
          console.log(`    Values: ${values.join(' ')}`);
          console.log(
            `    Estimated k-map anonymity: ${valueBucket.estimatedAnonymity}`
          );
        });
      });
    }
    
    await kMapEstimationAnalysis();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Exception;
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishToPubSub;
    use Google\Cloud\Dlp\V2\BigQueryTable;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\PrivacyMetric;
    use Google\Cloud\Dlp\V2\PrivacyMetric\KMapEstimationConfig;
    use Google\Cloud\Dlp\V2\PrivacyMetric\KMapEstimationConfig\TaggedField;
    use Google\Cloud\Dlp\V2\RiskAnalysisJobConfig;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Computes the k-map risk estimation of a column set in a Google BigQuery table.
     *
     * @param string   $callingProjectId  The project ID to run the API call under
     * @param string   $dataProjectId     The project ID containing the target Datastore
     * @param string   $topicId           The name of the Pub/Sub topic to notify once the job completes
     * @param string   $subscriptionId    The name of the Pub/Sub subscription to use when listening for job
     * @param string   $datasetId         The ID of the dataset to inspect
     * @param string   $tableId           The ID of the table to inspect
     * @param string   $regionCode        The ISO 3166-1 region code that the data is representative of
     * @param string[] $quasiIdNames      Array columns that form a composite key (quasi-identifiers)
     * @param string[] $infoTypes         Array of infoTypes corresponding to the chosen quasi-identifiers
     */
    function k_map(
        string $callingProjectId,
        string $dataProjectId,
        string $topicId,
        string $subscriptionId,
        string $datasetId,
        string $tableId,
        string $regionCode,
        array $quasiIdNames,
        array $infoTypes
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
        $pubsub = new PubSubClient();
        $topic = $pubsub->topic($topicId);
    
        // Verify input
        if (count($infoTypes) != count($quasiIdNames)) {
            throw new Exception('Number of infoTypes and number of quasi-identifiers must be equal!');
        }
    
        // Map infoTypes to quasi-ids
        $quasiIdObjects = array_map(function ($quasiId, $infoType) {
            $quasiIdField = (new FieldId())
                ->setName($quasiId);
    
            $quasiIdType = (new InfoType())
                ->setName($infoType);
    
            $quasiIdObject = (new TaggedField())
                ->setInfoType($quasiIdType)
                ->setField($quasiIdField);
    
            return $quasiIdObject;
        }, $quasiIdNames, $infoTypes);
    
        // Construct analysis config
        $statsConfig = (new KMapEstimationConfig())
            ->setQuasiIds($quasiIdObjects)
            ->setRegionCode($regionCode);
    
        $privacyMetric = (new PrivacyMetric())
            ->setKMapEstimationConfig($statsConfig);
    
        // Construct items to be analyzed
        $bigqueryTable = (new BigQueryTable())
            ->setProjectId($dataProjectId)
            ->setDatasetId($datasetId)
            ->setTableId($tableId);
    
        // Construct the action to run when job completes
        $pubSubAction = (new PublishToPubSub())
            ->setTopic($topic->name());
    
        $action = (new Action())
            ->setPubSub($pubSubAction);
    
        // Construct risk analysis job config to run
        $riskJob = (new RiskAnalysisJobConfig())
            ->setPrivacyMetric($privacyMetric)
            ->setSourceTable($bigqueryTable)
            ->setActions([$action]);
    
        // Listen for job notifications via an existing topic/subscription.
        $subscription = $topic->subscription($subscriptionId);
    
        // Submit request
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setRiskJob($riskJob);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        // Poll Pub/Sub using exponential backoff until job finishes
        // Consider using an asynchronous execution model such as Cloud Functions
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
                    break 2; // break from parent do while
                }
            }
            print('Waiting for job to complete' . PHP_EOL);
            // Exponential backoff with max delay of 60 seconds
            sleep(min(60, pow(2, ++$attempt)));
        } while (time() - $startTime < 600); // 10 minute timeout
    
        // Print finding counts
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $histBuckets = $job->getRiskDetails()->getKMapEstimationResult()->getKMapEstimationHistogram();
    
                foreach ($histBuckets as $bucketIndex => $histBucket) {
                    // Print bucket stats
                    printf('Bucket %s:' . PHP_EOL, $bucketIndex);
                    printf(
                        '  Anonymity range: [%s, %s]' . PHP_EOL,
                        $histBucket->getMinAnonymity(),
                        $histBucket->getMaxAnonymity()
                    );
                    printf('  Size: %s' . PHP_EOL, $histBucket->getBucketSize());
    
                    // Print bucket values
                    foreach ($histBucket->getBucketValues() as $percent => $valueBucket) {
                        printf(
                            '  Estimated k-map anonymity: %s' . PHP_EOL,
                            $valueBucket->getEstimatedAnonymity()
                        );
    
                        // Pretty-print quasi-ID values
                        print('  Values: ' . PHP_EOL);
                        foreach ($valueBucket->getQuasiIdsValues() as $index => $value) {
                            print('    ' . $value->serializeToJsonString() . PHP_EOL);
                        }
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
                print('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                print('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import concurrent.futures
    from typing import List
    
    import google.cloud.dlp
    from google.cloud.dlp_v2 import types
    import google.cloud.pubsub
    
    
    def k_map_estimate_analysis(
        project: str,
        table_project_id: str,
        dataset_id: str,
        table_id: str,
        topic_id: str,
        subscription_id: str,
        quasi_ids: List[str],
        info_types: List[str],
        region_code: str = "US",
        timeout: int = 300,
    ) -> None:
        """Uses the Data Loss Prevention API to compute the k-map risk estimation
            of a column set in a Google BigQuery table.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            table_project_id: The Google Cloud project id where the BigQuery table
                is stored.
            dataset_id: The id of the dataset to inspect.
            table_id: The id of the table to inspect.
            topic_id: The name of the Pub/Sub topic to notify once the job
                completes.
            subscription_id: The name of the Pub/Sub subscription to use when
                listening for job completion notifications.
            quasi_ids: A set of columns that form a composite key and optionally
                their re-identification distributions.
            info_types: Type of information of the quasi_id in order to provide a
                statistical model of population.
            region_code: The ISO 3166-1 region code that the data is representative
                of. Can be omitted if using a region-specific infoType (such as
                US_ZIP_5)
            timeout: The number of seconds to wait for a response from the API.
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Create helper function for unpacking values
        def get_values(obj: types.[Value](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Value.html)) -> int:
            return int(obj.integer_value)
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into full resource ids.
        topic = google.cloud.pubsub.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html).topic_path(project, topic_id)
        parent = f"projects/{project}/locations/global"
    
        # Location info of the BigQuery table.
        source_table = {
            "project_id": table_project_id,
            "dataset_id": dataset_id,
            "table_id": table_id,
        }
    
        # Check that numbers of quasi-ids and info types are equal
        if len(quasi_ids) != len(info_types):
            raise ValueError(
                """Number of infoTypes and number of quasi-identifiers
                                must be equal!"""
            )
    
        # Convert quasi id list to Protobuf type
        def map_fields(quasi_id: str, info_type: str) -> dict:
            return {"field": {"name": quasi_id}, "info_type": {"name": info_type}}
    
        quasi_ids = map(map_fields, quasi_ids, info_types)
    
        # Tell the API where to send a notification when the job is complete.
        actions = [{"pub_sub": {"topic": topic}}]
    
        # Configure risk analysis job
        # Give the name of the numeric column to compute risk metrics for
        risk_job = {
            "privacy_metric": {
                "k_map_estimation_config": {
                    "quasi_ids": quasi_ids,
                    "region_code": region_code,
                }
            },
            "source_table": source_table,
            "actions": actions,
        }
    
        # Call API to start risk analysis job
        operation = dlp.create_dlp_job(request={"parent": parent, "risk_job": risk_job})
    
        def callback(message: google.cloud.pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
            if message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes)["DlpJobName"] == operation.name:
                # This is the message we're looking for, so acknowledge it.
                message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
                # Now that the job is done, fetch the results and print them.
                job = dlp.get_dlp_job(request={"name": operation.name})
                print(f"Job name: {job.name}")
                histogram_buckets = (
                    job.risk_details.k_map_estimation_result.k_map_estimation_histogram
                )
                # Print bucket stats
                for i, bucket in enumerate(histogram_buckets):
                    print(f"Bucket {i}:")
                    print(
                        "   Anonymity range: [{}, {}]".format(
                            bucket.min_anonymity, bucket.max_anonymity
                        )
                    )
                    print(f"   Size: {bucket.bucket_size}")
                    for value_bucket in bucket.bucket_values:
                        print(
                            "   Values: {}".format(
                                map(get_values, value_bucket.quasi_ids_values)
                            )
                        )
                        print(
                            "   Estimated k-map anonymity: {}".format(
                                value_bucket.estimated_anonymity
                            )
                        )
                subscription.set_result(None)
            else:
                # This is not the message we're looking for.
                message.[drop](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_drop)()
    
        # Create a Pub/Sub client and find the subscription. The subscription is
        # expected to already be listening to the topic.
        subscriber = google.cloud.pubsub.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
        subscription_path = subscriber.subscription_path(project, subscription_id)
        subscription = [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback)
    
        try:
            subscription.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            print(
                "No event received before the timeout. Please verify that the "
                "subscription provided is subscribed to the topic provided."
            )
            subscription.[close](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client.html#google_cloud_pubsub_v1_subscriber_client_Client_close)()
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
