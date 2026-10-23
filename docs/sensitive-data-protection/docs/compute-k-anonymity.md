---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-anonymity/
title: Computing k-anonymity for a dataset \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:15.072882+00:00
---

# Computing k-anonymity for a dataset  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-anonymity/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Computing k-anonymity for a dataset Stay organized with collections  Save and categorize content based on your preferences. 

[_K-anonymity_](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#about-k-anonymity) is a property of a dataset that indicates the re-identifiability of its records. A dataset is _k_ -anonymous if quasi-identifiers for each person in the dataset are identical to at least _k_ – 1 other people also in the dataset.

You can compute the _k_ -anonymity value based on one or more columns, or fields, of a dataset. This topic demonstrates how to compute _k_ -anonymity values for a dataset using Sensitive Data Protection. For more information about _k_ -anonymity or risk analysis in general, see the [risk analysis concept topic](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis) before continuing on.

**Note:** Prematurely canceling an operation midway through a job still incurs costs for the portion of the job that was completed. For more information about billing, see [Sensitive Data Protection pricing](https://cloud.google.com/sensitive-data-protection/pricing).

##  Before you begin 

Before continuing, be sure you've done the following: 

  1. [Sign in](https://accounts.google.com/Login) to your Google Account.
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
[Go to the project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
  3. Make sure that billing is enabled for your Google Cloud project. [Learn how to confirm billing is enabled for your project.](https://docs.cloud.google.com/billing/docs/how-to/modify-project)
  4. Enable Sensitive Data Protection.
[Enable Sensitive Data Protection](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)

  5. Select a BigQuery dataset to analyze. Sensitive Data Protection calculates the _k_ -anonymity metric by scanning a BigQuery table.
  6. Determine an identifier (if applicable) and at least one quasi-identifier in the dataset. For more information, see [Risk analysis terms and techniques](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#risk_analysis_terms_and_techniques).



## Compute k-anonymity

Sensitive Data Protection performs risk analysis whenever a risk analysis job runs. You must create the job first, either by using the Google Cloud console, sending a DLP API request, or using a Sensitive Data Protection client library.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### Console

  1. In the Google Cloud console, go to the **Create risk analysis** page.

[Go to Create risk analysis](https://console.cloud.google.com/security/sensitive-data-protection/create/riskAnalysisJob;source=7)

  2. In the **Choose input data** section, specify the BigQuery table to scan by entering the project ID of the project containing the table, the dataset ID of the table, and the name of the table.

  3. Under **Privacy metric to compute** , select **k-anonymity**.

  4. In the **Job ID** section, you can optionally give the job a custom identifier and select [a resource location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location) in which Sensitive Data Protection will process your data. When you're done, click **Continue**.

  5. In the **Define fields** section, you specify [identifiers and quasi-identifiers](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#risk_analysis_terms_and_techniques) for the _k_ -anonymity risk job. Sensitive Data Protection accesses the metadata of the BigQuery table you specified in the previous step and attempts to populate the list of fields.

     1. Select the appropriate checkbox to specify a field as either an identifier (ID) or quasi-identifier (QI). You must select either 0 or 1 identifiers and at least 1 quasi-identifier.
     2. If Sensitive Data Protection isn't able to populate the fields, click **Enter field name** to manually enter one or more fields and set each one as identifier or quasi-identifier. When you're done, click **Continue**.
  6. In the **Add actions** section, you can add optional [actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions) to perform when the risk job is complete. The available options are:

**Important:** Be aware that running a risk analysis job may persist some of the [quote](https://docs.cloud.google.com/sensitive-data-protection/docs/quote) values of the selected quasi-identifiers to the risk analysis job results. These quote values are used to build the histogram and output tables.
     * **Save to BigQuery** : Saves the results of the risk analysis scan to a BigQuery table.
     * **Publish to Pub/Sub** : Publishes a notification to a [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/publisher).

**Note:** If there are configuration or permission issues with the Pub/Sub topic, Sensitive Data Protection retries sending the Pub/Sub notification for up to two weeks. After two weeks, the notification is discarded. 
     * **Notify by email** : Sends you an email with results. When you're done, click **Create**.




The _k_ -anonymity risk analysis job starts immediately.

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
    
    public class RiskAnalysisCreateKAnonymity
    {
        public static AnalyzeDataSourceRiskDetails.Types.KAnonymityResult KAnonymity(
            string callingProjectId,
            string tableProjectId,
            string datasetId,
            string tableId,
            string topicId,
            string subscriptionId,
            IEnumerable<FieldId> quasiIds)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct + submit the job
            var KAnonymityConfig = new KAnonymityConfig
            {
                QuasiIds = { quasiIds }
            };
    
            var config = new [RiskAnalysisJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RiskAnalysisJobConfig.html)
            {
                PrivacyMetric = new [PrivacyMetric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.html)
                {
                    KAnonymityConfig = KAnonymityConfig
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
            var subscriptionName = new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html)(callingProjectId, subscriptionId);
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
    
            var result = resultJob.RiskDetails.KAnonymityResult;
    
            for (var bucketIdx = 0; bucketIdx < result.EquivalenceClassHistogramBuckets.Count; bucketIdx++)
            {
                var bucket = result.[EquivalenceClassHistogramBuckets](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KAnonymityResult.html#Google_Cloud_Dlp_V2_AnalyzeDataSourceRiskDetails_Types_KAnonymityResult_EquivalenceClassHistogramBuckets)[bucketIdx];
                Console.WriteLine($"Bucket {bucketIdx}");
                Console.WriteLine($"  Bucket size range: [{bucket.[EquivalenceClassSizeLowerBound](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KAnonymityResult.Types.KAnonymityHistogramBucket.html#Google_Cloud_Dlp_V2_AnalyzeDataSourceRiskDetails_Types_KAnonymityResult_Types_KAnonymityHistogramBucket_EquivalenceClassSizeLowerBound)}, {bucket.[EquivalenceClassSizeUpperBound](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KAnonymityResult.Types.KAnonymityHistogramBucket.html#Google_Cloud_Dlp_V2_AnalyzeDataSourceRiskDetails_Types_KAnonymityResult_Types_KAnonymityHistogramBucket_EquivalenceClassSizeUpperBound)}].");
                Console.WriteLine($"  {bucket.BucketSize} unique value(s) total.");
    
                foreach (var bucketValue in bucket.BucketValues)
                {
                    // 'UnpackValue(x)' is a prettier version of 'x.toString()'
                    Console.WriteLine($"    Quasi-ID values: [{String.Join(',', bucketValue.QuasiIdsValues.Select(x => UnpackValue(x)))}]");
                    Console.WriteLine($"    Class size: {bucketValue.EquivalenceClassSize}");
                }
            }
    
            return result;
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
    )
    
    // riskKAnonymity computes the risk of the given columns using K Anonymity.
    func riskKAnonymity(w io.Writer, projectID, dataProject, pubSubTopic, pubSubSub, datasetID, tableID string, columnNames ...string) error {
    	// projectID := "my-project-id"
    	// dataProject := "bigquery-public-data"
    	// pubSubTopic := "dlp-risk-sample-topic"
    	// pubSubSub := "dlp-risk-sample-sub"
    	// datasetID := "nhtsa_traffic_fatalities"
    	// tableID := "accident_2015"
    	// columnNames := "state_number" "county"
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
    	var q []*dlppb.FieldId
    	for _, c := range columnNames {
    		q = append(q, &dlppb.FieldId{Name: c})
    	}
    
    	// Create a configured request.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_RiskJob{
    			RiskJob: &dlppb.RiskAnalysisJobConfig{
    				// PrivacyMetric configures what to compute.
    				PrivacyMetric: &dlppb.PrivacyMetric{
    					Type: &dlppb.PrivacyMetric_KAnonymityConfig_{
    						KAnonymityConfig: &dlppb.PrivacyMetric_KAnonymityConfig{
    							QuasiIds: q,
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
    		h := j.GetRiskDetails().GetKAnonymityResult().GetEquivalenceClassHistogramBuckets()
    		for i, b := range h {
    			fmt.Fprintf(w, "Histogram bucket %v\n", i)
    			fmt.Fprintf(w, "  Size range: [%v,%v]\n", b.GetEquivalenceClassSizeLowerBound(), b.GetEquivalenceClassSizeUpperBound())
    			fmt.Fprintf(w, "  %v unique values total\n", b.GetBucketSize())
    			for _, v := range b.GetBucketValues() {
    				var qvs []string
    				for _, qv := range v.GetQuasiIdsValues() {
    					qvs = append(qvs, qv.String())
    				}
    				fmt.Fprintf(w, "    QuasiID values: %s\n", strings.Join(qvs, ", "))
    				fmt.Fprintf(w, "    Class size: %v\n", v.GetEquivalenceClassSize())
    			}
    		}
    		// Stop listening for more messages.
    		cancel()
    	})
    	if err != nil {
    		return fmt.Errorf("Receive: %w", err)
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
    import com.google.privacy.dlp.v2.[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.html).[KAnonymityResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.html);
    import com.google.privacy.dlp.v2.[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.html).[KAnonymityResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.html).[KAnonymityEquivalenceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityEquivalenceClass.html);
    import com.google.privacy.dlp.v2.[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.html).[KAnonymityResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.html).[KAnonymityHistogramBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityHistogramBucket.html);
    import com.google.privacy.dlp.v2.[BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html);
    import com.google.privacy.dlp.v2.[PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html).[KAnonymityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KAnonymityConfig.html);
    import com.google.privacy.dlp.v2.[RiskAnalysisJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RiskAnalysisJobConfig.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import java.util.stream.Collectors;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    class RiskAnalysisKAnonymity {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String datasetId = "your-bigquery-dataset-id";
        String tableId = "your-bigquery-table-id";
        String topicId = "pub-sub-topic";
        String subscriptionId = "pub-sub-subscription";
        calculateKAnonymity(projectId, datasetId, tableId, topicId, subscriptionId);
      }
    
      public static void calculateKAnonymity(
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
          List<String> quasiIds = Arrays.asList("Age", "Mystery");
    
          // Configure the privacy metric for the job
          List<FieldId> quasiIdFields =
              quasiIds.stream()
                  .map(columnName -> [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName(columnName).build())
                  .collect(Collectors.toList());
          [KAnonymityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KAnonymityConfig.html) kanonymityConfig =
              [KAnonymityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KAnonymityConfig.html).newBuilder().addAllQuasiIds(quasiIdFields).build();
          [PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html) privacyMetric =
              [PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html).newBuilder().[setKAnonymityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.Builder.html#com_google_privacy_dlp_v2_PrivacyMetric_Builder_setKAnonymityConfig_com_google_privacy_dlp_v2_PrivacyMetric_KAnonymityConfig_)(kanonymityConfig).build();
    
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
          [KAnonymityResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.html) kanonymityResult = completedJob.[getRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getRiskDetails__)().getKAnonymityResult();
          List<KAnonymityHistogramBucket> histogramBucketList =
              kanonymityResult.getEquivalenceClassHistogramBucketsList();
          for ([KAnonymityHistogramBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityHistogramBucket.html) result : histogramBucketList) {
            System.out.printf(
                "Bucket size range: [%d, %d]\n",
                result.getEquivalenceClassSizeLowerBound(), result.getEquivalenceClassSizeUpperBound());
    
            for ([KAnonymityEquivalenceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityEquivalenceClass.html) bucket : result.getBucketValuesList()) {
              List<String> quasiIdValues =
                  bucket.getQuasiIdsValuesList().stream()
                      .map(Value::toString)
                      .collect(Collectors.toList());
    
              System.out.println("\tQuasi-ID values: " + String.join(", ", quasiIdValues));
              System.out.println("\tClass size: " + bucket.getEquivalenceClassSize());
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
    
    // A set of columns that form a composite key ('quasi-identifiers')
    // const quasiIds = [{ name: 'age' }, { name: 'city' }];
    async function kAnonymityAnalysis() {
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
            kAnonymityConfig: {
              quasiIds: quasiIds,
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
        job.riskDetails.kAnonymityResult.equivalenceClassHistogramBuckets;
    
      histogramBuckets.forEach((histogramBucket, histogramBucketIdx) => {
        console.log(`Bucket ${histogramBucketIdx}:`);
        console.log(
          `  Bucket size range: [${histogramBucket.equivalenceClassSizeLowerBound}, ${histogramBucket.equivalenceClassSizeUpperBound}]`
        );
    
        histogramBucket.bucketValues.forEach(valueBucket => {
          const quasiIdValues = valueBucket.quasiIdsValues
            .map(getValue)
            .join(', ');
          console.log(`  Quasi-ID values: {${quasiIdValues}}`);
          console.log(`  Class size: ${valueBucket.equivalenceClassSize}`);
        });
      });
    }
    await kAnonymityAnalysis();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\RiskAnalysisJobConfig;
    use Google\Cloud\Dlp\V2\BigQueryTable;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishToPubSub;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\PrivacyMetric;
    use Google\Cloud\Dlp\V2\PrivacyMetric\KAnonymityConfig;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Computes the k-anonymity of a column set in a Google BigQuery table.
     *
     * @param string    $callingProjectId  The project ID to run the API call under
     * @param string    $dataProjectId     The project ID containing the target Datastore
     * @param string    $topicId           The name of the Pub/Sub topic to notify once the job completes
     * @param string    $subscriptionId    The name of the Pub/Sub subscription to use when listening for job
     * @param string    $datasetId         The ID of the dataset to inspect
     * @param string    $tableId           The ID of the table to inspect
     * @param string[]  $quasiIdNames      Array columns that form a composite key (quasi-identifiers)
     */
    function k_anonymity(
        string $callingProjectId,
        string $dataProjectId,
        string $topicId,
        string $subscriptionId,
        string $datasetId,
        string $tableId,
        array $quasiIdNames
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
        $pubsub = new PubSubClient();
        $topic = $pubsub->topic($topicId);
    
        // Construct risk analysis config
        $quasiIds = array_map(
            function ($id) {
                return (new FieldId())->setName($id);
            },
            $quasiIdNames
        );
    
        $statsConfig = (new KAnonymityConfig())
            ->setQuasiIds($quasiIds);
    
        $privacyMetric = (new PrivacyMetric())
            ->setKAnonymityConfig($statsConfig);
    
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
                $histBuckets = $job->getRiskDetails()->getKAnonymityResult()->getEquivalenceClassHistogramBuckets();
    
                foreach ($histBuckets as $bucketIndex => $histBucket) {
                    // Print bucket stats
                    printf('Bucket %s:' . PHP_EOL, $bucketIndex);
                    printf(
                        '  Bucket size range: [%s, %s]' . PHP_EOL,
                        $histBucket->getEquivalenceClassSizeLowerBound(),
                        $histBucket->getEquivalenceClassSizeUpperBound()
                    );
    
                    // Print bucket values
                    foreach ($histBucket->getBucketValues() as $percent => $valueBucket) {
                        // Pretty-print quasi-ID values
                        print('  Quasi-ID values:' . PHP_EOL);
                        foreach ($valueBucket->getQuasiIdsValues() as $index => $value) {
                            print('    ' . $value->serializeToJsonString() . PHP_EOL);
                        }
                        printf(
                            '  Class size: %s' . PHP_EOL,
                            $valueBucket->getEquivalenceClassSize()
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
    
    
    def k_anonymity_analysis(
        project: str,
        table_project_id: str,
        dataset_id: str,
        table_id: str,
        topic_id: str,
        subscription_id: str,
        quasi_ids: List[str],
        timeout: int = 300,
    ) -> None:
        """Uses the Data Loss Prevention API to compute the k-anonymity of a
            column set in a Google BigQuery table.
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
            quasi_ids: A set of columns that form a composite key.
            timeout: The number of seconds to wait for a response from the API.
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Create helper function for unpacking values
        def get_values(obj: types.[Value](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Value.html)) -> int:
            return int(obj.integer_value)
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        topic = google.cloud.pubsub.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html).topic_path(project, topic_id)
        parent = f"projects/{project}/locations/global"
    
        # Location info of the BigQuery table.
        source_table = {
            "project_id": table_project_id,
            "dataset_id": dataset_id,
            "table_id": table_id,
        }
    
        # Convert quasi id list to Protobuf type
        def map_fields(field: str) -> dict:
            return {"name": field}
    
        quasi_ids = map(map_fields, quasi_ids)
    
        # Tell the API where to send a notification when the job is complete.
        actions = [{"pub_sub": {"topic": topic}}]
    
        # Configure risk analysis job
        # Give the name of the numeric column to compute risk metrics for
        risk_job = {
            "privacy_metric": {"k_anonymity_config": {"quasi_ids": quasi_ids}},
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
                    job.risk_details.k_anonymity_result.equivalence_class_histogram_buckets
                )
                # Print bucket stats
                for i, bucket in enumerate(histogram_buckets):
                    print(f"Bucket {i}:")
                    if bucket.equivalence_class_size_lower_bound:
                        print(
                            "   Bucket size range: [{}, {}]".format(
                                bucket.equivalence_class_size_lower_bound,
                                bucket.equivalence_class_size_upper_bound,
                            )
                        )
                        for value_bucket in bucket.bucket_values:
                            print(
                                "   Quasi-ID values: {}".format(
                                    map(get_values, value_bucket.quasi_ids_values)
                                )
                            )
                            print(
                                "   Class size: {}".format(
                                    value_bucket.equivalence_class_size
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
    
    

### REST

To run a new risk analysis job to compute _k_ -anonymity, send a request to the [`projects.dlpJobs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/list) resource, where PROJECT_ID indicates your [project identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects):
    
    
    https://dlp.googleapis.com/v2/projects/PROJECT_ID/dlpJobs

The request contains a [`RiskAnalysisJobConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.RiskAnalysisJobConfig) object, which is composed of the following:

  * A [`PrivacyMetric`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#privacymetric) object. This is where you specify that you're calculating _k_ -anonymity by including a [`KAnonymityConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#kanonymityconfig) object.

  * A [`BigQueryTable`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable) object. Specify the BigQuery table to scan by including all of the following:

    * `projectId`: The project ID of the project containing the table.
    * `datasetId`: The dataset ID of the table.
    * `tableId`: The name of the table.
  * A set of one or more [`Action`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action) objects, which represent actions to run, in the order given, at the completion of the job. Each `Action` object can contain one of the following actions:

    * [`SaveFindings`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#SaveFindings) object: Saves the results of the risk analysis scan to a BigQuery table.
    * [`PublishToPubSub`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishToPubSub) object: [Publishes a notification to a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/publisher).

**Note:** If there are configuration or permission issues with the Pub/Sub topic, Sensitive Data Protection retries sending the Pub/Sub notification for up to two weeks. After two weeks, the notification is discarded. 
    * [`JobNotificationEmails`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#JobNotificationEmails) object: Sends you an email with results.

Within the [`KAnonymityConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#kanonymityconfig) object, you specify the following:

**Important:** Be aware that running a risk analysis job may persist some of the [quote](https://docs.cloud.google.com/sensitive-data-protection/docs/quote) values of the selected quasi-identifiers to the risk analysis job results. These quote values are used to build the histogram and output tables.
    * `quasiIds[]`: One or more quasi-identifiers ([`FieldId`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId) objects) to scan and use to compute _k_ -anonymity. When you specify multiple quasi-identifiers, they are considered a single composite key. Structs and repeated data types are not supported, but nested fields are supported as long as they are not structs themselves or nested within a repeated field.
    * `entityId`: Optional identifier value that, when set, indicates that all rows corresponding to each distinct `entityId` should be grouped together for _k_ -anonymity computation. Typically, an `entityId` will be a column that represents a unique user, like a customer ID or a user ID. When an `entityId` appears on several rows with different quasi-identifier values, these rows will be joined to form a multiset that will be used as the quasi-identifiers for that entity. For more information about entity IDs, see [Entity IDs and computing _k_ -anonymity](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#entity-ids) in the [Risk analysis](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis) conceptual topic.



As soon as you send a request to the DLP API, it starts the risk analysis job.

## List completed risk analysis jobs

You can view a list of the risk analysis jobs that have been run in the current project.

###  Console 

To list running and previously run risk analysis jobs in the Google Cloud console, do the following:

  1. In the Google Cloud console, open Sensitive Data Protection.

[Go to Sensitive Data Protection](https://console.cloud.google.com/security/sensitive-data-protection;source=7)

  2. Click the **Jobs & job triggers** tab at the top of the page.

  3. Click the **Risk jobs** tab.




The risk job listing appears.

###  Protocol 

To list running and previously run risk analysis jobs, send a GET request to the [`projects.dlpJobs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/list) resource. Adding a job type filter (`?type=RISK_ANALYSIS_JOB`) narrows the response to only risk analysis jobs.
    
    
    https://dlp.googleapis.com/v2/projects/PROJECT_ID/dlpJobs?type=RISK_ANALYSIS_JOB

The response you receive contains a JSON representation of all current and previous risk analysis jobs.

## View k-anonymity job results

Sensitive Data Protection in the Google Cloud console features built-in visualizations for completed _k_ -anonymity jobs. After following the instructions in the previous section, from the risk analysis job listing, select the job for which you want to view results. Assuming the job has run successfully, the top of the **Risk analysis details** page looks like this:

![](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/compute-risk-analysis-k-results1.png)

At the top of the page is information about the _k_ -anonymity risk job, including its job ID and, under **Container** , its resource location.

To view the results of the _k_ -anonymity calculation, click the **K-anonymity** tab. To view the risk analysis job's configuration, click the **Configuration** tab.

The **K-anonymity** tab first lists the entity ID (if any) and the quasi-identifiers used to calculate _k_ -anonymity.

### Risk chart

The **Re-identification risk** chart plots, on the _y_ -axis, the potential percentage of data loss for both unique rows and unique quasi-identifier combinations to achieve, on the _x_ -axis, a _k_ -anonymity value. The chart's color also indicates risk potential. Darker shades of blue indicate a higher risk, while lighter shades indicate less risk.

Higher _k_ -anonymity values indicate less risk of re-identification. To achieve higher _k_ -anonymity values, however, you would need to remove higher percentages of the total rows and higher unique quasi-identifier combinations, which might decrease the utility of the data. To see a specific potential percentage loss value for a certain _k_ -anonymity value, hover your cursor over the chart. As shown in the screenshot, a tooltip appears on the chart.

To view more detail about a specific _k_ -anonymity value, click the corresponding data point. A detailed explanation is shown under the chart and a sample data table appears further down the page.

### Risk sample data table

The second component to the risk job results page is the sample data table. It displays quasi-identifier combinations for a given target _k_ -anonymity value.

![](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/compute-risk-analysis-k-results2.png)

The first column of the table lists the k-anonymity values. Click a _k_ -anonymity value to view corresponding sample data that would need to be dropped to achieve that value.

The second column displays the respective potential data loss of unique rows and quasi-identifier combinations, as well as the number of groups with at least _k_ records and the total number of records.

The last column displays a sample of groups that share a quasi-identifier combination, along with the number of records that exist for that combination.

## Retrieve job details using REST

To retrieve the results of the _k_ -anonymity risk analysis job using the REST API, send the following GET request to the [`projects.dlpJobs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/get) resource. Replace PROJECT_ID with your project ID and JOB_ID with the identifier of the job you want to obtain results for. The job ID was returned when you started the job, and can also be retrieved by listing all jobs.
    
    
    GET https://dlp.googleapis.com/v2/projects/PROJECT_ID/dlpJobs/JOB_ID

The request returns a JSON object containing an instance of the job. The results of the analysis are inside the `"riskDetails"` key, in an [`AnalyzeDataSourceRiskDetails`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.AnalyzeDataSourceRiskDetails) object. For more information, see the API reference for the [`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob) resource.

## Code sample: Compute for k-anonymity with an entity ID

This example creates a risk analysis job that computes for k-anonymity with an entity ID.

For more information about entity IDs, see [Entity IDs and computing _k_ -anonymity](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#entity-ids).

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using Newtonsoft.Json;
    
    public class CalculateKAnonymityOnDataset
    {
        public static DlpJob CalculateKAnonymitty(
            string projectId,
            string datasetId,
            string sourceTableId,
            string outputTableId)
        {
            // Construct the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the k-anonymity config by setting the EntityId as user_id column
            // and two quasi-identifiers columns.
            var kAnonymity = new PrivacyMetric.Types.KAnonymityConfig
            {
                EntityId = new [EntityId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.EntityId.html)
                {
                    Field = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Name" }
                },
                QuasiIds =
                {
                    new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Age" },
                    new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Mystery" }
                }
            };
    
            // Construct risk analysis job config by providing the source table, privacy metric
            // and action to save the findings to a BigQuery table.
            var riskJob = new [RiskAnalysisJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RiskAnalysisJobConfig.html)
            {
                SourceTable = new [BigQueryTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTable.html)
                {
                    ProjectId = projectId,
                    DatasetId = datasetId,
                    TableId = sourceTableId,
                },
                PrivacyMetric = new [PrivacyMetric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.html)
                {
                    KAnonymityConfig = kAnonymity,
                },
                Actions =
                {
                    new Google.Cloud.Dlp.V2.Action
                    {
                        SaveFindings = new Google.Cloud.Dlp.V2.Action.Types.SaveFindings
                        {
                            OutputConfig = new [OutputStorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OutputStorageConfig.html)
                            {
                                Table = new [BigQueryTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTable.html)
                                {
                                    ProjectId = projectId,
                                    DatasetId = datasetId,
                                    TableId = outputTableId
                                }
                            }
                        }
                    }
                }
            };
    
            // Construct the request by providing RiskJob object created above.
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                RiskJob = riskJob
            };
    
            // Send the job request.
            [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html) response = dlp.CreateDlpJob(request);
    
            Console.WriteLine($"Job created successfully. Job name: ${response.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html#Google_Cloud_Dlp_V2_DlpJob_Name)}");
    
            return response;
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
    )
    
    // Uses the Data Loss Prevention API to compute the k-anonymity of a
    // column set in a Google BigQuery table.
    func calculateKAnonymityWithEntityId(w io.Writer, projectID, datasetId, tableId string, columnNames ...string) error {
    	// projectID := "your-project-id"
    	// datasetId := "your-bigquery-dataset-id"
    	// tableId := "your-bigquery-table-id"
    	// columnNames := "age" "job_title"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Closing the client safely cleans up background resources.
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Specify the BigQuery table to analyze
    	bigQueryTable := &dlppb.BigQueryTable{
    		ProjectId: "bigquery-public-data",
    		DatasetId: "samples",
    		TableId:   "wikipedia",
    	}
    
    	// Configure the privacy metric for the job
    	// Build the QuasiID slice.
    	var q []*dlppb.FieldId
    	for _, c := range columnNames {
    		q = append(q, &dlppb.FieldId{Name: c})
    	}
    
    	entityId := &dlppb.EntityId{
    		Field: &dlppb.FieldId{
    			Name: "id",
    		},
    	}
    
    	kAnonymityConfig := &dlppb.PrivacyMetric_KAnonymityConfig{
    		QuasiIds: q,
    		EntityId: entityId,
    	}
    
    	privacyMetric := &dlppb.PrivacyMetric{
    		Type: &dlppb.PrivacyMetric_KAnonymityConfig_{
    			KAnonymityConfig: kAnonymityConfig,
    		},
    	}
    
    	// Specify the bigquery table to store the findings.
    	// The "test_results" table in the given BigQuery dataset will be created if it doesn't
    	// already exist.
    	outputbigQueryTable := &dlppb.BigQueryTable{
    		ProjectId: projectID,
    		DatasetId: datasetId,
    		TableId:   tableId,
    	}
    
    	// Create action to publish job status notifications to BigQuery table.
    	outputStorageConfig := &dlppb.OutputStorageConfig{
    		Type: &dlppb.OutputStorageConfig_Table{
    			Table: outputbigQueryTable,
    		},
    	}
    
    	findings := &dlppb.Action_SaveFindings{
    		OutputConfig: outputStorageConfig,
    	}
    
    	action := &dlppb.Action{
    		Action: &dlppb.Action_SaveFindings_{
    			SaveFindings: findings,
    		},
    	}
    
    	// Configure the risk analysis job to perform
    	riskAnalysisJobConfig := &dlppb.RiskAnalysisJobConfig{
    		PrivacyMetric: privacyMetric,
    		SourceTable:   bigQueryTable,
    		Actions: []*dlppb.Action{
    			action,
    		},
    	}
    
    	// Build the request to be sent by the client
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_RiskJob{
    			RiskJob: riskAnalysisJobConfig,
    		},
    	}
    
    	// Send the request to the API using the client
    	dlpJob, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "Created job: %v\n", dlpJob.GetName())
    
    	// Build a request to get the completed job
    	getDlpJobReq := &dlppb.GetDlpJobRequest{
    		Name: dlpJob.Name,
    	}
    
    	timeout := 15 * time.Minute
    	startTime := time.Now()
    
    	var completedJob *dlppb.DlpJob
    
    	// Wait for job completion
    	for time.Since(startTime) <= timeout {
    		completedJob, err = client.GetDlpJob(ctx, getDlpJobReq)
    		if err != nil {
    			return err
    		}
    
    		if completedJob.GetState() == dlppb.DlpJob_DONE {
    			break
    		}
    
    		time.Sleep(30 * time.Second)
    
    	}
    
    	if completedJob.GetState() != dlppb.DlpJob_DONE {
    		fmt.Println("Job did not complete within 15 minutes.")
    	}
    
    	// Retrieve completed job status
    	fmt.Fprintf(w, "Job status: %v", completedJob.State)
    	fmt.Fprintf(w, "Job name: %v", dlpJob.Name)
    
    	// Get the result and parse through and process the information
    	kanonymityResult := completedJob.GetRiskDetails().GetKAnonymityResult()
    
    	for _, result := range kanonymityResult.GetEquivalenceClassHistogramBuckets() {
    		fmt.Fprintf(w, "Bucket size range: [%d, %d]\n", result.GetEquivalenceClassSizeLowerBound(), result.GetEquivalenceClassSizeLowerBound())
    
    		for _, bucket := range result.GetBucketValues() {
    			quasiIdValues := []string{}
    			for _, v := range bucket.GetQuasiIdsValues() {
    				quasiIdValues = append(quasiIdValues, v.GetStringValue())
    			}
    			fmt.Fprintf(w, "\tQuasi-ID values: %s", strings.Join(quasiIdValues, ","))
    			fmt.Fprintf(w, "\tClass size: %d", bucket.EquivalenceClassSize)
    		}
    	}
    
    	return nil
    
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[SaveFindings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.SaveFindings.html);
    import com.google.privacy.dlp.v2.[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.html).[KAnonymityResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.html);
    import com.google.privacy.dlp.v2.[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.html).[KAnonymityResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.html).[KAnonymityEquivalenceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityEquivalenceClass.html);
    import com.google.privacy.dlp.v2.[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.html).[KAnonymityResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.html).[KAnonymityHistogramBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityHistogramBucket.html);
    import com.google.privacy.dlp.v2.[BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[EntityId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.EntityId.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[OutputStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.OutputStorageConfig.html);
    import com.google.privacy.dlp.v2.[PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html);
    import com.google.privacy.dlp.v2.[PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html).[KAnonymityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KAnonymityConfig.html);
    import com.google.privacy.dlp.v2.[RiskAnalysisJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RiskAnalysisJobConfig.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    import java.time.Duration;
    import java.util.Arrays;
    import java.util.List;
    import java.util.concurrent.TimeUnit;
    import java.util.stream.Collectors;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    public class RiskAnalysisKAnonymityWithEntityId {
    
      public static void main(String[] args) throws IOException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The BigQuery dataset id to be used and the reference table name to be inspected.
        String datasetId = "your-bigquery-dataset-id";
        String tableId = "your-bigquery-table-id";
        calculateKAnonymityWithEntityId(projectId, datasetId, tableId);
      }
    
      // Uses the Data Loss Prevention API to compute the k-anonymity of a column set in a Google
      // BigQuery table.
      public static void calculateKAnonymityWithEntityId(
          String projectId, String datasetId, String tableId) throws IOException, InterruptedException {
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
          List<String> quasiIds = Arrays.asList("Age", "Mystery");
    
          // Create a list of FieldId objects based on the provided list of column names.
          List<FieldId> quasiIdFields =
              quasiIds.stream()
                  .map(columnName -> [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName(columnName).build())
                  .collect(Collectors.toList());
    
          // Specify the unique identifier in the source table for the k-anonymity analysis.
          [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html) uniqueIdField = [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Name").build();
          [EntityId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.EntityId.html) entityId = [EntityId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.EntityId.html).newBuilder().setField(uniqueIdField).build();
          [KAnonymityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KAnonymityConfig.html) kanonymityConfig = [KAnonymityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KAnonymityConfig.html).newBuilder()
                  .addAllQuasiIds(quasiIdFields)
                  .[setEntityId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.KAnonymityConfig.Builder.html#com_google_privacy_dlp_v2_PrivacyMetric_KAnonymityConfig_Builder_setEntityId_com_google_privacy_dlp_v2_EntityId_)(entityId)
                  .build();
    
          // Configure the privacy metric to compute for re-identification risk analysis.
          [PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html) privacyMetric =
              [PrivacyMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.html).newBuilder().[setKAnonymityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.Builder.html#com_google_privacy_dlp_v2_PrivacyMetric_Builder_setKAnonymityConfig_com_google_privacy_dlp_v2_PrivacyMetric_KAnonymityConfig_)(kanonymityConfig).build();
    
          // Specify the bigquery table to store the findings.
          // The "test_results" table in the given BigQuery dataset will be created if it doesn't
          // already exist.
          [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html) outputbigQueryTable =
              [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html).newBuilder()
                  .setProjectId(projectId)
                  .setDatasetId(datasetId)
                  .setTableId("test_results")
                  .build();
    
          // Create action to publish job status notifications to BigQuery table.
          [OutputStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.OutputStorageConfig.html) outputStorageConfig =
              [OutputStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.OutputStorageConfig.html).newBuilder().setTable(outputbigQueryTable).build();
          [SaveFindings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.SaveFindings.html) findings =
              [SaveFindings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.SaveFindings.html).newBuilder().[setOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.SaveFindings.Builder.html#com_google_privacy_dlp_v2_Action_SaveFindings_Builder_setOutputConfig_com_google_privacy_dlp_v2_OutputStorageConfig_)(outputStorageConfig).build();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setSaveFindings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setSaveFindings_com_google_privacy_dlp_v2_Action_SaveFindings_)(findings).build();
    
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
    
          // Build a request to get the completed job
          [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html) getDlpJobRequest =
              [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html).newBuilder().setName(dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)()).build();
    
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) completedJob = null;
          // Wait for job completion
          try {
            Duration timeout = Duration.ofMinutes(15);
            long startTime = System.currentTimeMillis();
            do {
              completedJob = dlpServiceClient.getDlpJob(getDlpJobRequest);
              TimeUnit.SECONDS.sleep(30);
            } while (completedJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)() != DlpJob.JobState.DONE
                && System.currentTimeMillis() - startTime <= timeout.toMillis());
          } catch (InterruptedException e) {
            System.out.println("Job did not complete within 15 minutes.");
          }
    
          // Retrieve completed job status
          System.out.println("Job status: " + completedJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
          // Get the result and parse through and process the information
          [KAnonymityResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.html) kanonymityResult = completedJob.[getRiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getRiskDetails__)().getKAnonymityResult();
          for ([KAnonymityHistogramBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityHistogramBucket.html) result :
              kanonymityResult.getEquivalenceClassHistogramBucketsList()) {
            System.out.printf(
                "Bucket size range: [%d, %d]\n",
                result.getEquivalenceClassSizeLowerBound(), result.getEquivalenceClassSizeUpperBound());
    
            for ([KAnonymityEquivalenceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityEquivalenceClass.html) bucket : result.getBucketValuesList()) {
              List<String> quasiIdValues =
                  bucket.getQuasiIdsValuesList().stream()
                      .map(Value::toString)
                      .collect(Collectors.toList());
    
              System.out.println("\tQuasi-ID values: " + String.join(", ", quasiIdValues));
              System.out.println("\tClass size: " + bucket.getEquivalenceClassSize());
            }
          }
        }
      }
    }
    

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('@google-cloud/dlp');
    
    // Instantiates a client
    const dlp = new DLP.DlpServiceClient();
    
    // The project ID to run the API call under.
    // const projectId = "your-project-id";
    
    // The ID of the dataset to inspect, e.g. 'my_dataset'
    // const datasetId = 'my_dataset';
    
    // The ID of the table to inspect, e.g. 'my_table'
    // const sourceTableId = 'my_source_table';
    
    // The ID of the table where outputs are stored
    // const outputTableId = 'my_output_table';
    
    async function kAnonymityWithEntityIds() {
      // Specify the BigQuery table to analyze.
      const sourceTable = {
        projectId: projectId,
        datasetId: datasetId,
        tableId: sourceTableId,
      };
    
      // Specify the unique identifier in the source table for the k-anonymity analysis.
      const uniqueIdField = {name: 'Name'};
    
      // These values represent the column names of quasi-identifiers to analyze
      const quasiIds = [{name: 'Age'}, {name: 'Mystery'}];
    
      // Configure the privacy metric to compute for re-identification risk analysis.
      const privacyMetric = {
        kAnonymityConfig: {
          entityId: {
            field: uniqueIdField,
          },
          quasiIds: quasiIds,
        },
      };
      // Create action to publish job status notifications to BigQuery table.
      const action = [
        {
          saveFindings: {
            outputConfig: {
              table: {
                projectId: projectId,
                datasetId: datasetId,
                tableId: outputTableId,
              },
            },
          },
        },
      ];
    
      // Configure the risk analysis job to perform.
      const riskAnalysisJob = {
        sourceTable: sourceTable,
        privacyMetric: privacyMetric,
        actions: action,
      };
      // Combine configurations into a request for the service.
      const createDlpJobRequest = {
        parent: `projects/${projectId}/locations/global`,
        riskJob: riskAnalysisJob,
      };
    
      // Send the request and receive response from the service
      const [createdDlpJob] = await dlp.createDlpJob(createDlpJobRequest);
      const jobName = createdDlpJob.name;
    
      // Waiting for a maximum of 15 minutes for the job to get complete.
      let job;
      let numOfAttempts = 30;
      while (numOfAttempts > 0) {
        // Fetch DLP Job status
        [job] = await dlp.getDlpJob({name: jobName});
    
        // Check if the job has completed.
        if (job.state === 'DONE') {
          break;
        }
        if (job.state === 'FAILED') {
          console.log('Job Failed, Please check the configuration.');
          return;
        }
        // Sleep for a short duration before checking the job status again.
        await new Promise(resolve => {
          setTimeout(() => resolve(), 30000);
        });
        numOfAttempts -= 1;
      }
    
      // Create helper function for unpacking values
      const getValue = obj => obj[Object.keys(obj)[0]];
    
      // Print out the results.
      const histogramBuckets =
        job.riskDetails.kAnonymityResult.equivalenceClassHistogramBuckets;
    
      histogramBuckets.forEach((histogramBucket, histogramBucketIdx) => {
        console.log(`Bucket ${histogramBucketIdx}:`);
        console.log(
          `  Bucket size range: [${histogramBucket.equivalenceClassSizeLowerBound}, ${histogramBucket.equivalenceClassSizeUpperBound}]`
        );
    
        histogramBucket.bucketValues.forEach(valueBucket => {
          const quasiIdValues = valueBucket.quasiIdsValues
            .map(getValue)
            .join(', ');
          console.log(`  Quasi-ID values: {${quasiIdValues}}`);
          console.log(`  Class size: ${valueBucket.equivalenceClassSize}`);
        });
      });
    }
    await kAnonymityWithEntityIds();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\SaveFindings;
    use Google\Cloud\Dlp\V2\BigQueryTable;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\EntityId;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\OutputStorageConfig;
    use Google\Cloud\Dlp\V2\PrivacyMetric;
    use Google\Cloud\Dlp\V2\PrivacyMetric\KAnonymityConfig;
    use Google\Cloud\Dlp\V2\RiskAnalysisJobConfig;
    
    /**
     * Computes the k-anonymity of a column set in a Google BigQuery table with entity id.
     *
     * @param string    $callingProjectId  The project ID to run the API call under.
     * @param string    $datasetId         The ID of the dataset to inspect.
     * @param string    $tableId           The ID of the table to inspect.
     * @param string[]  $quasiIdNames      Array columns that form a composite key (quasi-identifiers).
     */
    
    function k_anonymity_with_entity_id(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $datasetId,
        string $tableId,
        array  $quasiIdNames
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Specify the BigQuery table to analyze.
        $bigqueryTable = (new BigQueryTable())
            ->setProjectId($callingProjectId)
            ->setDatasetId($datasetId)
            ->setTableId($tableId);
    
        // Create a list of FieldId objects based on the provided list of column names.
        $quasiIds = array_map(
            function ($id) {
                return (new FieldId())
                    ->setName($id);
            },
            $quasiIdNames
        );
    
        // Specify the unique identifier in the source table for the k-anonymity analysis.
        $statsConfig = (new KAnonymityConfig())
            ->setEntityId((new EntityId())
                ->setField((new FieldId())
                    ->setName('Name')))
            ->setQuasiIds($quasiIds);
    
        // Configure the privacy metric to compute for re-identification risk analysis.
        $privacyMetric = (new PrivacyMetric())
            ->setKAnonymityConfig($statsConfig);
    
        // Specify the bigquery table to store the findings.
        // The "test_results" table in the given BigQuery dataset will be created if it doesn't
        // already exist.
        $outBigqueryTable = (new BigQueryTable())
            ->setProjectId($callingProjectId)
            ->setDatasetId($datasetId)
            ->setTableId('test_results');
    
        $outputStorageConfig = (new OutputStorageConfig())
            ->setTable($outBigqueryTable);
    
        $findings = (new SaveFindings())
            ->setOutputConfig($outputStorageConfig);
    
        $action = (new Action())
            ->setSaveFindings($findings);
    
        // Construct risk analysis job config to run.
        $riskJob = (new RiskAnalysisJobConfig())
            ->setPrivacyMetric($privacyMetric)
            ->setSourceTable($bigqueryTable)
            ->setActions([$action]);
    
        // Submit request.
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setRiskJob($riskJob);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        $numOfAttempts = 10;
        do {
            printf('Waiting for job to complete' . PHP_EOL);
            sleep(10);
            $getDlpJobRequest = (new GetDlpJobRequest())
                ->setName($job->getName());
            $job = $dlp->getDlpJob($getDlpJobRequest);
            if ($job->getState() == JobState::DONE) {
                break;
            }
            $numOfAttempts--;
        } while ($numOfAttempts > 0);
    
        // Print finding counts
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $histBuckets = $job->getRiskDetails()->getKAnonymityResult()->getEquivalenceClassHistogramBuckets();
    
                foreach ($histBuckets as $bucketIndex => $histBucket) {
                    // Print bucket stats.
                    printf('Bucket %s:' . PHP_EOL, $bucketIndex);
                    printf(
                        '  Bucket size range: [%s, %s]' . PHP_EOL,
                        $histBucket->getEquivalenceClassSizeLowerBound(),
                        $histBucket->getEquivalenceClassSizeUpperBound()
                    );
    
                    // Print bucket values.
                    foreach ($histBucket->getBucketValues() as $percent => $valueBucket) {
                        // Pretty-print quasi-ID values.
                        printf('  Quasi-ID values:' . PHP_EOL);
                        foreach ($valueBucket->getQuasiIdsValues() as $index => $value) {
                            print('    ' . $value->serializeToJsonString() . PHP_EOL);
                        }
                        printf(
                            '  Class size: %s' . PHP_EOL,
                            $valueBucket->getEquivalenceClassSize()
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
    
    
    import time
    from typing import List
    
    import google.cloud.dlp_v2
    from google.cloud.dlp_v2 import [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html)
    
    
    def k_anonymity_with_entity_id(
        project: str,
        source_table_project_id: str,
        source_dataset_id: str,
        source_table_id: str,
        entity_id: str,
        quasi_ids: List[str],
        output_table_project_id: str,
        output_dataset_id: str,
        output_table_id: str,
    ) -> None:
        """Uses the Data Loss Prevention API to compute the k-anonymity using entity_id
            of a column set in a Google BigQuery table.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            source_table_project_id: The Google Cloud project id where the BigQuery table
                is stored.
            source_dataset_id: The id of the dataset to inspect.
            source_table_id: The id of the table to inspect.
            entity_id: The column name of the table that enables accurately determining k-anonymity
             in the common scenario wherein several rows of dataset correspond to the same sensitive
             information.
            quasi_ids: A set of columns that form a composite key.
            output_table_project_id: The Google Cloud project id where the output BigQuery table
                is stored.
            output_dataset_id: The id of the output BigQuery dataset.
            output_table_id: The id of the output BigQuery table.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Location info of the source BigQuery table.
        source_table = {
            "project_id": source_table_project_id,
            "dataset_id": source_dataset_id,
            "table_id": source_table_id,
        }
    
        # Specify the bigquery table to store the findings.
        # The output_table_id in the given BigQuery dataset will be created if it doesn't
        # already exist.
        dest_table = {
            "project_id": output_table_project_id,
            "dataset_id": output_dataset_id,
            "table_id": output_table_id,
        }
    
        # Convert quasi id list to Protobuf type
        def map_fields(field: str) -> dict:
            return {"name": field}
    
        #  Configure column names of quasi-identifiers to analyze
        quasi_ids = map(map_fields, quasi_ids)
    
        # Tell the API where to send a notification when the job is complete.
        actions = [{"save_findings": {"output_config": {"table": dest_table}}}]
    
        # Configure the privacy metric to compute for re-identification risk analysis.
        # Specify the unique identifier in the source table for the k-anonymity analysis.
        privacy_metric = {
            "k_anonymity_config": {
                "entity_id": {"field": {"name": entity_id}},
                "quasi_ids": quasi_ids,
            }
        }
    
        # Configure risk analysis job.
        risk_job = {
            "privacy_metric": privacy_metric,
            "source_table": source_table,
            "actions": actions,
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call API to start risk analysis job.
        response = dlp.create_dlp_job(
            request={
                "parent": parent,
                "risk_job": risk_job,
            }
        )
        job_name = response.name
        print(f"Inspection Job started : {job_name}")
    
        # Waiting for a maximum of 15 minutes for the job to be completed.
        job = dlp.get_dlp_job(request={"name": job_name})
        no_of_attempts = 30
        while no_of_attempts > 0:
            # Check if the job has completed
            if job.state == google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).DONE:
                break
            if job.state == google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).FAILED:
                print("Job Failed, Please check the configuration.")
                return
    
            # Sleep for a short duration before checking the job status again
            time.sleep(30)
            no_of_attempts -= 1
    
            # Get the DLP job status
            job = dlp.get_dlp_job(request={"name": job_name})
    
        if job.state != google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).DONE:
            print("Job did not complete within 15 minutes.")
            return
    
        # Create helper function for unpacking values
        def get_values(obj: [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html).[Value](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Value.html)) -> str:
            return str(obj.string_value)
    
        # Print out the results.
        print(f"Job name: {job.name}")
        histogram_buckets = (
            job.risk_details.k_anonymity_result.equivalence_class_histogram_buckets
        )
        # Print bucket stats
        for i, bucket in enumerate(histogram_buckets):
            print(f"Bucket {i}:")
            if bucket.equivalence_class_size_lower_bound:
                print(
                    f"Bucket size range: [{bucket.equivalence_class_size_lower_bound}, "
                    f"{bucket.equivalence_class_size_upper_bound}]"
                )
                for value_bucket in bucket.bucket_values:
                    print(
                        f"Quasi-ID values: {get_values(value_bucket.quasi_ids_values[0])}"
                    )
                    print(f"Class size: {value_bucket.equivalence_class_size}")
            else:
                print("No findings.")
    
    

## What's next

  * Learn how to calculate the [_l_ -diversity](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-l-diversity) value for a dataset.
  * Learn how to calculate the [_k_ -map](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-map) value for a dataset.
  * Learn how to calculate the [_δ_ -presence](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-d-presence) value for a dataset.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
