---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResourceStatusEffectiveInstanceMetadata
title: Class ResourceStatusEffectiveInstanceMetadata (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:17.231401+00:00
---

# Class ResourceStatusEffectiveInstanceMetadata (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResourceStatusEffectiveInstanceMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ResourceStatusEffectiveInstanceMetadata (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    ResourceStatusEffectiveInstanceMetadata(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Effective values of predefined metadata keys for an instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`block_project_ssh_keys_metadata_value` |  `bool`   
Effective block-project-ssh-keys value at Instance level. This field is a member of `oneof`_ `_block_project_ssh_keys_metadata_value`.   
`enable_guest_attributes_metadata_value` |  `bool`   
Effective enable-guest-attributes value at Instance level. This field is a member of `oneof`_ `_enable_guest_attributes_metadata_value`.   
`enable_os_inventory_metadata_value` |  `bool`   
Effective enable-os-inventory value at Instance level. This field is a member of `oneof`_ `_enable_os_inventory_metadata_value`.   
`enable_osconfig_metadata_value` |  `bool`   
Effective enable-osconfig value at Instance level. This field is a member of `oneof`_ `_enable_osconfig_metadata_value`.   
`enable_oslogin_metadata_value` |  `bool`   
Effective enable-oslogin value at Instance level. This field is a member of `oneof`_ `_enable_oslogin_metadata_value`.   
`gce_container_declaration_metadata_value` |  `bool`   
Effective gce-container-declaration value at Instance level. This field is a member of `oneof`_ `_gce_container_declaration_metadata_value`.   
`serial_port_enable_metadata_value` |  `bool`   
Effective serial-port-enable value at Instance level. This field is a member of `oneof`_ `_serial_port_enable_metadata_value`.   
`serial_port_logging_enable_metadata_value` |  `bool`   
Effective serial-port-logging-enable value at Instance level. This field is a member of `oneof`_ `_serial_port_logging_enable_metadata_value`.   
`vm_dns_setting_metadata_value` |  `str`   
Effective VM DNS setting at Instance level. This field is a member of `oneof`_ `_vm_dns_setting_metadata_value`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
