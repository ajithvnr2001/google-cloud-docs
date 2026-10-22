---
url: https://docs.cloud.google.com/monitoring/alerts/policies-in-api/
title: Create alerting policies by using the API \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:47.479016+00:00
---

# Create alerting policies by using the API  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/policies-in-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create alerting policies by using the API Stay organized with collections  Save and categorize content based on your preferences. 

An alerting policy is represented in the Cloud Monitoring API by an [`AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) object, which describes a set of conditions indicating a potentially unhealthy status in your system.

This document describes the following:

  * How the Monitoring API represents alerting policies.
  * The types of conditions the Monitoring API provides for alerting policies.
  * How to create an alerting policy by using the Google Cloud CLI or client libraries.

**Note:** To use the Cloud Monitoring API, you must provide an end-user credential, not an API key, because this API operates on access-controlled data. This credential can be provided as an OAuth2 token for a user or for a service account. For more information see [Using OAuth2](https://developers.google.com/identity/protocols/OAuth2) and [Google Cloud: Authentication overview](https://docs.cloud.google.com/docs/authentication).

This feature is supported only for Google Cloud projects. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

## Structure of an alerting policy

The [`AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) structure defines the components of an alerting policy. When you create a policy, you specify values for the following `AlertPolicy` fields:

  * `displayName`: A descriptive label for the policy.
  * [`documentation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Documentation): We recommend that you use this field to provide information that helps alert responders. For more information, see [Annotate notifications with user-defined documentation](https://docs.cloud.google.com/monitoring/alerts/doc-variables).
  * `userLabels`: Any user-defined labels attached to the policy. Alerting policies, alerts, and notifications display these labels. For information about using labels with alerting, see [Annotate alerts with labels](https://docs.cloud.google.com/monitoring/alerts/labels).

  * `conditions[]`: An array of [`Condition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition) structures.

  * `combiner`: A logical operator that determines how to handle multiple conditions.

  * `notificationChannels[]`: an array of resource names, each identifying a [`NotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels#NotificationChannel).

  * [`alertStrategy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertStrategy): Specifies the following:

    * How quickly Monitoring closes alerts when data stops arriving.
    * For metric-based alerting policies, whether Monitoring sends a notification when an alert is closed.
    * For metric-based alerting policies, whether repeated notifications are enabled, and the interval between those notifications. For more information, see [Configure repeated notifications for metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/policies-in-api#send-repeated-notifications).



You can also specify the `severity` field when you use the Cloud Monitoring API and the Google Cloud console. This field lets you define the severity level of alerts. If you don't specify a severity, then Cloud Monitoring sets the alerting policy severity to `No Severity`.

There are other fields you might use, depending on the conditions you create.

When an alerting policy contains one condition, a notification is sent when that condition is met. For information about notifications when alerting policies contain multiple conditions, see [Policies with multiple conditions](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#condition-combiners) and [When Monitoring sends notifications and creates alerts](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#notify-alert-policy).

When you create or modify the alerting policy, Monitoring sets other fields as well, including the `name` field. The value of the `name` field is the resource name for the alerting policy, which identifies the policy. The resource name has the following form:
    
    
    projects/PROJECT_ID/alertPolicies/POLICY_ID
    

In the previous expression:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * POLICY_ID: The ID of the alerting policy



## Types of conditions in the API

The Cloud Monitoring API supports a variety of condition types in the [`Condition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition) structure. There are multiple condition types for metric-based alerting policies, and one for log-based alerting policies. The following sections describe the available condition types.

### Conditions for metric-based alerting policies

To create an alerting policy that monitors metric data, including log-based metrics, you can use the following condition types:

  * [`MetricAbsence`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricAbsence)
  * [`MetricThreshold`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricThreshold)
  * [`PrometheusQueryLanguageCondition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#PrometheusQueryLanguageCondition)



#### Filter-based metric conditions

The `MetricAbsence` and `MetricThreshold` conditions use [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters) to select the time-series data to monitor. Other fields in the condition structure specify how to filter, group, and aggregate the data. For more information on these concepts, see [Filtering and aggregation: manipulating time series](https://docs.cloud.google.com/monitoring/api/v3/aggregation).

If you use the `MetricAbsence` condition type, then you can create a condition that is met only when all of the time series are absent. This condition uses the `aggregations` parameter to aggregate multiple time series into a single time series. For more information, see the [`MetricAbsence`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricAbsence) reference in the API documentation.

A metric-absence alerting policy requires that some data has been written previously; for more information, see [Create metric-absence alerting policies](https://docs.cloud.google.com/monitoring/alerts/metric-absence).

If you want to get notified based on a forecasted value, then configure your alerting policy to use the `MetricThreshold` condition type and to set the `forecastOptions` field. When this field isn't set, then the measured data is compared to a threshold. However, when this field is set, then predicted data is compared to a threshold. For more information, see [Create forecasted metric-value alerting policies](https://docs.cloud.google.com/monitoring/alerts/metric-forecast).

#### PromQL-based metric conditions

The `PrometheusQueryLanguageCondition` condition uses Prometheus Query Language (PromQL) queries to select and manipulate time-series data to monitor. Your condition can compute a ratio of metrics, evaluate metric comparisons, and more.

If you use a `PrometheusQueryLanguageCondition` condition, it must be the only condition in your alerting policy. For more information, see [Alerting policies with PromQL](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).

#### Conditions for alerting on ratios

You can create metric-threshold alerting policies to monitor the ratio of two metrics. You can create these policies by using either the `MetricThreshold` or `PrometheusQueryLanguageCondition` condition type. You can also use PromQL directly in the Google Cloud console. You can't create or manage ratio-based conditions by using the graphical interface for creating threshold conditions.

We recommend using PromQL to create ratio-based alerting policies. PromQL lets you build more powerful and flexible queries than you can build by using the `MetricTheshold` condition type and Monitoring filters. For example, with a `PrometheusQueryLanguageCondition` condition, you can compute the ratio of a gauge metric to a delta metric.

If you use the `MetricThreshold` condition, the numerator and denominator of the ratio must have the same [`MetricKind`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind). For a list of metrics and their properties, see [Metric lists](https://docs.cloud.google.com/monitoring/api/metrics).

In general, it is best to compute ratios based on time series collected for a single metric type, by using label values. A ratio computed over two different metric types is subject to anomalies due to different sampling periods and alignment windows.

For example, suppose that you have two different metric types, an RPC total count and an RPC error count, and you want to compute the ratio of error-count RPCs over total RPCs. The unsuccessful RPCs are counted in the time series of both metric types. Therefore, there is a chance that, when you align the time series, an unsuccessful RPC doesn't appear in the same alignment interval for both time series. This difference can happen for several reasons, including the following:

  * Because there are two different time series recording the same event, there are two underlying counter values implementing the collection, and they aren't updated atomically.
  * The sampling rates might differ. When the time series are aligned to a common period, the counts for a single event might appear in adjacent alignment intervals in the time series for the different metrics.



The difference in the number of values in corresponding alignment intervals can lead to nonsensical `error/total` ratio values like 1/0 or 2/1.

Ratios of larger numbers are less likely to result in nonsensical values. You can get larger numbers by aggregation, either by using an alignment window that is longer than the sampling period, or by grouping data for certain labels. These techniques minimize the effect of small differences in the number of points in a given interval. That is, a two-point disparity is more significant when the expected number of points in an interval is 3 than when the expected number is 300.

If you are using built-in metric types, then you might have no choice but to compute ratios across metric types to get the value you need.

If you are designing custom metrics that might count the same thing—like RPCs returning error status—in two different metrics, consider instead a single metric, which includes each count only once. For example, suppose that you are counting RPCs and you want to track the ratio of unsuccessful RPCs to all RPCs. To solve this problem, create a single metric type to count RPCs, and use a label to record the status of the invocation, including the "OK" status. Then each status value, error or "OK", is recorded by updating a single counter for that case.

### Condition for log-based alerting policies

To create a log-based alerting policy, which notifies you when a message matching your filter appears in your log entries, use the [`LogMatch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#LogMatch) condition type. If you use a `LogMatch` condition, it must be the only condition in your alerting policy.

Don't try to use the `LogMatch` condition type in conjunction with log-based metrics. Alerting policies that monitor log-based metrics are metric-based policies. For more information about choosing between alerting policies that monitor log-based metrics or log entries, see [Monitoring your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs).

The alerting policies used in the examples in the [Manage alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api) document are metric-based alerting policies, although the principles are the same for log-based alerting policies. For information specific to log-based alerting policies, see [Create a log-based alerting policy by using the Monitoring API](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api) in the Cloud Logging documentation.

## How to associate an alerting policy with an App Hub application

Google Cloud generates dashboards that help you monitor your [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) applications. These dashboards display information like log and metric data for your applications, and the services and workloads that are part of the application. Alerting policies and their alerts are also shown on these dashboards, when those policies are associated with an application's service or workload. For more information about Application Monitoring, see [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring).

To associate an alerting policy with an [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) application, attach labels with the following keys to your policy:

  * `apphub_application_location`
  * `apphub_application_id`
  * `apphub_service_id` or `apphub_workload_id`

For example, the `userLabels` section of the JSON representation of an alerting policy might by like the following: 
    
    
    
      "userLabels": {
        "apphub_service_id": "my-service-id",
        "apphub_application_location": "my-app-location",
        "apphub_application_id": "my-app"
      },
    

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

**Note:** If you want to create an alerting policy with forecasting enabled, then you use the Google Cloud console, the Google Cloud CLI commands, or invoke the [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create) API method. The support to create an alerting policy with forecasting enabled might not be available in all client libraries. For more information about using the Google Cloud console, see [Create forecasted metric-value alerting policies](https://docs.cloud.google.com/monitoring/alerts/metric-forecast).

To create an alerting policy in a project, use the `alertPolicies.create` method. For information about how to invoke this method, its parameters, and the response data, see the reference page [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create).

You can create policies from JSON or YAML files. The Google Cloud CLI accepts these files as arguments, and you can programmatically read JSON files, convert them to `AlertPolicy` objects, and create policies from them by using the [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create) method. If you have a Prometheus JSON or YAML configuration file with an alerting rule, then the gcloud CLI can migrate it to a Cloud Monitoring alerting policy with a PromQL condition. For more information, see [Migrate alerting rules and receivers from Prometheus](https://docs.cloud.google.com/monitoring/promql/promql-migrate).

Each alerting policy belongs to a scoping project of a metrics scope. Each project can contain up to 2,000 policies. For API calls, you must provide a “project ID”; use the ID of the scoping project of a metrics scope as the value. In these examples, the ID of the scoping project of a metrics scope is `a-gcp-project`.

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

## Configure repeated notifications for metric-based alerting policies

By default, a metric-based alerting policy sends one notification to each notification channel when an alert is opened. However, you can change the default behavior and configure an alerting policy to resend notifications to all or some of the notification channels for your alerting policy. These repeated notifications are sent for alerts with a status of Open or Acknowledged. The interval between these notifications must be at least 30 minutes and no more than 24 hours, expressed in seconds.

To configure repeated notifications, add to the alerting policy's configuration an [`AlertStrategy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertStrategy) object that contains at least one `NotificationChannelStrategy` object. A `NotificationChannelStrategy` object has two fields:

  * `renotifyInterval`: The interval, in seconds, between repeated notifications.

If you change the value of the `renotifyInterval` field when an alert for the alerting policy is opened, then the following happens:

    * The alerting policy sends out another notification for the alert.
    * The alerting policy restarts the interval period.
  * `notificationChannelNames`: An array of notification channel resource names, which are strings in the format of `projects/PROJECT_ID/notificationChannels/CHANNEL_ID`, where CHANNEL_ID is a numeric value. For information about how to retrieve the channel ID, see [List notification channels in a project](https://docs.cloud.google.com/monitoring/alerts/using-channels-api#api-list-channels).




For example, the following JSON sample shows an alert strategy configured to send repeated notifications every 1800 seconds (30 minutes) to one notification channel:
    
    
      "alertStrategy": {
        "notificationChannelStrategy": [
          {
            "notificationChannelNames": [
              "projects/PROJECT_ID/notificationChannels/CHANNEL_ID"
            ],
            "renotifyInterval": "1800s"
          }
        ]
      }
    

To temporarily stop repeated notifications, create a [snooze](https://docs.cloud.google.com/monitoring/alerts/manage-snooze). To prevent repeated notifications, edit the alerting policy by using the API and remove the `NotificationChannelStrategy` object.

## What's next

  * [Manage alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api)
  * [Create and manage notification channels by API](https://docs.cloud.google.com/monitoring/alerts/using-channels-api)


  * [Use Tags to control access to alerting policies](https://docs.cloud.google.com/monitoring/docs/access-control-with-tags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
