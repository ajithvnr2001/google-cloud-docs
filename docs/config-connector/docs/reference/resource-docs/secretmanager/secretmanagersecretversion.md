---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/secretmanager/secretmanagersecretversion/
title: SecretManagerSecretVersion \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:01.980321+00:00
---

# SecretManagerSecretVersion  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/secretmanager/secretmanagersecretversion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SecretManagerSecretVersion

**Property** | **Value**  
---|---  
Google Cloud Service Name | Secret Manager  
Google Cloud Service Documentation | [/secret-manager/docs/](https://docs.cloud.google.com/secret-manager/docs)  
Google Cloud REST Resource Name | v1.projects.secrets.versions  
Google Cloud REST Resource Documentation | [/secret-manager/docs/reference/rest/v1/projects.secrets.versions](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions)  
Config Connector Resource Short Names | gcpsecretmanagersecretversion  
gcpsecretmanagersecretversions  
secretmanagersecretversion  
Config Connector Service Name | secretmanager.googleapis.com  
Config Connector Resource Fully Qualified Name | secretmanagersecretversions.secretmanager.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    deletionPolicy: string
    enabled: boolean
    isSecretDataBase64: boolean
    resourceID: string
    secretData:
      value: string
      valueFrom:
        secretKeyRef:
          key: string
          name: string
    secretRef:
      external: string
      name: string
      namespace: string
    

Fields  
---  
`deletionPolicy` _Optional_ |  `string` DEPRECATED. You do not need to set this field in direct reconciler mode. Use delete-policy annotation instead. https://cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#keeping_resources_after_deletion The deletion policy for the secret version. Setting 'ABANDON' allows the resource to be abandoned rather than deleted. Setting 'DISABLE' allows the resource to be disabled rather than deleted. Default is 'DELETE'. Possible values are: * DELETE * DISABLE * ABANDON.  
`enabled` _Optional_ |  `boolean` Should enable or disable the current SecretVersion. - Enabled version can be accessed and described. - Disabled version cannot be accessed, but the secret's contents still exist  
`isSecretDataBase64` _Optional_ |  `boolean` DEPRECATED. You do not need to set this field in direct reconciler mode.  
`resourceID` _Optional_ |  `string` The service-generated SecretVersion number. If given, Config Connector acquires the resource from the Secret Manager service. If not given, Config Connector adds a new secret version to the Google Cloud service, and you can find out the version number from `status.observedState.version`  
`secretData` _Optional_ |  `object` The actual secret data. Config Connector supports secret data stored in Kubernetes secret or plain data (base64)  
`secretData.value` _Optional_ |  `string` Value of the field. Cannot be used if 'valueFrom' is specified.  
`secretData.valueFrom` _Optional_ |  `object` Source for the field's value. Cannot be used if 'value' is specified.  
`secretData.valueFrom.secretKeyRef` _Optional_ |  `object` Reference to a value with the given key in the given Secret in the resource's namespace.  
`secretData.valueFrom.secretKeyRef.key` _Required*_ |  `string` Key that identifies the value to be extracted.  
`secretData.valueFrom.secretKeyRef.name` _Required*_ |  `string` Name of the Secret to extract a value from.  
`secretRef` _Optional_ |  `object` The resource name of the [Secret][google.cloud.secretmanager.v1.Secret] to create a [SecretVersion][google.cloud.secretmanager.v1.SecretVersion] for.  
`secretRef.external` _Optional_ |  `string` A reference to an externally managed SecretManagerSecret resource. Should be in the format "projects/{{projectID}}/locations/{{location}}/secrets/{{secretID}}".  
`secretRef.name` _Optional_ |  `string` The name of a SecretManagerSecret resource.  
`secretRef.namespace` _Optional_ |  `string` The namespace of a SecretManagerSecret resource.  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    createTime: string
    destroyTime: string
    externalRef: string
    name: string
    observedGeneration: integer
    observedState:
      clientSpecifiedPayloadChecksum: boolean
      createTime: string
      customerManagedEncryption:
        kmsKeyVersionName: string
      destroyTime: string
      name: string
      replicationStatus:
        automatic:
          customerManagedEncryption:
            kmsKeyVersionName: string
        userManaged:
          replicas:
          - customerManagedEncryption:
              kmsKeyVersionName: string
            location: string
      scheduledDestroyTime: string
    version: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the object's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`createTime` |  `string` DEPRECATING NOTE: Please use status.observedState.createTime instead.  
`destroyTime` |  `string` DEPRECATING NOTE: Please use status.observedState.destroyTime instead.  
`externalRef` |  `string` A unique specifier for the SecretManagerSecretVersion resource in Google Cloud.  
`name` |  `string` DEPRECATING NOTE: Please use status.observedState.name instead.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`observedState` |  `object` ObservedState is the state of the resource as most recently observed in Google Cloud.  
`observedState.clientSpecifiedPayloadChecksum` |  `boolean` Output only. True if payload checksum specified in [SecretPayload][google.cloud.secretmanager.v1.SecretPayload] object has been received by [SecretManagerService][google.cloud.secretmanager.v1.SecretManagerService] on [SecretManagerService.AddSecretVersion][google.cloud.secretmanager.v1.SecretManagerService.AddSecretVersion].  
`observedState.createTime` |  `string` Output only. The time at which the [SecretVersion][google.cloud.secretmanager.v1.SecretVersion] was created.  
`observedState.customerManagedEncryption` |  `object` Output only. The customer-managed encryption status of the [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]. Only populated if customer-managed encryption is used and [Secret][google.cloud.secretmanager.v1.Secret] is a Regionalised Secret.  
`observedState.customerManagedEncryption.kmsKeyVersionName` |  `string` Required. The resource name of the Cloud KMS CryptoKeyVersion used to encrypt the secret payload, in the following format: `projects/*/locations/*/keyRings/*/cryptoKeys/*/versions/*`.  
`observedState.destroyTime` |  `string` Output only. The time this [SecretVersion][google.cloud.secretmanager.v1.SecretVersion] was destroyed. Only present if [state][google.cloud.secretmanager.v1.SecretVersion.state] is [DESTROYED][google.cloud.secretmanager.v1.SecretVersion.State.DESTROYED].  
`observedState.name` |  `string` Output only. The resource name of the [SecretVersion][google.cloud.secretmanager.v1.SecretVersion] in the format `projects/*/secrets/*/versions/*`. [SecretVersion][google.cloud.secretmanager.v1.SecretVersion] IDs in a [Secret][google.cloud.secretmanager.v1.Secret] start at 1 and are incremented for each subsequent version of the secret.  
`observedState.replicationStatus` |  `object` The replication status of the [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].  
`observedState.replicationStatus.automatic` |  `object` Describes the replication status of a [SecretVersion][google.cloud.secretmanager.v1.SecretVersion] with automatic replication. Only populated if the parent [Secret][google.cloud.secretmanager.v1.Secret] has an automatic replication policy.  
`observedState.replicationStatus.automatic.customerManagedEncryption` |  `object` Output only. The customer-managed encryption status of the [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]. Only populated if customer-managed encryption is used.  
`observedState.replicationStatus.automatic.customerManagedEncryption.kmsKeyVersionName` |  `string` Required. The resource name of the Cloud KMS CryptoKeyVersion used to encrypt the secret payload, in the following format: `projects/*/locations/*/keyRings/*/cryptoKeys/*/versions/*`.  
`observedState.replicationStatus.userManaged` |  `object` Describes the replication status of a [SecretVersion][google.cloud.secretmanager.v1.SecretVersion] with user-managed replication. Only populated if the parent [Secret][google.cloud.secretmanager.v1.Secret] has a user-managed replication policy.  
`observedState.replicationStatus.userManaged.replicas` |  `list (object)` Output only. The list of replica statuses for the [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].  
`observedState.replicationStatus.userManaged.replicas[]` |  `object`  
`observedState.replicationStatus.userManaged.replicas[].customerManagedEncryption` |  `object` Output only. The customer-managed encryption status of the [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]. Only populated if customer-managed encryption is used.  
`observedState.replicationStatus.userManaged.replicas[].customerManagedEncryption.kmsKeyVersionName` |  `string` Required. The resource name of the Cloud KMS CryptoKeyVersion used to encrypt the secret payload, in the following format: `projects/*/locations/*/keyRings/*/cryptoKeys/*/versions/*`.  
`observedState.replicationStatus.userManaged.replicas[].location` |  `string` Output only. The canonical ID of the replica location. For example: `"us-east1"`.  
`observedState.scheduledDestroyTime` |  `string` Optional. Output only. Scheduled destroy time for secret version. This is a part of the Delayed secret version destroy feature. For a Secret with a valid version destroy TTL, when a secert version is destroyed, the version is moved to disabled state and it is scheduled for destruction. The version is destroyed only after the `scheduled_destroy_time`.  
`version` |  `string` DEPRECATED.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: secretmanager.cnrm.cloud.google.com/v1beta1
    kind: SecretManagerSecretVersion
    metadata:
      name: secretmanagersecretversion-sample
    spec:
      enabled: true
      secretData:
        valueFrom:
          secretKeyRef:
            key: secretData
            name: secretmanagersecretversion-dep
      secretRef:
        name: secretmanagersecretversion-dep
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: secretmanagersecretversion-dep
    data:
      secretData: SSBhbHdheXMgbG92ZWQgc3BhcnJpbmcgd2l0aCBnaWFudCBjYW5keSBzd29yZHMsIGJ1dCBJIGhhZCBubyBpZGVhIHRoYXQgd2FzIG15IHN1cGVyIHNlY3JldCBpbmZvcm1hdGlvbiE=
    ---
    apiVersion: secretmanager.cnrm.cloud.google.com/v1beta1
    kind: SecretManagerSecret
    metadata:
      name: secretmanagersecretversion-dep
    spec:
      replication:
        automatic: true
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
