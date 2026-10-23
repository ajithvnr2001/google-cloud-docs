---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-bigquery/
title: Inspect BigQuery for sensitive data \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:11.166299+00:00
---

# Inspect BigQuery for sensitive data  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-bigquery/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Inspect BigQuery for sensitive data Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates finding sensitive data that is stored in BigQuery.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Inspect Google Cloud storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Collections.Generic;
    using System.Threading;
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    
    public class InspectBigQuery
    {
        public static object Inspect(
            string projectId,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood,
            int maxFindings,
            bool includeQuote,
            IEnumerable<FieldId> identifyingFields,
            IEnumerable<InfoType> infoTypes,
            IEnumerable<CustomInfoType> customInfoTypes,
            string datasetId,
            string tableId)
        {
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
                {
                    BigQueryOptions = new [BigQueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions.html)
                    {
                        TableReference = new Google.Cloud.Dlp.V2.BigQueryTable
                        {
                            ProjectId = projectId,
                            DatasetId = datasetId,
                            TableId = tableId,
                        },
                        IdentifyingFields =
                            {
                                identifyingFields
                            }
                    },
    
                    TimespanConfig = new StorageConfig.Types.TimespanConfig
                    {
                        StartTime = [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html).[FromDateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTime_System_DateTime_)(System.[DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.html).UtcNow.AddYears(-1)),
                        EndTime = [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html).[FromDateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTime_System_DateTime_)(System.[DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.html).UtcNow)
                    }
                },
    
                InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                {
                    InfoTypes = { infoTypes },
                    CustomInfoTypes = { customInfoTypes },
                    Limits = new [FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html)
                    {
                        MaxFindingsPerRequest = maxFindings
                    },
                    ExcludeInfoTypes = false,
                    IncludeQuote = includeQuote,
                    MinLikelihood = minLikelihood
                },
                Actions =
                    {
                        new Google.Cloud.Dlp.V2.Action
                        {
                            // Save results in BigQuery Table
                            SaveFindings = new Google.Cloud.Dlp.V2.Action.Types.SaveFindings
                            {
                                OutputConfig = new [OutputStorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OutputStorageConfig.html)
                                {
                                    Table = new Google.Cloud.Dlp.V2.BigQueryTable
                                    {
                                        ProjectId = projectId,
                                        DatasetId = datasetId,
                                        TableId = tableId
                                    }
                                }
                            },
                        }
                    }
            };
    
            // Issue Create Dlp Job Request
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                InspectJob = inspectJob,
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
            };
    
            // We need created job name
            var dlpJob = client.CreateDlpJob(request);
            var jobName = dlpJob.Name;
    
            // Make sure the job finishes before inspecting the results.
            // Alternatively, we can inspect results opportunistically, but
            // for testing purposes, we want consistent outcome
            var finishedJob = EnsureJobFinishes(projectId, jobName);
            var bigQueryClient = [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_)(projectId);
            var table = bigQueryClient.GetTable(datasetId, tableId);
    
            // Return only first page of 10 rows
            Console.WriteLine("DLP v2 Results:");
            var firstPage = table.ListRows(new [ListRowsOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.ListRowsOptions.html) { StartIndex = 0, PageSize = 10 });
            foreach (var item in firstPage)
            {
                Console.WriteLine($"\t {item[""]}");
            }
    
            return finishedJob;
        }
    
        private static DlpJob EnsureJobFinishes(string projectId, string jobName)
        {
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var request = new [GetDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDlpJobRequest.html)
            {
                DlpJobName = new [DlpJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.html)(projectId, jobName),
            };
    
            // Simple logic that gives the job 5*30 sec at most to complete - for testing purposes only
            var numOfAttempts = 5;
            do
            {
                var dlpJob = client.GetDlpJob(request);
                numOfAttempts--;
                if (dlpJob.State != [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types.html).[JobState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types.JobState.html).[Running](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types.JobState.html#Google_Cloud_Dlp_V2_DlpJob_Types_JobState_Running))
                {
                    return dlpJob;
                }
    
                Thread.Sleep(TimeSpan.FromSeconds(30));
            } while (numOfAttempts > 0);
    
            throw new InvalidOperationException("Job did not complete in time");
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
    
    // inspectBigquery searches for the given info types in the given Bigquery dataset table.
    func inspectBigquery(w io.Writer, projectID string, infoTypeNames []string, customDictionaries []string, customRegexes []string, pubSubTopic, pubSubSub, dataProject, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// infoTypeNames := []string{"US_SOCIAL_SECURITY_NUMBER"}
    	// customDictionaries := []string{...}
    	// customRegexes := []string{...}
    	// pubSubTopic := "dlp-risk-sample-topic"
    	// pubSubSub := "dlp-risk-sample-sub"
    	// dataProject := "my-data-project-ID"
    	// datasetID := "my_dataset"
    	// tableID := "mytable"
    
    	ctx := context.Background()
    
    	client, err := dlp.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    
    	// Convert the info type strings to a list of InfoTypes.
    	var infoTypes []*dlppb.InfoType
    	for _, it := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: it})
    	}
    	// Convert the custom dictionary word lists and custom regexes to a list of CustomInfoTypes.
    	var customInfoTypes []*dlppb.CustomInfoType
    	for idx, it := range customDictionaries {
    		customInfoTypes = append(customInfoTypes, &dlppb.CustomInfoType{
    			InfoType: &dlppb.InfoType{
    				Name: fmt.Sprintf("CUSTOM_DICTIONARY_%d", idx),
    			},
    			Type: &dlppb.CustomInfoType_Dictionary_{
    				Dictionary: &dlppb.CustomInfoType_Dictionary{
    					Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    						WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    							Words: strings.Split(it, ","),
    						},
    					},
    				},
    			},
    		})
    	}
    	for idx, it := range customRegexes {
    		customInfoTypes = append(customInfoTypes, &dlppb.CustomInfoType{
    			InfoType: &dlppb.InfoType{
    				Name: fmt.Sprintf("CUSTOM_REGEX_%d", idx),
    			},
    			Type: &dlppb.CustomInfoType_Regex_{
    				Regex: &dlppb.CustomInfoType_Regex{
    					Pattern: it,
    				},
    			},
    		})
    	}
    
    	// Create a PubSub Client used to listen for when the inspect job finishes.
    	pubsubClient, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer pubsubClient.Close()
    
    	// Create a PubSub subscription we can use to listen for messages.
    	// Create the Topic if it doesn't exist.
    	t := pubsubClient.Topic(pubSubTopic)
    	if exists, err := t.Exists(ctx); err != nil {
    		return fmt.Errorf("t.Exists: %w", err)
    	} else if !exists {
    		if t, err = pubsubClient.CreateTopic(ctx, pubSubTopic); err != nil {
    			return fmt.Errorf("CreateTopic: %w", err)
    		}
    	}
    
    	// Create the Subscription if it doesn't exist.
    	s := pubsubClient.Subscription(pubSubSub)
    	if exists, err := s.Exists(ctx); err != nil {
    		return fmt.Errorf("s.Exits: %w", err)
    	} else if !exists {
    		if s, err = pubsubClient.CreateSubscription(ctx, pubSubSub, pubsub.SubscriptionConfig{Topic: t}); err != nil {
    			return fmt.Errorf("CreateSubscription: %w", err)
    		}
    	}
    
    	// topic is the PubSub topic string where messages should be sent.
    	topic := "projects/" + projectID + "/topics/" + pubSubTopic
    
    	// Create a configured request.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: &dlppb.InspectJobConfig{
    				// StorageConfig describes where to find the data.
    				StorageConfig: &dlppb.StorageConfig{
    					Type: &dlppb.StorageConfig_BigQueryOptions{
    						BigQueryOptions: &dlppb.BigQueryOptions{
    							TableReference: &dlppb.BigQueryTable{
    								ProjectId: dataProject,
    								DatasetId: datasetID,
    								TableId:   tableID,
    							},
    						},
    					},
    				},
    				// InspectConfig describes what fields to look for.
    				InspectConfig: &dlppb.InspectConfig{
    					InfoTypes:       infoTypes,
    					CustomInfoTypes: customInfoTypes,
    					MinLikelihood:   dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    					Limits: &dlppb.InspectConfig_FindingLimits{
    						MaxFindingsPerRequest: 10,
    					},
    					IncludeQuote: true,
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
    	// Create the inspect job.
    	j, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateDlpJob: %w", err)
    	}
    	fmt.Fprintf(w, "Created job: %v\n", j.GetName())
    
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
    			fmt.Fprintf(w, "  Found %v instances of infoType %v\n", s.GetCount(), s.GetInfoType().GetName())
    		}
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
    import com.google.privacy.dlp.v2.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html);
    import com.google.privacy.dlp.v2.[BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class InspectBigQueryTable {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String bigQueryDatasetId = "your-bigquery-dataset-id";
        String bigQueryTableId = "your-bigquery-table-id";
        String topicId = "your-pubsub-topic-id";
        String subscriptionId = "your-pubsub-subscription-id";
        inspectBigQueryTable(projectId, bigQueryDatasetId, bigQueryTableId, topicId, subscriptionId);
      }
    
      // Inspects a BigQuery Table
      public static void inspectBigQueryTable(
          String projectId,
          String bigQueryDatasetId,
          String bigQueryTableId,
          String topicId,
          String subscriptionId)
          throws ExecutionException, InterruptedException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the BigQuery table to be inspected.
          [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html) tableReference =
              [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html).newBuilder()
                  .setProjectId(projectId)
                  .setDatasetId(bigQueryDatasetId)
                  .setTableId(bigQueryTableId)
                  .build();
    
          [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html) bigQueryOptions =
              [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html).newBuilder().setTableReference(tableReference).build();
    
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder().[setBigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setBigQueryOptions_com_google_privacy_dlp_v2_BigQueryOptions_)(bigQueryOptions).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes =
              Stream.of("PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          // Specify how the content should be inspected.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addAllInfoTypes(infoTypes).[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true).build();
    
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
    
    // The project ID the table is stored under
    // This may or (for public datasets) may not equal the calling project ID
    // const dataProjectId = 'my-project';
    
    // The ID of the dataset to inspect, e.g. 'my_dataset'
    // const datasetId = 'my_dataset';
    
    // The ID of the table to inspect, e.g. 'my_table'
    // const tableId = 'my_table';
    
    // The minimum likelihood required before returning a match
    // const minLikelihood = 'LIKELIHOOD_UNSPECIFIED';
    
    // The maximum number of findings to report per request (0 = server maximum)
    // const maxFindings = 0;
    
    // The infoTypes of information to match
    // const infoTypes = [{ name: 'PHONE_NUMBER' }, { name: 'EMAIL_ADDRESS' }, { name: 'CREDIT_CARD_NUMBER' }];
    
    // The customInfoTypes of information to match
    // const customInfoTypes = [{ infoType: { name: 'DICT_TYPE' }, dictionary: { wordList: { words: ['foo', 'bar', 'baz']}}},
    //   { infoType: { name: 'REGEX_TYPE' }, regex: {pattern: '\\(\\d{3}\\) \\d{3}-\\d{4}'}}];
    
    // The name of the Pub/Sub topic to notify once the job completes
    // TODO(developer): create a Pub/Sub topic to use for this
    // const topicId = 'MY-PUBSUB-TOPIC'
    
    // The name of the Pub/Sub subscription to use when listening for job
    // completion notifications
    // TODO(developer): create a Pub/Sub subscription to use for this
    // const subscriptionId = 'MY-PUBSUB-SUBSCRIPTION'
    
    async function inspectBigquery() {
      // Construct item to be inspected
      const storageItem = {
        bigQueryOptions: {
          tableReference: {
            projectId: dataProjectId,
            datasetId: datasetId,
            tableId: tableId,
          },
        },
      };
    
      // Construct request for creating an inspect job
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: {
          inspectConfig: {
            infoTypes: infoTypes,
            customInfoTypes: customInfoTypes,
            minLikelihood: minLikelihood,
            limits: {
              maxFindingsPerRequest: maxFindings,
            },
          },
          storageConfig: storageItem,
          actions: [
            {
              pubSub: {
                topic: `projects/${projectId}/topics/${topicId}`,
              },
            },
          ],
        },
      };
    
      // Run inspect-job creation request
      const [topicResponse] = await pubsub.topic(topicId).get();
      // Verify the Pub/Sub topic and listen for job notifications via an
      // existing subscription.
      const subscription = await topicResponse.subscription(subscriptionId);
      const [jobsResponse] = await dlp.createDlpJob(request);
      const jobName = jobsResponse.name;
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
      // Wait for DLP job to fully complete
      setTimeout(() => {
        console.log('Waiting for DLP job to fully complete');
      }, 500);
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
    
    await inspectBigquery();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishToPubSub;
    use Google\Cloud\Dlp\V2\BigQueryOptions;
    use Google\Cloud\Dlp\V2\BigQueryTable;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\StorageConfig;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Inspect a BigQuery table , using Pub/Sub for job status notifications.
     *
     * @param string $callingProjectId  The project ID to run the API call under
     * @param string $dataProjectId     The project ID containing the target Datastore
     * @param string $topicId           The name of the Pub/Sub topic to notify once the job completes
     * @param string $subscriptionId    The name of the Pub/Sub subscription to use when listening for job
     * @param string $datasetId         The ID of the dataset to inspect
     * @param string $tableId           The ID of the table to inspect
     * @param int    $maxFindings       (Optional) The maximum number of findings to report per request (0 = server maximum)
     */
    function inspect_bigquery(
        string $callingProjectId,
        string $dataProjectId,
        string $topicId,
        string $subscriptionId,
        string $datasetId,
        string $tableId,
        int $maxFindings = 0
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
        $pubsub = new PubSubClient();
        $topic = $pubsub->topic($topicId);
    
        // The infoTypes of information to match
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
        $creditCardNumberInfoType = (new InfoType())
            ->setName('CREDIT_CARD_NUMBER');
        $infoTypes = [$personNameInfoType, $creditCardNumberInfoType];
    
        // The minimum likelihood required before returning a match
        $minLikelihood = likelihood::LIKELIHOOD_UNSPECIFIED;
    
        // Specify finding limits
        $limits = (new FindingLimits())
            ->setMaxFindingsPerRequest($maxFindings);
    
        // Construct items to be inspected
        $bigqueryTable = (new BigQueryTable())
            ->setProjectId($dataProjectId)
            ->setDatasetId($datasetId)
            ->setTableId($tableId);
    
        $bigQueryOptions = (new BigQueryOptions())
            ->setTableReference($bigqueryTable);
    
        $storageConfig = (new StorageConfig())
            ->setBigQueryOptions($bigQueryOptions);
    
        // Construct the inspect config object
        $inspectConfig = (new InspectConfig())
            ->setMinLikelihood($minLikelihood)
            ->setLimits($limits)
            ->setInfoTypes($infoTypes);
    
        // Construct the action to run when job completes
        $pubSubAction = (new PublishToPubSub())
            ->setTopic($topic->name());
    
        $action = (new Action())
            ->setPubSub($pubSubAction);
    
        // Construct inspect job config to run
        $inspectJob = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Listen for job notifications via an existing topic/subscription.
        $subscription = $topic->subscription($subscriptionId);
    
        // Submit request
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJob);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        // Poll Pub/Sub using exponential backoff until job finishes
        // Consider using an asynchronous execution model such as Cloud Functions
        $attempt = 1;
        $startTime = time();
        do {
            foreach ($subscription->pull() as $message) {
                if (isset($message->attributes()['DlpJobName']) &&
                    $message->attributes()['DlpJobName'] === $job->getName()) {
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
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    print('No findings.' . PHP_EOL);
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
                print('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                print('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import threading
    from typing import List, Optional
    
    import google.cloud.dlp
    import google.cloud.pubsub
    
    
    def inspect_bigquery(
        project: str,
        bigquery_project: str,
        dataset_id: str,
        table_id: str,
        topic_id: str,
        subscription_id: str,
        info_types: List[str],
        custom_dictionaries: List[str] = None,
        custom_regexes: List[str] = None,
        min_likelihood: Optional[int] = None,
        max_findings: Optional[int] = None,
        timeout: int = 500,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze BigQuery data.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            bigquery_project: The Google Cloud project id of the target table.
            dataset_id: The id of the target BigQuery dataset.
            table_id: The id of the target BigQuery table.
            topic_id: The id of the Cloud Pub/Sub topic to which the API will
                broadcast job completion. The topic must already exist.
            subscription_id: The id of the Cloud Pub/Sub subscription to listen on
                while waiting for job completion. The subscription must already
                exist and be subscribed to the topic.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            timeout: The number of seconds to wait for a response from the API.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries (protos are also accepted).
        if not info_types:
            info_types = ["FIRST_NAME", "LAST_NAME", "EMAIL_ADDRESS"]
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Prepare custom_info_types by parsing the dictionary word lists and
        # regex patterns.
        if custom_dictionaries is None:
            custom_dictionaries = []
        dictionaries = [
            {
                "info_type": {"name": f"CUSTOM_DICTIONARY_{i}"},
                "dictionary": {"word_list": {"words": custom_dict.split(",")}},
            }
            for i, custom_dict in enumerate(custom_dictionaries)
        ]
        if custom_regexes is None:
            custom_regexes = []
        regexes = [
            {
                "info_type": {"name": f"CUSTOM_REGEX_{i}"},
                "regex": {"pattern": custom_regex},
            }
            for i, custom_regex in enumerate(custom_regexes)
        ]
        custom_info_types = dictionaries + regexes
    
        # Construct the configuration dictionary. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": info_types,
            "custom_info_types": custom_info_types,
            "min_likelihood": min_likelihood,
            "limits": {"max_findings_per_request": max_findings},
        }
    
        # Construct a storage_config containing the target Bigquery info.
        storage_config = {
            "big_query_options": {
                "table_reference": {
                    "project_id": bigquery_project,
                    "dataset_id": dataset_id,
                    "table_id": table_id,
                }
            }
        }
    
        # Convert the project id into full resource ids.
        topic = google.cloud.pubsub.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html).topic_path(project, topic_id)
        parent = f"projects/{project}/locations/global"
    
        # Tell the API where to send a notification when the job is complete.
        actions = [{"pub_sub": {"topic": topic}}]
    
        # Construct the inspect_job, which defines the entire inspect content task.
        inspect_job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
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
    
        def callback(message: google.cloud.pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
            try:
                if message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes)["DlpJobName"] == operation.name:
                    # This is the message we're looking for, so acknowledge it.
                    message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
                    # Now that the job is done, fetch the results and print them.
                    job = dlp.get_dlp_job(request={"name": operation.name})
                    print(f"Job name: {job.name}")
                    if job.inspect_details.result.info_type_stats:
                        for finding in job.inspect_details.result.info_type_stats:
                            print(
                                "Info type: {}; Count: {}".format(
                                    finding.info_type.name, finding.count
                                )
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
