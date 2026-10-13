---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment
title: Class Deployment (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:38.211587+00:00
---

# Class Deployment (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Deployment (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 
    
    
    Deployment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A Deployment is a group of resources and configs managed and provisioned by Infra Manager.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`terraform_blueprint` |  `[google.cloud.config_v1.types.TerraformBlueprint](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformBlueprint)`   
A blueprint described using Terraform's HashiCorp Configuration Language as a root module. This field is a member of `oneof`_ `blueprint`.   
`name` |  `str`   
Identifier. Resource name of the deployment. Format: `projects/{project}/locations/{location}/deployments/{deployment}`  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the deployment was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the deployment was last modified.   
`labels` |  `MutableMapping[str, str]`   
Optional. User-defined metadata for the deployment.   
`state` |  `[google.cloud.config_v1.types.Deployment.State](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment.State)`   
Output only. Current state of the deployment.   
`latest_revision` |  `str`   
Output only. Revision name that was most recently applied. Format: `projects/{project}/locations/{location}/deployments/{deployment}/ revisions/{revision}`  
`state_detail` |  `str`   
Output only. Additional information regarding the current state.   
`error_code` |  `[google.cloud.config_v1.types.Deployment.ErrorCode](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment.ErrorCode)`   
Output only. Error code describing errors that may have occurred.   
`delete_results` |  `[google.cloud.config_v1.types.ApplyResults](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ApplyResults)`   
Output only. Location of artifacts from a DeleteDeployment operation.   
`delete_build` |  `str`   
Output only. Cloud Build instance UUID associated with deleting this deployment.   
`delete_logs` |  `str`   
Output only. Location of Cloud Build logs in Google Cloud Storage, populated when deleting this deployment. Format: `gs://{bucket}/{object}`.   
`tf_errors` |  `MutableSequence[[google.cloud.config_v1.types.TerraformError](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformError)]`   
Output only. Errors encountered when deleting this deployment. Errors are truncated to 10 entries, see `delete_results` and `error_logs` for full details.   
`error_logs` |  `str`   
Output only. Location of Terraform error logs in Google Cloud Storage. Format: `gs://{bucket}/{object}`.   
`artifacts_gcs_bucket` |  `str`   
User-defined location of Cloud Build logs and artifacts in Google Cloud Storage. Format: `gs://{bucket}/{folder}` A default bucket will be bootstrapped if the field is not set or empty. Default bucket format: `gs://` Constraints: \- The bucket needs to be in the same project as the deployment \- The path cannot be within the path of `gcs_source` \- The field cannot be updated, including changing its presence This field is a member of `oneof`_ `_artifacts_gcs_bucket`.   
`service_account` |  `str`   
Required. User-specified Service Account (SA) credentials to be used when actuating resources. Format: `projects/{projectID}/serviceAccounts/{serviceAccount}` This field is a member of `oneof`_ `_service_account`.   
`import_existing_resources` |  `bool`   
By default, Infra Manager will return a failure when Terraform encounters a 409 code (resource conflict error) during actuation. If this flag is set to true, Infra Manager will instead attempt to automatically import the resource into the Terraform state (for supported resource types) and continue actuation. Not all resource types are supported, refer to documentation. This field is a member of `oneof`_ `_import_existing_resources`.   
`worker_pool` |  `str`   
The user-specified Cloud Build worker pool resource in which the Cloud Build job will execute. Format: `projects/{project}/locations/{location}/workerPools/{workerPoolId}`. If this field is unspecified, the default Cloud Build worker pool will be used. This field is a member of `oneof`_ `_worker_pool`.   
`lock_state` |  `[google.cloud.config_v1.types.Deployment.LockState](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment.LockState)`   
Output only. Current lock state of the deployment.   
`tf_version_constraint` |  `str`   
The user-specified Terraform version constraint. Example: "=1.3.10". This field is a member of `oneof`_ `_tf_version_constraint`.   
`tf_version` |  `str`   
Output only. The current Terraform version set on the deployment. It is in the format of "Major.Minor.Patch", for example, "1.3.10".   
`quota_validation` |  `[google.cloud.config_v1.types.QuotaValidation](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.QuotaValidation)`   
Optional. Input to control quota checks for resources in terraform configuration files. There are limited resources on which quota validation applies.   
`annotations` |  `MutableMapping[str, str]`   
Optional. Arbitrary key-value metadata storage e.g. to help client tools identify deployments during automation. See https://google.aip.dev/148#annotations for details on format and size limitations.   
`provider_config` |  `[google.cloud.config_v1.types.ProviderConfig](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ProviderConfig)`   
Optional. This field specifies the provider configurations.   
  
## Classes 

### AnnotationsEntry
    
    
    AnnotationsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### ErrorCode
    
    
    ErrorCode(value)

Possible errors that can occur with deployments.

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### LockState
    
    
    LockState(value)

Possible lock states of a deployment.

### State
    
    
    State(value)

Possible states of a deployment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
