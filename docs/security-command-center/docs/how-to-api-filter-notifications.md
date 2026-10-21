---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications/
title: Filtering notifications \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:50.539360+00:00
---

# Filtering notifications  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Filtering notifications Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page shows example filters that you can use with the Security Command Center API notifications feature, and the messages that it exports to [Pub/Sub](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) or [BigQuery](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query). You can filter notifications by any [finding field](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#resource:-finding), including:

  * `parent`
  * `state`
  * `resource_name`
  * `category`
  * `source_properties` (v1 API only)
  * `security_marks`



You can also use standard operators as part of your filter string:

  * `AND` to include fields that contain all of a set of values
  * `OR` to include fields that contain one of a set of values
  * `-` to exclude fields that contain a specific value
  * Parentheses to group a set of values, for example:

`(category = \"BUCKET_LOGGING_DISABLED\" OR category = \"CLUSTER_LOGGING_DISABLED\") AND state = \"ACTIVE\"`




## Setting up a source filter

Every Security Command Center finding includes the source ID of the security source provider. For example, a finding from Security Health Analytics includes a source ID that's unique to Security Health Analytics. The source ID is used in a `NotificationConfig` filter to specify the provider findings that you want to send to the notifications Pub/Sub topic or BigQuery dataset.

### Step 1: Getting the source ID

Use the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) to get a provider's source ID.

### Console

  1. Go to the Security Command Center **Findings** page in the Google Cloud console.  
[Go to the Findings page](https://console.cloud.google.com/security/command-center/findings)  

  2. Select the organization for which you want to create a notifications filter. The **Findings** page opens.
  3. In the **Quick filters** panel, go to the **Source display name** section and select the name of the provider that you want to use to filter the notifications results.
  4. In the **Category** column of the **Findings query results** panel, display the finding details panel by clicking the name of one of the findings.
  5. On the findings detail panel, click the **JSON** tab. The complete JSON for the finding is displayed.
  6. In the JSON, copy the value of the `parent` attribute. For example:
         
         "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID"

The IDs are represented by the following:

     * `ORGANIZATION_ID`: the ID of the organization of the parent source provider.
     * `SOURCE_ID`: the ID of the parent source provider.



### gcloud

To retrieve a source ID, run the following command:
    
    
      gcloud scc sources describe ORGANIZATION_ID --source-display-name="SOURCE_NAME"
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID.
  * `SOURCE_NAME`: the name of the service for which you want the source ID. Use the name of any finding provider, including Security Command Center's built-in services, Security Health Analytics, Web Security Scanner, Event Threat Detection, and Container Threat Detection.



The output for the gcloud CLI command resembles the following and includes the source ID:
    
    
     {
       "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
       "displayName": "example-source",
       "description": "A source that creates findings."
     }
    

Next, use the organization ID and source ID to create a notifications filter.

### Step 2: Creating a filter

To create a notifications filter, you [create](https://docs.cloud.google.com/security-command-center/docs/how-to-api-manage-notifications#create-config) a new `NotificationConfig`.

You can add a filter to the `NotificationConfig` file to include or exclude a specific source:

  * Filter findings to send notifications from only the specified source:
        
        state = \"ACTIVE\" AND parent = \"organizations/$ORGANIZATION_ID/sources/$SOURCE_ID\"
        

  * Filter findings to send notifications from all sources except the specified source:
        
        state = \"ACTIVE\" AND -parent = \"organizations/$ORGANIZATION_ID/sources/$SOURCE_ID\"
        




For more examples of filters you can use, see [Listing security findings using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings).

## Filtering findings by category and state when using Pub/Sub topics

The following sections provide examples of how to create a filter for specific sources and finding types, and the notification message that it sends to your Pub/Sub topic.

If you are using BigQuery datasets instead of Pub/Sub topics, the findings and related fields are described in [Export findings to BigQuery for analysis](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query).

### Security Health Analytics

This Security Health Analytics example uses the following filters:
    
    
    category = \"OPEN_FIREWALL\" AND state = \"ACTIVE\"
    

For more information about the types of findings that Security Health Analytics creates, see the [Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics-findings) page.

The Pub/Sub message for the Security Health Analytics filtered finding notification looks like the following:
    
    
    {
       "notificationConfigName": "organizations/ORGANIZATION_ID/notificationConfigs/security-health-analytics-active-findings",
       "finding": {
         "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
         "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
         "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/global/firewalls/,
         "state": "ACTIVE",
         "category": "OPEN_FIREWALL",
         "externalUri": "https://console.cloud.google.com/networking/firewalls/details/default-allow-icmp?project\u003PROJECT_ID",
         "sourceProperties": {
           "ReactivationCount": 0.0,
           "Allowed": "[{\"ipProtocol\":\"icmp\"}]",
           "WhitelistInstructions": "Add the security mark \"allow_open_firewall_rule\" to the asset with a value of \"true\" to prevent this finding from being activated again.",
           "Recommendation": "Restrict the firewall rules at: https://console.cloud.google.com/networking/firewalls/details/default-allow-icmp?project\u003PROJECT_ID",
           "AllowedIpRange": "All",
           "ActivationTrigger": "Allows all IP addresses",
           "SourceRange": "[\"0.0.0.0/0\"]",
           "ScanRunId": "2019-04-06T08:50:58.832-07:00",
           "SeverityLevel": "High",
           "ProjectId": "PROJECT_ID",
           "AssetCreationTime": "2019-03-28t17:58:54.409-07:00",
           "ScannerName": "FIREWALL_SCANNER",
           "Explanation": "Firewall rules that allow connections from all IP addresses or on all ports may expose resources to attackers."
         },
         "securityMarks": {
           "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks",
           "marks": {
             "sccquery152cd5aa66ea4bc8a672d8186a125580": "true",
             "sccquerya3cf2270123f4e91b84a3e613d2cac67": "true"
           }
         },
         "eventTime": "2019-09-22T21:26:57.189Z",
         "createTime": "2019-03-29T15:51:26.435Z"
       }
     }
    

### Anomaly Detection

This Anomaly Detection notification example uses the following filters:
    
    
    category = \"resource_involved_in_coin_mining\" AND state = \"ACTIVE\"
    

For more information about the types of findings that Anomaly Detection creates, see the [Viewing vulnerabilities and threats](https://docs.cloud.google.com/security-command-center/docs/how-to-view-vulnerabilities-threats#anomaly_detection) page.

The Pub/Sub message for the Anomaly Detection filtered finding notification looks like the following:
    
    
    {
       "notificationConfigName": "organizations/ORGANIZATION_ID/notificationConfigs/cloud-anomaly-detection-active-findings",
       "finding": {
         "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
         "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
         "resourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
         "state": "ACTIVE",
         "category": "resource_involved_in_coin_mining",
         "sourceProperties": {
           "vm_ips": "35.231.191.191",
           "end_time_usec": "1569003180000000",
           "abuse_target_ips": "54.38.176.231",
           "end_datetime_UTC": "2019-09-20 18:13:00 UTC",
           "urls": "swap2.luckypool.io, bitcash.luckypool.io",
           "vm_host_and_zone_names": "ubuntu-1804-tp100-gminer:us-east1-b",
           "finding_type": "Abuse originating from a resource in your organization.",
           "start_time_usec": "1569002700000000",
           "action_taken": "Notification sent",
           "summary_message": "We have recently detected activity on your Google Cloud Platform/APIs project that violates our Terms of Service or Acceptable Use Policy.",
           "start_datetime_UTC": "2019-09-20 18:05:00 UTC"
         },
         "securityMarks": {
           "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks",
           "marks": {
             "teste123": "true",
             "sccquery94c23b35ea0b4f8388268415a0dc6c1b": "true"
           }
         },
         "eventTime": "2019-09-20T18:59:00Z",
         "createTime": "2019-05-16T14:16:35.674Z"
       }
     }
    

### Event Threat Detection

This Event Threat Detection example uses the following filters:
    
    
    category = \"Persistence: Iam Anomalous Grant\" AND state = \"ACTIVE\"
    

For more information about the types of findings that Event Threat Detection creates, see the [Viewing vulnerabilities and threats](https://docs.cloud.google.com/security-command-center/docs/how-to-view-vulnerabilities-threats#etd) page.

The Pub/Sub message for the Event Threat Detection filtered finding notification looks like the following:
    
    
    {
      "notificationConfigName": "organizations/ORGANIZATION_ID/notificationConfigs/event-threat-detection-active-findings",
      "finding": {
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "resourceName": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID",
        "state": "ACTIVE",
        "category": "Persistence: IAM Anomalous Grant",
        "sourceProperties": {
          "sourceId": {
            "organizationNumber": "ORGANIZATION_ID",
            "customerOrganizationNumber": "ORGANIZATION_ID"
          },
          "detectionCategory": {
            "technique": "persistence",
            "indicator": "audit_log",
            "ruleName": "iam_anomalous_grant",
            "subRuleName": "external_member_added_to_policy"
          },
          "detectionPriority": "HIGH",
          "evidence": [{
            "sourceLogId": {
              "timestamp": {
                "seconds": "1601066317",
                "nanos": 4.63E8
              },
              "insertId": "INSERT_ID"
            }
          }],
          "properties": {
            "sensitiveRoleGrant": {
              "principalEmail": "PRINCIPAL_EMAIL@gmail.com",
              "bindingDeltas": [{
                "action": "ADD",
                "role": "roles/owner",
                "member": "user:USER_EMAIL@gmail.com"
              }, {
                "action": "REMOVE",
                "role": "roles/viewer",
                "member": "user:USER_EMAIL@gmail.com"
              }],
              "members": ["USER_EMAIL@gmail.com"]
            }
          },
          "findingId": "FINDING_ID"
        },
        "securityMarks": {
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks"
        },
        "eventTime": "2020-09-25T20:38:39.441Z",
        "createTime": "2020-09-25T20:38:40.667Z"
      }
    }
    

### Sensitive Data Protection

This Sensitive Data Protection example uses the following filters:
    
    
    category = \"CREDIT_CARD_NUMBER\" AND state = \"ACTIVE\"
    

For more information about the types of findings that Sensitive Data Protection creates, see the [Viewing vulnerabilities and threats](https://docs.cloud.google.com/security-command-center/docs/how-to-view-vulnerabilities-threats#dlp) page.

The Pub/Sub message for the Sensitive Data Protection filtered finding notification looks like the following:
    
    
    {
       "notificationConfigName": "organizations/ORGANIZATION_ID/notificationConfigs/dlp-data-discovery-active-findings",
       "finding": {
         "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
         "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
         "resourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
         "state": "ACTIVE",
         "category": "CREDIT_CARD_NUMBER",
         "externalUri": "https://console.cloud.google.com/dlp/projects/PROJECT_ID/dlpJobs/i-7536622736814356939;source\u003d5",
         "sourceProperties": {
           "COUNT": 2.0,
           "JOB_NAME": "projects/PROJECT_ID/dlpJobs/i-7536622736814356939",
           "FULL_SCAN": false
         },
         "securityMarks": {
           "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks",
           "marks": {
             "priority": "p1",
             "sccquerya3cf2270123f4e91b84a3e613d2cac67": "true"
           }
         },
         "eventTime": "2019-09-16T23:21:19.650Z",
         "createTime": "2019-04-22T23:18:17.731Z"
       }
     }
    

### Finding deletion notifications and filters

When deletion notifications are enabled on an export configuration, filter expressions (such as `state = "ACTIVE"`) evaluate against the finding's attributes at the time of deletion.

If the finding's pre-deletion attributes match the filter, the deletion notification is exported to the Pub/Sub topic or BigQuery dataset with `"deletedFinding": true` (in the Pub/Sub JSON payload) or `deleted_finding = true` (in BigQuery).

The event time in the notification is the time the finding was deleted in Security Command Center.

When deletion notifications are disabled, findings deleted from Security Command Center don't generate notifications.

## What's next

  * Learn more about [accessing Security Command Center using a client library](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).
  * Learn how to [list security findings using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
