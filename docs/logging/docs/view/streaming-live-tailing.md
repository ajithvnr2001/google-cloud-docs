---
url: https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing/
title: Streaming and live tailing log entries \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:30.160053+00:00
---

# Streaming and live tailing log entries  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Streaming and live tailing log entries Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view your log entries in real time by streaming and live tailing. Streaming logs lets you view log entries in real time and is available in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). Live tailing lets you view log entries in real time and is available as the gcloud CLI command [`gcloud alpha logging tail`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/tail) and as the Cloud Logging API method [`entries.tail`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/tail).

When you view and analyze your logs using the Logs Explorer, [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read), or the API method [`entries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list), you're viewing log entries that Cloud Logging has stored. When you stream or live tail log entries, you're viewing log entries as your applications write them to the Cloud Logging API.

**Note:** If your data is managed through an [Assured Workloads environment](https://docs.cloud.google.com/assured-workloads/docs/key-concepts), then this feature might be impacted or restricted. For information, see [Restrictions and limitations in Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/eu-sovereign-controls-restrictions-limitations#features_logging).

## Stream logs in the Logs Explorer

In the Logs Explorer, you can view your logs data in real time using **Stream logs**. When you use **Stream logs** , you can add a query to stream only those logs that match the query. To stream logs, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **Query** field, enter a query and then click **Stream logs**.

As Logging writes the logs data, only logs that match the query are shown in the **Query results** pane. If a query isn't provided, then Logging shows the recently stored log entries. Logs continue streaming until you select the scroll bar on the logs panel. When streaming has stopped, a **Restart streaming** button is shown.

For information about queries, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).




## Use live tailing in the Google Cloud CLI

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Live tailing lets you view your log entries in real time as Cloud Logging writes them, by using either the Google Cloud CLI or the Cloud Logging API.

Live tailing isn't supported for log buckets with [field-level access controls](https://docs.cloud.google.com/logging/docs/field-level-acl), however you can [stream logs](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing#streaming) for those buckets in the Logs Explorer.

For information on the API method for live tailing, see the [entries.tail](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/tail) method.

### Installing `gcloud alpha logging tail`

To use `gcloud alpha logging tail`, you need to have Python 3 and the `grpcio` Python package installed.

For instructions on how to install Python, see the [Python page](https://www.python.org/downloads/). For instructions on how to install the Python package manager, `pip`, that is needed to install the `grpcio` package, see [The Python Package Installer page](https://pip.pypa.io/en/stable/).

Complete the following steps to install `gcloud alpha logging tail`:

  1. Verify that you have the Google Cloud CLI installed. For instructions on how to install the Google Cloud CLI, see [Installing Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  2. Verify that you're using version 302.0.0 or greater of the gcloud CLI.
         
         gcloud version
         

For instructions on updating the gcloud CLI, see [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update).

  3. Install the gcloud CLI alpha components:
         
         gcloud components install alpha
         

  4. **For MacOS, Linux, and Cloud Shell users** :

     1. Install gRPC client libraries:
            
            sudo pip3 install grpcio
            

     2. Set the environment variable `CLOUDSDK_PYTHON_SITEPACKAGES` to any value:
            
            export CLOUDSDK_PYTHON_SITEPACKAGES=1
            

**Note:** By default, the Google Cloud CLI ignores Python libraries installed on your local system. To allow the Google Cloud CLI to use the `grpcio` library, you need to enable site packages. To enable site packages, set the `CLOUDSDK_PYTHON_SITEPACKAGES` environment variable to `1`. With site packages enabled, the gcloud CLI can use extra libraries outside of the `google-cloud-sdk/lib` directory.
  5. Use the following commands to set your Google Cloud project ID and to authenticate:
         
         gcloud config set project PROJECT_ID
         gcloud auth login
         

To get the project ID, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  6. Verify that `gcloud alpha logging tail` is installed by running the following command:
         
         gcloud alpha logging tail
         

The command displays the following message:

`Initializing tail session.`

You are now viewing the log entries for your Google Cloud project as Logging writes them.

![Log entries during a live-tail session.](https://docs.cloud.google.com/static/logging/docs/images/live-tail.png)




For more information on using live tailing, see the [`gcloud alpha logging tail` reference guide](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/tail).

### Buffering and ordering

Because Logging can receive log entries out of chronological order, live tailing provides a buffer-window setting so you can balance the tradeoff between viewing the log entries as they are being written and viewing them in ascending order. You can set the buffer window between `0` and `60` seconds.

Note the following characteristics of the buffer window:

  * The default buffer window is two seconds.

  * Logging delays writing the log entries to log buckets for the duration of the buffer window.

  * If a log entry is written outside of the buffer window, then Logging returns the log entries as they are received.




When configuring the buffer window, you make a tradeoff between viewing logs as they are written and viewing the entries out of order.

Buffer window | Tradeoff  
---|---  
`0` seconds | Newest log entries returned, but with more likelihood of them being out of order.  
`60` seconds | A delay of 60 seconds before seeing the entries returned, but most of the logs are returned in ascending order.  
  
### Limits and quotas

The following table lists the limits and quotas for live tailing: 

Limits and quotas | Value  
---|---  
Entries returned per minute | 60,000  
If more than 60,000 entries match a filter, then Logging returns the count of entries in the response.   
Open live-tailing sessions per Google Cloud project | 10  
  
### Client limitations

For a Google Cloud project that writes lots of entries quickly, your client might be unable to consume them as quickly as they're being written. In this case, Logging limits the total number of entries sent, prioritizing the most recent entries. At the end of the tail session, Logging returns the number of entries that were not displayed due to the limits of the client.

## Use live tailing with client libraries

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Live tailing lets you view your log entries in real time as Cloud Logging writes them. For information on the API method for live tailing, see the [entries.tail](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/tail) method.

Live tailing isn't supported for log buckets with [field-level access controls](https://docs.cloud.google.com/logging/docs/field-level-acl), however you can [stream logs](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing#streaming) for those buckets in the Logs Explorer.

This sample demonstrates live tailing log entries of a given logger.

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

### Node.js

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {Logging} = require('[@google-cloud/logging](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest/overview.html)');
    const logging = new [Logging](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest/logging/logging.html)();
    
    /**
     * TODO(developer): Replace logName with the name of your log.
     */
    const log = logging.log(logName);
    console.log('running tail log entries test');
    
    const stream = log
      .tailEntries({
        filter: 'timestamp > "2021-01-01T23:00:00Z"',
      })
      .on('error', console.error)
      .on('[data](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest/logging/entry.html)', resp => {
        console.log(resp.entries);
        console.log(resp.suppressionInfo);
        // If you anticipate many results, you can end a stream early to prevent
        // unnecessary processing and API requests.
        [stream](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/logging-bunyan/loggingbunyan.html).end();
      })
      .on('end', () => {
        console.log('log entry stream has ended');
      });
    
    // Note: to get all project logs, invoke logging.tailEntries

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
