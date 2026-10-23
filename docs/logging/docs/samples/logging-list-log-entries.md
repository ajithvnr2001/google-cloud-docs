---
url: https://docs.cloud.google.com/logging/docs/samples/logging-list-log-entries/
title: List log entries \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:52.016324+00:00
---

# List log entries  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-list-log-entries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  List log entries Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list log entries.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [View and write Cloud Run function logs](https://docs.cloud.google.com/functions/1stgendocs/monitoring/logging)



## Code sample

### C#

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private void ListLogEntries(string logId)
    {
        var client = LoggingServiceV2Client.Create();
        LogName logName = new LogName(s_projectId, logId);
        ProjectName projectName = new ProjectName(s_projectId);
        var results = client.ListLogEntries(Enumerable.Repeat(projectName, 1), $"logName={logName.ToString()}",
            "timestamp desc", callSettings: _retryAWhile);
        foreach (var row in results)
        {
            Console.WriteLine($"{row.TextPayload.Trim()}");
        }
    }
    

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"time"
    
    	"cloud.google.com/go/logging"
    	"cloud.google.com/go/logging/logadmin"
    	"google.golang.org/api/iterator"
    )
    
    func getEntries(projectID string) ([]*logging.[Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Entry), error) {
    	ctx := context.Background()
    	adminClient, err := logadmin.NewClient(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Failed to create logadmin client: %v", err)
    	}
    	defer adminClient.Close()
    
    	var entries []*logging.[Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Entry)
    	const name = "log-example"
    	lastHour := time.Now().Add(-1 * time.Hour).Format(time.RFC3339)
    
    	iter := adminClient.Entries(ctx,
    		// Only get entries from the "log-example" log within the last hour.
    		logadmin.Filter(fmt.Sprintf(`logName = "projects/%s/logs/%s" AND timestamp > "%s"`, projectID, name, lastHour)),
    		// Get most recent entries first.
    		logadmin.NewestFirst(),
    	)
    
    	// Fetch the most recent 20 entries.
    	for len(entries) < 20 {
    		entry, err := iter.Next()
    		if err == iterator.Done {
    			return entries, nil
    		}
    		if err != nil {
    			return nil, err
    		}
    		entries = append(entries, entry)
    	}
    	return entries, nil
    }
    

### Java

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.logging.[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html).[EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption.html);
    import com.google.cloud.logging.[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html);
    import java.text.DateFormat;
    import java.text.SimpleDateFormat;
    import java.util.Calendar;
    import java.util.TimeZone;
    
    public class ListLogEntries {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace the variable value with valid log name before running the sample
        // or provide it as an argument.
        String logName = args.length > 0 ? args[0] : "test-log";
    
        try ([Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) logging = [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html).[getDefaultInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html#com_google_cloud_logging_LoggingOptions_getDefaultInstance__)().getService()) {
    
          // When composing a filter, using indexed fields, such as timestamp, resource.type, logName
          // and
          // others can help accelerate the results
          // Full list of indexed fields here:
          // https://cloud.google.com/logging/docs/view/advanced-queries#finding-quickly
          // This sample restrict the results to only last minute to minimize number of API calls
          Calendar calendar = Calendar.getInstance(TimeZone.getTimeZone("UTC"));
          calendar.add(Calendar.MINUTE, -1);
          DateFormat rfc3339 = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
          String logFilter =
              "logName=projects/"
                  + logging.[getOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.testing.RemoteLoggingHelper.html#com_google_cloud_logging_testing_RemoteLoggingHelper_getOptions__)().getProjectId()
                  + "/logs/"
                  + logName
                  + " AND timestamp>=\""
                  + rfc3339.format(calendar.getTime())
                  + "\"";
    
          // List all log entries
          Page<LogEntry> entries = logging.listLogEntries([EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption.html).filter(logFilter));
          while (entries != null) {
            for ([LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html) logEntry : entries.iterateAll()) {
              System.out.println(logEntry);
            }
            entries = entries.getNextPage();
          }
        }
      }
    }

### PHP

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Logging\LoggingClient;
    
    /**
     * Print the timestamp and entry for the project and logger.
     *
     * @param string $projectId The Google project ID.
     * @param string $loggerName The name of the logger.
     */
    function list_entries($projectId, $loggerName)
    {
        $logging = new LoggingClient(['projectId' => $projectId]);
        $loggerFullName = sprintf('projects/%s/logs/%s', $projectId, $loggerName);
        $oneDayAgo = date(\DateTime::RFC3339, strtotime('-24 hours'));
        $filter = sprintf(
            'logName = "%s" AND timestamp >= "%s"',
            $loggerFullName,
            $oneDayAgo
        );
        $options = [
            'filter' => $filter,
        ];
        $entries = $logging->entries($options);
    
        // Print the entries
        foreach ($entries as $entry) {
            /* @var $entry \Google\Cloud\Logging\Entry */
            $entryInfo = $entry->info();
            if (isset($entryInfo['textPayload'])) {
                $entryText = $entryInfo['textPayload'];
            } else {
                $entryPayload = [];
                foreach ($entryInfo['jsonPayload'] as $key => $value) {
                    $entryPayload[] = "$key: $value";
                }
                $entryText = '{' . implode(', ', $entryPayload) . '}';
            }
            printf('%s : %s' . PHP_EOL, $entryInfo['timestamp'], $entryText);
        }
    }

### Python

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_entries(logger_name):
        """Lists the most recent entries for a given logger."""
        logging_client = logging.Client()
        logger = logging_client.logger(logger_name)
    
        print("Listing entries for logger {}:".format(logger.name))
    
        for entry in logger.list_entries():
            timestamp = entry.timestamp.isoformat()
            print("* {}: {}".format(timestamp, entry.payload))
    
    

### Ruby

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/logging"
    
    # log_name = "my_log_name"
    logging = Google::Cloud::[Logging](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html)
    entries = logging.entries filter: "logName:#{log_name}",
                              max:    1000,
                              order:  "timestamp desc"
    
    entries.each do |entry|
      puts "[#{entry.timestamp}] #{entry.log_name} #{entry.[payload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Entry.html).inspect}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
