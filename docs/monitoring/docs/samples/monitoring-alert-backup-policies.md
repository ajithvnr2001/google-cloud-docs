---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-backup-policies/
title: Back up policies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:13.424218+00:00
---

# Back up policies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-backup-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Back up policies Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to back up alerting policies.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
