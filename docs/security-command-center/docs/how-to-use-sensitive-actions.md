---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-use-sensitive-actions/
title: Use Sensitive Actions Service \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:14.641642+00:00
---

# Use Sensitive Actions Service  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-use-sensitive-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Sensitive Actions Service Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page shows you how to review Sensitive Actions Service findings in the Google Cloud console and includes examples of Sensitive Actions Service findings.

Sensitive Actions Service is a built-in service of Security Command Center that detects when actions are taken in your Google Cloud organization, folders, and projects that could be damaging to your business if they are taken by a malicious actor. To learn more, see [Sensitive Actions Service overview](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview).

## Reviewing Sensitive Actions Service findings

Sensitive Actions Service is always enabled when you activate Security Command Center and cannot be disabled. For more information about Sensitive Actions Service finding types, see [Findings](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview#findings).

When Sensitive Actions Service detects an action that is considered sensitive, it creates a finding and a log entry. You can view the finding in the Google Cloud console. You can query the log entries in Cloud Logging. To test Sensitive Actions Service, perform a sensitive action and make sure the finding appears on the **Findings** page in the Google Cloud console. For more information, see [Testing Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/how-to-test-sensitive-actions).

### Reviewing findings in Security Command Center

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

To review Sensitive Actions Service findings in the console, follow these steps:

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for your organization, you must access the page using the jurisdictional console. For more information, see [Use the console with data residency enabled](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#console-jconsole).

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Sensitive Actions Service**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



### View the findings caused by the same actor

When investigating whether a sensitive action was taken by a malicious actor, consider searching for other findings caused by that actor.

To view all findings caused by the same actor, follow these steps:

  1. Open the finding and view its details.
  2. On the finding details pane, copy the email address next to **Principal email**.
  3. Close the pane.
  4. In the query editor, enter the following query:
         
         access.principal_email="PRINCIPAL_EMAIL"
         

Replace PRINCIPAL_EMAIL with the email address that you previously copied. Security Command Center displays all findings that are associated with actions taken by the actor that you specified.




### Viewing findings in Cloud Logging

Sensitive Actions Service writes a log entry to the [Google Cloud platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs#sensitive_actions_service) for each sensitive action that the service finds. These log entries are written even if you have not enabled Security Command Center.

To view the log entries for sensitive actions in Cloud Logging, do the following:

  1. Go to **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Project selector** at the top of the page, select the project for which you would like to see the Sensitive Actions Service log entries. Alternatively, to see log entries at the organization level, select the organization.

  3. In the **Query** text box, enter the following resource definition: `resource.type="sensitiveaction.googleapis.com/Location"`

  4. Click **Run Query**. The **Query results** table is updated with any matching log entries that were written within the time period of your query.

  5. To view the details of a log entry, click a table row, then click **Expand nested fields**.




You can create [advanced log queries](https://docs.cloud.google.com/logging/docs/view/advanced-queries) to specify a set of log entries from any number of logs.

## Example Finding Formats

This section includes the JSON output for the Sensitive Actions Service findings as they appear when you create exports from the Google Cloud console or run list methods in the Security Command Center API.

The output examples contain the fields most common to all findings. However, all fields might not appear in every finding. The actual output you see depends on a resource's configuration and the type and state of findings.

To see example findings, expand one or more of the following nodes.

#### Defense Evasion: Organization Policy Changed

This finding isn't available for project-level activations.
    
    
          {
            "findings": {
              "access": {
                "principalEmail": "PRINCIPAL_EMAIL",
                "callerIp": "PRINCIPAL_IP_ADDRESS",
                "callerIpGeo": {
                  "regionCode": "US"
                },
                "serviceName": "orgpolicy.googleapis.com",
                "methodName": "google.cloud.orgpolicy.v2.OrgPolicy.CreatePolicy",
                "principalSubject": "user:PRINCIPAL_EMAIL"
              },
              "canonicalName": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
              "category": "Defense Evasion: Organization Policy Changed",
              "contacts": {
                "technical": {
                  "contacts": [
                    {
                      "email": "EMAIL_ADDRESS_1"
                    },
                    {
                      "email": "EMAIL_ADDRESS_2"
                    },
                  ]
                }
              },
              "createTime": "2022-08-27T12:35:30.466Z",
              "database": {},
              "eventTime": "2022-08-27T12:35:30.264Z",
              "exfiltration": {},
              "findingClass": "OBSERVATION",
              "indicator": {},
              "kubernetes": {},
              "mitreAttack": {
                "primaryTactic": "DEFENSE_EVASION",
                "primaryTechniques": [
                  "IMPAIR_DEFENSES"
                ]
              },
              "mute": "UNDEFINED",
              "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
              "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
              "parentDisplayName": "Sensitive Actions",
              "resourceName": "//orgpolicy.googleapis.com/organizations/ORGANIZATION_ID/policies/storage.publicAccessPrevention",
              "severity": "LOW",
              "sourceDisplayName": "Sensitive Actions Service",
              "state": "ACTIVE",
              "vulnerability": {},
              "workflowState": "NEW"
            },
            "resource": {
              "name": "//orgpolicy.googleapis.com/organizations/ORGANIZATION_ID/policies/storage.publicAccessPrevention",
              "display_name": "",
              "project_name": "",
              "project_display_name": "",
              "parent_name": "",
              "parent_display_name": "",
              "type": "",
              "folders": []
            },
            "sourceProperties": {
              "sourceId": {
                "organizationNumber": "ORGANIZATION_ID",
                "customerOrganizationNumber": "ORGANIZATION_ID"
              },
              "detectionCategory": {
                "ruleName": "sensitive_action",
                "subRuleName": "change_organization_policy"
              },
              "detectionPriority": "LOW",
              "affectedResources": [
                {
                  "gcpResourceName": "//orgpolicy.googleapis.com/organizations/ORGANIZATION_ID"
                },
                {
                  "gcpResourceName": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID"
                },
                {
                  "gcpResourceName": "//orgpolicy.googleapis.com/organizations/ORGANIZATION_ID/policies/storage.publicAccessPrevention"
                }
              ],
              "evidence": [
                {
                  "sourceLogId": {
                    "resourceContainer": "organizations/ORGANIZATION_ID",
                    "timestamp": {
                      "seconds": "1661603725",
                      "nanos": 12242032
                    },
                    "insertId": "INSERT_ID"
                  }
                }
              ],
              "properties": {},
              "findingId": "FINDING_ID",
              "contextUris": {
                "mitreUri": {
                  "displayName": "MITRE Link",
                  "url": "https://attack.mitre.org/techniques/T1562/"
                },
                "cloudLoggingQueryUri": [
                  {
                    "displayName": "Cloud Logging Query Link",
                    "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222022-08-27T12:35:25.012242032Z%22%0AinsertId%3D%22INSERT_ID%22%0Aresource.labels.project_id%3D%22%22?project="
                  }
                ],
                "relatedFindingUri": {}
              }
            }
          }
        

#### Defense Evasion: Remove Billing Admin

This finding isn't available for project-level activations.
    
    
          {
            "findings": {
              "access": {
                "principalEmail": "PRINCIPAL_EMAIL",
                "callerIp": "PRINCIPAL_IP_ADDRESS",
                "callerIpGeo": {},
                "serviceName": "cloudresourcemanager.googleapis.com",
                "methodName": "SetIamPolicy",
                "principalSubject": "user:PRINCIPAL_EMAIL"
              },
              "assetDisplayName": "organizations/ORGANIZATION_ID",
              "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
              "canonicalName": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
              "category": "Defense Evasion: Remove Billing Admin",
              "contacts": {
                "technical": {
                  "contacts": [
                    {
                      "email": "EMAIL_ADDRESS_1"
                    },
                    {
                      "email": "EMAIL_ADDRESS_2"
                    },
                  ]
                }
              },
              "createTime": "2022-08-31T14:47:11.752Z",
              "database": {},
              "eventTime": "2022-08-31T14:47:11.256Z",
              "exfiltration": {},
              "findingClass": "OBSERVATION",
              "iamBindings": [
                {
                  "action": "REMOVE",
                  "role": "roles/billing.admin",
                  "member": "user:PRINCIPAL_ACCOUNT_CHANGED"
                }
              ],
              "indicator": {},
              "kubernetes": {},
              "mitreAttack": {
                "primaryTactic": "DEFENSE_EVASION",
                "primaryTechniques": [
                  "MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE"
                ]
              },
              "mute": "UNDEFINED",
              "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
              "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
              "parentDisplayName": "Sensitive Actions Service",
              "resourceName": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID",
              "severity": "LOW",
              "sourceDisplayName": "Sensitive Actions Service",
              "state": "ACTIVE",
              "vulnerability": {},
              "workflowState": "NEW"
            },
            "resource": {
              "name": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID",
              "display_name": "ORGANIZATION_NAME",
              "project_name": "",
              "project_display_name": "",
              "parent_name": "",
              "parent_display_name": "",
              "type": "google.cloud.resourcemanager.Organization",
              "folders": []
            },
            "sourceProperties": {
              "sourceId": {
                "organizationNumber": "ORGANIZATION_ID",
                "customerOrganizationNumber": "ORGANIZATION_ID"
              },
              "detectionCategory": {
                "ruleName": "sensitive_action",
                "subRuleName": "remove_billing_admin"
              },
              "detectionPriority": "LOW",
              "affectedResources": [
                {
                  "gcpResourceName": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID"
                }
              ],
              "evidence": [
                {
                  "sourceLogId": {
                    "resourceContainer": "organizations/ORGANIZATION_ID",
                    "timestamp": {
                      "seconds": "1661957226",
                      "nanos": 356329000
                    },
                    "insertId": "INSERT_ID"
                  }
                }
              ],
              "properties": {},
              "findingId": "FINDING_ID",
              "contextUris": {
                "mitreUri": {
                  "displayName": "MITRE Link",
                  "url": "https://attack.mitre.org/techniques/T1578/"
                },
                "cloudLoggingQueryUri": [
                  {
                    "displayName": "Cloud Logging Query Link",
                    "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222022-08-31T14:47:06.356329Z%22%0AinsertId%3D%22INSERT_ID%22%0Aresource.labels.project_id%3D%22%22?project="
                  }
                ],
                "relatedFindingUri": {}
              }
            }
          }
        

#### Impact: GPU Instance Created
    
    
          {
            "findings": {
              "access": {
                "principalEmail": "PRINCIPAL_EMAIL",
                "callerIp": "PRINCIPAL_IP_ADDRESS",
                "callerIpGeo": {
                  "regionCode": "US"
                },
                "serviceName": "compute.googleapis.com",
                "methodName": "beta.compute.instances.insert"
              },
              "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
              "category": "Impact: GPU Instance Created",
              "contacts": {
                "technical": {
                  "contacts": [
                    {
                      "email": "EMAIL_ADDRESS_1"
                    },
                    {
                      "email": "EMAIL_ADDRESS_2"
                    },
                  ]
                }
              },
              "createTime": "2022-08-11T19:13:11.134Z",
              "database": {},
              "eventTime": "2022-08-11T19:13:09.885Z",
              "exfiltration": {},
              "findingClass": "OBSERVATION",
              "indicator": {},
              "kubernetes": {},
              "mitreAttack": {
                "primaryTactic": "IMPACT",
                "primaryTechniques": [
                  "RESOURCE_HIJACKING"
                ]
              },
              "mute": "UNDEFINED",
              "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
              "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
              "parentDisplayName": "Sensitive Actions",
              "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/VM_INSTANCE_NAME",
              "severity": "LOW",
              "sourceDisplayName": "Sensitive Actions Service",
              "state": "ACTIVE",
              "vulnerability": {},
              "workflowState": "NEW"
            },
            "resource": {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/VM_INSTANCE_NAME",
              "display_name": "VM_INSTANCE_NAME",
              "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
              "project_display_name": "PROJECT_ID",
              "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
              "parent_display_name": "PROJECT_ID",
              "type": "google.compute.Instance",
              "folders": [
                {
                  "resourceFolderDisplayName": "FOLDER_NAME",
                  "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER"
                }
              ]
            },
            "sourceProperties": {
              "sourceId": {
                "projectNumber": "PROJECT_NUMBER",
                "customerOrganizationNumber": "ORGANIZATION_ID"
              },
              "detectionCategory": {
                "ruleName": "sensitive_action",
                "subRuleName": "gpu_instance_created"
              },
              "detectionPriority": "LOW",
              "affectedResources": [
                {
                  "gcpResourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/VM_INSTANCE_NAME"
                },
                {
                  "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
                }
              ],
              "evidence": [
                {
                  "sourceLogId": {
                    "projectId": "PROJECT_ID",
                    "resourceContainer": "projects/PROJECT_ID",
                    "timestamp": {
                      "seconds": "1660245184",
                      "nanos": 578768000
                    },
                    "insertId": "INSERT_ID"
                  }
                }
              ],
              "properties": {},
              "findingId": "FINDING_ID",
              "contextUris": {
                "mitreUri": {
                  "displayName": "MITRE Link",
                  "url": "https://attack.mitre.org/techniques/T1496/"
                },
                "cloudLoggingQueryUri": [
                  {
                    "displayName": "Cloud Logging Query Link",
                    "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222022-08-11T19:13:04.578768Z%22%0AinsertId%3D%22INSERT_ID%22%0Aresource.labels.project_id%3D%22PROJECT_ID%22?project=PROJECT_ID"
                  }
                ],
                "relatedFindingUri": {}
              }
            }
          }
        

#### Impact: Many Instances Created
    
    
        {
          "findings": {
            "access": {
              "principalEmail": "PRINCIPAL_EMAIL",
              "callerIpGeo": {},
              "serviceName": "compute.googleapis.com",
              "methodName": "v1.compute.instances.insert",
              "principalSubject": "user:USER_EMAIL"
            },
            "canonicalName": "projects/PROJECT_NUMBER/sources/SENSITIVE_ACTIONS_INSTANCE_NUMBER/findings/FINDING_ID",
            "category": "Impact: Many Instances Created",
            "contacts": {
              "technical": {
                "contacts": [
                  {
                    "email": "EMAIL_ADDRESS_1"
                  },
                  {
                    "email": "EMAIL_ADDRESS_2"
                  },
                ]
              }
            },
            "createTime": "2022-08-22T21:18:18.112Z",
            "database": {},
            "eventTime": "2022-08-22T21:18:17.759Z",
            "exfiltration": {},
            "findingClass": "OBSERVATION",
            "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/sensitive_actions",
            "indicator": {},
            "kubernetes": {},
            "mitreAttack": {
              "primaryTactic": "IMPACT",
              "primaryTechniques": [
                "RESOURCE_HIJACKING"
              ]
            },
            "mute": "UNDEFINED",
            "name": "organizations/ORGANIZATION_ID/sources/SENSITIVE_ACTIONS_INSTANCE_NUMBER/findings/FINDING_ID",
            "parent": "organizations/ORGANIZATION_ID/sources/SENSITIVE_ACTIONS_INSTANCE_NUMBER",
            "parentDisplayName": "Sensitive Actions",
            "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/VM_INSTANCE_NAME",
            "severity": "LOW",
            "sourceDisplayName": "Sensitive Actions",
            "state": "ACTIVE",
            "vulnerability": {},
            "workflowState": "NEW"
          },
          "resource": {
            "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/VM_INSTANCE_NAME",
            "display_name": "",
            "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "project_display_name": "PROJECT_ID",
            "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "parent_display_name": "PROJECT_ID",
            "type": "google.compute.Instance",
            "folders": [
              {
                "resourceFolderDisplayName": "FOLDER_NAME",
                "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER"
              }
            ]
          },
          "sourceProperties": {
            "sourceId": {
              "projectNumber": "PROJECT_NUMBER",
              "customerOrganizationNumber": "ORGANIZATION_ID"
            },
            "detectionCategory": {
              "ruleName": "sensitive_action",
              "subRuleName": "many_instances_created"
            },
            "detectionPriority": "LOW",
            "affectedResources": [
              {
                "gcpResourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/VM_INSTANCE_NAME"
              },
              {
                "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
              }
            ],
            "evidence": [
              {
                "sourceLogId": {
                  "projectId": "PROJECT_ID",
                  "resourceContainer": "projects/PROJECT_ID",
                  "timestamp": {
                    "seconds": "1661203092",
                    "nanos": 314642000
                  },
                  "insertId": "INSERT_ID"
                }
              }
            ],
            "properties": {},
            "findingId": "FINDING_ID",
            "contextUris": {
              "mitreUri": {
                "displayName": "MITRE Link",
                "url": "https://attack.mitre.org/techniques/T1496/"
              },
              "cloudLoggingQueryUri": [
                {
                  "displayName": "Cloud Logging Query Link",
                  "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222022-08-22T21:18:12.314642Z%22%0AinsertId%3D%22INSERT_ID%22%0Aresource.labels.project_id%3D%22PROJECT_ID%22?project=PROJECT_ID"
                }
              ],
              "relatedFindingUri": {}
            }
          }
        }
        

#### Impact: Many Instances Deleted
    
    
        {
          "findings": {
            "access": {
              "principalEmail": "PRINCIPAL_EMAIL",
              "callerIpGeo": {},
              "serviceName": "compute.googleapis.com",
              "methodName": "v1.compute.instances.delete",
              "principalSubject": "user:USER_EMAIL"
            },
            "canonicalName": "projects/PROJECT_NUMBER/sources/SENSITIVE_ACTIONS_INSTANCE_NUMBER/findings/FINDING_ID",
            "category": "Impact: Many Instances Deleted",
            "contacts": {
              "technical": {
                "contacts": [
                  {
                    "email": "EMAIL_ADDRESS_1"
                  },
                  {
                    "email": "EMAIL_ADDRESS_2"
                  },
                ]
              }
            },
            "createTime": "2022-08-22T21:21:11.432Z",
            "database": {},
            "eventTime": "2022-08-22T21:21:11.144Z",
            "exfiltration": {},
            "findingClass": "OBSERVATION",
            "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/sensitive_actions",
            "indicator": {},
            "kubernetes": {},
            "mitreAttack": {
              "primaryTactic": "IMPACT",
              "primaryTechniques": [
                "DATA_DESTRUCTION"
              ]
            },
            "mute": "UNDEFINED",
            "name": "organizations/ORGANIZATION_ID/sources/SENSITIVE_ACTIONS_INSTANCE_NUMBER/findings/FINDING_ID",
            "parent": "organizations/ORGANIZATION_ID/sources/SENSITIVE_ACTIONS_INSTANCE_NUMBER",
            "parentDisplayName": "Sensitive Actions",
            "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/VM_INSTANCE_NAME",
            "severity": "LOW",
            "sourceDisplayName": "Sensitive Actions",
            "state": "ACTIVE",
            "vulnerability": {},
            "workflowState": "NEW"
          },
          "resource": {
            "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/VM_INSTANCE_NAME",
            "display_name": "VM_INSTANCE_NAME",
            "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "project_display_name": "PROJECT_ID",
            "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "parent_display_name": "PROJECT_ID",
            "type": "google.compute.Instance",
            "folders": [
              {
                "resourceFolderDisplayName": "FOLDER_NAME",
                "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER"
              }
            ]
          },
          "sourceProperties": {
            "sourceId": {
              "projectNumber": "PROJECT_NUMBER",
              "customerOrganizationNumber": "ORGANIZATION_ID"
            },
            "detectionCategory": {
              "ruleName": "sensitive_action",
              "subRuleName": "many_instances_deleted"
            },
            "detectionPriority": "LOW",
            "affectedResources": [
              {
                "gcpResourceName": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/VM_INSTANCE_NAME"
              },
              {
                "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
              }
            ],
            "evidence": [
              {
                "sourceLogId": {
                  "projectId": "PROJECT_ID",
                  "resourceContainer": "projects/PROJECT_ID",
                  "timestamp": {
                    "seconds": "1661203265",
                    "nanos": 669160000
                  },
                  "insertId": "INSERT_ID"
                }
              }
            ],
            "properties": {},
            "findingId": "FINDING_ID",
            "contextUris": {
              "mitreUri": {
                "displayName": "MITRE Link",
                "url": "https://attack.mitre.org/techniques/T1485/"
              },
              "cloudLoggingQueryUri": [
                {
                  "displayName": "Cloud Logging Query Link",
                  "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222022-08-22T21:21:05.669160Z%22%0AinsertId%3D%22INSERT_ID%22%0Aresource.labels.project_id%3D%22PROJECT_ID%22?project=PROJECT_ID"
                }
              ],
              "relatedFindingUri": {}
            }
          }
        }
        

#### Persistence: Add Sensitive Role

This finding isn't available for project-level activations.
    
    
    {
          "findings": {
            "access": {
              "principalEmail": "PRINCIPAL_EMAIL",
              "callerIp": "PRINCIPAL_IP_ADDRESS",
              "callerIpGeo": {},
              "serviceName": "cloudresourcemanager.googleapis.com",
              "methodName": "SetIamPolicy",
              "principalSubject": "user:PRINCIPAL_EMAIL"
            },
            "assetDisplayName": "organizations/ORGANIZATION_ID",
            "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
            "canonicalName": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
            "category": "Persistence: Add Sensitive Role",
            "contacts": {
              "technical": {
                "contacts": [
                  {
                    "email": "EMAIL_ADDRESS_1"
                  },
                  {
                    "email": "EMAIL_ADDRESS_2"
                  },
                ]
              }
            },
            "createTime": "2022-08-31T17:20:13.305Z",
            "database": {},
            "eventTime": "2022-08-31T17:20:11.929Z",
            "exfiltration": {},
            "findingClass": "OBSERVATION",
            "iamBindings": [
              {
                "action": "ADD",
                "role": "roles/editor",
                "member": "user:PRINCIPAL_ACCOUNT_CHANGED"
              }
            ],
            "indicator": {},
            "kubernetes": {},
            "mitreAttack": {
              "primaryTactic": "PERSISTENCE",
              "primaryTechniques": [
                "ACCOUNT_MANIPULATION"
              ]
            },
            "mute": "UNDEFINED",
            "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
            "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
            "parentDisplayName": "Sensitive Actions Service",
            "resourceName": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID",
            "severity": "LOW",
            "sourceDisplayName": "Sensitive Actions Service",
            "state": "ACTIVE",
            "vulnerability": {},
            "workflowState": "NEW"
          },
          "resource": {
            "name": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID",
            "display_name": "ORGANIZATION_NAME",
            "project_name": "",
            "project_display_name": "",
            "parent_name": "",
            "parent_display_name": "",
            "type": "google.cloud.resourcemanager.Organization",
            "folders": []
          },
          "sourceProperties": {
            "sourceId": {
              "organizationNumber": "ORGANIZATION_ID",
              "customerOrganizationNumber": "ORGANIZATION_ID"
            },
            "detectionCategory": {
              "ruleName": "sensitive_action",
              "subRuleName": "add_sensitive_role"
            },
            "detectionPriority": "LOW",
            "affectedResources": [
              {
                "gcpResourceName": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID"
              }
            ],
            "evidence": [
              {
                "sourceLogId": {
                  "resourceContainer": "organizations/ORGANIZATION_ID",
                  "timestamp": {
                    "seconds": "1661966410",
                    "nanos": 132148000
                  },
                  "insertId": "INSERT_ID"
                }
              }
            ],
            "properties": {},
            "findingId": "FINDING_ID",
            "contextUris": {
              "mitreUri": {
                "displayName": "MITRE Link",
                "url": "https://attack.mitre.org/techniques/T1098/"
              },
              "cloudLoggingQueryUri": [
                {
                  "displayName": "Cloud Logging Query Link",
                  "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222022-08-31T17:20:10.132148Z%22%0AinsertId%3D%22INSERT_ID%22%0Aresource.labels.project_id%3D%22%22?project="
                }
              ],
              "relatedFindingUri": {}
            }
          }
        }
        

#### Persistence: Project SSH Key Added
    
    
        {
          "findings": {
            "access": {
              "principalEmail": "PRINCIPAL_EMAIL",
              "callerIp": "PRINCIPAL_IP_ADDRESS",
              "callerIpGeo": {
                "regionCode": "US"
              },
              "serviceName": "compute.googleapis.com",
              "methodName": "v1.compute.projects.setCommonInstanceMetadata",
              "principalSubject": "user:USER_EMAIL"
            },
            "canonicalName": "projects/PROJECT_NUMBER/sources/SENSITIVE_ACTIONS_INSTANCE_NUMBER/findings/FINDING_ID",
            "category": "Persistence: Project SSH Key Added",
            "contacts": {
              "technical": {
                "contacts": [
                  {
                    "email": "EMAIL_ADDRESS_1"
                  },
                  {
                    "email": "EMAIL_ADDRESS_2"
                  },
                ]
              }
            },
            "createTime": "2022-08-25T13:24:43.142Z",
            "database": {},
            "eventTime": "2022-08-25T13:24:42.719Z",
            "exfiltration": {},
            "findingClass": "OBSERVATION",
            "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/sensitive_actions",
            "indicator": {},
            "kubernetes": {},
            "mitreAttack": {
              "primaryTactic": "PERSISTENCE",
              "primaryTechniques": [
                "ACCOUNT_MANIPULATION",
                "SSH_AUTHORIZED_KEYS"
              ]
            },
            "mute": "UNDEFINED",
            "name": "organizations/ORGANIZATION_ID/sources/SENSITIVE_ACTIONS_INSTANCE_NUMBER/findings/FINDING_ID",
            "parent": "organizations/ORGANIZATION_ID/sources/SENSITIVE_ACTIONS_INSTANCE_NUMBER",
            "parentDisplayName": "Sensitive Actions",
            "resourceName": "//compute.googleapis.com/projects/PROJECT_ID",
            "severity": "LOW",
            "sourceDisplayName": "Sensitive Actions",
            "state": "ACTIVE",
            "vulnerability": {},
            "workflowState": "NEW"
          },
          "resource": {
            "name": "//compute.googleapis.com/projects/PROJECT_ID",
            "display_name": "PROJECT_ID",
            "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "project_display_name": "PROJECT_ID",
            "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "parent_display_name": "PROJECT_ID",
            "type": "google.compute.Project",
            "folders": [
              {
                "resourceFolderDisplayName": "FOLDER_NAME",
                "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER"
              }
            ]
          },
          "sourceProperties": {
            "sourceId": {
              "projectNumber": "PROJECT_NUMBER",
              "customerOrganizationNumber": "ORGANIZATION_ID"
            },
            "detectionCategory": {
              "ruleName": "sensitive_action",
              "subRuleName": "add_ssh_key"
            },
            "detectionPriority": "LOW",
            "affectedResources": [
              {
                "gcpResourceName": "//compute.googleapis.com/projects/PROJECT_ID"
              },
              {
                "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
              }
            ],
            "evidence": [
              {
                "sourceLogId": {
                  "projectId": "PROJECT_ID",
                  "resourceContainer": "projects/PROJECT_ID",
                  "timestamp": {
                    "seconds": "1661433879",
                    "nanos": 413362000
                  },
                  "insertId": "INSERT_ID"
                }
              }
            ],
            "properties": {},
            "findingId": "FINDING_ID",
            "contextUris": {
              "mitreUri": {
                "displayName": "MITRE Link",
                "url": "https://attack.mitre.org/techniques/T1098/004/"
              },
              "cloudLoggingQueryUri": [
                {
                  "displayName": "Cloud Logging Query Link",
                  "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222022-08-25T13:24:39.413362Z%22%0AinsertId%3D%22INSERT_ID%22%0Aresource.labels.project_id%3D%22PROJECT_ID%22?project=PROJECT_ID"
                }
              ],
              "relatedFindingUri": {}
            }
          }
        }
        

## What's next

  * Learn more about [how Sensitive Actions Service works](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview).
  * Learn how to [investigate and develop response plans](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats) for threats.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
