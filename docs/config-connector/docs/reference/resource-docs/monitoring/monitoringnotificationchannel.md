---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/monitoring/monitoringnotificationchannel/
title: MonitoringNotificationChannel \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:51.816975+00:00
---

# MonitoringNotificationChannel  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/monitoring/monitoringnotificationchannel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MonitoringNotificationChannel

**Property** | **Value**  
---|---  
Google Cloud Service Name | Cloud Monitoring  
Google Cloud Service Documentation | [/monitoring/docs/](https://docs.cloud.google.com/monitoring/docs)  
Google Cloud REST Resource Name | v3.projects.notificationChannels  
Google Cloud REST Resource Documentation | [/monitoring/api/ref_v3/rest/v3/projects.notificationChannels](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels)  
Config Connector Resource Short Names | gcpmonitoringnotificationchannel  
gcpmonitoringnotificationchannels  
monitoringnotificationchannel  
Config Connector Service Name | monitoring.googleapis.com  
Config Connector Resource Fully Qualified Name | monitoringnotificationchannels.monitoring.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Annotations

Fields  
---  
`cnrm.cloud.google.com/project-id`  
  
### Spec

#### Schema
    
    
    description: string
    enabled: boolean
    forceDelete: boolean
    labels:
      string: string
    resourceID: string
    sensitiveLabels:
      authToken:
        value: string
        valueFrom:
          secretKeyRef:
            key: string
            name: string
      password:
        value: string
        valueFrom:
          secretKeyRef:
            key: string
            name: string
      serviceKey:
        value: string
        valueFrom:
          secretKeyRef:
            key: string
            name: string
    type: string
    

Fields  
---  
`description` _Optional_ |  `string` An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters.  
`enabled` _Optional_ |  `boolean` Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future.  
`forceDelete` _Optional_ |  `boolean` If true, the notification channel will be deleted regardless of its use in alert policies (the policies will be updated to remove the channel). If false, channels that are still referenced by an existing alerting policy will fail to be deleted in a delete operation.  
`labels` _Optional_ |  `map (key: string, value: string)` Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the NotificationChannelDescriptor.labels of the NotificationChannelDescriptor corresponding to the type field.  
`resourceID` _Optional_ |  `string` Immutable. Optional. The service-generated name of the resource. Used for acquisition only. Leave unset to create a new resource.  
`sensitiveLabels` _Optional_ |  `object` Different notification type behaviors are configured primarily using the the 'labels' field on this resource. This block contains the labels which contain secrets or passwords so that they can be marked sensitive and hidden from plan output. The name of the field, eg: password, will be the key in the 'labels' map in the api request. Credentials may not be specified in both locations and will cause an error. Changing from one location to a different credential configuration in the config will require an apply to update state.  
`sensitiveLabels.authToken` _Optional_ |  `object` An authorization token for a notification channel. Channel types that support this field include: slack.  
`sensitiveLabels.authToken.value` _Optional_ |  `string` Value of the field. Cannot be used if 'valueFrom' is specified.  
`sensitiveLabels.authToken.valueFrom` _Optional_ |  `object` Source for the field's value. Cannot be used if 'value' is specified.  
`sensitiveLabels.authToken.valueFrom.secretKeyRef` _Optional_ |  `object` Reference to a value with the given key in the given Secret in the resource's namespace.  
`sensitiveLabels.authToken.valueFrom.secretKeyRef.key` _Required*_ |  `string` Key that identifies the value to be extracted.  
`sensitiveLabels.authToken.valueFrom.secretKeyRef.name` _Required*_ |  `string` Name of the Secret to extract a value from.  
`sensitiveLabels.password` _Optional_ |  `object` An password for a notification channel. Channel types that support this field include: webhook_basicauth.  
`sensitiveLabels.password.value` _Optional_ |  `string` Value of the field. Cannot be used if 'valueFrom' is specified.  
`sensitiveLabels.password.valueFrom` _Optional_ |  `object` Source for the field's value. Cannot be used if 'value' is specified.  
`sensitiveLabels.password.valueFrom.secretKeyRef` _Optional_ |  `object` Reference to a value with the given key in the given Secret in the resource's namespace.  
`sensitiveLabels.password.valueFrom.secretKeyRef.key` _Required*_ |  `string` Key that identifies the value to be extracted.  
`sensitiveLabels.password.valueFrom.secretKeyRef.name` _Required*_ |  `string` Name of the Secret to extract a value from.  
`sensitiveLabels.serviceKey` _Optional_ |  `object` An servicekey token for a notification channel. Channel types that support this field include: pagerduty.  
`sensitiveLabels.serviceKey.value` _Optional_ |  `string` Value of the field. Cannot be used if 'valueFrom' is specified.  
`sensitiveLabels.serviceKey.valueFrom` _Optional_ |  `object` Source for the field's value. Cannot be used if 'value' is specified.  
`sensitiveLabels.serviceKey.valueFrom.secretKeyRef` _Optional_ |  `object` Reference to a value with the given key in the given Secret in the resource's namespace.  
`sensitiveLabels.serviceKey.valueFrom.secretKeyRef.key` _Required*_ |  `string` Key that identifies the value to be extracted.  
`sensitiveLabels.serviceKey.valueFrom.secretKeyRef.name` _Required*_ |  `string` Name of the Secret to extract a value from.  
`type` _Required_ |  `string` The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of valid values such as "email", "slack", etc...  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    name: string
    observedGeneration: integer
    verificationStatus: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the object's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`name` |  `string` The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The [CHANNEL_ID] is automatically assigned by the server on creation.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`verificationStatus` |  `string` Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require verification or that this specific channel has been exempted from verification because it was created prior to verification being required for channels of this type.This field cannot be modified using a standard UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.  
  
## Sample YAML(s)

### Basicauth Webhook Monitoring Notification Channel
    
    
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringNotificationChannel
    metadata:
      # The metadata.labels field doesn't configure the notification channel
      # Specify notification channel configuration in spec.labels
      labels:
        response-priority: all
        target-user: automation
      name: monitoringnotificationchannel-sample-basicauth-webhook
    spec:
      type: webhook_basicauth
      # The spec.labels field below is for configuring the desired behaviour of the notification channel
      # It does not apply labels to the resource in the cluster
      labels:
        url: http://hooks.example.com/notifications
        username: admin
      description: Sends notifications to indicated webhook URL using HTTP-standard basic authentication. Should be used in conjunction with SSL/TLS to reduce the risk of attackers snooping the credentials.
      sensitiveLabels:
        password:
          valueFrom:
            secretKeyRef:
              key: password
              name: monitoringnotificationchannel-dep-basicauthwebhook
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: monitoringnotificationchannel-dep-basicauthwebhook
    data:
      password: cGFzc3dvcmQK
    

### Disabled Email Monitoring Notification Channel
    
    
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringNotificationChannel
    metadata:
      # The metadata.labels field doesn't configure the notification channel
      # Specify notification channel configuration in spec.labels
      labels:
        response-priority: longterm
        target-user: dev
      name: monitoringnotificationchannel-sample-disabled-email
    spec:
      type: email
      # The spec.labels field below is for configuring the desired behaviour of the notification channel
      # It does not apply labels to the resource in the cluster
      labels:
        email_address: dev@example.com
      description: A disabled channel that would send notifications via email if enabled.
      enabled: false
    

### PubSub Monitoring Notification Channel
    
    
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringNotificationChannel
    metadata:
      # The metadata.labels field doesn't configure the notification channel
      # Specify notification channel configuration in spec.labels
      labels:
        response-priority: all
        target-user: automation
      name: monitoringnotificationchannel-sample-pubsub
    spec:
      type: pubsub
      # The spec.labels field below is for configuring the desired behaviour of the notification channel
      # It does not apply labels to the resource in the cluster
      labels:
        # Replace ${PROJECT_ID?} with the Pub/Sub topic's project ID.
        topic: projects/${PROJECT_ID?}/topics/monitoringnotificationchannel-dep-pubsub
      description: A channel that sends notifications to a Pub/Sub topic.
      enabled: true
    ---
    apiVersion: iam.cnrm.cloud.google.com/v1beta1
    kind: IAMPolicyMember
    metadata:
      name: monitoringnotificationchannel-dep-pubsub
    spec:
      # Replace ${PROJECT_NUMBER?} with your project number.
      member: serviceAccount:service-${PROJECT_NUMBER?}@gcp-sa-monitoring-notification.iam.gserviceaccount.com
      role: roles/pubsub.publisher
      resourceRef:
        kind: PubSubTopic
        name: monitoringnotificationchannel-dep-pubsub
    ---
    apiVersion: pubsub.cnrm.cloud.google.com/v1beta1
    kind: PubSubTopic
    metadata:
      labels:
        label-one: "value-one"
      name: monitoringnotificationchannel-dep-pubsub
    

### Sms Monitoring Notification Channel
    
    
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringNotificationChannel
    metadata:
      # The metadata.labels field doesn't configure the notification channel
      # Specify notification channel configuration in spec.labels
      labels:
        response-priority: intervention
        target-user: on-call
      name: monitoringnotificationchannel-sample-sms
    spec:
      type: sms
      # The spec.labels field below is for configuring the desired behaviour of the notification channel
      # It does not apply labels to the resource in the cluster
      labels:
        number: "12025550196"
      description: A channel that sends notifications via Short Message Service (SMS).
      enabled: true
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
