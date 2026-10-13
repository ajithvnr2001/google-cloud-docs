---
url: https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse/
title: FetchEffectiveSettingsResponse \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:18.495016+00:00
---

# FetchEffectiveSettingsResponse  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  FetchEffectiveSettingsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ServiceAccountApproverSettings
    * JSON representation
  * EmailNotificationSettings
    * JSON representation
  * DisableAllNotifications
  * CustomNotificationBehavior
    * JSON representation
  * RequesterNotifications
    * JSON representation
  * AdminNotifications
    * JSON representation
  * ApproverNotifications
    * JSON representation



The effective value of the settings at the given location resource, evaluated based on the crm resource hierarchy.

JSON representation  
---  
      
    
    {
      "parent": string,
      "serviceAccountApproverSettings": {
        object ([ServiceAccountApproverSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#ServiceAccountApproverSettings))
      },
      "emailNotificationSettings": {
        object ([EmailNotificationSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#EmailNotificationSettings))
      }
    }  
  
Fields  
---  
`parent` |  `string` Output only. The resource on which the settings are effective. Possible formats:

  * `projects/{project-number|project-id}/locations/{region}`
  * `folders/{folder-number}/locations/{region}`
  * `organizations/{organization-number}/locations/{region}`

  
`serviceAccountApproverSettings` |  `object (`[ServiceAccountApproverSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#ServiceAccountApproverSettings)`)` Output only. Effective settings for allowing service account as approvers.  
`emailNotificationSettings` |  `object (`[EmailNotificationSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#EmailNotificationSettings)`)` Output only. `EmailNotificationSettings` defines effective node-wide email notification preferences for various PAM events.  
  
## ServiceAccountApproverSettings

This controls whether service accounts are allowed to approve grants or can be designated as approvers within PAM entitlements.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "source": string
    }  
  
Fields  
---  
`enabled` |  `boolean` Output only. Indicates whether service account is allowed to grant approvals.  
`source` |  `string` Output only. The resource from which the service account approver setting is inherited. This field remains empty if the setting is not defined at either the parent or resource level, in which case PAM's default behavior is applied.  
  
## EmailNotificationSettings

`EmailNotificationSettings` reflects the effective node-wide email notification settings.

JSON representation  
---  
      
    
    {
      "source": string,
    
      // Union field notification_behavior can be only one of the following:
      "disableAllNotifications": {
        object ([DisableAllNotifications](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#DisableAllNotifications))
      },
      "customNotificationBehavior": {
        object ([CustomNotificationBehavior](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#CustomNotificationBehavior))
      }
      // End of list of possible types for union field notification_behavior.
    }  
  
Fields  
---  
`source` |  `string` Output only. The name of the resource from which the notification behavior is inherited. This field remains empty if the setting is not defined at either the parent or resource level, in which case PAM's default behavior is applied.  
Union field `notification_behavior`. Notification behavior. `notification_behavior` can be only one of the following:  
`disableAllNotifications` |  `object (`[DisableAllNotifications](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#DisableAllNotifications)`)` Output only. Disable all notifications.  
`customNotificationBehavior` |  `object (`[CustomNotificationBehavior](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#CustomNotificationBehavior)`)` Output only. Granular settings of notifications.  
  
## DisableAllNotifications

This type has no fields.

This option indicates that all email notifications are disabled.

## CustomNotificationBehavior

`CustomNotificationBehavior` reflects the granular notification delivery settings for specific events and personas, as configured by the admin.

JSON representation  
---  
      
    
    {
      "requesterNotifications": {
        object ([RequesterNotifications](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#RequesterNotifications))
      },
      "adminNotifications": {
        object ([AdminNotifications](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#AdminNotifications))
      },
      "approverNotifications": {
        object ([ApproverNotifications](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#ApproverNotifications))
      }
    }  
  
Fields  
---  
`requesterNotifications` |  `object (`[RequesterNotifications](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#RequesterNotifications)`)` Output only. Requester email notifications.  
`adminNotifications` |  `object (`[AdminNotifications](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#AdminNotifications)`)` Output only. Admin email notifications.  
`approverNotifications` |  `object (`[ApproverNotifications](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/FetchEffectiveSettingsResponse#ApproverNotifications)`)` Output only. Approver email notifications.  
  
## RequesterNotifications

Email notifications specific to Requesters.

JSON representation  
---  
      
    
    {
      "notifyEntitlementAssigned": boolean,
      "notifyGrantActivated": boolean,
      "notifyGrantDenied": boolean,
      "notifyGrantExpired": boolean,
      "notifyGrantEnded": boolean,
      "notifyGrantRevoked": boolean,
      "notifyGrantExternallyModified": boolean,
      "notifyGrantActivationFailed": boolean,
      "notifyGrantActivationScheduled": boolean
    }  
  
Fields  
---  
`notifyEntitlementAssigned` |  `boolean` Output only. Notification delivery for entitlement assigned.  
`notifyGrantActivated` |  `boolean` Output only. Notification delivery for grant activated.  
`notifyGrantDenied` |  `boolean` Output only. Notification delivery for grant denied.  
`notifyGrantExpired` |  `boolean` Output only. Notification delivery for grant request expired.  
`notifyGrantEnded` |  `boolean` Output only. Notification delivery for grant ended.  
`notifyGrantRevoked` |  `boolean` Output only. Notification delivery for grant revoked.  
`notifyGrantExternallyModified` |  `boolean` Output only. Notification delivery for grant externally modified.  
`notifyGrantActivationFailed` |  `boolean` Output only. Notification delivery for grant activation failed.  
`notifyGrantActivationScheduled` |  `boolean` Output only. Notification delivery for grant activation scheduled.  
  
## AdminNotifications

Email notifications specific to Admins.

JSON representation  
---  
      
    
    {
      "notifyGrantActivated": boolean,
      "notifyGrantEnded": boolean,
      "notifyGrantExternallyModified": boolean,
      "notifyGrantActivationFailed": boolean,
      "notifyGrantActivationScheduled": boolean
    }  
  
Fields  
---  
`notifyGrantActivated` |  `boolean` Output only. Notification delivery for grant activated.  
`notifyGrantEnded` |  `boolean` Output only. Notification delivery for grant ended.  
`notifyGrantExternallyModified` |  `boolean` Output only. Notification delivery for grant externally modified.  
`notifyGrantActivationFailed` |  `boolean` Output only. Notification delivery for grant activation failed.  
`notifyGrantActivationScheduled` |  `boolean` Output only. Notification delivery for grant being scheduled for activation.  
  
## ApproverNotifications

Email notifications specific to Approvers.

JSON representation  
---  
      
    
    {
      "notifyPendingApproval": boolean
    }  
  
Fields  
---  
`notifyPendingApproval` |  `boolean` Output only. Notification delivery for pending approval.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-13 UTC."],[],[]] 
