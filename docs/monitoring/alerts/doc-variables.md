---
url: https://docs.cloud.google.com/monitoring/alerts/doc-variables/
title: Annotate notifications with user-defined documentation \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:01.483446+00:00
---

# Annotate notifications with user-defined documentation  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/doc-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Annotate notifications with user-defined documentation Stay organized with collections  Save and categorize content based on your preferences. 

Alerting policies let you add custom documentation that Cloud Monitoring includes in notifications. This user-defined documentation can include troubleshooting information and links, and it can help your responders resolve alerts. You can format this documentation with Markdown and add variables; Monitoring replaces variables with details about the alerting policy and monitored data when sending notifications.

## Documentation structure

The documentation of an alerting policy consists of a subject, content, and links. You can configure documentation in the Google Cloud console, the Cloud Monitoring API, and the Google Cloud CLI.

### Subjects

The **subject** of your documentation appears in the subject of notifications for alerts related to your alerting policy. Notification recipients can manage and sort their notifications by subject.

Subject lines are limited to 255 characters. If you don't define a subject in your documentation, then Cloud Monitoring determines the subject line. Subject lines support plain text and [variables](https://docs.cloud.google.com/monitoring/alerts/doc-variables#doc-vars).

###  Cloud Monitoring API

Configure the notification subject line by using the `subject` field of the alerting policy [`documentation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Documentation).

###  Google Cloud console 

Configure the notification subject line by using the **Notification subject line** field in the **Notifications and name** section of the **Create alerting policy** page.

### Content

The **content** of your documentation appears in the following notification types:

  * Email, in the **Policy Documentation** section
  * PagerDuty
  * Pub/Sub
  * Slack
  * Webhooks



We recommend configuring your content so that alert responders can view remediation steps and alert information in notifications related to your alerting policy. For example, you might configure the documentation to include a summary of the alert and information about relevant resources.

Documentation content supports the following:

  * Plain text
  * [Variables](https://docs.cloud.google.com/monitoring/alerts/doc-variables#doc-vars)
  * [Channel-specific controls](https://docs.cloud.google.com/monitoring/alerts/doc-variables#channel-docs)
  * [Markdown](https://docs.cloud.google.com/monitoring/alerts/doc-variables#doc-markdown)




###  Cloud Monitoring API

Configure documentation content by using the `content` field of the alerting policy [`documentation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Documentation).

###  Google Cloud console 

Configure documentation content by using the **Documentation** field in the **Notifications and name** section of the **Create alerting policy** page.

### Links

You can add links to your documentation so that alert responders can access resources such as playbooks, repositories, and Google Cloud dashboards from a notification.

The Cloud Monitoring API lets you define an object that contains the most relevant links for responders. While the Google Cloud console doesn't have a field specifically for links, you can add a section for links in your documentation body.

###  Cloud Monitoring API

You can add links to your documentation by defining one or more [`Link`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Link) objects in the `links` field of the alerting policy [`documentation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Documentation). Each `Link` object consists of a `display_name` and a `url`. You can have up to three links in your documentation.

The following configuration shows the `links` field with one `Link` object representing a URL to an alert playbook. The URL includes a variable so that notification recipients can access the correct playbook based on the monitored resource where the alert occurred:
    
    
    "links" [
      {
        "displayName": "Playbook",
        "url": "https://myownpersonaldomain.com/playbook?name=${resource.type}"
      }
    ]
    

Documentation links added using the `Link` field appear in the following notification types:

  * Email, in the **Quick Links** section
  * PagerDuty
  * Pub/Sub
  * Webhooks



###  Google Cloud console 

You can add links to your documentation content by including them in the **Documentation** field of your alerting policy. For example, the following documentation lists a URL for a customer playbook:
    
    
    ### Troubleshooting and Debug References
    
    Playbook: https://myownpersonaldomain.com/playbook?name=${resource.type}
    

Documentation links added using the Google Cloud console appear with the rest of your documentation content in the following notification types:

  * Email, in the **Policy Documentation** section
  * PagerDuty
  * Pub/Sub
  * Slack
  * Webhooks



## Markdown in documentation content

You can use Markdown to format your documentation content. Documentation content supports the following subset of Markdown tagging:

  * Headers, indicated by initial hash characters.
  * Unordered lists, indicated by initial plus, minus, or asterisk characters.
  * Ordered lists, indicated by an initial number followed by a period.
  * Italic text, indicated by single underscores or asterisks around a phrase.
  * Bold text, indicated by double underscores or asterisks around a phrase.
  * Links, indicated by `[link text](url)` syntax. To add links to your notification, we recommend that you use the Cloud Monitoring API and configure the [`Link`](https://docs.cloud.google.com/monitoring/alerts/doc-variables#add-links) object.



For more information about this tagging, see any Markdown reference, for example, [Markdown guide](https://www.markdownguide.org/basic-syntax).

## Variables in documentation

**Note:** Make sure that the labels upon which your variables depend exist after the time series are aggregated. When a variable depends on a label that doesn't exist, the value of the variable in the notification is `null`. For example, if your aggregation settings group time series by the value of the `zone` label, then after aggregation, you have one time series for each zone. Further, those time series have one label, `zone`. For more information, see [Variable for a metric label has a value of null](https://docs.cloud.google.com/monitoring/alerts/troubleshooting-alerts#null-variables).

To customize the text in your documentation, you can use variables of the form `${varname}`. When the documentation is sent with a notification, the string `${varname}` is replaced with a value drawn from the corresponding Google Cloud resource, as described in the following table.

Variable | Value  
---|---  
`condition.name` | The REST resource name of the condition, such as  
`projects/foo/alertPolicies/1234/conditions/5678`.   
`condition.display_name` | The display name of a condition, such as `CPU usage increasing rapidly`. For log-based alerting policies that you create by using the Logs Explorer, the value of this field is `"Log match condition"`. To customize the value of this field, use the Cloud Monitoring API.  
`log.extracted_label.KEY` |  The value of the label `KEY`, extracted from a log entry. For log-based alerting policies only; for more information, see [ Create a log-based alerting policy by using the Monitoring API](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api).  
`metadata.system_label.KEY` | The value of the system-supplied resource metadata label `KEY`.1  
`metadata.user_label.KEY` | The value of the user-defined resource metadata label `KEY`.1,3  
`metric.type` | The metric type, such as  
`compute.googleapis.com/instance/cpu/utilization`.  
`metric.display_name` | The display name for the metric type, such as `CPU utilization`.  
`metric.label.KEY` | The value of the metric label `KEY`.1  
To find the labels associated with the metric type, see [Metric list](https://docs.cloud.google.com/monitoring/api/metrics). When the value of the variable `${metric.label.KEY}` doesn't start with a digit, a letter, a forward slash (`/`), or an equal sign (`=`), Monitoring omits the label from notifications. When you [migrate a Prometheus alerting rule](https://docs.cloud.google.com/monitoring/promql/promql-migrate), the Prometheus alert field templates `{{$value}}` and `{{humanize $value}}` appear as `${metric.label.value}` in the alerting policy documentation configuration. In this case, `${metric.label.value}` holds the trigger value of the Prometheus alerting rule.  You can also use `${metric.label.value}` when you create PromQL queries in Google Cloud.  
`metric.label.metadata_system_VALUE` | References a PromQL metadata system label, where VALUE is the specific label name, such as `region` or `version`. Example usage: `${metric.label.metadata_system_version}`.  
`metric.label.metadata_user_VALUE` | References a PromQL metadata user label, where VALUE is the specific label name, such as `region` or `name`. Example usage: `${metric.label.metadata_user_name}`.  
`metric_or_resource.labels` |  This variable renders all metric and resource label values as a sorted list of `key-value` pairs. If a metric label and a resource label have the same name, then only the metric label is rendered. When you [migrate a Prometheus alerting rule](https://docs.cloud.google.com/monitoring/promql/promql-migrate), the Prometheus alert field templates `{{$labels}}` and `{{humanize $labels}}` appear as `${metric_or_resource.labels}` in the alerting policy documentation configuration.  
`metric_or_resource.label.KEY` | 

  * If KEY is a valid label, then this variable renders in the notification as the value of `${metric.label.KEY}`.
  * If KEY is a valid resource, then this variable renders in the notification as the value of `${resource.label.KEY}`.
  * If KEY is neither a valid label nor a valid resource, then this variable renders in the notification as an empty string.

When you [migrate a Prometheus alerting rule](https://docs.cloud.google.com/monitoring/promql/promql-migrate), the Prometheus alert field templates `{{$labels.KEY}}` and `{{humanize $labels.KEY}}` appear as `${metric_or_resource.labels.KEY}` in the alerting policy documentation configuration.  
`policy.name` | The REST resource name of the policy, such as `projects/foo/alertPolicies/1234`.  
`policy.display_name` | The display name of a policy, such as `High CPU rate of change`.  
`policy.user_label.KEY` | The value of the user label `KEY`.1Keys must start with a lowercase letter. Keys and values can contain only lowercase letters, digits, underscores, and dashes.  
`project` | The ID of the scoping project of a metrics scope, such as `a-gcp-project`.  
`resource.type` | The monitored-resource type, such as `gce_instance`.  
`resource.project` | The project ID of the monitored resource of the alerting policy.  
`resource.label.KEY` |  The value of the resource label `KEY`.1,2,3  
To find the labels associated with the monitored-resource type, see [Resource list](https://docs.cloud.google.com/monitoring/api/resources).  
  
1 For example, `${resource.label.zone}` is replaced with the value of the `zone` label. The values of these variables are subject to grouping; see `null` values for more information.  
2 To retrieve the value of the `project_id` label on a monitored resource in the alerting policy, use `${resource.project}`.  
3 You can't access user-defined resource metadata labels by using `resource.label.KEY.` Use `metadata.user_label.KEY` instead.

### Usage notes

  * Only the variables in the table are supported. You can't combine them into more complex expressions, like `${varname1 + varname2}`.
  * To include the literal string `${` in your documentation, escape the `$` symbol with a second `$` symbol, and `$${` renders as `${` in your documentation.
  * Alerting policies always display variable strings like `${varname}`.
  * For some notification channels, Cloud Monitoring replaces variable strings like `${varname}` with the corresponding values. For more information, see Variable resolution.
  * When the Google Cloud console displays the details view of an alert, it usually replaces variable strings like `${varname}` with the corresponding values.
  * Verify that the aggregation settings of the condition don't eliminate the label. If the label is eliminated, then the value of the label in the notification is `null`. For more information, see [Variable for a metric label is null](https://docs.cloud.google.com/monitoring/alerts/troubleshooting-alerts#null-variables).

**Note:** Labels that you add to log-based metrics can't be used in template expressions. However, you can display these labels in chart legends and you can filter time series by the label values.

### `null` values

Values for the `metric.*`, `resource.*` and `metadata.*` variables are derived from time series. Their values can be `null` if no values are returned from the time series query.

  * The `resource.label.KEY` and `metric.label.KEY` variables can have `null` values if your alerting policy uses cross-series aggregation (reduction), for example, calculating the SUM across each of the time-series that match a filter. When using cross-series aggregation, any labels _not_ used in grouping are dropped and as a result they render as `null` when the variable is replaced with its value. All labels are retained when there is no cross-series aggregation. For more information, see [Variable for a metric label is null](https://docs.cloud.google.com/monitoring/alerts/troubleshooting-alerts#null-variables).

  * Values for `metadata.*` variables are available only if the labels are explicitly included in a condition's filter or grouping for cross-series aggregation. That is, you must refer to the metadata label in either filter or grouping for it to have a value for the template.




### Variable resolution

Variables in documentation templates are resolved in the following contexts:

  * Notifications sent by using the following notification channels: 
    * Email
    * Google Chat
    * Slack
    * Pub/Sub, JSON schema version 1.2
    * Webhooks, JSON schema version 1.2
    * PagerDuty, JSON schema version 1.2
  * The Google Cloud console alert details view.

**Note:** Variables aren't resolved, but appear as strings like `${varname}`, in other contexts.

## Channel controls

The text in the documentation field can also include special characters used by the notification channel itself to control formatting and notifications.

For example, Slack uses `@` for mentions. You can use `@` to link the notification to a specific user ID. Mentions can't include names. Suppose you include a string like this in the documentation field:
    
    
    <@backendoncall> Alert created based on policy ${policy.display_name}
    

When the documentation field is received by the relevant Slack channel as part of the notification, the previous string causes Slack to send an additional message to the user ID `backendoncall`. The message sent by Slack to the user could contain relevant information from the notification; for example, "Alert created based on policy High CPU rate of change".

These additional options are specific to the channels; for more information on what may be available, consult the documentation provided by the channel vendor.

## Example

The following example shows Google Cloud console and Cloud Monitoring API versions of template documentation for a CPU utilization alerting policy. These examples use an email for the [notification channel type](https://docs.cloud.google.com/monitoring/alerts/using-channels-api#ncd). The documentation templates include several variables to summarize the alert and to reference the alerting policy and condition REST resources.

###  Cloud Monitoring API 
    
    
      "documentation": {
        "content": "### CPU utilization exceeded\n\n### Summary\n\nThe ${metric.display_name} of the ${resource.type} ${resource.label.instance_id} in the project ${resource.project} has exceeded 5% for over 60 seconds.\n\n#### Additional resource information\n\nCondition resource name: ${condition.name}  \nAlerting policy resource name: ${policy.name}",
        "mimeType": "text/markdown",
        "subject": "Alert: ${metric.display_name} exceeded",
        "links": [
          {
            "displayName": "Playbook",
            "url": "https://myownpersonaldomain.com/playbook?name=${resource.type}"
          },
          {
            "displayName": "Repository with debug scripts",
            "url": "https://altostrat.com"
          },
          {
            "displayName": "Google Cloud dashboard",
            "url": "https://example.com"
          }
        ]
      }
    

The following image shows how this template appears in an email notification:

![Example of how documentation renders in a notification. Links are shown in the 'Quick Links' section.](https://docs.cloud.google.com/static/monitoring/images/sample-alert-doc-quicklinks.png)

###  Google Cloud console 
    
    
    ### CPU utilization exceeded
    
    #### Summary
    
    The ${metric.display_name} of the ${resource.type}
    ${resource.label.instance_id} in the project ${resource.project} has
    exceeded 5% for over 60 seconds.
    
    #### Additional resource information
    
    Condition resource name: ${condition.name}  
    Alerting policy resource name: ${policy.name}  
    
    #### Troubleshooting and Debug References
    
    Playbook: https://myownpersonaldomain.com/playbook?name=${resource.type}  
    Repository with debug scripts: https://altostrat.com  
    ${resource.type} dashboard: https://example.com
    

The following image shows how this template appears in an email notification:

![Example of how documentation renders in a notification. Links are shown under a 'Troubleshooting and Debug References' header.](https://docs.cloud.google.com/static/monitoring/images/sample-alert-documentation.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
