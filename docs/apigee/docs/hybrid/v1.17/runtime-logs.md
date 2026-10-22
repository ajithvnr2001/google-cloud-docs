---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/runtime-logs/
title: Runtime logs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:59.002713+00:00
---

# Runtime logs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/runtime-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Runtime logs Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/runtime-logs.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/runtime-logs.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/runtime-logs.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/runtime-logs.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/runtime-logs.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/runtime-logs.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/runtime-logs.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/runtime-logs.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/runtime-logs.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/runtime-logs.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/runtime-logs.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/runtime-logs.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/runtime-logs.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/runtime-logs.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/runtime-logs.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/runtime-logs.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/runtime-logs.html)



Use the runtime logs to help diagnose problems with the `apigee-runtime` pods. Each runtime pod contains a message processor, which is responsible for processing API proxy traffic, executing policies, routing requests, and more.

## Using runtime logs

Logs are a good way to troubleshoot problems with your installation. See [Logging](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/logging) for details. 

###  Use the logs command 

You can view runtime system logs using the `kubectl logs` command. For example: 
    
    
    kubectl logs -f -n APIGEE_NAMESPACE apigee-runtime-apigee-gcp-prod1-test-blue-hd77q

### Contract version information

The following table briefly describes log entries related to loading the contract from the management plane: 

**Log Entry** | **Meaning**  
---|---  
`hybrid-runtime Apigee-Timer-9 INFO RUNTIME-SYNC-SERVICE - RuntimeSyncServiceImpl.updateToVersion() : Switched to newer version 750 from version null` | The MP changed to a newer version of the configuration contract.   
`hybrid-runtime Apigee-Timer-6 INFO RUNTIME-SYNC-SERVICE - RuntimeSyncServiceImpl.loadLatestVersionIfAvailable() : Found a newer version 750` | The MP loaded the latest contract configuration version from `version.properties`.   
`hybrid-runtime Apigee-Timer-6 INFO RUNTIME-SYNC-SERVICE - RuntimeSyncServiceImpl.updateToVersion() : Attempting to update to a newer version 750` | The MP is updating to a newer version of the configuration contract.   
`hybrid-runtime Apigee-Timer-6 INFO RUNTIME-SYNC-SERVICE - RuntimeSyncServiceImpl.updateToVersion() : Switched to newer version 751 from version 750` | The MP loaded the latest contract configuration version from `version.properties`.   
  
### Deployment errors

The following runtime errors relate to proxy deployments: 

**Log Entry** | **Meaning**  
---|---  
`hybrid-runtime org:hybrid env:prod Apigee-Main-6 ERROR i.a.h.e.i.HermesEngineImpl - HermesEngineImpl.handleHermesException() : Keyspace cache_hybrid_hybrid does not exist` | Keyspace `cache_orgname_hybrid` is not provisioned in Cassandra.   
`hybrid-runtime org:hybrid Apigee-Timer-9 ERROR c.a.s.e.k.HybridEncryptionKeyServiceImpl - HybridEncryptionKeyServiceImpl.getEncryptionKey() : Encryption key does not exist for organization hybrid and type KmsKey` | Keyspace `kms_orgname_hybrid` is not provisioned in Cassandra.   
  
###  Message processor deployment error logs 

Look for the following deployment error entries in the message processor logs:

Log entry | Description  
---|---  
`hybrid-runtime org:hybrid env:prod Apigee-Main-6 ERROR i.a.h.e.i.HermesEngineImpl - HermesEngineImpl.handleHermesException() : Keyspace cache_hybrid_hybrid does not exist` | Keyspace `cache_orgname_hybrid is not provisioned in Cassandra.`  
`hybrid-runtime org:hybrid Apigee-Timer-9 ERROR c.a.s.e.k.HybridEncryptionKeyServiceImpl - HybridEncryptionKeyS erviceImpl.getEncryptionKey() : Encryption key does not exist for organization hybrid and type KmsKey` |  Keyspace `kms_orgname_hybrid` is not provisioned in Cassandra.   
  
##  Message processor error codes 

Error codes for the message processor start with `runtime.sync.error-name`. For example: 

Log Entry  | Meaning   
---|---  
`runtime.sync.ContractLoadFailedMessage: Error loading spec file` | **Reason** : The error could be caused by an invalid schema, corrupted contract specification file, or invalid contract. Any of these issues could prevent the message processor from loading the spec file.  **Remedy** : Make sure either the contract specification file is available, the file system is not corrupted, or the schema/contract is valid.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
