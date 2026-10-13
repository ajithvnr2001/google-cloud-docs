---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory
title: Class ActiveDirectory (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:10.001715+00:00
---

# Class ActiveDirectory (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ActiveDirectory (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 
    
    
    ActiveDirectory(mapping=None, *, ignore_unknown_fields=False, **kwargs)

ActiveDirectory is the public representation of the active directory config.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the active directory. Format: `projects/{project_number}/locations/{location_id}/activeDirectories/{active_directory_id}`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Create time of the active directory.   
`state` |  `[google.cloud.netapp_v1.types.ActiveDirectory.State](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory.State)`   
Output only. The state of the AD.   
`domain` |  `str`   
Required. Name of the Active Directory domain   
`site` |  `str`   
The Active Directory site the service will limit Domain Controller discovery too.   
`dns` |  `str`   
Required. Comma separated list of DNS server IP addresses for the Active Directory domain.   
`net_bios_prefix` |  `str`   
Required. NetBIOSPrefix is used as a prefix for SMB server name.   
`organizational_unit` |  `str`   
The Organizational Unit (OU) within the Windows Active Directory the user belongs to.   
`aes_encryption` |  `bool`   
If enabled, AES encryption will be enabled for SMB communication.   
`username` |  `str`   
Required. Username of the Active Directory domain administrator.   
`password` |  `str`   
Required. Password of the Active Directory domain administrator.   
`backup_operators` |  `MutableSequence[str]`   
Optional. Users to be added to the Built-in Backup Operator active directory group.   
`administrators` |  `MutableSequence[str]`   
Optional. Users to be added to the Built-in Admininstrators group.   
`security_operators` |  `MutableSequence[str]`   
Optional. Domain users to be given the SeSecurityPrivilege.   
`kdc_hostname` |  `str`   
Name of the active directory machine. This optional parameter is used only while creating kerberos volume   
`kdc_ip` |  `str`   
KDC server IP address for the active directory machine.   
`nfs_users_with_ldap` |  `bool`   
If enabled, will allow access to local users and LDAP users. If access is needed for only LDAP users, it has to be disabled.   
`description` |  `str`   
Description of the active directory.   
`ldap_signing` |  `bool`   
Specifies whether or not the LDAP traffic needs to be signed.   
`encrypt_dc_connections` |  `bool`   
If enabled, traffic between the SMB server to Domain Controller (DC) will be encrypted.   
`labels` |  `MutableMapping[str, str]`   
Labels for the active directory.   
`state_details` |  `str`   
Output only. The state details of the Active Directory.   
  
## Classes 

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
  
### State
    
    
    State(value)

The Active Directory States

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
