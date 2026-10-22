---
url: https://docs.cloud.google.com/monitoring/alerts/using-alerting-api/
title: Manage alerting policies by API \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:26.895390+00:00
---

# Manage alerting policies by API  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/using-alerting-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Manage alerting policies by API Stay organized with collections  Save and categorize content based on your preferences. 

This document illustrates using the Cloud Monitoring API to create, edit, delete, list, and get metric-based alerting policies programmatically. The examples show how to use of the Google Cloud CLI and how to use client libraries. This content does not apply to log-based alerting policies. For information about log-based alerting policies, see [Monitoring your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs). 

These tasks can also be performed by using the Google Cloud console; for more information, see the following documents:

  * [Create metric-threshold alerting policies by using the Google Cloud console](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui)
  * [Manage alerting policies by using the Google Cloud console](https://docs.cloud.google.com/monitoring/alerts/manage-alerts)



This feature is supported only for Google Cloud projects. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

## About alerting policies

An alerting policy is represented by an [`AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) object, which describes a set of conditions indicating a potentially unhealthy status in your system. Alerting policies reference notification channels, which let you specify how you want to be informed that an alerting policy has been triggered.

Each alerting policy belongs to a scoping project of a metrics scope. Each project can contain up to 2,000 policies. For API calls, you must provide a “project ID”; use the ID of the scoping project of a metrics scope as the value. In these examples, the ID of the scoping project of a metrics scope is `a-gcp-project`.

The `AlertPolicy` resource supports five operations:

  * Creating new policies
  * Deleting existing policies
  * Retrieving specific policies
  * Retrieving all policies
  * Modifying existing policies



Alerting policies can be expressed in JSON or YAML, which lets you record policies in files, and use files to back up and restore policies. With Google Cloud CLI, you can create policies from files in either format. With the REST API, you can create policies from JSON files. See [Sample policies](https://docs.cloud.google.com/monitoring/alerts/policies-in-json) for a selection of alerting policies in JSON format.

**Note:** To use this API, you must provide an end-user credential, not an API key, because this API operates on access-controlled data. This credential can be provided as an OAuth2 token for a user or for a service account. For more information see [Using OAuth2](https://developers.google.com/identity/protocols/OAuth2) and [Google Cloud: Authentication overview](https://docs.cloud.google.com/docs/authentication).

The following examples use the `gcloud` interface and the API to illustrate these basic use cases. The API samples are excerpted from a sample program that uses the API to implement a backup and restore system for alerting policies. Fuller samples are shown in Example: backup and restore.

## Before you begin

Before writing code against the API, you should:

  * Be familiar with the general concepts and terminology used with alerting policies; see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts) for more information.
  * Ensure that the Cloud Monitoring API is enabled for use; see [Enabling the API](https://docs.cloud.google.com/monitoring/api/enable-api) for more information.
  * If you plan to use client libraries, then install the libraries for the languages that you want to use; see [Client Libraries](https://docs.cloud.google.com/monitoring/docs/reference/libraries) for details. API support for alerting is available only for C#, Go, Java, Node.js, and Python.
  * If you plan to use the Google Cloud CLI, then install it. However, if you use [Cloud Shell](https://docs.cloud.google.com/shell), then Google Cloud CLI is already installed.

Examples using the `gcloud` interface are also provided here. Note that the `gcloud` examples all assume that the current project has already been set as the target (`gcloud config set project [PROJECT_ID]`) so invocations omit the explicit `--project` flag. The ID of the current project in the examples is `a-gcp-project`. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.



  * To get the permissions that you need to create and modify alerting policies by using the Cloud Monitoring API, ask your administrator to grant you the [Monitoring AlertPolicy Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.alertPolicyEditor) (`roles/monitoring.alertPolicyEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For detailed information about IAM roles for Monitoring, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

  * Design your application to single-thread Cloud Monitoring API calls that modify the state of an alerting policy in a Google Cloud project. For example, single-thread API calls that create, update, or delete an alerting policy.




## Create an alerting policy

**Note:** If you want to create an alerting policy with forecasting enabled, then you use the Google Cloud console, the Google Cloud CLI commands, or invoke the [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create) API method. The support to create an alerting policy with forecasting enabled might not be available in all client libraries. For more information about using the Google Cloud console, see [Create forecasted metric-value alerting policies][alert-metric-forecast].

To create an alerting policy in a project, use the `alertPolicies.create` method. For information about how to invoke this method, its parameters, and the response data, see the reference page [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create).

You can create policies from JSON or YAML files. The Google Cloud CLI accepts these files as arguments, and you can programmatically read JSON files, convert them to `AlertPolicy` objects, and create policies from them by using the [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create) method. If you have a Prometheus JSON or YAML configuration file with an alerting rule, then the gcloud CLI can migrate it to a Cloud Monitoring alerting policy with a PromQL condition. For more information, see [Migrate alerting rules and receivers from Prometheus][promql-alerts-migrate].

The following samples illustrate the creation of alerting policies, but they don't describe how to create a JSON or YAML file that describes an alerting policy. Instead, the samples assume that a JSON-formatted file exists and they illustrate how to issue the API call. For example JSON files, see [Sample policies](https://docs.cloud.google.com/monitoring/alerts/policies-in-json). For general information about monitoring ratios of metrics, see [Ratios of metrics](https://docs.cloud.google.com/monitoring/charts/metric-ratios).

### gcloud

To create an alerting policy in a project, use the `gcloud monitoring policies create` command. The following example creates an alerting policy in `a-gcp-project` from the `rising-cpu-usage.json` file:
    
    
    gcloud monitoring policies create --policy-from-file="rising-cpu-usage.json"
    

If successful, this command returns the name of the new policy, for example:
    
    
    Created alert policy [projects/a-gcp-project/alertPolicies/12669073143329903307].
    

The file `rising-cpu-usage.json` file contains the JSON for a policy with the display name “High CPU rate of change”. For details about this policy, see [Rate-of-change policy](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-rate-of-change).

See the [`gcloud monitoring policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/create) reference for more information.

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
    
    

The created [`AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) object will have additional fields. The policy itself will have `name`, `creationRecord`, and `mutationRecord` fields. Additionally, each condition in the policy is also given a `name`. These fields cannot be modified externally, so there is no need to set them when creating a policy. None of the JSON examples used for creating policies include them, but if policies created from them are retrieved after creation, the fields will be present.

## List and get alerting policies

To retrieve a list of the policies in a project, use the [`alertPolicies.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/list) method. Use this method to retrieve policies and apply some action to each of them, for example, backing them up. This method also supports `filter` and `orderBy` options to restrict and sort the results; see [Sorting and Filtering](https://docs.cloud.google.com/monitoring/api/v3/sorting-and-filtering).

If you are looking for a specific policy and you know its name, you can use the [`alertPolicies.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/get) method to retrieve only that policy. The name of a policy is the value of the `name` field, not the `displayName`, in the `AlertPolicy` object. The name of a policy has the format `projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]`, for example:
    
    
    projects/a-gcp-project/alertPolicies/12669073143329903307
    

### gcloud

To list all alerting policies in a project, use the `gcloud monitoring policies list` command:
    
    
    gcloud monitoring policies list
    

If successful, the `list` command provides a listing of all the policies in the specified project, formatted as YAML. For example, the [policy with the display name “High CPU rate of change”](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-rate-of-change) in the project `a-gcp-project` is listed like this, among the other policies listed:
    
    
    ---
    combiner: OR
    conditions:
    - conditionThreshold:
        aggregations:
        - alignmentPeriod: 900s
          perSeriesAligner: ALIGN_PERCENT_CHANGE
        comparison: COMPARISON_GT
        duration: 180s
        filter: metric.type="compute.googleapis.com/instance/cpu/utilization" AND resource.type="gce_instance"
        thresholdValue: 0.5
        trigger:
          count: 1
      displayName: CPU usage is increasing at a high rate
      name: projects/a-gcp-project/alertPolicies/12669073143329903307/conditions/12669073143329903008
    creationRecord:
      mutateTime: '2018-03-26T18:52:39.363601689Z'
      mutatedBy: [USER@DOMAIN]
    displayName: High CPU rate of change
    enabled: true
    mutationRecord:
      mutateTime: '2018-03-26T18:52:39.363601689Z'
      mutatedBy: [USER@DOMAIN]
    name: projects/a-gcp-project/alertPolicies/12669073143329903307
    ---
    

To list a single alerting policy, use `gcloud monitoring policies describe`, instead, and specify the name of the policy. For example, this command returns only the listing above:
    
    
    gcloud monitoring policies describe projects/a-gcp-project/alertPolicies/12669073143329903307
    

See the [`gcloud monitoring policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/list) and [`describe`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/describe) references for more information. The `describe` command corresponds to the [`alertPolicies.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/get) method in the API.

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void ListAlertPolicies(string projectId)
    {
        var client = AlertPolicyServiceClient.Create();
        var response = client.ListAlertPolicies(new ProjectName(projectId));
        foreach (AlertPolicy policy in response)
        {
            Console.WriteLine(policy.Name);
            if (policy.DisplayName != null)
            {
                Console.WriteLine(policy.DisplayName);
            }
            if (policy.Documentation?.Content != null)
            {
                Console.WriteLine(policy.Documentation.Content);
            }
            Console.WriteLine();
        }
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // listAlertPolicies lists the alert policies in the project.
    func listAlertPolicies(w io.Writer, projectID string) error {
    	ctx := context.Background()
    	client, err := monitoring.NewAlertPolicyClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	req := &monitoringpb.ListAlertPoliciesRequest{
    		Name: "projects/" + projectID,
    		// Filter:  "", // See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering.
    		// OrderBy: "", // See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering.
    	}
    	it := client.ListAlertPolicies(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			fmt.Fprintln(w, "Done")
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "  Name: %q\n", resp.GetName())
    		fmt.Fprintf(w, "  Display Name: %q\n", resp.GetDisplayName())
    		fmt.Fprintf(w, "  Documentation Content: %q\n\n", resp.GetDocumentation().GetContent())
    	}
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void listAlertPolicies(String projectId) throws IOException {
      try (AlertPolicyServiceClient client = AlertPolicyServiceClient.create()) {
        ListAlertPoliciesPagedResponse response = client.listAlertPolicies(ProjectName.of(projectId));
    
        System.out.println("Alert Policies:");
        for (AlertPolicy policy : response.iterateAll()) {
          System.out.println(
              String.format("\nPolicy %s\nalert-id: %s", policy.getDisplayName(), policy.getName()));
          int channels = policy.getNotificationChannelsCount();
          if (channels > 0) {
            System.out.println("notification-channels:");
            for (int i = 0; i < channels; i++) {
              System.out.println("\t" + policy.getNotificationChannels(i));
            }
          }
          if (policy.hasDocumentation() && policy.getDocumentation().getContent() != null) {
            System.out.println(policy.getDocumentation().getContent());
          }
        }
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[AlertPolicyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function listPolicies() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'YOUR_PROJECT_ID';
    
      const listAlertPoliciesRequest = {
        name: client.projectPath(projectId),
      };
      const [policies] = await client.listAlertPolicies(listAlertPoliciesRequest);
      console.log('Policies:');
      policies.forEach(policy => {
        console.log(`  Display name: ${policy.displayName}`);
        if (policy.documentation && policy.documentation.content) {
          console.log(`     Documentation: ${policy.documentation.content}`);
        }
      });
    }
    listPolicies();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\AlertPolicyServiceClient;
    use Google\Cloud\Monitoring\V3\ListAlertPoliciesRequest;
    
    /**
     * Adds a new column to the Albums table in the example database.
     * Example:
     * ```
     * alert_list_policies($projectId);
     * ```
     *
     * @param string $projectId Your project ID
     */
    function alert_list_policies($projectId)
    {
        $projectName = 'projects/' . $projectId;
        $alertClient = new AlertPolicyServiceClient([
            'projectId' => $projectId,
        ]);
        $listAlertPoliciesRequest = (new ListAlertPoliciesRequest())
            ->setName($projectName);
    
        $policies = $alertClient->listAlertPolicies($listAlertPoliciesRequest);
        foreach ($policies->iterateAllElements() as $policy) {
            printf('Name: %s (%s)' . PHP_EOL, $policy->getDisplayName(), $policy->getName());
        }
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_alert_policies(project_name):
        """List alert policies in a project.
    
        Arguments:
            project_name (str): The Google Cloud Project to use. The project name
                must be in the format - 'projects/<PROJECT_NAME>'.
        """
    
        client = monitoring_v3.AlertPolicyServiceClient()
        policies = client.list_alert_policies(name=project_name)
        print(
            str(
                tabulate.tabulate(
                    [(policy.name, policy.display_name) for policy in policies],
                    ("name", "display_name"),
                )
            )
        )
    
    

## Delete an alerting policy

To delete a policy from a project, use the [`alertPolicies.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/delete) method and supply the name of the alerting policy to delete.

### gcloud

To delete an alerting policy, use `gcloud monitoring policies delete`, and specify the name of the policy to delete. For example, the following command deletes the [policy with the display name “High CPU rate of change”](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-rate-of-change):
    
    
    gcloud monitoring policies delete projects/a-gcp-project/alertPolicies/12669073143329903307
    

See the [`gcloud monitoring policies delete`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/delete) reference for more information. 

## Modify an alerting policy

**Caution:** If you're working with Google Cloud support to investigate the cause of an alert, then don't modify the associated alerting policy. Modifying an alerting policy causes the system to discard the precomputed data that the system uses to determine when to create an alert. Discarding this data results in the loss of the historical record of the alert.

To modify an alerting policy, use the [`alertPolicies.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/patch) method (in the REST API). Other API implementations and the `gcloud` interface call this `update` instead of `patch`.

An update operation can wholly replace the existing policy, or it can modify a subset of fields. An update operation takes a new `AlertPolicy` object and an optional [**field mask**](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask).

If a field mask is specified, then any field listed in the field mask is updated with the value in the supplied policy. If the supplied policy does not include a field mentioned in the field mask, then that field is cleared and set to its default value. Any field not listed in the mask retains its previous value.

If no field mask is specified, then the existing policy is replaced by the supplied one, but the name (`projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]`) is reused. Any conditions in the new policy that have `name` values that include a `CONDITION_ID` will keep those names. If not, new condition and policy names are created.

When using the `gcloud` command-line to update policies, command-line flags rather than a field mask are used to specify fields to update. See the [`gcloud monitoring policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/update) for details.

You can use labels to associate an alerting policy with an [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) application. For more information, see [How to associate an alerting policy with an App Hub application](https://docs.cloud.google.com/monitoring/alerts/policies-in-api#app-labels).

### Enable or disable an alerting policy

To enable or disable a policy, change the value of the boolean `enabled` field in the `AlertPolicy` object. Note that after you enable a policy, it can still be triggered by data collected while it was disabled.

### gcloud

To disable an alerting policy, use the `gcloud monitoring policies update` command and provide the `--no-enabled` flag. The following command disables the “High CPU rate of change” alerting policy in the project `a-gcp-project`:
    
    
    gcloud monitoring policies update projects/a-gcp-project/alertPolicies/12669073143329903307 --no-enabled
    

To enable the policy, use the same command and provide the `--enabled` flag. See the [`gcloud monitoring policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/update) reference for more information. The `update` command corresponds to the [`alertPolicies.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/patch) method in the REST API.

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static object EnablePolicies(string projectId, string filter, bool enable)
    {
        var client = AlertPolicyServiceClient.Create();
        var request = new ListAlertPoliciesRequest()
        {
            ProjectName = new ProjectName(projectId),
            Filter = filter
        };
        var response = client.ListAlertPolicies(request);
        int result = 0;
        foreach (AlertPolicy policy in response)
        {
            try
            {
                if (policy.Enabled == enable)
                {
                    Console.WriteLine("Policy {0} is already {1}.",
                        policy.Name, enable ? "enabled" : "disabled");
                    continue;
                }
                policy.Enabled = enable;
                var fieldMask = new FieldMask { Paths = { "enabled" } };
                client.UpdateAlertPolicy(fieldMask, policy);
                Console.WriteLine("{0} {1}.", enable ? "Enabled" : "Disabled",
                    policy.Name);
            }
            catch (Grpc.Core.RpcException e)
            when (e.Status.StatusCode == StatusCode.InvalidArgument)
            {
                Console.WriteLine(e.Message);
                result -= 1;
            }
        }
        // Return a negative count of how many enable operations failed.
        return result;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // enablePolicies enables or disables all alert policies in the project.
    func enablePolicies(w io.Writer, projectID string, enable bool) error {
    	ctx := context.Background()
    
    	client, err := monitoring.NewAlertPolicyClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	req := &monitoringpb.ListAlertPoliciesRequest{
    		Name: "projects/" + projectID,
    		// Filter:  "", // See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering.
    		// OrderBy: "", // See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering.
    	}
    	it := client.ListAlertPolicies(ctx, req)
    	for {
    		a, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		if a.GetEnabled().GetValue() == enable {
    			fmt.Fprintf(w, "Policy %q already has enabled=%v", a.GetDisplayName(), enable)
    			continue
    		}
    		a.Enabled = &wrappers.BoolValue{Value: enable}
    		req := &monitoringpb.UpdateAlertPolicyRequest{
    			AlertPolicy: a,
    			UpdateMask: &fieldmask.FieldMask{
    				Paths: []string{"enabled"},
    			},
    		}
    		if _, err := client.UpdateAlertPolicy(ctx, req); err != nil {
    			return err
    		}
    	}
    	fmt.Fprintln(w, "Successfully updated alerts.")
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void enablePolicies(String projectId, String filter, boolean enable)
        throws IOException {
      try (AlertPolicyServiceClient client = AlertPolicyServiceClient.create()) {
        ListAlertPoliciesPagedResponse response =
            client.listAlertPolicies(
                ListAlertPoliciesRequest.newBuilder()
                    .setName(ProjectName.of(projectId).toString())
                    .setFilter(filter)
                    .build());
    
        for (AlertPolicy policy : response.iterateAll()) {
          if (policy.getEnabled().getValue() == enable) {
            System.out.println(
                String.format(
                    "Policy %s is already %b.", policy.getName(), enable ? "enabled" : "disabled"));
            continue;
          }
          AlertPolicy updatedPolicy =
              AlertPolicy.newBuilder()
                  .setName(policy.getName())
                  .setEnabled(BoolValue.newBuilder().setValue(enable))
                  .build();
          AlertPolicy result =
              client.updateAlertPolicy(
                  FieldMask.newBuilder().addPaths("enabled").build(), updatedPolicy);
          System.out.println(
              String.format(
                  "%s %s",
                  result.getDisplayName(), result.getEnabled().getValue() ? "enabled" : "disabled"));
        }
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[AlertPolicyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function enablePolicies() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'YOUR_PROJECT_ID';
      // const enabled = true;
      // const filter = 'A filter for selecting policies, e.g. description:"cloud"';
    
      const listAlertPoliciesRequest = {
        name: client.projectPath(projectId),
        // See https://cloud.google.com/monitoring/alerting/docs/sorting-and-filtering
        filter: filter,
      };
    
      const [policies] = await client.listAlertPolicies(listAlertPoliciesRequest);
      const responses = [];
      for (const policy of policies) {
        responses.push(
          await client.updateAlertPolicy({
            updateMask: {
              paths: ['enabled'],
            },
            alertPolicy: {
              name: policy.name,
              enabled: {
                value: enabled,
              },
            },
          })
        );
      }
      responses.forEach(response => {
        const alertPolicy = response[0];
        console.log(`${enabled ? 'Enabled' : 'Disabled'} ${alertPolicy.name}.`);
      });
    }
    enablePolicies();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\AlertPolicyServiceClient;
    use Google\Cloud\Monitoring\V3\ListAlertPoliciesRequest;
    use Google\Cloud\Monitoring\V3\UpdateAlertPolicyRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Enable or disable alert policies in a project.
     *
     * @param string $projectId Your project ID
     * @param bool $enable Enable or disable the policies.
     * @param string $filter Only enable/disable alert policies that match a filter.
     *        See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering
     */
    function alert_enable_policies($projectId, $enable = true, $filter = null)
    {
        $alertClient = new AlertPolicyServiceClient([
            'projectId' => $projectId,
        ]);
        $projectName = 'projects/' . $projectId;
        $listAlertPoliciesRequest = (new ListAlertPoliciesRequest())
            ->setName($projectName)
            ->setFilter($filter);
    
        $policies = $alertClient->listAlertPolicies($listAlertPoliciesRequest);
        foreach ($policies->iterateAllElements() as $policy) {
            $isEnabled = $policy->getEnabled()->getValue();
            if ($enable == $isEnabled) {
                printf('Policy %s is already %s' . PHP_EOL,
                    $policy->getName(),
                    $isEnabled ? 'enabled' : 'disabled'
                );
            } else {
                $policy->getEnabled()->setValue((bool) $enable);
                $mask = new FieldMask();
                $mask->setPaths(['enabled']);
                $updateAlertPolicyRequest = (new UpdateAlertPolicyRequest())
                    ->setAlertPolicy($policy)
                    ->setUpdateMask($mask);
                $alertClient->updateAlertPolicy($updateAlertPolicyRequest);
                printf('%s %s' . PHP_EOL,
                    $enable ? 'Enabled' : 'Disabled',
                    $policy->getName()
                );
            }
        }
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def enable_alert_policies(project_name, enable, filter_=None):
        """Enable or disable alert policies in a project.
    
        Arguments:
            project_name (str): The Google Cloud Project to use. The project name
                must be in the format - 'projects/<PROJECT_NAME>'.
            enable (bool): Enable or disable the policies.
            filter_ (str, optional): Only enable/disable alert policies that match
                this filter_.  See
                https://cloud.google.com/monitoring/api/v3/sorting-and-filtering
        """
    
        client = monitoring_v3.AlertPolicyServiceClient()
        policies = client.list_alert_policies(
            request={"name": project_name, "filter": filter_}
        )
    
        for policy in policies:
            if bool(enable) == policy.enabled:
                print(
                    "Policy",
                    policy.name,
                    "is already",
                    "enabled" if policy.enabled else "disabled",
                )
            else:
                policy.enabled = bool(enable)
                mask = field_mask.FieldMask()
                mask.paths.append("enabled")
                client.update_alert_policy(alert_policy=policy, update_mask=mask)
                print("Enabled" if enable else "Disabled", policy.name)
    
    

### Update notification channels in an alerting policy

You can also update the notification channels referenced by an alerting policy. Alerting policies refer to notification channels by name. The channels must exist before they can be used in an alerting policy.

You create and manage notification channels programmatically by using the [`NotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels) and [`NotificationChannelDescriptors`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors) resources. These examples in this section assume these channels already exist, and uses of these APIs also appear in the programmatic samples.

For more discussion of the notification-channel objects, see [Create and manage notification channels by API](https://docs.cloud.google.com/monitoring/alerts/using-channels-api).

### gcloud

To modify the notification channels in an alerting policy, use the `gcloud monitoring policies update` command. There are several flags related to notification channels, letting you remove notification channels, replace notification channels, and add new notification channels.

For example, the policy with the display name [“High CPU rate of change”](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-rate-of-change) in the project a-gcp-project was created with no notification channels.

To add a notification channel to this policy, use the `gcloud monitoring policies update` command, and specify the channel to add with the `--add-notification-channels` flag:
    
    
    gcloud monitoring policies update projects/a-gcp-project/alertPolicies/12669073143329903307 \
    --add-notification-channels="projects/a-gcp-project/notificationChannels/1355376463305411567"
    

See the [`gcloud monitoring policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/update) reference for more information. The `update` command corresponds to the [`alertPolicies.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/patch) method in the REST API.

The notification channel added here must already exist; see [Create a notification channel](https://docs.cloud.google.com/monitoring/alerts/using-channels-api#api-create-channels) for more information.

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
    
    

### Modify documentation in an alerting policy

A policy can include documentation that is included with alerts and notifications associated with the policy. Use this field to include information to help responders understand and handle the problem indicated by the alert policy. Documentation is included in email notifications and notification types that allow for it; other channel types may omit it.

### gcloud

To add documentation to a policy, or replace existing documentation, use the `gcloud monitoring policies update` command and provide the `--documentation-format="text/markdown"` flag (the only supported format) and either the `--documentation` flag (to enter the value from the command line) or the `--documentation-from-file` flag (to read the value from a file). 

For example, the policy with the display name [“High CPU rate of change”](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-rate-of-change) in the project a-gcp-project was created with no documentation.

The following command sets the `documentation` field in the specified policy to the contents of the `cpu-usage-doc.md` file:
    
    
    gcloud monitoring policies update projects/a-gcp-project/alertPolicies/12669073143329903307 \
    --documentation-format="text/markdown" \
    --documentation-from-file="cpu-usage-doc.md"
    

See the [`gcloud monitoring policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/update) reference for more information. The `update` command corresponds to the [`alertPolicies.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/patch) method in the REST API.

## Add an alerting policy to a dashboard

To display a summary of a single-condition alerting policy on custom dashboard, add an [`AlertChart`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#AlertChart) widget to the dashboard. You use the [`dashboards.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/create) method for a new dashboard and the [`dashboards.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/patch) method for an existing dashboard.

If you specify a multi-condition alerting policy, then the `AlertChart` widget won't display data.

For detailed information about using these API methods, see [Create and manage dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard).

## Example: backup and restore

All of the API examples shown are pulled from a larger application that can back up the alerting policies in a project to a file and can restore the policies, possibly to another project. If the projects used for backup and restore are different, the application effectively exports and imports policies from one project to another.

This section shows the code for backup and restore in context rather than as a set of small, isolated excerpts.

### Backing up policies

The back-up operation is straight-forward. The set of alerting policies and the set of notification channels in each project is collected and saved to external storage in JSON.

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void BackupPolicies(string projectId, string filePath)
    {
        var policyClient = AlertPolicyServiceClient.Create();
        var channelClient = NotificationChannelServiceClient.Create();
        var projectName = new ProjectName(projectId);
        File.WriteAllText(filePath, JsonConvert.SerializeObject(
            new BackupRecord()
            {
                ProjectId = projectId,
                Policies = policyClient.ListAlertPolicies(projectName),
                Channels = channelClient.ListNotificationChannels(projectName)
            }, new ProtoMessageConverter()));
    }
    class BackupRecord
    {
        public string ProjectId { get; set; }
        public IEnumerable<AlertPolicy> Policies { get; set; }
        public IEnumerable<NotificationChannel> Channels { get; set; }
    }
    
    /// <summary>
    /// Lets Newtonsoft.Json and Protobuf's json converters play nicely
    /// together.  The default Netwtonsoft.Json Deserialize method will
    /// not correctly deserialize proto messages.
    /// </summary>
    class ProtoMessageConverter : JsonConverter
    {
        public override bool CanConvert(System.Type objectType)
        {
            return typeof(Google.Protobuf.IMessage)
                .IsAssignableFrom(objectType);
        }
    
        public override object ReadJson(JsonReader reader,
            System.Type objectType, object existingValue,
            JsonSerializer serializer)
        {
            // Read an entire object from the reader.
            var converter = new ExpandoObjectConverter();
            object o = converter.ReadJson(reader, objectType, existingValue,
                serializer);
            // Convert it back to json text.
            string text = JsonConvert.SerializeObject(o);
            // And let protobuf's parser parse the text.
            IMessage message = (IMessage)Activator
                .CreateInstance(objectType);
            return Google.Protobuf.JsonParser.Default.Parse(text,
                message.Descriptor);
        }
    
        public override void WriteJson(JsonWriter writer, object value,
            JsonSerializer serializer)
        {
            writer.WriteRawValue(Google.Protobuf.JsonFormatter.Default
                .Format((IMessage)value));
        }
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // backupPolicies writes a JSON representation of the project's alert
    // policies and notification channels.
    func backupPolicies(w io.Writer, projectID string) error {
    	b := backup{ProjectID: projectID}
    	ctx := context.Background()
    
    	alertClient, err := monitoring.NewAlertPolicyClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer alertClient.Close()
    	alertReq := &monitoringpb.ListAlertPoliciesRequest{
    		Name: "projects/" + projectID,
    		// Filter:  "", // See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering.
    		// OrderBy: "", // See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering.
    	}
    	alertIt := alertClient.ListAlertPolicies(ctx, alertReq)
    	for {
    		resp, err := alertIt.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		b.AlertPolicies = append(b.AlertPolicies, &alertPolicy{resp})
    	}
    
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
    	bs, err := json.MarshalIndent(b, "", "  ")
    	if err != nil {
    		return err
    	}
    	if _, err := w.Write(bs); err != nil {
    		return err
    	}
    	return nil
    }
    
    // alertPolicy is a wrapper around the AlertPolicy proto to
    // ensure JSON marshaling/unmarshaling works correctly.
    type alertPolicy struct {
    	*monitoringpb.AlertPolicy
    }
    
    // channel is a wrapper around the NotificationChannel proto to
    // ensure JSON marshaling/unmarshaling works correctly.
    type channel struct {
    	*monitoringpb.NotificationChannel
    }
    
    // backup is used to backup and restore a project's policies.
    type backup struct {
    	ProjectID     string
    	AlertPolicies []*alertPolicy
    	Channels      []*channel
    }
    
    func (a *alertPolicy) MarshalJSON() ([]byte, error) {
    	m := &jsonpb.Marshaler{EmitDefaults: true}
    	b := new(bytes.Buffer)
    	m.Marshal(b, a.AlertPolicy)
    	return b.Bytes(), nil
    }
    
    func (a *alertPolicy) UnmarshalJSON(b []byte) error {
    	u := &jsonpb.Unmarshaler{}
    	a.AlertPolicy = new(monitoringpb.AlertPolicy)
    	return u.Unmarshal(bytes.NewReader(b), a.AlertPolicy)
    }
    
    func (c *channel) MarshalJSON() ([]byte, error) {
    	m := &jsonpb.Marshaler{}
    	b := new(bytes.Buffer)
    	m.Marshal(b, c.NotificationChannel)
    	return b.Bytes(), nil
    }
    
    func (c *channel) UnmarshalJSON(b []byte) error {
    	u := &jsonpb.Unmarshaler{}
    	c.NotificationChannel = new(monitoringpb.NotificationChannel)
    	return u.Unmarshal(bytes.NewReader(b), c.NotificationChannel)
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void backupPolicies(String projectId, String filePath) throws IOException {
      List<AlertPolicy> alertPolicies = getAlertPolicies(projectId);
      List<NotificationChannel> notificationChannels = getNotificationChannels(projectId);
      writePoliciesBackupFile(projectId, filePath, alertPolicies, notificationChannels);
      System.out.println(String.format("Saved policies to %s", filePath));
    }
    
    private static List<AlertPolicy> getAlertPolicies(String projectId) throws IOException {
      List<AlertPolicy> alertPolicies = Lists.newArrayList();
      try (AlertPolicyServiceClient client = AlertPolicyServiceClient.create()) {
        ListAlertPoliciesPagedResponse response = client.listAlertPolicies(ProjectName.of(projectId));
    
        for (AlertPolicy policy : response.iterateAll()) {
          alertPolicies.add(policy);
        }
      }
      return alertPolicies;
    }
    
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
    
    private static void writePoliciesBackupFile(
        String projectId,
        String filePath,
        List<AlertPolicy> alertPolicies,
        List<NotificationChannel> notificationChannels)
        throws IOException {
      JsonObject backupContents = new JsonObject();
      backupContents.add("project_id", new JsonPrimitive(projectId));
      JsonArray policiesJson = new JsonArray();
      for (AlertPolicy policy : alertPolicies) {
        policiesJson.add(gson.toJsonTree(policy));
      }
      backupContents.add("policies", policiesJson);
    
      JsonArray notificationsJson = new JsonArray();
      for (NotificationChannel channel : notificationChannels) {
        notificationsJson.add(gson.toJsonTree(channel));
      }
      backupContents.add("notification_channels", notificationsJson);
    
      FileWriter writer = new FileWriter(filePath);
      writer.write(backupContents.toString());
      writer.close();
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const fs = require('fs');
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[AlertPolicyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function backupPolicies() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'YOUR_PROJECT_ID';
    
      const listAlertPoliciesRequest = {
        name: client.projectPath(projectId),
      };
    
      let [policies] = await client.listAlertPolicies(listAlertPoliciesRequest);
    
      // filter out any policies created by tests for this sample
      policies = policies.filter(policy => {
        return !policy.displayName.startsWith('gcloud-tests-');
      });
    
      fs.writeFileSync(
        './policies_backup.json',
        JSON.stringify(policies, null, 2),
        'utf-8'
      );
    
      console.log('Saved policies to ./policies_backup.json');

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\AlertPolicyServiceClient;
    use Google\Cloud\Monitoring\V3\Client\NotificationChannelServiceClient;
    use Google\Cloud\Monitoring\V3\ListAlertPoliciesRequest;
    use Google\Cloud\Monitoring\V3\ListNotificationChannelsRequest;
    
    /**
     * Back up alert policies.
     *
     * @param string $projectId Your project ID
     */
    function alert_backup_policies($projectId)
    {
        $alertClient = new AlertPolicyServiceClient([
            'projectId' => $projectId,
        ]);
        $channelClient = new NotificationChannelServiceClient([
            'projectId' => $projectId,
        ]);
        $projectName = 'projects/' . $projectId;
    
        $record = [
            'project_name' => $projectName,
            'policies' => [],
            'channels' => [],
        ];
        $listAlertPoliciesRequest = (new ListAlertPoliciesRequest())
            ->setName($projectName);
        $policies = $alertClient->listAlertPolicies($listAlertPoliciesRequest);
        foreach ($policies->iterateAllElements() as $policy) {
            $record['policies'][] = json_decode($policy->serializeToJsonString());
        }
        $listNotificationChannelsRequest = (new ListNotificationChannelsRequest())
            ->setName($projectName);
        $channels = $channelClient->listNotificationChannels($listNotificationChannelsRequest);
        foreach ($channels->iterateAllElements() as $channel) {
            $record['channels'][] = json_decode($channel->serializeToJsonString());
        }
        file_put_contents('backup.json', json_encode($record, JSON_PRETTY_PRINT));
        print('Backed up alert policies and notification channels to backup.json.');
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def backup(project_name, backup_filename):
        """Backup alert policies from a project to a local file.
    
        Arguments:
            project_name (str): The Google Cloud Project to use. The project name
                must be in the format - 'projects/<PROJECT_NAME>'
            backup_filename (str): Name of the file (along with its path) to which
                the alert policies will be written as backup.
        """
    
        alert_client = monitoring_v3.AlertPolicyServiceClient()
        channel_client = monitoring_v3.NotificationChannelServiceClient()
        record = {
            "project_name": project_name,
            "policies": list(alert_client.list_alert_policies(name=project_name)),
            "channels": list(channel_client.list_notification_channels(name=project_name)),
        }
        json.dump(record, open(backup_filename, "wt"), cls=ProtoEncoder, indent=2)
        print(
            "Backed up alert policies and notification channels to {}.".format(
                backup_filename
            )
        )
    
    
    class ProtoEncoder(json.JSONEncoder):
        """Encode protobufs as json."""
    
        def default(self, obj):
            if type(obj) in (monitoring_v3.AlertPolicy, monitoring_v3.NotificationChannel):
                text = proto.Message.to_json(obj)
                return json.loads(text)
            return super(ProtoEncoder, self).default(obj)
    
    

### Restoring the backed-up policies

The restoration process is more complex than the original back-up. You can restore to the project you originally backed up. You can also restore to a different project, effectively providing import of alerting policies.

If restoring to the same project, any existing channels or policies are updated if they still exist. If they don't, they are recreated. Read-only fields, like the creation and mutation records, in the backed-up policies are cleared by the restoration process before policies and notifications are recreated.

You can use a policy saved in one project to create a new, or similar, policy in another project. However, you must first make the following changes in a copy of the saved policy:

  * Remove the following fields from any notification channels: 
    * `name`
    * `verificationStatus`
  * Create notification channels before referring to the channels in alerting policies (you need the new channel identifiers).
  * Remove the following fields from any alerting policies you are recreating: 
    * `name`
    * `condition.name`
    * `creationRecord`
    * `mutationRecord`



If the policy is being recreated in a new project, the names of any conditions in the backed-up policies are cleared along with the creation and mutation records.

Additionally, when a notification channel is recreated in a different project, it gets a different name, so the restore process has to map the names of channels in backed-up alerting policies to their new names, and replace the old names with the new ones.

In addition to the names of notification channels, the value of the `verificationStatus` field cannot be set when the channel is created or updated, so a sentinel value, `unspecified` is used. After channels have been restored into a new project, they must be explicitly verified.

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
    
    class BackupRecord
    {
        public string ProjectId { get; set; }
        public IEnumerable<AlertPolicy> Policies { get; set; }
        public IEnumerable<NotificationChannel> Channels { get; set; }
    }
    
    /// <summary>
    /// Lets Newtonsoft.Json and Protobuf's json converters play nicely
    /// together.  The default Netwtonsoft.Json Deserialize method will
    /// not correctly deserialize proto messages.
    /// </summary>
    class ProtoMessageConverter : JsonConverter
    {
        public override bool CanConvert(System.Type objectType)
        {
            return typeof(Google.Protobuf.IMessage)
                .IsAssignableFrom(objectType);
        }
    
        public override object ReadJson(JsonReader reader,
            System.Type objectType, object existingValue,
            JsonSerializer serializer)
        {
            // Read an entire object from the reader.
            var converter = new ExpandoObjectConverter();
            object o = converter.ReadJson(reader, objectType, existingValue,
                serializer);
            // Convert it back to json text.
            string text = JsonConvert.SerializeObject(o);
            // And let protobuf's parser parse the text.
            IMessage message = (IMessage)Activator
                .CreateInstance(objectType);
            return Google.Protobuf.JsonParser.Default.Parse(text,
                message.Descriptor);
        }
    
        public override void WriteJson(JsonWriter writer, object value,
            JsonSerializer serializer)
        {
            writer.WriteRawValue(Google.Protobuf.JsonFormatter.Default
                .Format((IMessage)value));
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
    
    
    private static void restorePolicies(String projectId, String filePath) throws IOException {
      FileReader reader = new FileReader(filePath);
      BufferedReader bufferedReader = new BufferedReader(reader);
    
      JsonObject backupContent = getPolicyJsonContents(filePath, bufferedReader);
      String backupProjectId = backupContent.get("project_id").getAsString();
      boolean isSameProject = projectId.equals(backupProjectId);
    
      AlertPolicy[] policies = gson.fromJson(backupContent.get("policies"), AlertPolicy[].class);
      List<NotificationChannel> notificationChannels = readNotificationChannelsJson(backupContent);
      Map<String, String> restoredChannelIds =
          restoreNotificationChannels(projectId, notificationChannels, isSameProject);
      List<AlertPolicy> policiesToRestore =
          reviseRestoredPolicies(policies, isSameProject, restoredChannelIds);
    
      restoreRevisedPolicies(projectId, isSameProject, policiesToRestore);
    }
    
    private static List<AlertPolicy> reviseRestoredPolicies(
        AlertPolicy[] policies, boolean isSameProject, Map<String, String> restoredChannelIds) {
      List<AlertPolicy> newPolicies = Lists.newArrayListWithCapacity(policies.length);
      for (AlertPolicy policy : policies) {
        AlertPolicy.Builder policyBuilder =
            policy
                .toBuilder()
                .clearNotificationChannels()
                .clearMutationRecord()
                .clearCreationRecord();
        // Update restored notification channel names.
        for (String channelName : policy.getNotificationChannelsList()) {
          String newChannelName = restoredChannelIds.get(channelName);
          if (!Strings.isNullOrEmpty(newChannelName)) {
            policyBuilder.addNotificationChannels(newChannelName);
          }
        }
        if (!isSameProject) {
          policyBuilder.clearName();
          policyBuilder.clearConditions();
          for (AlertPolicy.Condition condition : policy.getConditionsList()) {
            policyBuilder.addConditions(condition.toBuilder().clearName());
          }
        }
        newPolicies.add(policyBuilder.build());
      }
      return newPolicies;
    }
    
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
    
    private static List<NotificationChannel> readNotificationChannelsJson(JsonObject backupContent) {
      if (backupContent.has("notification_channels")) {
        NotificationChannel[] channels =
            gson.fromJson(backupContent.get("notification_channels"), NotificationChannel[].class);
        return Lists.newArrayList(channels);
      }
      return Lists.newArrayList();
    }
    
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
    
    private static JsonObject getPolicyJsonContents(String filePath, BufferedReader content) {
      try {
        return gson.fromJson(content, JsonObject.class);
      } catch (JsonSyntaxException jse) {
        throw new RuntimeException(String.format("Could not parse policies file %s", filePath), jse);
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
    
    

## Alerting and Google Cloud CLI

In Google Cloud CLI, the command group for managing alerting policies and notification channels is [`monitoring`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring). These commands will all begin with:
    
    
    gcloud monitoring
    

To check if you have the Google Cloud CLI installed, run this command:
    
    
    gcloud --version
    

If you don't have the Google Cloud CLI installed, see [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

To check for the `monitoring` group, run this command:
    
    
    gcloud monitoring --help
    

If the `monitoring` group is not included, Google Cloud CLI will prompt you to add it:
    
    
    You do not currently have this command group installed.
    [...]
    Do you want to continue (Y/n)?  y
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
