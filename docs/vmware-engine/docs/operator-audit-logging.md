---
url: https://docs.cloud.google.com/vmware-engine/docs/operator-audit-logging/
title: VMware Engine operator audit logging information \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:16.841873+00:00
---

# VMware Engine operator audit logging information  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/operator-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Engine operator audit logging information 

Activities of Google Cloud operators or support personnel on your private cloud are generated as audit logs. When manual interaction from the Google Cloud logs side is required, Google Cloud monitors the support representative's actions so that you can see what was done to your resource.

The `protoPayload.metadata` field is typed and unique to the operator and [system audit logging](https://docs.cloud.google.com/vmware-engine/docs/system-audit-logging) methods.

`insertID`, `logName`, `protopayload`, `receiveTimestamp`, `resource`, and `timestamp` follow [LogEntry](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) methods.

`protopayload.@type`, `protopayload.authenticationInfo`, `protopayload.methodName`, `protopayload.resourceName`, and `protopayload.serviceName` follow [AuditLog](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog) methods.

An individual entry in a log.

JSON representation  
---  
      
    
    {
      "insertID": string,
      "logName": string,
      "protoPayload": {
        "@type": string,
        "authenticationInfo": {
          "principalEmail": string
        },
        "metadata" [(VMwareEngineAuditMetadata)](https://docs.cloud.google.com/vmware-engine/docs/operator-audit-logging#FIELDS): {
          "@type": string,
          "message": string,
          "operationState": string,
          "operationType": string,
          "resourceType": string
        },
        "methodName": string,
        "resourceName": string,
        "serviceName": string
      },
      "receiveTimestamp": string,
      "resource": {
        "labels": {
          "method": string,
          "project_id": string,
          "service": string,
        },
        "type": string
      },  
      "timestamp": string
    }  
  
VMwareEngineAuditMetadata  
---  
@type |  `string` URI of identifying the type of the metadata. Example: "type.googleapis.com/google.cloud.audit.VMwareEngineAuditMetadata"  
message |  `string` The short description of action that was performed for you. Example: "Replacement of failed node `node-1` with new node `node-2` complete"- indicates that failed node removal was successful in your private cloud.  
operationState |  `string` Indicates the state of action. The value can be one of the following: STARTED, COMPLETED, FAILED, CANCELED, OPERATION_STATE_UNSPECIFIED. Example: COMPLETED - the action was fully executed successfully. STARTED - action was started. FAILED - action execution was unsuccessful. `CANCELED` - action execution was canceled. OPERATION_STATE_UNSPECIFIED - action state is not determined.  
operationType |  `string` Indicates the type of operation. The value can be one of the following: OPERATION_TYPE_UNSPECIFIED, CREATE, UPDATE, DELETE. Example: CREATE - the operation created some resource for you. UPDATE - updated some resource. DELETE - deleted some resource. OPERATION_TYPE_UNSPECIFIED - operation type couldn't be determined.  
resourceType |  `string` Indicates the type of the resource on which the action is performed. Example: PRIVATE_CLOUD - the action was performed on a private cloud. This can mean that some node was removed from or added to the private cloud or the private cloud itself was removed or created.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
