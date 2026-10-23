---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-delete-channel/
title: Delete a notification channel \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:14.882744+00:00
---

# Delete a notification channel  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-delete-channel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Delete a notification channel Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to delete a notification channel.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage notification channels by API](https://docs.cloud.google.com/monitoring/alerts/using-channels-api)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Monitoring.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.html);
    using System;
    
    partial class AlertSnippets
    {
        public void DeleteNotificationChannel(
            string channelName = "projects/your-project-id/notificationChannels/123")
        {
            var client = [NotificationChannelServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannelServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannelServiceClient.html#Google_Cloud_Monitoring_V3_NotificationChannelServiceClient_Create)();
            client.DeleteNotificationChannel(
                name: [NotificationChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannelName.html).[Parse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannelName.html#Google_Cloud_Monitoring_V3_NotificationChannelName_Parse_System_String_)(channelName),
                force: true);
            Console.WriteLine("Deleted {0}.", channelName);
        }
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	monitoring "cloud.google.com/go/monitoring/apiv3"
    	"cloud.google.com/go/monitoring/apiv3/v2/monitoringpb"
    )
    
    // deleteChannel deletes the given channel. channelName should be of the form
    // "projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]".
    func deleteChannel(w io.Writer, channelName string) error {
    	ctx := context.Background()
    
    	client, err := monitoring.NewNotificationChannelClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	req := &monitoringpb.DeleteNotificationChannelRequest{
    		Name: channelName,
    	}
    
    	if err := client.DeleteNotificationChannel(ctx, req); err != nil {
    		return fmt.Errorf("DeleteNotificationChannel: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted channel %q", channelName)
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void deleteNotificationChannel(String channelName) throws IOException {
      String projectId = System.getProperty("projectId");
      try (NotificationChannelServiceClient client = NotificationChannelServiceClient.create()) {
        NotificationChannelName name = NotificationChannelName.of(projectId, channelName);
        client.deleteNotificationChannel(channelName, false);
        System.out.println("Deleted notification channel " + channelName);
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[NotificationChannelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function deleteChannels() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'YOUR_PROJECT_ID';
      // const filter = 'A filter for selecting policies, e.g. description:"cloud"';
    
      const request = {
        name: client.projectPath(projectId),
        filter,
      };
      const channels = await client.listNotificationChannels(request);
      console.log(channels);
      for (const channel of channels[0]) {
        console.log(`Deleting channel ${channel.displayName}`);
        try {
          await client.deleteNotificationChannel({
            name: channel.name,
          });
        } catch (err) {
          // ignore error
        }
      }
    }
    deleteChannels();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\NotificationChannelServiceClient;
    use Google\Cloud\Monitoring\V3\DeleteNotificationChannelRequest;
    
    /**
     * @param string $projectId Your project ID
     * @param string $channelId
     */
    function alert_delete_channel(string $projectId, string $channelId): void
    {
        $channelClient = new NotificationChannelServiceClient([
            'projectId' => $projectId,
        ]);
        $channelName = $channelClient->notificationChannelName($projectId, $channelId);
        $deleteNotificationChannelRequest = (new DeleteNotificationChannelRequest())
            ->setName($channelName);
    
        $channelClient->deleteNotificationChannel($deleteNotificationChannelRequest);
        printf('Deleted notification channel %s' . PHP_EOL, $channelName);
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_notification_channels(project_name, channel_ids, force=None):
        """Delete alert notification channels.
    
        Arguments:
            project_name (str): The Google Cloud Project to use. The project name
                must be in the format - 'projects/<PROJECT_NAME>'.
            channel_ids list(str): List of IDs of notification channels to delete.
            force (bool): If true, the notification channels are deleted regardless
                of its in use by alert policies. If false, channels that are still
                referenced by an existing alerting policy will fail to be deleted.
        """
    
        channel_client = monitoring_v3.NotificationChannelServiceClient()
        for channel_id in channel_ids:
            channel_name = "{}/notificationChannels/{}".format(project_name, channel_id)
            try:
                channel_client.delete_notification_channel(name=channel_name, force=force)
                print("Channel {} deleted".format(channel_name))
            except ValueError:
                print("The parameters are invalid")
            except Exception as e:
                print("API call failed: {}".format(e))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
