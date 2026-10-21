---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection/
title: Use Virtual Machine Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:05.555517+00:00
---

# Use Virtual Machine Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Virtual Machine Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes how to view and manage VM Threat Detection findings. It also shows you how to enable or disable the service and its modules.

## Overview

Virtual Machine Threat Detection is a built-in service of Security Command Center. This service scans virtual machines to detect potentially malicious applications, such as cryptocurrency mining software, kernel-mode rootkits, and malware running in compromised cloud environments.

VM Threat Detection is part of the Security Command Center threat detection suite and is designed to complement the existing capabilities of [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview).

For more information, see [VM Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview).

## Before you begin

To get the permissions that you need to manage the Virtual Machine Threat Detection service and its modules, ask your administrator to grant you the [Security Center Management Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.admin) (`roles/securitycentermanagement.admin`) IAM role on the organization, folder, or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Test VM Threat Detection

To test VM Threat Detection cryptocurrency mining detection, you can run a cryptocurrency mining application on your VM. For a list of binary names and [YARA rules](https://yara.readthedocs.io/en/v4.1.0/index.html) that trigger findings, see Software names and YARA rules. If you install and test mining applications, we recommended that you only run applications in an isolated test environment, closely monitor their use, and remove them completely after testing.

To test VM Threat Detection malware detection, you can download malware applications on your VM. If you download malware, we recommend that you do so in an isolated test environment, and remove them completely after testing.

## Review findings in the Google Cloud console

To review VM Threat Detection findings in the Google Cloud console, do the following:

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for your organization, you must access the page using the jurisdictional console. For more information, see [Use the console with data residency enabled](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#console-jconsole).

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Virtual Machine Threat Detection**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



For information about how to respond to a specific VM Threat Detection finding, search for the finding in the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).

For high-level response recommendations, see [Respond to Compute Engine threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-compute-engine-threats).

For a list of VM Threat Detection findings, see [Findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#findings).

### Severity

VM Threat Detection findings are assigned **High** , **Medium** , and **Low** severity based on the threat classification confidence.

### Combined detections

Combined detections occur when multiple categories of findings are detected within a day. The findings can be caused by one or more malicious applications. For example, a single application can simultaneously trigger `Execution: Cryptocurrency Mining YARA Rule` and `Execution: Cryptocurrency Mining Hash Match` findings. However, all threats detected from a single source within the same day are rolled into one _combined detection_ finding. In the following days, if more threats are found, even the same ones, they are attached to new findings.

For an example of a combined detection finding, see Example finding formats.

## Example finding formats

This section provides examples of JSON output for VM Threat Detection findings. You see this output when you [export findings](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#export-console) using the Google Cloud console or [list findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings) using the Security Command Center API or the Google Cloud CLI.

The examples on this page show different types of findings. Each example includes only the fields that are most relevant to that type of finding. For a complete list of fields that are available in a finding, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings) resource.

You can [export findings through the Security Command Center console](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#export-console) or [list findings through the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings).

To see the example findings, expand one or more of the following nodes. For information about each field in the finding, see [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#resource:-finding).

### `Defense Evasion: Rootkit`

This output example shows a finding of a known kernel-mode rootkit: Diamorphine. 
    
    
    {
      "findings": {
        "access": {},
        "assetDisplayName": "DISPLAY_NAME",
        "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Defense Evasion: Rootkit",
        "createTime": "2023-01-12T00:39:33.007Z",
        "database": {},
        "eventTime": "2023-01-11T21:24:05.326Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
        "indicator": {},
        "kernelRootkit": {
          "name": "Diamorphine",
          "unexpected_kernel_code_pages": true,
          "unexpected_system_call_handler": true
        },
        "kubernetes": {},
        "mitreAttack": {
          "version": "9"
        },
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Virtual Machine Threat Detection",
        "processes": [],
        "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
        "severity": "HIGH",
        "sourceDisplayName": "Virtual Machine Threat Detection",
        "state": "ACTIVE",
        "vulnerability": {},
        "workflowState": "NEW"
      },
      "resource": {
        "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
        "display_name": "DISPLAY_NAME",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "project_display_name": "PROJECT_ID",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parent_display_name": "DISPLAY_NAME",
        "type": "google.compute.Instance",
        "folders": []
      },
      "sourceProperties": {}
    }
          

### `Defense Evasion: Unexpected ftrace handler`
    
    
      {
        "findings": {
          "access": {},
          "assetDisplayName": "DISPLAY_NAME",
          "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
          "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
          "category": "Defense Evasion: Unexpected ftrace handler",
          "createTime": "2023-01-12T00:39:33.007Z",
          "database": {},
          "eventTime": "2023-01-11T21:24:05.326Z",
          "exfiltration": {},
          "findingClass": "THREAT",
          "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
          "indicator": {},
          "kernelRootkit": {},
          "kubernetes": {},
          "mitreAttack": {
            "version": "9"
          },
          "mute": "UNDEFINED",
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
          "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
          "parentDisplayName": "Virtual Machine Threat Detection",
          "processes": [],
          "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "severity": "HIGH",
          "sourceDisplayName": "Virtual Machine Threat Detection",
          "state": "ACTIVE",
          "vulnerability": {},
          "workflowState": "NEW"
        },
        "resource": {
          "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "display_name": "DISPLAY_NAME",
          "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "project_display_name": "PROJECT_ID",
          "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "parent_display_name": "DISPLAY_NAME",
          "type": "google.compute.Instance",
          "folders": []
        },
        "sourceProperties": {}
      }
          

### `Defense Evasion: Unexpected interrupt handler`
    
    
      {
        "findings": {
          "access": {},
          "assetDisplayName": "DISPLAY_NAME",
          "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
          "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
          "category": "Defense Evasion: Unexpected interrupt handler",
          "createTime": "2023-01-12T00:39:33.007Z",
          "database": {},
          "eventTime": "2023-01-11T21:24:05.326Z",
          "exfiltration": {},
          "findingClass": "THREAT",
          "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
          "indicator": {},
          "kernelRootkit": {},
          "kubernetes": {},
          "mitreAttack": {
            "version": "9"
          },
          "mute": "UNDEFINED",
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
          "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
          "parentDisplayName": "Virtual Machine Threat Detection",
          "processes": [],
          "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "severity": "HIGH",
          "sourceDisplayName": "Virtual Machine Threat Detection",
          "state": "ACTIVE",
          "vulnerability": {},
          "workflowState": "NEW"
        },
        "resource": {
          "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "display_name": "DISPLAY_NAME",
          "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "project_display_name": "PROJECT_ID",
          "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "parent_display_name": "DISPLAY_NAME",
          "type": "google.compute.Instance",
          "folders": []
        },
        "sourceProperties": {}
      }
          

### `Defense Evasion: Unexpected kernel modules`
    
    
      {
        "findings": {
          "access": {},
          "assetDisplayName": "DISPLAY_NAME",
          "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
          "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
          "category": "Defense Evasion: Unexpected kernel modules",
          "createTime": "2023-01-12T00:39:33.007Z",
          "database": {},
          "eventTime": "2023-01-11T21:24:05.326Z",
          "exfiltration": {},
          "findingClass": "THREAT",
          "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
          "indicator": {},
          "kernelRootkit": {},
          "kubernetes": {},
          "mitreAttack": {
            "version": "9"
          },
          "mute": "UNDEFINED",
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
          "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
          "parentDisplayName": "Virtual Machine Threat Detection",
          "processes": [],
          "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "severity": "HIGH",
          "sourceDisplayName": "Virtual Machine Threat Detection",
          "state": "ACTIVE",
          "vulnerability": {},
          "workflowState": "NEW"
        },
        "resource": {
          "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "display_name": "DISPLAY_NAME",
          "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "project_display_name": "PROJECT_ID",
          "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "parent_display_name": "DISPLAY_NAME",
          "type": "google.compute.Instance",
          "folders": []
        },
        "sourceProperties": {}
      }
          

### `Defense Evasion: Unexpected kernel read-only data modification`
    
    
      {
        "findings": {
          "access": {},
          "assetDisplayName": "DISPLAY_NAME",
          "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
          "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
          "category": "Defense Evasion: Unexpected kernel read-only data modification",
          "createTime": "2023-01-12T00:39:33.007Z",
          "database": {},
          "eventTime": "2023-01-11T21:24:05.326Z",
          "exfiltration": {},
          "findingClass": "THREAT",
          "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
          "indicator": {},
          "kernelRootkit": {},
          "kubernetes": {},
          "mitreAttack": {
            "version": "9"
          },
          "mute": "UNDEFINED",
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
          "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
          "parentDisplayName": "Virtual Machine Threat Detection",
          "processes": [],
          "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "severity": "HIGH",
          "sourceDisplayName": "Virtual Machine Threat Detection",
          "state": "ACTIVE",
          "vulnerability": {},
          "workflowState": "NEW"
        },
        "resource": {
          "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "display_name": "DISPLAY_NAME",
          "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "project_display_name": "PROJECT_ID",
          "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "parent_display_name": "DISPLAY_NAME",
          "type": "google.compute.Instance",
          "folders": []
        },
        "sourceProperties": {}
      }
          

### `Defense Evasion: Unexpected kprobe handler`
    
    
      {
        "findings": {
          "access": {},
          "assetDisplayName": "DISPLAY_NAME",
          "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
          "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
          "category": "Defense Evasion: Unexpected kprobe handler",
          "createTime": "2023-01-12T00:39:33.007Z",
          "database": {},
          "eventTime": "2023-01-11T21:24:05.326Z",
          "exfiltration": {},
          "findingClass": "THREAT",
          "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
          "indicator": {},
          "kernelRootkit": {},
          "kubernetes": {},
          "mitreAttack": {
            "version": "9"
          },
          "mute": "UNDEFINED",
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
          "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
          "parentDisplayName": "Virtual Machine Threat Detection",
          "processes": [],
          "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "severity": "HIGH",
          "sourceDisplayName": "Virtual Machine Threat Detection",
          "state": "ACTIVE",
          "vulnerability": {},
          "workflowState": "NEW"
        },
        "resource": {
          "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "display_name": "DISPLAY_NAME",
          "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "project_display_name": "PROJECT_ID",
          "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "parent_display_name": "DISPLAY_NAME",
          "type": "google.compute.Instance",
          "folders": []
        },
        "sourceProperties": {}
      }
          

### `Defense Evasion: Unexpected processes in runqueue`
    
    
      {
        "findings": {
          "access": {},
          "assetDisplayName": "DISPLAY_NAME",
          "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
          "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
          "category": "Defense Evasion: Unexpected processes in runqueue",
          "createTime": "2023-01-12T00:39:33.007Z",
          "database": {},
          "eventTime": "2023-01-11T21:24:05.326Z",
          "exfiltration": {},
          "findingClass": "THREAT",
          "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
          "indicator": {},
          "kernelRootkit": {},
          "kubernetes": {},
          "mitreAttack": {
            "version": "9"
          },
          "mute": "UNDEFINED",
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
          "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
          "parentDisplayName": "Virtual Machine Threat Detection",
          "processes": [],
          "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "severity": "HIGH",
          "sourceDisplayName": "Virtual Machine Threat Detection",
          "state": "ACTIVE",
          "vulnerability": {},
          "workflowState": "NEW"
        },
        "resource": {
          "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "display_name": "DISPLAY_NAME",
          "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "project_display_name": "PROJECT_ID",
          "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "parent_display_name": "DISPLAY_NAME",
          "type": "google.compute.Instance",
          "folders": []
        },
        "sourceProperties": {}
      }
          

### `Defense Evasion: Unexpected system call handler`
    
    
      {
        "findings": {
          "access": {},
          "assetDisplayName": "DISPLAY_NAME",
          "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
          "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
          "category": "Defense Evasion: Unexpected system call handler",
          "createTime": "2023-01-12T00:39:33.007Z",
          "database": {},
          "eventTime": "2023-01-11T21:24:05.326Z",
          "exfiltration": {},
          "findingClass": "THREAT",
          "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
          "indicator": {},
          "kernelRootkit": {},
          "kubernetes": {},
          "mitreAttack": {
            "version": "9"
          },
          "mute": "UNDEFINED",
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
          "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
          "parentDisplayName": "Virtual Machine Threat Detection",
          "processes": [],
          "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "severity": "HIGH",
          "sourceDisplayName": "Virtual Machine Threat Detection",
          "state": "ACTIVE",
          "vulnerability": {},
          "workflowState": "NEW"
        },
        "resource": {
          "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
          "display_name": "DISPLAY_NAME",
          "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "project_display_name": "PROJECT_ID",
          "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
          "parent_display_name": "DISPLAY_NAME",
          "type": "google.compute.Instance",
          "folders": []
        },
        "sourceProperties": {}
      }
          

### `Execution: Cryptocurrency Mining Combined Detection`

This output example shows a threat that was detected by both the `CRYPTOMINING_HASH` and `CRYPTOMINING_YARA` modules. 
    
    
    {
      "findings": {
        "access": {},
        "assetDisplayName": "DISPLAY_NAME",
        "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
        "canonicalName": "projects/PROJECT_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Cryptocurrency Mining Combined Detection",
        "createTime": "2023-01-05T01:40:48.994Z",
        "database": {},
        "eventTime": "2023-01-05T01:39:36.876Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
        "indicator": {
          "signatures": [
            {
              "yaraRuleSignature": {
                "yaraRule": "YARA_RULE1"
              }
            },
            {
              "yaraRuleSignature": {
                "yaraRule": "YARA_RULE9"
              }
            },
            {
              "yaraRuleSignature": {
                "yaraRule": "YARA_RULE10"
              }
            },
            {
              "yaraRuleSignature": {
                "yaraRule": "YARA_RULE25"
              }
            },
            {
              "memoryHashSignature": {
                "binaryFamily": "XMRig",
                "detections": [
                  {
                    "binary": "linux-x86-64_xmrig_6.12.2",
                    "percentPagesMatched": 1
                  }
                ]
              }
            }
          ]
        },
        "kernelRootkit": {},
        "kubernetes": {},
        "mitreAttack": {
          "version": "9"
        },
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Virtual Machine Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "BINARY_PATH"
            },
            "script": {},
            "args": [
              "./miner",
              ""
            ],
            "pid": "123",
            "parentPid": "456",
            "name": "miner"
          }
        ],
        "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
        "severity": "HIGH",
        "sourceDisplayName": "Virtual Machine Threat Detection",
        "state": "ACTIVE",
        "vulnerability": {},
        "workflowState": "NEW"
      },
      "resource": {
        "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
        "display_name": "DISPLAY_NAME",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "project_display_name": "DISPLAY_NAME",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "parent_display_name": "DISPLAY_NAME",
        "type": "google.compute.Instance",
        "folders": []
      },
      "sourceProperties": {}
    }
        

### `Execution: Cryptocurrency Mining Hash Match Detection`
    
    
    {
      "findings": {
        "access": {},
        "assetDisplayName": "DISPLAY_NAME",
        "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
        "canonicalName": "projects/PROJECT_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Cryptocurrency Mining Hash Match",
        "createTime": "2023-01-05T01:40:48.994Z",
        "database": {},
        "eventTime": "2023-01-05T01:39:36.876Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
        "indicator": {
          "signatures": [
            {
              "memoryHashSignature": {
                "binaryFamily": "XMRig",
                "detections": [
                  {
                    "binary": "linux-x86-64_xmrig_6.12.2",
                    "percentPagesMatched": 1
                  }
                ]
              }
            }
          ]
        },
        "kernelRootkit": {},
        "kubernetes": {},
        "mitreAttack": {
          "version": "9"
        },
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Virtual Machine Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "BINARY_PATH"
            },
            "script": {},
            "args": [
              "./miner",
              ""
            ],
            "pid": "123",
            "parentPid": "456",
            "name": "miner"
          }
        ],
        "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
        "severity": "HIGH",
        "sourceDisplayName": "Virtual Machine Threat Detection",
        "state": "ACTIVE",
        "vulnerability": {},
        "workflowState": "NEW"
      },
      "resource": {
        "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
        "display_name": "DISPLAY_NAME",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "project_display_name": "DISPLAY_NAME",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "parent_display_name": "DISPLAY_NAME",
        "type": "google.compute.Instance",
        "folders": []
      },
      "sourceProperties": {}
    }
        

### `Execution: Cryptocurrency Mining YARA Rule`
    
    
    {
      "findings": {
        "access": {},
        "assetDisplayName": "DISPLAY_NAME",
        "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
        "canonicalName": "projects/PROJECT_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Cryptocurrency Mining YARA Rule",
        "createTime": "2023-01-05T00:37:38.450Z",
        "database": {},
        "eventTime": "2023-01-05T01:12:48.828Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
        "indicator": {
          "signatures": [
            {
              "yaraRuleSignature": {
                "yaraRule": "YARA_RULE9"
              }
            },
            {
              "yaraRuleSignature": {
                "yaraRule": "YARA_RULE10"
              }
            },
            {
              "yaraRuleSignature": {
                "yaraRule": "YARA_RULE25"
              }
            }
          ]
        },
        "kernelRootkit": {},
        "kubernetes": {},
        "mitreAttack": {
          "version": "9"
        },
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Virtual Machine Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "BINARY_PATH"
            },
            "script": {},
            "args": [
              "./miner",
              ""
            ],
            "pid": "123",
            "parentPid": "456",
            "name": "miner"
          }
        ],
        "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
        "severity": "HIGH",
        "sourceDisplayName": "Virtual Machine Threat Detection",
        "state": "ACTIVE",
        "vulnerability": {},
        "workflowState": "NEW"
      },
      "resource": {
        "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
        "display_name": "DISPLAY_NAME",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "project_display_name": "DISPLAY_NAME",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "parent_display_name": "DISPLAY_NAME",
        "type": "google.compute.Instance",
        "folders": []
      },
      "sourceProperties": {}
    }
        

### `Malware: Malicious file on disk (YARA)`
    
    
    {
      "findings": {
        "assetDisplayName": "DISPLAY_NAME",
        "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
        "canonicalName": "projects/PROJECT_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Malware: Malicious file on disk (YARA)",
        "createTime": "2023-01-05T00:37:38.450Z",
        "eventTime": "2023-01-05T01:12:48.828Z",
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/vmtd",
        "indicator": {
          "signatures": [
            {
              "yaraRuleSignature": {
                "yaraRule": "M_Backdoor_REDSONJA_4"
              },
              "signatureType": "SIGNATURE_TYPE_FILE",
            },
            {
              "yaraRuleSignature": {
                "yaraRule": "M_Backdoor_REDSONJA_3"
              },
              "signatureType": "SIGNATURE_TYPE_FILE",
            }
          ]
        },
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Virtual Machine Threat Detection",
        "files": [
          {
            "diskPath": {
              "partition_uuid": "b411dc99-f0a0-4c87-9e05-184977be8539",
              "relative_path": "RELATIVE_PATH"
            },
            "size": "21238",
            "sha256": "65d860160bdc9b98abf72407e14ca40b609417de7939897d3b58d55787aaef69",
            "hashedSize": "21238"
          }
        ],
        "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
        "severity": "HIGH",
        "sourceDisplayName": "Virtual Machine Threat Detection",
        "state": "ACTIVE",
        "vulnerability": {},
        "workflowState": "NEW"
      },
      "resource": {
        "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID",
        "display_name": "DISPLAY_NAME",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "project_display_name": "DISPLAY_NAME",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "parent_display_name": "DISPLAY_NAME",
        "type": "google.compute.Instance",
        "folders": []
      },
      "sourceProperties": {}
    }
        

## Change the state of findings

When you resolve threats identified by VM Threat Detection, the service does not automatically set a finding's state to **Inactive** in subsequent scans. Due to the nature of our threat domain, VM Threat Detection can't determine if a threat is mitigated or has changed to avoid detection.

When your security teams are satisfied that a threat is mitigated, they can perform the following steps to change the state of findings to inactive.

  1. Go to Security Command Center's **Findings** page in the Google Cloud console.

[Go to Findings](https://console.cloud.google.com/security/command-center/findings)

  2. Next to **View by** , click **Source Type**.

  3. In the **Source type** list, select **Virtual Machine Threat Detection**. A table populates with findings for the source type you selected.

  4. Select the checkbox next to the findings that are resolved.

  5. Click **Change Active State**.

  6. Click **Inactive**.




## Enable or disable VM Threat Detection for Google Cloud

This section describes how to enable or disable VM Threat Detection for Compute Engine VMs. To enable VM Threat Detection for AWS VMs, see [Enable VM Threat Detection for AWS](https://docs.cloud.google.com/security-command-center/docs/enable-vmtd-aws) instead.

VM Threat Detection is enabled by default for all customers that enroll in Security Command Center Premium after July 15, 2022, which is when this service became generally available. If needed, you can disable or re-enable it manually for your project or organization.

When you enable VM Threat Detection on an organization or project, the service automatically scans all [supported resources](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#supported_assets) in that organization or project. Conversely, when you disable VM Threat Detection on an organization or project, the service stops scanning all supported resources in it.

To enable or disable VM Threat Detection, do the following:

### Console

  1. In the Google Cloud console, go to the **Virtual Machine Threat Detection Service Enablement** page.

[Go to Service Enablement](https://console.cloud.google.com/projectselector2/security/command-center/config/services/vm-threat-detection/enablement?supportedpurview=project,folder,organizationId)

  2. Select your organization or project.

  3. On the **Service Enablement** tab, in the **Virtual Machine Threat Detection** column, select the enablement status of the organization, folder, or project that you want to modify, and then select one of the following:

     * **Enable** : enable VM Threat Detection
     * **Disable** : disable VM Threat Detection
     * **Inherit** : inherit the enablement status from the parent folder or organization; available only for projects and folders



### gcloud

The [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command updates the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organization`, `folder`, or `project`) 
  * `RESOURCE_ID`: the numeric identifier of the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `NEW_STATE`: `ENABLED` to enable VM Threat Detection; `DISABLED` to disable VM Threat Detection; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



Execute the [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services update vm-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID \
        --enablement-state=NEW_STATE

#### Windows (PowerShell)
    
    
    gcloud scc manage services update vm-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID `
        --enablement-state=NEW_STATE

#### Windows (cmd.exe)
    
    
    gcloud scc manage services update vm-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --enablement-state=NEW_STATE

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    modules:
      CRYPTOMINING_HASH:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CRYPTOMINING_YARA:
        effectiveEnablementState: ENABLED
      KERNEL_INTEGRITY_TAMPERING:
        effectiveEnablementState: ENABLED
      KERNEL_MEMORY_TAMPERING:
        effectiveEnablementState: ENABLED
      MALWARE_DISK_SCAN_YARA:
        effectiveEnablementState: ENABLED
    name: projects/1234567890123/locations/global/securityCenterServices/vm-threat-detection
    updateTime: '2024-08-05T22:32:01.536452397Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method updates the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier of the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `NEW_STATE`: `ENABLED` to enable VM Threat Detection; `DISABLED` to disable VM Threat Detection; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection?updateMask=intendedEnablementState

Request JSON body: 
    
    
    {
      "intendedEnablementState": "NEW_STATE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection?updateMask=intendedEnablementState"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection?updateMask=intendedEnablementState" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/1234567890123/locations/global/securityCenterServices/vm-threat-detection",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "CRYPTOMINING_YARA": {
          "effectiveEnablementState": "ENABLED"
        },
        "KERNEL_MEMORY_TAMPERING": {
          "effectiveEnablementState": "ENABLED"
        },
        "KERNEL_INTEGRITY_TAMPERING": {
          "effectiveEnablementState": "ENABLED"
        },
        "CRYPTOMINING_HASH": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "MALWARE_DISK_SCAN_YARA": {
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2024-08-05T22:32:01.536452397Z"
    }
    

## Enable or disable a VM Threat Detection module

To enable or disable an individual VM Threat Detection detector, also known as a _module_ , do the following. It can take up to an hour for your changes to take effect.

When you disable a service, all of its modules become inactive, even if the modules are individually enabled.

For information about all VM Threat Detection threat findings and the modules that generate them, see [Threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#threat_detection).

### Console

The Google Cloud console lets you enable or disable VM Threat Detection modules at the organization level. To enable or disable VM Threat Detection modules at the folder or project level, use the gcloud CLI or the REST API.

  1. In the Google Cloud console, go to the **Virtual Machine Threat Detection Modules** page.

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/vm-threat-detection/modules?supportedpurview=organizationId)

  2. Click the tab for the cloud provider that you want to enable or disable modules for—for example, **Google Cloud**.

  3. On the **Modules** tab, in the **Status** column, select the current status of the module that you want to enable or disable, and then select one of the following:

     * **Enable** : Enable the module.
     * **Disable** : Disable the module.



### gcloud

The [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command updates the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organization`, `folder`, or `project`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#threat_detection). 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



Save the following content in a file called `request.json`: 
    
    
    {
      "MODULE_NAME": {
        "intendedEnablementState": "NEW_STATE"
      }
    }

Execute the [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services update vm-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID \
        --module-config-file=request.json

#### Windows (PowerShell)
    
    
    gcloud scc manage services update vm-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID `
        --module-config-file=request.json

#### Windows (cmd.exe)
    
    
    gcloud scc manage services update vm-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --module-config-file=request.json

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    modules:
      CRYPTOMINING_HASH:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CRYPTOMINING_YARA:
        effectiveEnablementState: ENABLED
      KERNEL_INTEGRITY_TAMPERING:
        effectiveEnablementState: ENABLED
      KERNEL_MEMORY_TAMPERING:
        effectiveEnablementState: ENABLED
      MALWARE_DISK_SCAN_YARA:
        effectiveEnablementState: ENABLED
    name: projects/1234567890123/locations/global/securityCenterServices/vm-threat-detection
    updateTime: '2024-08-05T22:32:01.536452397Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method updates the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#threat_detection). 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection?updateMask=modules

Request JSON body: 
    
    
    {
      "modules": {
        "MODULE_NAME": {
          "intendedEnablementState": "NEW_STATE"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection?updateMask=modules"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection?updateMask=modules" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/1234567890123/locations/global/securityCenterServices/vm-threat-detection",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "CRYPTOMINING_YARA": {
          "effectiveEnablementState": "ENABLED"
        },
        "KERNEL_MEMORY_TAMPERING": {
          "effectiveEnablementState": "ENABLED"
        },
        "KERNEL_INTEGRITY_TAMPERING": {
          "effectiveEnablementState": "ENABLED"
        },
        "CRYPTOMINING_HASH": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "MALWARE_DISK_SCAN_YARA": {
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2024-08-05T22:32:01.536452397Z"
    }
    

## View the settings of the VM Threat Detection modules

For information about all VM Threat Detection threat findings and the modules that generate them, see the [Threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#threat_detection) table.

### Console

The Google Cloud console lets you view settings for VM Threat Detection modules at the organization level. To view settings for VM Threat Detection modules at the folder or project level, use the gcloud CLI or the REST API.

To view the settings in the Google Cloud console, go to the **Virtual Machine Threat Detection Modules** page.

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/vm-threat-detection/modules?supportedpurview=organizationId)

### gcloud

The [`gcloud scc manage services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe) command gets the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organization`, `folder`, or `project`) 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



Execute the [`gcloud scc manage services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services describe vm-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud scc manage services describe vm-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud scc manage services describe vm-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    modules:
      CRYPTOMINING_HASH:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CRYPTOMINING_YARA:
        effectiveEnablementState: ENABLED
      KERNEL_INTEGRITY_TAMPERING:
        effectiveEnablementState: ENABLED
      KERNEL_MEMORY_TAMPERING:
        effectiveEnablementState: ENABLED
      MALWARE_DISK_SCAN_YARA:
        effectiveEnablementState: ENABLED
    name: projects/1234567890123/locations/global/securityCenterServices/vm-threat-detection
    updateTime: '2024-08-05T22:32:01.536452397Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.get](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method gets the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



HTTP method and URL: 
    
    
    GET https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/1234567890123/locations/global/securityCenterServices/vm-threat-detection",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "CRYPTOMINING_YARA": {
          "effectiveEnablementState": "ENABLED"
        },
        "KERNEL_MEMORY_TAMPERING": {
          "effectiveEnablementState": "ENABLED"
        },
        "KERNEL_INTEGRITY_TAMPERING": {
          "effectiveEnablementState": "ENABLED"
        },
        "CRYPTOMINING_HASH": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "MALWARE_DISK_SCAN_YARA": {
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2024-08-05T22:32:01.536452397Z"
    }
    

## Software names and YARA rules for cryptocurrency mining detection

The following lists include the names of binaries and YARA rules that trigger cryptocurrency mining findings. To see the lists, expand the nodes.

#### `Execution: Cryptocurrency Mining Hash Match`

  * **Arionum CPU miner** : mining software for [Arionum](https://www.arionum.com/) cryptocurrency 
  * **Avermore** : mining software for scrypt-based cryptocurrencies 
  * **Beam CUDA miner** : mining software for Equihash-based cryptocurrencies 
  * **Beam OpenCL miner** : mining software for Equihash-based cryptocurrencies 
  * **BFGMiner** : ASIC/FPGA-based mining software for Bitcoin
  * **BMiner** : mining software for various cryptocurrencies
  * **Cast XMR** : mining software for [ CryptoNight](https://monerodocs.org/proof-of-work/cryptonight/)-based cryptocurrencies 
  * **ccminer** : CUDA-based mining software
  * **cgminer** : ASIC/FPGA-based mining software for Bitcoin
  * **Claymore's miner** : GPU-based mining software for various cryptocurrencies 
  * **CPUMiner** : family of CPU-based mining software
  * **CryptoDredge** : family of mining software for [CryptoDredge](https://cryptodredge.org/)
  * **CryptoGoblin** : mining software for [ CryptoNight](https://monerodocs.org/proof-of-work/cryptonight/)-based cryptocurrencies 
  * **DamoMiner** : GPU-based mining software for [Ethereum](https://ethereum.org/en/) and other cryptocurrencies 
  * **DigitsMiner** : mining software for Digits 
  * **EasyMiner** : mining software for Bitcoin and other cryptocurrencies 
  * **Ethminer** : mining software for [Ethereum](https://ethereum.org/en/) and other cryptocurrencies 
  * **EWBF** : mining software for Equihash-based cryptocurrencies
  * **FinMiner** : mining software for Ethash and [ CryptoNight](https://monerodocs.org/proof-of-work/cryptonight/)-based cryptocurrencies 
  * **Funakoshi Miner** : mining software for [Bitcoin-Gold](https://bitcoingold.org/) cryptocurrencies 
  * **Geth** : mining software for [Ethereum](https://ethereum.org/en/)
  * **GMiner** : mining software for various cryptocurrencies
  * **gominer** : mining software for [Decred](https://decred.org/)
  * **GrinGoldMiner** : mining software for [Grin](https://grin.mw/)
  * **Hush** : mining software for [Zcash](https://z.cash/)-based cryptocurrencies 
  * **IxiMiner** : mining software for [Ixian](https://www.ixian.io/)
  * **kawpowminer** : mining software for [Ravencoin](https://ravencoin.org/)
  * **Komodo** : family of mining software for Komodo
  * **lolMiner** : mining software for various cryptocurrencies
  * **lukMiner** : mining software for various cryptocurrencies
  * **MinerGate** : mining software for various cryptocurrencies
  * **miniZ** : mining software for Equihash-based cryptocurrencies
  * **Mirai** : malware that can be used to mine cryptocurrencies
  * **MultiMiner** : mining software for various cryptocurrencies
  * **nanominer** : mining software for various cryptocurrencies
  * **NBMiner** : mining software for various cryptocurrencies
  * **Nevermore** : mining software for various cryptocurrencies
  * **nheqminer** : mining software for [NiceHash](https://www.nicehash.com/)
  * **NinjaRig** : mining software for Argon2-based cryptocurrencies 
  * **NodeCore PoW CUDA Miner** : mining software for [VeriBlock](https://veriblock.org/)
  * **NoncerPro** : mining software for [Nimiq](https://www.nimiq.com/)
  * **Optiminer/Equihash** : mining software for Equihash-based cryptocurrencies
  * **PascalCoin** : family of mining software for PascalCoin 
  * **PhoenixMiner** : mining software for [Ethereum](https://ethereum.org/en/)
  * **Pooler CPU Miner** : mining software for [Litecoin](https://litecoin.org/) and Bitcoin 
  * **ProgPoW Miner** : mining software for [Ethereum](https://ethereum.org/en/) and other cryptocurrencies 
  * **rhminer** : mining software for [PascalCoin](https://www.pascalcoin.org/)
  * **sgminer** : mining software for scrypt-based cryptocurrencies 
  * **simplecoin** : family of mining software for scrypt-based SimpleCoin 
  * **Skypool Nimiq Miner** : mining software for [Nimiq](https://www.nimiq.com/)
  * **SwapReferenceMiner** : mining software for [Grin](https://grin.mw/)
  * **Team Red Miner** : AMD-based mining software for various cryptocurrencies 
  * **T-Rex** : mining software for various cryptocurrencies
  * **TT-Miner** : mining software for various cryptocurrencies
  * **Ubqminer** : mining software for Ubqhash-based cryptocurrencies 
  * **VersusCoin** : mining software for VersusCoin
  * **violetminer** : mining software for Argon2-based cryptocurrencies 
  * **webchain-miner** : mining software for [MintMe](https://www.mintme.com/coin/)
  * **WildRig** : mining software for various cryptocurrencies
  * **XCASH_ALL_Miner** : mining software for [XCASH](https://www.xcash.foundation/)
  * **xFash** : mining software for MinerGate
  * **XLArig** : mining software for [ CryptoNight](https://monerodocs.org/proof-of-work/cryptonight/)-based cryptocurrencies 
  * **XMRig** : mining software for various cryptocurrencies
  * **Xmr-Stak** : mining software for [ CryptoNight](https://monerodocs.org/proof-of-work/cryptonight/)-based cryptocurrencies 
  * **XMR-Stak TurtleCoin** : mining software for [ CryptoNight](https://monerodocs.org/proof-of-work/cryptonight/)-based cryptocurrencies 
  * **Xtl-Stak** : mining software for [ CryptoNight](https://monerodocs.org/proof-of-work/cryptonight/)-based cryptocurrencies 
  * **Yam Miner** : mining software for MinerGate
  * **YCash** : mining software for YCash
  * **ZCoin** : mining software for ZCoin/Fire
  * **Zealot/Enemy** : mining software for various cryptocurrencies
  * **Cryptocurrency miner signal** 1



1 This generic threat name indicates that an unknown cryptocurrency miner might be operating in the VM, but VM Threat Detection does not have specific information about the miner. 

#### `Execution: Cryptocurrency Mining YARA Rule`

  * **YARA_RULE1** : matches mining software for [Monero](https://www.getmonero.org/)
  * **YARA_RULE9** : matches mining software that uses the [Blake2](https://www.blake2.net/) and AES cipher 
  * **YARA_RULE10** : matches mining software that uses the [ CryptoNight](https://monerodocs.org/proof-of-work/cryptonight/) proof-of-work routine 
  * **YARA_RULE15** : matches mining software for [NBMiner](https://nbminer.com)
  * **YARA_RULE17** : matches mining software that uses the [Scrypt](https://en.wikipedia.org/wiki/Scrypt) proof-of-work routine 
  * **YARA_RULE18** : matches mining software that uses the [Scrypt](https://en.wikipedia.org/wiki/Scrypt) proof-of-work routine 
  * **YARA_RULE19** : matches mining software for [BFGMiner](https://github.com/luke-jr/bfgminer)
  * **YARA_RULE24** : matches mining software for [XMR-Stak](https://github.com/fireice-uk/xmr-stak)
  * **YARA_RULE25** : matches mining software for [XMRig](https://xmrig.com)
  * **DYNAMIC_YARA_RULE_BFGMINER_2** : matches mining software for [BFGMiner](https://github.com/luke-jr/bfgminer)



## What's next

  * Learn more about [VM Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview).
  * Learn how to [allow VM Threat Detection to scan VMs in VPC Service Controls perimeters](https://docs.cloud.google.com/security-command-center/docs/vmtd-allow-access-vpcsc).
  * Learn how to [enable VM Threat Detection for AWS](https://docs.cloud.google.com/security-command-center/docs/enable-vmtd-aws).
  * Learn how to [respond to Compute Engine threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-compute-engine-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
