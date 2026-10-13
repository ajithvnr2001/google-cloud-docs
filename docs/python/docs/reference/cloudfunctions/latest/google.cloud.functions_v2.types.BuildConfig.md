---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.BuildConfig
title: Class BuildConfig (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:05.107639+00:00
---

# Class BuildConfig (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.BuildConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BuildConfig (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 
    
    
    BuildConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes the Build step of the function that builds a container from the given source.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`automatic_update_policy` |  `[google.cloud.functions_v2.types.AutomaticUpdatePolicy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.AutomaticUpdatePolicy)`   
This field is a member of `oneof`_ `runtime_update_policy`.   
`on_deploy_update_policy` |  `[google.cloud.functions_v2.types.OnDeployUpdatePolicy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.OnDeployUpdatePolicy)`   
This field is a member of `oneof`_ `runtime_update_policy`.   
`build` |  `str`   
Output only. The Cloud Build name of the latest successful deployment of the function.   
`runtime` |  `str`   
The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function. For a complete list of possible choices, see the ```gcloud`` command reference   
`entry_point` |  `str`   
The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named "function". For Node.js this is name of a function exported by the module specified in `source_location`.   
`source` |  `[google.cloud.functions_v2.types.Source](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Source)`   
The location of the function source code.   
`source_provenance` |  `[google.cloud.functions_v2.types.SourceProvenance](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.SourceProvenance)`   
Output only. A permanent fixed identifier for source.   
`worker_pool` |  `str`   
Name of the Cloud Build Custom Worker Pool that should be used to build the function. The format of this field is `projects/{project}/locations/{region}/workerPools/{workerPool}` where {project} and {region} are the project id and region respectively where the worker pool is defined and {workerPool} is the short name of the worker pool. If the project id is not the same as the function, then the Cloud Functions Service Agent (service-  
`environment_variables` |  `MutableMapping[str, str]`   
User-provided build-time environment variables for the function   
`docker_registry` |  `[google.cloud.functions_v2.types.BuildConfig.DockerRegistry](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.BuildConfig.DockerRegistry)`   
Docker Registry to use for this deployment. This configuration is only applicable to 1st Gen functions, 2nd Gen functions can only use Artifact Registry. Deprecated: As of March 2025, `CONTAINER_REGISTRY` option is no longer available in response to Container Registry's deprecation: https://cloud.google.com/artifact-registry/docs/transition/transition-from-gcr Please use Artifact Registry instead, which is the default choice. If unspecified, it defaults to `ARTIFACT_REGISTRY`. If `docker_repository` field is specified, this field should either be left unspecified or set to `ARTIFACT_REGISTRY`.   
`docker_repository` |  `str`   
Repository in Artifact Registry to which the function docker image will be pushed after it is built by Cloud Build. If specified by user, it is created and managed by user with a customer managed encryption key. Otherwise, GCF will create and use a repository named 'gcf-artifacts' for every deployed region. It must match the pattern `projects/{project}/locations/{location}/repositories/{repository}`. Repository format must be 'DOCKER'.   
`service_account` |  `str`   
Service account to be used for building the container. The format of this field is `projects/{projectId}/serviceAccounts/{serviceAccountEmail}`.   
  
## Classes 

### DockerRegistry
    
    
    DockerRegistry(value)

Docker Registry to use for storing function Docker images.

### EnvironmentVariablesEntry
    
    
    EnvironmentVariablesEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
