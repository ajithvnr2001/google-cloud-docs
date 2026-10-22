---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-create-policy/
title: Create an alerting policy, in the context of recreating policies from a backup. \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:26.633037+00:00
---

# Create an alerting policy, in the context of recreating policies from a backup.  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-create-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Create an alerting policy, in the context of recreating policies from a backup. Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to create an alerting policy.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create alerting policies by using the API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api)
  * [Manage alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api)



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
        }
        foreach (AlertPolicy policy in backup.Policies)
        {
            string policyName = policy.Name;
            // These two fields cannot be set directly, so clear them.
            policy.CreationRecord = null;
            policy.MutationRecord = null;
            // Update channel names if the channel was recreated with
            // another name.
            for (int i = 0; i < policy.NotificationChannels.Count; ++i)
            {
                if (channelNameMap.ContainsKey(policy.NotificationChannels[i]))
                {
                    policy.NotificationChannels[i] =
                        channelNameMap[policy.NotificationChannels[i]];
                }
            }
            try
            {
                Console.WriteLine("Updating policy.\n{0}",
                    policy.DisplayName);
                bool updated = false;
                if (isSameProject)
                    try
                    {
                        policyClient.UpdateAlertPolicy(null, policy);
                        updated = true;
                    }
                    catch (Grpc.Core.RpcException e)
                    when (e.Status.StatusCode == StatusCode.NotFound)
                    { }
                if (!updated)
                {
                    // The policy no longer exists.  Recreate it.
                    policy.Name = null;
                    foreach (var condition in policy.Conditions)
                    {
                        condition.Name = null;
                    }
                    policyClient.CreateAlertPolicy(projectName, policy);
                }
                Console.WriteLine("Restored {0}.", policyName);
            }
            catch (Exception e)
            {
                // If one failed, continue trying to update the others.
                exceptions.Add(e);
            }
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
    
    
    private static void restoreRevisedPolicies(
        String projectId, boolean isSameProject, List<AlertPolicy> policies) throws IOException {
      try (AlertPolicyServiceClient client = AlertPolicyServiceClient.create()) {
        for (AlertPolicy policy : policies) {
          if (!isSameProject) {
            policy = client.createAlertPolicy(ProjectName.of(projectId), policy);
          } else {
            try {
              client.updateAlertPolicy(null, policy);
            } catch (Exception e) {
              policy =
                  client.createAlertPolicy(
                      ProjectName.of(projectId), policy.toBuilder().clearName().build());
            }
          }
          System.out.println(String.format("Restored %s", policy.getName()));
        }
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const fs = require('fs');
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[AlertPolicyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function restorePolicies() {
      // Note: The policies are restored one at a time due to limitations in
      // the API. Otherwise, you may receive a 'service unavailable'  error
      // while trying to create multiple alerts simultaneously.
    
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'YOUR_PROJECT_ID';
    
      console.log('Loading policies from ./policies_backup.json');
      const fileContent = fs.readFileSync('./policies_backup.json', 'utf-8');
      const policies = JSON.parse(fileContent);
    
      for (const index in policies) {
        // Restore each policy one at a time
        let policy = policies[index];
        if (await doesAlertPolicyExist(policy.name)) {
          policy = await client.updateAlertPolicy({
            alertPolicy: policy,
          });
        } else {
          // Clear away output-only fields
          delete policy.name;
          delete policy.creationRecord;
          delete policy.mutationRecord;
          policy.conditions.forEach(condition => delete [condition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.condition-class.html).name);
    
          policy = await client.createAlertPolicy({
            name: client.projectPath(projectId),
            alertPolicy: policy,
          });
        }
    
        console.log(`Restored ${policy[0].name}.`);
      }
      async function doesAlertPolicyExist(name) {
        try {
          const [policy] = await client.getAlertPolicy({
            name,
          });
          return policy ? true : false;
        } catch (err) {
          if (err && err.code === 5) {
            // Error code 5 comes from the google.rpc.code.NOT_FOUND protobuf
            return false;
          }
          throw err;
        }
      }
    }
    restorePolicies();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\AlertPolicy;
    use Google\Cloud\Monitoring\V3\AlertPolicy\Condition;
    use Google\Cloud\Monitoring\V3\AlertPolicy\Condition\MetricThreshold;
    use Google\Cloud\Monitoring\V3\AlertPolicy\ConditionCombinerType;
    use Google\Cloud\Monitoring\V3\Client\AlertPolicyServiceClient;
    use Google\Cloud\Monitoring\V3\ComparisonType;
    use Google\Cloud\Monitoring\V3\CreateAlertPolicyRequest;
    use Google\Protobuf\Duration;
    
    /**
     * @param string $projectId Your project ID
     */
    function alert_create_policy($projectId)
    {
        $alertClient = new AlertPolicyServiceClient([
            'projectId' => $projectId,
        ]);
        $projectName = 'projects/' . $projectId;
    
        $policy = new AlertPolicy();
        $policy->setDisplayName('Test Alert Policy');
        $policy->setCombiner(ConditionCombinerType::PBOR);
        /** @see https://cloud.google.com/monitoring/api/resources for a list of resource.type */
        /** @see https://cloud.google.com/monitoring/api/metrics_gcp for a list of metric.type */
        $policy->setConditions([new Condition([
            'display_name' => 'condition-1',
            'condition_threshold' => new MetricThreshold([
                'filter' => 'resource.type = "gce_instance" AND metric.type = "compute.googleapis.com/instance/cpu/utilization"',
                'duration' => new Duration(['seconds' => '60']),
                'comparison' => ComparisonType::COMPARISON_LT,
            ])
        ])]);
        $createAlertPolicyRequest = (new CreateAlertPolicyRequest())
            ->setName($projectName)
            ->setAlertPolicy($policy);
    
        $policy = $alertClient->createAlertPolicy($createAlertPolicyRequest);
        printf('Created alert policy %s' . PHP_EOL, $policy->getName());
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
