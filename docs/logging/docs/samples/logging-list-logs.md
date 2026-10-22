---
url: https://docs.cloud.google.com/logging/docs/samples/logging-list-logs/
title: List logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:47.363985+00:00
---

# List logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-list-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  List logs Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list the names of available Logs.

## Code sample

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/logging/logadmin"
    	"google.golang.org/api/iterator"
    )
    
    // listLogs lists all available logs in the project.
    func listLogs(w io.Writer, projectID string) error {
    	ctx := context.Background()
    
    	client, err := logadmin.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return err
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_Close)()
    
    	iter := client.[Logs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_Logs)(ctx)
    	for {
    		log, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("List logs failed: %w", err)
    		}
    		fmt.Fprintf(w, "%s\n", log)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html);
    import com.google.cloud.logging.[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html);
    
    public class ListLogs {
    
      public static void main(String... args) throws Exception {
    
        try ([Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) logging = [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html).[getDefaultInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html#com_google_cloud_logging_LoggingOptions_getDefaultInstance__)().getService()) {
    
          // List all log names
          Page<String> logNames = logging.listLogs();
          while (logNames != null) {
            for (String logName : logNames.iterateAll()) {
              System.out.println(logName);
            }
            logNames = logNames.getNextPage();
          }
        }
      }
    }

### Python

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    from google.cloud import logging_v2
    
    
    def list_logs(project_id: str) -> List[str]:
        """Lists all logs in a project.
    
        Args:
            project_id: the ID of the project
    
        Returns:
            A list of log names.
        """
        client = logging_v2.services.logging_service_v2.LoggingServiceV2Client()
        request = logging_v2.types.ListLogsRequest(
            parent=f"projects/{project_id}",
        )
    
        logs = client.list_logs(request=request)
        for log in logs:
            print(log)
    
        return logs
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
