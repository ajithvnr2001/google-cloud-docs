---
url: https://docs.cloud.google.com/logging/docs/samples/logging-tail-log-entries/
title: Tail log entries \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:57:12.270599+00:00
---

# Tail log entries  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-tail-log-entries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  Tail log entries Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to tail live log entries.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Streaming and live tailing log entries](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing)



## Code sample

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	logging "cloud.google.com/go/logging/apiv2"
    	"cloud.google.com/go/logging/apiv2/loggingpb"
    )
    
    // tailLogs creates a channel to stream log entries that were recently ingested for a project
    func tailLogs(projectID string) error {
    	// projectID := "your_project_id"
    
    	ctx := context.Background()
    	client, err := logging.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/apiv2.html#cloud_google_com_go_logging_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient error: %w", err)
    	}
    	defer client.Close()
    
    	stream, err := client.TailLogEntries(ctx)
    	if err != nil {
    		return fmt.Errorf("TailLogEntries error: %w", err)
    	}
    	defer stream.CloseSend()
    
    	req := &loggingpb.TailLogEntriesRequest{
    		ResourceNames: []string{
    			"projects/" + projectID,
    		},
    	}
    	if err := stream.Send(req); err != nil {
    		return fmt.Errorf("stream.Send error: %w", err)
    	}
    
    	// read and print two or more streamed log entries
    	for counter := 0; counter < 2; {
    		resp, err := stream.Recv()
    		if err == io.EOF {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("stream.Recv error: %w", err)
    		}
    		fmt.Printf("received:\n%v\n", resp)
    		if resp.Entries != nil {
    			counter += len(resp.Entries)
    		}
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.logging.[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html);
    import com.google.cloud.logging.[LogEntryServerStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntryServerStream.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html).[TailOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.TailOption.html);
    import com.google.cloud.logging.[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html);
    
    public class TailLogEntries {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Optionally provide the logname as an argument.
        String logName = args.length > 0 ? args[0] : "";
    
        [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html) options = [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html).[getDefaultInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html#com_google_cloud_logging_LoggingOptions_getDefaultInstance__)();
        try ([Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) logging = options.getService()) {
    
          // Optionally compose a filter to tail log entries only from specific log
          [LogEntryServerStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntryServerStream.html) stream;
    
          if (logName != "") {
            stream =
                logging.[tailLogEntries](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html#com_google_cloud_logging_Logging_tailLogEntries_com_google_cloud_logging_Logging_TailOption____)(
                    [TailOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.TailOption.html).filter(
                        "logName=projects/" + options.getProjectId() + "/logs/" + logName));
          } else {
            stream = logging.[tailLogEntries](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html#com_google_cloud_logging_Logging_tailLogEntries_com_google_cloud_logging_Logging_TailOption____)();
          }
          System.out.println("start streaming..");
          for ([LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html) log : stream) {
            System.out.println(log);
            // cancel infinite streaming after receiving first entry
            stream.[cancel](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntryServerStream.html#com_google_cloud_logging_LogEntryServerStream_cancel__)();
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
