---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-replace-channels/
title: Replace notification channels \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:05:35.068709+00:00
---

# Replace notification channels  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-replace-channels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Replace notification channels Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to replace notification channels across alerting policies.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void ReplaceChannels(string projectId, string alertPolicyId,
        IEnumerable<string> channelIds)
    {
        var alertClient = AlertPolicyServiceClient.Create();
        var policy = new AlertPolicy()
        {
            Name = new AlertPolicyName(projectId, alertPolicyId).ToString()
        };
        foreach (string channelId in channelIds)
        {
            policy.NotificationChannels.Add(
                new NotificationChannelName(projectId, channelId)
                .ToString());
        }
        var response = alertClient.UpdateAlertPolicy(
            new FieldMask { Paths = { "notification_channels" } }, policy);
        Console.WriteLine("Updated {0}.", response.Name);
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // replaceChannels replaces the notification channels in the alert policy
    // with channelIDs.
    func replaceChannels(w io.Writer, projectID, alertPolicyID string, channelIDs []string) error {
    	ctx := context.Background()
    
    	client, err := monitoring.NewAlertPolicyClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	policy := &monitoringpb.AlertPolicy{
    		Name: "projects/" + projectID + "/alertPolicies/" + alertPolicyID,
    	}
    	for _, c := range channelIDs {
    		c = "projects/" + projectID + "/notificationChannels/" + c
    		policy.NotificationChannels = append(policy.NotificationChannels, c)
    	}
    	req := &monitoringpb.UpdateAlertPolicyRequest{
    		AlertPolicy: policy,
    		UpdateMask: &fieldmask.FieldMask{
    			Paths: []string{"notification_channels"},
    		},
    	}
    	if _, err := client.UpdateAlertPolicy(ctx, req); err != nil {
    		return fmt.Errorf("UpdateAlertPolicy: %w", err)
    	}
    	fmt.Fprintf(w, "Successfully replaced channels.")
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void replaceChannels(String projectId, String alertPolicyId, String[] channelIds)
        throws IOException {
      AlertPolicy.Builder policyBuilder =
          AlertPolicy.newBuilder().setName(AlertPolicyName.of(projectId, alertPolicyId).toString());
      for (String channelId : channelIds) {
        policyBuilder.addNotificationChannels(
            NotificationChannelName.of(projectId, channelId).toString());
      }
      try (AlertPolicyServiceClient client = AlertPolicyServiceClient.create()) {
        AlertPolicy result =
            client.updateAlertPolicy(
                FieldMask.newBuilder().addPaths("notification_channels").build(),
                policyBuilder.build());
        System.out.println(String.format("Updated %s", result.getName()));
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates clients
    const alertClient = new monitoring.[AlertPolicyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    const notificationClient = new monitoring.[NotificationChannelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function replaceChannels() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'YOUR_PROJECT_ID';
      // const alertPolicyId = '123456789012314';
      // const channelIds = [
      //   'channel-1',
      //   'channel-2',
      //   'channel-3',
      // ];
    
      const notificationChannels = channelIds.map(id =>
        notificationClient.projectNotificationChannelPath(projectId, id)
      );
    
      for (const channel of notificationChannels) {
        const updateChannelRequest = {
          updateMask: {
            paths: ['enabled'],
          },
          notificationChannel: {
            name: channel,
            enabled: {
              value: true,
            },
          },
        };
        try {
          await notificationClient.updateNotificationChannel(
            updateChannelRequest
          );
        } catch (err) {
          const createChannelRequest = {
            notificationChannel: {
              name: channel,
              notificationChannel: {
                type: 'email',
              },
            },
          };
          const newChannel =
            await notificationClient.createNotificationChannel(
              createChannelRequest
            );
          notificationChannels.push(newChannel);
        }
      }
    
      const updateAlertPolicyRequest = {
        updateMask: {
          paths: ['notification_channels'],
        },
        alertPolicy: {
          name: alertClient.projectAlertPolicyPath(projectId, alertPolicyId),
          notificationChannels: notificationChannels,
        },
      };
      const [alertPolicy] = await alertClient.updateAlertPolicy(
        updateAlertPolicyRequest
      );
      console.log(`Updated ${alertPolicy.name}.`);
    }
    replaceChannels();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\AlertPolicy;
    use Google\Cloud\Monitoring\V3\Client\AlertPolicyServiceClient;
    use Google\Cloud\Monitoring\V3\Client\NotificationChannelServiceClient;
    use Google\Cloud\Monitoring\V3\UpdateAlertPolicyRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $projectId Your project ID
     * @param string $alertPolicyId Your alert policy id ID
     * @param string[] $channelIds array of channel IDs
     */
    function alert_replace_channels(string $projectId, string $alertPolicyId, array $channelIds): void
    {
        $alertClient = new AlertPolicyServiceClient([
            'projectId' => $projectId,
        ]);
    
        $channelClient = new NotificationChannelServiceClient([
            'projectId' => $projectId,
        ]);
        $policy = new AlertPolicy();
        $policy->setName($alertClient->alertPolicyName($projectId, $alertPolicyId));
    
        $newChannels = [];
        foreach ($channelIds as $channelId) {
            $newChannels[] = $channelClient->notificationChannelName($projectId, $channelId);
        }
        $policy->setNotificationChannels($newChannels);
        $mask = new FieldMask();
        $mask->setPaths(['notification_channels']);
        $updateAlertPolicyRequest = (new UpdateAlertPolicyRequest())
            ->setAlertPolicy($policy)
            ->setUpdateMask($mask);
        $updatedPolicy = $alertClient->updateAlertPolicy($updateAlertPolicyRequest);
        printf('Updated %s' . PHP_EOL, $updatedPolicy->getName());
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def replace_notification_channels(project_name, alert_policy_id, channel_ids):
        """Replace notification channel of an alert.
    
        Arguments:
            project_name (str): The Google Cloud Project to use. The project name
                must be in the format - 'projects/<PROJECT_NAME>'.
            alert_policy_id (str): The ID of the alert policy whose notification
                channels are to be replaced.
            channel_ids (str): ID of notification channel to be added as channel
                for the given alert policy.
        """
    
        _, project_id = project_name.split("/")
        alert_client = monitoring_v3.AlertPolicyServiceClient()
        channel_client = monitoring_v3.NotificationChannelServiceClient()
        policy = monitoring_v3.AlertPolicy()
        policy.name = alert_client.alert_policy_path(project_id, alert_policy_id)
    
        for channel_id in channel_ids:
            policy.notification_channels.append(
                channel_client.notification_channel_path(project_id, channel_id)
            )
    
        mask = field_mask.FieldMask()
        mask.paths.append("notification_channels")
        updated_policy = alert_client.update_alert_policy(
            alert_policy=policy, update_mask=mask
        )
        print("Updated", updated_policy.name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
