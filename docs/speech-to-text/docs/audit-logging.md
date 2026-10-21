---
url: https://docs.cloud.google.com/speech-to-text/docs/audit-logging/
title: Speech-to-Text audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:28.502492+00:00
---

# Speech-to-Text audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Speech-to-Text audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Speech-to-Text. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Speech-to-Text audit logs use the service name `speech.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="speech.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Speech-to-Text generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.speech.v2.Speech.GetConfig`  
`google.cloud.speech.v2.Speech.GetRecognizer`  
`google.cloud.speech.v2.Speech.ListRecognizers`  
`ADMIN_WRITE` | `google.cloud.speech.v2.Speech.CreateRecognizer` (LRO)  
`google.cloud.speech.v2.Speech.DeleteRecognizer` (LRO)  
`google.cloud.speech.v2.Speech.UndeleteRecognizer` (LRO)  
`google.cloud.speech.v2.Speech.UpdateConfig`  
`google.cloud.speech.v2.Speech.UpdateRecognizer` (LRO)  
`DATA_READ` | `google.cloud.speech.v2.Speech.BatchRecognize` (LRO)  
`google.cloud.speech.v2.Speech.GetCustomClass`  
`google.cloud.speech.v2.Speech.GetPhraseSet`  
`google.cloud.speech.v2.Speech.ListCustomClasses`  
`google.cloud.speech.v2.Speech.ListPhraseSets`  
`google.cloud.speech.v2.Speech.Recognize`  
`google.cloud.speech.v2.Speech.StreamingRecognize`  
`DATA_WRITE` | `google.cloud.speech.v2.Speech.CreateCustomClass` (LRO)  
`google.cloud.speech.v2.Speech.CreatePhraseSet` (LRO)  
`google.cloud.speech.v2.Speech.DeleteCustomClass` (LRO)  
`google.cloud.speech.v2.Speech.DeletePhraseSet` (LRO)  
`google.cloud.speech.v2.Speech.UndeleteCustomClass` (LRO)  
`google.cloud.speech.v2.Speech.UndeletePhraseSet` (LRO)  
`google.cloud.speech.v2.Speech.UpdateCustomClass` (LRO)  
`google.cloud.speech.v2.Speech.UpdatePhraseSet` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Speech-to-Text.

### `google.cloud.speech.v2.Speech`

The following audit logs are associated with methods belonging to `google.cloud.speech.v2.Speech`.

#### `BatchRecognize`

  * **Method** : `google.cloud.speech.v2.Speech.BatchRecognize`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.recognizers.recognize - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.BatchRecognize" `  




#### `CreateCustomClass`

  * **Method** : `google.cloud.speech.v2.Speech.CreateCustomClass`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.customClasses.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.CreateCustomClass" `  




#### `CreatePhraseSet`

  * **Method** : `google.cloud.speech.v2.Speech.CreatePhraseSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.phraseSets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.CreatePhraseSet" `  




#### `CreateRecognizer`

  * **Method** : `google.cloud.speech.v2.Speech.CreateRecognizer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `speech.recognizers.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.CreateRecognizer" `  




#### `DeleteCustomClass`

  * **Method** : `google.cloud.speech.v2.Speech.DeleteCustomClass`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.customClasses.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.DeleteCustomClass" `  




#### `DeletePhraseSet`

  * **Method** : `google.cloud.speech.v2.Speech.DeletePhraseSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.phraseSets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.DeletePhraseSet" `  




#### `DeleteRecognizer`

  * **Method** : `google.cloud.speech.v2.Speech.DeleteRecognizer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `speech.recognizers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.DeleteRecognizer" `  




#### `GetConfig`

  * **Method** : `google.cloud.speech.v2.Speech.GetConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.config.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.GetConfig" `  




#### `GetCustomClass`

  * **Method** : `google.cloud.speech.v2.Speech.GetCustomClass`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.customClasses.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.GetCustomClass" `  




#### `GetPhraseSet`

  * **Method** : `google.cloud.speech.v2.Speech.GetPhraseSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.phraseSets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.GetPhraseSet" `  




#### `GetRecognizer`

  * **Method** : `google.cloud.speech.v2.Speech.GetRecognizer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.recognizers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.GetRecognizer" `  




#### `ListCustomClasses`

  * **Method** : `google.cloud.speech.v2.Speech.ListCustomClasses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.customClasses.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.ListCustomClasses" `  




#### `ListPhraseSets`

  * **Method** : `google.cloud.speech.v2.Speech.ListPhraseSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.phraseSets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.ListPhraseSets" `  




#### `ListRecognizers`

  * **Method** : `google.cloud.speech.v2.Speech.ListRecognizers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.recognizers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.ListRecognizers" `  




#### `Recognize`

  * **Method** : `google.cloud.speech.v2.Speech.Recognize`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.recognizers.recognize - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.Recognize" `  




#### `StreamingRecognize`

  * **Method** : `google.cloud.speech.v2.Speech.StreamingRecognize`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.recognizers.recognize - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.StreamingRecognize" `  




#### `UndeleteCustomClass`

  * **Method** : `google.cloud.speech.v2.Speech.UndeleteCustomClass`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.customClasses.undelete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.UndeleteCustomClass" `  




#### `UndeletePhraseSet`

  * **Method** : `google.cloud.speech.v2.Speech.UndeletePhraseSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.phraseSets.undelete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.UndeletePhraseSet" `  




#### `UndeleteRecognizer`

  * **Method** : `google.cloud.speech.v2.Speech.UndeleteRecognizer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `speech.recognizers.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.UndeleteRecognizer" `  




#### `UpdateConfig`

  * **Method** : `google.cloud.speech.v2.Speech.UpdateConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `speech.config.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.UpdateConfig" `  




#### `UpdateCustomClass`

  * **Method** : `google.cloud.speech.v2.Speech.UpdateCustomClass`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.customClasses.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.UpdateCustomClass" `  




#### `UpdatePhraseSet`

  * **Method** : `google.cloud.speech.v2.Speech.UpdatePhraseSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `speech.phraseSets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.UpdatePhraseSet" `  




#### `UpdateRecognizer`

  * **Method** : `google.cloud.speech.v2.Speech.UpdateRecognizer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `speech.recognizers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.speech.v2.Speech.UpdateRecognizer" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.speech.v1.Adaptation.CreateCustomClass`
  * `google.cloud.speech.v1.Adaptation.CreatePhraseSet`
  * `google.cloud.speech.v1.Adaptation.DeleteCustomClass`
  * `google.cloud.speech.v1.Adaptation.DeletePhraseSet`
  * `google.cloud.speech.v1.Adaptation.GetCustomClass`
  * `google.cloud.speech.v1.Adaptation.GetPhraseSet`
  * `google.cloud.speech.v1.Adaptation.ListCustomClasses`
  * `google.cloud.speech.v1.Adaptation.ListPhraseSet`
  * `google.cloud.speech.v1.Adaptation.UpdateCustomClass`
  * `google.cloud.speech.v1.Adaptation.UpdatePhraseSet`
  * `google.cloud.speech.v1.Speech.LongRunningRecognize`
  * `google.cloud.speech.v1.Speech.Recognize`
  * `google.cloud.speech.v1.Speech.StreamingRecognize`
  * `google.cloud.speech.v1p1beta1.Adaptation.CreateCustomClass`
  * `google.cloud.speech.v1p1beta1.Adaptation.CreatePhraseSet`
  * `google.cloud.speech.v1p1beta1.Adaptation.DeleteCustomClass`
  * `google.cloud.speech.v1p1beta1.Adaptation.DeletePhraseSet`
  * `google.cloud.speech.v1p1beta1.Adaptation.GetCustomClass`
  * `google.cloud.speech.v1p1beta1.Adaptation.GetPhraseSet`
  * `google.cloud.speech.v1p1beta1.Adaptation.ListCustomClasses`
  * `google.cloud.speech.v1p1beta1.Adaptation.ListPhraseSet`
  * `google.cloud.speech.v1p1beta1.Adaptation.UpdateCustomClass`
  * `google.cloud.speech.v1p1beta1.Adaptation.UpdatePhraseSet`
  * `google.cloud.speech.v1p1beta1.Speech.LongRunningRecognize`
  * `google.cloud.speech.v1p1beta1.Speech.Recognize`
  * `google.cloud.speech.v1p1beta1.Speech.StreamingRecognize`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
