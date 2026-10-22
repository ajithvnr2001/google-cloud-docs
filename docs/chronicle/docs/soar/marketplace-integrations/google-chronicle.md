---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chronicle/
title: Integrate Google Chronicle with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:09.078914+00:00
---

# Integrate Google Chronicle with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chronicle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Google Chronicle with Google SecOps

**Caution:** The Backstory and Ingestion APIs are deprecated. Starting October 26, 2026 (EOS date), new instances won't be able to call legacy APIs, and End of Life (EOL) will take place on July 20, 2027. 

To prevent playbook disruptions, you must upgrade this integration to version 54 or higher.

* **Authentication** : You must set up authentication (JSON key or Workload Identity) identically across the integration configuration, connectors, and jobs.
* **Playbook Monitoring** : You must review your playbooks after upgrading, as action execution outputs may differ.

For details, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api) and Migrate Backstory API to Chronicle API.

This document explains how to integrate Google Chronicle with Google Security Operations.

**Important:** Google Chronicle was rebranded to Google SecOps. In the Google SecOps platform, the integration for Google SecOps is called _Google Chronicle_.

## Use cases

The **Google Chronicle** integration uses Google SecOps capabilities to support the following use cases:

  * **Automated phishing investigation and remediation:** Automatically query for historical email data, user activity logs, and threat intelligence to assess email legitimacy. The automated remediation can help you with triage and containment by preventing the spread of malware or data breaches.

  * **Enrichment of security alerts:** Enrich an alert generated in a SIEM with historical context, such as past user behavior and asset information. This provides analysts with a comprehensive view of an incident, enabling faster and more informed decision-making.

  * **Threat hunting based on Google SecOps insights:** Automate the process of querying other security tools for related indicators of compromise (IOCs). This can help you proactively identify potential breaches before they escalate.

  * **Automated incident response playbooks:** Trigger predefined playbooks that use Google SecOps data to isolate compromised systems, block malicious IP addresses, and notify relevant stakeholders. This can reduce incident response time and minimize the impact of security incidents.

  * **Compliance reporting and auditing:** Automate the collection of security data from Google SecOps for compliance reporting, streamlining the audit process, and reducing manual effort.




## Before you begin

Before you configure the Google Chronicle integration in Google SecOps, make sure you have access to an active Google Cloud project.

### Migration from Backstory API to Chronicle API

Some new features and actions in this integration only support the Chronicle API, so we strongly recommend that all users migrate their deployment to use the Chronicle API credentials.

**Important:** New deployments provisioned from the start of Q4 2025 are provisioned with the Chronicle API credentials configured in the system. 

The only requirement is to find the Chronicle API root and enter it into the integration configuration. This value can be found in your instance's connectors and job's `API Root` parameter.

If a connection test fails after entering the new API root, continue with the following steps.

#### Finding the Chronicle API Root

When accessing Chronicle API, you must locate your environment's unique `API Root` for the integration configuration.

  1. Open your browser's **Developer Tools** and navigate to the Google SecOps platform.

  2. Select **Investigation > Data Tables**.

  3. In Developer Tools, navigate to the **Network** tab and click an item in the Name column, such as `dataTables?pageSize=1000`.

  4. In the details pane, select **Headers** and copy the value of `Request URL`, found under **General** , excluding the endpoint and any query parameters (the name of the selected item).

For example, if the value is `https://{api_root}/v1alpha/projects/{project_id}/locations/{location}/instances/{customer_id}/dataTables?pageSize=1000`, the API root excludes `/dataTables?pageSize=1000` and is `https://{api_root}/v1alpha/projects/{project_id}/locations/{location}/instances/{customer_id}`.




#### Credentialing Requirements for Chronicle API

Access to the Chronicle API requires both a new API root and new credentials, which depend on how your underlying Google Cloud project is managed:

Project Type | Credential Requirement  
---|---  
Google-Managed Project (Default) | Contact Google Support to provision the necessary hidden credentials and grant permissions to your environment.  
Bring Your Own Project (BYOP) | You must manually configure a dedicated Service Account in your project using either a JSON Key or a Workload Identity, and assign the `Chronicle API Editor` role.  
  
### Authentication with a service account JSON key

Authentication using a service account JSON Key is supported for the Chronicle API and is mandatory for BYOP users who don't authenticate using a Workload Identity.

**Note:** Authentication can be done with either a JSON key or a Workload Identity. We recommend using a Workload Identity.

#### Create a dedicated service account and create your JSON key

For authentication with a service account JSON key, complete the following steps to create your JSON key:

  1. In the Google Cloud console, go to [**IAM & Admin > Service Accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts).

  2. Select **Create Service Account** and follow the prompts.

  3. Select the email address of the new Service Account and go to **Keys > Add Key > Create new key**.

  4. Select `JSON` as the key type and click **Create**. A JSON key file is downloaded to your computer.




#### Chronicle API: Role required for your service account

When using Chronicle API, your service account requires the `Chronicle API Editor` role.

  1. In the Google Cloud console, go to [**APIs and Services > Credentials**](https://console.cloud.google.com/apis/credentials).

  2. Under **Service Accounts** , select your service account and click **Permissions > Manage access**.

  3. Click add**Add role** and select the **`Chronicle API Editor`** role. Click **Save**.




### Authentication with a Workload Identity (recommended)

Authentication using a Workload Identity is the recommended and most secure method.

To set up authentication with a Workload Identity, follow these steps:

#### Create a service account

To create a service account, complete the following steps:

  1. In the Google Cloud console, go to the **Credentials** page.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. From the **Create credentials** menu, select **Service account**.

  3. Under **Service account details** , enter a name in the **Service account name** field.

  4. Optional: Edit the service account ID.

  5. Click **Create and continue**. A **Permissions** screen appears.

  6. Click **Continue**. A **Principals with access** screen appears.

  7. Click **Done**.




#### Chronicle API: Role required for your service account

When using Chronicle API, your service account requires the `Chronicle API Editor` role.

  1. In the Google Cloud console, go to [**APIs and Services > Credentials**](https://console.cloud.google.com/apis/credentials).

  2. Under **Service Accounts** , select your service account and click **Permissions > Manage access**.

  3. Click add**Add role** and select the **`Chronicle API Editor`** role. Click **Save**.




#### Grant impersonation permissions to your Google SecOps instance

To use a Workload Identity, you must grant your Google SecOps instance permission to impersonate your service account. This is the final step that allows the instance to securely access Google Cloud resources.

  1. In Google SecOps, go to **Content Hub > [Response Integrations](https://docs.cloud.google.com/marketplace/integrations)**.

  2. Select the integration you're configuring, and enter your service account email in `Workload Identity Email`.

  3. Click **Save > Test**. The test is expected to fail.

  4. Click close_small to the right of **Test** and search the error message for `gke-init-python@`PROJECT `.iam.gserviceaccount.com` or `soar-python@`TENANT_PROJECT `.iam.gserviceaccount.com`. Copy this unique email (it identifies your Google SecOps instance).

  5. Go to **[Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)** , select your project, and select your service account. 

  6. Select **Principals with access > addGrant access**.

  7. Under **Add principals** , paste the value you copied.

  8. Under **Add Roles** , select the **`Service Account Token Creator`** (`roles/iam.serviceAccountTokenCreator`) role.

**Note:** It may take a few minutes after completing this step for the test to pass.



### Troubleshoot connectivity to Chronicle API

If you encounter issues connecting your integration to the Chronicle API, follow these steps to troubleshoot the configuration and resolve credential issues:

  1. Find the Chronicle API root and ensure it is correctly entered into the integration configuration.
  2. Ensure all other mandatory configuration parameters are accurately filled.
  3. Test the connection. If the test succeeds, no further steps are needed. If the test fails, proceed to the next step.

  4. Verify Google Cloud project ownership and credentials:

     * **Google-Managed Project** : If your Google Cloud project is managed by Google (default deployment), contact Google Support for assistance with credential issues.
     * **Bring Your Own Project (BYOP)** : If your Google Cloud project is self-managed (BYOP), verify that you have manually configured a service account and assigned it the appropriate roles.



## Integration parameters

The **Google Chronicle** integration requires the following parameters:

Parameter | Description  
---|---  
`UI Root` | Required. The base URL of the Google SecOps interface. This is used to automatically generate direct links back to the SIEM platform from your case records. The default value is `https://INSTANCE.chronicle.security/`.  
`API Root` |  Required. The API root for your Google SecOps instance. The value depends on your authentication method:

  * For **Backstory API** (using default credentials): Use the legacy format. The default value is `https://backstory.googleapis.com`.
  * For **Chronicle API** (requires configured Service Account): Use the new format, including your project ID, region, and instance ID. For example, `https://us-chronicle.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/instances/INSTANCE_ID`. For information on how to find this value, go to Finding the Chronicle API Root. Using the wrong credentials for the API root results in a connection failure.

  
`User's Service Account` | Optional. The full content of the service account JSON key file. **Important:** To use the Chronicle API, you must provide either this field or `Workload Identity Email`. Do not populate this field if you intend to use `Workload Identity Email`, as providing both causes authentication conflicts. If both fields are empty, the integration defaults to the instance service account, which only supports the Backstory API.  
`Workload Identity Email` | Optional. The client email address of the service account used for Workload Identity impersonation. **Important:** Do not populate this field if `User's Service Account` is already provided. To prevent "Permission Denied" errors, grant the [ `Service Account Token Creator`](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) role to the Google SecOps instance service account on the email provided in this field.   
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Google SecOps server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Entry To Watchlist

Use the **Add Entry To Watchlist** action to add a specified entity to an existing Risk Analytics Watchlist in Google SecOps.

This action doesn't run on Google SecOps entities. 

**Note:** This action requires Chronicle API authentication. Legacy Backstory API authentication isn't supported.

#### Action inputs

The **Add Entry To Watchlist** action requires the following parameters:

Parameter | Description  
---|---  
`Watchlist Name` | Required. The name of the Risk Analytics watchlist to add the entry to.  
`Entry` | Required. The JSON object representing the entity to add to the watchlist. The JSON structure requires the entity value, entity type, and an optional namespace. The default value is:
    
    
       [
       {
        "entity": "",
        "type": "ASSET_IP_ADDRESS/MAC/HOSTNAME/PRODUCT_SPECIFIC_ID/USERNAME/EMAIL/EMPLOYEE_ID/WINDOWS_SID/PRODUCT_OBJECT_ID",
        "namespace": "Optional"
       }
       ]
         
  
#### Action outputs

The **Add Entry To Watchlist** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Add Entry To Watchlist** action:
    
    
    [
        {
            "namespace": "Yuriy",
            "asset": {
                "hostname": "koko"
            }
        },
        {
            "namespace": "Yuriy",
            "asset": {
                "hostname": "koko"
            }
        }
    ]
    

##### Output messages

The **Add Entry To Watchlist** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added new entries to a watchlist WATCHLIST in Google SecOps.` | The action succeeded.  
`Error executing action "Add Entry To Watchlist". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Entry To Watchlist** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Rows To Data Table

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **Add Rows To Data Table** action to add rows to a data table in Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

To configure the action, use the following parameters:

Parameter | Description  
---|---  
`Data Table Name` | Required. The display name of the data table to update.  
`Rows` | Required. A list of JSON objects containing information about the rows to add. For example:
    
    
      [
        {
            "columnName1": "value1",
            "columnName2": "value2",        
        },
        {
            "columnName1": "value1",
            "columnName2": "value2",        
        }
      ]
      
  
#### Action outputs

The **Add Rows To Data Table** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment  | Not available   
Case wall link  | Not available   
Case wall table  | Not available   
Enrichment table  | Not available   
Entity insight  | Not available   
JSON result  | Available   
Output messages | Available  
Script result  | Available   
  
##### JSON result

The following example shows a sample JSON result returned by the **Add Rows To Data Table** action:
    
    
    {
              "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/dataTables/data_table/dataTableRows/840d18a85944833e1b97ed6d2fb11377",
              "values": {
                  "columnName1": "asda",
                  "columnName2": "asdasd",
                  "columnName3": "zxczxc"
              }
    }
    

##### Output messages

The **Add Rows To Data Table** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added rows to the data table DATA_TABLE_NAME in Google SecOps.` | The action succeeded.   
`Error executing action "Add Rows to Data Table". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Add Rows To Data Table** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Values To Reference List

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **Add Values To Reference List** action to add values to a reference list in Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

To configure the action, use the following parameters:

Parameter | Description  
---|---  
`Reference List Name` | Required. The name of the reference list to update.  
`Values` | Required. A comma-separated list of values to add to the reference list.  
  
#### Action outputs

The **Add Value To Reference List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment  | Not available   
Case wall link  | Not available   
Case wall table  | Not available   
Enrichment table  | Not available   
Entity insight  | Not available   
JSON result  | Available   
Output messages  | Available   
Script result  | Available   
  
##### JSON result

The following example describes the JSON result output received when using the **Add Value To Reference List** action with Backstory API:
    
    
    {
       "name": "list_name",
       "description": "description of the list",
       "lines": [
           "192.0.2.0/24",
           "198.51.100.0/24"
       ],
       "create_time": "2020-11-20T17:18:20.409247Z",
       "content_type": "CIDR"
    }
    

The following example describes the JSON result output received when using the **Add Value To Reference List** action with Chronicle API:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us/instances/INSTANCE_ID/referenceLists/REFERENCE_LIST_NAME",
      "displayName": "REFERENCE_LIST_NAME",
      "revisionCreateTime": "2025-01-16T09:15:21.795743Z",
      "description": "Test reference list",
      "entries": [
        {
          "value": "example.com"
        },
        {
          "value": "exampledomain.com"
        }
      ],
      "syntaxType": "REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING",
      "scopeInfo": {
        "referenceListScope": {}
      },
      "createTime": "2025-01-16T09:15:21.795743Z",
      "lines": [
        "example.com",
        "exampledomain.com"
      ]
    }
    

##### Output messages

The **Add Values To Reference List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added values to the reference list REFERENCE_LIST_NAME.` | The action succeeded.   
`Error executing action "Add Values To Reference List". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Add Values To Reference List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ask Gemini

Use the **Ask Gemini** action to send a text prompt to Gemini in Google SecOps.

This action doesn't run on Google SecOps entities. 

**Note:** This action only works with Chronicle API authentication. Backstory API isn't supported. If you're using a Unified SecOps deployment, verify that you have configured a dedicated service account and provided credentials in the integration parameters.

#### Processing limits and timeouts

This action is subject to processing constraints within the Google SecOps pipeline. Actions that exceed these constraints typically result in a `503 Service Unavailable` error.

To ensure successful execution, your requests must adhere to the following specifications:

  * **Timeouts** : Intent recognition has a 30-second timeout. Large summarization tasks or complex prompts that exceed this processing time cause the action to fail.

  * **Response generation cap** : The generation phase is limited to a maximum of 28,000 tokens.




#### Action inputs

The **Ask Gemini** action requires the following parameters:

Parameter | Description  
---|---  
`Automatic Opt-in` | Optional. If selected, the playbook automatically opts in the user for the Gemini conversation without requiring a manual confirmation. Enabled by default.  
`Prompt` | Required. The initial text prompt or question to send to Gemini. **Important:** Prompts that require extensive processing (such as summarizing large result sets) can be subject to a 30-second timeout. For details, see Processing limits and timeouts.   
  
#### Action outputs

The **Ask Gemini** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment  | Not available   
Case wall link  | Not available   
Case wall table  | Not available   
Enrichment table  | Not available   
Entity insight  | Not available   
JSON result  | Available   
Output messages  | Available   
Script result  | Available   
  
##### JSON result

The following example describes the JSON result output received when using the **Ask Gemini** action:
    
    
    {
      {
            "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/users/me/conversations/db3b0fc2-94f8-42ae-b743-c3693f593269/messages/b58e3186-e697-4400-9da8-8ef252a20bd9",
            "input": {
                "body": "Is IP 159.138.84.217 malicious? What can you tell me about it?"
            },
            "responses": [
                {
                    "blocks": [
                        {
                            "blockType": "HTML",
                            "htmlContent": {
                                "privateDoNotAccessOrElseSafeHtmlWrappedValue": "<p>The IP address 159.138.84.217 is associated with malware and threat actors.</p>\n<ul>\n<li>It is an IPv4 indicator.</li>\n<li>It is associated with BEACON malware.</li>\n<li>It is categorized as malware-Backdoor.</li>\n<li>It has a low confidence, high severity threat rating.</li>\n<li>VirusTotal&#39;s IP Address Report indicates the network for this IP is 159.138.80.0/20, and the IP is associated with HUAWEI CLOUDS in Singapore.</li>\n<li>VirusTotal&#39;s last analysis on April 22, 2025, showed 8 malicious detections out of 94 sources.</li>\n</ul>\n<p>I might have more details for a question with more context (e.g., what is the source of the IP, what type of network traffic is associated with the IP).</p>\n"
                            }
                        }
                    ],
                    "references": [
                        {
                            "blockType": "HTML",
                            "htmlContent": {
                                "privateDoNotAccessOrElseSafeHtmlWrappedValue": "<ol>\n<li><a href=\"https://advantage.mandiant.com/indicator/ipv4/159.138.84.217\" target=\"_blank\">Mandiant - indicator - 159.138.84.217</a></li>\n</ol>\n"
                            }
                        }
                    ],
                    "groundings": [
                        "IP address 159.138.84.217 malicious cybersecurity",
                        "IP address 159.138.84.217 threat intelligence"
                    ]
                }
            ],
            "createTime": "2025-05-16T11:31:36.660538Z"
        }
    }
    

##### Output messages

The **Ask Gemini** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully executed a prompt in Google SecOps.` | The action succeeded.   
`Error executing action "GoogleChronicle - Ask Gemini". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Ask Gemini** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enrich Domain - Deprecated

**Deprecated:** This action is deprecated.

Use the **Enrich Domain** action to enrich domains using information from IoCs in Google SecOps.

This action runs on the following Google SecOps entities:

  * `URL`
  * `Hostname`



#### Action inputs

The **Enrich Domain** action requires the following parameters:

Parameter | Description  
---|---  
`Create Insight` | If selected, action will create an insight containing information about the entities.Enabled by default.  
`Only Suspicious Insight` | If selected, action will only create an insight for entities that are marked as suspicious.Not enabled by default. If you select this parameter, you must also select `Create Insight`.  
`Lowest Suspicious Severity` | Required. The lowest severity associated with the domain needed to flag it as suspicious.The default value is `Medium`. The possible values are as follows:

  * `High`
  * `Medium`
  * `Low`
  * `Info`

  
`Mark Suspicious N/A Severity` | Required. If selected and the information about severity is unavailable, the action marks the entity as suspicious.  
  
#### Action outputs

The **Enrich Domain** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Available  
Entity insight | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Enrich Domain** action provides the following table:

Name: ENTITY_IDENTIFIER

Columns:

  * **Source**
  * **Severity**
  * **Category**
  * **Confidence**



##### Entity enrichment

The **Enrich Domain** action supports the following entity enrichment logic:

Enrichment field | Logic (when to apply)  
---|---  
`severity` | When available in JSON  
`average_confidence` | When available in JSON  
`related_domains` | When available in JSON  
`categories` | When available in JSON  
`sources` | When available in JSON  
`first_seen` | When available in JSON  
`last_seen` | When available in JSON  
`report_link` | When available in JSON  
  
##### JSON Result

The following example describes the JSON result output received when using the **Enrich Domain** action with Backstory API:
    
    
      {
                  {
                      "sources": [
                          {
                              "source": "ET Intelligence Rep List",
                              "confidenceScore": {
                                  "normalizedConfidenceScore": "Low",
                                  "intRawConfidenceScore": 0
                              },
                              "rawSeverity": "High",
                              "category": "Malware Command and Control Server"
                          }
                      ],
                      "iocIngestTime": "2021-01-26T17:00:00Z",
                      "firstSeenTime": "2018-10-03T00:03:53Z",
                      "lastSeenTime": "2022-02-09T10:52:21.229Z",
                      "uri": [
                          "https://INSTANCE/domainResults?domain=example.net&selectedList=DomainViewDistinctAssets&whoIsTimestamp=2022-02-09T11%3A51%3A52.393783515Z"
                      ]
                  }
      }
      

The following example describes the JSON result output received when using the **Enrich Domain** action with the Chronicle API:
    
    
    [
      {
        "Entity": "example.com",
        "EntityResult": {
          "sources": [
            {
              "category": "Indicator was published in publicly available sources",
              "firstActiveTime": "1970-01-01T00:00:01Z",
              "lastActiveTime": "9999-12-31T23:59:59Z",
              "addresses": [
                {
                  "domain": "example.com"
                }
              ],
              "rawSeverity": "medium",
              "confidenceScore": {
                "strRawConfidenceScore": "100"
              }
            },
            {
              "category": "Phishing",
              "firstActiveTime": null,
              "lastActiveTime": "2020-11-27T14:31:37Z",
              "addresses": [
                {
                  "domain": "example.com"
                },
                {
                  "ipAddress": "IP_ADDRESS"
                }
              ],
              "rawSeverity": "high",
              "confidenceScore": {
                "strRawConfidenceScore": "high"
              }
            },
            {
              "category": "Indicator was published in publicly available sources",
              "firstActiveTime": "1970-01-01T00:00:01Z",
              "lastActiveTime": "9999-12-31T23:59:59Z",
              "addresses": [
                {
                  "domain": "example.com"
                }
              ],
              "rawSeverity": "medium",
              "confidenceScore": {
                "strRawConfidenceScore": "100"
              }
            }
          ],
          "feeds": [
            {
              "metadata": {
                "title": "Mandiant Open Source Intelligence",
                "description": "Open Source Intel IoC",
                "confidenceScoreBucket": {
                  "rangeEnd": 100
                }
              },
              "iocs": [
                {
                  "domainAndPorts": {
                    "domain": "example.com"
                  },
                  "categorization": "Indicator was published in publicly available sources",
                  "activeTimerange": {
                    "start": "1970-01-01T00:00:01Z",
                    "end": "9999-12-31T23:59:59Z"
                  },
                  "confidenceScore": "100",
                  "rawSeverity": "Medium"
                }
              ]
            },
            {
              "metadata": {
                "title": "ESET Threat Intelligence",
                "description": "ESET Threat Intelligence"
              },
              "iocs": [
                {
                  "domainAndPorts": {
                    "domain": "example.com"
                  },
                  "categorization": "Phishing",
                  "activeTimerange": {
                    "end": "2020-11-27T14:31:37Z"
                  },
                  "ipAndPorts": {
                    "ipAddress": "IP_ADDRESS"
                  },
                  "confidenceScore": "High",
                  "rawSeverity": "High"
                }
              ]
            },
            {
              "metadata": {
                "title": "Mandiant Active Breach Intelligence",
                "description": "Mandiant Active Breach IoC",
                "confidenceScoreBucket": {
                  "rangeEnd": 100
                }
              },
              "iocs": [
                {
                  "domainAndPorts": {
                    "domain": "example.com"
                  },
                  "categorization": "Indicator was published in publicly available sources",
                  "activeTimerange": {
                    "start": "1970-01-01T00:00:01Z",
                    "end": "9999-12-31T23:59:59Z"
                  },
                  "confidenceScore": "100",
                  "rawSeverity": "Medium"
                }
              ]
            }
          ]
        }
      }
    ]
      

##### Output messages

The **Enrich Domain** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following domain in Google Chronicle: LIST_OF_IDS` | The action succeeded.  
`Error executing action "Enrich Domain". Reason: ERROR_REASON` | The action failed. Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Enrich Domain** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enrich Entities

Use the **Enrich Entities** action to query Google SecOps for additional context and attributes for specified entity types. This action enhances threat investigation data by integrating external intelligence.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `URL` (extracts domain from URL)
  * `User`
  * `Email` (user entity with email regex)

**Note:** This action only works with Chronicle API authentication. Backstory API is not supported. If you are using a Unified SecOps deployment, ensure you have configured a dedicated service account and provided credentials in the integration parameters.

#### Action inputs

The **Enrich Entities** action requires the following parameters:

Parameter | Description  
---|---  
`Namespace` | Optional. The logical grouping or scope of the entities to enrich. If not selected, the enrichment applies to entities in the default namespace or all accessible namespaces. Entities must belong to this namespace to be processed.  
`Time Frame` | Optional. A relative timeframe (for example, `1 day`, `2 hours`). This parameter takes precedence over `Start Time` and `End Time`.   
`Start Time` | Optional.The start time for the enrichment period in ISO 8601 format. Use this with `End Time` if `Time Frame` isn't set.  
`End Time` | Optional.The absolute end time for the enrichment period in ISO 8601 format. Used with `Start Time` if `Time Frame` isn't set.  
  
#### Action outputs

The **Enrich Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
* The **Enrich Entities** action supports the following entity enrichment for any entity:
Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`GoogleSecOps_related_entities` | The number of related_entities | When available in the JSON result.  
`GoogleSecOps_alert_count_`ruleName | {alertCounts.count} for each specific rule | When available in the JSON result.  
`GoogleSecOps_first_seen` | `metric.firstSeen` | When available in the JSON result.  
`GoogleSecOps_last_seen` | `metric.lastSeen` | When available in the JSON result.  
`GoogleSecOps_`flattened_key_under_entity | The value of the key, flattened from the nested structure under the `"entity"` object. | When available in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Enrich Entities** action:
    
    
    [
     {
       "Entity": "HTTP://MARKOSSOLOMON.COM/F1Q7QX.PHP",
       "EntityResult": {
         "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/ChFtYXJrb3Nzb2xvbW9uLmNvbRDIAQ",
         "metadata": { "entityType": "DOMAIN_NAME" },
         "entity": {
           "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/ChFtYXJrb3Nzb2xvbW9uLmNvbRDIAQ",
           "metadata": { "entityType": "DOMAIN_NAME" },
           "entity": {
             "domain": {
               "name": "markossolomon.com",
               "firstSeenTime": "1970-01-01T00:00:00Z",
               "lastSeenTime": "1970-01-01T00:00:00Z",
               "registrar": "NameCheap, Inc.",
               "creationTime": "2013-12-06T02:41:09Z",
               "updateTime": "2019-11-06T11:48:33Z",
               "expirationTime": "2020-12-06T02:41:09Z",
               "registrant": {
                 "userDisplayName": "WhoisGuard Protected",
                 "emailAddresses": [
                   "58d09cb5035042e9920408f8bafd0869.protect@whoisguard.com"
                 ],
                 "personalAddress": { "countryOrRegion": "PANAMA" },
                 "companyName": "WhoisGuard, Inc."
               }
             }
           }
         },
         "timeline": {
           "buckets": [
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {}
           ],
           "bucketSize": "172800s"
         }
       }
     },
     {
       "Entity": "npatni-sysops",
       "EntityResult": {
         "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/Cg1ucGF0bmktc3lzb3BzEGYaBVl1cml5IhsKCwiC-OzCBhCAvYMUEgwIqvnnwwYQgMyI4QE",
         "metadata": {
           "entityType": "ASSET",
           "interval": {
             "startTime": "2025-06-25T00:00:02.042Z",
             "endTime": "2025-07-18T07:50:02.472Z"
           }
         },
         "entity": {
           "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/Cg1ucGF0bmktc3lzb3BzEGYaBVl1cml5IhsKCwiC-OzCBhCAvYMUEgwIqvnnwwYQgMyI4QE",
           "metadata": {
             "entityType": "ASSET",
             "interval": {
               "startTime": "2025-06-25T00:00:02.042Z",
               "endTime": "2025-07-18T07:50:02.472Z"
             }
           },
           "entity": {
             "namespace": "Yuriy",
             "asset": { "hostname": "npatni-sysops" }
           },
           "metric": {
             "firstSeen": "2025-06-25T00:00:02.042Z",
             "lastSeen": "2025-07-18T07:50:02.472Z"
           }
         },
         "metric": {
           "firstSeen": "2025-06-25T00:00:02.042Z",
           "lastSeen": "2025-07-18T07:50:02.472Z"
         },
         "alertCounts": [
           { "rule": "rule_Pavel_test_Risk_score", "count": "329" },
           { "rule": "rule_testbucket", "count": "339" },
           { "rule": "pavel_test2_rule_1749239699456", "count": "332" }
         ],
         "timeline": {
           "buckets": [
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             { "alertCount": 1000 }
           ],
           "bucketSize": "172800s"
         }
       }
     },
     {
       "Entity": "exlab2019-ad",
       "EntityResult": {
         "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/CgxleGxhYjIwMTktYWQQZhoFWXVyaXkiGwoMCLv57MIGEMCp7qgDEgsI8PTnwwYQwLD6SA",
         "metadata": {
           "entityType": "ASSET",
           "interval": {
             "startTime": "2025-06-25T00:03:07.891Z",
             "endTime": "2025-07-18T07:40:32.153Z"
           }
         },
         "entity": {
           "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/CgxleGxhYjIwMTktYWQQZhoFWXVyaXkiGwoMCLv57MIGEMCp7qgDEgsI8PTnwwYQwLD6SA",
           "metadata": {
             "entityType": "ASSET",
             "interval": {
               "startTime": "2025-06-25T00:03:07.891Z",
               "endTime": "2025-07-18T07:40:32.153Z"
             }
           },
           "entity": {
             "namespace": "Yuriy",
             "asset": { "hostname": "exlab2019-ad" }
           },
           "metric": {
             "firstSeen": "2025-06-25T00:03:07.891Z",
             "lastSeen": "2025-07-18T07:40:32.153Z"
           }
         },
         "metric": {
           "firstSeen": "2025-06-25T00:03:07.891Z",
           "lastSeen": "2025-07-18T07:40:32.153Z"
         },
         "alertCounts": [
           { "rule": "pavel_test2_rule_1749239699456", "count": "319" },
           { "rule": "rule_testbucket", "count": "360" },
           { "rule": "rule_Pavel_test_Risk_score", "count": "321" }
         ],
         "timeline": {
           "buckets": [
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             { "alertCount": 26 },
             { "alertCount": 175 },
             { "alertCount": 185 },
             { "alertCount": 195 },
             { "alertCount": 182 },
             { "alertCount": 168 },
             { "alertCount": 69 }
           ],
           "bucketSize": "172800s"
         }
       }
     },
     {
       "Entity": "172.30.202.229",
       "EntityResult": {
         "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/Cg4xNzIuMzAuMjAyLjIyORBkGgVZdXJpeSIbCgwIu_nswgYQwKnuqAMSCwjw9OfDBhDAsPpI",
         "metadata": {
           "entityType": "ASSET",
           "interval": {
             "startTime": "2025-06-25T00:03:07.891Z",
             "endTime": "2025-07-18T07:40:32.153Z"
           }
         },
         "entity": {
           "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/Cg4xNzIuMzAuMjAyLjIyORBkGgVZdXJpeSIbCgwIu_nswgYQwKnuqAMSCwjw9OfDBhDAsPpI",
           "metadata": {
             "entityType": "ASSET",
             "interval": {
               "startTime": "2025-06-25T00:03:07.891Z",
               "endTime": "2025-07-18T07:40:32.153Z"
             }
           },
           "entity": {
             "namespace": "Yuriy",
             "asset": { "ip": ["172.30.202.229"] }
           },
           "metric": {
             "firstSeen": "2025-06-25T00:03:07.891Z",
             "lastSeen": "2025-07-18T07:40:32.153Z"
           }
         },
         "metric": {
           "firstSeen": "2025-06-25T00:03:07.891Z",
           "lastSeen": "2025-07-18T07:40:32.153Z"
         },
         "alertCounts": [
           { "rule": "rule_Pavel_test_Risk_score", "count": "321" },
           { "rule": "rule_testbucket", "count": "360" },
           { "rule": "pavel_test2_rule_1749239699456", "count": "319" }
         ],
         "timeline": {
           "buckets": [
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             { "alertCount": 26 },
             { "alertCount": 175 },
             { "alertCount": 185 },
             { "alertCount": 195 },
             { "alertCount": 182 },
             { "alertCount": 168 },
             { "alertCount": 69 }
           ],
           "bucketSize": "172800s"
         }
       }
     },
     {
       "Entity": "172.17.0.1",
       "EntityResult": {
         "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/CgoxNzIuMTcuMC4xEGQaBVl1cml5IhsKCwjOzre-BhDA1rU_EgwI9ZOMwAYQgPn82QM",
         "metadata": {
           "entityType": "ASSET",
           "interval": {
             "startTime": "2025-03-09T19:09:02.133Z",
             "endTime": "2025-04-19T02:27:01.994Z"
           }
         },
         "entity": {
           "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/CgoxNzIuMTcuMC4xEGQaBVl1cml5IhsKCwjOzre-BhDA1rU_EgwI9ZOMwAYQgPn82QM",
           "metadata": {
             "entityType": "ASSET",
             "interval": {
               "startTime": "2025-03-09T19:09:02.133Z",
               "endTime": "2025-04-19T02:27:01.994Z"
             }
           },
           "entity": { "namespace": "Yuriy", "asset": { "ip": ["172.17.0.1"] } },
           "metric": {
             "firstSeen": "2025-03-09T19:09:02.133Z",
             "lastSeen": "2025-04-19T02:27:01.994Z"
           }
         },
         "metric": {
           "firstSeen": "2025-03-09T19:09:02.133Z",
           "lastSeen": "2025-04-19T02:27:01.994Z"
         },
         "timeline": {
           "buckets": [
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {}
           ],
           "bucketSize": "172800s"
         }
       }
     },
     {
       "Entity": "911d039e71583a07320b32bde22f8e22",
       "EntityResult": {
         "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/CiA5MTFkMDM5ZTcxNTgzYTA3MzIwYjMyYmRlMjJmOGUyMhCwAiIVCgYItrj6ugYSCwi_9ufDBhDAyroV",
         "metadata": {
           "entityType": "FILE",
           "interval": {
             "startTime": "2024-12-15T09:07:02Z",
             "endTime": "2025-07-18T07:43:59.045Z"
           }
         },
         "entity": {
           "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/CiA5MTFkMDM5ZTcxNTgzYTA3MzIwYjMyYmRlMjJmOGUyMhCwAiIVCgYItrj6ugYSCwi_9ufDBhDAyroV",
           "metadata": {
             "entityType": "FILE",
             "interval": {
               "startTime": "2024-12-15T09:07:02Z",
               "endTime": "2025-07-18T07:43:59.045Z"
             }
           },
           "entity": {
             "file": {
               "sha256": "bc866cfcdda37e24dc2634dc282c7a0e6f55209da17a8fa105b07414c0e7c527",
               "md5": "911d039e71583a07320b32bde22f8e22",
               "sha1": "ded8fd7f36417f66eb6ada10e0c0d7c0022986e9",
               "size": "278528",
               "fileType": "FILE_TYPE_PE_EXE",
               "names": [
                 "C:\\Windows\\System32\\cmd.exe",
                 "cmd",
                 "Cmd.Exe",
                 "C:\\Windows\\system32\\cmd.exe",
                 "C:\\Windows\\SYSTEM32\\cmd.exe",
                 "cmd.exe",
                 "C:\\\\Windows\\\\System32\\\\cmd.exe",
                 "C:\\windows\\SYSTEM32\\cmd.exe",
                 "C:\\Users\\user\\AppData\\Local\\Temp\\wjxpour4.d0f\\cmd.exe",
                 "c:\\Windows\\System32\\cmd.exe",
                 "Utilman.exe",
                 "c:\\windows\\system32\\cmd.exe",
                 "System32/cmd.exe",
                 "UtilityVM/Files/Windows/System32/cmd.exe",
                 "KerishDoctor/Data/KerishDoctor/Restore/cmd.rst",
                 "cmd.exe_",
                 "C:\\WINDOWS\\SYSTEM32\\cmd.exe",
                 "Cmd.exe",
                 "Windows/System32/cmd.exe",
                 "sethc.exe",
                 "C:\\WINDOWS\\System32\\cmd.exe",
                 "esRzqurX.exe",
                 "rofl.png",
                 "F:\\Windows\\SYSTEM32\\cmd.exe",
                 "utilman.exe",
                 "C:\\Windows\\system32\\CMD.exe",
                 "sys32exe/cmd.exe",
                 "cmd.txt",
                 "C:\\WINDOWS\\system32\\cmd.exe",
                 "cmd2.exe",
                 "Utilman.exe.sc",
                 "uhrHRIv8.exe",
                 "C:\\windows\\system32\\cmd.exe",
                 "submitted_file",
                 "C:\\Users\\user\\AppData\\Local\\Temp\\n1qo0bq3.2tn\\KerishDoctor\\Data\\KerishDoctor\\Restore\\cmd.rst",
                 "J6ff7z0hLYo.exe",
                 "N:\\Windows\\System32\\cmd.exe",
                 "Q:\\Windows\\System32\\cmd.exe",
                 "C:\\Users\\user\\AppData\\Local\\Temp\\cmd.exe",
                 "C:\\Users\\<USER>\\AppData\\Local\\Temp\\cmd.exe",
                 "test.exe",
                 "68E2F01F8DE9EFCAE9C0DD893DF0E8C34E2B5C98A6C4073C9C9E8093743D318600.blob",
                 "8FCVE0Kq.exe",
                 "cmd (7).exe",
                 "cmd (8).exe",
                 "21455_16499564_bc866cfcdda37e24dc2634dc282c7a0e6f55209da17a8fa105b07414c0e7c527_cmd.exe",
                 "LinX v0.9.11 (Intel)/cmd.exe",
                 "C:\\Users\\user\\AppData\\Local\\Temp\\inbvmkaa.1xd\\LinX v0.9.11 (Intel)\\cmd.exe",
                 "cmd_b.exe",
                 "C:\\Users\\user\\AppData\\Local\\Temp\\sfd5bhoe.nqi\\cmd.exe",
                 "cMd.exe",
                 "Repl_Check.bat__",
                 "cmd.pdf",
                 "cmd.EXE",
                 "C:\\Users\\user\\AppData\\Local\\Temp\\uszjr42t.kda\\cmd.exe",
                 "LFepc1St.exe",
                 "firefox.exe",
                 "3BcnNlWV.exe",
                 "Utilman.exebak",
                 "utilman1.exe",
                 "1.exe",
                 "C:\\Users\\user\\AppData\\Local\\Temp\\ispvscgp.ep2\\sys32exe\\cmd.exe",
                 "cmd_1771019736291028992.exe",
                 "C:\\Users\\user\\AppData\\Local\\Temp\\xijgwqvd.54g\\cmd.exe",
                 "Sethc.exe",
                 "\\Device\\CdRom1\\DANFE352023067616112\\DANFE352023067616112.EXE",
                 "DANFE352023067616112.exe",
                 "file.exe",
                 "DANFE352023067616112/DANFE352023067616112.exe",
                 "C:\\Windows\\SYSTEM32\\Cmd.exe",
                 "pippo.exe",
                 "C:\\Windows\\System32\\sethc.exe",
                 "cmd.exe-bws024-windowsfolder",
                 "whatever.exe",
                 "sethc.exe.bak",
                 "S71dbOR1.exe",
                 "F:\\windows\\SYSTEM32\\cmd.exe",
                 "L6puhWL7.exe",
                 "DANFE357986551413927.exe",
                 "DANFE357666506667634.exe",
                 "\\Device\\CdRom1\\DANFE357666506667634\\DANFE357666506667634.EXE",
                 "\\Device\\CdRom1\\DANFE357986551413927\\DANFE357986551413927.EXE",
                 "\\Device\\CdRom1\\DANFE358567378531506\\DANFE358567378531506.EXE",
                 "\\Device\\CdRom1\\HtmlFactura3f48daa069f0e42253194ca7b51e7481DPCYKJ4Ojk\\HTMLFACTURA3F48DAA069F0E42253194CA7B51E7481DPCYKJ4OJK.EXE",
                 "\\Device\\CdRom1\\DANFE357410790837014\\DANFE357410790837014.EXE",
                 "\\Device\\CdRom1\\DANFE357702036539112\\DANFE357702036539112.EXE",
                 "winlogon.exe",
                 "AccessibilityEscalation.A' in file 'utilman.exe'",
                 "qpl9AqT0.exe",
                 "C:\\windows\\system32\\CMD.exe",
                 "C:\\po8az\\2po9hmc\\4v1b5.exe",
                 "batya.exe",
                 "nqAwJaba.exe",
                 "\\Device\\CdRom1\\DANFE356907191810758\\DANFE356907191810758.EXE",
                 "/Volumes/10_11_2023/DANFE356907191810758/DANFE356907191810758.exe",
                 "/Volumes/09_21_2023/DANFE357986551413927/DANFE357986551413927.exe",
                 "\\Device\\CdRom1\\DANFE355460800350113\\DANFE355460800350113.EXE",
                 "/Volumes/09_19_2023/DANFE355460800350113/DANFE355460800350113.exe",
                 "DANFE352429512050669.exe",
                 "/Volumes/04_15_2023/HtmlFacturaeb58f4396e2028a70905705291031e7b3dlvDNyGp3/HtmlFacturaeb58f4396e2028a70905705291031e7b3dlvDNyGp3.exe"
               ],
               "firstSeenTime": "2024-12-15T09:07:02Z",
               "lastSeenTime": "2025-07-18T07:43:59.045Z",
               "lastAnalysisTime": "2025-07-16T10:06:40Z",
               "signatureInfo": {
                 "sigcheck": {
                   "verificationMessage": "Signed",
                   "verified": true,
                   "signers": [{ "name": "Microsoft Windows" }]
                 }
               },
               "firstSubmissionTime": "2025-07-15T16:30:27Z"
             }
           },
           "metric": {
             "firstSeen": "2024-12-15T09:07:02Z",
             "lastSeen": "2025-07-18T07:43:59.045Z"
           }
         },
         "metric": {
           "firstSeen": "2024-12-15T09:07:02Z",
           "lastSeen": "2025-07-18T07:43:59.045Z"
         },
         "alertCounts": [
           { "rule": "pavel_test2_rule_1749239699456", "count": "329" },
           { "rule": "rule_testbucket", "count": "345" },
           { "rule": "rule_Pavel_test_Risk_score", "count": "326" }
         ],
         "timeline": {
           "buckets": [
             {},
             {},
             {},
             {},
             { "alertCount": 31 },
             { "alertCount": 111 },
             { "alertCount": 109 },
             { "alertCount": 82 },
             { "alertCount": 86 },
             { "alertCount": 98 },
             { "alertCount": 86 },
             { "alertCount": 85 },
             { "alertCount": 92 },
             { "alertCount": 89 },
             { "alertCount": 90 },
             { "alertCount": 41 }
           ],
           "bucketSize": "172800s"
         },
         "prevalenceResult": [
           { "prevalenceTime": "2025-01-16T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-17T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-18T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-19T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-20T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-21T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-22T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-23T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-24T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-25T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-26T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-27T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-28T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-29T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-30T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-01-31T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-01T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-02T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-03T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-04T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-05T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-06T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-07T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-08T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-09T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-10T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-11T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-12T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-13T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-14T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-15T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-16T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-17T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-18T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-19T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-20T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-21T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-22T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-23T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-24T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-25T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-26T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-27T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-02-28T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-01T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-02T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-03T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-04T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-05T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-06T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-07T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-08T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-09T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-10T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-11T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-12T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-13T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-14T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-15T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-16T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-17T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-18T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-19T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-20T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-21T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-22T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-23T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-24T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-25T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-26T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-27T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-28T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-29T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-30T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-03-31T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-01T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-02T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-03T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-04T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-05T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-06T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-07T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-08T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-09T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-10T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-11T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-12T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-13T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-14T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-15T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-16T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-17T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-18T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-19T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-20T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-21T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-22T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-23T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-24T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-25T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-26T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-27T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-28T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-29T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-04-30T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-01T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-02T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-03T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-04T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-05T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-06T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-07T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-08T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-09T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-10T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-11T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-12T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-13T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-14T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-15T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-16T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-17T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-18T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-19T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-20T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-21T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-22T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-23T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-24T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-25T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-26T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-27T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-28T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-29T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-30T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-05-31T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-01T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-02T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-03T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-04T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-05T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-06T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-07T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-08T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-09T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-10T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-11T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-12T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-13T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-14T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-15T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-16T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-17T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-18T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-19T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-20T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-21T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-22T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-23T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-24T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-25T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-26T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-27T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-28T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-29T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-06-30T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-01T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-02T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-03T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-04T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-05T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-06T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-07T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-08T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-09T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-10T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-11T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-12T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-13T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-14T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-15T00:00:00Z", "count": 1 },
           { "prevalenceTime": "2025-07-16T00:00:00Z", "count": 2 },
           { "prevalenceTime": "2025-07-17T00:00:00Z", "count": 2 },
           { "prevalenceTime": "2025-07-18T00:00:00Z", "count": 2 }
         ],
         "relatedEntities": [
           {
             "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/CgxleGxhYjIwMTktYWQQZhoFWXVyaXkiFQoGCPbso7wGEgsIv_bnwwYQwMq6FQ",
             "metadata": {
               "entityType": "ASSET",
               "interval": {
                 "startTime": "2025-01-16T12:07:18Z",
                 "endTime": "2025-07-18T07:43:59.045Z"
               }
             },
             "entity": {
               "namespace": "Yuriy",
               "asset": {
                 "hostname": "exlab2019-ad",
                 "firstSeenTime": "2025-01-16T12:07:18Z"
               }
             },
             "metric": {
               "firstSeen": "2025-01-16T12:07:18Z",
               "lastSeen": "2025-07-18T07:43:59.045Z"
             }
           },
           {
             "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/Cg4xNzIuMzAuMjAyLjIyORBkGgVZdXJpeSIVCgYI9uyjvAYSCwi_9ufDBhDAyroV",
             "metadata": {
               "entityType": "ASSET",
               "interval": {
                 "startTime": "2025-01-16T12:07:18Z",
                 "endTime": "2025-07-18T07:43:59.045Z"
               }
             },
             "entity": {
               "namespace": "Yuriy",
               "asset": {
                 "ip": ["172.30.202.229"],
                 "firstSeenTime": "2025-01-16T12:07:18Z"
               }
             },
             "metric": {
               "firstSeen": "2025-01-16T12:07:18Z",
               "lastSeen": "2025-07-18T07:43:59.045Z"
             }
           }
         ]
       }
     },
     {
       "Entity": "tencent.com",
       "EntityResult": {
         "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/Cgt0ZW5jZW50LmNvbRDIASIQCgYInNyZvAYSBgjo-Jm8Bg",
         "metadata": {
           "entityType": "DOMAIN_NAME",
           "interval": {
             "startTime": "2025-01-14T14:01:00Z",
             "endTime": "2025-01-14T15:02:00Z"
           }
         },
         "entity": {
           "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/Cgt0ZW5jZW50LmNvbRDIASIQCgYInNyZvAYSBgjo-Jm8Bg",
           "metadata": {
             "entityType": "DOMAIN_NAME",
             "interval": {
               "startTime": "2025-01-14T14:01:00Z",
               "endTime": "2025-01-14T15:02:00Z"
             }
           },
           "entity": {
             "domain": {
               "name": "tencent.com",
               "firstSeenTime": "2025-01-14T14:01:00Z",
               "lastSeenTime": "2025-01-14T15:02:00Z",
               "registrar": "MarkMonitor Information Technology (Shanghai) Co., Ltd.",
               "creationTime": "1998-09-14T04:00:00Z",
               "updateTime": "2024-08-20T08:04:01Z",
               "expirationTime": "2032-09-13T04:00:00Z",
               "registrant": {
                 "emailAddresses": [""],
                 "personalAddress": { "countryOrRegion": "CHINA" },
                 "companyName": "\u6df1\u5733\u5e02\u817e\u8baf\u8ba1\u7b97\u673a\u7cfb\u7edf\u6709\u9650\u516c\u53f8"
               }
             }
           },
           "metric": {
             "firstSeen": "2025-01-14T14:01:00Z",
             "lastSeen": "2025-01-14T15:02:00Z"
           }
         },
         "metric": {
           "firstSeen": "2025-01-14T14:01:00Z",
           "lastSeen": "2025-01-14T15:02:00Z"
         },
         "timeline": {
           "buckets": [
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {}
           ],
           "bucketSize": "172800s"
         }
       }
     },
     {
       "Entity": "00:50:56:b6:34:86",
       "EntityResult": {
         "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/ChEwMDo1MDo1NjpiNjozNDo4NhBlGgVZdXJpeSIKCgASBgjemLzBBg",
         "metadata": {
           "entityType": "ASSET",
           "interval": {
             "startTime": "1970-01-01T00:00:00Z",
             "endTime": "2025-05-22T11:37:02Z"
           }
         },
         "entity": {
           "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/entities/ChEwMDo1MDo1NjpiNjozNDo4NhBlGgVZdXJpeSIKCgASBgjemLzBBg",
           "metadata": {
             "entityType": "ASSET",
             "interval": {
               "startTime": "1970-01-01T00:00:00Z",
               "endTime": "2025-05-22T11:37:02Z"
             }
           },
           "entity": {
             "namespace": "Yuriy",
             "asset": { "mac": ["00:50:56:b6:34:86"] }
           },
           "metric": {
             "firstSeen": "1970-01-01T00:00:00Z",
             "lastSeen": "2025-05-22T11:37:02Z"
           }
         },
         "metric": {
           "firstSeen": "1970-01-01T00:00:00Z",
           "lastSeen": "2025-05-22T11:37:02Z"
         },
         "timeline": {
           "buckets": [
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {},
             {}
           ],
           "bucketSize": "172800s"
         }
       }
     }
    ]
    

##### Output messages

The **Enrich Entities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following entities information from Google SecOps: ENTITY_ID ` `Action wasn't able to enrich the following entities using information from Google SecOps: ENTITY_ID` `None of the provided entities were enriched using information from Google SecOps.` | The action succeeded.  
`Error executing action "Enrich Entities". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Entities** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enrich IP - Deprecated

**Deprecated:** This action is deprecated.

Use the **Enrich IP** action to enrich IP entities using information from IoCs in Google SecOps.

This action runs on the `IP Address` entity.

#### Action inputs

The **Enrich IP** action requires the following parameters:

Parameter | Description  
---|---  
`Create Insight` | Optional.If selected, the action creates an insight which contains information about entities.Enabled by default.  
`Only Suspicious Insight` | Optional.If selected, the action creates insights only for entities that are marked as suspicious.Not enabled by default. If you select this parameter, `Create Insight` must also be selected.  
`Lowest Suspicious Severity` | Required. The lowest severity associated with the IP address to mark it suspicious.The default value is `Medium`. The possible values are as follows:

  * `High`
  * `Medium`
  * `Low`
  * `Info`

  
`Mark Suspicious N/A Severity` | Required. If selected and the information about severity is unavailable, the action marks the entity as suspicious.  
  
#### Action outputs

The **Enrich IP** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

Name: ENTITY_IDENTIFIER

Columns:

  * **Source**
  * **Severity**
  * **Category**
  * **Confidence**
  * **Related Domains**



#### Entity enrichment

The **Enrich IP** action supports the following entity enrichment logic:

Enrichment field | Logic (when to apply)  
---|---  
`severity` | When available in JSON  
`average_confidence` | When available in JSON  
`related_domains` | When available in JSON  
`categories` | When available in JSON  
`sources` | When available in JSON  
`first_seen` | When available in JSON  
`last_seen` | When available in JSON  
`report_link` | When available in JSON  
  
##### JSON result

The following example describes the JSON result output received when using the **Enrich IP** action with Backstory API:
    
    
    {
                {
                    "sources": [
                        {
                            "source": "Example List",
                            "confidenceScore": {
                                "normalizedConfidenceScore": "Low",
                                "intRawConfidenceScore": 0
                            },
                            "rawSeverity": "High",
                            "category": "Malware Command and Control Server"
                        }
                    ],
                    "iocIngestTime": "2021-01-26T17:00:00Z",
                    "firstSeenTime": "2018-10-03T00:03:53Z",
                    "lastSeenTime": "2022-02-09T10:52:21.229Z",
                    "uri": [
                        "https://INSTANCE/domainResults?domain=example.net&selectedList=DomainViewDistinctAssets&whoIsTimestamp=2022-02-09T11%3A51%3A52.393783515Z"
                    ]
                }
    }
    

The following example describes the JSON result output received when using the **Enrich IP** action with Chronicle API:
    
    
    [
      {
        "Entity": "192.0.2.121",
        "EntityResult": {
          "sources": [
            {
              "category": "Indicator was published in publicly available sources",
              "firstActiveTime": "1970-01-01T00:00:01Z",
              "lastActiveTime": "9999-12-31T23:59:59Z",
              "addresses": [
                {
                  "ipAddress": "IP_ADDRESS"
                }
              ],
              "rawSeverity": "low",
              "confidenceScore": {
                "strRawConfidenceScore": "67"
              }
            }
          ],
          "feeds": [
            {
              "metadata": {
                "title": "Mandiant Open Source Intelligence",
                "description": "Open Source Intel IoC",
                "confidenceScoreBucket": {
                  "rangeEnd": 100
                }
              },
              "iocs": [
                {
                  "categorization": "Indicator was published in publicly available sources",
                  "activeTimerange": {
                    "start": "1970-01-01T00:00:01Z",
                    "end": "9999-12-31T23:59:59Z"
                  },
                  "ipAndPorts": {
                    "ipAddress": "IP_ADDRESS"
                  },
                  "confidenceScore": "67",
                  "rawSeverity": "Low"
                }
              ]
            }
          ]
        }
      }
    ]
    

##### Output messages

The **Enrich IP** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following IPs from Google Chronicle: ` LIST_OF_IPS | The action succeeded.  
`Error executing action "Enrich IP". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Enrich IP** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Execute Retrohunt

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **Execute Retrohunt** action to execute a rule retrohunt in Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Execute Retrohunt** action requires the following parameters:

Parameter | Description  
---|---  
`Rule ID` | Required. The ID of the rule to run a retrohunt for. Use the format `ru_{UUID}` for the latest version of a rule, or `ru_{UUID}@v_{int64}_{int64}` for a specific version.  
`Time Frame` | Optional. A period to retrieve the results for. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Alert Time Till Now`
  * `5 Minutes Around Alert Time`
  * `30 Minutes Around Alert Time`
  * `1 Hour Around Alert Time`
  * `Custom`

If `Custom` is selected, the `Start Time` parameter is required. The default value is `Last Hour`.  
`Start Time` | The start time for the results in ISO 8601 format. This parameter is required if the `Time Frame` parameter is set to `Custom`.  
`End Time` | The end time for the results in ISO 8601 format. If you don't set a value and select the `Custom` value for the `Time Frame` parameter, the current time is used.   
  
#### Action outputs

The **Execute Retrohunt** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
Entity insight | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Execute Retrohunt** action with Backstory API:
    
    
    {
      "retrohuntId": "oh_d738c8ea-8fd7-4cc1-b43d-25835b8e1785",
      "ruleId": "ru_30979d84-aa89-47d6-bf4d-b4bb0eacb497",
      "versionId": "ru_30979d84-aa89-47d6-bf4d-b4bb0eacb497@v_1612472807_179679000",
      "eventStartTime": "2021-01-14T23:00:00Z",
      "eventEndTime": "2021-01-30T23:00:00Z",
      "retrohuntStartTime": "2021-02-08T02:40:59.192113Z",
      "state": "RUNNING"
    }
    

The following example describes the JSON result output received when using the **Execute Retrohunt** action with Chronicle API:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us/instances/INSTANCE_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/RetrohuntMetadata",
        "retrohunt": "projects/PROJECT_ID/locations/us/instances/INSTANCE_ID/rules/RULE_ID/retrohunts/RETROHUNT_ID",
        "executionInterval": {
          "startTime": "2025-01-22T12:16:20.963182Z",
          "endTime": "2025-01-23T12:16:20.963182Z"
        }
      },
      "retrohuntId": "RETROHUNT_ID",
      "ruleId": "RULE_ID",
      "versionId": "VERSION_ID",
      "eventStartTime": "2025-01-22T12:16:20.963182Z",
      "eventEndTime": "2025-01-23T12:16:20.963182Z"
    }
    

##### Output messages

The **Execute Retrohunt** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully executed a retrohunt for the provided rule in Google Chronicle.` | The action succeeded.   
`Error executing action "Execute Retrohunt". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Execute Retrohunt** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Execute UDM Query

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **Execute UDM Query** action to execute a custom UDM query in Google SecOps.

This action doesn't run on Google SecOps entities. 

**Note:** For information about rate limits, see [UDM search rate limits](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#QPHlimits).

#### Action inputs

The **Execute UDM Query** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | Required. The query to execute in Google SecOps. **Note:** This parameter performs an explicit case-sensitivity check on the UDM query (unlike in the UDM search). To bypass this check, add `nocase` to the UDM Query parameter value.   
`Include Raw Log Data` | Optional. If selected, the action retrieves the original raw log file associated with the UDM search results. This option is only available when using Chronicle API authentication. Disabled by default.  
`Time Frame` | Optional. A period to retrieve the results for. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Alert Time Till Now`
  * `5 Minutes Around Alert Time`
  * `30 Minutes Around Alert Time`
  * `1 Hour Around Alert Time`
  * `Custom`

If `Custom` is selected, the `Start Time` parameter is required. The default value is `Last Hour`.  
`Start Time` | Optional.The start time for the results in ISO 8601 format (for example, `YYYY-MM-DD HH:mm:ss.SSSZ`). This parameter is required if the `Time Frame` parameter is set to `Custom`. The maximum time range is 90 days.  
`End Time` | Optional. The end time for the results in an ISO 8601 format (for example, `YYYY-MM-DD HH:mm:ss.SSSZ`). If you don't set a value and the `Time Frame` parameter is set to `Custom`, the current time is used. The maximum time range is 90 days.  
`Max Results To Return` | Optional. The number of results to return for a single query. The maximum value is `10,000`. The default value is `50`.  
  
#### Action outputs

The **Execute UDM Query** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Execute UDM Query** action:
    
    
    {
        "events": [
            {
                "name": "02c2c701c5bb7e7042701ayyyyyyyyyx,4,16496990275yyyxx,EMAIL,",
                "udm": {
                    "metadata": {
                        "enrichmentState": "ENRICHED",
                        "eventTimestamp": "2022-04-11T17:43:47.586Z",
                        "eventType": "EMAIL_TRANSACTION",
                        "ingestedTimestamp": "2022-04-11T15:50:21.912562Z",
                        "productName": "Chronicle Internal"
                    },
                    "network": {
                        "email": {
                            "from": "test@example.com",
                            "subject": [
                                "I did not create this service account"
                            ],
                            "to": [
                                "test@example.com"
                            ]
                        }
                    },
                    "principal": {
                        "asset": {
                            "assetId": "CS:8973060bcf1d441a8cf10eyyyyyyyyyx",
                            "hostname": "test-pc",
                            "ip": [
                                "10.2.xx.yyy"
                            ],
                            "mac": [
                                "b5:1c:8b:xx:xx:xx"
                            ]
                        },
                        "assetId": "CS:8973060bcf1d441a8cf10eyyyyyyyyyx",
                        "hostname": "test-pc",
                        "ip": [
                            "10.2.xx.yyy"
                        ],
                        "location": {
                            "city": "San Francisco",
                            "countryOrRegion": "US",
                            "state": "California"
                        },
                        "mac": [
                            "b5:1c:8b:xx:xx:xx"
                        ],
                        "user": {
                            "attribute": {
                                "labels": [
                                    {
                                        "key": "2FA Enabled",
                                        "value": "false"
                                    }
                                ]
                            },
                            "department": [
                                "Cymbal Investments IT Contractors"
                            ],
                            "emailAddresses": [
                                "test@example.com"
                            ],
                            "groupIdentifiers": [
                                "Contractors"
                            ],
                            "productObjectId": "test",
                            "title": "IT Support Agent",
                            "userDisplayName": "test test",
                            "userid": "test",
                            "windowsSid": "S-1-5-21-2623356yyy-8883713yyy-9684409yyy-yyyxx"
                        }
                    },
                    "rawLogData": {
                        "agent_id": "yyyyyy",
                        "aggregate_id": "yyyyyy",
                        "created_timestamp": "yyyyyy",
                        "decodedString": "yyyyyy",
                        "description": "yyyyyy",
                        "display_name": "yyyyyy",
                        "filename": "yyyyyy"
                    },
                    "securityResult": [
                        {
                            "action": [
                                "ALLOW"
                            ]
                        }
                    ]
                }
            },
            {
                "name": "02c2c701c5bb7e7042701ayyyyyyyyyx,3,16496987245yyyxx,EMAIL,",
                "udm": {
                    "metadata": {
                        "enrichmentState": "ENRICHED",
                        "eventTimestamp": "2022-04-11T17:38:44.586Z",
                        "eventType": "EMAIL_TRANSACTION",
                        "ingestedTimestamp": "2022-04-11T15:50:21.912562Z",
                        "productName": "Chronicle Internal"
                    },
                    "network": {
                        "email": {
                            "from": "test@example.com",
                            "subject": [
                                "Did you create this service account"
                            ],
                            "to": [
                                "test@example.com"
                            ]
                        }
                    },
                    "principal": {
                        "asset": {
                            "assetId": "CS:8973060bcf1d441a8cf10eyyyyyyyyyx",
                            "hostname": "test-pc",
                            "ip": [
                                "10.2.xx.yyy"
                            ],
                            "mac": [
                                "b5:1c:8b:xx:xx:xx"
                            ]
                        },
                        "assetId": "CS:8973060bcf1d441a8cf10eyyyyyyyyyx",
                        "hostname": "test-pc",
                        "ip": [
                            "10.2.xx.yyy"
                        ],
                        "location": {
                            "city": "San Francisco",
                            "countryOrRegion": "US",
                            "state": "California"
                        },
                        "mac": [
                            "b5:1c:8b:xx:xx:xx"
                        ],
                        "user": {
                            "attribute": {
                                "labels": [
                                    {
                                        "key": "2FA Enabled",
                                        "value": "false"
                                    }
                                ]
                            },
                            "department": [
                                "Cymbal Investments IT Contractors"
                            ],
                            "emailAddresses": [
                                "test@example.com"
                            ],
                            "groupIdentifiers": [
                                "Contractors"
                            ],
                            "productObjectId": "test",
                            "title": "IT Support Agent",
                            "userDisplayName": "test test",
                            "userid": "test",
                            "windowsSid": "S-1-5-21-2623356yyy-8883713yyy-9684409yyy-yyyxx"
                        }
                    },
                    "rawLogData": {
                        "agent_id": "yyyyyy",
                        "aggregate_id": "yyyyyy",
                        "created_timestamp": "yyyyyy",
                        "decodedString": "yyyyyy",
                        "description": "yyyyyy",
                        "display_name": "yyyyyy",
                        "filename": "yyyyyy"
                    },
                    "securityResult": [
                        {
                            "action": [
                                "ALLOW"
                            ]
                        }
                    ]
                }
            },
            {
                "avg_seconds": {
                    "values": [
                        {
                            "doubleVal": 1755680893.3333333
                        }
                    ]
                },
                "event_type_array": {
                    "values": [
                        {
                            "stringVal": "673961a71ba82e0556ef95cb2147e212"
                        }
                    ]
                },
                "target.file.vhash": {
                    "values": [
                        {
                            "stringVal": "673961a71ba82e0556ef95cb2147e212"
                        }
                    ]
                }
            }
        ]
    }
    

##### Output messages

The **Execute UDM Query** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully returned results for the query QUERY in Google Chronicle.` `No results were found for the query QUERY in Google Chronicle.` | The action succeeded.  
`Error executing action "Execute UDM Query". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
`Error executing action "Execute UDM Query". Reason: you've reached a rate limit. Please wait for several minutes and try again.` | The action failed. Wait for several minutes before running the action again.  
  
##### Script result

The following table describes the values for the script result output when using the **Execute UDM Query** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Execute UDM Query Async

**Important:** Aggregated queries are only supported through Chronicle API configuration of the integration.

Use the **Execute UDM Query Async** action to execute a custom UDM query in Google SecOps.

This action doesn't run on Google SecOps entities. 

**Note:** This action is asynchronous. Adjust the script timeout value in the Google SecOps integrated development environment (IDE) for the action as needed. 

For information about rate limits, see [UDM search rate limits](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#QPHlimits).

#### Action inputs

The **Execute UDM Query** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | Required. The query to execute in Google SecOps. **Note:** This parameter performs an explicit case-sensitivity check on the UDM query (unlike in the UDM search). To bypass this check, add `nocase` to the UDM Query parameter value.   
`Time Frame` | Optional. A period to retrieve the results for. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Alert Time Till Now`
  * `5 Minutes Around Alert Time`
  * `30 Minutes Around Alert Time`
  * `1 Hour Around Alert Time`
  * `Custom`

If `Alert Time Till Now` is selected, the action searches from the alert start time to the current time. If `5 Minutes Around Alert Time`, `30 Minutes Around Alert Time`, or `1 Hour Around Alert Time` is selected, the action searches the specified minutes around the alert start time. If `Custom` is selected, the `Start Time` parameter is required. The default value is `Last Hour`.  
`Start Time` | Optional.The start time for the results in ISO 8601 format (`YYYY-MM-DD HH:mm:ss.SSSZ`). This parameter is required if `Time Frame` is set to `Custom`. **Note:** `Start Time` and `End Time` must be within 90 days of each other.   
`End Time` | Optional. The end time for the results in an ISO 8601 format (`YYYY-MM-DD HH:mm:ss.SSSZ`). If you don't set a value and `Time Frame` is set to `Custom`, the current time is used. **Note:** `Start Time` and `End Time` must be within 90 days of each other.   
`Max Results To Return` | Optional. The number of results to return for a single query. The maximum value is `1,000,000`. The default value is `50`.  
  
#### Action outputs

The **Execute UDM Query Async** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Execute UDM Query Async** action:
    
    
    {
        "events": [
            {
                "event": {
                    "metadata": {
                        "eventTimestamp": "2022-01-20T09:15:15.687Z",
                        "eventType": "USER_LOGIN",
                        "vendorName": "Microsoft",
                        "productName": "Active Directory",
                        "ingestedTimestamp": "2022-01-20T09:45:07.433587Z"
                    },
                    "principal": {
                        "hostname": "workstation-01",
                        "ip": [
                            "192.168.1.50"
                        ],
                        "mac": [
                            "00:1A:2B:3C:4D:5E",
                            "00:1A:2B:3C:4D:5E",
                            "00:1A:2B:3C:4D:5E"
                        ],
                        "location": {
                            "city": "Metropolis",
                            "state": "New York",
                            "countryOrRegion": "US"
                        },
                        "asset": {
                            "hostname": "workstation-01",
                            "ip": [
                                "192.168.1.50",
                                "192.168.1.50",
                                "192.168.1.50"
                            ],
                            "mac": [
                                "00:1A:2B:3C:4D:5E",
                                "00:1A:2B:3C:4D:5E",
                                "00:1A:2B:3C:4D:5E"
                            ]
                        }
                    },
                    "target": {
                        "user": {
                            "userid": "user_alpha",
                            "userDisplayName": "User Alpha",
                            "windowsSid": "S-1-5-21-1111111111-2222222222-3333333333-1000",
                            "emailAddresses": [
                                "alpha@example.com",
                                "admin.alpha@example.com"
                            ],
                            "employeeId": "1234567",
                            "productObjectId": "11111111-2222-3333-4444-555555555555",
                            "firstName": "User",
                            "lastName": "Alpha",
                            "phoneNumbers": [
                                "555-0199-0000"
                            ],
                            "title": "Executive Assistant",
                            "companyName": "Example Corp",
                            "department": [
                                "Executive - Admin"
                            ],
                            "managers": [
                                {
                                    "userDisplayName": "Manager Beta",
                                    "windowsSid": "S-1-5-21-1111111111-2222222222-3333333333-2000",
                                    "emailAddresses": [
                                        "beta@example.com"
                                    ],
                                    "employeeId": "7654321",
                                    "productObjectId": "66666666-7777-8888-9999-000000000000",
                                    "firstName": "Manager",
                                    "lastName": "Beta",
                                    "phoneNumbers": [
                                        "555-0199-0001 ext 123"
                                    ],
                                    "title": "Chief Technology Officer",
                                    "companyName": "Example Corp",
                                    "department": [
                                        "Executive - Admin"
                                    ]
                                }
                            ]
                        },
                        "ip": [
                            "203.0.113.10"
                        ],
                        "email": "alpha@example.com",
                        "application": "Windows Sign In"
                    },
                    "securityResult": [
                        {
                            "summary": "Successful Login",
                            "action": [
                                "ALLOW"
                            ]
                        }
                    ],
                    "rawLogData": {
                        "agent_id": "00000000000000000000000000000001",
                        "aggregate_id": "aggind:00000000000000000000000000000001:123456789012",
                        "data_domains": [
                            "Endpoint"
                        ],
                        "description": "A suspicious process related to a likely malicious file was launched. Review any binaries involved as they may be related to malware.",
                        "device": {
                            "agent_load_flags": "0",
                            "agent_local_time": "2025-08-07T01:42:54.415Z",
                            "agent_version": "7.27.18003.0",
                            "bios_manufacturer": "Generic Manufacturer LTD"
                        },
                        "template_instance_id": "10001",
                        "timestamp": "2025-08-19T15:08:13.742Z",
                        "user_name": "root"
                    },
                    "extensions": {
                        "auth": {
                            "type": "SSO"
                        }
                    }
                },
                "eventLogToken": "abcdef0123456789abcdef0123456789,1,1642670115687000,USER,|USER_LOGIN"
            }
        ]
    }
    

##### Output messages

The **Execute UDM Query Async** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully returned results for the query QUERY in Google Chronicle.` `No results were found for the query QUERY in Google Chronicle.` | The action succeeded.  
`Error executing action "Execute UDM Query Async". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
`Error executing action "Execute UDM Query Async ". Reason: you've reached a rate limit. Please wait for several minutes and try again.` | The action failed. Wait for several minutes before running the action again.  
  
##### Script result

The following table describes the values for the script result output when using the **Execute UDM Query Async** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Generate UDM Query

(Preview) Use the **Generate UDM Query** action to construct complex UDM queries using natural language prompts in Google SecOps.

This action doesn't run on Google SecOps entities. 

**Note:** This action requires Chronicle API authentication. The legacy Backstory API authentication isn't supported

#### Action inputs

The **Generate UDM Query** action requires the following parameters:

Parameter | Description  
---|---  
`Prompt` | Required. The prompt that the system uses to generate the structured UDM query.  
  
#### Action outputs

The **Get Data Tables** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Generate UDM Query** action:
    
    
    {
      "query": "ip = \"10.0.0.1\""
    }
    

##### Output messages

The **Generate UDM Query** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully generated a UDM query in Google SecOps.` | The action succeeded.  
`Error executing action "Generate UDM Query". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Generate UDM Query** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Data Tables

Use the **Get Data Tables** action to retrieve available data tables in Google SecOps.

This action doesn't run on Google SecOps entities. 

**Note:** This action only works with Chronicle API authentication. Backstory API is not supported. If you are using a Unified SecOps deployment, ensure you have configured a dedicated service account and provided credentials in the integration parameters.

#### Action inputs

The **Get Data Tables** action requires the following parameters:

Parameter | Description  
---|---  
`Filter Key` | Optional. The key to filter by The `Name` option refers to the display name of the data table. The possible values are as follows:
* `Name`
* `Description`  
`Filter Logic` | Optional. The filter logic to apply. The possible values are as follows:
* `Equal` (for exact matches)
* `Contains`(for substring matches)  
`Filter Value` | Optional. The value to use in the filter. The possible values are as follows:
* `Equal` (for exact matches)
* `Contains`(for substring matches)
`Equal` works with the `Title` parameter, while `Contains` works with all values in the response. If nothing is provided, the filter won't be applied.  
`Expanded Rows` | Optional. If selected, the response includes detailed data table rows. Not enabled by default.  
`Max Data Tables To Return` | Required. The number of data tables to return. The maximum value is `1000`.  
`Max Data Table Rows To Return` | Required. The amount of data table rows to return. Only use this parameter if `Expanded Rows` is enabled. The maximum value is `1000`.  
  
#### Action outputs

The **Get Data Tables** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Get Data Tables** action:
    
    
    {
          "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/dataTables/data_table",
          "displayName": "data_table",
          "createTime": "2025-05-14T12:52:50.064133Z",
          "updateTime": "2025-05-14T13:13:48.631442Z",
          "columnInfo": [
              {
                  "originalColumn": "columnName1",
                  "columnType": "STRING"
              },
              {
                  "columnIndex": 1,
                  "originalColumn": "columnName2",
                  "columnType": "STRING"
              },
              {
                  "columnIndex": 2,
                  "originalColumn": "columnName3",
                  "columnType": "STRING"
              }
          ],
          "dataTableUuid": "c3cce57bb8d940d5ac4523c37d540436",
          "approximateRowCount": "2",
          "rows": [
              {
                  "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/dataTables/data_table/dataTableRows/840d18a85944833e1b97ed6d2fb11377",
                  "values": {
                      "columnName1": "asda",
                      "columnName2": "asdasd",
                      "columnName3": "zxczxc"
                  },
                  "createTime": "2025-05-14T12:52:51.908143Z",
                  "updateTime": "2025-05-14T12:52:51.908143Z"
              }
          ]
    }
    

##### Output messages

The **Get Data Tables** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found data tables for the provided criteria in Google SecOps` | The action succeeded.  
`Error executing action "Get Data Tables". Reason: ERROR_REASON` | The action failed. Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Get Data Tables** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Detection Details

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **Get Detection Details** action to retrieve information about a detection in Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Detection Details** action requires the following parameters:

Parameter | Description  
---|---  
`Rule ID` | Required. The ID of the rule related to the detection. Use the format `ru_{UUID}` for the latest version of a rule, or `ru_{UUID}@v_{int64}_{int64}` for a specific version.  
`Detection ID` | Required. The ID of the detection to fetch details for. If special characters are provided, the action doesn't fail, but returns a list of detections.  
`Include Raw Log Data` | Optional. If selected, the action retrieves the original raw log file associated with the UDM search results. This option is only available when using Chronicle API authentication. Disabled by default.  
  
#### Action outputs

The **Get Detection Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Get Detection Details** action:
    
    
    {
        "collectionElements": [
            {
                "label": "e",
                "references": [
                    {
                        "event": {
                            "metadata": {
                                "eventTimestamp": "2023-10-04T21:18:44Z",
                                "eventType": "NETWORK_CONNECTION",
                                "id": "yyyx=",
                                "ingestedTimestamp": "2023-10-04T21:31:03.790969Z",
                                "logType": "UDM",
                                "productEventType": "Traffic - start",
                                "productLogId": "yyyx-yyyx-yyyx45fc-yyyx-yyyx",
                                "productName": "NGFW",
                                "vendorName": "Palo Alto Networks"
                            },
                            "network": {
                                "ipProtocol": "TCP",
                                "receivedBytes": "yyyyyyyyyxx",
                                "sentBytes": "yyyyyyyyyxx",
                                "sessionId": "yyyyyyyyyxx"
                            },
                            "principal": {
                                "asset": {
                                    "hostname": "test3",
                                    "ip": [
                                        "00.0.0.00"
                                    ],
                                    "mac": [
                                        "00:00:00:0b:c9:11"
                                    ]
                                },
                                "hostname": "test3",
                                "ip": [
                                    "x.x.0.x"
                                ],
                                "mac": [
                                    "00:00:00:0b:c9:11"
                                ],
                                "port": 18985
                            },
                            "rawLogData": {
                                "action": "yyyyyy",
                                "decodedString": "yyyyyy",
                                "external_id": "yyyyyy",
                                "matching_status": "yyyyyy",
                                "severity": "yyyyyy",
                                "source": "yyyyyy"
                            },
                            "securityResult": [
                                {
                                    "action": [
                                        "ALLOW"
                                    ]
                                }
                            ],
                            "target": {
                                "asset": {
                                    "hostname": "youtube.com"
                                },
                                "hostname": "youtube.com",
                                "port": 4548
                            }
                        }
                    }
                ]
            }
        ],
        "createdTime": "2023-10-04T22:16:22.145254Z",
        "detection": [
            {
                "alertState": "ALERTING",
                "riskScore": 40,
                "ruleId": "yyyx-f66d-yyyx-yyyx-yyyx",
                "ruleLabels": [
                    {
                        "key": "priority",
                        "value": "Medium"
                    },
                    {
                        "key": "severity",
                        "value": "Medium"
                    }
                ],
                "ruleName": "dns_not_google",
                "ruleType": "SINGLE_EVENT",
                "ruleVersion": "yyyx-yyyx-yyyx-b682-yyyx@yyyx",
                "urlBackToProduct": "https://unotest2.backstory-dev.chronicle.yyyx/alert?yyyx=yyyx-e380-yyyx-d29c-yyyx"
            }
        ],
        "detectionTime": "2023-10-04T21:18:44Z",
        "id": "yyyx-e380-yyyx-yyyx-yyyx",
        "timeWindow": {
            "endTime": "2023-10-04T21:18:44Z",
            "startTime": "2023-10-04T21:18:44Z"
        },
        "type": "RULE_DETECTION"
    }
    

##### Output messages

The **Get Detection Details** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched information about the detection with ID DETECTION_ID in Google Chronicle.` | The action succeeded.  
`Error executing action "Get Detection Details". Reason: ERROR_REASON` | The action failed. Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Get Detection Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Reference Lists

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **Get Reference Lists** action to retrieve available reference lists in Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Reference Lists** action requires the following parameters:

Parameter | Description  
---|---  
`Filter Key` | The key to filter by. The possible values are as follows:

  * `Name`
  * `Content Type`
  * `Description`

  
`Filter Logic` | The filter logic to apply. The possible values are as follows:
* `Equal` (for exact matches)
* `Contains`(for substring matches)
The default value is `Equal`.  
`Filter Value` | The value to use in the filter. The possible values are as follows:
* `Equal` (for exact matches)
* `Contains`(for substring matches)
`Equal` works with `Title` parameter, while `Contains` works with all values in response. If no value is provided, the filter isn't applied.  
`Expanded Details` | If selected, the action returns detailed information about the reference lists. Not enabled by default.  
`Max Reference Lists To Return` | The number of reference lists to return. The default value is `100`.  
  
#### Action outputs

The **Get Reference List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment  | Not available   
Case wall link  | Not available   
Case wall table  | Available   
Enrichment table  | Not available   
JSON result  | Available   
Output messages  | Available   
Script result  | Available   
  
##### Case wall table

On a Case Wall, the **Get Reference Lists** provides the following table:

Name: **Available Reference Lists**

Columns:

  * **Name**
  * **Description**
  * **Type**



##### JSON result

The following example describes the JSON result output received when using the **Get Reference Lists** action with Backstory API:
    
    
    {
       "name": "list_name",
       "description": "description of the list",
       "lines": [
           "192.0.2.0/24",
           "198.51.100.0/24"
       ],
       "create_time": "2020-11-20T17:18:20.409247Z",
       "content_type": "CIDR"
    }
    

The following example describes the JSON result output received when using the **Get Reference Lists** action with Chronicle API:
    
    
    [
      {
        "name": "projects/PROJECT_ID/locations/us/instances/INSTANCE_ID/referenceLists/REFERENCE_LIST_ID",
        "displayName": "REFERENCE_LIST_ID",
        "revisionCreateTime": "2025-01-09T15:53:10.851775Z",
        "description": "Test reference list",
        "syntaxType": "REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING",
        "scopeInfo": {
          "referenceListScope": {}
        },
        "createTime": "2025-01-09T15:53:10.851775Z"
      }
    ]
    
    

##### Output messages

The **Get Reference Lists** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found reference lists for the provided criteria in Google Chronicle.` `The filter was not applied because parameter "Filter Value" has an empty value.` | The action succeeded.   
`Error executing action ACTION_NAME. Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
`Error executing action ACTION_NAME. Reason: "Invalid value was provided for "Max Reference Lists to Return": PROVIIDED_VALUE. Positive number should be provided.` | The action failed. Check the value for the `Max Reference Lists to Return` parameter.  
  
##### Script

The following table describes the values for the script result output when using the **Get Reference Lists** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Rule Details

Use the **Get Rule Details** action to retrieve information about a rule in Google SecOps.

This action doesn't run on Google SecOps entities. 

**Note:** Information regarding curated rules can only be retrieved using the Chronicle API and may require specific permissions.

#### Action inputs

The **Get Rule Details** action requires the following parameters:

Parameter | Description  
---|---  
`Rule ID` | Required. The unique ID of the rule for which to fetch details. The default value is `[Alert.rule_id]`.  
  
#### Action outputs

The **Get Rule Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Get Rule Details** action with Backstory API:
    
    
    {
        "ruleId": "ru_e6abfcb5-1b85-41b0-b64c-695b3250436f",
        "versionId": "ru_e6abfcb5-1b85-41b0-b64c-695b3250436f@v_1602631093_146879000",
        "ruleName": "SampleRule",
        "metadata": {
          "description": "Sample Description of the Rule",
          "author": "author@example.com"
        },
        "ruleText": "rule SampleRule {
            meta:
              description = \"Sample Description of the Rule\"
              author = \"author@example.com\"
            events:
              // This will just generate lots of detections
              $event.metadata.event_type = \"NETWORK_HTTP\"
            condition:
              $event
            } ",
        "liveRuleEnabled": true,
        "versionCreateTime": "2020-10-13T23:18:13.146879Z",
        "compilationState": "SUCCEEDED"
      }
    

The following example describes the JSON result output received when using the **Get Rule Details** action with Chronicle API:
    
    
    {
        "name": "projects/PROJECT_ID/locations/us/instances/INSTANCE_ID/rules/RULE_ID",
        "revisionId": "v_1733917896_973567000",
        "displayName": "Test_rule_SingleEvent",
        "text": "rule Test_rule_SingleEvent {\n  // This rule matches single events. Rules can also match multiple events within\n  // some time window. For details about how to write a multi-event rule, see\n  // URL\n\n  meta:\n    // Allows for storage of arbitrary key-value pairs of rule details - who\n    // wrote it, what it detects on, version control, etc.\n    // The \"author\" and \"severity\" fields are special, as they are used as\n    // columns on the rules dashboard. If you want to sort based on\n    // these fields on the dashboard, make sure to add them here.\n    // Severity value, by convention, should be \"Low\", \"Medium\" or \"High\"\n    author = \"example_user\"\n    description = \"windowed single event example rule\"\n    //severity = \"Medium\"\n\n  events:\n    $e.metadata.event_type = \"USER_LOGIN\"\n    $e.principal.user.userid = $user\n\n  //outcome:\n    // For a multi-event rule an aggregation function is required\n    // e.g., risk_score = max(0)\n    // See URL\n    //$risk_score = 0\n  match:\n    $user over 1m\n\n  condition:\n    #e > 0\n}\n",
        "author": "example_user",
        "metadata": {
            "author": "example_user",
            "description": "windowed single event example rule",
            "severity": null
        },
        "createTime": "2024-12-11T11:36:18.192127Z",
        "revisionCreateTime": "2024-12-11T11:51:36.973567Z",
        "compilationState": "SUCCEEDED",
        "type": "SINGLE_EVENT",
        "allowedRunFrequencies": [
            "LIVE",
            "HOURLY",
            "DAILY"
        ],
        "etag": "CMj55boGEJjondAD",
        "ruleId": "RULE_ID",
        "versionId": "RULE_ID@v_1733917896_973567000",
        "ruleName": "Test_rule_SingleEvent",
        "ruleText": "rule Test_rule_SingleEvent {\n  // This rule matches single events. Rules can also match multiple events within\n  // some time window. For details about how to write a multi-event rule, see\n  // URL\n\n  meta:\n    // Allows for storage of arbitrary key-value pairs of rule details - who\n    // wrote it, what it detects on, version control, etc.\n    // The \"author\" and \"severity\" fields are special, as they are used as\n    // columns on the rules dashboard. If you want to sort based on\n    // these fields on the dashboard, make sure to add them here.\n    // Severity value, by convention, should be \"Low\", \"Medium\" or \"High\"\n    author = \"example_user\"\n    description = \"windowed single event example rule\"\n    //severity = \"Medium\"\n\n  events:\n    $e.metadata.event_type = \"USER_LOGIN\"\n    $e.principal.user.userid = $user\n\n  //outcome:\n    // For a multi-event rule an aggregation function is required\n    // e.g., risk_score = max(0)\n    // See URL\n    //$risk_score = 0\n  match:\n    $user over 1m\n\n  condition:\n    #e > 0\n}\n",
        "ruleType": "SINGLE_EVENT",
        "versionCreateTime": "2024-12-11T11:51:36.973567Z"
    }
    

##### Output messages

The **Get Rule Details** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched information about the rule with ID RULE_ID in Google Chronicle.` | The action succeeded.   
`Error executing action "Get Rule Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Get Rule Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Is CIDR In Data Table

Use the **Is CIDR In Data Table** to check if specific CIDR values are found in a specific data table in Google SecOps.

This action doesn't run on Google SecOps entities. 

**Note:** This action only works with Chronicle API authentication. Backstory API isn't supported. 

If you are using a Unified SecOps deployment, ensure you have configured a dedicated service account and provided credentials in the integration parameters.

#### Action inputs

The **Is CIDR In Data Table** action requires the following parameters:

Parameter | Description  
---|---  
`Data Table Name` | Required. The display name of the data table to search.  
`Column` | Optional. A comma-separated list of columns to search within the data table. If you don't provide a value, the action searches all columns.  
`CIDR` | Required. The comma-separated list of CIDR values to search for in the data table.  
`Max Data Table Rows To Return` | Required. The number of data table rows to return for every matched value. The maximum value is `1000`. The default value is `1000`.  
  
#### Action outputs

The **Is CIDR In Data Table** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment  | Not available   
Case wall link  | Not available   
Case wall table  | Not available   
Enrichment table  | Not available   
JSON result  | Available   
Output messages  | Available   
Script result  | Available   
  
##### JSON result

The following example describes the JSON result output received when using the **Is CIDR In Data Table** action:
    
    
    [{
       "Entity": "asda",
       "EntityResult": {
           "is_found": true,
           "matched_rows": [
               {
                   "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/dataTables/data_table/dataTableRows/840d18a85944833e1b97ed6d2fb11377",
                   "values": {
                       "columnName1": "asda",
                       "columnName2": "asdasd",
                       "columnName3": "zxczxc"
                   },
                   "createTime": "2025-05-14T12:52:51.908143Z",
                   "updateTime": "2025-05-14T12:52:51.908143Z"
               }
           ]
       }
    }]
    

##### Output messages

The **Is CIDR In Data Table** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully searched provided CIDR values in the data table DATA_TABLE_NAME in Google SecOps` | The action succeeded.  
`Error executing action "Is CIDR In Data Table". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Is CIDR In Data Table** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Is Value In Data Table

Use the **Is Value In Data Table** to check if provided values are in a data table in Google SecOps.

This action doesn't run on Google SecOps entities. 

**Note:** This action only works with Chronicle API authentication. Backstory API is not supported. If you are using a Unified SecOps deployment, ensure you have configured a dedicated service account and provided credentials in the integration parameters.

#### Action inputs

The **Is Value In Data Table** action requires the following parameters:

Parameter | Description  
---|---  
`Data Table Name` | Required. The display name of the data table to search.  
`Column` | Optional. A comma-separated list of columns to search. If no value is provided, the action searches all columns.  
`Values` | Required. A comma-separated list of values to search for.  
`Case Insensitive Search` | Optional. If selected, the search is case-insensitive. Enabled by default.  
`Max Data Table Rows To Return` | Required. The number of data table rows to return per matched value. The maximum value is `1000`.  
  
#### Action outputs

The **Is Value In Data Table** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment  | Not available   
Case wall link  | Not available   
Case wall table  | Not available   
Enrichment table  | Not available   
JSON result  | Available   
Output messages  | Available   
Script result  | Available   
  
##### JSON result

The following example describes the JSON result output received when using the **Is Value In Data Table** action:
    
    
    [{
      "Entity": "asda",
      "EntityResult": {
          "is_found": true,
          "matched_rows": [
              {
                  "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/dataTables/data_table/dataTableRows/840d18a85944833e1b97ed6d2fb11377",
                  "values": {
                      "columnName1": "asda",
                      "columnName2": "asdasd",
                      "columnName3": "zxczxc"
                  },
                  "createTime": "2025-05-14T12:52:51.908143Z",
                  "updateTime": "2025-05-14T12:52:51.908143Z"
              }
          ]
      }
    }]
    

##### Output messages

The **Is Value In Data Table** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully searched provided values in the data table DATA_TABLE_NAME in Google SecOps.` | The action succeeded.   
Error executing action "Is Value In Data Table". Reason: ERROR_REASON | The action failed. Check the connection to the server, the input parameters, or the credentials.  
`Error executing action "Is Value In Data Table". Reason: the following data tables were not found in: DATA_TABLE_NAME: COLUMN_NAMES. Please check the spelling.` | The action failed.  
`Error executing action "Is Value In Data Table". Reason: This action isn't supported for Backstory API configuration. Please update the integration configuration.` | The action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Is Value In Data Table** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Is Value In Data Table Async

Use the **Is Value In Data Table Async** action to check if provided values are found in a data table in Google SecOps asynchronously using long-running search operations.

This action doesn't run on Google SecOps entities. 

**Note:** This is an asynchronous action. Adjust the script timeout value in the Google SecOps IDE for the action as needed. 

This action only works with Chronicle API authentication. Backstory API isn't supported. If you're using a Unified SecOps deployment, make sure you have configured a dedicated service account and provided credentials in the integration parameters.

#### Action inputs

The **Is Value In Data Table Async** action requires the following parameters:

Parameter | Description  
---|---  
`Data Table Name` | Required. The display name of the data table to search.  
`Column` | Optional. A comma-separated list of columns to search within the data table. If no value is provided, the action searches all columns.  
`Values` | Required. A comma-separated list of values to search for inside the data table.  
`Case Insensitive Search` | Optional. If selected, the search is case-insensitive. Enabled by default.  
`Max Data Table Rows To Return` | Required. The number of data table rows to return for every matched value. The maximum value is `1000`. The default value is `1000`.  
  
#### Action outputs

The **Is Value In Data Table Async** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment  | Not available   
Case wall link  | Not available   
Case wall table  | Not available   
Enrichment table  | Not available   
JSON result  | Available   
Output messages  | Available   
Script result  | Available   
  
##### JSON result

The following example describes the JSON result output received when using the **Is Value In Data Table Async** action:
    
    
    [
      {
        "Entity": "example_value",
        "EntityResult": {
          "is_found": true,
          "matched_rows": [
            {
              "createTime": "",
              "name": "projects/{project_id}/locations/{location}/instances/{instance_id}/dataTables/{table_id}/dataTableRows/{row_id}",
              "updateTime": "",
              "values": {
                "columnName1": "example_value",
                "columnName2": "sample_data"
              }
            }
          ]
        }
      }
    ]
    

##### Output messages

The **Is Value In Data Table Async** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully searched provided values in the data table DATA_TABLE_NAME.` `No provided values were found in the data table DATA_TABLE_NAME.` | The action succeeded.   
`Error executing action "Is Value In Data Table Async". Reason: ERROR_REASON.` | The action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Is Value In Data Table Async** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Is Value In Reference List

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **Is Value In Reference List** action to check if provided values are found in reference lists in Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Is Value In Reference List** action requires the following parameters:

Parameter | Description  
---|---  
`Reference List Names` | Required. A comma-separated list of reference list names to search.  
`Values` | Required. A comma-separated list of values to search for.  
`Case Insensitive Search` | Optional. If selected, the search is case-insensitive.  
  
#### Action outputs

The **Is Value In Reference List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment  | Not available   
Case wall link  | Not available   
Case wall table  | Not available   
Enrichment table  | Not available   
JSON result  | Available   
Output messages  | Available   
Script result  | Available   
  
##### JSON result

The following example describes the JSON result output received when using the **Is Value In Reference List** action with Backstory API:
    
    
    {
        "Entity": "example.com",
        "EntityResult": {
            "found_in": [
                "Reference list names, where item was found"
            ],
            "not_found_in": [
                "Reference list names, where items wasn't found"
            ],
            "overall_status": "found, if at least one reference list had the value/not found, if non of the reference lists found the value"
        }
    }
    
    

The following example describes the JSON result output received when using the **Is Value In Reference List** action with Chronicle API:
    
    
    {
        "Entity": "example.com",
        "EntityResult": {
            "found_in": [
                "Reference list names, where item was found"
            ],
            "not_found_in": [
                "Reference list names, where items wasn't found"
            ],
            "overall_status": "found, if at least one reference list had the value/not found, if non of the reference lists found the value"
        }
    }
    

##### Output messages

The **Is Value In Reference List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully searched provided values in the reference lists in Google Chronicle.` | The action succeeded.   
Error executing action "Is Value In Reference List". Reason: ERROR_REASON | The action failed. Check the connection to the server, the input parameters, or the credentials.  
`Error executing action "Is Value In Reference List". Reason: the following reference lists were not found in Google Chronicle: MISSING_REFERENCE_LIST_NAME(S). Please use the action "Get Reference Lists" to see what reference lists are available.` | The action failed.Run the **Get Reference Lists** action to check for available lists.  
  
##### Script result

The following table describes the values for the script result output when using the **Is Value In Reference List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List Assets

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **List Assets** action to list assets in Google SecOps based on related entities within a specified time period.

This action only supports the `MD5`, `SHA-1`, and `SHA-256` hashes.

This action runs on the following Google SecOps entities:

  * `URL`
  * `IP Address`
  * `Hash`



#### Action inputs

The **List Assets** action requires the following parameters:

Parameter | Description  
---|---  
`Max Hours Backwards` | The number of hours prior to now to fetch the assets. The default value is `1`.  
`Create Insight` | If selected, the action creates an insight with information about the entities.Enabled by default.  
`Max Assets To Return` | The number of assets to return.The default value is `50`.  
`Time Frame` | Optional. A period to retrieve the results for. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Alert Time Till Now`
  * `5 Minutes Around Alert Time`
  * `30 Minutes Around Alert Time`
  * `1 Hour Around Alert Time`
  * `Custom`

If `Custom` is selected, the `Start Time` parameter is required. The default value is `Last Hour`.  
`Start Time` | The start time in ISO 8601 format. This parameter is required if the `Time Frame` parameter is set to `Custom`.  
`End Time` | The end time in ISO 8601 format. If you don't set a value and set the `Time Frame` parameter to `Custom`, the current time is used.  
  
#### Action outputs

The **List Assets** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

Name: ENTITY_IDENTIFIER

Columns:

  * **Hostname**
  * **IP Address**
  * **First Seen Artifact**
  * **Last Seen Artifact**



##### JSON result

The following example describes the JSON result output received when using the **List Assets** action with Backstory API:
    
    
    {
        "assets": [
          {
            "asset": {
              "hostname": "example"
            },
            "firstSeenArtifactInfo": {
              "artifactIndicator": {
                "domainName": "www.example.com"
              },
              "seenTime": "2020-02-28T09:18:15.675Z"
            },
            "lastSeenArtifactInfo": {
              "artifactIndicator": {
                "domainName": "www.example.com"
              },
              "seenTime": "2020-09-24T06:43:59Z"
            }
          }
        ],
        "uri": [
          "https://INSTANCE/domainResults?domain=www.example.com&selectedList=DomainViewDistinctAssets&whoIsTimestamp=2020-09-27T12%3A07%3A34.166830443Z"
        ]
      }
    

The following example describes the JSON result output received when using the **List Assets** action with Chronicle API:
    
    
    [
      {
        "Entity": "192.0.2.229",
        "EntityResult": {
          "assets": [
            {
              "artifactIndicator": {
                "domain": "example.com"
              },
              "sources": [
                "Mandiant Open Source Intelligence"
              ],
              "categories": [
                "Indicator was published in publicly available sources"
              ],
              "assetIndicators": [
                {
                  "assetIpAddress": "192.0.2.229"
                }
              ],
              "iocIngestTimestamp": "2024-09-20T14:14:07.843Z",
              "firstSeenTimestamp": "2025-01-15T11:20:00Z",
              "lastSeenTimestamp": "2025-01-15T11:20:00Z",
              "filterProperties": {
                "stringProperties": {
                  "TLD": {
                    "values": [
                      {
                        "rawValue": ".com"
                      }
                    ]
                  },
                  "IOC FEED": {
                    "values": [
                      {
                        "rawValue": "Mandiant Open Source Intelligence"
                      }
                    ]
                  },
                  "IOC CATEGORIES": {
                    "values": [
                      {
                        "rawValue": "Indicator was published in publicly available sources"
                      }
                    ]
                  },
                  "IOC CONFIDENCE SCORE": {
                    "values": [
                      {
                        "rawValue": "High"
                      }
                    ]
                  },
                  "IOC/ALERT SEVERITY": {
                    "values": [
                      {
                        "rawValue": "Medium"
                      }
                    ]
                  }
                }
              },
              "confidenceBucket": "High",
              "rawSeverity": "Medium",
              "logType": "OPEN_SOURCE_INTEL_IOC",
              "confidenceScore": 100,
              "globalCustomerId": "ID",
              "confidenceScoreBucket": {
                "rangeEnd": 100
              },
              "categorization": "Indicator was published in publicly available sources",
              "domainAndPorts": {
                "domain": "example.com"
              },
              "activeTimerange": {
                "startTime": "1970-01-01T00:00:01Z",
                "endTime": "9999-12-31T23:59:59Z"
              },
              "feedName": "MANDIANT",
              "id": "ID",
              "fieldAndValue": {
                "value": "ex  ",
                "valueType": "DOMAIN_NAME"
              }
            },
            {
              "artifactIndicator": {
                "domain": "example.com"
              },
              "sources": [
                "Mandiant Active Breach Intelligence"
              ],
              "categories": [
                "Indicator was published in publicly available sources"
              ],
              "assetIndicators": [
                {
                  "assetIpAddress": "192.0.2.229"
                }
              ],
              "iocIngestTimestamp": "2023-07-05T02:42:52.935Z",
              "firstSeenTimestamp": "2025-01-15T11:20:00Z",
              "lastSeenTimestamp": "2025-01-15T11:20:00Z",
              "filterProperties": {
                "stringProperties": {
                  "IOC/ALERT SEVERITY": {
                    "values": [
                      {
                        "rawValue": "Medium"
                      }
                    ]
                  },
                  "IOC CONFIDENCE SCORE": {
                    "values": [
                      {
                        "rawValue": "High"
                      }
                    ]
                  },
                  "IOC FEED": {
                    "values": [
                      {
                        "rawValue": "Mandiant Active Breach Intelligence"
                      }
                    ]
                  },
                  "IOC CATEGORIES": {
                    "values": [
                      {
                        "rawValue": "Indicator was published in publicly available sources"
                      }
                    ]
                  },
                  "TLD": {
                    "values": [
                      {
                        "rawValue": ".com"
                      }
                    ]
                  }
                }
              },
              "confidenceBucket": "High",
              "rawSeverity": "Medium",
              "logType": "MANDIANT_ACTIVE_BREACH_IOC",
              "confidenceScore": 100,
              "globalCustomerId": "ID",
              "confidenceScoreBucket": {
                "rangeEnd": 100
              },
              "categorization": "Indicator was published in publicly available sources",
              "domainAndPorts": {
                "domain": "example.com"
              },
              "activeTimerange": {
                "startTime": "1970-01-01T00:00:01Z",
                "endTime": "9999-12-31T23:59:59Z"
              },
              "feedName": "MANDIANT",
              "id": "ID",
              "fieldAndValue": {
                "value": "example.com",
                "valueType": "DOMAIN_NAME"
              }
            }
          ],
          "uri": "https://INSTANCE.backstory.chronicle.security/destinationIpResults?ADDRESS=192.0.2.229&selectedList=IpViewDistinctAssets&referenceTime=2025-01-23T11%3A16%3A24.517449Z"
        }
      }
    ]
    

##### Output messages

The **List Assets** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully listed related assets for the following entities from Google Chronicle: ENTITY_IDENTIFIER` | The action succeeded.  
`Error executing action "List Assets". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **List Assets** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List Events

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **List Events** action to list events on a particular asset within a specified time period.

This action can only retrieve 10,000 events.

This action runs on the following Google SecOps entities:

  * `IP address`
  * `MAC address`
  * `Hostname`



#### Action inputs

The **List Events** action requires the following parameters:

Parameter | Description  
---|---  
`Event Types` | A comma-separated list of event types. If no value is provided, all event types are fetched. For a list of all possible values, see Event type possible values.  
`Time Frame` | The specified time period. We recommend keeping it as small as possible for better results. If `Custom` is selected, the `Start Time` parameter is required. If `Max Hours Backwards` is selected, it provides a time filter and ensures backwards compatibility. The possible values are as follows:

  * `Max Hours Backwards`
  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

The default value is `Custom`.  
`Start Time` | The start time in ISO 8601 format. This parameter is required if the `Time Frame` parameter is set to `Custom`.  
`End Time` | The end time in ISO 8601 format. If no value is provided and the `Time Frame` parameter is set to `Custom`, the current time is used. This parameter accepts the `now` value.  
`Reference Time` | The reference time for the event search. If no value is provided, the action uses the end time as the reference.  
`Output` | Required. The output format. The possible values are as follows:

  * `Events + Statistics`
  * `Only Events`
  * `Only Statistics`

  
`Max Events To Return` | The number of events to process for each entity type. The default value is `100`.  
  
##### Event type possible values

The possible values for the `Event Type` parameter are as follows: 

  * `EVENTTYPE_UNSPECIFIED`
  * `PROCESS_UNCATEGORIZED`
  * `PROCESS_LAUNCH`
  * `PROCESS_INJECTION`
  * `PROCESS_PRIVILEGE_ESCALATION`
  * `PROCESS_TERMINATION`
  * `PROCESS_OPEN`
  * `PROCESS_MODULE_LOAD`
  * `REGISTRY_UNCATEGORIZED`
  * `REGISTRY_CREATION`
  * `REGISTRY_MODIFICATION`
  * `REGISTRY_DELETION`
  * `SETTING_UNCATEGORIZED`
  * `SETTING_CREATION`
  * `SETTING_MODIFICATION`
  * `SETTING_DELETION`
  * `MUTEX_UNCATEGORIZED`
  * `MUTEX_CREATION`
  * `FILE_UNCATEGORIZED`
  * `FILE_CREATION`
  * `FILE_DELETION`
  * `FILE_MODIFICATION`
  * `FILE_READ`
  * `FILE_COPY`
  * `FILE_OPEN`
  * `FILE_MOVE`
  * `FILE_SYNC`
  * `USER_UNCATEGORIZED`
  * `USER_LOGIN`
  * `USER_LOGOUT`
  * `USER_CREATION`
  * `USER_CHANGE_PASSWORD`
  * `USER_CHANGE_PERMISSIONS`
  * `USER_STATS`
  * `USER_BADGE_IN`
  * `USER_DELETION`
  * `USER_RESOURCE_CREATION`
  * `USER_RESOURCE_UPDATE_CONTENT`
  * `USER_RESOURCE_UPDATE_PERMISSIONS`
  * `USER_COMMUNICATION`
  * `USER_RESOURCE_ACCESS`
  * `USER_RESOURCE_DELETION`
  * `GROUP_UNCATEGORIZED`
  * `GROUP_CREATION`
  * `GROUP_DELETION`
  * `GROUP_MODIFICATION`
  * `EMAIL_UNCATEGORIZED`
  * `EMAIL_TRANSACTION`
  * `EMAIL_URL_CLICK`
  * `NETWORK_UNCATEGORIZED`
  * `NETWORK_FLOW`
  * `NETWORK_CONNECTION`
  * `NETWORK_FTP`
  * `NETWORK_DHCP`
  * `NETWORK_DNS`
  * `NETWORK_HTTP`
  * `NETWORK_SMTP`
  * `STATUS_UNCATEGORIZED`
  * `STATUS_HEARTBEAT`
  * `STATUS_STARTUP`
  * `STATUS_SHUTDOWN`
  * `STATUS_UPDATE`
  * `SCAN_UNCATEGORIZED`
  * `SCAN_FILE`
  * `SCAN_PROCESS_BEHAVIORS`
  * `SCAN_PROCESS`
  * `SCAN_HOST`
  * `SCAN_VULN_HOST`
  * `SCAN_VULN_NETWORK`
  * `SCAN_NETWORK`
  * `SCHEDULED_TASK_UNCATEGORIZED`
  * `SCHEDULED_TASK_CREATION`
  * `SCHEDULED_TASK_DELETION`
  * `SCHEDULED_TASK_ENABLE`
  * `SCHEDULED_TASK_DISABLE`
  * `SCHEDULED_TASK_MODIFICATION`
  * `SYSTEM_AUDIT_LOG_UNCATEGORIZED`
  * `SYSTEM_AUDIT_LOG_WIPE`
  * `SERVICE_UNSPECIFIED`
  * `SERVICE_CREATION`
  * `SERVICE_DELETION`
  * `SERVICE_START`
  * `SERVICE_STOP`
  * `SERVICE_MODIFICATION`
  * `GENERIC_EVENT`
  * `RESOURCE_CREATION`
  * `RESOURCE_DELETION`
  * `RESOURCE_PERMISSIONS_CHANGE`
  * `RESOURCE_READ`
  * `RESOURCE_WRITTEN`
  * `ANALYST_UPDATE_VERDICT`
  * `ANALYST_UPDATE_REPUTATION`
  * `ANALYST_UPDATE_SEVERITY_SCORE`
  * `ANALYST_UPDATE_STATUS`
  * `ANALYST_ADD_COMMENT`



#### Action outputs

The **List Events** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **List Events** action:
    
    
    {
        "statistics": {
    "NETWORK_CONNECTION": 10
    }
    {
        "events": [
          {
            "metadata": {
              "eventTimestamp": "2020-09-28T14:20:00Z",
              "eventType": "NETWORK_CONNECTION",
              "productName": "EXAMPLE Name",
              "productEventType": "NETWORK_DNS",
              "ingestedTimestamp": "2020-09-28T16:28:11.615578Z"
            },
            "principal": {
              "hostname": "user-example-pc",
              "assetId": "EXAMPLE:user-example-pc",
              "process": {
                "pid": "1101",
                "productSpecificProcessId": "EXAMPLE:32323"
              }
            },
            "target": {
              "hostname": "example.com",
              "user": {
                "userid": "user"
              },
              "process": {
                "pid": "8172",
                "file": {
                  "md5": "a219fc7fcc93890a842183388f80369e",
                  "fullPath": "C:\\Program Files(x86)\\adobe\\acrobat reader dc\\reader\\acrord32.exe"
                },
                "commandLine": "\"C:\\Program Files(x86)\\adobe\\acrobat reader dc\\reader\\acrord32.exe\" ...",
                "productSpecificProcessId": "EXAMPLE:82315"
              }
            }
          },
          {
            "metadata": {
              "eventTimestamp": "2020-09-28T17:20:00Z",
              "eventType": "NETWORK_CONNECTION",
              "productName": "EXAMPLE Name",
              "productEventType": "NETWORK_DNS",
              "ingestedTimestamp": "2020-09-28T16:28:11.615578Z"
            },
            "principal": {
              "hostname": "user-example-pc",
              "assetId": "EXAMPLE:user-example-pc",
              "process": {
                "pid": "1101",
                "productSpecificProcessId": "EXAMPLE:32323"
              }
            },
            "target": {
              "hostname": "example.com",
              "user": {
                "userid": "user"
              },
              "process": {
                "pid": "8172",
                "file": {
                  "md5": "a219fc7fcc93890a842183388f80369e",
                  "fullPath": "C:\\Program Files(x86)\\adobe\\acrobat reader dc\\reader\\acrord32.exe"
                },
                "commandLine": "\"C:\\Program Files(x86)\\adobe\\acrobat reader dc\\reader\\acrord32.exe\" ...",
                "productSpecificProcessId": "EXAMPLE:82315"
              }
            }
          }
        ],
        "uri": [
          "https://INSTANCE/assetResults?assetIdentifier=user-example-pc&referenceTime=2020-09-28T17%3A00%3A00Z&selectedList=AssetViewTimeline&startTime=2020-09-28T14%3A20%3A00Z&endTime=2020-09-28T20%3A20%3A00Z"
        ]
      }
    }
    

##### Output messages

The **List Events** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully listed related events for the following entities from Google Chronicle: ENTITY_IDENTIFIER` | The action succeeded.  
`Error executing action "List Events". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
`Error executing action "List Events". Reason: invalid event type is provided. Please check the spelling. Supported event types: SUPPORTED_EVENT_TYPES` |  The action failed. Check the spelling.  
  
##### Script result

The following table describes the values for the script result output when using the **List Events** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List IOCs

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **List IOCs** action to list all IoCs discovered in your enterprise within a specified time range.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List IOCs** action requires the following parameters:

Parameter | Description  
---|---  
`Start Time` | The start time for the results in ISO 8601 format.  
`Max IoCs to Fetch` | The maximum number of IoCs to return. The range is `1` \- `10,000`. The default value is `50`.  
  
#### Action outputs

The **List IOCs** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

Columns:

  * **Domain**
  * **Category**
  * **Source**
  * **Confidence**
  * **Severity**
  * **IoC Ingest Time**
  * **IoC First Seen Time**
  * **IoC Last Seen Time**
  * **URI**



##### JSON result

The following example describes the JSON result output received when using the **List IOCs** action:
    
    
    {
       "matches":[
          {
             "artifact":{
                "domainName":"www.example.com"
             },
             "firstSeenTime":"2018-05-25T20:47:11.048998Z",
             "iocIngestTime":"2019-08-14T21:00:00Z",
             "lastSeenTime":"2019-10-24T16:19:46.880830Z",
             "sources":[
                {
                   "category":"Spyware Reporting Server",
                   "confidenceScore":{
                      "intRawConfidenceScore":0,
                      "normalizedConfidenceScore":"Low"
                   },
                   "rawSeverity":"Medium",
                   "source":"Example List"
                }
             ],
             "uri":["URI"]
          }
       ],
       "moreDataAvailable":true
    }
    

##### Output messages

The **List IOCs** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully listed IOCs from the provided timeframe in Google Chronicle.` | The action succeeded.  
`Error executing action "List IOCs". Reason: ERROR_REASON.` | The action failed. Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **List IOCs** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Lookup Similar Alerts

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **Lookup Similar Alerts** action to search for similar alerts in Google SecOps.

**Important:** This action only works with Google SecOps alerts received from the **Chronicle Alerts Connector**.

#### Action inputs

The **Lookup Similar Alerts** action requires the following parameters:

Parameter | Description  
---|---  
`Time Frame` | The time period for the results. To get the best results, keep the timeframe as narrow as possible. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Alert Time Till Now`: Searches for events from the start time of the alert to `End Time`.
  * `5 Minutes Around Alert Time`: Searches for events 5 minutes before and after the alert's creation time.
  * `30 Minutes Around Alert Time`: Searches for events 30 minutes before and after the alert's creation time.
  * `1 Hour Around Alert Time`
: Searches for events 1 hour before and after the alert's creation time.
  
`IOCs / Assets` | Required. A comma-separated list of IoCs or assets to find in the alerts. The action performs a separate search for each provided item.  
`Similarity By` | The attributes to use for finding similar alerts. The possible values are as follows:

  * `Alert Name, Alert Type and Product`
  * `Alert Name and Alert Type`
  * `Product`
  * `Only IOCs/Assets`
For more information on this parameter's behavior.
The default value is `Alert Name, Alert Type and Product`.  
  
#### How the Similarity By parameter works

The `Similarity By` parameter applies differently to Rule alerts and External alerts.

  * If `Alert Name, Alert Type and Product` or `Alert Name, Alert Type` is selected:

    * For External alerts, the action searches for other External alerts that have the same name.

    * For Rule alerts, the action processes alerts that originated from the same rule.

  * If `Product` is selected:

    * The action processes alerts that originated from the same product, regardless of whether they are Rule alerts or External alerts.

For example, an alert originating in Crowdstrike will only be matched with other alerts from Crowdstrike.

  * If `Only IOCs/Assets` is selected:

    * The action matches alerts based on the IOCs provided in the `IOCs/Assets` parameter. It searches for these indicators in both Rule alerts and External alerts.

    * An IOC alert can only run this action when this option is selected. If any other option is provided, the action defaults to `Only IOCs/Assets`.




The **Lookup Similar Alerts** action is a versatile tool for analyzing alerts. It enables analysts to correlate alerts from the same time period and extract relevant IOCs to determine if an incident is a true positive.

#### Action outputs

The **Lookup Similar Alerts** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

The **Lookup Similar Alerts** action can return the following links:

  * CBN: GENERATED_LINK_BASED_ON_IU_ROOT_URL
  * Rule: GENERATED_LINK_BASED_ON_IU_ROOT_URL



##### Case wall table

Table name: **IOC/ASSET_IDENTIFIER**

Table columns:

  * **Product**
  * **Hostnames**
  * **IPs**
  * **Users**
  * **Email Addresses**
  * **Subjects**
  * **URLs**
  * **Hashes**
  * **Processes**
  * **First Seen**
  * **Last Seen**
  * **Alert Name**
  * **General**



##### JSON result

The following example describes the JSON result output received when using the **Lookup Similar Alerts** action:
    
    
    {
        "count": 123,
        "distinct": [
            {
                "first_seen": "time of the first alert that matched our conditions",
                "last_seen": "time of the last alert that matched our conditions",
                "product_name": "product name",
                "used_ioc_asset": "what user provided in the parameter IOCs and Assets",
                "name": "Alert Name/Rule Name",
                "hostnames": "csv list of unique hostnames that were found in alerts",
                "urls": "csv list of unique urls that were found in alerts",
                "ips": "csv list of unique ips that were found in alerts",
                "subjects": "csv list of unique subjects that were found in alerts",
                "users": "csv list of unique users that were found in alerts",
                "email_addresses": "csv list of unique email_addresses that were found in alerts",
                "hashes": "csv list of unique hashes that were found in alerts",
                "processes": "csv list of unique processes that were found in alerts"
                "rule_urls": ["Chronicle URL from API response for Rule"]
                "count": 123
            }
        ],
        "processed_alerts": 10000,
        "run_time": "how long it took to run the action or at least API request",
        "EXTERNAL_url": "Chronicle URL from API response for EXTERNAL"
    
    }
    

##### Output messages

The **Lookup Similar Alerts** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found similar alerts from the provided timeframe in Google Chronicle.` `No similar alerts were found from the provided timeframe in Google Chronicle.` | The action succeeded.  
`Error executing action "Lookup Similar Alerts". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
`Error executing action "Lookup Similar Alerts". Reason: all of the retries are exhausted. Please wait for a minute and try again.` | The action failed. Wait a few minutes before running the action again.  
  
##### Script result

The following table describes the values for the script result output when using the **Lookup Similar Alerts** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to Google SecOps.

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
  
##### Output messages

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Google Chronicle backstory with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Google Chronicle backstory. Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Remove Rows From Data Table

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **Remove Rows From Data Table** action to remove rows from a data table in Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Remove Rows From Data Table** action requires the following parameters:

Parameter | Description  
---|---  
`Data Table Name` | Required. The display name of the data table to update.  
`Rows` | Required. A list of JSON objects used to search for and delete rows. Only include valid columns. The default value is as follows:
    
    
      [
        {
            "columnName1": "value1",
            "columnName2": "value2",        
        },
        {
            "columnName1": "value1",
            "columnName2": "value2",        
        }
      ]
        
  
#### Action outputs

The **Remove Rows From Data Table** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Remove Rows From Data Table** action:
    
    
    {
              "name": "projects/365235532452/locations/us/instances/df6f1958-0381-41f9-8794-08a3229744a5/dataTables/data_table/dataTableRows/840d18a85944833e1b97ed6d2fb11377",
              "values": {
                  "columnName1": "asda",
                  "columnName2": "asdasd",
                  "columnName3": "zxczxc"
              },
              "createTime": "2025-05-14T12:52:51.908143Z",
              "updateTime": "2025-05-14T12:52:51.908143Z"
    }
    

##### Output messages

The **Remove Rows From Data Table** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully removed rows from the data table DATA_TABLE_NAME in Google SecOps.` | The action succeeded.  
`Error executing action "Remove Rows From Data Table". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Remove Rows From Data Table** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Remove Values From Reference List

**Caution:** This action relies on the legacy Backstory API, which will permanently stop working on July 20, 2027. To prevent playbook failures, you must upgrade your Google Chronicle integration to version 54 or higher to use the Chronicle API. Monitor this action's outputs after upgrading, as output formats may change.

Use the **Remove Values From Reference List** action to remove values from a reference list in Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Remove Values From Reference List** action requires the following parameters:

Parameter | Description  
---|---  
`Reference List Name` | Required. The name of the reference list to update.  
`Values` | Required. A comma-separated list of values to remove from the reference list.  
  
#### Action outputs

The **Remove Values From Reference List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Remove Values From Reference List** action with Backstory API:
    
    
    {
       "name": "list_name",
       "description": "description of the list",
       "lines": [
           "192.0.2.0/24",
           "198.51.100.0/24"
       ],
       "create_time": "2020-11-20T17:18:20.409247Z",
       "content_type": "CIDR"
    }
    

The following example describes the JSON result output received when using the **Remove Values From Reference List** action with Chronicle API:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us/instances/INSTANCE_ID/referenceLists/<var class="readonly">REFERENCE_LIST_NAME</var>' }}",
      "displayName": "REFERENCE_LIST_NAME",
      "revisionCreateTime": "2025-01-16T09:15:21.795743Z",
      "description": "Test reference list",
      "entries": [
        {
          "value": "example.com"
        },
        {
          "value": "exampledomain.com"
        }
      ],
      "syntaxType": "REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING",
      "scopeInfo": {
        "referenceListScope": {}
      },
      "createTime": "2025-01-16T09:15:21.795743Z",
      "lines": [
        "example.com",
        "exampledomain.com"
      ]
    }
    

##### Output messages

The **Remove Values From Reference List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully removed values from the reference list.` | The action succeeded.  
`Error executing action "Remove Values From Reference List". Reason: ERROR_REASON` | The action failed. Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Remove Values From Reference List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Google Chronicle - Chronicle Alerts Connector

**Important:** To ensure continued functionality before the legacy API deprecation, you must explicitly configure this connector to use the Chronicle API. Verify that the authentication method applied here matches your integration configuration identically.

Use the **Google Chronicle - Chronicle Alerts Connector** to pull information about rule-based alerts from Google SecOps.

**Note:** This connector can be filtered using a dynamic list.

#### Overview

The **Google Chronicle - Chronicle Alerts Connector** ingests rule-based alerts from Google SecOps. 

Key features and operational details include:

  * Queries data within a one-week period. To prevent missed alerts from indexing delays, a padding period and increased connector timeout can be configured, though significant padding may negatively affect performance.

  * Utilizes dynamic lists for flexible configuration.

  * Provides a `Fallback Severity` for alerts that lack a severity value.

**Note:** The connector ingests data after the `Script Timeout (Seconds)` limit is reached or the `Max Alerts To Fetch` threshold is met. In low-volume alert environments, a high script timeout value can cause a delay because the process remains active while waiting for data. Because optimal settings depend on your specific tenant volume and ingestion requirements, Google recommends testing configurations to balance timeout limits against alert arrival rates.



#### Dynamic list filter

The dynamic list is used to filter alerts directly from the connector configuration page.

##### Operator logic

The dynamic list uses a combination of set-based evaluation and multi-line logic to process filter rules:

  * **Comma-separated values (set evaluation)** : Values on the same line, separated by a comma, are treated as a single set. The logic applied depends on the operator used:

    * **Inclusion (`=`)**: Acts as an allowlist.

Ingests the alert if the value matches any item in the list (for example, `Rule.severity = low,medium` means `low` OR `medium`).

    * **Exclusion (`!=`)**: Acts as a blocklist.

Ingests the alert only if the value matches none of the items in the list (for example, `Rule.ruleName != rule_a,rule_b` means the rule name is NOT `rule_a` AND NOT `rule_b`).

  * **Separate lines (AND logic)** : Each separate line in the dynamic list further restricts the filter (for example, Line 1 AND Line 2).

  * **Supported operators** : (`=`, `!=`, `>`, `<`, `>=`, `<=`) vary depending on the filter key.




The following are examples of using operator rules:

  * **Rule.severity = medium** : The connector only ingests rule alerts with the medium severity.

  * **Rule.severity = low,medium** : The connector only ingests rule alerts with the medium or low severity.

  * **Rule.ruleName != rule_a,rule_b** : The connector ingests all alerts except those where the rule name is `rule_a` or `rule_b`.

  * **Rule.ruleName = default_rule** : The connector only ingests rule alerts with the `default_rule` name.




##### Supported filters

The **Chronicle Alerts Connector** supports filtering on the following keys:

Filter key | Response key | Operators | Possible values  
---|---|---|---  
`Rule.severity` | `detection` or `ruleLabels` or `severity` | `=`, `!=`, `>`, `<`, `>=`, `<=` | `Info`, `Error`, `Low`, `Medium`, `High`, `Critical`. The values are case-insensitive.  
`Rule.ruleName` | `detection` or `ruleName` | `=`, `!=` | Defined by the user.  
`Rule.ruleID` | `detection` or `ruleId` | `=`, `!=` | Defined by the user.  
`Rule.ruleType` | `detection` or `ruleClass` | `=`, `!=` | `curated`, `custom`. The values are case-insensitive.  
`Rule.ruleLabels.{key}` | `detection` or `ruleLabels` | `=`, `!=` | Defined by the user.  
  
##### Handling `ruleLabels`

To filter on a specific label within a rule, use the `Rule.ruleLabels.{key}` format.

For example, to filter on a label with the key `type` and value `suspicious_behaviour`, the dynamic list input should be:

`Rule.ruleLabels.type=suspicious_behaviour`

##### Connector inputs

The **Chronicle Alerts Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required. The name of the field that determines the event name (subtype).  
`Environment Field Name` | Optional. The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | Required. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`API Root` | Required. The API root of the Google SecOps instance. Google SecOps provides regional endpoints for each API, for example, `https://europe-backstory.googleapis.com` or `https://asia-southeast1-backstory.googleapis.com` [Contact Cloud Customer Care](https://docs.cloud.google.com/chronicle/docs/getting-support) to find out which endpoint to use. The default value is `https://backstory.googleapis.com`.  
`User's Service Account` | Required. The full JSON content of the service account used for authentication.  
`Fallback Severity` | Required. The default severity to use if the alert from Google SecOps doesn't include a severity value. The possible values are as follows:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`
  * `Info`

The default value is `Medium`.  
`Max Hours Backwards` | Optional. The number of hours prior to the initial connector run to retrieve incidents from. This parameter applies only once. The maximum value is `168` (one week). The default value is `1`.  
`Max Alerts To Fetch` | Optional. The number of alerts to process in every connector iteration. The default value is `100`.  
`Disable Event Splitting` | Optional. If selected, the connector doesn't split original events into multiple parts, ensuringthe event count matches between the source and Google SecOps SOAR.  Not enabled by default.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Google SecOps server. Enabled by default.  
`Proxy Server Address` | Optional.The address of the proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
`Disable Overflow` | Optional. If selected, the connector ignores the Google SecOps overflow mechanism. Not enabled by default.  
`Validate Dynamic List Entries` | Optional. If enabled, the connector validates that the entries in the Dynamic List exist in the platform before processing to prevent ingestion errors. Not enabled by default.  
  
#### Connector rules

The **Google Chronicle - Chronicle Alerts Connector** supports proxies.

#### Connector events

The following section describes the structure of the events retrieved by the connector. This connector specifically pulls alerts generated by detection rules within Google SecOps.

##### Rule-based alerts

This event type is generated when a detection rule matches incoming log data. The JSON output contains the rule metadata, the unique detection ID, and the associated UDM event data that triggered the alert.
    
    
     {
        "alert_type": "RULE",
        "event_type": "NETWORK_DHCP",
        "type": "RULE_DETECTION",
        "detection": [
            {
                "ruleName": "d3_test",
                "urlBackToProduct": "https://INSTANCE/ruleDetections?ruleId=ru_74dd17e2-5aad-4053-acd7-958bead014f2&selectedList=RuleDetectionsViewTimeline&selectedParentDetectionId=de_b5dadaf4-b398-325f-9f09-833b71b3ffbb&selectedTimestamp=2022-02-08T05:02:36Z&versionTimestamp=2020-11-19T18:19:11.951951Z",
                "ruleId": "ru_74dd17e2-5aad-4053-acd7-958bead014f2",
                "ruleVersion": "ru_74dd17e2-5aad-4053-acd7-958bead014f2@v_1605809951_951951000",
                "alertState": "NOT_ALERTING",
                "ruleType": "SINGLE_EVENT",
                "ruleLabels": [
                    {
                        "key": "author",
                        "value": "analyst123"
                    },
                    {
                        "key": "description",
                        "value": "8:00 AM local time"
                    },
                    {
                        "key": "severity",
                        "value": "Medium"
                    }
                ]
            }
        ],
        "createdTime": "2022-02-08T06:07:33.944951Z",
        "id": "de_b5dadaf4-b398-325f-9f09-833b71b3ffbb",
        "timeWindow": {
            "startTime": "2022-02-08T05:02:36Z",
            "endTime": "2022-02-08T05:02:36Z"
        },
        "collectionElements": [
            {
                "references": [
                    {
                        "event": {
                            "metadata": {
                                "eventTimestamp": "2022-02-08T05:02:36Z",
                                "eventType": "NETWORK_DHCP",
                                "productName": "Infoblox DHCP",
                                "ingestedTimestamp": "2022-02-08T05:03:03.892234Z"
                            },
                            "principal": {
                                "ip": [
                                    "198.51.100.255",
                                    "198.51.100.1"
                                ],
                                "mac": [
                                    "01:23:45:ab:cd:ef"
                                ],
                                "email_address": [
                                    "example@example.com"
                                ]
                            },
                            "target": {
                                "hostname": "dhcp_server",
                                "ip": [
                                    "198.51.100.0",
                                    "198.51.100.1"
                                ]
                            },
                            "network": {
                                "applicationProtocol": "DHCP",
                                "dhcp": {
                                    "opcode": "BOOTREQUEST",
                                    "ciaddr": "198.51.100.255",
                                    "giaddr": "198.51.100.0",
                                    "chaddr": "01:23:45:ab:cd:ef",
                                    "type": "REQUEST",
                                    "clientHostname": "example-user-pc",
                                    "clientIdentifier": "AFm/LDfjAw=="
                                }
                            }
                        }
                    }
                ],
                "label": "e"
            }
        ],
        "detectionTime": "2022-02-08T05:02:36Z"
    }
    

#### Alert structure

The following table describes how the **Google Chronicle - Chronicle Alerts Connector** populates the attributes of an alert in Google SecOps.

##### Internally generated attributes

These attributes are derived from the source alert.

**Note:** Some alert attributes aren't populated by this connector because the Chronicle API doesn't provide a corresponding field for this data in the alert responses.Alert Attribute Name | Source  
---|---  
`SourceSystemName` | Internally generated by the framework.  
`TicketId` | The value is taken from the `ids.json` file.  
`DisplayId` | Automatically generated.  
  
##### Attributes for all alert types

These attributes are derived from the source alert.

**Note:** Some alert attributes aren't populated by this connector because the Chronicle API doesn't provide a corresponding field for this data in the alert responses.Alert Attribute Name | Source  
---|---  
`Priority` | Taken from the API response or the `Fallback Severity` parameter.  
`DeviceVendor` | Hardcoded value is `Google Chronicle`.  
`DeviceProduct` | Hardcoded value is `RULE`.  
`Description` | Sourced from `detection/ruleLabels/description` (if it exists).  
`Reason` | Not available.  
`SourceGroupingIdentifier` | Not available.  
`Chronicle Alert - Attachments` | Not available.  
  
### Deprecated: Google Chronicle - Alerts Connector

This connector no longer gets updates or code changes. 

Use the Chronicle Alerts Connector instead.

This connector pulls asset alerts from Google SecOps and converts them into Google SecOps alerts.

You can authenticate using the [Google library](https://google-auth.readthedocs.io/en/latest/) with `google.oauth2.service_account` and `AuthorizedSession`.

This connector requires the Google SecOps [SIEM Search API](https://docs.cloud.google.com/chronicle/docs/reference/search-api).

#### Connector inputs

The **Alerts Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` |  Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Environment Field Name` |  Optional. The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Environment Regex Pattern` |  Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` |  Required. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`Service Account Credentials` |  Required. The content of the service account JSON file.  
`Fetch Max Hours Backwards` |  Optional. The number of hours prior to the initial connector run to retrieve incidents from. This parameter applies only once. The maximum value is `168` (one week). The default value is `1`.  
  
### Deprecated: Google Chronicle - IoCs Connector

This connector is no longer getting updates or code changes. 

Use the Chronicle Alerts Connector instead.

This connector pulls the IOC domain matches from Google SecOps and converts them into Google SecOps alerts.

You can authenticate using the [Google library](https://google-auth.readthedocs.io/en/latest/) with `google.oauth2.service_account` and `AuthorizedSession`.

This connector uses the Google SecOps Search API.

#### Connector inputs

The Google Chronicle - IoCs Connector requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` |  Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Environment Field Name` |  Optional. The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Environment Regex Pattern` |  Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` |  Required. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`Service Account Credentials` |  Required. The content of the service account JSON file.  
`Fetch Max Hours Backwards` |  Optional. The number of hours prior to the initial connector run to retrieve alerts from. This parameter applies only once. The maximum value is `168` (one week). The default value is `1`.  
`Max Alerts To Fetch` |  Optional. The maximum number of alerts to process in every connector iteration. The default value is `100`.  
  
## Jobs

For more information on jobs, see [ Configure a new job](https://docs.cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://docs.cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling).

### Job configuration prerequisites

**Important:** If you update the integration, re-create Google SecOps jobs to update their code.

Before proceeding to the job configuration, configure the Chronicle Alerts Connector.

To configure Google Chronicle jobs, follow these steps:

  1. In Google SecOps SOAR, go to **Response > Job Scheduler**.

  2. Click **add Create New Job**.

  3. In the **Add Job** dialog that appears, select the corresponding Google Chronicle job and click **Save**.

  4. Optional: Edit the job name and description, if necessary.

  5. In the **Job Details** section:

     * Make sure that **GoogleChronicle** is selected in the **Integration** field.
     * To automatically run the job at specified intervals, set up a scheduler interval. Configuring the scheduler is mandatory to complete the job configuration.

As Google Chronicle jobs can synchronize large amounts of data in one run, Google recommends that you minimally set the scheduler interval to 2 minutes.




### Google Chronicle - Sync Data Job

**Important:** To ensure continued functionality before the legacy API deprecation, you must explicitly configure this connector to use the Chronicle API. Verify that the authentication method applied here matches your integration configuration identically.

This job works with alerts created by the Chronicle Alerts Connector and the **Chronicle Alerts Creator** job, but not with alerts from deprecated connectors (**Alerts Connector** and **IOCs Connector**).

The **Google Chronicle Sync Data** job synchronizes updated Google SecOps alerts and cases managed in Google SecOps SOAR back to Google SecOps. Consequently, you can track the same information on both systems immediately after you make changes in Google SecOps SOAR.

#### Case and alerts data synchronization

The **Google Chronicle Sync Data** job tracks and synchronizes the following fields for cases:

Tracked field | Synchronized field  
---|---  
`Priority` | `Priority`  
`Status` | `Status`  
`Title` | `Title`  
Not applicable | `Stage`  
Not applicable | `Google SecOps Case ID`  
Not applicable | `Google SecOps Case ID`  
  
Google SecOps Case ID is a unique case identifier in Google SecOps SOAR and Google SecOps.

The **Google Chronicle Sync Data** job tracks and synchronizes the following fields for alerts:

Tracked field | Synchronized field  
---|---  
`Priority` | `Priority`  
`Status` | `Status`  
`Case ID` | Not applicable  
Not applicable | `Google SecOps Alert ID`  
Not applicable | `Google SecOps Case ID`  
Not applicable | `Verdict`  
Not applicable | `Closure Comment`  
Not applicable | `Closure Reason`  
Not applicable | `Closure Root Cause`  
Not applicable | `Usefulness`  
  
Google SecOps Alert ID is a unique alert identifier in Google SecOps SOAR.

In one iteration, the job synchronizes up to 1,000 cases and 1,000 alerts. The synchronization occurs within the Google SecOps SOAR environment that is specified in the job configuration. The synchronization mechanism ensures that a case from the specified environment cannot be synced with another environment.

#### Configure the Google Chronicle Sync Data job

This job only synchronizes Google SecOps SOAR cases ingested from Google SecOps.

Ensure you've completed the prerequisite steps before you configure this job.

To configure the **Google Chronicle Sync Data** job, follow these steps:

  1. In the **Parameters** section, configure the following parameters:

Parameter | Description  
---|---  
`Environment` | Required.The name of the environment created in Google SecOps SOAR to sync cases and alerts to.  
`API Root` | Required.The API root of the Google SecOps instance. Google SecOps provides regional endpoints for each API. For example, `https://europe-backstory.googleapis.com` or `https://asia-southeast1-backstory.googleapis.com`. If you don't know which endpoint to use, [contact Cloud Customer Care](/chronicle/docs/getting-support). The default value is `https://backstory.googleapis.com`.  
`User's Service Account` | Required.The content of the service account JSON file of your Google SecOps instance.  
`Max Hours Backwards` | Optional.The number of hours to fetch alerts from. Only use positive numbers. The default value is `24`.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Google SecOps server. Enabled by default.  
  
The **Google Chronicle Sync Data** job is enabled by default. When you save the correctly configured job, it starts synchronizing data with Google SecOps immediately. To disable the job, switch the toggle next to the job name.

  2. To complete the configuration, click **Save**.

If the **Save** button is inactive, make sure that you have set all mandatory parameters.

  3. Optional: To run the job immediately after saving, click **Run Now**.

The **Run Now** option lets you trigger a single job run that synchronizes the current Google SecOps SOAR alerts and cases data with Google SecOps.




#### Log messages

The following table lists possible log messages for the **Google Chronicle Data Sync** job:

Log entry | Type | Description  
---|---|---  
`Unable to parse credentials as JSON. Please validate creds.` | Error | The service account provided in the `User's Service Account` parameter is corrupted.  
`"Max Hours Backwards" parameter must be a positive number.` | Error | The `Max Hours backwards` parameter is set to 0 or a negative number.  
`Current platform version doesn't support SDK methods designed for Google SecOps. Please use version 6.1.33 or higher.` | Error | The current Google SecOps platform instance version doesn't support the Chronicle Sync Data job script execution. This means that the instance's build version is older than 6.1.33.  
`Unable to connect to Google SecOps, please validate your credentials: CREDENTIALS` | Error | The service account or API root values couldn't be validated against the Google SecOps instance. This error is reported if the connectivity testing fails.  
`--- Start Processing Updated Cases ---` | Info | The case processing loop has started running.  
`Last success time. Date time:DATE_AND_TIME. Unix:UNIX_EPOCH_TIME ` | Info | The timestamp of the last successful script execution for cases or alerts:

  * `datetime_result` is a date and time value
  * `unix_result` is a Unix epoch time value

  
`Key: "DATABASE_KEY" doesn't exist in the database. Returning default value instead: DEFAULT_VALUE` | Info | The pending case or alert database key doesn't exist in the database. This log entry always appears in the first execution of the script.  
`Failed to parse data as JSON. Returning default value instead: "DEFAULT_VALUE. ERROR: ERROR` | Error | The value retrieved from the database isn't a valid JSON format.  
`Exception was raised from the database. ERROR: ERROR.` | Error | There is a connection problem with the database.  
`Successfully loaded CASE_IDS pending IDs. ` `Successfully loaded ALERT_IDS pending alert IDs.` | Info | The pending cases or alerts IDs have been successfully retrieved from the backlog. CASE_IDS is the number of case IDs brought.  
`Cases overload: case limit is 1000 NUMBER_OF_CASES cases will not be synced.` `Alerts overload: alert limit is 1000 NUMBER_OF_ALERTS alerts will not be synced.` | Error | The number of pending cases or alerts IDs that are fetched from the database is greater than the limit (1000). Any IDs over the limit are ignored. This error can indicate a possible database corruption.  
`Found NUMBER_OF_UPDATED_CASES updated cases since last fetch time.` | Info | The newly updated case or alert IDs were successfully fetched from the platform.  
`--- Start Updating Cases in Google SecOps ---- ` `-- Start Processing Updated Alerts ---` | Info | The update of cases and alerts in the Google SecOps instance has started.  
`Failed to update case CASE_ID. Reason: ERROR_REASON` `Failed to update alert ALERT_ID. Reason: ERROR_REASON` | Error | The specified case or alert cannot be synchronized with Google SecOps.  
`Max retries reached for case CASE_ID. Removing from backlog.` `Max retries reached for alert ALERT_GROUP_ID . Removing from backlog.` | Info | The specified pending case or alert has reached the sync retry limit (5) and isn't inserted back to the backlog.  
`The following cases were not synced: CASE_IDS` `The following alerts were not synced: ALERT_IDS` | Info | The list of case or alert IDs that cannot be synchronized with Google SecOps.  
`Updated External Case IDs for the following cases: CASE_IDS` | Info | The list of cases for which the job updated the matching Google SecOps external case ID in the Google SecOps SOAR platform.  
`Failed to update external ids.` | Error | The log entry indicating that there was a problem with the SDK method or connection that prevented updating external case IDs in the platform.  
`Failed to update cases in Google SecOps.` `Failed to update alerts in Google SecOps.` | Error | The log entry indicating that there was a certain terminating error that prevented the case or alerts processing loop to finish naturally. The stacktrace is printed after this log with the specific error.  
`--- Finished Updating Cases in Google SecOps --- ` `--- Finished Updating Alerts in Google SecOps ---` | Info | The cases and alerts processing loop has finished, either naturally or with an error.  
`The following failed case ids were put in the backlog: CASE_IDS` `The following failed alert ids were put in the backlog: ALERT_IDS` | Error | The list of failed case or alert IDs that have a retry count less than or equal to 5 to be written back to the backlog.  
`--- Finished Processing Updated Cases ---` `--- Finished Processing Updated Alerts ---` | Info | The stage of processing case and alert has been finished.  
`Saving timestamps.` | Info | Saving the last successful case and alert update timestamps to the database.   
`Saving pending ids.` | Info | Saving pending case and alert IDs to the database.  
`Got exception on main handler. Error: ERROR_REASON` | Error | A general termination error has occurred. The stacktrace is printed after this log with the specific error.  
  
### Google Chronicle Alerts Creator job

**Important:** To ensure continued functionality before the legacy API deprecation, you must explicitly configure this connector to use the Chronicle API. Verify that the authentication method applied here matches your integration configuration identically.

The **Google Chronicle Alerts Creator** job requires the Google SecOps platform version 6.2.30 or later.

This job creates all alerts from Google SecOps SOAR to Google SecOps, including overflow alerts. The **Google Chronicle Alerts Creator** job doesn't replicate alerts that originate from Google SecOps.

The **Google Chronicle Alerts Creator** job queries the SOAR platform using the Python SDK for non-synchronized alerts. The job sends non-synchronized alerts to SIEM individually. SIEM updates and returns the identifiers of the corresponding SIEM alerts, and SOAR saves the identifiers using the SOAR platform API through the Python SDK.

#### Relationship between the Google Chronicle jobs

A complete Google SecOps system runs the following three components concurrently:

  1. **Chronicle Alerts Connector**
  2. **Google Chronicle Sync Data** job
  3. **Google Chronicle Alerts Creator** job



The **Google Chronicle Sync Data** job creates and synchronizes cases. It also synchronizes the case and alert modifications, such as priority changes.

The **Google Chronicle Alerts Creator** job generates all alerts, except SIEM alerts. The **Google Chronicle Sync Data** job sends updates on unsynchronized alerts after the **Google Chronicle Alerts Creator** job creates the alerts.

#### Case and alerts data synchronization

Cases are synchronized in the same manner as with the Google Chronicle Sync Data job.

In Google SecOps, each alert is identified with a SIEM alert identifier. SOAR alerts can adopt a SIEM identifier in two scenarios:

  1. Alert is generated in SIEM.

This alert already exists in Google SecOps and there is no need to duplicate it. The connector populates the `siem_alert_id` field.

  2. Alert is generated in third-party connectors.

This alert doesn't exist in Google SecOps and requires running an explicit synchronization operation that the **Google Chronicle Alerts Creator** job is responsible for. Upon completing the synchronization operation, the alert acquires a new SIEM identifier.




#### Configure the Google Chronicle Alerts Creator job

Make sure you have completed the prerequisite steps before configuring the job.

To configure the **Google Chronicle Alerts Creator** job, follow these steps:

  1. Configure the job parameters from the following table:

Parameter | Description  
---|---  
`Environment` | Required.The name of the environment created in Google SecOps SOAR where you want to sync cases and alerts.  
`API Root` | Required.The API root of the Google SecOps instance. Google SecOps provides regional endpoints for each API. For example, `https://europe-backstory.googleapis.com` or `https://asia-southeast1-backstory.googleapis.com`. If you don't know which endpoint to use, [contact Cloud Customer Care](/chronicle/docs/getting-support). The default value is `https://backstory.googleapis.com`.  
`User's Service Account` | Required.The content of the service account JSON file of your Google SecOps instance.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Google SecOps server. Enabled by default.  
  2. To complete the configuration, click **Save**.

If the **Save** button is inactive, make sure that you have set all mandatory parameters.

  3. Optional: To run the job immediately after saving, click **Run Now**.

The **Run Now** option lets you trigger a single job run that synchronizes the current Google SecOps SOAR alerts and cases data with Google SecOps.




#### Log messages and error handling

Log | Level | Description  
---|---|---  
` Unable to parse credentials as JSON. Please validate creds. ` | ERROR | The service account provided in the User's Service Account parameter is corrupted.  
` Current platform version doesn't support SDK methods designed for Google Chronicle. Please use version 6.2.30 or later. ` | ERROR | The current Google SecOps platform instance version doesn't support the Google Chronicle Alerts Creator Job script execution. This error means that the instance build version is earlier than 6.2.30.  
` Unable to connect to Google Chronicle, please validate your credentials: CREDENTIALS ` | ERROR | The service account or API root values cannot be validated against the Google SecOps instance. This error is reported if the connectivity testing fails.  
` --------------- JOB STARTED --------------- ` | INFO | Log message indicating that the job has started.  
` ----------------- Main - Started ----------------- ` | INFO | Log message indicating that the main function has started.  
` "Starting i + 1/MAXIMUM_ITERATIONS_NUMBER fetch attempt" ` | INFO | Log message indicating the iteration number for the current consecutive attempt.  
` "Fetching up to BATCH_SIZE new alerts from the SOAR" ` | INFO | Log message indicating that the code doesn't retrieve more than BATCH_SIZE new alerts from SOAR.  
` "NUMBER_OF_NEW_ALERTS SOAR alerts were fetched" ` | INFO | Log message indicating that NUMBER_OF_NEW_ALERTS SOAR alerts were fetched.  
` "No new SOAR alerts were found. Stopping..." ` | INFO | Log message indicating that no new SOAR alerts were found, and that the job is stopping.  
` "Fetched the following SOAR alerts: ID_LIST" ` | INFO | Log message indicating that the job has fetched the SOAR alerts with the following identifiers in the ID list. You can use this information to track the progress of the job and to troubleshoot issues with the code.   
` "Dispatching SOAR alerts to SIEM" ` | INFO | Log message indicating that the job is dispatching SOAR alerts to SIEM.  
` "Failed to create alert ALERT_GROUP_ID in SIEM. Reason: ERROR_REASON" ` | ERROR | Log message indicating that the alert was not created successfully in SIEM due to an error.  
` "Updating SOAR with SIEM response" ` | INFO | Log message indicating that the job is updating SOAR with the SIEM response.   
` "SOAR has failed updating the status of alert ALERT_ID" ` | WARNING | Indicates that SOAR was unable to update the status of the alert synchronization.  
` "Total of NUMBER_OF_SYNCED_ALERTS alerts were synced in this run"` | INFO | Log message indicating that a total of `total_synced` alerts were synced in the current run.  
` "--------------- JOB FINISHED ---------------" ` | INFO | Log message indicating that the job has finished.  
` "Got exception on main handler. Error: ERROR_REASON" ` | ERROR | Log message indicating that an exception occurred in the main function. The exception message is included in the log message.  
  
## Use cases

The **Google Chronicle** integration lets you run the following use cases:

  * **Chronicle Windows Threats Investigation and Response**
  * **Security Command Center and Chronicle Cloud DIR**



### Install the use case

  1. In the Google SecOps Content Hub, go to the **Use Cases** tab.

  2. In a search field, enter the use case name.

  3. Click the use case.

  4. Follow the configuration steps and instructions in the installation wizard.




Once finished, all of the required components are installed on your Google SecOps machine. To finalize the installation, configure the **Initialization** block in the playbook that corresponds to your use case.

### Chronicle Windows Threats Investigation & Response

Use the power of Google SecOps to respond in real time to Windows threats in your environment. Using Threat Intelligence for Google SecOps, security teams can take advantage of a high-fidelity threat intelligence service together with Google SecOps. Real threats in your environment can now be automatically triaged and remediated in a short and effective time period.

  1. In Google SecOps, go to **Response > Playbooks**.

  2. Select the **Google Chronicle - Windows Threats Investigation & Response** playbook. The playbook opens in the playbook designer view.

  3. Double-click **Set Initialization Block_1**. The block configuration dialog opens.

  4. To configure the playbook, use the following parameters:

Input parameter | Possible values | Description  
---|---|---  
`edr_product` | 
     * Crowdstrike
     * Carbon Black
     * None
| The EDR product to use in the playbook.  
`itsm_product` | 
     * Service Now
     * Jira
     * ZenDesk
     * None
| The ITSM product to use in the playbook. Jira requires additional configuration in the Open Ticket block.  
`crowdstrike_use_spotlight` | `true` or `false` | If `True`, the playbook executes Crowdstrike actions that require a Spotlight license (Vulnerability information).  
`use_mandiant` | `true` or `false` | If `True`, the playbook executes the Mandiant block.   
`slack_user` | Username or Email Address | The username or email address of the Slack user. If none is provided, the playbook skips Slack blocks.  
  5. Click **Save**. The block configuration dialog closes.

  6. In the playbook designer pane, click **Save**.




To test the playbook in the use case, ingest the test case included in the package. Some test case capabilities can fail because the data used for testing are unavailable in your environment.

### Security Command Center and Chronicle Cloud DIR

Integrate Security Command Center with Google SecOps to let your analysts investigate incidents and threats that Security Command Center detects.

#### Configure the use case

The use case requires you to configure the following integrations:

  * [Siemplify](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify)
  * Tools
  * [Mitre ATT&CK](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mitre-att-and-ck)
  * [Google Cloud IAM](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-iam)
  * [Google Chronicle](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chronicle)
  * Functions
  * [Google Cloud Compute](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-compute)
  * [Email V2](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/email-v2)
  * [VirusTotal v3](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/virustotal-v3)



The [Google Security Command Center](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-security-command-center) and [Mandiant](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant) integrations are optional.

Make sure that you have installed the use case before configuring it.

  1. In Google SecOps, go to the **Playbooks** tab.
  2. Select the **SCC & Chronicle Cloud DIR** playbook.
  3. Double-click the **Initialization block** to configure it.
  4. Configure the playbook using the following parameters:

Parameter name | Possible values | Description  
---|---|---  
`Mandiant_Enrichment` | `true` or `false` | If `True`, the playbook uses Mandiant for additional enrichment.The Mandiant integration needs to be configured for this setup. You can remove the enrichment if you rarely get meaningful information. Removing the enrichment block improves the execution speed of the playbook.  
`SCC_Enrichment` | `true` or `false` | If `True`, the playbook uses Security Command Center capabilities for additional enrichment.The Security Command Center integration must be configured for this setup. You can remove the enrichment if you rarely get meaningful information. Removing the enrichment block improves the execution speed of the playbook.  
`IAM_Enrichment` | `true` or `false` | If `True`, the playbook uses the IAM capabilities for additional enrichment. You can remove the enrichment if you rarely get meaningful information. Removing the enrichment block improves the execution speed of the playbook.  
`Compute_Enrichment` | `true` or `false` | If `True`, the playbook uses Compute Engine capabilities for additional enrichment. You can remove the enrichment if you rarely get meaningful information. Removing the enrichment block improves the execution speed of the playbook.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
