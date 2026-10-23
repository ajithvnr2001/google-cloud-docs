---
url: https://docs.cloud.google.com/monitoring/alerts/using-channels-api/
title: Create and manage notification channels by API \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:22.608082+00:00
---

# Create and manage notification channels by API  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/using-channels-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create and manage notification channels by API Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Cloud Monitoring API and the Google Cloud CLI let you programmatically create and manage the notification channels that Cloud Monitoring uses to alert you or your on-call team when an alerting policy triggers. Using client libraries or the Google Cloud CLI, you create notification channels from built-in notification-channel descriptors and then reference those channels in your alerting policies.

To configure notification channels in the Google Cloud console instead, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options). The code samples in this document come from the alerting-policy API example in [Example: backup and restore](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api#api-example).

## About the API

The [`NotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels) resource supports operations that let you manage your notification channels. It also supports operations related to managing the `verificationStatus` field of a channel:

  * Sending a verification code
  * Generating a code for copying the verification status of a verified channel to other identical channels in the same or a new project
  * Verifying the channel using the code created by the previous two operations



For more information, see the [`notificationChannels`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels) reference documents.

## Limitations

  * **Deprecated channel types** : The `campfire` and `hipchat` channel types are deprecated. Don't create new channels of these types.
  * **Pub/Sub message storage policies** : If you configure a message storage policy or data residency restrictions for a Pub/Sub topic, then Monitoring might not be able to publish to the topic. For more information, see [`FAILED_PRECONDITION` error](https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications#pubsub-failed-precondition).
  * **Concurrent API calls** : Design your application to call the Cloud Monitoring API from a single thread when creating, modifying, or deleting a notification channel in a Google Cloud project.



## Before you begin

  * To get the permissions that you need to view and configure notification channels by using the Cloud Monitoring API, ask your administrator to grant you the [Monitoring NotificationChannel Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationChannelEditor) (`roles/monitoring.notificationChannelEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

  * Select the tab for how you plan to use the samples on this page:

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### C#

To use the .NET samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Node.js

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### PHP

To use the PHP samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

  * If you plan to use the Google Cloud CLI, then configure the default project:
        
        gcloud config set project PROJECT_ID
        

Before you run the previous command, replace the following:

    * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.



## List the types of notification channels

Monitoring provides a number of built-in notification-channel types. Each of these types is described in a [`NotificationChannelDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors). Each descriptor has a `type` field whose value identifies the channel type when you create a channel instance. To retrieve a list of channel types that you can create with the Cloud Monitoring API or the Google Cloud CLI, enter the following command:
    
    
    $ gcloud beta monitoring channel-descriptors list --format='value(type)'
    campfire
    email
    google_chat
    hipchat
    pagerduty
    pubsub
    slack
    sms
    webhook_basicauth
    webhook_tokenauth
    

If your preferred notification channel isn't supported, consider creating a pipeline that relies on sending your notifications to Pub/Sub. For a Python example that uses Flask, see [Creating custom notifications with Cloud Monitoring and Cloud Run](https://cloud.google.com/blog/products/operations/write-and-deploy-cloud-monitoring-alert-notifications-to-third-party-services). For other examples, see the [cloud-alerting-notification-forwarding Git repository](https://github.com/googlecloudplatform/cloud-alerting-notification-forwarding).

### List all channel types

To retrieve all the channel descriptors in a Google Cloud project, use the `gcloud beta monitoring channel-descriptors list` command or use the [`notificationChannelDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list) API method. The retrieved descriptors are read-only.
    
    
    gcloud beta monitoring channel-descriptors list
    

When successful, the `list` command provides a listing of all the channel descriptors in the specified project. For example, the `email` channel descriptor appears in the list like this:
    
    
    ---
    description: A channel that sends notifications via email.
    displayName: Email
    labels:
    - description: An address to send email.
      key: email_address
    name: projects/[PROJECT_ID]/notificationChannelDescriptors/email
    type: email
    ---
    

All channel descriptors include these fields:

  * `name`: The fully qualified resource name of the channel descriptor.
  * `type`: The part of the name that indicates the type of channel.
  * `displayName`: A description of the `type` field, for display purposes.
  * `description`: A brief description of the channel.
  * `labels`: A set of fields specific to a channel type. Each channel type has its own set of labels.



When a channel is created, it also gets an `enabled` field, with the value `true` by default.

### List a specific channel type

If you are looking for a specific descriptor and you know its name, use `gcloud beta monitoring channel-descriptors describe` or the [`notificationChannelDescriptors.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/get) API method. The name of a channel descriptor has the format `projects/[PROJECT_ID]/notificationChannelDescriptors/[CHANNEL_TYPE]`. `[CHANNEL_TYPE]` must be one of the types previously listed. For example:
    
    
    gcloud beta monitoring channel-descriptors describe email
    
    gcloud beta monitoring channel-descriptors describe projects/[PROJECT_ID]/notificationChannelDescriptors/email
    

See the [`gcloud beta monitoring channel-descriptors list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/channel-descriptors/list) and [`describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/channel-descriptors/describe) references for more information. The `describe` command corresponds to the [`notificationChannelDescriptors.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/get) method in the API.

## Create a notification channel

You can create notification channels for your Google Cloud projects from JSON or YAML files by using the Google Cloud CLI, and you can create them programmatically.

To create a notification channel, you must supply values for the fields in its descriptor. Most of these, like `type`, are common across all notification-channel descriptors; see [`notificationChannelDescriptors`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors).

Each descriptor also has a set of labels, and this set varies across the descriptors. To see the set of labels for a particular descriptor, retrieve the descriptor using the `gcloud beta monitoring channel-descriptors describe` command described in List the types of notification channels. For example, retrieving the `email` channel descriptor shows a single label:
    
    
        labels:
        - description: An address to send email.
          key: email_address
    

The `pubsub` channel descriptor also contains a single label; that label identifies the Pub/Sub topic. However, channels can contain multiple labels. For example, the `slack` channel descriptor has two labels:
    
    
        labels:
        - description: A permanent authentication token provided by Slack. This field is obfuscated by returning only a few characters of the key when fetched.
          key: auth_token
        - description: The Slack channel to which to post notifications.
          key: channel_name
    

Retrieving the `webhook_basicauth` channel descriptor shows several labels:
    
    
        labels:
        - description: The password. The field is obfuscated when the channel is fetched.
          key: password
        - description: The public URL to which to publish the webhook.
          key: url
        - description: The username.
          key: username
    

Whether you create a new channel programmatically or from the command line, the value of the `type` in your specification must match the `type` field in the corresponding notification-channel descriptor. Any required label keys must also match those in the channel descriptor.

Some labels correspond to credentials used to authenticate with the provider. When creating a channel, the values for these labels must be obtained from the provider. Obtaining a credential might involve using an API key-generation page on the provider's website or completing an OAuth login flow with the provider. The specifics of how to obtain such a credential depend on the particular provider.

Channels are enabled by default. If you want to create an inactive channel, you can include the field `enabled` with the value `false`.

**Note:** We recommend that you create multiple notification channels for redundancy purposes. Google Cloud has no control over many of the delivery systems after it has passed a notification to those systems. SMS in particular isn't a fully reliable notification channel type, and it might not be available in certain regions. If you use an SMS notification channel, then also use a different notification channel type as a redundant channel. Additionally, Cloud Mobile App, PagerDuty, webhooks, and Slack notifications are all powered by a single Google Cloud internal service and therefore share a single point of failure. If you use one of these notification channels, then use email or Pub/Sub as the redundant channel.

The following examples illustrate the creation of notification channels.

### Example: Create a Pub/Sub notification channel using the gcloud CLI

To create a notification channel in a Google Cloud project, use the [`gcloud beta monitoring channels create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/channels/create) command. To load the channel from a file, use the `--channel-content-from-file` flag to specify the file.

For example, the following shows the specification of a new `pubsub` notification channel in JSON:
    
    
        {
          "type": "pubsub",
          "displayName": "Notifications",
          "description": "Pub/Sub channel for notifications",
          "labels": {
            "topic": "projects/[PROJECT_ID]/topics/notificationTopic"
          },
        }
    

The `type` value (`pubsub`) and the single label key (`topic`) match the `type` and `labels.key` fields in the corresponding channel descriptor.

The following example creates a new Pub/Sub channel from the `pubsub-channel.json` file:
    
    
    gcloud beta monitoring channels create --channel-content-from-file="pubsub-channel.json"
    

When successful, this command returns the name of the new channel. For example:
    
    
    Created notification channel [projects/[PROJECT_ID]/notificationChannels/1355376463305411567].
    

When you create a `pubsub` notification channel, make sure that you [authorize the notifications service account](https://docs.cloud.google.com/monitoring/support/notification-options#auth-pubsub-service-account) to publish to the topic. Also note that if the topic has a message storage policy or data residency restrictions, Monitoring might not be able to publish to it; see [`FAILED_PRECONDITION` error](https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications#pubsub-failed-precondition).

### Example: Create a notification channel using client libraries

The following examples show how to create a notification channel by using a client library:

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

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\NotificationChannelServiceClient;
    use Google\Cloud\Monitoring\V3\CreateNotificationChannelRequest;
    use Google\Cloud\Monitoring\V3\NotificationChannel;
    
    /**
     * @param string $projectId Your project ID
     */
    function alert_create_channel(string $projectId): void
    {
        $channelClient = new NotificationChannelServiceClient([
            'projectId' => $projectId,
        ]);
        $projectName = 'projects/' . $projectId;
    
        $channel = new NotificationChannel();
        $channel->setDisplayName('Test Notification Channel');
        $channel->setType('email');
        $channel->setLabels(['email_address' => 'fake@example.com']);
        $createNotificationChannelRequest = (new CreateNotificationChannelRequest())
            ->setName($projectName)
            ->setNotificationChannel($channel);
    
        $channel = $channelClient->createNotificationChannel($createNotificationChannelRequest);
        printf('Created notification channel %s' . PHP_EOL, $channel->getName());
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
    
    

### Example: Create a Slack notification channel

To configure a notification channel for a Slack app, do the following:

  1. Configure your Slack app:

     1. If you don't already have a Slack app, follow the [Slack reference documentation](https://api.slack.com/start/quickstart) to create one and install it to your workspace.
     2. Configure your Slack app with OAuth scopes for [`chat:write`](https://api.slack.com/scopes/chat:write) and [`chat:write.public`](https://api.slack.com/scopes/chat:write.public).
     3. Copy the app's Bot User OAuth token.
  2. Create a file that defines the configuration of your notification channel. Include a label where the `auth_token` key has the value of your Slack app's Bot User OAuth token. For example:
         
         {
           "description": "A Slack notification channel",
           "displayName": "Slack",
           "type": "slack",
           "enabled": true,
           "labels": {
             "auth_token": "OAUTH_TOKEN_VALUE",
             "channel_name": "SLACK_CHANNEL_NAME"
           }
         }
         

  3. Run the following command to create the notification channel:
         
         gcloud beta monitoring channels create --channel-content-from-file="FILE_NAME"
         




## List notification channels in a project

To retrieve all the notification channels in a Google Cloud project, use the [`notificationChannels.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/list) method. This method also supports `filter` and `orderBy` options to restrict and sort the results; see [Sorting and Filtering](https://docs.cloud.google.com/monitoring/api/v3/sorting-and-filtering).

If you are looking for a specific channel and you know its name, you can use the [`notificationChannels.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/get) method to retrieve only that channel. The name of a channel has the format `projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]`. For example:
    
    
        projects/[PROJECT_ID]/notificationChannels/1355376463305411567
    

When you retrieve a channel, sensitive values like authentication tokens and API keys might be obfuscated for security reasons. If you are creating a new channel by copying an existing one, any obfuscated values need to be corrected.

### gcloud

To list all the notification channels in a Google Cloud project, use the `gcloud beta monitoring channels list` command:
    
    
    gcloud beta monitoring channels list
    

If successful, the `list` command provides a listing of all the channels in the specified project. For example, the preceding command might return a list that includes the following entries:
    
    
        ---
        description: E-mail channel created by gcloud as a test
        displayName: test e-mail channel
        enabled: false
        labels:
          email_address: user@example.com
        name: projects/[PROJECT_ID]/notificationChannels/1355376463305411567
        type: email
        ---
        description: Pub/Sub channel for notifications
        displayName: Notifications
        enabled: true
        labels:
          topic: projects/[PROJECT_ID]/topics/notificationTopic
        name: projects/[PROJECT_ID]/notificationChannels/1355376463305411567
        type: pubsub
    

To list a single channel instead, use `gcloud beta monitoring channels describe` and specify the name of the channel. For example, this command returns the Pub/Sub channel shown in the preceding listing:
    
    
    gcloud beta monitoring channels describe projects/[PROJECT_ID]/notificationChannels/1355376463305411567
    

See the [`gcloud beta monitoring channels list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/channels/list) and [`describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/channels/describe) references for more information. The `describe` command corresponds to the [`notificationChannels.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/get) method in the API.

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
    
    

## Delete a notification channel from a project

To delete a notification channel from a Google Cloud project, use the [`notificationChannels.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/delete) method and supply the name of the notification channel to delete. The name of a channel is the value of the `name` field, not the `displayName`, in the `NotificationChannel` instance. The name of a channel has the format `projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]`. For example:
    
    
        projects/[PROJECT_ID]/notificationChannels/1355376463305411567
    

By default, if you attempt to delete a channel that is referenced by an alerting policy, then the channel won't be deleted. To force the removal of references from alerting policies and delete the channel, set the `force` option to `true`. This option automatically removes the channel from all referencing policies.

### gcloud

To delete a notification channel, use `gcloud beta monitoring channels delete` and specify the name of the channel to delete. For example, the following command deletes the `email` channel created in another example:
    
    
    gcloud beta monitoring channels delete projects/[PROJECT_ID]/notificationChannels/1355376463305411567
    

See the [`gcloud beta monitoring channels delete`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/channels/delete) reference for more information. 

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
    
    

## Modify a notification channel

To modify a notification channel, use the [`notificationChannels.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/patch) method (in the REST API). Other API implementations and the Google Cloud CLI call this `update` instead of `patch`.

**Note:** You can't update the `verificationStatus` field with an update operation. To change this value, you must use the [`notificationChannels.verify`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/verify) method.

An update operation can wholly replace the existing channel, or it can modify a subset of fields. For example, you can enable and disable the channel. Disabling a channel prevents delivery of notifications to the channel. Disabling a channel is typically more convenient than removing the channel from the alerting policies that refer to it, if the change is intended to be temporary.

### gcloud

To enable a notification channel that is disabled, use the `gcloud beta monitoring channels update` command and provide the `--enabled` flag. The following command enables the `email` notification channel created—in the disabled state—in a previous example:
    
    
    gcloud beta monitoring channels update projects/[PROJECT_ID]/notificationChannels/1355376463305411567 --enabled
    

To disable a notification channel, use the same command and provide the `--no-enabled` flag. See the [`gcloud beta monitoring channels update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/channels/update) reference for more information. The `update` command corresponds to the [`notificationChannels.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/patch) method in the REST API.

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Monitoring.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    partial class AlertSnippets
    {
        public NotificationChannel EnableNotificationChannel(
            string channelName = "projects/your-project-id/notificationChannels/123")
        {
            var client = [NotificationChannelServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannelServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannelServiceClient.html#Google_Cloud_Monitoring_V3_NotificationChannelServiceClient_Create)();
            [NotificationChannel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannel.html) channel = new [NotificationChannel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannel.html)();
            channel.[Enabled](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannel.html#Google_Cloud_Monitoring_V3_NotificationChannel_Enabled) = true;
            channel.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannel.html#Google_Cloud_Monitoring_V3_NotificationChannel_Name) = channelName;
            var fieldMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) { Paths = { "enabled" } };
            channel = client.UpdateNotificationChannel(
                updateMask: fieldMask,
                notificationChannel: channel);
            Console.WriteLine("Enabled {0}.", channel.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.NotificationChannel.html#Google_Cloud_Monitoring_V3_NotificationChannel_Name));
            return channel;
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
    	"github.com/golang/protobuf/ptypes/wrappers"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // enableChannel enables the given channel. channelName should be of the form
    // "projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]".
    func enableChannel(w io.Writer, channelName string) error {
    	ctx := context.Background()
    
    	client, err := monitoring.NewNotificationChannelClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	req := &monitoringpb.UpdateNotificationChannelRequest{
    		UpdateMask: &field_mask.FieldMask{Paths: []string{"enabled"}},
    		NotificationChannel: &monitoringpb.NotificationChannel{
    			Name:    channelName,
    			Enabled: &wrappers.BoolValue{Value: true},
    		},
    	}
    
    	if _, err := client.UpdateNotificationChannel(ctx, req); err != nil {
    		return fmt.Errorf("EnableNotificationChannel: %w", err)
    	}
    
    	fmt.Fprintf(w, "Enabled channel %q", channelName)
    	return nil
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
    
    

## View notification channel logs

You can use the Logs Explorer to view notification channel errors:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter and run your query. For queries specific to notification channel errors, see [Cloud Monitoring queries](https://docs.cloud.google.com/logging/docs/view/query-library#monitoring-filters).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
