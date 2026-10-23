---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-list-channels/
title: List notification channels \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:18.302902+00:00
---

# List notification channels  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-list-channels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  List notification channels Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list notification channels.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage notification channels by API](https://docs.cloud.google.com/monitoring/alerts/using-channels-api)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void ListNotificationChannels(string projectId)
    {
        var client = NotificationChannelServiceClient.Create();
        var response = client.ListNotificationChannels(new ProjectName(projectId));
        foreach (NotificationChannel channel in response)
        {
            Console.WriteLine(channel.Name);
            if (channel.DisplayName != null)
            {
                Console.WriteLine(channel.DisplayName);
            }
            Console.WriteLine();
        }
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    channelClient, err := monitoring.NewNotificationChannelClient(ctx)
    if err != nil {
    	return err
    }
    defer channelClient.Close()
    channelReq := &monitoringpb.ListNotificationChannelsRequest{
    	Name: "projects/" + projectID,
    	// Filter:  "", // See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering.
    	// OrderBy: "", // See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering.
    }
    channelIt := channelClient.ListNotificationChannels(ctx, channelReq)
    for {
    	resp, err := channelIt.Next()
    	if err == iterator.Done {
    		break
    	}
    	if err != nil {
    		return err
    	}
    	b.Channels = append(b.Channels, &channel{resp})
    }

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static List<NotificationChannel> getNotificationChannels(String projectId)
        throws IOException {
      List<NotificationChannel> notificationChannels = Lists.newArrayList();
      try (NotificationChannelServiceClient client = NotificationChannelServiceClient.create()) {
        ListNotificationChannelsPagedResponse listNotificationChannelsResponse =
            client.listNotificationChannels(ProjectName.of(projectId));
        for (NotificationChannel channel : listNotificationChannelsResponse.iterateAll()) {
          notificationChannels.add(channel);
        }
      }
      return notificationChannels;
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
    use Google\Cloud\Monitoring\V3\ListNotificationChannelsRequest;
    
    /**
     * @param string $projectId Your project ID
     */
    function alert_list_channels($projectId)
    {
        $projectName = 'projects/' . $projectId;
        $channelClient = new NotificationChannelServiceClient([
            'projectId' => $projectId,
        ]);
        $listNotificationChannelsRequest = (new ListNotificationChannelsRequest())
            ->setName($projectName);
    
        $channels = $channelClient->listNotificationChannels($listNotificationChannelsRequest);
        foreach ($channels->iterateAllElements() as $channel) {
            printf('Name: %s (%s)' . PHP_EOL, $channel->getDisplayName(), $channel->getName());
        }
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_notification_channels(project_name):
        """List alert notification channels in a project.
    
        Arguments:
            project_name (str): The Google Cloud Project to use. The project name
                must be in the format - 'projects/<PROJECT_NAME>'.
        """
    
        client = monitoring_v3.NotificationChannelServiceClient()
        channels = client.list_notification_channels(name=project_name)
        print(
            tabulate.tabulate(
                [(channel.name, channel.display_name) for channel in channels],
                ("name", "display_name"),
            )
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
