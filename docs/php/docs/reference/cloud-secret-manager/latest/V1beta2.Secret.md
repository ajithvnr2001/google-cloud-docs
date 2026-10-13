---
url: https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret
title: Secret Manager V1beta2 Client - Class Secret (2.5.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:57.188823+00:00
---

# Secret Manager V1beta2 Client - Class Secret (2.5.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Secret Manager V1beta2 Client - Class Secret (2.5.4) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.4 (latest)  2.4.0  2.3.0  2.2.2  2.1.1  2.0.2  1.15.4  1.13.0  1.12.3  1.11.0  1.10.4  1.9.7 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Secret Manager V1beta2 Client class Secret.

A [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) is a logical secret whose value and versions can be accessed.

A [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) is made up of zero or more [SecretVersions](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) that represent the secret data.

Generated from protobuf message `google.cloud.secretmanager.v1beta2.Secret`

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

Output only. The resource name of the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) in the format `projects/*/secrets/*`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. The resource name of the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) in the format `projects/*/secrets/*`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReplication

Optional. Immutable. The replication policy of the secret data attached to the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret).

The replication policy cannot be changed after the Secret has been created.

**Returns**  
---  
**Type** | **Description**  
`[Replication](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Replication)|null` |   
  
### hasReplication

### clearReplication

### setReplication

Optional. Immutable. The replication policy of the secret data attached to the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret).

The replication policy cannot be changed after the Secret has been created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Replication](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Replication)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The time at which the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The time at which the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLabels

The labels assigned to this Secret.

Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}` Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No more than 64 labels can be assigned to a given resource.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setLabels

The labels assigned to this Secret.

Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}` Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No more than 64 labels can be assigned to a given resource.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTopics

Optional. A list of up to 10 Pub/Sub topics to which messages are published when control plane operations are called on the secret or its versions.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[Topic](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Topic)>` |   
  
### setTopics

Optional. A list of up to 10 Pub/Sub topics to which messages are published when control plane operations are called on the secret or its versions.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Topic](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Topic)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExpireTime

Optional. Timestamp in UTC when the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) is scheduled to expire. This is always provided on output, regardless of what was sent on input.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasExpireTime

### setExpireTime

Optional. Timestamp in UTC when the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) is scheduled to expire. This is always provided on output, regardless of what was sent on input.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTtl

Input only. The TTL for the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret).

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasTtl

### setTtl

Input only. The TTL for the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEtag

Optional. Etag of the currently stored [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEtag

Optional. Etag of the currently stored [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRotation

Optional. Rotation policy attached to the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret). May be excluded if there is no rotation policy.

**Returns**  
---  
**Type** | **Description**  
`[Rotation](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Rotation)|null` |   
  
### hasRotation

### clearRotation

### setRotation

Optional. Rotation policy attached to the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret). May be excluded if there is no rotation policy.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Rotation](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Rotation)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getVersionAliases

Optional. Mapping from version alias to version name.

A version alias is a string with a maximum length of 63 characters and can contain uppercase and lowercase letters, numerals, and the hyphen (`-`) and underscore ('_') characters. An alias string must start with a letter and cannot be the string 'latest' or 'NEW'. No more than 50 aliases can be assigned to a given secret. Version-Alias pairs will be viewable via GetSecret and modifiable via UpdateSecret. Access by alias is only supported for GetSecretVersion and AccessSecretVersion.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setVersionAliases

Optional. Mapping from version alias to version name.

A version alias is a string with a maximum length of 63 characters and can contain uppercase and lowercase letters, numerals, and the hyphen (`-`) and underscore ('_') characters. An alias string must start with a letter and cannot be the string 'latest' or 'NEW'. No more than 50 aliases can be assigned to a given secret. Version-Alias pairs will be viewable via GetSecret and modifiable via UpdateSecret. Access by alias is only supported for GetSecretVersion and AccessSecretVersion.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAnnotations

Optional. Custom metadata about the secret.

Annotations are distinct from various forms of labels. Annotations exist to allow client tools to store their own state information without requiring a database. Annotation keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, begin and end with an alphanumeric character ([a-z0-9A-Z]), and may have dashes (-), underscores (_), dots (.), and alphanumerics in between these symbols. The total size of annotation keys and values must be less than 16KiB.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setAnnotations

Optional. Custom metadata about the secret.

Annotations are distinct from various forms of labels. Annotations exist to allow client tools to store their own state information without requiring a database. Annotation keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, begin and end with an alphanumeric character ([a-z0-9A-Z]), and may have dashes (-), underscores (_), dots (.), and alphanumerics in between these symbols. The total size of annotation keys and values must be less than 16KiB.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getVersionDestroyTtl

Optional. Secret Version TTL after destruction request This is a part of the Delayed secret version destroy feature.

For secret with TTL>0, version destruction doesn't happen immediately on calling destroy instead the version goes to a disabled state and destruction happens after the TTL expires.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasVersionDestroyTtl

### clearVersionDestroyTtl

### setVersionDestroyTtl

Optional. Secret Version TTL after destruction request This is a part of the Delayed secret version destroy feature.

For secret with TTL>0, version destruction doesn't happen immediately on calling destroy instead the version goes to a disabled state and destruction happens after the TTL expires.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCustomerManagedEncryption

Optional. The customer-managed encryption configuration of the Regionalised Secrets. If no configuration is provided, Google-managed default encryption is used.

Updates to the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) encryption configuration only apply to [SecretVersions](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) added afterwards. They do not apply retroactively to existing [SecretVersions](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion).

**Returns**  
---  
**Type** | **Description**  
`CustomerManagedEncryption|null` |   
  
### hasCustomerManagedEncryption

### clearCustomerManagedEncryption

### setCustomerManagedEncryption

Optional. The customer-managed encryption configuration of the Regionalised Secrets. If no configuration is provided, Google-managed default encryption is used.

Updates to the [Secret](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Secret) encryption configuration only apply to [SecretVersions](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) added afterwards. They do not apply retroactively to existing [SecretVersions](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `CustomerManagedEncryption`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExpiration

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
