---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-update-channel/
title: Update a notification channel \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:29.913428+00:00
---

# Update a notification channel  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-update-channel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Update a notification channel Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to update a notification channel.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage notification channels by API](https://docs.cloud.google.com/monitoring/alerts/using-channels-api)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void RestorePolicies(string projectId, string filePath)
    {
        var policyClient = AlertPolicyServiceClient.Create();
        var channelClient = NotificationChannelServiceClient.Create();
        List<Exception> exceptions = new List<Exception>();
        var backup = JsonConvert.DeserializeObject<BackupRecord>(
            File.ReadAllText(filePath), new ProtoMessageConverter());
        var projectName = new ProjectName(projectId);
        bool isSameProject = projectId == backup.ProjectId;
        // When a channel is recreated, rather than updated, it will get
        // a new name.  We have to update the AlertPolicy with the new
        // name.  Track the names in this map.
        var channelNameMap = new Dictionary<string, string>();
        foreach (NotificationChannel channel in backup.Channels)
        {
            try
            {
                bool updated = false;
                Console.WriteLine("Updating channel.\n{0}",
                    channel.DisplayName);
                // This field is immutable and it is illegal to specify a
                // non-default value (UNVERIFIED or VERIFIED) in the
                // Create() or Update() operations.
                channel.VerificationStatus = NotificationChannel.Types
                    .VerificationStatus.Unspecified;
                if (isSameProject)
                    try
                    {
                        channelClient.UpdateNotificationChannel(
                            null, channel);
                        updated = true;
                    }
                    catch (Grpc.Core.RpcException e)
                    when (e.Status.StatusCode == StatusCode.NotFound)
                    { }
                if (!updated)
                {
                    // The channel no longer exists.  Recreate it.
                    string oldName = channel.Name;
                    channel.Name = null;
                    var response = channelClient.CreateNotificationChannel(
                        projectName, channel);
                    channelNameMap.Add(oldName, response.Name);
                }
            }
            catch (Exception e)
            {
                // If one failed, continue trying to update the others.
                exceptions.Add(e);
            }
        }
        foreach (AlertPolicy policy in backup.Policies)
        {
        }
        if (exceptions.Count > 0)
        {
            throw new AggregateException(exceptions);
        }
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // restorePolicies updates the project with the alert policies and
    // notification channels in r.
    func restorePolicies(w io.Writer, projectID string, r io.Reader) error {
    	b := backup{}
    	if err := json.NewDecoder(r).Decode(&b); err != nil {
    		return err
    	}
    	sameProject := projectID == b.ProjectID
    
    	ctx := context.Background()
    
    	alertClient, err := monitoring.NewAlertPolicyClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer alertClient.Close()
    	channelClient, err := monitoring.NewNotificationChannelClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer channelClient.Close()
    
    	// When a channel is recreated, rather than updated, it will get
    	// a new name.  We have to update the AlertPolicy with the new
    	// name.  channelNames keeps track of the new names.
    	channelNames := make(map[string]string)
    	for _, c := range b.Channels {
    		fmt.Fprintf(w, "Updating channel %q\n", c.GetDisplayName())
    		c.VerificationStatus = monitoringpb.NotificationChannel_VERIFICATION_STATUS_UNSPECIFIED
    		updated := false
    		if sameProject {
    			req := &monitoringpb.UpdateNotificationChannelRequest{
    				NotificationChannel: c.NotificationChannel,
    			}
    			_, err := channelClient.UpdateNotificationChannel(ctx, req)
    			if err == nil {
    				updated = true
    			}
    		}
    		if !updated {
    			req := &monitoringpb.CreateNotificationChannelRequest{
    				Name:                "projects/" + projectID,
    				NotificationChannel: c.NotificationChannel,
    			}
    			oldName := c.GetName()
    			c.Name = ""
    			newC, err := channelClient.CreateNotificationChannel(ctx, req)
    			if err != nil {
    				return err
    			}
    			channelNames[oldName] = newC.GetName()
    		}
    	}
    
    	for _, policy := range b.AlertPolicies {
    		fmt.Fprintf(w, "Updating alert %q\n", policy.GetDisplayName())
    		policy.CreationRecord = nil
    		policy.MutationRecord = nil
    		for i, aChannel := range policy.GetNotificationChannels() {
    			if c, ok := channelNames[aChannel]; ok {
    				policy.NotificationChannels[i] = c
    			}
    		}
    		updated := false
    		if sameProject {
    			req := &monitoringpb.UpdateAlertPolicyRequest{
    				AlertPolicy: policy.AlertPolicy,
    			}
    			_, err := alertClient.UpdateAlertPolicy(ctx, req)
    			if err == nil {
    				updated = true
    			}
    		}
    		if !updated {
    			req := &monitoringpb.CreateAlertPolicyRequest{
    				Name:        "projects/" + projectID,
    				AlertPolicy: policy.AlertPolicy,
    			}
    			if _, err = alertClient.CreateAlertPolicy(ctx, req); err != nil {
    				log.Fatal(err)
    			}
    		}
    	}
    	fmt.Fprintf(w, "Successfully restored alerts.")
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static Map<String, String> restoreNotificationChannels(
        String projectId, List<NotificationChannel> channels, boolean isSameProject)
        throws IOException {
      Map<String, String> newChannelNames = Maps.newHashMap();
      try (NotificationChannelServiceClient client = NotificationChannelServiceClient.create()) {
        for (NotificationChannel channel : channels) {
          // Update channel name if project ID is different.
          boolean channelUpdated = false;
          if (isSameProject) {
            try {
              NotificationChannel updatedChannel =
                  client.updateNotificationChannel(NOTIFICATION_CHANNEL_UPDATE_MASK, channel);
              newChannelNames.put(channel.getName(), updatedChannel.getName());
              channelUpdated = true;
            } catch (Exception e) {
              channelUpdated = false;
            }
          }
          if (!channelUpdated) {
            NotificationChannel newChannel =
                client.createNotificationChannel(
                    ProjectName.of(projectId),
                    channel.toBuilder().clearName().clearVerificationStatus().build());
            newChannelNames.put(channel.getName(), newChannel.getName());
          }
        }
      }
      return newChannelNames;
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
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Monitoring\V3\AlertPolicy;
    use Google\Cloud\Monitoring\V3\Client\AlertPolicyServiceClient;
    use Google\Cloud\Monitoring\V3\Client\NotificationChannelServiceClient;
    use Google\Cloud\Monitoring\V3\CreateAlertPolicyRequest;
    use Google\Cloud\Monitoring\V3\CreateNotificationChannelRequest;
    use Google\Cloud\Monitoring\V3\NotificationChannel;
    use Google\Cloud\Monitoring\V3\NotificationChannel\VerificationStatus;
    use Google\Cloud\Monitoring\V3\UpdateAlertPolicyRequest;
    use Google\Cloud\Monitoring\V3\UpdateNotificationChannelRequest;
    
    /**
     * @param string $projectId Your project ID
     */
    function alert_restore_policies(string $projectId): void
    {
        $alertClient = new AlertPolicyServiceClient([
            'projectId' => $projectId,
        ]);
    
        $channelClient = new NotificationChannelServiceClient([
            'projectId' => $projectId,
        ]);
    
        print('Loading alert policies and notification channels from backup.json.' . PHP_EOL);
        $projectName = 'projects/' . $projectId;
        $record = json_decode((string) file_get_contents('backup.json'), true);
        $isSameProject = $projectName == $record['project_name'];
    
        # Convert dicts to AlertPolicies.
        $policies = [];
        foreach ($record['policies'] as $policyArray) {
            $policy = new AlertPolicy();
            $policy->mergeFromJsonString((string) json_encode($policyArray));
            $policies[] = $policy;
        }
    
        # Convert dicts to NotificationChannels
        $channels = [];
        foreach (array_filter($record['channels']) as $channelArray) {
            $channel = new NotificationChannel();
            $channel->mergeFromJsonString((string) json_encode($channelArray));
            $channels[] = $channel;
        }
    
        # Restore the channels.
        $channelNameMap = [];
        foreach ($channels as $channel) {
            $updated = false;
            printf('Updating channel %s' . PHP_EOL, $channel->getDisplayName());
    
            # This field is immutable and it is illegal to specify a
            # non-default value (UNVERIFIED or VERIFIED) in the
            # Create() or Update() operations.
            $channel->setVerificationStatus(
                VerificationStatus::VERIFICATION_STATUS_UNSPECIFIED
            );
    
            if ($isSameProject) {
                try {
                    $updateNotificationChannelRequest = (new UpdateNotificationChannelRequest())
                        ->setNotificationChannel($channel);
                    $channelClient->updateNotificationChannel($updateNotificationChannelRequest);
                    $updated = true;
                } catch (ApiException $e) {
                    # The channel was deleted.  Create it below.
                    if ($e->getStatus() !== 'NOT_FOUND') {
                        throw $e;
                    }
                }
            }
    
            if (!$updated) {
                # The channel no longer exists.  Recreate it.
                $oldName = $channel->getName();
                $channel->setName('');
                $createNotificationChannelRequest = (new CreateNotificationChannelRequest())
                    ->setName($projectName)
                    ->setNotificationChannel($channel);
                $newChannel = $channelClient->createNotificationChannel($createNotificationChannelRequest);
                $channelNameMap[$oldName] = $newChannel->getName();
            }
        }
    
        # Restore the alerts
        foreach ($policies as $policy) {
            printf('Updating policy %s' . PHP_EOL, $policy->getDisplayName());
            # These two fields cannot be set directly, so clear them.
            $policy->clearCreationRecord();
            $policy->clearMutationRecord();
    
            $notificationChannels = $policy->getNotificationChannels();
    
            # Update old channel names with new channel names.
            foreach ($notificationChannels as $i => $channel) {
                if (isset($channelNameMap[$channel])) {
                    $notificationChannels[$i] = $channelNameMap[$channel];
                }
            }
    
            $updated = false;
            if ($isSameProject) {
                try {
                    $updateAlertPolicyRequest = (new UpdateAlertPolicyRequest())
                        ->setAlertPolicy($policy);
                    $alertClient->updateAlertPolicy($updateAlertPolicyRequest);
                    $updated = true;
                } catch (ApiException $e) {
                    # The policy was deleted.  Create it below.
                    if ($e->getStatus() !== 'NOT_FOUND') {
                        throw $e;
                    }
                }
            }
    
            if (!$updated) {
                # The policy no longer exists.  Recreate it.
                $oldName = $policy->getName();
                $policy->setName('');
                foreach ($policy->getConditions() as $condition) {
                    $condition->setName('');
                }
                $createAlertPolicyRequest = (new CreateAlertPolicyRequest())
                    ->setName($projectName)
                    ->setAlertPolicy($policy);
                $policy = $alertClient->createAlertPolicy($createAlertPolicyRequest);
            }
            printf('Updated %s' . PHP_EOL, $policy->getName());
        }
        print('Restored alert policies and notification channels from backup.json.');
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def restore(project_name, backup_filename):
        """Restore alert policies in a project.
    
        Arguments:
            project_name (str): The Google Cloud Project to use. The project name
                must be in the format - 'projects/<PROJECT_NAME>'.
            backup_filename (str): Name of the file (along with its path) from
                which the alert policies will be restored.
        """
        print(
            "Loading alert policies and notification channels from {}.".format(
                backup_filename
            )
        )
        record = json.load(open(backup_filename, "rt"))
        is_same_project = project_name == record["project_name"]
        # Convert dicts to AlertPolicies.
        policies_json = [json.dumps(policy) for policy in record["policies"]]
        policies = [
            monitoring_v3.AlertPolicy.from_json(policy_json)
            for policy_json in policies_json
        ]
        # Convert dicts to NotificationChannels
        channels_json = [json.dumps(channel) for channel in record["channels"]]
        channels = [
            monitoring_v3.NotificationChannel.from_json(channel_json)
            for channel_json in channels_json
        ]
    
        # Restore the channels.
        channel_client = monitoring_v3.NotificationChannelServiceClient()
        channel_name_map = {}
    
        for channel in channels:
            updated = False
            print("Updating channel", channel.display_name)
            # This field is immutable and it is illegal to specify a
            # non-default value (UNVERIFIED or VERIFIED) in the
            # Create() or Update() operations.
            channel.verification_status = (
                monitoring_v3.NotificationChannel.VerificationStatus.VERIFICATION_STATUS_UNSPECIFIED
            )
    
            if is_same_project:
                try:
                    channel_client.update_notification_channel(notification_channel=channel)
                    updated = True
                except google.api_core.exceptions.NotFound:
                    pass  # The channel was deleted.  Create it below.
    
            if not updated:
                # The channel no longer exists.  Recreate it.
                old_name = channel.name
                del channel.name
                new_channel = channel_client.create_notification_channel(
                    name=project_name, notification_channel=channel
                )
                channel_name_map[old_name] = new_channel.name
    
        # Restore the alerts
        alert_client = monitoring_v3.AlertPolicyServiceClient()
    
        for policy in policies:
            print("Updating policy", policy.display_name)
            # These two fields cannot be set directly, so clear them.
            del policy.creation_record
            del policy.mutation_record
    
            # Update old channel names with new channel names.
            for i, channel in enumerate(policy.notification_channels):
                new_channel = channel_name_map.get(channel)
                if new_channel:
                    policy.notification_channels[i] = new_channel
    
            updated = False
    
            if is_same_project:
                try:
                    alert_client.update_alert_policy(alert_policy=policy)
                    updated = True
                except google.api_core.exceptions.NotFound:
                    pass  # The policy was deleted.  Create it below.
                except google.api_core.exceptions.InvalidArgument:
                    # Annoying that API throws InvalidArgument when the policy
                    # does not exist.  Seems like it should throw NotFound.
                    pass  # The policy was deleted.  Create it below.
    
            if not updated:
                # The policy no longer exists.  Recreate it.
                old_name = policy.name
                del policy.name
                for condition in policy.conditions:
                    del condition.name
                policy = alert_client.create_alert_policy(
                    name=project_name, alert_policy=policy
                )
            print("Updated", policy.name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
