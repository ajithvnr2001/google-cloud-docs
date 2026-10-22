---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/proofpoint-threat-protection/
title: Integrate Proofpoint Threat Protection with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:48.945066+00:00
---

# Integrate Proofpoint Threat Protection with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/proofpoint-threat-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Proofpoint Threat Protection with Google SecOps 

This document explains how to integrate Proofpoint Threat Protection with Google Security Operations.

## Use cases

In the Google SecOps platform, the **Proofpoint Threat Protection** integration supports the following use cases:

  * **Automated phishing mitigation** : Automatically add malicious sender email addresses and domains to the Proofpoint block list after a phishing alert is verified to prevent further delivery of similar threats across the organization.

  * **Accelerated incident response** : Rapidly update block list entries for IP addresses and hostnames during an active investigation to ensure that newly discovered indicators of compromise (IOCs) are immediately neutralized at the email gateway.

  * **Proactive threat protection** : Proactively query and retrieve existing allow and block list entries to ensure security policies remain up to date and consistent with current threat intelligence, reducing the organization's attack surface.

  * **Simplified policy management** : Streamline the administration of email security policies by using playbooks to manage bulk additions or removals of trusted senders to the allow list based on approved business requests.




## Before you begin

Before you configure the integration in the Google SecOps platform, verify that you have the following:

  * **Proofpoint Threat Protection API credentials** : Ensure you have a valid client ID and client secret. These are generated within the [Proofpoint administrative console](https://threatinsight.proofpoint.com/)

  * **Cluster ID** : Identify the specific cluster ID associated with your Proofpoint instance. This ID is required to target the correct allow and block lists.

  * **Network connectivity** : Verify that the Google SecOps environment can communicate with the Proofpoint Threat Protection API root endpoint. If you're using a proxy, ensure the credentials and addresses are available.




## Integration parameters

The **Proofpoint Threat Protection** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required. The base URL of the Proofpoint Threat Protection instance.  
`Client ID` | Required. The client ID associated with your Proofpoint Threat Protection API credentials.  
`Client Secret` | Required. The client secret associated with your Proofpoint Threat Protection API credentials.  
`Cluster ID` | Required. The cluster ID associated with your Proofpoint Threat Protection API instance.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the Proofpoint Threat Protection server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Entry to Allow List

Use the **Add Entry to Allow List** action to add an entry to the Proofpoint Threat Protection allow list.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Entry to Allow List** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster ID` | Optional. The cluster ID of the allow list. If no value is provided, the action uses the cluster ID from the integration configuration.  
`Allowlist Item` | Required. The JSON object representing the allow list item to add. The default value is:
    
    
    {
        "action": "add",
        "attribute": "",
        "operator": "",
        "value": "",
        "comment": ""
    }
      
  
#### Action outputs

The **Add Entry to Allow List** action provides the following outputs:

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

The **Add Entry to Allow List** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added a new entry to the allow list.` | The action succeeded.  
`Error ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Entry to Allow List** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
### Add Entry to Block List

Use the **Add Entry to Block List** action to add an entry to the Proofpoint Threat Protection block list.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Entry to Block List** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster ID` | Optional. The cluster ID of the block list. If no value is provided, the action uses the cluster ID from the integration configuration.  
`Blocklist Item` | Required. The JSON object representing the block list item to add. The default value is:
    
    
    {
        "action": "add",
        "attribute": "",
        "operator": "",
        "value": "",
        "comment": ""
    }
      
  
#### Action outputs

The **Add Entry to Block List** action provides the following outputs:

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

The **Add Entry to Block List** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added new entry to the block list.` | The action succeeded.  
`Error ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Entry to Block List** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
### Add IOC to Allow List

Use the **Add IOC to Allow List** action to add specific IOCs to the Proofpoint Threat Protection allow list.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add IOC to Allow List** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster ID` | Optional. The cluster ID of the allow list. If no value is provided, the action uses the cluster ID from the integration configuration.  
`Recipient Email Address` | Optional. A comma-separated list of recipient email addresses to add to the allow list.  
`Sender Email Address` | Optional. A comma-separated list of sender email addresses to add to the allow list.  
`Sender IP Address` | Optional. A comma-separated list of sender IP addresses to add to the allow list.  
`Sender Hostname` | Optional. A comma-separated list of sender hostnames to add to the allow list.  
`Sender HELO Domain Name` | Optional. A comma-separated list of HELO domain names to add to the allow list.  
`Message Header From (Address Only)` | Optional. A comma-separated list of "Message Header From" entries to add to the allow list.  
`Comment` | Optional. A description or justification associated with the allow list entries.  
  
#### Action outputs

The **Add IOC to Allow List** action provides the following outputs:

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

The **Add IOC to Allow List** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added new entries to the allow list.` | The action succeeded.  
`Error ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add IOC to Allow List** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
### Add IOC to Block List

Use the **Add IOC to Block List** action to add specific IOCs to the Proofpoint Threat Protection block list.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add IOC to Block List** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster ID` | Optional. The cluster ID of the block list. If no value is provided, the action uses the cluster ID from the integration configuration.  
`Recipient Email Address` | Optional. A comma-separated list of recipient email addresses to add to the block list.  
`Sender Email Address` | Optional. A comma-separated list of sender email addresses to add to the block list.  
`Sender IP Address` | Optional. A comma-separated list of sender IP addresses to add to the block list.  
`Sender Hostname` | Optional. A comma-separated list of sender hostnames to add to the block list.  
`Sender HELO Domain Name` | Optional. A comma-separated list of HELO domain names to add to the block list.  
`Message Header From (Address Only)` | Optional. A comma-separated list of "Message Header From" entries to add to the block list.  
`Comment` | Optional. A description or justification associated with the block list entries.  
  
#### Action outputs

The **Add IOC to Block List** action provides the following outputs:

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

The **Add IOC to Block List** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added new entries to the block list.` | The action succeeded.  
`Error ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add IOC to Block List** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
### Get Allow List Entries

Use the **Get Allow List Entries** action to retrieve existing entries from the Proofpoint Threat Protection allow list.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Allow List Entries** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster ID` | Required. The cluster ID of the allow list. If no value is provided, the action uses the cluster ID from the integration configuration.  
`IOC Type To Return` | Optional. The types of IOCs to return. If `All` is selected, the action returns all entries. The possible values are as follows:

  * `All`
  * `Recipient Email Address`
  * `Sender Email Address`
  * `Sender IP Address`
  * `Sender Hostname`
  * `Sender HELO Domain Name`
  * `Message Header From (Address Only)`

The default value is `All`.  
`Max IOCs To Return` | Optional. The number of IOCs to return. The maximum value is `1000`. The default value is `100`.  
  
#### Action outputs

The **Get Allow List Entries** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Allow List Entries** action:
    
    
    [
           {
               "attribute": "$from",
               "operator": "equal",
               "value": "test@example.com",
               "comment": ""
           }
    ]
    

##### Output messages

The **Get Allow List Entries** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully listed entries in the allow list based on the provided criteria.` | The action succeeded.  
`Error ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Allow List Entries** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
### Get Block List Entries

Use the **Get Block List Entries** action to retrieve existing entries from the Proofpoint Threat Protection block list.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Block List Entries** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster ID` | Required. The cluster ID of the block list. If no value is provided, the action uses the cluster ID from the integration configuration.  
`IOC Type To Return` | Optional. The types of IOCs to return. If `All` is selected, the action returns all entries. The possible values are as follows:

  * `All`
  * `Recipient Email Address`
  * `Sender Email Address`
  * `Sender IP Address`
  * `Sender Hostname`
  * `Sender HELO Domain Name`
  * `Message Header From (Address Only)`

The default value is `All`.  
`Max IOCs To Return` | Optional. The number of IOCs to return. The maximum value is `1000`. The default value is `100`.  
  
#### Action outputs

The **Get Block List Entries** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Block List Entries** action:
    
    
    [
           {
               "attribute": "$from",
               "operator": "equal",
               "value": "test@example.com",
               "comment": ""
           }
    ]
    

##### Output messages

The **Get Block List Entries** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully listed entries in the block list based on the provided criteria.` | The action succeeded.  
`Error ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Block List Entries** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to Proofpoint Threat Protection.

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

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Proofpoint Threat Protection server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Proofpoint Threat Protection server! Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
### Remove Entry from Allow List

Use the **Remove Entry from Allow List** action to remove an entry from the Proofpoint Threat Protection allow list.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Remove Entry from Allow List** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster ID` | Required. The cluster ID of the allow list. If no value is provided, the action uses the cluster ID from the integration configuration.  
`IOC Type To Search` | Optional. The types of IOCs to search for. If `All` is selected, the action removes all entries matching the value. The possible values are as follows:

  * `All`
  * `Recipient Email Address`
  * `Sender Email Address`
  * `Sender IP Address`
  * `Sender Hostname`
  * `Sender HELO Domain Name`
  * `Message Header From (Address Only)`

The default value is `All`.  
`Value` | Optional. The value to remove from the allow list.  
`Case Insensitive Search` | Required. If selected, the action performs a case-insensitive search to identify and remove all matching entries.  
  
#### Action outputs

The **Remove Entry from Allow List** action provides the following outputs:

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

The **Remove Entry from Allow List** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully deleted entry in the allow list based on the provided criteria.` | The action succeeded.  
`Error ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove Entry from Allow List** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
### Remove Entry from Block List

Use the **Remove Entry from Block List** action to remove an entry from the Proofpoint Threat Protection block list.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Remove Entry from Block List** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster ID` | Required. The cluster ID of the block list. If no value is provided, the action uses the cluster ID from the integration configuration.  
`IOC Type To Search` | Optional. The types of IOCs to search for. If `All` is selected, the action removes all entries matching the value. The possible values are as follows:

  * `All`
  * `Recipient Email Address`
  * `Sender Email Address`
  * `Sender IP Address`
  * `Sender Hostname`
  * `Sender HELO Domain Name`
  * `Message Header From (Address Only)`

The default value is `All`.  
`Value` | Optional. The value to remove from the block list.  
`Case Insensitive Search` | Required. If selected, the action performs a case-insensitive search to identify and remove all matching entries.  
  
#### Action outputs

The **Remove Entry from Block List** action provides the following outputs:

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

The **Remove Entry from Block List** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully deleted entry in the block list based on the provided criteria.` | The action succeeded.  
`Error ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove Entry from Block List** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
