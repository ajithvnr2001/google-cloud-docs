---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sync-logs/
title: Synchronizer logs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:59.745174+00:00
---

# Synchronizer logs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sync-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Synchronizer logs Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sync-logs.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sync-logs.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/sync-logs.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/sync-logs.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/sync-logs.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/sync-logs.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/sync-logs.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/sync-logs.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/sync-logs.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/sync-logs.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/sync-logs.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/sync-logs.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/sync-logs.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/sync-logs.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/sync-logs.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/sync-logs.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/sync-logs.html)



Logs are a good way to troubleshoot problems with your Apigee hybrid installation. See [Logging](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/logging) for details.

You can view Apigee synchronizer logs using the `kubectl logs` command. For example: 
    
    
    kubectl logs -n APIGEE_NAMESPACE apigee-synchronizer-apigee-example-test

## Synchronizer log entries

The following table describes the fields that you will see in Synchronizer log files.

Field | Indicates  
---|---  
**`org:`** | Organization name  
**`env:`** | Environment name  
**`target:`** | Path of entity to which the log entry represents  
**`action:`** | Action SYNC=Upstream sync action REPLICATE=Replicate/download action  
**`context-id:`** | The contract version wherever applicable  
  
For example:
    
    
    2019-02-05 00:00:59,098 org:hybrid env:test target: action:SYNC context-id: mode: Apigee-Timer-5 INFO  CONFIG-CHANGE - SyncContext.syncUpStream() : Upstream sync started with https://apigee.googleapis.com

## Understanding Synchronizer logs

If you need to troubleshoot a problem with the Synchronizer, look at the log files. The following table may help you troubleshoot errors may see in the Synchronizer logs. See also [Logging](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/logging).

Log entry | What does it mean  
---|---  
`org:test env:dev target: action:SYNC context-id: mode: Apigee-Timer-0 INFO CONFIG-CHANGE - SyncContext.syncUpStream() : **Upstream sync started with http://localhost:8080**` | Upstream poll was started for the org and environment and given management plane URL  
`2019-01-21 16:58:02,275 org:test env:qa target: action:SYNC context-id: mode: Apigee-Timer-1 INFO CONFIG-CHANGE - ManagementServerBasedReplicationContext.getContract() : **Upstream contract poll returned 200**` | Contract was received successfully  
`2019-01-21 16:58:02,536 org:test env:dev target: action:SYNC context-id: mode: Apigee-Timer-0 INFO CONFIG-CHANGE - ManagementServerBasedReplicationContext.getContract() : **Received a new contract version 20190121.090851.339**` | A contract version was received  
`2019-01-21 17:58:56,530 org:test env:qa target:/organizations/test/environments/qa action:REPLICATE context-id:20190121.090859.699 mode: Apigee-Timer-1 INFO CONFIG-CHANGE - ConfigReplicator.startReplication() : **Replication started**` | Indicates Replication start. MDC fields indicate the details about what is being replicated  
`2019-01-21 17:58:56,654 org:test env:qa target:/organizations/test/environments/qa/resourcefiles/js/JavaScriptCallout.js action:REPLICATE context-id:20190121.090859.699 mode: Apigee-Timer-1 INFO CONFIG-CHANGE - ConfigReplicator.startReplication() : **Replication complete**` | Indicates Replication finished. MDC fields indicate the details about what is being replicated  
`2019-01-21 17:58:56,654 org:test env:qa target:/organizations/test/environments/qa action:REPLICATE context-id:20190121.090859.699 mode: Apigee-Timer-1 **ERROR CONFIG-CHANGE - ConfigReplicator.startReplication() : Replication failed**` | Indicates a replication error  
`2019-01-21 17:59:00,246 org:test env:qa target: action:SYNC context-id: mode: Apigee-Timer-1 INFO CONFIG-CHANGE - SyncContext.syncUpStream() : **Upstream sync finished in 4 seconds**` | Indicates end of a sync cycle and also provides time taken to sync  
`2019-01-21 18:00:00,249 org:test env:dev target: action:SYNC context-id: mode: Apigee-Timer-1 INFO CONFIG-CHANGE - ManagementServerBasedReplicationContext.getContract() : **Upstream contract poll returned 304**` | Indicates that a newer contract was not available  
`2019-01-21 18:21:39,128 org:test env:qa target: action:SYNC context-id: mode: Apigee-Timer-1 ERROR CONFIG-CHANGE - ManagementServerBasedReplicationContext.getContract() : **Upstream contract poll returned error 0**` | Indicates that the management plane was not reachable  
`2019-01-21 18:21:39,128 org:test env:qa target: action:SYNC context-id: mode: Apigee-Timer-1 ERROR CONFIG-CHANGE - ManagementServerBasedReplicationContext.getContract() : **Upstream contract poll returned error 404**` | Indicates that the management plane returned a 404 response for the contract  
`2019-01-21 18:22:39,217 org:test1 env:dev target: action:SYNC context-id: mode: Apigee-Timer-2 ERROR CONFIG-CHANGE - ManagementServerBasedReplicationContext.getContract() : **Upstream contract poll returned error 403**` | Indicates that environment being polled for is not hybrid-enabled  
`2019-01-21 18:22:39,217 org:test1 env:dev target: action:SYNC context-id: mode: Apigee-Timer-2 ERROR CONFIG-CHANGE - ManagementServerBasedReplicationContext.getContract() : **Upstream contract poll returned error 401**` | Supplied credentials has some issues  
  
## Error troubleshooting

Logs are a good way to troubleshoot problems with your installation. See [Logging](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/logging) for details.

### Synchronizer fails to start

Below are a few errors and their remediation explained. Each of these errors message start with an ErrorCode of type sync._< error-code>_. Below are possible error codes

**sync.NullOrEmptyConfig**

**Message:** Null or empty config supplied via com.apigee.sync.config

**Reason:** You will see this error message when the Synchronizer's configuration properties were not supplied properly.

**Remedy:** Make sure all configuration properties are populated with appropriate values.

**sync.ConfigFileNotFound**

**Reason:** The Synchronizer was set to read its configuration properties from a file but the file could not be loaded

**Remedy:** make sure the file is available and accessible during Synchronizer bootup

**sync.IncorrectSettings**

**Reason:** One or more required configuration properties are missing from the Synchronizer configuration or they values that are outside the expected range. The error should have more details about the exact property that is causing the problem. These errors are in-built into the parser to make sure that and setting errors are caught even before the service starts.

The following table lists some possible IncorrectSettings errors:

Error | What's wrong  
---|---  
**`configuration.json.IncorrectSettings: [com.apigee.sync.config.json] Error:/controlPlane/retries numeric instance is greater than the required maximum (maximum: 3, found: 20)`** | Value supplied to retries field in controlPlane section has exceeded the allowed  
**`configuration.json.IncorrectSettings: [com.apigee.sync.config.json] Error:/controlPlane/connectionTimeout numeric instance is lower than the required minimum (minimum: 10, found: 1)`** | Value supplied to connectionTimeout field in controlPlane section is lower than allowed  
**`configuration.json.IncorrectSettings: [com.apigee.sync.config.json] Error:/controlPlane object has missing required properties ([\"contractProvider\"])`** | controlPlane section is missing the mandatory field contractProvider  
**`configuration.json.IncorrectSettings: [com.apigee.sync.config.json] Error:/controlPlane/contractProvider string \"http://\\uapi.apigee.com\" is not a valid URI`** | Contract provider URI is not a valid URI  
**`configuration.json.IncorrectSettings: [com.apigee.sync.config.json] Error:/environments array is too short: must have at least 1 elements but instance has 0 elements`** | The environments array must have at least one environment  
**`configuration.json.IncorrectSettings: [com.apigee.sync.config.json] Error:/environments/0 object has missing required properties ([\"environmentName\"])`** | Environment at index 0 is missing the mandatory field environmentName  
**`configuration.json.IncorrectSettings: [com.apigee.sync.config.json] Error:/environments/0 object has missing required properties ([\"organizationName\"])`** | Environment at index 0 is missing the mandatory field organizationName  
**`configuration.json.IncorrectSettings: [com.apigee.sync.config.json] Error:/environments/0/pollInterval numeric instance is lower than the required minimum (minimum: 60, found: 6)`** | Environment at index 0 has a poll interval which is under the allowed limit of 60  
  
**Remedy:** Fix the setting to include the required block

**sync.ReplicationRootDoesNotExist**

**Reason:** The Synchronizer was supplied with a replication root which does not exist

**Remedy:** make sure the supplied root folder exists and is writeable

**sync.ReadOnlyReplicationRoot**

**Reason:** The Synchronizer was supplied with a replication root which do not have write permissions

**Remedy:** make sure the supplied root folder exists and is writeable

**sync.ReplicationRootNotADir**

**Reason:** The Synchronizer was supplied with a replication root which is possibly a file

**Remedy:** make sure the supplied root folder exists and is writeable

**sync.InvalidControlPlaneURL**

**Reason:** The Synchronizer was supplied with a config URL which is empty

**Remedy:** Make sure the supplied root folder exists and is writeable

**sync.InvalidControlPlaneSubscriptionURL**

**Reason:** The Synchronizer was supplied with an incorrect, incomplete, or empty config URL for subscription creation.

**Remedy:** Correct the URL to a valid config URL for pub/sub subscription creation to handle signals from control plane.

**sync.InvalidControlPlaneUnsubscriptionURL**

**Reason:** The Synchronizer was supplied with an incorrect, incomplete, or empty config URL for subscription deletion.

**Remedy:** Correct the URL to a valid config URL for pub/sub subscription deletion to handle signals from control plane.

**sync.CannotCreateEnvironmentFolder**

**Reason:** The Synchronizer tried to create a folder for replicating environment qa but could not create the required folder

**Remedy:** make sure the replication root does not have a conflicting path with the same name which is either read-only of a file

**sync.DuplicateEnvironmentEntries**

**Reason:** The same environment was added multiple times in the configuration.

**Remedy:** Every environment can be specified only once.

**sync.DiskExceedsAllowedCapacity**

**Reason:** The supplied storage disk is already at threshold capacity supplied via the configuration properties.

**Remedy:** Make sure there is enough disk space or check if the storage settings can be tweaked to allow more disk space.

**sync.OwnershipClaimFailed**

**Reason:** Synchronizer tried to claim ownership on the environment folder but failed

**Remedy:** every Synchronizer will first try to make sure it is a sole writer to the file system. The error indicates the path and the reason for the failure. Address the root cause

## Synchronizer errors during runtime

The following Synchronizer errors can occur during runtime.

**sync.replicators.PollReturnedError**

Associated message will include the upstream status. Below are the error statuses

**status 0**

**Reason:** Indicates a connectivity issue. The management plane was not reachable

**Remedy:** Make sure the management plane details are correct and the contracts API is reachable

**status 404**

**Reason:** Most likely the org/env name is not found on the server

**Remedy:** Make sure the management plane details are correct and the contracts API is reachable

**status 401**

**Reason:** Most likely credentials supplied do not have the org admin privileges.

**Remedy:** Make sure the management plane credentials are correct and the contracts API is reachable

**status 403**

**Reason:** Indicates the environment being polled for is not set up as hybrid environment

**Remedy:** Make sure the org has the required flag **"features.hybrid.enabled=true"**

**sync.OwnershipClaimedByOther**

**Reason:** During the operation Synchronizer found that the file root is being accessed by another instance of Synchronizer. (This can happen when a file system is shared among Synchronizers.)

**Remedy:** Address the root problem to make sure no two Synchronizer instances share the same file system. The Synchronizer would have marked itself down and would be in an unrecoverable position here. It would also make sure the other Synchronizer which is accessing the same file root gets notified about it via their ownership files

**sync.DiskExceedsAllowedCapacity**

**Reason:** During the operation Synchronizer realized that the disk occupancy has exceeded the allowed limit.

**Remedy:** At this point Synchronizer would abort any downloads and try a stale file cleanup operation. However this may become a recurring condition and the only way to recover completely is to make sure the Synchronizer has enough disk memory to operate.

### Diagnose contract download failures

If you see "upstream contract poll" in an error message, try calling the contract API and check the details, where username is your Apigee username (your email address). The contract represents the entire collection of data that the Synchronizer downloads from the management plane.

### No data residency
    
    
    curl https://apigee.googleapis.com/v1/organizations/org/environments/env/contracts/1.0 -u username

### Data residency
    
    
    curl https://$CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/org/environments/env/contracts/1.0 -u username

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
