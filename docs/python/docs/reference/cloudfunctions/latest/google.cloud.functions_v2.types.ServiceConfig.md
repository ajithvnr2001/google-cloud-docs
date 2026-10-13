---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig
title: Class ServiceConfig (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:10.090236+00:00
---

# Class ServiceConfig (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ServiceConfig (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 
    
    
    ServiceConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes the Service being deployed. Currently Supported : Cloud Run (fully managed).

## Attributes  
  
---  
**Name** | **Description**  
`service` |  `str`   
Output only. Name of the service associated with a Function. The format of this field is `projects/{project}/locations/{region}/services/{service}`  
`timeout_seconds` |  `int`   
The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds.   
`available_memory` |  `str`   
The amount of memory available for a function. Defaults to 256M. Supported units are k, M, G, Mi, Gi. If no unit is supplied the value is interpreted as bytes. See https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go a full description.   
`available_cpu` |  `str`   
The number of CPUs used in a single container instance. Default value is calculated from available memory. Supports the same values as Cloud Run, see https://cloud.google.com/run/docs/reference/rest/v1/Container#resourcerequirements Example: "1" indicates 1 vCPU   
`environment_variables` |  `MutableMapping[str, str]`   
Environment variables that shall be available during function execution.   
`max_instance_count` |  `int`   
The limit on the maximum number of function instances that may coexist at a given time. In some cases, such as rapid traffic surges, Cloud Functions may, for a short period of time, create more instances than the specified max instances limit. If your function cannot tolerate this temporary behavior, you may want to factor in a safety margin and set a lower max instances value than your function can tolerate. See the `Max Instances   
`min_instance_count` |  `int`   
The limit on the minimum number of function instances that may coexist at a given time. Function instances are kept in idle state for a short period after they finished executing the request to reduce cold start time for subsequent requests. Setting a minimum instance count will ensure that the given number of instances are kept running in idle state always. This can help with cold start times when jump in incoming request count occurs after the idle instance would have been stopped in the default case.   
`vpc_connector` |  `str`   
The Serverless VPC Access connector that this cloud function can connect to. The format of this field is `projects/*/locations/*/connectors/*`.   
`vpc_connector_egress_settings` |  `[google.cloud.functions_v2.types.ServiceConfig.VpcConnectorEgressSettings](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig.VpcConnectorEgressSettings)`   
The egress settings for the connector, controlling what traffic is diverted through it.   
`ingress_settings` |  `[google.cloud.functions_v2.types.ServiceConfig.IngressSettings](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig.IngressSettings)`   
The ingress settings for the function, controlling what traffic can reach it.   
`uri` |  `str`   
Output only. URI of the Service deployed.   
`service_account_email` |  `str`   
The email of the service's service account. If empty, defaults to `{project_number}-compute@developer.gserviceaccount.com`.   
`all_traffic_on_latest_revision` |  `bool`   
Whether 100% of traffic is routed to the latest revision. On CreateFunction and UpdateFunction, when set to true, the revision being deployed will serve 100% of traffic, ignoring any traffic split settings, if any. On GetFunction, true will be returned if the latest revision is serving 100% of traffic.   
`secret_environment_variables` |  `MutableSequence[[google.cloud.functions_v2.types.SecretEnvVar](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.SecretEnvVar)]`   
Secret environment variables configuration.   
`secret_volumes` |  `MutableSequence[[google.cloud.functions_v2.types.SecretVolume](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.SecretVolume)]`   
Secret volumes configuration.   
`revision` |  `str`   
Output only. The name of service revision.   
`max_instance_request_concurrency` |  `int`   
Sets the maximum number of concurrent requests that each instance can receive. Defaults to 1.   
`security_level` |  `[google.cloud.functions_v2.types.ServiceConfig.SecurityLevel](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig.SecurityLevel)`   
Security level configure whether the function only accepts https. This configuration is only applicable to 1st Gen functions with Http trigger. By default https is optional for 1st Gen functions; 2nd Gen functions are https ONLY.   
`binary_authorization_policy` |  `str`   
Optional. The binary authorization policy to be checked when deploying the Cloud Run service.   
  
## Classes 

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
  
### IngressSettings
    
    
    IngressSettings(value)

Available ingress settings.

This controls what traffic can reach the function.

If unspecified, ALLOW_ALL will be used.

### SecurityLevel
    
    
    SecurityLevel(value)

Available security level settings.

This enforces security protocol on function URL.

Security level is only configurable for 1st Gen functions, If unspecified, SECURE_OPTIONAL will be used. 2nd Gen functions are SECURE_ALWAYS ONLY.

### VpcConnectorEgressSettings
    
    
    VpcConnectorEgressSettings(value)

Available egress settings.

This controls what traffic is diverted through the VPC Access Connector resource. By default PRIVATE_RANGES_ONLY will be used.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
