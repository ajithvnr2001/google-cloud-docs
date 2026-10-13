---
url: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Finding
title: Class Finding (1.47.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:01.913142+00:00
---

# Class Finding (1.47.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Finding

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Finding (1.47.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.47.0 (latest)  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.1  1.33.1  1.32.1  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.1  1.25.0  1.24.1  1.23.2  1.22.0  1.21.0  1.20.0  1.19.1  1.18.2  1.17.0  1.16.2  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.7.3  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    Finding(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Security Command Center finding.

A finding is a record of assessment data like security, risk, health, or privacy, that is ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, a cross-site scripting (XSS) vulnerability in an App Engine application is a finding.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The `relative resource name   
`canonical_name` |  `str`   
Output only. The canonical name of the finding. The following list shows some examples: \- `organizations/{organization_id}/sources/{source_id}/findings/{finding_id}` \+ `organizations/{organization_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}` \- `folders/{folder_id}/sources/{source_id}/findings/{finding_id}` \- `folders/{folder_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}` \- `projects/{project_id}/sources/{source_id}/findings/{finding_id}` \- `projects/{project_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}` The prefix is the closest CRM ancestor of the resource associated with the finding.   
`parent` |  `str`   
The relative resource name of the source and location the finding belongs to. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name This field is immutable after creation time. The following list shows some examples: \- `organizations/{organization_id}/sources/{source_id}` \- `folders/{folders_id}/sources/{source_id}` \- `projects/{projects_id}/sources/{source_id}` \- `organizations/{organization_id}/sources/{source_id}/locations/{location_id}` \- `folders/{folders_id}/sources/{source_id}/locations/{location_id}` \- `projects/{projects_id}/sources/{source_id}/locations/{location_id}`  
`resource_name` |  `str`   
Immutable. For findings on Google Cloud resources, the full resource name of the Google Cloud resource this finding is for. See: https://cloud.google.com/apis/design/resource_names#full_resource_name When the finding is for a non-Google Cloud resource, the resourceName can be a customer or partner defined string.   
`state` |  `[google.cloud.securitycenter_v2.types.Finding.State](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Finding.State)`   
Output only. The state of the finding.   
`category` |  `str`   
Immutable. The additional taxonomy group within findings from a given source. Example: "XSS_FLASH_INJECTION".   
`external_uri` |  `str`   
The URI that, if available, points to a web page outside of Security Command Center where additional information about the finding can be found. This field is guaranteed to be either empty or a well formed URL.   
`source_properties` |  `MutableMapping[str, google.protobuf.struct_pb2.Value]`   
Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.   
`security_marks` |  `[google.cloud.securitycenter_v2.types.SecurityMarks](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.SecurityMarks)`   
Output only. User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the finding.   
`event_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time the finding was first detected. If an existing finding is updated, then this is the time the update occurred. For example, if the finding represents an open firewall, this property captures the time the detector believes the firewall became open. The accuracy is determined by the detector. If the finding is later resolved, then this time reflects when the finding was resolved. This must not be set to a value greater than the current timestamp.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the finding was created in Security Command Center.   
`severity` |  `[google.cloud.securitycenter_v2.types.Finding.Severity](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Finding.Severity)`   
The severity of the finding. This field is managed by the source that writes the finding.   
`mute` |  `[google.cloud.securitycenter_v2.types.Finding.Mute](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Finding.Mute)`   
Indicates the mute state of a finding (either muted, unmuted or undefined). Unlike other attributes of a finding, a finding provider shouldn't set the value of mute.   
`mute_info` |  `[google.cloud.securitycenter_v2.types.Finding.MuteInfo](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Finding.MuteInfo)`   
Output only. The mute information regarding this finding.   
`finding_class` |  `[google.cloud.securitycenter_v2.types.Finding.FindingClass](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Finding.FindingClass)`   
The class of the finding.   
`indicator` |  `[google.cloud.securitycenter_v2.types.Indicator](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Indicator)`   
Represents what's commonly known as an *indicator of compromise* (IoC) in computer forensics. This is an artifact observed on a network or in an operating system that, with high confidence, indicates a computer intrusion. For more information, see `Indicator of compromise   
`vulnerability` |  `[google.cloud.securitycenter_v2.types.Vulnerability](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Vulnerability)`   
Represents vulnerability-specific fields like CVE and CVSS scores. CVE stands for Common Vulnerabilities and Exposures (https://cve.mitre.org/about/)   
`mute_update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The most recent time this finding was muted or unmuted.   
`external_systems` |  `MutableMapping[str, [google.cloud.securitycenter_v2.types.ExternalSystem](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ExternalSystem)]`   
Output only. Third party SIEM/SOAR fields within SCC, contains external system information and external system finding fields.   
`mitre_attack` |  `[google.cloud.securitycenter_v2.types.MitreAttack](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.MitreAttack)`   
MITRE ATT&CK tactics and techniques related to this finding. See: https://attack.mitre.org   
`access` |  `[google.cloud.securitycenter_v2.types.Access](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Access)`   
Access details associated with the finding, such as more information on the caller, which method was accessed, and from where.   
`connections` |  `MutableSequence[[google.cloud.securitycenter_v2.types.Connection](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Connection)]`   
Contains information about the IP connection associated with the finding.   
`mute_initiator` |  `str`   
Records additional information about the mute operation, for example, the `mute configuration   
`processes` |  `MutableSequence[[google.cloud.securitycenter_v2.types.Process](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Process)]`   
Represents operating system processes associated with the Finding.   
`contacts` |  `MutableMapping[str, [google.cloud.securitycenter_v2.types.ContactDetails](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ContactDetails)]`   
Output only. Map containing the points of contact for the given finding. The key represents the type of contact, while the value contains a list of all the contacts that pertain. Please refer to: https://cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories :: { "security": { "contacts": [ { "email": "person1@company.com" }, { "email": "person2@company.com" } ] } }   
`compliances` |  `MutableSequence[[google.cloud.securitycenter_v2.types.Compliance](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Compliance)]`   
Contains compliance information for security standards associated to the finding.   
`parent_display_name` |  `str`   
Output only. The human readable display name of the finding source such as "Event Threat Detection" or "Security Health Analytics".   
`description` |  `str`   
Contains more details about the finding.   
`exfiltration` |  `[google.cloud.securitycenter_v2.types.Exfiltration](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Exfiltration)`   
Represents exfiltrations associated with the finding.   
`iam_bindings` |  `MutableSequence[[google.cloud.securitycenter_v2.types.IamBinding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.IamBinding)]`   
Represents IAM bindings associated with the finding.   
`next_steps` |  `str`   
Steps to address the finding.   
`module_name` |  `str`   
Unique identifier of the module which generated the finding. Example: folders/598186756061/securityHealthAnalyticsSettings/customModules/56799441161885   
`containers` |  `MutableSequence[[google.cloud.securitycenter_v2.types.Container](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Container)]`   
Containers associated with the finding. This field provides information for both Kubernetes and non-Kubernetes containers.   
`kubernetes` |  `[google.cloud.securitycenter_v2.types.Kubernetes](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Kubernetes)`   
Kubernetes resources associated with the finding.   
`database` |  `[google.cloud.securitycenter_v2.types.Database](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Database)`   
Database associated with the finding.   
`attack_exposure` |  `[google.cloud.securitycenter_v2.types.AttackExposure](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.AttackExposure)`   
The results of an attack path simulation relevant to this finding.   
`files` |  `MutableSequence[[google.cloud.securitycenter_v2.types.File](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.File)]`   
File associated with the finding.   
`cloud_dlp_inspection` |  `[google.cloud.securitycenter_v2.types.CloudDlpInspection](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.CloudDlpInspection)`   
Cloud Data Loss Prevention (Cloud DLP) inspection results that are associated with the finding.   
`cloud_dlp_data_profile` |  `[google.cloud.securitycenter_v2.types.CloudDlpDataProfile](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.CloudDlpDataProfile)`   
Cloud DLP data profile that is associated with the finding.   
`kernel_rootkit` |  `[google.cloud.securitycenter_v2.types.KernelRootkit](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.KernelRootkit)`   
Signature of the kernel rootkit.   
`org_policies` |  `MutableSequence[[google.cloud.securitycenter_v2.types.OrgPolicy](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.OrgPolicy)]`   
Contains information about the org policies associated with the finding.   
`job` |  `[google.cloud.securitycenter_v2.types.Job](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Job)`   
Job associated with the finding.   
`application` |  `[google.cloud.securitycenter_v2.types.Application](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Application)`   
Represents an application associated with the finding.   
`ip_rules` |  `[google.cloud.securitycenter_v2.types.IpRules](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.IpRules)`   
IP rules associated with the finding.   
`backup_disaster_recovery` |  `[google.cloud.securitycenter_v2.types.BackupDisasterRecovery](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.BackupDisasterRecovery)`   
Fields related to Backup and DR findings.   
`security_posture` |  `[google.cloud.securitycenter_v2.types.SecurityPosture](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.SecurityPosture)`   
The security posture associated with the finding.   
`log_entries` |  `MutableSequence[[google.cloud.securitycenter_v2.types.LogEntry](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.LogEntry)]`   
Log entries that are relevant to the finding.   
`load_balancers` |  `MutableSequence[[google.cloud.securitycenter_v2.types.LoadBalancer](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.LoadBalancer)]`   
The load balancers associated with the finding.   
`cloud_armor` |  `[google.cloud.securitycenter_v2.types.CloudArmor](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.CloudArmor)`   
Fields related to Cloud Armor findings.   
`notebook` |  `[google.cloud.securitycenter_v2.types.Notebook](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Notebook)`   
Notebook associated with the finding.   
`toxic_combination` |  `[google.cloud.securitycenter_v2.types.ToxicCombination](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ToxicCombination)`   
Contains details about a group of security issues that, when the issues occur together, represent a greater risk than when the issues occur independently. A group of such issues is referred to as a toxic combination. This field cannot be updated. Its value is ignored in all update requests.   
`group_memberships` |  `MutableSequence[[google.cloud.securitycenter_v2.types.GroupMembership](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.GroupMembership)]`   
Contains details about groups of which this finding is a member. A group is a collection of findings that are related in some way. This field cannot be updated. Its value is ignored in all update requests.   
`disk` |  `[google.cloud.securitycenter_v2.types.Disk](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Disk)`   
Disk associated with the finding.   
`data_access_events` |  `MutableSequence[[google.cloud.securitycenter_v2.types.DataAccessEvent](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.DataAccessEvent)]`   
Data access events associated with the finding.   
`data_flow_events` |  `MutableSequence[[google.cloud.securitycenter_v2.types.DataFlowEvent](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.DataFlowEvent)]`   
Data flow events associated with the finding.   
`networks` |  `MutableSequence[[google.cloud.securitycenter_v2.types.Network](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Network)]`   
Represents the VPC networks that the resource is attached to.   
`data_retention_deletion_events` |  `MutableSequence[[google.cloud.securitycenter_v2.types.DataRetentionDeletionEvent](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.DataRetentionDeletionEvent)]`   
Data retention deletion events associated with the finding.   
`affected_resources` |  `[google.cloud.securitycenter_v2.types.AffectedResources](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.AffectedResources)`   
AffectedResources associated with the finding.   
`ai_model` |  `[google.cloud.securitycenter_v2.types.AiModel](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.AiModel)`   
The AI model associated with the finding.   
`chokepoint` |  `[google.cloud.securitycenter_v2.types.Chokepoint](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Chokepoint)`   
Contains details about a chokepoint, which is a resource or resource group where high-risk attack paths converge, based on [attack path simulations] (https://cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_path_simulations). This field cannot be updated. Its value is ignored in all update requests.   
`vertex_ai` |  `[google.cloud.securitycenter_v2.types.VertexAi](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.VertexAi)`   
VertexAi associated with the finding.   
`agent` |  `[google.cloud.securitycenter_v2.types.Agent](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.Agent)`   
Primary Agent that the specified finding was flagged for   
`agent_sessions` |  `MutableSequence[[google.cloud.securitycenter_v2.types.AgentSession](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.AgentSession)]`   
Conversational session(s) where the finding occurred.   
`agent_anomaly` |  `[google.cloud.securitycenter_v2.types.AgentAnomaly](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.AgentAnomaly)`   
Details about behavior anomalies detected in AI agents.   
  
## Classes 

### ContactsEntry
    
    
    ContactsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### ExternalSystemsEntry
    
    
    ExternalSystemsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### FindingClass
    
    
    FindingClass(value)

Represents what kind of Finding it is.

### Mute
    
    
    Mute(value)

Mute state a finding can be in.

### MuteInfo
    
    
    MuteInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Mute information about the finding, including whether the finding has a static mute or any matching dynamic mute rules.

### Severity
    
    
    Severity(value)

The severity of the finding.
    
    
        A critical vulnerability is easily discoverable
        by an external actor, exploitable, and results
        in the direct ability to execute arbitrary code,
        exfiltrate data, and otherwise gain additional
        access and privileges to cloud resources and
        workloads. Examples include publicly accessible
        unprotected user data and public SSH access with
        weak or no passwords.
    
        Threat:
    
        Indicates a threat that is able to access,
        modify, or delete data or execute unauthorized
        code within existing resources.
    HIGH (2):
        Vulnerability:
    
        A high risk vulnerability can be easily
        discovered and exploited in combination with
        other vulnerabilities in order to gain direct
        access and the ability to execute arbitrary
        code, exfiltrate data, and otherwise gain
        additional access and privileges to cloud
        resources and workloads. An example is a
        database with weak or no passwords that is only
        accessible internally. This database could
        easily be compromised by an actor that had
        access to the internal network.
    
        Threat:
    
        Indicates a threat that is able to create new
        computational resources in an environment but
        not able to access data or execute code in
        existing resources.
    MEDIUM (3):
        Vulnerability:
    
        A medium risk vulnerability could be used by an
        actor to gain access to resources or privileges
        that enable them to eventually (through multiple
        steps or a complex exploit) gain access and the
        ability to execute arbitrary code or exfiltrate
        data. An example is a service account with
        access to more projects than it should have. If
        an actor gains access to the service account,
        they could potentially use that access to
        manipulate a project the service account was not
        intended to.
    
        Threat:
    
        Indicates a threat that is able to cause
        operational impact but may not access data or
        execute unauthorized code.
    LOW (4):
        Vulnerability:
    
        A low risk vulnerability hampers a security
        organization's ability to detect vulnerabilities
        or active threats in their deployment, or
        prevents the root cause investigation of
        security issues. An example is monitoring and
        logs being disabled for resource configurations
        and access.
    
        Threat:
    
        Indicates a threat that has obtained minimal
        access to an environment but is not able to
        access data, execute code, or create resources.
    

### SourcePropertiesEntry
    
    
    SourcePropertiesEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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

The state of the finding.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
