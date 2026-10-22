---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mitre-att-and-ck/
title: Integrate MITRE ATT&CK with Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:39.159133+00:00
---

# Integrate MITRE ATT&CK with Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mitre-att-and-ck/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate MITRE ATT&CK with Google Security Operations

This document explains how to integrate MITRE ATT&CK with Google Security Operations (Google SecOps).

## Use cases

The **MITRE ATT &CK** integration uses the Google SecOps capabilities to support the following use cases:

  * **Tactical threat correlation** : Automatically identify _Intrusion Sets_ (known threat groups) associated with a specific malicious attack technique or tactic observed in an alert, providing immediate context on the threat actor behind the activity.

  * **Mitigation Gap Analysis** : For a flagged attack technique, automatically retrieve and analyze the associated Mitigations available in the MITRE ATT&CK framework. This allows security teams to verify if their current defense controls are sufficient or if patching or tool implementation is required.

  * **Incident Enrichment and Prioritization** : Enrich security incidents by adding detailed technique information (including description, detection methods, and data sources) directly to the case wall, helping analysts quickly understand the attack methodology and prioritize response steps.

  * **Historical Technique Analysis** : Search for comprehensive details on any MITRE ATT&CK Technique by its identifier (such as T1050), facilitating proactive threat hunting and providing authoritative knowledge for security training and reporting.




## Before you begin

This integration provides native platform capabilities and doesn't require external third-party API keys or credentials for authentication. Before you begin, ensure the integration is installed from the Content Hub within your Google SecOps instance.

## Integration parameters

The **MITRE ATT &CK** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` |  Required. The URL address of the MITRE ATT&CK CTI repository instance.  
`Verify SSL` |  Optional. If selected, the integration validates the SSL certificate when connecting to the MITRE ATT&CK server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

**Note:** The integration retrieves all MITRE ATT&CK object information, including Intrusion Sets, directly from the [MITRE ATT&CK CTI repository](https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json). 

This repository serves as the authoritative source for the integration's threat intelligence data.

### Get Associated Intrusions

Use the **Get Associated Intrusions** action to retrieve information about the Intrusion Sets (known adversary groups) linked to a specific MITRE ATT&CK Technique.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Associated Intrusions** action requires the following parameters:

Parameter | Description  
---|---  
`Technique ID` | Required. The identifier (ID, Name, or External ID) used to find associated intrusion sets.  
`Identifier Type` | Required. The type of identifier provided in `Technique ID`. **Note:** The UI options correspond to the `name`, `id`, and `external_id` fields in the raw JSON output. The possible values are as follows:

  * `Attack Name` (such as `Access Token Manipulation`)
  * `Attack ID` (such as `attack-pattern--478...`)
  * `External Attack ID` (such as `T1050`)

The default value is `Attack ID`.  
`Max Intrusions to Return` | Optional. The maximum number of intrusion sets to retrieve. The default value is `20`.  
  
#### Action outputs

The **Get Associated Intrusions** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON Result

The following example shows the JSON result outputs received when using the **Get Associated Intrusions** action:

**Note:** The terms `Attack ID`, `Attack Name`, and `External Attack ID` are generic labels used in the UI's drop-down menu. They correspond to the `id`, `name`, and `external_id` fields in the JSON output, which can represent various MITRE ATT&CK objects (such as Intrusion Sets).
    
    
    [
    {
        "created_by_ref":"identity--generic-ref-a1b2c3d4e5f6",
        "description":"[ADVERSARY GROUP 01](https://attack.mitre.org/groups/G0001) is a threat group that has been active since at least 2014. The group ...",
        "created":"2017-12-14T16:46:06.044Z",
        "x_mitre_contributors":["Security Researcher A, Organization B"],
        "modified":"2019-07-17T13:11:37.402Z",
        "name":"ADVERSARY GROUP 01",
        "object_marking_refs":["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
        "x_mitre_version":"2.0",
        "aliases":["ADVERSARY-01","ThreatGroup A","CyberSquad X","T-C-00"],
        "type":"intrusion-set",
        "id":"intrusion-set--a1b2c3d4-e5f6-7g8h-9i0j-1k2l3m4n5o6p",
        "external_references":
        [
            {
                "url":"https://attack.mitre.org/groups/G0001",
                "source_name":"mitre-attack",
                "external_id":"G0001"
            },{
                "source_name":"ADVERSARY GROUP 01",
                "description":"(Citation: SecurityVendor A May 2017) (Citation: Research Org B Nov 2017)(Citation: SecurityFirm C May 2017)"
            }]},{
                "created_by_ref":"identity--generic-ref-a1b2c3d4e5f6",
                "name":"ADVERSARY GROUP 02",
                "created":"2018-01-16T16:13:52.465Z",
                "description":"[ADVERSARY GROUP 02](https://attack.mitre.org/groups/G0002) is a cyber espionage group with...",
                "modified":"2019-03-22T19:57:36.804Z",
                "object_marking_refs":["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
                "external_references": [
                    {
                        "url":"https://attack.mitre.org/groups/G0002",
                        "source_name":"mitre-attack",
                        "external_id":"G0002"
                    },{
                        "source_name":"ADVERSARY GROUP 02",
                        "description":"(Citation: Trend Research Daserf Nov 2017)"
                    }],
                "x_mitre_version":"1.0",
                "type":"intrusion-set",
                "id":"intrusion-set--b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q",
                "aliases":["ADVERSARY-02","ResearchGroup Z","Tango"]
            },{
                "created_by_ref":"identity--generic-ref-a1b2c3d4e5f6",
                "name":"ADVERSARY GROUP 03",
                "created":"2018-01-16T16:13:52.465Z",
                "description":"[ADVERSARY GROUP 03](https://attack.mitre.org/groups/G0003) is a cyber espionage group that has been ...",
                "modified":"2019-05-03T16:42:19.026Z",
                "object_marking_refs":["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
                "external_references":
              [{
                  "url":"https://attack.mitre.org/groups/G0003",
                  "source_name":"mitre-attack",
                  "external_id":"G0003"
              },{
                  "source_name":"ADVERSARY GROUP 03",
                  "description":"(Citation: ClearSky Analysis March 2017) (Citation: ClearSky Report July 2017) (Citation: Research Nov 2015)"
              },],
                "x_mitre_version":"1.1",
                "type":"intrusion-set",
                "id":"intrusion-set--c1d2e3f4-g5h6-7i8j-9k0l-1m2n3o4p5q6r",
                "aliases":["ADVERSARY-03"]
            }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Get Associated Intrusions** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Mitigations

Use the **Get Mitigations** action to retrieve Mitigation strategies associated with a specific MITRE ATT&CK Technique.

This action doesn't run on Google SecOps entities. 

**Important:** This action uses the internal MITRE ATT&CK `id` field for searching within the [MITRE ATT&CK JSON data](https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json). 

Results are only returned if the MITRE ATT&CK data includes a direct relationship of the type `'mitigates'` linking the mitigation to the technique.

#### Action inputs

The **Get Mitigations** action requires the following parameters:

Parameter | Description  
---|---  
`Technique ID` | Required. The identifier (Name, Internal ID, or External ID) used to find associated mitigations for the MITRE ATT&CK Technique.  
`Identifier Type` | Required. The type of identifier provided in `Technique ID`. **Note:** The UI options correspond to the `name`, `id`, and `external_id` fields in the raw JSON output. The possible values are as follows:

  * `Attack Name` (such as `Access Token Manipulation`)
  * `Attack ID` (such as `attack-pattern--478...`)
  * `External Attack ID` (such as `T1050`)

The default value is `Attack ID`.  
`Max Mitigations to Return` | Optional. The maximum number of mitigation controls to retrieve. The default value is `20`.  
  
#### Action outputs

The **Get Mitigations** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON Result

The following example shows the JSON result outputs received when using the **Get Mitigations** action:
    
    
    [
        {
            "created_by_ref": "identity--generic-ref-a1b2c3d4e5f6",
            "description": "Examine and restrict unnecessary system utilities, third-party tools, or software capable of file encryption. Audit and/or block these tools using application control methods (Citation: Resource A 2010), such as Whitelisting Policy (Citation: Security Blog C 2016) or Software Restriction Mechanisms (Citation: Security Guide D 2014) where applicable. (Citation: Tech Ref E)",
            "created": "2018-10-17T00:14:20.652Z",
            "x_mitre_deprecated": true,
            "modified": "2019-07-24T14:26:14.411Z",
            "object_marking_refs": ["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
            "external_references": [
                {
                    "url": "https://attack.mitre.org/mitigations/T9000",
                    "source_name": "mitre-attack",
                    "external_id": "T9000"
                },
                {
                    "url": "http://www.generic-security.org/whitepapers/application/app-whitelisting-33599",
                    "source_name": "Resource A 2010",
                    "description": "General Author, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014."
                },
                {
                    "url": "http://blog.generic-cert.org/2016/01/windows-commands-abused-by-attackers.html",
                    "source_name": "Security Blog C 2016",
                    "description": "Researcher X. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016."
                },
                {
                    "url": "https://www.generic-agency.gov/ia-guidance/tech-briefs/app-whitelisting.cfm",
                    "source_name": "Security Guide D 2014",
                    "description": "Government Agency Directorate. (2014, August). Application Whitelisting Using Policy Engine. Retrieved March 31, 2016."
                },
                {
                    "url": "http://technet.generic-corp.com/magazine/2008.06.srp.aspx",
                    "source_name": "Tech Ref E 2008",
                    "description": "Author C, & Author D. P. (2008, June). Application Lockdown with Restriction Policies. Retrieved November 18, 2014."
                },
                {
                    "url": "https://technet.generic-corp.com/library/ee791851.aspx",
                    "source_name": "Tech Ref F",
                    "description": "Generic Corp. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016."
                }
            ],
            "x_mitre_version": "1.0",
            "type": "course-of-action",
            "id": "course-of-action--a1b2c3d4-e5f6-7g8h-9i0j-1k2l3m4n5o6p",
            "name": "File Encryption Mitigation"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Get Mitigations** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Technique Details

Use the **Get Technique Details** action to retrieve comprehensive, detailed information about a specific MITRE ATT&CK Technique.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Technique Details** action requires the following parameters:

Parameter | Description  
---|---  
`Technique Identifier` | Required. A comma-separated list of identifiers (Name, Internal ID, or External ID) used to find detailed information about MITRE ATT&CK Techniques.  
`Identifier Type` | Required. The type of identifier provided in `Technique Identifier`. **Note:** The UI options correspond to the `name`, `id`, and `external_id` fields in the raw JSON output. The possible values are as follows:

  * `Attack Name` (Example: `Access Token Manipulation`)
  * `Attack ID` (Example: `attack-pattern--478...`)
  * `External Attack ID` (Example: `T1050`)

The default value is `Attack ID`.  
`Create Insights` | Optional. If selected, the action generates a separate security insight for every processed MITRE ATT&CK Technique. Disabled by default.  
  
#### Action outputs

The **Get Technique Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON Result

The following example shows the JSON result outputs received when using the **Get Technique Details** action:
    
    
    {
        "created_by_ref": "identity--generic-ref-a1b2c3d4e5f6",
        "external_references": [
            {
                "url": "https://attack.mitre.org/techniques/T9000",
                "external_id": "T9000",
                "source_name": "mitre-attack"
            },
            {
                "url": "http://www.security-research.org/~author/DetectingEncryptedTraffic.pdf",
                "source_name": "Research Group A 2013",
                "description": "Author, H., Co-Author, C., & Co-Author, D. (2013, April). Detecting encrypted botnet traffic. Retrieved August 19, 2015."
            },
            {
                "url": "https://generic-wiki.org/FileSignatures",
                "source_name": "Wiki File Header Signatures",
                "description": "Generic Wiki. (2016, March 31). List of file signatures. Retrieved April 22, 2016."
            }
        ],
        "created": "2017-05-31T21:30:30.26Z",
        "x_mitre_platforms": ["Linux", "macOS", "Windows"],
        "type": "attack-pattern",
        "description": "Sensitive data is encrypted prior to exfiltration to conceal the information from detection tools or to make the activity less conspicuous upon defender inspection. The encryption process uses a utility, programming library, or custom script and is separate from any encryption used by the command and control or file transfer protocol. Common archive formats capable of encryption include RAR and zip.\\n\\nOther exfiltration techniques may be used to transfer the encrypted information out of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041) and [Exfiltration Over Alternate Protocol](https://attack.mitre.org/techniques/T1048)",
        "kill_chain_phases": [
            {
                "phase_name": "exfiltration",
                "kill_chain_name": "mitre-attack"
            }
        ],
        "modified": "2018-10-17T00:14:20.652Z",
        "id": "attack-pattern--a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "object_marking_refs": ["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
        "x_mitre_network_requirements": false,
        "x_mitre_version": "1.0",
        "x_mitre_data_sources": ["File monitoring", "Process monitoring", "Process command-line parameters", "Binary file metadata"],
        "x_mitre_detection": "Encrypted files and related execution software can be detected through various means. Monitoring processes and command-line arguments for known encryption utilities may reveal suspicious activity. A process loading a key operating system DLL may be utilized to perform encryption. \\n\\nNetwork traffic analysis can reveal high entropy data indicative of encrypted transmission (Citation: Research Group A 2013). If the communications channel is unencrypted, network intrusion or DLP systems can detect encrypted files in transit by analyzing file headers (Citation: Wiki File Header Signatures).",
        "name": "Data Encryption for Exfiltration"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Get Technique Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Techniques Details

Use the **Get Techniques Details** action to retrieve comprehensive, detailed information about MITRE ATT&CK Techniques.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Techniques Details** action requires the following parameters:

Parameter | Description  
---|---  
`Technique Identifier` | Required. A comma-separated list of identifiers (Name, Internal ID, or External ID) used to find detailed information about MITRE ATT&CK Techniques.  
`Identifier Type` | Required. The type of identifier provided in `Technique Identifier`. **Note:** The UI options correspond to the `name`, `id`, and `external_id` fields in the raw JSON output. The possible values are as follows:

  * `Name` (Example: `Access Token Manipulation`)
  * `ID` (Example: `attack-pattern--478...`)
  * `External ID` (Example: `T1050`)

The default value is `ID`.  
  
#### Action outputs

The **Get Techniques Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON Result

The following example shows the JSON result outputs received when using the **Get Techniques Details** action:
    
    
    [
        {
            "Entity": "course-of-action--generic-ref-1a2b3c4d5e6f",
            "EntityResult": {
                "created_by_ref": "identity--generic-ref-a1b2c3d4e5f6",
                "external_references": [
                    {
                        "url": "https://attack.mitre.org/techniques/T9000",
                        "external_id": "T9000",
                        "source_name": "mitre-attack"
                    },
                    {
                        "url": "http://www.security-research.org/~author/encrypted-botnet-traffic.pdf",
                        "source_name": "Research Group A 2013",
                        "description": "Author, H., Co-Author, C., & Massey, D. (2013, April). Detecting encrypted botnet traffic. Retrieved August 19, 2015."
                    },
                    {
                        "url": "https://generic-wiki.org/FileHeaderSignatures",
                        "source_name": "Wiki File Header Signatures",
                        "description": "Generic Wiki. (2016, March 31). List of file signatures. Retrieved April 22, 2016."
                    }
                ],
                "created": "2017-05-31T21:30:30.26Z",
                "x_mitre_platforms": ["Linux", "macOS", "Windows"],
                "type": "attack-pattern",
                "description": "Sensitive data is encrypted prior to exfiltration to conceal the information from detection tools or to make the activity less conspicuous upon defender inspection. The encryption process uses a utility, programming library, or custom script and is separate from any encryption used by the command and control or file transfer protocol. Common archive formats capable of encryption include RAR and zip.\\n\\nOther exfiltration techniques likely apply as well to transfer the information out of the network, such as [Exfiltration Over Command and Control Channel](https://attack.mitre.org/techniques/T1041) and [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048)",
                "kill_chain_phases": [
                    {
                        "phase_name": "exfiltration",
                        "kill_chain_name": "mitre-attack"
                    }
                ],
                "modified": "2018-10-17T00:14:20.652Z",
                "id": "attack-pattern--a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
                "object_marking_refs": ["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
                "x_mitre_network_requirements": false,
                "x_mitre_version": "1.0",
                "x_mitre_data_sources": [
                    "File monitoring",
                    "Process monitoring",
                    "Process command-line parameters",
                    "Binary file metadata"
                ],
                "x_mitre_detection": "Encryption software and encrypted files can be detected in many ways. Common utilities that may be present on the system or brought in by an adversary may be detectable through process monitoring and monitoring for command-line arguments for known encryption utilities. This may yield a significant amount of benign events, depending on how systems in the environment are typically used. The encryption key is often stated within command-line invocation of the software. A process that loads the Windows DLL crypt32.dll may be used to perform encryption, decryption, or verification of file signatures. Network traffic may also be analyzed for entropy to determine if encrypted data is being transmitted. (Citation: Research Group A 2013) If the communications channel is unencrypted, encrypted files of known file types can be detected in transit during exfiltration with a network intrusion detection or data loss prevention system analyzing file headers. (Citation: Wiki File Header Signatures)",
                "name": "Data Encryption for Exfiltration"
            }
        }
    ]
    

##### Output messages

The **Get Techniques Details** action can return the following output messages:

Output message | Message description  
---|---  
`Retrieved detailed information about the following techniques: TECHNIQUES.` `Action wasn't able to retrieve detailed information about the following techniques: TECHNIQUES` `Action wasn't able to find the provided techniques.` | The action succeeded.  
`Error executing action "Get Technique Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Techniques Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Techniques Mitigations

Use the **Get Techniques Mitigations** action to retrieve Mitigation strategies associated with a specified list of MITRE attack Techniques.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Techniques Mitigations** action requires the following parameters:

Parameter | Description  
---|---  
`Technique ID` | Required. A comma-separated list of identifiers (Name, Internal ID, or External ID) used to find associated mitigations for the MITRE ATT&CK Techniques.  
`Identifier Type` | Required. The type of identifier provided in `Technique ID`. The possible values are as follows:

  * `Attack Name` (Example: `Access Token Manipulation`)
  * `Attack ID` (Example: `attack-pattern--478...`)
  * `External Attack ID` (Example: `T1050`)

The default value is `Attack ID`.  
`Max Mitigations to Return` | Optional. The maximum number of mitigation controls to retrieve. The default value is `20`.  
  
#### Action outputs

The **Get Techniques Mitigations** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON Result

The following example shows the JSON result outputs received when using the **Get Techniques Mitigations** action:
    
    
    [
        {
            "Entity": "course-of-action--generic-ref-1a2b3c4d5e6f",
            "EntityResult": {
                "mitigations": [
                    {
                        "created_by_ref": "identity--generic-ref-a1b2c3d4e5f6",
                        "description": "Examine and restrict unnecessary system utilities, third-party tools, or software capable of file encryption. Audit and/or block these tools using application control methods (Citation: Research Org A 2010) such as Whitelisting Policy (Citation: Security Blog C 2016) or Software Restriction Mechanisms (Citation: Security Guide D 2014) where appropriate. (Citation: Tech Ref E)",
                        "created": "2018-10-17T00:14:20.652Z",
                        "x_mitre_deprecated": true,
                        "modified": "2019-07-24T14:26:14.411Z",
                        "object_marking_refs": ["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
                        "external_references": [
                            {
                                "url": "https://attack.mitre.org/mitigations/T9000",
                                "source_name": "mitre-attack",
                                "external_id": "T9000"
                            },
                            {
                                "url": "http://www.generic-security.org/whitepapers/application/app-whitelisting-33599",
                                "source_name": "Research Org A 2010",
                                "description": "Generic Author, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014."
                            },
                            {
                                "url": "http://blog.generic-cert.org/2016/01/windows-commands-abused-by-attackers.html",
                                "source_name": "Security Blog C 2016",
                                "description": "Researcher X. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016."
                            },
                            {
                                "url": "https://www.generic-agency.gov/ia-guidance/tech-briefs/app-whitelisting.cfm",
                                "source_name": "Security Guide D 2014",
                                "description": "Government Agency Directorate. (2014, August). Application Whitelisting Using Policy Engine. Retrieved March 31, 2016."
                            },
                            {
                                "url": "http://technet.generic-corp.com/magazine/2008.06.srp.aspx",
                                "source_name": "Tech Ref E 2008",
                                "description": "Author C, & Author D. P. (2008, June). Application Lockdown with Restriction Policies. Retrieved November 18, 2014."
                            },
                            {
                                "url": "https://technet.generic-corp.com/library/ee791851.aspx",
                                "source_name": "Tech Ref F",
                                "description": "Generic Corp. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016."
                            }
                        ],
                        "x_mitre_version": "1.0",
                        "type": "course-of-action",
                        "id": "course-of-action--a1b2c3d4-e5f6-7g8h-9i0j-1k2l3m4n5o6p",
                        "name": "File Encryption Mitigation"
                    }
                ]
            }
        }
    ]
    

##### Output messages

The **Get Techniques Mitigations** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved mitigations for the following techniques: TECHNIQUES.` `Action wasn't able to to find mitigations for the following techniques: TECHNIQUES` | The action succeeded.  
`Error executing action "Get Techniques Mitigations". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Techniques Mitigations** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to MITRE ATT&CK.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
