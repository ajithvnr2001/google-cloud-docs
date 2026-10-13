---
url: https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.types.HiveMetastoreConfig
title: Class HiveMetastoreConfig (1.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:34.499217+00:00
---

# Class HiveMetastoreConfig (1.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.types.HiveMetastoreConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class HiveMetastoreConfig (1.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.24.0 (latest)  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.3  1.17.0  1.16.1  1.15.5  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.3  1.5.1  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.3.3  0.2.2  0.1.0 
    
    
    HiveMetastoreConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specifies configuration information specific to running Hive metastore software as the metastore service.

## Attributes  
  
---  
**Name** | **Description**  
`version` |  `str`   
Immutable. The Hive metastore schema version.   
`config_overrides` |  `MutableMapping[str, str]`   
A mapping of Hive metastore configuration key-value pairs to apply to the Hive metastore (configured in `hive-site.xml`). The mappings override system defaults (some keys cannot be overridden). These overrides are also applied to auxiliary versions and can be further customized in the auxiliary version's `AuxiliaryVersionConfig`.   
`kerberos_config` |  `[google.cloud.metastore_v1alpha.types.KerberosConfig](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.types.KerberosConfig)`   
Information used to configure the Hive metastore service as a service principal in a Kerberos realm. To disable Kerberos, use the `UpdateService` method and specify this field's path (`hive_metastore_config.kerberos_config`) in the request's `update_mask` while omitting this field from the request's `service`.   
`endpoint_protocol` |  `[google.cloud.metastore_v1alpha.types.HiveMetastoreConfig.EndpointProtocol](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.types.HiveMetastoreConfig.EndpointProtocol)`   
The protocol to use for the metastore service endpoint. If unspecified, defaults to `THRIFT`.   
`auxiliary_versions` |  `MutableMapping[str, [google.cloud.metastore_v1alpha.types.AuxiliaryVersionConfig](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.types.AuxiliaryVersionConfig)]`   
A mapping of Hive metastore version to the auxiliary version configuration. When specified, a secondary Hive metastore service is created along with the primary service. All auxiliary versions must be less than the service's primary version. The key is the auxiliary service name and it must match the regular expression `a-z <[-a-z0-9]*[a-z0-9]>`__?. This means that the first character must be a lowercase letter, and all the following characters must be hyphens, lowercase letters, or digits, except the last character, which cannot be a hyphen.   
  
## Classes 

### AuxiliaryVersionsEntry
    
    
    AuxiliaryVersionsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### ConfigOverridesEntry
    
    
    ConfigOverridesEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### EndpointProtocol
    
    
    EndpointProtocol(value)

Protocols available for serving the metastore service endpoint.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
