---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ContactOrBuilder
title: Interface ContactOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:29.299681+00:00
---

# Interface ContactOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ContactOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ContactOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.6  2.2.0  2.1.11 
    
    
    public interface ContactOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEmail()
    
    
    public abstract String getEmail()

Required. The email address to send notifications to. The email address does not need to be a Google Account.

`string email = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The email.  
  
### getEmailBytes()
    
    
    public abstract ByteString getEmailBytes()

Required. The email address to send notifications to. The email address does not need to be a Google Account.

`string email = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for email.  
  
### getLanguageTag()
    
    
    public abstract String getLanguageTag()

Required. The preferred language for notifications, as a ISO 639-1 language code. See [Supported languages](https://cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages) for a list of supported languages.

`string language_tag = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageTag.  
  
### getLanguageTagBytes()
    
    
    public abstract ByteString getLanguageTagBytes()

Required. The preferred language for notifications, as a ISO 639-1 language code. See [Supported languages](https://cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages) for a list of supported languages.

`string language_tag = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageTag.  
  
### getName()
    
    
    public abstract String getName()

Output only. The identifier for the contact. Format: {resource_type}/{resource_id}/contacts/{contact_id}

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. The identifier for the contact. Format: {resource_type}/{resource_id}/contacts/{contact_id}

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNotificationCategorySubscriptions(int index)
    
    
    public abstract NotificationCategory getNotificationCategorySubscriptions(int index)

Required. The categories of notifications that the contact will receive communications for.

` repeated .google.cloud.essentialcontacts.v1.NotificationCategory notification_category_subscriptions = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[NotificationCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.NotificationCategory)` | The notificationCategorySubscriptions at the given index.  
  
### getNotificationCategorySubscriptionsCount()
    
    
    public abstract int getNotificationCategorySubscriptionsCount()

Required. The categories of notifications that the contact will receive communications for.

` repeated .google.cloud.essentialcontacts.v1.NotificationCategory notification_category_subscriptions = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of notificationCategorySubscriptions.  
  
### getNotificationCategorySubscriptionsList()
    
    
    public abstract List<NotificationCategory> getNotificationCategorySubscriptionsList()

Required. The categories of notifications that the contact will receive communications for.

` repeated .google.cloud.essentialcontacts.v1.NotificationCategory notification_category_subscriptions = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NotificationCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.NotificationCategory)>` | A list containing the notificationCategorySubscriptions.  
  
### getNotificationCategorySubscriptionsValue(int index)
    
    
    public abstract int getNotificationCategorySubscriptionsValue(int index)

Required. The categories of notifications that the contact will receive communications for.

` repeated .google.cloud.essentialcontacts.v1.NotificationCategory notification_category_subscriptions = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of notificationCategorySubscriptions at the given index.  
  
### getNotificationCategorySubscriptionsValueList()
    
    
    public abstract List<Integer> getNotificationCategorySubscriptionsValueList()

Required. The categories of notifications that the contact will receive communications for.

` repeated .google.cloud.essentialcontacts.v1.NotificationCategory notification_category_subscriptions = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for notificationCategorySubscriptions.  
  
### getValidateTime()
    
    
    public abstract Timestamp getValidateTime()

The last time the validation_state was updated, either manually or automatically. A contact is considered stale if its validation state was updated more than 1 year ago.

`.google.protobuf.Timestamp validate_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The validateTime.  
  
### getValidateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getValidateTimeOrBuilder()

The last time the validation_state was updated, either manually or automatically. A contact is considered stale if its validation state was updated more than 1 year ago.

`.google.protobuf.Timestamp validate_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getValidationState()
    
    
    public abstract ValidationState getValidationState()

Output only. The validity of the contact. A contact is considered valid if it is the correct recipient for notifications for a particular resource.

` .google.cloud.essentialcontacts.v1.ValidationState validation_state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ValidationState](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ValidationState)` | The validationState.  
  
### getValidationStateValue()
    
    
    public abstract int getValidationStateValue()

Output only. The validity of the contact. A contact is considered valid if it is the correct recipient for notifications for a particular resource.

` .google.cloud.essentialcontacts.v1.ValidationState validation_state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for validationState.  
  
### hasValidateTime()
    
    
    public abstract boolean hasValidateTime()

The last time the validation_state was updated, either manually or automatically. A contact is considered stale if its validation state was updated more than 1 year ago.

`.google.protobuf.Timestamp validate_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the validateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
