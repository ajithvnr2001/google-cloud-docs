---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment
title: Class Deployment (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:37.716368+00:00
---

# Class Deployment (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Deployment (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    Deployment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Details of the deployment where APIs are hosted. A deployment could represent an Apigee proxy, API gateway, other Google Cloud services or non-Google Cloud services as well. A deployment entity is a root level entity in the API hub and exists independent of any API.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The name of the deployment. Format: `projects/{project}/locations/{location}/deployments/{deployment}`  
`display_name` |  `str`   
Required. The display name of the deployment.   
`description` |  `str`   
Optional. The description of the deployment.   
`documentation` |  `[google.cloud.apihub_v1.types.Documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Documentation)`   
Optional. The documentation of the deployment.   
`deployment_type` |  `[google.cloud.apihub_v1.types.AttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues)`   
Required. The type of deployment. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-deployment-type` attribute. The number of values for this attribute will be based on the cardinality of the attribute. The same can be retrieved via GetAttribute API. All values should be from the list of allowed values defined for the attribute.   
`resource_uri` |  `str`   
Required. The resource URI identifies the deployment within its gateway. For Apigee gateways, its recommended to use the format: organizations/{org}/environments/{env}/apis/{api}. For ex: if a proxy with name `orders` is deployed in `staging` environment of `cymbal` organization, the resource URI would be: `organizations/cymbal/environments/staging/apis/orders`.   
`endpoints` |  `MutableSequence[str]`   
Required. The endpoints at which this deployment resource is listening for API requests. This could be a list of complete URIs, hostnames or an IP addresses.   
`api_versions` |  `MutableSequence[str]`   
Output only. The API versions linked to this deployment. Note: A particular deployment could be linked to multiple different API versions (of same or different APIs).   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the deployment was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the deployment was last updated.   
`slo` |  `[google.cloud.apihub_v1.types.AttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues)`   
Optional. The SLO for this deployment. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-slo` attribute. The number of values for this attribute will be based on the cardinality of the attribute. The same can be retrieved via GetAttribute API. All values should be from the list of allowed values defined for the attribute.   
`environment` |  `[google.cloud.apihub_v1.types.AttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues)`   
Optional. The environment mapping to this deployment. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-environment` attribute. The number of values for this attribute will be based on the cardinality of the attribute. The same can be retrieved via GetAttribute API. All values should be from the list of allowed values defined for the attribute.   
`attributes` |  `MutableMapping[str, [google.cloud.apihub_v1.types.AttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues)]`   
Optional. The list of user defined attributes associated with the deployment resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.   
`source_metadata` |  `MutableSequence[[google.cloud.apihub_v1.types.SourceMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SourceMetadata)]`   
Output only. The list of sources and metadata from the sources of the deployment.   
`management_url` |  `[google.cloud.apihub_v1.types.AttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues)`   
Optional. The uri where users can navigate to for the management of the deployment. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-management-url` The number of values for this attribute will be based on the cardinality of the attribute. The same can be retrieved via GetAttribute API. The value of the attribute should be a valid URL.   
`source_uri` |  `[google.cloud.apihub_v1.types.AttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues)`   
Optional. The uri where additional source specific information for this deployment can be found. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-source-uri` The number of values for this attribute will be based on the cardinality of the attribute. The same can be retrieved via GetAttribute API. The value of the attribute should be a valid URI, and in case of Cloud Storage URI, it should point to a Cloud Storage object, not a directory.   
`source_project` |  `str`   
Optional. The project to which the deployment belongs. For GCP gateways, this will refer to the project identifier. For others like Edge/OPDK, this will refer to the org identifier.   
`source_environment` |  `str`   
Optional. The environment at source for the deployment. For example: prod, dev, staging, etc.   
  
## Classes 

### AttributesEntry
    
    
    AttributesEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
