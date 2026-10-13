---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Preview
title: Class Preview (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:03.620823+00:00
---

# Class Preview (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Preview

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Preview (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 
    
    
    Preview(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A preview represents a set of actions Infra Manager would perform to move the resources towards the desired state as specified in the configuration.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`terraform_blueprint` |  `[google.cloud.config_v1.types.TerraformBlueprint](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformBlueprint)`   
The terraform blueprint to preview. This field is a member of `oneof`_ `blueprint`.   
`name` |  `str`   
Identifier. Resource name of the preview. Resource name can be user provided or server generated ID if unspecified. Format: `projects/{project}/locations/{location}/previews/{preview}`  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time the preview was created.   
`labels` |  `MutableMapping[str, str]`   
Optional. User-defined labels for the preview.   
`state` |  `[google.cloud.config_v1.types.Preview.State](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Preview.State)`   
Output only. Current state of the preview.   
`deployment` |  `str`   
Optional. Deployment reference. If specified, the preview will be performed using the provided deployment's current state and use any relevant fields from the deployment unless explicitly specified in the preview create request.   
`preview_mode` |  `[google.cloud.config_v1.types.Preview.PreviewMode](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Preview.PreviewMode)`   
Optional. Current mode of preview.   
`service_account` |  `str`   
Required. User-specified Service Account (SA) credentials to be used when previewing resources. Format: `projects/{projectID}/serviceAccounts/{serviceAccount}`  
`artifacts_gcs_bucket` |  `str`   
User-defined location of Cloud Build logs, artifacts, and in Google Cloud Storage. Format: `gs://{bucket}/{folder}` A default bucket will be bootstrapped if the field is not set or empty Default Bucket Format: `gs://` Constraints: \- The bucket needs to be in the same project as the deployment \- The path cannot be within the path of `gcs_source` If omitted and deployment resource ref provided has artifacts_gcs_bucket defined, that artifact bucket is used. This field is a member of `oneof`_ `_artifacts_gcs_bucket`.   
`worker_pool` |  `str`   
The user-specified Worker Pool resource in which the Cloud Build job will execute. Format projects/{project}/locations/{location}/workerPools/{workerPoolId} If this field is unspecified, the default Cloud Build worker pool will be used. If omitted and deployment resource ref provided has worker_pool defined, that worker pool is used. This field is a member of `oneof`_ `_worker_pool`.   
`error_code` |  `[google.cloud.config_v1.types.Preview.ErrorCode](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Preview.ErrorCode)`   
Output only. Code describing any errors that may have occurred.   
`error_status` |  `google.rpc.status_pb2.Status`   
Output only. Additional information regarding the current state.   
`build` |  `str`   
Output only. Cloud Build instance UUID associated with this preview.   
`tf_errors` |  `MutableSequence[[google.cloud.config_v1.types.TerraformError](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformError)]`   
Output only. Summary of errors encountered during Terraform preview. It has a size limit of 10, i.e. only top 10 errors will be summarized here.   
`error_logs` |  `str`   
Output only. Link to tf-error.ndjson file, which contains the full list of the errors encountered during a Terraform preview. Format: `gs://{bucket}/{object}`.   
`preview_artifacts` |  `[google.cloud.config_v1.types.PreviewArtifacts](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.PreviewArtifacts)`   
Output only. Artifacts from preview.   
`logs` |  `str`   
Output only. Location of preview logs in `gs://{bucket}/{object}` format.   
`tf_version` |  `str`   
Output only. The current Terraform version set on the preview. It is in the format of "Major.Minor.Patch", for example, "1.3.10".   
`tf_version_constraint` |  `str`   
The user-specified Terraform version constraint. Example: "=1.3.10". This field is a member of `oneof`_ `_tf_version_constraint`.   
`annotations` |  `MutableMapping[str, str]`   
Optional. Arbitrary key-value metadata storage e.g. to help client tools identify preview during automation. See https://google.aip.dev/148#annotations for details on format and size limitations.   
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

Possible errors that can occur with previews.

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
  
### PreviewMode
    
    
    PreviewMode(value)

Preview mode provides options for customizing preview operations.

### State
    
    
    State(value)

Possible states of a preview.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
