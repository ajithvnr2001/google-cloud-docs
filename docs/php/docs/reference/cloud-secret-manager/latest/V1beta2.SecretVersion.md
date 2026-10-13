---
url: https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion
title: Secret Manager V1beta2 Client - Class SecretVersion (2.5.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:08.231376+00:00
---

# Secret Manager V1beta2 Client - Class SecretVersion (2.5.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Secret Manager V1beta2 Client - Class SecretVersion (2.5.4) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.4 (latest)  2.4.0  2.3.0  2.2.2  2.1.1  2.0.2  1.15.4  1.13.0  1.12.3  1.11.0  1.10.4  1.9.7 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Secret Manager V1beta2 Client class SecretVersion.

A secret version resource in the Secret Manager API.

Generated from protobuf message `google.cloud.secretmanager.v1beta2.SecretVersion`

## Namespace

Google \ Cloud \ SecretManager \ V1beta2

## Methods 

### __construct

Constructor.

**Parameter**  
---  
**Name** | **Description**  
`data` |  `mixed`   
  
  
### getName

Output only. The resource name of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) in the format `projects/*/secrets/*/versions/*`.

[SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) IDs in a [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) start at 1 and are incremented for each subsequent version of the secret.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. The resource name of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) in the format `projects/*/secrets/*/versions/*`.

[SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) IDs in a [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) start at 1 and are incremented for each subsequent version of the secret.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The time at which the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The time at which the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDestroyTime

Output only. The time this [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) was destroyed. Only present if [state](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion#_Google_Cloud_SecretManager_V1beta2_SecretVersion__getState__) is [DESTROYED](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion.State#_Google_Cloud_SecretManager_V1beta2_SecretVersion_State__DESTROYED).

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasDestroyTime

### clearDestroyTime

### setDestroyTime

Output only. The time this [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) was destroyed. Only present if [state](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion#_Google_Cloud_SecretManager_V1beta2_SecretVersion__getState__) is [DESTROYED](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion.State#_Google_Cloud_SecretManager_V1beta2_SecretVersion_State__DESTROYED).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The current state of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion).

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion.State).  
  
### setState

Output only. The current state of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReplicationStatus

The replication status of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion).

**Returns**  
---  
**Type** | **Description**  
`[ReplicationStatus](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.ReplicationStatus)|null` |   
  
### hasReplicationStatus

### clearReplicationStatus

### setReplicationStatus

The replication status of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ReplicationStatus](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.ReplicationStatus)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEtag

Output only. Etag of the currently stored [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEtag

Output only. Etag of the currently stored [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getClientSpecifiedPayloadChecksum

Output only. True if payload checksum specified in [SecretPayload](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretPayload) object has been received by [SecretManagerService](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Client.SecretManagerServiceClient) on [SecretManagerService.AddSecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Client.SecretManagerServiceClient#_Google_Cloud_SecretManager_V1beta2_Client_SecretManagerServiceClient__addSecretVersion__).

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setClientSpecifiedPayloadChecksum

Output only. True if payload checksum specified in [SecretPayload](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretPayload) object has been received by [SecretManagerService](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Client.SecretManagerServiceClient) on [SecretManagerService.AddSecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Client.SecretManagerServiceClient#_Google_Cloud_SecretManager_V1beta2_Client_SecretManagerServiceClient__addSecretVersion__).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getScheduledDestroyTime

Optional. Output only. Scheduled destroy time for secret version.

This is a part of the Delayed secret version destroy feature. For a Secret with a valid version destroy TTL, when a secert version is destroyed, version is moved to disabled state and it is scheduled for destruction Version is destroyed only after the scheduled_destroy_time.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasScheduledDestroyTime

### clearScheduledDestroyTime

### setScheduledDestroyTime

Optional. Output only. Scheduled destroy time for secret version.

This is a part of the Delayed secret version destroy feature. For a Secret with a valid version destroy TTL, when a secert version is destroyed, version is moved to disabled state and it is scheduled for destruction Version is destroyed only after the scheduled_destroy_time.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCustomerManagedEncryption

Output only. The customer-managed encryption status of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion). Only populated if customer-managed encryption is used and [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) is a Regionalised Secret.

**Returns**  
---  
**Type** | **Description**  
`[CustomerManagedEncryptionStatus](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.CustomerManagedEncryptionStatus)|null` |   
  
### hasCustomerManagedEncryption

### clearCustomerManagedEncryption

### setCustomerManagedEncryption

Output only. The customer-managed encryption status of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion). Only populated if customer-managed encryption is used and [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) is a Regionalised Secret.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[CustomerManagedEncryptionStatus](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.CustomerManagedEncryptionStatus)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
